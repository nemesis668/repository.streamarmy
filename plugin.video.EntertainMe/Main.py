#############################################################
#################### START ADDON IMPORTS ####################
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import os
import re
import requests
import sys
import base64
import json
import time
import datetime
import display
import viewer
import pyxbmct.addonwindow as pyxbmct
from addon.common.addon import Addon
import StorageServer
# reload(sys)
# sys.setdefaultencoding("utf-8")

dialog = xbmcgui.Dialog()
cache               = StorageServer.StorageServer("entertainme", 0.2)

#############################################################
#################### SET ADDON ID ###########################
_addon_id_ = 'plugin.video.EntertainMe'
_self_ = xbmcaddon.Addon(id=_addon_id_)
Date = time.strftime("%A %B %d")
AddonTitle = '[B][COLOR red]E[COLOR yellow]ntertain Me[/B][/COLOR]'
dp = xbmcgui.DialogProgress()
icon  = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_, 'icon.png'))


#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bg.jpg'))
TText	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingtxt.png'))
AddonIcon = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_, 'icon.png'))
SText	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'searchtxt.png'))
BannerA	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'banner.png'))
ButtonTrending1S = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingS.png'))
ButtonTrending1 = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trending.png'))
ButtonMovies = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Movies_Button.png'))
ButtonMoviesS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Movies_ButtonS.png'))
ButtonTvShows = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Shows_Button.png'))
ButtonTvShowsS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Shows_ButtonS.png'))
ButtonRelease = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Upcoming_Button.png'))
ButtonReleaseS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Upcoming_ButtonS.png'))
ButtonSearch = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_search.png'))
ButtonSearchS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_searchS.png'))
ButtonQuit = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Quit_Button.png'))
ButtonQuitS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Quit_ButtonS.png'))




#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():

	window = Main('EntertainMe')
	window.doModal()
	del window
def GetTokens():
	try:
		dp.create (AddonTitle,("[COLOR yellow]EntertainMe[/COLOR]"))
		dp.update(0)
		time.sleep(1)
		from cloudscraper2 import CloudScraper
		dp.update (50,("[COLOR pink]Grabbing Cloudflare Token[/COLOR]"))
		scraper = CloudScraper.create_scraper()
		ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
		scraper.headers.update({'User-Agent': ua})
		cookies = scraper.get('http://www.seehd.pl/wp-content/themes/kickass-mediaspace/favicon.png').cookies.get_dict()
		dp.update (100,("[COLOR pink]Secuirty Bypassed, Addon Opening[/COLOR]"))
		time.sleep(1)
		dp.close()
		return (cookies, ua)
	except:
		dialog.ok(AddonTitle,"[COLOR yellow]Failed To Grab Cloudflare Token, Try Again[/COLOR]")
		quit()

url = 'http://www.seehd.pl/'
cookies, ua = cache.cacheFunction(GetTokens)
headers = {'User-Agent': ua}
link = requests.get(url, cookies=cookies, headers=headers).text
logos = []
trendingurl = []
trending = re.findall('<div class="movie">(.*?)</div>',link,flags=re.DOTALL)
for content in trending:
	url = re.findall('''href=['"](.*?)['"]''',content,flags=re.DOTALL)[0]
	img = re.findall('''src=['"](.*?)['"]''',content,flags=re.DOTALL)[0]
	img += '|Cookie=cf_clearance='+cookies['cf_clearance']+'&User-Agent='+ua
	logos.append(img)
	trendingurl.append(url)

try: LOGO = logos[0]
except: LOGO = AddonIcon 
try: LOGO1 = logos[1]
except: LOGO1 = AddonIcon 
try: LOGO2 = logos[2]
except: LOGO2 = AddonIcon 
try: LOGO3 = logos[3]
except: LOGO3 = AddonIcon 
try: LOGO4 = logos[4]
except: LOGO4 = AddonIcon 
try: Trendingplay1 = trendingurl[0]
except: Trendingplay1 = ''
try: Trendingplay2 = trendingurl[1]
except: Trendingplay2 = ''
try: Trendingplay3 = trendingurl[2]
except: Trendingplay3 = ''
try: Trendingplay4 = trendingurl[3]
except: Trendingplay4 = ''
try: Trendingplay5 = trendingurl[4]
except: Trendingplay5 = ''
def tick(self):

    self.DATE.setLabel(str(Date))
