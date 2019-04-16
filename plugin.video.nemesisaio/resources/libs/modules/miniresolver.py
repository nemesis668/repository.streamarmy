import xbmc,xbmcaddon,xbmcgui,xbmcplugin,base64,cfscrape
import requests
import re
import resolveurl
import sys,os
dialog = xbmcgui.Dialog()
AddonTitle = '[COLOR yellow][B]Nemesis[/B][/COLOR]'
addon_id   = 'plugin.video.nemesis'
Addonicon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.gif'))
scraper = cfscrape.create_scraper()
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.gif'))
ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')
	  
def Checker(url):
	if 'rarbg' in url: RarBG(url)
	elif 'filepursuit' in url: FilePursuit(url)
	elif 'putlocker' in url: PutLocker(url)
	elif 'limetorrent' in url: LimeTorrent(url)
	elif 'watchepisodeseries' in url: WatchSeries(url)
	else: return url

def RarBG(url):
	link = requests.get(url, headers={"User-Agent":ua}).content
	play = re.findall('''href=['"](magnet:\?xt=urn:.*?)=''',link,flags=re.DOTALL)[0]
	if play:
		Player(play)
	else: dialog.notification(AddonTitle,"[B][COLOR yellow]No Playable Link Found[/B][/COLOR]",icon,5000)
def FilePursuit(url):
	playable = requests.get(url, headers={"User-Agent":ua}).content
	play = re.findall('id="visible-input">(.*?)</code>',playable,flags=re.DOTALL)[0].strip()
	if play:
		Player(play)
	else: dialog.notification(AddonTitle,"[B][COLOR yellow]No Playable Link Found[/B][/COLOR]",icon,5000)
	
def LimeTorrent(url):
	playable = scraper.get(url, headers={"User-Agent":ua}).content
	play = re.findall('''href=['"](magnet:\?xt=urn:.*?)=''',playable,flags=re.DOTALL)[0]
	if play:
		Player(play)
	else: dialog.notification(AddonTitle,"[B][COLOR yellow]No Playable Link Found[/B][/COLOR]",icon,5000)
	
def WatchSeries(url):
	dialog.notification(AddonTitle, '[COLOR yellow]Be Patient The Link Takes 10 secs to Resolve[/COLOR]', Addonicon, 8000)
	playable = scraper.get(url, headers={"User-Agent":ua}).content
	play = re.findall('''<div class="wb-main">.*?href=['"](.*?)['"]''',playable,flags=re.DOTALL)[0]
	if play:
		Player(play)
	else: dialog.notification(AddonTitle,"[B][COLOR yellow]No Playable Link Found[/B][/COLOR]",icon,5000)

def PutLocker(url):
	playable = requests.get(url, headers={"User-Agent":ua}).content
	getbase64 = re.findall('document.write\(Base64.decode\("(.+?)"\)', playable)[0]
	decrypt = base64.b64decode(getbase64)
	play = re.findall('src="(.*?)"',decrypt)[0]
	if play:
		Player(play)
	else: dialog.notification(AddonTitle,"[B][COLOR yellow]No Playable Link Found[/B][/COLOR]",icon,5000)

def Player(link):
	hmf = resolveurl.HostedMediaFile(link)
	if hmf.valid_url(): link = hmf.resolve()
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, xbmcgui.ListItem(path=link))
	quit()