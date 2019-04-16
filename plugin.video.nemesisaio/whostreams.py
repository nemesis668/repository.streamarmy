import jsunpack
import requests
import re



def resolve(link):

	domain = 'whostreams.net'
	packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
	clappr = re.compile('new\s+Clappr\.Player\(\{\s*?source:\s*?["\'](.+?)["\']')
	source = re.compile('sources\s*:\s*\[\s*\{\s*(?:type\s*:\s*[\'\"].+?[\'\"],|)src\s*:\s*[\'\"](.+?)[\'\"]')
	ua = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0', 'Referer' : link }
	uStr = 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'

	if not 'http' in link: link = 'https:' + link
	page = requests.get(link, headers=ua).text
	packed = packer.findall(page)[0]
	unpacked = jsunpack.unpack(packed)
	try:
		stream = clappr.findall(unpacked)[0]
	except:
		try:
			stream = source.findall(unpacked)[0]
		except IndexError:
			stream = 'NONE'
	if not 'NONE' in stream:
		stream += '|User-Agent={ua}&Referer={ref}'.format(ua=uStr, ref=link)
		return stream