
import logging
import re
import sys
import requests


# ------------------------------------------------------------------------------- #
# Here comes gujal ;)
# ------------------------------------------------------------------------------- #
def solve_cf_challenge(body, netloc):
  
    domain = netloc
   

    try:

        form_index = body.find('id="challenge-form"')
        if form_index == -1:
            raise Exception('CF form not found')
        sub_body = body[form_index:]

        if body.find('id="cf-dn-', form_index) != -1:
            extra_div_expression = re.search('id="cf-dn-.*?>(.+?)<', sub_body).group(1)

        # Initial value.
        js_answer = cf_parse_expression(
            re.search('setTimeout\(function\(.*?:(.*?)}', body, re.DOTALL).group(1)
        )
        # Extract the arithmetic operations.
        builder = re.search("challenge-form'\);\s*;(.*);a.value", body, re.DOTALL).group(1)
        # Remove a function semicolon before splitting on semicolons, else it messes the order.
        lines = builder.replace(' return +(p)}();', '', 1).split(';')

        for line in lines:
            if len(line) and '=' in line:
                heading, expression = line.split('=', 1)
                if 'eval(eval(' in expression:
                    # Uses the expression in an external <div>.
                    expression_value = cf_parse_expression(extra_div_expression)
                elif 'function(p' in expression:
                    # Expression + domain sampling function.
                    expression_value = cf_parse_expression(expression, domain)
                else:
                    expression_value = cf_parse_expression(expression)
                js_answer = cf_arithmetic_op(heading[-1], js_answer, expression_value)

        if '+ t.length' in body:
            js_answer += len(domain) # Only older variants add the domain length.


        return '%.10f' % js_answer

    except Exception as e:
        
        logging.error("[!] %s ." % e)
        raise
# ------------------------------------------------------------------------------- #

def cf_sample_domain_function(func_expression, domain):
    parameter_start_index = func_expression.find('}(') + 2
    # Send the expression with the "+" char and enclosing parenthesis included, as they are
    # stripped inside ".cf_parse_expression()'.
    sample_index = cf_parse_expression(
        func_expression[parameter_start_index : func_expression.rfind(')))')]
    )
    return ord(domain[int(sample_index)])
# ------------------------------------------------------------------------------- #

def cf_arithmetic_op(op, a, b):
    if op == '+':
        return a + b
    elif op == '/':
        return a / float(b)
    elif op == '*':
        return a * float(b)
    elif op == '-':
        return a - b
    else:
        raise Exception('Unknown operation')
# ------------------------------------------------------------------------------- #

def cf_parse_expression(expression, domain=None):

    def _get_jsfuck_number(section):
        digit_expressions = section.replace('!+[]', '1').replace('+!![]', '1').replace('+[]', '0').split('+')
        return int(
            # Form a number string, with each digit as the sum of the values inside each parenthesis block.
            ''.join(
                str(sum(int(digit_char) for digit_char in digit_expression[1:-1])) # Strip the parenthesis.
                for digit_expression in digit_expressions
            )
        )

    if '/' in expression:
        dividend, divisor = expression.split('/')
        dividend = dividend[2:-1] # Strip the leading '+' char and the enclosing parenthesis.

        if domain:
            # 2019-04-02: At this moment, this extra domain sampling function always appears on the
            # divisor side, at the end.
            divisor_a, divisor_b = divisor.split('))+(')
            divisor_a = _get_jsfuck_number(divisor_a[5:]) # Left-strip the sequence of "(+(+(".
            divisor_b = cf_sample_domain_function(divisor_b, domain)
            return _get_jsfuck_number(dividend) / float(divisor_a + divisor_b)
        else:
            divisor = divisor[2:-1]
            return _get_jsfuck_number(dividend) / float(_get_jsfuck_number(divisor))
    else:
        return _get_jsfuck_number(expression[2:-1])

# ------------------------------------------------------------------------------- #