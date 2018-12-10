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
import player


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
nextpage = ''



#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_			= _self_.getSetting('Theme')
_images_		= '/resources/' + _theme_	


#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image	= xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'bgviewer.gif'))
ButtonBox1S = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trendingS.png'))
ButtonBox1 = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'trending.png'))
ButtonBox13S = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Next-PageS.gif'))
ButtonBox13 = xbmc.translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'Next-Page.gif'))


#############################################################
########## Function To Call That Starts The Window ##########
def MainWindow(type):
	GetContent(type)
	window = Main('Viewer')
	window.doModal()
	del window
	
def GetContent(url):
	global LOGO1
	global LOGO2
	global LOGO3
	global LOGO4
	global LOGO5
	global LOGO6
	global LOGO7
	global LOGO8
	global LOGO9
	global LOGO10
	global LOGO11
	global LOGO12
	global titles
	global urls
	global nextpage
	logos = []
	urls = []
	titles = []
	link = requests.get(url).content
	match = re.findall('<div class="movie big">(.*?)</div>',link,flags=re.DOTALL)
	try:
		nextpage = re.findall('''next\s+page.+?href=['"](.*?)['"]''',link,flags=re.DOTALL)[0]
	except: pass
	for content in match:
		url = re.findall('<a href="(.*?)"',content,flags=re.DOTALL)[1]
		icon = re.findall('src="(.*?)" ',content,flags=re.DOTALL)[0]
		title = re.findall('<h2 class="thumb_title">(.*?)</h2>',content,flags=re.DOTALL)[0].replace('Watch Online','')
		title = CLEANUP(title)
		logos.append(icon)
		urls.append(url)
		titles.append(title)
	try: LOGO1 = logos[0]
	except IndexError : LOGO1 = ''
	try: LOGO2 = logos[1]
	except IndexError: LOGO2 = ''
	try: LOGO3 = logos[2]
	except IndexError: LOGO3 = ''
	try: LOGO4 = logos[3]
	except IndexError: LOGO4 = ''
	try: LOGO5 = logos[4]
	except IndexError: LOGO5 = ''
	try: LOGO6 = logos[5]
	except IndexError: LOGO6 = ''
	try: LOGO7 = logos[6]
	except IndexError: LOGO7 = ''
	try: LOGO8 = logos[7]
	except IndexError: LOGO8 =''
	try: LOGO9 = logos[8]
	except IndexError: LOGO9 =''
	try: LOGO10 = logos[9]
	except IndexError: LOGO10 = ''
	try: LOGO11 = logos[10]
	except IndexError: LOGO11 = ''
	try: LOGO12 = logos[11]
	except IndexError: LOGO12 = ''

def GoToNextPage(self,url):
	MainWindow(url)
	self.close()

