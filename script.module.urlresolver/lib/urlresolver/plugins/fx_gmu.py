"""
flashx.tv urlresolver plugin
Copyright (C) 2015 tknorris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import re
import urlparse
import urllib
from lib import helpers
from urlresolver import common
from urlresolver.resolver import ResolverError

SORT_KEY = {'High': 3, 'Middle': 2, 'Low': 1}
net = common.Net()

def get_media_url(url):
    try:
        hostname = urlparse.urlparse(url).hostname
        headers = {'User-Agent': common.FF_USER_AGENT}
        html = net.http_GET(url, headers=headers).content
        headers.update({'Referer': url})
        for match in re.finditer('''<script[^>]*src=["']([^'"]+)''', html):
            _html = get_js(match.group(1), headers, hostname)
                
        match = re.search('''href=['"]([^'"]+)''', html)
        if match:
            playvid_url = match.group(1)
            html = net.http_GET(playvid_url, headers=headers).content
            headers.update({'Referer': playvid_url})
            for match in re.finditer('''<script[^>]*src=["']([^'"]+)''', html):
                js = get_js(match.group(1), headers, hostname)
                match = re.search('''!=\s*null.*?get\(['"]([^'"]+).*?\{([^:]+)''', js, re.DOTALL)
                if match:
                    fx_url, fx_param = match.groups()
                    fx_url = resolve_url(urlparse.urljoin('http://www.flashx.tv', fx_url) + '?' + urllib.urlencode({fx_param: 1}))
                    common.log_utils.log('fxurl: %s' % (fx_url))
                    _html = net.http_GET(fx_url, headers=headers).content
                    
            headers.update({'Referer': url})
            html = net.http_GET(playvid_url, headers=headers).content
            html = helpers.add_packed_data(html)
        
        common.log_utils.log(html)
        sources = helpers.parse_sources_list(html)
        try: sources.sort(key=lambda x: SORT_KEY.get(x[0], 0), reverse=True)
        except: pass
        source = helpers.pick_source(sources)
        return source + helpers.append_headers(headers)
        
    except Exception as e:
        common.log_utils.log_debug('Exception during flashx resolve parse: %s' % e)
        raise
    
    raise ResolverError('Unable to resolve flashx link. Filelink not found.')

def get_js(js_url, headers, hostname):
    js = ''
    if not js_url.startswith('http'):
        base_url = 'http://' + hostname
        js_url = urlparse.urljoin(base_url, js_url)
    
    if hostname in js_url:
        common.log_utils.log('Getting JS: |%s| - |%s|' % (js_url, headers))
        js = net.http_GET(js_url, headers=headers).content
    return js
    
def resolve_url(url):
    parts = list(urlparse.urlsplit(url))
    segments = parts[2].split('/')
    segments = [segment + '/' for segment in segments[:-1]] + [segments[-1]]
    resolved = []
    for segment in segments:
        if segment in ('../', '..'):
            if resolved[1:]:
                resolved.pop()
        elif segment not in ('./', '.'):
            resolved.append(segment)
    parts[2] = ''.join(resolved)
    return urlparse.urlunsplit(parts)