def search():
	string =''
	keyboard = xbmc.Keyboard(string, '[COLOR yellow][B]What Are We Searching For?[/B][/COLOR]')
	keyboard.doModal()
	if keyboard.isConfirmed():
		string = keyboard.getText()
		string = string.replace(' ','+')
		if len(string)>1:
			term = string.lower()
			url = ('http://www.seehd.pl/?s=%s' %term)
			viewer.MainWindow(url)
		else:
			dialog.notification(AddonTitle, "[COLOR red][B]Sorry, No Search Term Was Entered![/B][/COLOR]", icon, 5000)
			quit()

def opendisplay(self):
	display.MainWindow()
	
def openviewerMovies(self):
	viewer.MainWindow('http://www.seehd.pl/category/movies/')
	
def openviewerTvShows(self):
	viewer.MainWindow('http://www.seehd.pl/category/tv-shows/')
def killaddon(self):
	xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
	xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
def resolvetrending(url):
	sources = []
	titles = []
	cookies, ua = cache.cacheFunction(GetTokens)
	headers = {'User-Agent': ua}
	link = requests.get(url, cookies=cookies, headers=headers).text
	pattern = r'''(?i)<iframe.+?src="(.*?)"'''
	findlinks = re.findall(pattern,link,flags=re.DOTALL)
	found = 0
	for links in findlinks:
		found += 1
		name = ('Link | %s' %str(found))
		titles.append(name)
		sources.append(links)
	select = dialog.select('[B][COLOR yellow]Choose A Source[/B][/COLOR]',titles)
	if select < 0:quit()
	url = sources[select]
	import resolveurl
	if resolveurl.HostedMediaFile(url).valid_url():
		try:
			dialog.notification(AddonTitle, "[COLOR yellow][B]Resolving With ResolveUrl, Be Patient[/B][/COLOR]", icon, 10000)
			stream_url = resolveurl.HostedMediaFile(url).resolve()
			liz = xbmcgui.ListItem(AddonTitle)
			stream_url = str(stream_url)
			liz.setPath(stream_url)
			xbmc.Player ().play(stream_url, liz, False)
		except:
			dialog.notification(AddonTitle, "[COLOR yellow][B]Seems The File Has Been Deleted At Source[/B][/COLOR]", icon, 5000)
			quit()
	elif '24hd.be' in url:
		dialog.notification(AddonTitle, "[COLOR yellow][B]Resolving Directly, Be Patient[/B][/COLOR]", icon, 10000)
		key = url.rsplit('/',1)[1]
		ref = url
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                   'X-Requested-With' : 'XMLHttpRequest',
                   'Referer' : ref}
		link = requests.post('https://24hd.be/api/source/%s' % key, headers=headers).json()
		source = link['data'][0]['file']
		xbmc.Player ().play(source)
	else: dialog.notification(AddonTitle, "[COLOR yellow][B]Host %s Not Supported[/B][/COLOR]" %url, icon, 5000)

	

