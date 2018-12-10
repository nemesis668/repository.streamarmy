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
tmdbapi = '5135334daa33251bc407e5f24cb1c6a5'

#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	

poster = ''
desc = ''

#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bgplayer.gif'))
ButtonBox1S = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingS.png'))
ButtonBox1 = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trending.png'))
PlayButton = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'play.png'))
PlayButtonS = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'playS.png'))
#############################################################
########## Function To Call That Starts The Window ##########
dataurl = ''
MainTitle=''
playlinks = []
playtitles = []
def MainWindow(url,title):
	global dataurl
	global MainTitle
	dataurl = url
	MainTitle = title
	getinfo(dataurl)
	window = Main('Player')
	window.doModal()
	del window

def getinfo(dataurl):
	global poster
	global desc
	global playlinks
	global playtitles
	playlinks = []
	playtitles = []
	link = requests.get(dataurl).content
	pattern = r'''<iframe.+?src="(.*?)"'''
	findlinks = re.findall(pattern,link,flags=re.DOTALL)
	found = 0
	for links in findlinks:
		found += 1
		name = ('Link | %s' %str(found))
		playtitles.append(name)
		playlinks.append(links)
	try:
		imdbid = re.findall('<a href="https://www.imdb.com/title/(.*?)/"',link,flags=re.DOTALL)[0]
	except IndexError:
		try:
			imdbid = re.findall('<a href="http://www.imdb.com/title/(.*?)/"',link,flags=re.DOTALL)[0]
		except IndexError: imdbid = ''
	if len(imdbid) >10 : imdbid = re.findall('<a href="https://www.imdb.com/title/(.*?)"',link,flags=re.DOTALL)[0]
	if not imdbid == '':
		tmdburl = ('https://api.themoviedb.org/3/find/%s?api_key=%s&external_source=imdb_id' % (imdbid,tmdbapi))
		link2 = requests.get(tmdburl).json()
		data = link2['tv_results']
		if len(data) <1  : data = link2['movie_results']
		for info in data:
			poster = info['poster_path']
			poster = 'http://image.tmdb.org/t/p/w500' + poster
			desc = info['overview']
	else:
		poster = icon
		desc = 'No TMDB Information Found For This Item'


def resolve():
	select = dialog.select('[B][COLOR yellow]Choose A Source[/B][/COLOR]',playtitles)
	if select < 0:quit()
	url = playlinks[select]
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
def tick(self):

    self.DATE.setLabel (str(Date))

def CLEANUP(text):

	text = str(text)
	text = text.replace('\\r','')
	text = text.replace('\\n','')
	text = text.replace('\\t','')
	text = text.replace('\\','')
	text = text.replace('<br />','\n')
	text = text.replace('<hr />','')
	text = text.replace('&#039;',"'")
	text = text.replace('&#39;',"'")
	text = text.replace('&quot;','"')
	text = text.replace('&rsquo;',"'")
	text = text.replace('&amp;',"&")
	text = text.replace('&#8211;',"&")
	text = text.replace('&#8217;',"'")
	text = text.replace('&#038;',"&")
	text = text.replace('&#8211;',"-")
	text = text.replace('&nbsp;',"")
	text = text.replace('&hellip;',"...")
	text = text.replace('&#8220;',"\"")
	text = text.replace('&#8230;',"...")
	text = text.replace('&#8221;',"\"")
	text = text.replace('<em>',"|")
	text = text.replace('</em>',"|")
	text = text.lstrip(' ')
	text = text.lstrip('	')

	return text
	

#############################################################
######### Class Containing the GUi Code / Controls ##########
class Main(pyxbmct.AddonFullWindow):
# DImensions = H,FL,BH,BW
	xbmc.executebuiltin("Dialog.Close(busydialog)")
	def __init__(self, title='EntertainMe'):
		super(Main, self).__init__(title)

		self.setGeometry(1280, 720, 100, 50)
		Background  = pyxbmct.Image(Background_Image)

		self.placeControl(Background, -10, -1, 123, 52)
		Box1 = pyxbmct.Image(poster)
		self.placeControl(Box1, 12, 1, 89, 18)
		self.textbox = pyxbmct.TextBox(textColor='0xFFFFFFFF',font='font24')
		self.placeControl(self.textbox, 12, 27, 41, 22)
		self.textbox.autoScroll(2000, 2000, 2000)
		self.textbox.setText(MainTitle+'\n\n'+desc)
		self.set_info_controls()

		self.set_active_controls()

		self.set_navigation()

		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
		
		self.connect(self.Button1, lambda:resolve())
		self.setFocus(self.Button1)


	def set_info_controls(self):
		self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
		self.DATE =  pyxbmct.Label('',textColor='0xFFFFFF00', font='font18')
		self.placeControl(self.Hello, -4, 1, 1, 50)
		self.placeControl(self.DATE,  -9, 41, 12, 15)

		
		

	def set_active_controls(self):
		self.Button1 = pyxbmct.Button('',   focusTexture=PlayButtonS,   noFocusTexture=PlayButton)
		self.placeControl(self.Button1, 84, 40,  25, 9)
		
		self.connectEventList(
			[pyxbmct.ACTION_MOVE_DOWN,
			 pyxbmct.ACTION_MOVE_UP,
			 pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
			 pyxbmct.ACTION_MOUSE_WHEEL_UP,
			 pyxbmct.ACTION_MOUSE_MOVE],
			self.List_update)

	def set_navigation(self):
		pass

	def setAnimation(self, control):
		control.setAnimations([('WindowOpen', 'effect=slide start=2000 end=0 time=1000',),
								('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
	def List_update(self):
		#tick(self)
		pass