def Player(url,title):
	player.MainWindow(url,title)
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

	xbmc.executebuiltin("Dialog.Close(busydialog)")

	def __init__(self, title='EntertainMe'):
		super(Main, self).__init__(title)

		self.setGeometry(1280, 720, 100, 50)
		Background  = pyxbmct.Image(Background_Image)

		self.placeControl(Background, -10, -1, 123, 52)
		

		self.set_info_controls()

		self.set_active_controls()
		self.set_navigation()
		
		try: url1 = urls[0]
		except IndexError: url1 = ''
		try: url2 = urls[1]
		except IndexError: url2 = ''
		try: url3 = urls[2]
		except IndexError: url3 = ''
		try: url4 = urls[3]
		except IndexError: url4 = ''
		try: url5 = urls[4]
		except IndexError: url5 = ''
		try: url6 = urls[5]
		except IndexError: url6 = ''
		try: url7 = urls[6]
		except IndexError: url7 = ''
		try: url8 = urls[7]
		except IndexError: url8 = ''
		try: url9 = urls[8]
		except IndexError: url9 = ''
		try: url10 = urls[9]
		except IndexError: url10 = ''
		try: url11 = urls[10]
		except IndexError: url11 = ''
		try: url12 = urls[11]
		except IndexError: url12 = ''
		try: title1 = titles[0]
		except IndexError: title1 = ''
		try: title2 = titles[1]
		except IndexError: title2 = ''
		try: title3 = titles[2]
		except IndexError: title3 = ''
		try: title4 = titles[3]
		except IndexError: title4 = ''
		try: title5 = titles[4]
		except IndexError: title5 = ''
		try: title6 = titles[5]
		except IndexError: title6 = ''
		try: title7 = titles[6]
		except IndexError: title7 = ''
		try: title8 = titles[7]
		except IndexError: title8 = ''
		try: title9 = titles[8]
		except IndexError: title9 = ''
		try: title10 = titles[9]
		except IndexError: title10 = ''
		try: title11 = titles[10]
		except IndexError: title11 = ''
		try: title12 = titles[11]
		except IndexError: title12 = ''
		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
		self.connect(self.button1, lambda:Player(url1,title1))
		self.connect(self.button2, lambda:Player(url2,title2))
		self.connect(self.button3, lambda:Player(url3,title3))
		self.connect(self.button4, lambda:Player(url4,title4))
		self.connect(self.button5, lambda:Player(url5,title5))
		self.connect(self.button6, lambda:Player(url6,title6))
		self.connect(self.button7, lambda:Player(url7,title7))
		self.connect(self.button8, lambda:Player(url8,title8))
		self.connect(self.button9, lambda:Player(url9,title9))
		self.connect(self.button10, lambda:Player(url10,title10))
		self.connect(self.button11, lambda:Player(url11,title11))
		self.connect(self.button12, lambda:Player(url12,title12))
		self.connect(self.button13, lambda:GoToNextPage(self,nextpage))

		Box1 = pyxbmct.Image(LOGO1)
		Box2 = pyxbmct.Image(LOGO2)
		Box3 = pyxbmct.Image(LOGO3)
		Box4 = pyxbmct.Image(LOGO4)
		Box5 = pyxbmct.Image(LOGO5)
		Box6 = pyxbmct.Image(LOGO6)
		Box7 = pyxbmct.Image(LOGO7)
		Box8 = pyxbmct.Image(LOGO8)
		Box9 = pyxbmct.Image(LOGO9)
		Box10 = pyxbmct.Image(LOGO10)
		Box11 = pyxbmct.Image(LOGO11)
		Box12 = pyxbmct.Image(LOGO12)
		
		self.placeControl(Box1, 8, 1, 30, 7)
		self.placeControl(Box2, 8, 9, 30, 7)
		self.placeControl(Box3, 8, 17, 30, 7)
		self.placeControl(Box4, 8, 25, 30, 7)
		self.placeControl(Box5, 8, 33, 30, 7)
		self.placeControl(Box6, 8, 41, 30, 7)
		self.placeControl(Box7, 43, 1, 30, 7)
		self.placeControl(Box8, 43, 9, 30, 7)
		self.placeControl(Box9, 43, 17, 30, 7)
		self.placeControl(Box10, 78, 1, 30, 7)
		self.placeControl(Box11, 78, 9, 30, 7)
		self.placeControl(Box12, 78, 17, 30, 7)
		self.setFocus(self.button1)

	def set_info_controls(self):
		self.textbox = pyxbmct.Label('',textColor='0xFFFFFFFF',font='font24',alignment=pyxbmct.ALIGN_CENTER)
		self.placeControl(self.textbox, 40, 28, 40, 15)
		self.Hello = pyxbmct.Label('', textColor='0xFFF44248', font='font60', alignment=pyxbmct.ALIGN_CENTER)
		self.DATE =  pyxbmct.Label('',textColor='0xFFFFFF00', font='font18')
		self.placeControl(self.Hello, -4, 1, 1, 50)
		self.placeControl(self.DATE,  -9, 41, 12, 15)
		
		

	def set_active_controls(self):
		self.button1 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button1, 7, 1,  35, 7)
		
		self.button2 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button2, 7, 9,  35, 7)
		
		self.button3 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button3, 7, 17,  35, 7)
		
		self.button4 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button4, 7, 25,  35, 7)
		
		self.button5 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button5, 7, 33,  35, 7)
		
		self.button6 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button6, 7, 41,  35, 7)
		
		self.button7 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button7, 42, 1,  35, 7)
		
		self.button8 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button8, 42, 9,  35, 7)
		
		self.button9 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button9, 42, 17,  35, 7)
		
		self.button10 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button10, 77, 1,  35, 7)
		
		self.button11 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button11, 77, 9,  35, 7)
		
		self.button12 = pyxbmct.Button('',   focusTexture=ButtonBox1S,   noFocusTexture=ButtonBox1)
		self.placeControl(self.button12, 77, 17,  35, 7)
		
		self.button13 = pyxbmct.Button('',   focusTexture=ButtonBox13S,   noFocusTexture=ButtonBox13)
		self.placeControl(self.button13, 100, 36,  10, 12)
		
		self.connectEventList(
			[pyxbmct.ACTION_MOVE_DOWN,
			 pyxbmct.ACTION_MOVE_UP,
			 pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
			 pyxbmct.ACTION_MOUSE_WHEEL_UP,
			 pyxbmct.ACTION_MOUSE_MOVE,
			 pyxbmct.ACTION_MOVE_LEFT,
			 pyxbmct.ACTION_MOVE_RIGHT],
			self.List_update)

	def set_navigation(self):
		self.button1.controlRight(self.button2)
		self.button2.controlRight(self.button3)
		self.button3.controlRight(self.button4)
		self.button4.controlRight(self.button5)
		self.button5.controlRight(self.button6)
		self.button7.controlRight(self.button8)
		self.button8.controlRight(self.button9)
		self.button9.controlRight(self.button13)
		self.button10.controlRight(self.button11)
		self.button11.controlRight(self.button12)
		self.button12.controlRight(self.button13)

		
		self.button2.controlLeft(self.button1)
		self.button3.controlLeft(self.button2)
		self.button4.controlLeft(self.button3)
		self.button5.controlLeft(self.button4)
		self.button6.controlLeft(self.button5)
		self.button8.controlLeft(self.button7)
		self.button9.controlLeft(self.button8)
		self.button11.controlLeft(self.button10)
		self.button12.controlLeft(self.button11)
		self.button13.controlLeft(self.button12)
		
		self.button1.controlDown(self.button7)
		self.button2.controlDown(self.button8)
		self.button3.controlDown(self.button9)
		self.button4.controlDown(self.button13)
		self.button5.controlDown(self.button13)
		self.button6.controlDown(self.button13)
		self.button7.controlDown(self.button10)
		self.button8.controlDown(self.button11)
		self.button9.controlDown(self.button12)
		
		
		self.button7.controlUp(self.button1)
		self.button8.controlUp(self.button2)
		self.button9.controlUp(self.button3)
		self.button10.controlUp(self.button7)
		self.button11.controlUp(self.button8)
		self.button12.controlUp(self.button9)
		self.button13.controlUp(self.button6)
		




	def setAnimation(self, control):
		control.setAnimations([('WindowOpen', 'effect=slide start=2000 end=0 time=1000',),
								('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
	def List_update(self):
		logos = []
		urls = []
		try: title1 = titles[0]
		except IndexError: title1 = ''
		try: title2 = titles[1]
		except IndexError: title2 = ''
		try: title3 = titles[2]
		except IndexError: title3 = ''
		try: title4 = titles[3]
		except IndexError: title4 = ''
		try: title5 = titles[4]
		except IndexError: title5 = ''
		try: title6 = titles[5]
		except IndexError: title6 = ''
		try: title7 = titles[6]
		except IndexError: title7 = ''
		try: title8 = titles[7]
		except IndexError: title8 = ''
		try: title9 = titles[8]
		except IndexError: title9 = ''
		try: title10 = titles[9]
		except IndexError: title10 = ''
		try: title11 = titles[10]
		except IndexError: title11 = ''
		try: title12 = titles[11]
		except IndexError: title12 = ''
		position = self.getFocus()
		if position == self.button1:
			self.textbox.setLabel(title1)
		elif position == self.button2:
			self.textbox.setLabel(title2)
		elif position == self.button3:
			self.textbox.setLabel(title3)
		elif position == self.button4:
			self.textbox.setLabel(title4)
		elif position == self.button5:
			self.textbox.setLabel(title5)
		elif position == self.button6:
			self.textbox.setLabel(title6)
		elif position == self.button7:
			self.textbox.setLabel(title7)
		elif position == self.button8:
			self.textbox.setLabel(title8)
		elif position == self.button9:
			self.textbox.setLabel(title9)
		elif position == self.button10:
			self.textbox.setLabel(title10)
		elif position == self.button11:
			self.textbox.setLabel(title11)
		elif position == self.button12:
			self.textbox.setLabel(title12)
		else:
			self.textbox.setLabel('EnterTain Me By @Nemzzy668')
			self.textbox.autoScroll(1000, 1000, 1000)
	