#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

	xbmc.executebuiltin("Dialog.Close(busydialog)")

	def __init__(self, title='EntertainMe'):
		#Trending()
		super(Main, self).__init__(title)
		#self.setFocus(self.button6)
		self.setGeometry(1280, 720, 100, 50)
		Background  = pyxbmct.Image(Background_Image)
		TrendingText     = pyxbmct.Image(TText)
		SearchText     = pyxbmct.Image(SText)
		Banner           = pyxbmct.Image(BannerA)
		Trending1        = pyxbmct.Image(LOGO)
		Trending2        = pyxbmct.Image(LOGO1)
		Trending3        = pyxbmct.Image(LOGO2)
		Trending4        = pyxbmct.Image(LOGO3)
		Trending5        = pyxbmct.Image(LOGO4)

		self.placeControl(Background, -10, -1, 123, 52)
		self.placeControl(TrendingText, 58, 0, 10, 8)
		self.placeControl(SearchText, 58, 38, 10, 8)
		self.placeControl(Banner, 66, 0, 2, 50)
		self.placeControl(Trending1, 68, 0, 35, 8)
		self.placeControl(Trending2, 68, 10, 35, 8)
		self.placeControl(Trending3, 68, 20, 35, 8)
		self.placeControl(Trending4, 68, 31, 35, 8)
		self.placeControl(Trending5, 68, 42, 35, 8)

		self.set_info_controls()

		self.set_active_controls()

		self.set_navigation()

		self.connect(pyxbmct.ACTION_NAV_BACK, lambda:killaddon(self))
		tick(self)
		self.connect(self.button1, lambda:resolvetrending(Trendingplay1))
		self.connect(self.button2, lambda:resolvetrending(Trendingplay2))
		self.connect(self.button3, lambda:resolvetrending(Trendingplay3))
		self.connect(self.button4, lambda:resolvetrending(Trendingplay4))
		self.connect(self.button5, lambda:resolvetrending(Trendingplay5))
		self.connect(self.button6, lambda:openviewerMovies(self))
		self.connect(self.button7, lambda:openviewerTvShows(self))
		self.connect(self.button8, lambda:opendisplay(self))
		self.connect(self.button9, lambda:search())
		self.connect(self.button10, lambda:killaddon(self))
		self.setFocus(self.button6)
		

	def set_info_controls(self):
		self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
		self.DATE =  pyxbmct.Label('',textColor='0xFFFFFF00', font='font18')
		self.placeControl(self.Hello, -4, 1, 1, 50)
		self.placeControl(self.DATE,  -9, 41, 12, 15)
		

	def set_active_controls(self):
		self.button1 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		self.placeControl(self.button1, 68, 0,  40, 8)
		
		self.button2 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		self.placeControl(self.button2, 68, 10,  40, 8)
		
		self.button3 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		self.placeControl(self.button3, 68, 20,  40, 8)
		
		self.button4 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		self.placeControl(self.button4, 68, 31,  40, 8)
		
		self.button5 = pyxbmct.Button('',   focusTexture=ButtonTrending1S,   noFocusTexture=ButtonTrending1)
		self.placeControl(self.button5, 68, 42,  40, 8)
		
		#Selection Buttons
		self.button6 = pyxbmct.Button('',   focusTexture=ButtonMoviesS,   noFocusTexture=ButtonMovies)
		self.placeControl(self.button6, -2, 0,  12, 13)
		
		self.button7 = pyxbmct.Button('',   focusTexture=ButtonTvShowsS,   noFocusTexture=ButtonTvShows)
		self.placeControl(self.button7, 10, 0,  12, 13)

		self.button8 = pyxbmct.Button('',   focusTexture=ButtonReleaseS,   noFocusTexture=ButtonRelease)
		self.placeControl(self.button8, 22, 0,  12, 13)
		
		self.button9 = pyxbmct.Button('',   focusTexture=ButtonSearchS,   noFocusTexture=ButtonSearch)
		self.placeControl(self.button9, 54, 45,  13, 5)
		
		self.button10 = pyxbmct.Button('',   focusTexture=ButtonQuitS,   noFocusTexture=ButtonQuit)
		self.placeControl(self.button10, 34, 0,  12, 13)


	def set_navigation(self):
		self.button1.controlUp(self.button10)
		self.button2.controlUp(self.button10)
		self.button3.controlUp(self.button10)
		self.button4.controlUp(self.button10)
		self.button5.controlUp(self.button10)
		self.button7.controlUp(self.button6)
		self.button8.controlUp(self.button7)
		self.button9.controlUp(self.button8)
		self.button10.controlUp(self.button8)
		
		self.button6.controlDown(self.button7)
		self.button7.controlDown(self.button8)
		self.button8.controlDown(self.button10)
		self.button9.controlDown(self.button5)
		self.button10.controlDown(self.button1)
		
		self.button2.controlLeft(self.button1)
		self.button3.controlLeft(self.button2)
		self.button4.controlLeft(self.button3)
		self.button5.controlLeft(self.button4)
		self.button9.controlLeft(self.button10)
		
		self.button6.controlRight(self.button9)
		self.button7.controlRight(self.button9)
		self.button8.controlRight(self.button9)
		self.button10.controlRight(self.button9)
		self.button1.controlRight(self.button2)
		self.button2.controlRight(self.button3)
		self.button3.controlRight(self.button4)
		self.button4.controlRight(self.button5)
		


	def setAnimation(self, control):
		control.setAnimations([('WindowOpen', 'effect=rotate start=0 end=720 time=1',),
								('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
