import requests,re,xbmc,xbmcgui,xbmcaddon
dialog = xbmcgui.Dialog()
RDenabled = (xbmcaddon.Addon('script.module.resolveurl').getSetting('RealDebridResolver_enabled'))
PMenabled = (xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_enabled'))

Return = []
Hashes = []
Cached = []
def CheckDebrid(data):
	for name,link in data:
		if 'magnet' not in link: Return.append({'title': name, 'url': link})
		else:
			GetHashes = re.findall(r'''btih:(.*?)&''',link)
			Hashes.append(GetHashes)
	if PMenabled == 'true': CheckPremiumize(data)
	
def CheckPremiumize(items):
	cachedtrue = 0
	PremToken = (xbmcaddon.Addon('script.module.resolveurl').getSetting('PremiumizeMeResolver_token'))
	ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
	  "Authorization" : "Bearer %s" % PremToken}
	Baseurl = 'https://www.premiumize.me/api/cache/check'
	data = {'items[]': Hashes}
	link = requests.post(Baseurl,data=data,headers=ua).json()
	for index, value in enumerate(link.get("response", [False])):
		if value: Cached.append(list(Hashes)[index])
	for name,link in items:
		for cleared in Cached:
			if cleared[0] in link: Return.append({'title': name, 'url': link})
			else: continue
	return Return
