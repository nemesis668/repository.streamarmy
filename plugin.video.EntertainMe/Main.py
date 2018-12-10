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

dialog = xbmcgui.Dialog()


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
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bg.gif'))
TText	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingtxt.png'))
SText	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'searchtxt.png'))
BannerA	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'banner.png'))
ButtonTrending1S = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingS.png'))
ButtonTrending1 = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trending.png'))
ButtonMovies = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_movies.gif'))
ButtonMoviesS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_moviesS.gif'))
ButtonTvShows = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_tvshows.gif'))
ButtonTvShowsS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_tvshowsS.gif'))
ButtonRelease = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_release.gif'))
ButtonReleaseS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_releaseS.gif'))
ButtonSearch = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_search.png'))
ButtonSearchS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_searchS.png'))
ButtonQuit = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_quit.gif'))
ButtonQuitS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'button_quitS.gif'))

url = 'http://www.seehd.pl/'
link = requests.get(url).content

logos = []
trendingurl = []
trending = re.findall('<h4>Trending(.*?)</div>',link,flags=re.DOTALL)[0]
pattern = r'''<a href="(.*?)">.+?src="(.*?)"'''
grabthem = re.findall(pattern,trending,flags=re.DOTALL)
for url,img in grabthem:
	logos.append(img)
	trendingurl.append(url)

LOGO = logos[0]
LOGO1 = logos[1]
LOGO2 = logos[2]
LOGO3 = logos[3]
LOGO4 = logos[4]
Trendingplay1 = trendingurl[0]
Trendingplay2 = trendingurl[1]
Trendingplay3 = trendingurl[2]
Trendingplay4 = trendingurl[3]
Trendingplay5 = trendingurl[4]


#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow():

	window = Main('EntertainMe')
	window.doModal()
	del window
    
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

def resolvetrending(url):
	sources = []
	titles = []
	link = requests.get(url).content
	pattern = r'''<iframe.+?src="(.*?)"'''
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
			dialog.notification(AddonTitle, "[COLOR yellow][B]Resolving With ResolveUrl[/B][/COLOR]", icon, 5000)
			stream_url = resolveurl.HostedMediaFile(url).resolve()
			liz = xbmcgui.ListItem(AddonTitle)
			stream_url = str(stream_url)
			liz.setPath(stream_url)
			xbmc.Player ().play(stream_url, liz, False)
		except:
			dialog.notification(AddonTitle, "[COLOR yellow][B]Seems The File Has Been Deleted At Source[/B][/COLOR]", icon, 5000)
			quit()
	else:
		dialog.notification(AddonTitle, "[COLOR yellow][B]Host %s Not Supported[/B][/COLOR]" %url, icon, 5000)

	

#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):

	xbmc.executebuiltin("Dialog.Close(busydialog)")

	def __init__(self, title='EntertainMe'):
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

		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
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
		self.connect(self.button10, self.close)
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
		self.placeControl(self.button6, 10, 0,  10, 6)
		
		self.button7 = pyxbmct.Button('',   focusTexture=ButtonTvShowsS,   noFocusTexture=ButtonTvShows)
		self.placeControl(self.button7, 22, 0,  10, 8)

		self.button8 = pyxbmct.Button('',   focusTexture=ButtonReleaseS,   noFocusTexture=ButtonRelease)
		self.placeControl(self.button8, 34, 0,  10, 10)
		
		self.button9 = pyxbmct.Button('',   focusTexture=ButtonSearchS,   noFocusTexture=ButtonSearch)
		self.placeControl(self.button9, 54, 45,  13, 5)
		
		self.button10 = pyxbmct.Button('',   focusTexture=ButtonQuitS,   noFocusTexture=ButtonQuit)
		self.placeControl(self.button10, 46, 0,  10, 6)


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
