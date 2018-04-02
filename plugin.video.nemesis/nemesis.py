#########################################
############CODE BY @NEMZZY668###########
#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , uuid , os , re , sys , base64 , json , time , shutil , random , liveresolver , hashlib , datetime , smtplib
from resources . libs . modules import cfscrape
from resources . libs . common_addon import Addon
from metahandler import metahandlers
from HTMLParser import HTMLParser
from datetime import datetime
import resolveurl
from resources . libs . modules import devilcheck
from resources . libs . modules import dom_parser2
from resources . libs . modules import regex
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.nemesis'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = base64 . b64decode ( b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L0ZjcHQyNTN4' )
iIiiiI1IiI1I1 = xbmcaddon . Addon ( id = o0OO00 )
o0OoOoOO00 = '[COLOR aqua][B]Nemesis[/B][/COLOR]'
I11i = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
O0O = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.nemesis' )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads/' ) )
iIiiiI = xbmcgui . DialogProgress ( )
Iii1ii1II11i = xbmcgui . Dialog ( )
iI111iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'intro.txt' ) )
IiII = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'settings.xml' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'adult.txt' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.SportsDevil' ) )
I1i1iiI1 = base64 . b64decode ( b'NTEzNTMzNGRhYTMzMjUxYmM0MDdlNWYyNGNiMWM2YTU=' )
iiIIIII1i1iI = [ 'program.plexus' ]
o0oO0 = ''
if 100 - 100: i11Ii11I1Ii1i
if 67 - 67: iiI1iIiI . ooo0Oo0 * i1 - Oooo0000 * i1IIi11111i / o000o0o00o0Oo
def ooIiII1I1i1i1ii ( ) :
 if 44 - 44: OOo0o0 / OOoOoo00oo - iI1 + OOooO % OOoO00o
 if 9 - 9: I1iiiiI1iII - oOo0 / i1Ii % i1IIi
 if not os . path . exists ( os . path . dirname ( o0OOO ) ) :
  try :
   os . makedirs ( os . path . dirname ( o0OOO ) )
   with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
    o00O00O0O0O . write ( "<date>000</date>" )
  except OSError as OooO0OO :
   if OooO0OO . errno != errno . EEXIST :
    raise
    if 28 - 28: i11Ii11I1Ii1i
def iii11iII ( ) :
 if 42 - 42: oOo0 + o000o0o00o0Oo
 OOoO000O0OO = xbmc . getInfoLabel ( "System.BuildVersion" )
 iiI1IiI = float ( OOoO000O0OO [ : 4 ] )
 if iiI1IiI >= 11.0 and iiI1IiI <= 11.9 :
  II = 'Eden'
 elif iiI1IiI >= 12.0 and iiI1IiI <= 12.9 :
  II = 'Frodo'
 elif iiI1IiI >= 13.0 and iiI1IiI <= 13.9 :
  II = 'Gotham'
 elif iiI1IiI >= 14.0 and iiI1IiI <= 14.9 :
  II = 'Helix'
 elif iiI1IiI >= 15.0 and iiI1IiI <= 15.9 :
  II = 'Isengard'
 elif iiI1IiI >= 16.0 and iiI1IiI <= 16.9 :
  II = 'Jarvis'
 elif iiI1IiI >= 17.0 and iiI1IiI <= 17.9 :
  II = 'Krypton'
 else : II = "Decline"
 if 57 - 57: OOo0o0
 if II == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif II == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 14 - 14: ooo0Oo0 . iiI1iIiI / OOooO
def IiiiI1II1I1 ( ) :
 if 95 - 95: OoooooooOO . iIii1I11I1II1
 O00o = [ 'plugin.video.ghostshader' ]
 O00 = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in O00o )
 i11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.ghostshader' ) )
 if O00 :
  import shutil
  Iii1ii1II11i . ok ( o0OoOoOO00 , "Sorry We Have Detected You Using An Addon That Steals Content From Us, Ghostshader is not supported by Nemesis and will be removed" )
  shutil . rmtree ( i11I1 )
  os . _exit ( 1 )
 else :
  return
  if 8 - 8: iIii1I11I1II1 - I1iiiiI1iII % iIii1I11I1II1 - OOooO * iiI1iIiI
def iI11i1I1 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) :
  return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) :
  return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) :
  return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) :
  return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) :
  return 'ios'
  if 71 - 71: i1Ii % OOoO00o / i1IIi11111i
def ii11i1iIII ( ) :
 if 3 - 3: i1IIi / iiI1iIiI % iI1 * i11iIiiIii / O0 * iI1
 III1ii1iII ( )
 IiiiI1II1I1 ( )
 oo0oooooO0 = baseurl
 i11Iiii = oo0oooooO0
 iI = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( iI >= 0000 ) and ( iI <= 1159 ) : I1i1I1II = "Morning"
 elif ( iI >= 1200 ) and ( iI <= 1759 ) : I1i1I1II = "Afternoon"
 else : I1i1I1II = "Evening"
 i1IiIiiI ( '[COLOR yellow]Good[COLOR aqua] ' + str ( I1i1I1II ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 i1IiIiiI ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  I1I = oOO00oOO ( baseurl )
  OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( I1I )
  for iIo00O in OoOo :
   try :
    if '<m3u>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 11 , Iii111II , I1ii11iIi11i )
    elif '<mamahdsports>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 14 , Iii111II , I1ii11iIi11i )
    elif '<atc>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<atc>(.+?)</atc>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 6 , Iii111II , I1ii11iIi11i )
    elif '<scanner>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 11 , Iii111II , I1ii11iIi11i )
    elif '<cartoons>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 29 , Iii111II , I1ii11iIi11i )
    elif '<Adult>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 38 , Iii111II , I1ii11iIi11i )
    elif '<Anime>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 51 , Iii111II , I1ii11iIi11i )
    elif '<audiobooks>' in iIo00O :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     oo0oooooO0 = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( iIo00O ) [ 0 ]
     iiii11I ( OOO0OOO00oo , oo0oooooO0 , 59 , Iii111II , I1ii11iIi11i )
    elif '<folder>' in iIo00O :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iIo00O )
     for OOO0OOO00oo , oo0oooooO0 , Iii111II , I1ii11iIi11i in Ooo0OO0oOO :
      iiii11I ( OOO0OOO00oo , oo0oooooO0 , 1 , Iii111II , I1ii11iIi11i )
    else :
     ii11i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( iIo00O )
     if len ( ii11i1 ) == 1 :
      Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iIo00O )
      IIIii1II1II = len ( OoOo )
      for OOO0OOO00oo , oo0oooooO0 , Iii111II , I1ii11iIi11i in Ooo0OO0oOO :
       if 'youtube.com/playlist' in oo0oooooO0 :
        iiii11I ( OOO0OOO00oo , oo0oooooO0 , 2 , Iii111II , I1ii11iIi11i )
       else :
        i1IiIiiI ( OOO0OOO00oo , oo0oooooO0 , 2 , Iii111II , I1ii11iIi11i )
     elif len ( ii11i1 ) > 1 :
      OOO0OOO00oo = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
      Iii111II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
      i1IiIiiI ( OOO0OOO00oo , i11Iiii , 3 , Iii111II , I1ii11iIi11i )
   except : pass
   if 42 - 42: OOooO + OOo0o0
  i1IiIiiI ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.resolveurl/settings.xml" )
   I1i1I1II = open ( file ) . read ( )
   o0O0o0Oo = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( I1i1I1II ) [ 0 ]
   o0O0o0Oo = o0O0o0Oo . strip ( )
   oo0oooooO0 = 'plugin://script.module.resolveurl/?mode=auth_rd'
   if 'value=""' in o0O0o0Oo :
    Ii11Ii1I = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    i1IiIiiI ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( Ii11Ii1I ) + '[/COLOR]' , oo0oooooO0 , 2 , I1IiI , Oo )
   else :
    Ii11Ii1I = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    i1IiIiiI ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( Ii11Ii1I ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  O00oO = 'https://i.imgur.com/o2Wvut7.jpg'
  iiii11I ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , O00oO , Oo )
  I11i1I1I = 'https://i.imgur.com/SxZzRX9.jpg'
  iiii11I ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , I11i1I1I , Oo )
  oO0Oo = 'https://i.imgur.com/zme6vuj.jpg'
  iiii11I ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , oO0Oo , Oo )
 except :
  oOOoo0Oo = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if oOOoo0Oo == 0 :
   i1IiIiiI ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   iiii11I ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if oOOoo0Oo == 1 :
   quit ( )
   if 78 - 78: iI1
 iii11iII ( )
 if 71 - 71: OOoOoo00oo + i1Ii % i11iIiiIii + o000o0o00o0Oo - I1iiiiI1iII
def oO0OOoO0 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i11Iiii = url
 I1I = oOO00oOO ( url )
 IiiiI1II1I1 ( )
 OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( I1I )
 for iIo00O in OoOo :
  try :
   if '<image>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 23 , iconimage , fanart )
   elif '<American>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 77 , iconimage , fanart )
   elif '<lordjd>' in iIo00O :
    ii11i1 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( iIo00O )
    if len ( ii11i1 ) == 1 :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iIo00O )
     IIIii1II1II = len ( OoOo )
     for name , url , iconimage , fanart in Ooo0OO0oOO :
      if 'youtube.com/playlist' in url :
       iiii11I ( name , url , 2 , iconimage , fanart )
      else :
       I111Ii111 ( name , url , 2 , iconimage , fanart )
    elif len ( ii11i1 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     I111Ii111 ( name , i11Iiii , 3 , iconimage , fanart )
   elif '<reddit>' in iIo00O :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( iIo00O ) [ 0 ]
    iiii11I ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in iIo00O :
    ii11i1 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( iIo00O )
    if len ( ii11i1 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( iIo00O ) [ 0 ]
     i111IiI1I = re . compile ( '<referer>(.+?)</referer>' ) . findall ( iIo00O ) [ 0 ]
     O0iII = i111IiI1I
     o0 = "/"
     if not O0iII . endswith ( o0 ) :
      ooOooo000oOO = O0iII + "/"
     else :
      ooOooo000oOO = O0iII
     I1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = I1I + '%26referer=' + ooOooo000oOO
     i1IiIiiI ( name , url , 10 , iconimage , fanart )
    elif len ( ii11i1 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     i1IiIiiI ( name , i11Iiii , 16 , iconimage , fanart )
     if 59 - 59: i11Ii11I1Ii1i + OoooooooOO * Oooo0000 + i1IIi
   elif '<folder>' in iIo00O :
    Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iIo00O )
    for name , url , iconimage , fanart in Ooo0OO0oOO :
     iiii11I ( name , url , 1 , iconimage , fanart )
     if 58 - 58: i11Ii11I1Ii1i * OOoOoo00oo * o000o0o00o0Oo / OOoOoo00oo
   else :
    ii11i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( iIo00O )
    if len ( ii11i1 ) == 1 :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iIo00O )
     IIIii1II1II = len ( OoOo )
     for name , url , iconimage , fanart in Ooo0OO0oOO :
      if 'youtube.com/playlist' in url :
       iiii11I ( name , url , 2 , iconimage , fanart )
      else :
       i1IiIiiI ( name , url , 2 , iconimage , fanart )
    elif len ( ii11i1 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iIo00O ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIo00O ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIo00O ) [ 0 ]
     i1IiIiiI ( name , i11Iiii , 3 , iconimage , fanart )
  except : pass
  if 75 - 75: OOo0o0
 iii11iII ( )
 if 50 - 50: OOooO / ooo0Oo0 - OOo0o0 - iI1 % OOoO00o - OOo0o0
 if 91 - 91: i1 / iI1 - i11Ii11I1Ii1i . iI1
 if 18 - 18: i1IIi11111i
 if 98 - 98: OOoO00o * OOoO00o / OOoO00o + iI1
 if 34 - 34: i1Ii
 if 15 - 15: iI1 * i1Ii * ooo0Oo0 % i11iIiiIii % Oooo0000 - OOoOoo00oo
 if 68 - 68: oOo0 % i1IIi . I1iiiiI1iII . o000o0o00o0Oo
 if 92 - 92: OOoO00o . oOo0
def i1i ( url ) :
 if 50 - 50: I1iiiiI1iII
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( I1I )
 for ii11i1 in OoOo :
  try :
   i11I1iIiII = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   iiii11I ( "[COLOR skyblue]" + i11I1iIiII + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 96 - 96: ooo0Oo0
def Ii1I1IIii1II ( url ) :
 if 65 - 65: OOooO . iIii1I11I1II1 / O0 - OOooO
 iii1i1iiiiIi = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 Iiii = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 i1IiIiiI ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 I1I = oOO00oOO ( url )
 ii11i1 = 0
 OO0OoO0o00 = re . compile ( 'href="([^"]+)' ) . findall ( I1I )
 for url in OO0OoO0o00 :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in iii1i1iiiiIi ) :
    ii11i1 += 1
    i11I1iIiII = "Link " + str ( ii11i1 ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    ooOO0O0ooOooO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     i1IiIiiI ( "[COLOR skyblue]" + i11I1iIiII + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in Iiii ) :
     i1IiIiiI ( "[COLOR yellow]" + i11I1iIiII + url + "[/COLOR]" , ooOO0O0ooOooO , 2 , I1IiI , I1ii11iIi11i )
    else :
     i1IiIiiI ( "[COLOR skyblue]" + i11I1iIiII + url + "[/COLOR]" , ooOO0O0ooOooO , 2 , I1IiI , I1ii11iIi11i )
     if 55 - 55: i1IIi11111i * Oooo0000
     if 61 - 61: iI1
     if 86 - 86: iI1 % Oooo0000 / iiI1iIiI / Oooo0000
def iIIi1i1 ( url ) :
 if 10 - 10: iI1
 if url == 'Football' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  OOooOO000 = oOO00oOO ( 'http://wizhdsports.is/sport/Cricket' )
 OOoOoo = dom_parser2 . parse_dom ( OOooOO000 , 'div' , { 'class' : 'card' } )
 OOoOoo = [ ( dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for oO0000OOo00 in OOoOoo ]
 if len ( OOoOoo ) < 1 :
  i1IiIiiI ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , Iii111II , Oo , '' )
 OOoOoo = [ ( oO0000OOo00 [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , oO0000OOo00 [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , oO0000OOo00 [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , oO0000OOo00 [ 2 ] [ 0 ] . content ) if oO0000OOo00 [ 2 ] else 'Upcoming' , oO0000OOo00 [ 3 ] [ 0 ] . content ) for oO0000OOo00 in OOoOoo ]
 if 27 - 27: iiI1iIiI % iiI1iIiI
 if 1 - 1: i1 - OOo0o0 . iI1 . i1 / ooo0Oo0 + iI1
 if 78 - 78: O0 . OOo0o0 . i11Ii11I1Ii1i % OOoOoo00oo
 if 49 - 49: OOooO / i1 . i11Ii11I1Ii1i
 OOoOoo = [ ( oO0000OOo00 [ 0 ] , oO0000OOo00 [ 1 ] , oO0000OOo00 [ 2 ] , oO0000OOo00 [ 3 ] , oO0000OOo00 [ 4 ] ) for oO0000OOo00 in OOoOoo ]
 ooOOoooooo = 0
 II1I = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for oO0000OOo00 in OOoOoo :
  O0i1II1Iiii1I11 = oO0000OOo00 [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( ooOOoooooo ) )
  ooOOoooooo += 1
  time . sleep ( 0.10 )
  O0i1II1Iiii1I11 = IIII ( O0i1II1Iiii1I11 )
  iiIiI = oO0000OOo00 [ 1 ]
  o00oooO0Oo = oO0000OOo00 [ 3 ]
  if 'Match Over' in o00oooO0Oo :
   II1I += 1
  o0O0OOO0Ooo = dom_parser2 . parse_dom ( oO0000OOo00 [ 4 ] , 'a' )
  for OOooOO000 in o0O0OOO0Ooo :
   iiIiII1 = re . sub ( '<.+?>' , '' , OOooOO000 . content )
   I1I = OOooOO000 . attrs [ 'href' ]
   I1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + I1I
   if not 'Match Over' in o00oooO0Oo :
    i1IiIiiI ( '[COLOR aqua]' + O0i1II1Iiii1I11 + '[COLOR yellow]' + ' ' + o00oooO0Oo + '[/COLOR]' , I1I , 2 , Iii111II , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( ooOOoooooo ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( II1I ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 86 - 86: Oooo0000 - OOooO - i1 * OOoO00o
def oooo0O0 ( url ) :
 if 51 - 51: i1 / i1
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = re . compile ( 'title="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  if 53 - 53: ooo0Oo0
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 29 - 29: o000o0o00o0Oo + OOo0o0 % O0
 try :
  I1I11 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( I1I ) [ 0 ]
  I1IiI = Iii111II
  iiii11I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1I11 , 18 , Iii111II , Oo , '' )
 except : pass
 if 34 - 34: iiI1iIiI . OOoOoo00oo * o000o0o00o0Oo + oOo0
def i11111IIIII ( url , iconimage , fanart ) :
 if 19 - 19: Oooo0000 * i1IIi
 i1IiIiiI ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( I1I )
 if 14 - 14: OOoO00o
 for ii11i1 in OoOo :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = str . lower ( url )
  if '1e' in ooOO0O0ooOooO :
   i11I1iIiII = '1st Half'
  else :
   i11I1iIiII = '2nd Half'
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 11 - 11: I1iiiiI1iII * iiI1iIiI . iIii1I11I1II1 % OoooooooOO + OOoO00o
def OOO ( ) :
 if 68 - 68: i11Ii11I1Ii1i + iI1
 oo0oooooO0 = 'http://www.goalsarena.org/en/'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( OoOo )
 for OoOO000 , i1Ii11i1i in I1I1I :
  iiii11I ( "[COLOR skyblue]" + i1Ii11i1i + "[/COLOR]" , OoOO000 , 21 , I1IiI , Oo , '' )
  if 91 - 91: i1
def oOooOo0 ( url ) :
 if 38 - 38: oOo0
 if 84 - 84: iIii1I11I1II1 % OOoO00o / iIii1I11I1II1 % iI1
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 oOOoo0Oo = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if oOOoo0Oo == 0 :
  try :
   OoOo = re . compile ( '<iframe src="(.+?)"' ) . findall ( I1I ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in OoOo :
   ii ( OOO0OOO00oo , OoOo , Iii111II )
  OOooooO0Oo = oOO00oOO ( OoOo )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = 'https:' + url
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  xbmc . Player ( ) . play ( url , OO , False )
  quit ( 0 )
 if oOOoo0Oo == 1 :
  try :
   OoOo = re . compile ( '<iframe src="(.+?)"' ) . findall ( I1I ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   oOooOo0 ( url )
  OOooooO0Oo = oOO00oOO ( OoOo )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = 'https:' + url
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  xbmc . Player ( ) . play ( url , OO , False )
  quit ( 0 )
  if 25 - 25: i1
def oOo0oO ( ) :
 if 51 - 51: ooo0Oo0 - OOo0o0 + i11Ii11I1Ii1i * OOooO . iI1 + OOo0o0
 oo0oooooO0 = 'http://m.liveatc.net/feeds/'
 I1I = OoO0o ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li>(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://m.liveatc.net' + oo0oooooO0
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 7 , I1IiI , Oo , '' )
  if 78 - 78: OOo0o0 % O0 % OOooO
def iiI1Ii1iI1 ( url ) :
 if 87 - 87: ooo0Oo0 . I1iiiiI1iII
 if 75 - 75: i1Ii + Oooo0000 + i1IIi11111i * iI1 % OOo0o0 . OOoO00o
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li>(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 55 - 55: OOoOoo00oo . iiI1iIiI
def oOo0O0o00o ( url ) :
 url = url . replace ( ' ' , '%20' )
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li>(.+?)</a>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '(.+?)</li>' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 64 - 64: OOoOoo00oo % iIii1I11I1II1 * OOo0o0
def o0iI11I1II ( url ) :
 if 40 - 40: iIii1I11I1II1 / Oooo0000 % o000o0o00o0Oo + i11Ii11I1Ii1i
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li>(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  try :
   i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
   i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   i1IiIiiI ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 27 - 27: i11Ii11I1Ii1i * Oooo0000 * iIii1I11I1II1
def oOo00oOoO000 ( ) :
 if 93 - 93: i1IIi11111i % i1IIi . OOooO . i11iIiiIii
 iiii11I ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 oo0oooooO0 = 'http://m.broadcastify.com/?a=la&coid=1'
 I1I = OoO0o ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://m.broadcastify.com' + oo0oooooO0
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 12 , I1IiI , Oo , '' )
  if 56 - 56: o000o0o00o0Oo % O0 - iiI1iIiI
def O00o0OO0 ( url ) :
 if 35 - 35: OOo0o0 % i1Ii / oOo0 + iIii1I11I1II1 . OoooooooOO . iiI1iIiI
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 71 - 71: I1iiiiI1iII * i11Ii11I1Ii1i * OOo0o0
def oOOo0 ( url ) :
 if 16 - 16: OOo0o0 % o000o0o00o0Oo * i11iIiiIii % i11iIiiIii
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 65 - 65: OOooO - OOo0o0 + OOo0o0 + i11Ii11I1Ii1i
def o0oooOOoOo0 ( url ) :
 if 74 - 74: iIii1I11I1II1 * o000o0o00o0Oo + Oooo0000 / i1IIi / i11Ii11I1Ii1i . ooo0Oo0
 I1I = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  OoOo = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( I1I ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 oooOo0OOOoo0 ( OoOo )
 if 51 - 51: ooo0Oo0 / Oooo0000 . OOoOoo00oo * i1IIi11111i + i1 * I1iiiiI1iII
def OOOoOo ( ) :
 if 51 - 51: i1Ii / iIii1I11I1II1 % ooo0Oo0 * iiI1iIiI % oOo0
 oo0oooooO0 = 'http://m.broadcastify.com/?a=top25'
 I1I = OoO0o ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  oOoooOOO = i11I1iIiII . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  i11I1iIiII = i11I1iIiII . split ( ')' ) [ - 1 ] . strip ( )
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://m.broadcastify.com' + oo0oooooO0
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[COLOR yellow] :: " + oOoooOOO + " Listening" + "[/COLOR]" , oo0oooooO0 , 14 , I1IiI , Oo , '' )
  if 52 - 52: OoooooooOO - i1Ii
def o0O0o0 ( url ) :
 if 37 - 37: o000o0o00o0Oo * iI1 % i11iIiiIii % i1Ii + OOooO
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( ii11i1 ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( ii11i1 ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in i11I1iIiII :
    ooOO0O0ooOooO = 'https://www.youtube.com' + url
    i1IiIiiI ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , ooOO0O0ooOooO , 2 , I1IiI , I1ii11iIi11i )
    if 11 - 11: iiI1iIiI
def I1111i ( ) :
 if 14 - 14: OOoOoo00oo / i1IIi11111i
 oo0oooooO0 = 'http://burningwhee1s.blogspot.co.uk/'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( OoOo )
 for I1I , i11I1iIiII in I1I1I :
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , I1I , 24 , I1IiI , Oo , '' )
  if 32 - 32: iiI1iIiI * ooo0Oo0
def O0OooOo0o ( url ) :
 if 29 - 29: iiI1iIiI % iiI1iIiI
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 94 - 94: iIii1I11I1II1 / ooo0Oo0 % OOoO00o * OOoO00o * i11Ii11I1Ii1i
def IIiIiI ( url , iconimage ) :
 if 94 - 94: OOo0o0 . i1IIi - i1IIi11111i % O0 - i1
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( OoOo )
 try :
  for ii11i1 in I1I1I :
   i11I1iIiII = re . compile ( '<b>(.+?)</b>' ) . findall ( ii11i1 ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    ooO0O00Oo0o = re . compile ( '<b>(.+?)</b>' ) . findall ( ii11i1 ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     ooO0O00Oo0o = re . compile ( '<b>(.+?)</b>' ) . findall ( ii11i1 ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     ooO0O00Oo0o = ''
   i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
   ooO0O00Oo0o = OOoOO0o0o0 ( ooO0O00Oo0o )
   OOOOo0o00OO0000 = re . compile ( '<option value="(.+?)"' ) . findall ( ii11i1 ) [ 1 ]
   i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "  " + ooO0O00Oo0o + "[/COLOR]" , OOOOo0o00OO0000 , 2 , I1IiI , Oo , '' )
 except :
  i1IiIiiI ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 1 - 1: i1Ii . i1Ii / Oooo0000 - oOo0
def oooO ( ) :
 if 26 - 26: OOooO % o000o0o00o0Oo
 if 76 - 76: I1iiiiI1iII * OOoO00o
 oo0oooooO0 = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 I1I = oOO00oOO ( oo0oooooO0 )
 Ooo0OO0oOO = json . loads ( I1I )
 ooooooo00o = Ooo0OO0oOO [ 'results' ]
 for o0oooOO00 in ooooooo00o :
  iiIiii1IIIII = 'https://image.tmdb.org/t/p/original'
  i11I1iIiII = o0oooOO00 [ 'title' ]
  I1IiI = o0oooOO00 [ 'poster_path' ]
  o00o = o0oooOO00 [ 'id' ]
  I1IiI = iiIiii1IIIII + I1IiI
  I1ii11iIi11i = o0oooOO00 [ 'backdrop_path' ]
  I1ii11iIi11i = iiIiii1IIIII + I1ii11iIi11i
  IIIIiiIiiI = o0oooOO00 [ 'overview' ]
  o00o = str ( o00o )
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , i11I1iIiII , 33 , I1IiI , I1ii11iIi11i , IIIIiiIiiI )
  if 10 - 10: Oooo0000 % Oooo0000 - Oooo0000 . OOoO00o
def o0OoOo00o0o ( url ) :
 if 41 - 41: i1Ii % i1 - ooo0Oo0 * oOo0 * ooo0Oo0
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = re . compile ( '<i>(.+?)</i>' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = i11I1iIiII . strip ( )
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  OOOoOO0o = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( I1I ) [ 0 ]
  i1II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  iiii11I ( '[COLOR yellow]Next Page >>[/COLOR]' , OOOoOO0o , 26 , i1II1 , I1ii11iIi11i )
 except : pass
 if 25 - 25: oOo0 / iIii1I11I1II1 % OOoO00o
def IiiiiI1i1Iii ( url , iconimage ) :
 if 87 - 87: i1IIi11111i
 I1I = oOO00oOO ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( I1I ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 OoOo = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( I1I )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 oO0000OOo00 = 1
 IiI1iiiIii = [ ]
 for ii11i1 in OoOo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  IiI1iiiIii . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( oO0000OOo00 ) )
  time . sleep ( 0.02 )
  oO0000OOo00 += 1
  i11I1iIiII = re . compile ( '(.+?)</p>' ) . findall ( ii11i1 ) [ 0 ] . replace ( 'Server' , '' )
  i11I1iIiII = i11I1iIiII . strip ( )
 I1III1111iIi = 1
 I1i1I1II = 0
 I1i111I = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 97 - 97: i1IIi . OOo0o0 / OOoO00o * O0
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if I1i1I1II > len ( IiI1iiiIii ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 73 - 73: OOoOoo00oo / OOo0o0
  if I1i111I == 0 :
   I1i1I1II += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( I1i1I1II ) + "[/COLOR]" , '' )
   try :
    I1I = oOO00oOO ( IiI1iiiIii [ I1i1I1II ] )
    I1I1I = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( I1I ) [ 0 ]
    o0OO0o0o00o = base64 . b64decode ( I1I1I )
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0OO0o0o00o ) [ 0 ]
    oOo0OOOoOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    I11IIIi = open ( oOo0OOOoOO ) . read ( )
    iIIiiI1II1i11 = re . compile ( '<url>(.+?)</url>' ) . findall ( I11IIIi )
    for o0o0 in iIIiiI1II1i11 :
     IIii1111 = re . compile ( '<bad>(.+?)<bad>' ) . findall ( o0o0 ) [ 0 ]
     if url == IIii1111 :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( I1i1I1II ) )
      time . sleep ( 0.5 )
      I1i111I = 5
      pass
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     I1iI = liveresolver . resolve ( url )
    else : I1iI = url
    OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( I1iI , OO , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( I1i1I1II ) )
    time . sleep ( 0.5 )
    I1i111I = 5
    pass
  if I1i111I == 5 :
   I1i111I = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   I1i111I += 1
   if 38 - 38: OOo0o0 % Oooo0000 + o000o0o00o0Oo . i11iIiiIii
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 oOo0OOOoOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 O0iII = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if O0iII :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( oOo0OOOoOO , "a" ) as oo0000ooooO0o :
   oo0000ooooO0o . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 40 - 40: o000o0o00o0Oo + i1IIi * OOoOoo00oo
def O0oOOoooOO0O ( url ) :
 if 86 - 86: i1IIi11111i
 if 5 - 5: I1iiiiI1iII * Oooo0000
 if url == 'search' :
  i1Ii1i1I11Iii = ''
  I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , 'Enter Search Term' )
  I1i1i1 . doModal ( )
  if I1i1i1 . isConfirmed ( ) :
   i1Ii1i1I11Iii = I1i1i1 . getText ( )
   if len ( i1Ii1i1I11Iii ) > 1 :
    OoO0O00O0oo0O = i1Ii1i1I11Iii . lower ( )
    if 36 - 36: OOoOoo00oo + O0 - OOooO - O0 % iI1 . OOo0o0
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , Iii111II , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , Iii111II , 5000 )
   quit ( )
  OoO0O00O0oo0O = OoO0O00O0oo0O . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + OoO0O00O0oo0O + '.html'
  ooo ( url , I1IiI )
  if 36 - 36: OoooooooOO . i1
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  ooo ( url , I1IiI )
  if 56 - 56: ooo0Oo0 . o000o0o00o0Oo . iiI1iIiI
def ooo ( url , icon ) :
 if 39 - 39: O0 + oOo0
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = re . compile ( '<i>(.+?)</i>' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 91 - 91: OoooooooOO - iIii1I11I1II1 + Oooo0000 / i1 . Oooo0000 + O0
def iIiii1iI1 ( ) :
 if 33 - 33: I1iiiiI1iII % iIii1I11I1II1 * iiI1iIiI
 oo0oooooO0 = 'http://www.genti.stream/'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( I1I )
 for ii11i1 in OoOo :
  o00o0 = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ] . strip ( )
  II1III1I1I1Ii = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( ii11i1 ) [ 1 ] . strip ( )
  oo0oooooO0 = re . compile ( 'href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://www.genti.stream/' + oo0oooooO0
  i1IiIiiI ( "[COLOR aqua]" + o00o0 + "[COLOR yellow] vs [COLOR aqua]" + II1III1I1I1Ii + "[/COLOR]" , oo0oooooO0 , 39 , I1IiI , I1ii11iIi11i )
  if 70 - 70: i1 % OOo0o0 + OOoOoo00oo / OOooO % O0
def oO00O0 ( url ) :
 if 36 - 36: OOo0o0 - OOooO . ooo0Oo0 - i11iIiiIii - OOoOoo00oo * ooo0Oo0
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OooOOOO = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( I1I ) [ 0 ]
 if not 'http' in OooOOOO :
  OooOOOO = 'http://www.genti.stream' + OooOOOO
 OoOO000 = oOO00oOO ( OooOOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iIIIiiI1i1i = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OoOO000 ) [ 0 ]
 OOooooO0Oo = oOO00oOO ( iIIIiiI1i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( OOooooO0Oo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( OOooooO0Oo ) [ 0 ]
 except : pass
 if 32 - 32: Oooo0000 / i1 + OOoOoo00oo
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , Iii111II , 5000 )
  quit ( )
 ii ( OOO0OOO00oo , url , Iii111II )
 if 32 - 32: iIii1I11I1II1 % OOoO00o
 if 65 - 65: i1Ii . OoooooooOO / o000o0o00o0Oo . i1IIi * i1
def IiIiII1 ( url ) :
 if 21 - 21: O0 % I1iiiiI1iII . iiI1iIiI / i11Ii11I1Ii1i + I1iiiiI1iII
 OOOO0O00o = cfscrape . create_scraper ( )
 i11Iiii = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( i11Iiii ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOo )
 for url , i11I1iIiII in I1I1I :
  url = 'http://kimcartoon.me/CartoonList' + url
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 62 - 62: iIii1I11I1II1
def i1II ( url ) :
 if 14 - 14: OOo0o0 / OOo0o0 % i1Ii
 OOOO0O00o = cfscrape . create_scraper ( )
 i11Iiii = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( i11Iiii )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   ooO = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( ii11i1 ) [ 0 ]
   ooO = OOoOO0o0o0 ( ooO )
  except IndexError :
   ooO = ''
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , ooO )
  if 6 - 6: iIii1I11I1II1 . i1Ii % i1IIi11111i
 try :
  I1Iii1 = re . compile ( '<li>(.+?)Next' ) . findall ( i11Iiii )
  for ii11i1 in I1Iii1 :
   OOOoOO0o = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ - 1 ]
   iiI11Iii = 'http://kimcartoon.me' + OOOoOO0o
   O0o0O0 = 'https://i.imgur.com/pOefPvV.jpg'
   iiii11I ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , iiI11Iii , 30 , O0o0O0 , I1ii11iIi11i )
 except : pass
 if 11 - 11: i11Ii11I1Ii1i % i1 * OOoO00o + i1Ii + OOooO
def II1Iiiiii ( url ) :
 if 36 - 36: iiI1iIiI - iI1
 OOOO0O00o = cfscrape . create_scraper ( )
 i11Iiii = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<td>(.+?)</td>' ) . findall ( i11Iiii )
 for ii11i1 in OoOo :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
   i11I1iIiII = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   i1IiIiiI ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 29 - 29: i1Ii * OOoOoo00oo
def I111i1i1111 ( url ) :
 if 49 - 49: i1 / OOo0o0 + O0 * i1IIi11111i
 oOOoo0Oo = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if oOOoo0Oo == 0 :
  url = url + '&s=rapidvideo'
  OOOO0O00o = cfscrape . create_scraper ( )
  i11Iiii = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1I1I = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i11Iiii )
   for I1I in I1I1I :
    url = re . compile ( 'src="(.+?)"' ) . findall ( I1I ) [ 0 ]
    if 'rapidvideo' in url :
     ii ( OOO0OOO00oo , url , Iii111II )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if oOOoo0Oo == 1 :
  url = url + '&s=openload'
  OOOO0O00o = cfscrape . create_scraper ( )
  i11Iiii = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1I1I = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i11Iiii )
   for I1I in I1I1I :
    url = re . compile ( 'src="(.+?)"' ) . findall ( I1I ) [ 0 ]
    ii ( OOO0OOO00oo , url , Iii111II )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 28 - 28: i1Ii + i11iIiiIii / iI1 % Oooo0000 % ooo0Oo0 - O0
   if 54 - 54: i1IIi + i11Ii11I1Ii1i
def oOOO0oo0 ( ) :
 if 46 - 46: I1iiiiI1iII
 oo0oooooO0 = "http://www.loyalbooks.com/genre-menu"
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( I1I )
 for iIo00O in OoOo :
  if "paid" not in iIo00O :
   OoOO000 = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
   OOooooO0Oo = "http://www.loyalbooks.com" + OoOO000
   OOO0OOO00oo = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
   iiii11I ( "[COLOR aqua]" + OOO0OOO00oo + "[/COLOR]" , OOooooO0Oo , 60 , I1IiI , Oo , '' )
   if 45 - 45: i1Ii
def IIi ( url ) :
 if 94 - 94: i11Ii11I1Ii1i - ooo0Oo0
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 oo0oO0 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( OoOo )
 for iIo00O in oo0oO0 :
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  OOooooO0Oo = "http://www.loyalbooks.com" + ooOO0O0ooOooO
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  Iii111II = "http://www.loyalbooks.com" + I1IiI
  OOO0OOO00oo = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + OOO0OOO00oo + "[/COLOR]" , OOooooO0Oo , 61 , Iii111II , Oo , '' )
 try :
  I1I = oOO00oOO ( url )
  I1I11 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  I1IiI = 'https://i.imgur.com/pOefPvV.jpg'
  iiii11I ( "[COLOR yellow]Next Page -->[/COLOR]" , I1I11 , 60 , I1IiI , Oo , '' )
 except : pass
 if 1 - 1: i1IIi . i11iIiiIii % OOoOoo00oo
 if 82 - 82: iIii1I11I1II1 + ooo0Oo0 . iIii1I11I1II1 % I1iiiiI1iII / OOooO . OOooO
def IIioOoO00oo0O ( name , url , iconimage ) :
 if 39 - 39: iIii1I11I1II1 / O0 / OOo0o0 - OOooO - OOoO00o % OOoOoo00oo
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( I1I )
 for iIo00O in OoOo :
  i11I1iIiII = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , ooOO0O0ooOooO , 10 , iconimage , Oo , '' )
  if 31 - 31: iI1 - O0 / i1Ii * Oooo0000
def iI111i1II ( ) :
 if 69 - 69: OOooO * O0 . i11iIiiIii / OOooO . i1IIi11111i
 oo0oooooO0 = 'http://www.shadownet.me/'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOo )
 for oo0oooooO0 , i11I1iIiII in I1I1I :
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  if 'P2P' not in i11I1iIiII :
   iiii11I ( "[COLOR skyblue]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 49 , I1IiI , Oo , '' )
   if 63 - 63: iI1 + i1IIi11111i . i11Ii11I1Ii1i - iiI1iIiI
   if 52 - 52: i1IIi11111i % ooo0Oo0
def Oo000ooOOO ( url ) :
 if 31 - 31: iIii1I11I1II1 % iI1 % i1Ii . OOooO - iI1
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( OoOo )
 for ii11i1 in I1I1I :
  i11I1iIiII = re . compile ( 'alt="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i1IiIiiI ( "[COLOR skyblue]" + i11I1iIiII + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  OOOoOO0o = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  iiii11I ( "[COLOR orange]Next Page --->[/COLOR]" , OOOoOO0o , 49 , I1IiI , Oo , '' )
 except : pass
 if 17 - 17: OOooO
def Ii1ii1IiIII ( url ) :
 if 57 - 57: iIii1I11I1II1 / iI1 - i1IIi
 def ooOOo00O00Oo ( url ) :
  IiII1 = urllib2 . Request ( url )
  IiII1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  IiII1 . add_header ( 'Referer' , url )
  I1iIi1iIiiIiI = urllib2 . urlopen ( IiII1 , timeout = 5 )
  I1I = I1iIi1iIiiIiI . read ( )
  I1iIi1iIiiIiI . close ( )
  return I1I
  if 47 - 47: OOooO + oOo0 / i1IIi % i11iIiiIii
 I1I = ooOOo00O00Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  OoOo = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( I1I ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in OoOo :
  url = OoOo
  ii ( OOO0OOO00oo , url , Iii111II )
 OOooooO0Oo = ooOOo00O00Oo ( OoOo )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 42 - 42: OOoO00o + I1iiiiI1iII
 import liveresolver
 import resolveurl
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  OO . setPath ( I1iI )
  xbmc . Player ( ) . play ( I1iI , OO , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  OO . setPath ( I1iI )
  xbmc . Player ( ) . play ( I1iI , OO , False )
 else :
  if '.m3u8' in url :
   ooOO0O0ooOooO = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + OOO0OOO00oo + '&amp;url=' + url + '&amp;iconImage=' + Iii111II
  elif '.ts' in url :
   ooOO0O0ooOooO = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + OOO0OOO00oo + '&amp;url=' + url + '&amp;iconImage=' + Iii111II
  else :
   ooOO0O0ooOooO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 96 - 96: OOoOoo00oo
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  OO . setPath ( url )
  if 85 - 85: i1IIi11111i . Oooo0000 / i1Ii . O0 % oOo0
  xbmc . Player ( ) . play ( ooOO0O0ooOooO , OO , False )
  if 90 - 90: ooo0Oo0 % O0 * iIii1I11I1II1 . OOoO00o
  if 8 - 8: i1Ii + i11Ii11I1Ii1i / OOoO00o / iI1
def ooo0O ( ) :
 if 16 - 16: Oooo0000
 oo0oooooO0 = 'https://m.skylinewebcams.com/en/webcam'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I1I = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 Iiiiii111i1ii = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I1I )
 for oo0oooooO0 , i11I1iIiII in Iiiiii111i1ii :
  if 'http|https' not in oo0oooooO0 :
   oo0oooooO0 = 'https://m.skylinewebcams.com' + oo0oooooO0
   iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 46 , I1IiI , Oo , '' )
   if 25 - 25: OOoOoo00oo - i1Ii / i11iIiiIii
def iiI1ii11i1 ( url ) :
 if 38 - 38: o000o0o00o0Oo - OOoO00o / O0 . oOo0
 I1I = oOO00oOO ( url )
 I1I1I = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( I1I )
 for url , I1IiI , i11I1iIiII in I1I1I :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 45 - 45: oOo0
  if 83 - 83: Oooo0000 . OoooooooOO
def Oo0ooo ( name , url , iconimage ) :
 if 28 - 28: OOo0o0 . i11Ii11I1Ii1i / o000o0o00o0Oo + i11Ii11I1Ii1i . OoooooooOO . I1iiiiI1iII
 I1I = oOO00oOO ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  OoOo = re . compile ( '<amp-video src="(.+?)"' ) . findall ( I1I ) [ 0 ]
  url = 'https:' + OoOo
  OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , OO , False )
  if 53 - 53: OOooO % OOooO * i1IIi11111i + Oooo0000
 except : pass
 quit ( 0 )
 if 92 - 92: OoooooooOO + i1IIi / OOooO * O0
def O00oOo00o0o ( ) :
 if 85 - 85: OOoO00o + OoooooooOO * OOoO00o - oOo0 % i11iIiiIii
 oo0oooooO0 = 'http://www.watchepisodeseries.com/home/schedule'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( OoOo )
 for oo0oooooO0 , OOo00OoO , iIi1 in I1I1I :
  iiii11I ( "[COLOR aqua]" + OOo00OoO + "  " + iIi1 + "[/COLOR]" , oo0oooooO0 , 67 , I1IiI , I1ii11iIi11i )
  if 21 - 21: iI1
  if 92 - 92: i11iIiiIii / oOo0 - OOoO00o % i1Ii * oOo0 + ooo0Oo0
def ii1 ( url ) :
 if 80 - 80: OoooooooOO - OOoOoo00oo * OOooO * o000o0o00o0Oo / iiI1iIiI / OOoOoo00oo
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 1 ]
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  Iii111II = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( ii11i1 ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 68 , Iii111II , I1ii11iIi11i )
  if 13 - 13: oOo0 * i1Ii + i11iIiiIii * oOo0 - i1Ii
  if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * I1iiiiI1iII
def I1Iiiiiii ( url , iconimage , fanart ) :
 if 39 - 39: I1iiiiI1iII * ooo0Oo0 + iIii1I11I1II1 - I1iiiiI1iII + OOoOoo00oo
 I1I = oOO00oOO ( url )
 o0iiiI1I1iIIIi1 = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in o0iiiI1I1iIIIi1 :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
 OoOo = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( I1I )
 oO0000OOo00 = datetime . now ( )
 for ii11i1 in OoOo :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
   i11I1iIiII = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ]
   i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
   Iii = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ]
   I1iiiiI1iI = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ]
   OOo00OoO = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in OOo00OoO :
    OOo00OoO = OOo00OoO . strip ( )
    OOo00OoO = time . strptime ( OOo00OoO , "%d/%m/%Y" )
    iIiiiii1i = ( "%s/%s/%s" % ( oO0000OOo00 . day , oO0000OOo00 . month , oO0000OOo00 . year ) )
    iIiiiii1i = time . strptime ( iIiiiii1i , "%d/%m/%Y" )
    if ( iIiiiii1i < OOo00OoO ) :
     i11I1iIiII = '[COLOR yellow]' + ( i11I1iIiII ) + ' - Not Aired Yet' + '[/COLOR]'
     I1iiiiI1iI = '[COLOR yellow]' + ( I1iiiiI1iI ) + '[/COLOR]'
     Iii = '[COLOR yellow]' + ( Iii ) + '[/COLOR]'
     if 40 - 40: O0 - OoooooooOO - I1iiiiI1iII
    if not 'Season 0' in Iii :
     iiii11I ( "[COLOR aqua]" + Iii + " " + I1iiiiI1iI + " " + i11I1iIiII + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 37 - 37: Oooo0000 / i11Ii11I1Ii1i / O0
  if 76 - 76: iiI1iIiI . i1Ii - o000o0o00o0Oo - OOoO00o * i1
def O0Oo00O ( url , iconimage , fanart ) :
 if 91 - 91: OOo0o0 % OOooO . i1Ii / OOoO00o * iIii1I11I1II1
 if 43 - 43: i1Ii + OOoO00o - oOo0 / O0 * ooo0Oo0 + iiI1iIiI
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( I1I )
 for ii11i1 in OoOo :
  try :
   i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
   i11I1iIiII = i11I1iIiII . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
   if not 'Lolzor.Com' in i11I1iIiII :
    if not 'Videoplayer.Gq' in i11I1iIiII :
     if not 'Vidbaba.Com' in i11I1iIiII :
      if not 'Gagomatic.Com' in i11I1iIiII :
       if not 'Favour.Me' in i11I1iIiII :
        if not 'Funblr.Com' in i11I1iIiII :
         if not 'Vid.Ag' in i11I1iIiII :
          if not 'Mycollection.Net' in i11I1iIiII :
           if not 'Adhqmedia.Com' in i11I1iIiII :
            if not 'Filenuke.Com' in i11I1iIiII :
             if not 'Mrfile.Me' in i11I1iIiII :
              i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 28 - 28: OOooO * i1IIi11111i - i1
  if 42 - 42: o000o0o00o0Oo
def OOooOOOOOOooo ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  url = re . compile ( 'href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  import resolveurl
  try :
   if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
    I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    I1iI = liveresolver . resolve ( url )
   else : I1iI = url
   OO = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   OO . setPath ( I1iI )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO )
   xbmc . Player ( ) . play ( I1iI )
   if 61 - 61: I1iiiiI1iII . i1IIi / oOo0 % i11iIiiIii * OOoO00o
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 31 - 31: OOoOoo00oo + O0
def oO0oOOoo00000 ( ) :
 if 52 - 52: iiI1iIiI
 i1Ii1i1I11Iii = ''
 I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , 'Enter Search Term' )
 I1i1i1 . doModal ( )
 if I1i1i1 . isConfirmed ( ) :
  i1Ii1i1I11Iii = I1i1i1 . getText ( )
  if len ( i1Ii1i1I11Iii ) > 1 :
   OoO0O00O0oo0O = i1Ii1i1I11Iii . lower ( )
   OoO0O00O0oo0O = OoO0O00O0oo0O . replace ( ' ' , '%20' )
   if 51 - 51: I1iiiiI1iII
  else : quit ( )
 else : OoO0O00O0oo0O = urllib . unquote_plus ( oo0oooooO0 ) . lower ( ) ; i1Ii1i1I11Iii = urllib . unquote_plus ( oo0oooooO0 )
 oo0oooooO0 = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + OoO0O00O0oo0O
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '"series"(.+?)"series_id"' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( 'original_name":"(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( '"seo_name":"(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://www.watchepisodeseries.com/' + ooOO0O0ooOooO
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + ooOO0O0ooOooO + '.jpg'
  iiii11I ( i11I1iIiII , oo0oooooO0 , 68 , I1IiI , I1ii11iIi11i , '' )
  if 88 - 88: OoooooooOO
def OO00 ( ) :
 if 28 - 28: OOo0o0 - i11iIiiIii . o000o0o00o0Oo + I1iiiiI1iII / o000o0o00o0Oo
 oo0oooooO0 = 'http://www.watchepisodeseries.com/home/popular-series'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<div title="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  iiii11I ( '[COLOR aqua]' + i11I1iIiII + '[/COLOR]' , oo0oooooO0 , 68 , I1IiI , I1ii11iIi11i )
  if 35 - 35: I1iiiiI1iII
  if 75 - 75: ooo0Oo0 / o000o0o00o0Oo . I1iiiiI1iII * OOoOoo00oo - i11Ii11I1Ii1i
def i1i1IIii1i1 ( ) :
 if 65 - 65: iiI1iIiI + Oooo0000 / OOoOoo00oo
 try :
  oOO = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1Ii1i1I11Iii = ''
  I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  I1i1i1 . doModal ( )
  if I1i1i1 . isConfirmed ( ) :
   i1Ii1i1I11Iii = I1i1i1 . getText ( )
   if len ( i1Ii1i1I11Iii ) > 1 :
    OoO0O00O0oo0O = i1Ii1i1I11Iii
   else : quit ( )
  if OoO0O00O0oo0O == oOO :
   oOooo0O0o ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  i1Ii1i1I11Iii = ''
  I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , 'Enter The Password You Set' )
  I1i1i1 . doModal ( )
  if I1i1i1 . isConfirmed ( ) :
   i1Ii1i1I11Iii = I1i1i1 . getText ( )
   if len ( i1Ii1i1I11Iii ) > 1 :
    OoO0O00O0oo0O = i1Ii1i1I11Iii
   else : quit ( )
  with open ( i1i1II , "w" ) as oo0000ooooO0o :
   oo0000ooooO0o . write ( OoO0O00O0oo0O )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 72 - 72: iIii1I11I1II1 / I1iiiiI1iII % OOoO00o % OOoOoo00oo - iI1 % OOoOoo00oo
   if 100 - 100: ooo0Oo0 + i11iIiiIii
   if 71 - 71: iI1 / i1IIi11111i / oOo0 % OOoOoo00oo
def oOooo0O0o ( ) :
 if 51 - 51: I1iiiiI1iII * O0 / i11Ii11I1Ii1i . OOooO % OOoOoo00oo / iiI1iIiI
 ii1iii1I1I = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 oO0Ooo0ooOO0 = '[COLOR aqua]Asian Special Porn[/COLOR]'
 iiii11I ( oO0Ooo0ooOO0 , ii1iii1I1I , 1 , I1IiI , Oo , '' )
 oo0oooooO0 = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<li class="">(.+?)</li>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<strong>(.+?)</strong>' ) . findall ( ii11i1 ) [ 0 ]
  i1IIiIii1i = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'https://www.eporner.com' + ooOO0O0ooOooO
  if not 'All' in i11I1iIiII :
   if not 'Homemade' in i11I1iIiII :
    iiii11I ( "[COLOR aqua]" + i11I1iIiII + "  " + "[COLOR yellow]" + i1IIiIii1i + "[/COLOR]" , oo0oooooO0 , 36 , I1IiI , Oo , '' )
    if 77 - 77: O0 % OOo0o0 - i1
def ooi1i1I ( url ) :
 if 25 - 25: iIii1I11I1II1 + o000o0o00o0Oo + OOoO00o / i11Ii11I1Ii1i / iI1
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( 'title="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = 'https://www.eporner.com' + ooOO0O0ooOooO
  iiii11I ( "[COLOR skyblue]" + i11I1iIiII + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 60 - 60: i1Ii * oOo0 + ooo0Oo0
 try :
  OOOoOO0o = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( I1I ) [ 0 ]
  I1I11 = 'https://www.eporner.com' + OOOoOO0o
  i1II1 = 'http://imgur.com/3eNoY0p'
  iiii11I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1I11 , 36 , i1II1 , Oo , '' )
 except : pass
 if 19 - 19: i1 * iI1 / iI1 . OoooooooOO - OOoOoo00oo + i11iIiiIii
def oo0OOo0O ( url , iconimage ) :
 if 39 - 39: OoooooooOO + OOo0o0 % OOoOoo00oo / OOoOoo00oo
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1i = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( I1i )
 for oooii1iiIi1 , I1I in I1I1I :
  oooii1iiIi1 = oooii1iiIi1 . replace ( ':' , '' )
  url = 'https://www.eporner.com' + I1I
  i1IiIiiI ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + oooii1iiIi1 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 34 - 34: OOoOoo00oo
def OooO0ooo0o ( url ) :
 if 47 - 47: OoooooooOO
 OOOO0O00o = cfscrape . create_scraper ( )
 I1I = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI ( "[COLOR yellow]Anime Catergories[/COLOR]" , url , 999 , I1IiI , Oo , '' )
 if 4 - 4: iiI1iIiI % iI1
 OoOo = re . compile ( '<ul class="nav nav-pills nav-stacked">(.+?)</ul>' ) . findall ( I1I ) [ 1 ]
 I1I1I = re . compile ( '<a href="(.+?)" title="(.+?)">.+?</a>' ) . findall ( OoOo )
 for url , i11I1iIiII in I1I1I :
  i11I1iIiII = i11I1iIiII . strip ( )
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 52 , I1IiI , Oo , '' )
  if 10 - 10: I1iiiiI1iII . OoooooooOO - i1 + I1iiiiI1iII - O0
def o0oO00 ( url ) :
 if 65 - 65: OOoOoo00oo . oOo0 . i1 . OOoO00o - OOoOoo00oo
 OOOO0O00o = cfscrape . create_scraper ( )
 I1I = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo = re . compile ( '<th class="st-sort-descent">(.+?)</table>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)".+?>(.+?)</a>' ) . findall ( OoOo )
 for url , i11I1iIiII in I1I1I :
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 19 - 19: i11iIiiIii + OOoO00o % i1Ii
def IIii11II11II1 ( url ) :
 if 10 - 10: iiI1iIiI / ooo0Oo0 % o000o0o00o0Oo * i1Ii
 OOOO0O00o = cfscrape . create_scraper ( )
 I1I = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1IiI = re . compile ( '''<div class=\"col-md-3\">.+?url\('(.+?)'\)''' ) . findall ( I1I ) [ 0 ]
 except :
  I1IiI = Iii111II
 OoOo = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '''<a class=".*?window.location='(.*?)'.*?>(.*?)<''' ) . findall ( OoOo )
 i1IiIiiI ( "[COLOR yellow]Links Can Take Up To 45 Secs To Play, Be Patient![/COLOR]" , url , 54 , I1IiI , Oo , '' )
 for url , i11I1iIiII in I1I1I :
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  if 6 - 6: OOoO00o . I1iiiiI1iII * Oooo0000 . i1IIi
def oOOo ( url , iconimage ) :
 if 46 - 46: I1iiiiI1iII + iIii1I11I1II1 + OOoOoo00oo + i1 . o000o0o00o0Oo
 OOOO0O00o = cfscrape . create_scraper ( )
 I1I = OOOO0O00o . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOOOo0o00OO0000 = re . compile ( '<source src="(.+?)"' ) . findall ( I1I ) [ 0 ]
 ii ( OOO0OOO00oo , OOOOo0o00OO0000 , iconimage )
 if 1 - 1: OOo0o0
 if 62 - 62: i1IIi - OOoOoo00oo
 if 96 - 96: i1IIi . o000o0o00o0Oo + OOo0o0
 if 48 - 48: iIii1I11I1II1 % i1IIi % OOoO00o + i1Ii
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . iI1 % iIii1I11I1II1
 if 62 - 62: ooo0Oo0 * Oooo0000
 if 79 - 79: i1 . OOoO00o * OOooO - OOoOoo00oo + i1Ii
 if 14 - 14: i11iIiiIii - OOoO00o * Oooo0000
def OO0o ( url ) :
 if 39 - 39: i1IIi11111i * i1Ii + OOooO * i11Ii11I1Ii1i
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( 'title="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( './' , '/' )
  if 97 - 97: iIii1I11I1II1 + iI1 + i11Ii11I1Ii1i % I1iiiiI1iII % oOo0 % OOo0o0
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  oooii1iiIi1 = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[COLOR yellow] " + oooii1iiIi1 + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 21 - 21: iiI1iIiI / i1Ii % i1Ii - i1IIi11111i
 try :
  I1I11 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( I1I ) [ 0 ]
  OOOoOO0o = re . compile ( '<a.+?href="(.+?)"' ) . findall ( I1I11 ) [ 5 ]
  if 'genre' in OOOoOO0o :
   oOOO00o00O = oOOO00o00O . replace ( '.com' , '.com/' )
  ii1iii11i1 = I1IiI
  iiii11I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OOOoOO0o , 42 , ii1iii11i1 , Oo , description = '' )
 except : pass
 if 4 - 4: I1iiiiI1iII . I1iiiiI1iII % o000o0o00o0Oo % OOooO / OOooO
def II11iIiiI1111 ( url , iconimage ) :
 if 71 - 71: i1IIi11111i % OOooO - i11Ii11I1Ii1i * OoooooooOO
 import requests
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOOO = re . compile ( 'data="(.+?)"' ) . findall ( I1I )
 ooo0oooo0 = 'http://m4ufree.com/ajax_new.php'
 for Ooo0OO0oOO in oOOO :
  try :
   ooo0oooo0 = 'http://m4ufree.com/ajax_new.php'
   OOO0ooo = requests . post ( ooo0oooo0 , data = { 'm4u' : Ooo0OO0oOO } )
   json = ( OOO0ooo . text )
   IIiiii = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
   iI111i1I1II = re . compile ( '{(.+?)}' ) . findall ( IIiiii )
   O00OO = 0
   for oO0000OOo00 in iI111i1I1II :
    O00OO += 1
    i11I1iIiII = 'Link ' + str ( O00OO )
    try :
     oooii1iiIi1 = re . compile ( '''"label":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     i11Iiii = re . compile ( '''"file":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     url = 'http://m4ufree.com/' + i11Iiii
     i1IiIiiI ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + oooii1iiIi1 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
    except :
     oooii1iiIi1 = re . compile ( """label:.+?'(.+?)'""" ) . findall ( oO0000OOo00 ) [ 0 ]
     i11Iiii = re . compile ( '''file: "(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     url = 'http://m4ufree.com/' + i11Iiii
     i1IiIiiI ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + oooii1iiIi1 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except : pass
  if 29 - 29: ooo0Oo0 % i1 % I1iiiiI1iII . i1IIi11111i / OoooooooOO * i1Ii
  if 54 - 54: O0
def OOoO000O00oO ( ) :
 if 34 - 34: O0
 oo0oooooO0 = 'https://www.livefootballol.me/acestream-channel-list-2017.html'
 I1I = oOO00oOO ( oo0oooooO0 )
 I1I1I = re . compile ( '<tr>(.+?)</tr>' ) . findall ( I1I )
 for OooOOOo0 in I1I1I :
  i11I1iIiII = re . compile ( '<strong>(.+?)</strong>' ) . findall ( OooOOOo0 ) [ 0 ]
  if len ( i11I1iIiII ) == 1 or '&nbsp;' in i11I1iIiII :
   i11I1iIiII = re . compile ( '<strong>(.+?)</strong>' ) . findall ( OooOOOo0 ) [ 1 ]
  if len ( i11I1iIiII ) > 40 :
   i11I1iIiII = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( OooOOOo0 ) [ 0 ]
  oo0oooooO0 = re . compile ( '<td>(.+?)</td>' ) . findall ( OooOOOo0 ) [ 2 ]
  O0O0o0o0o = re . compile ( '<td>(.+?)</td>' ) . findall ( OooOOOo0 ) [ 3 ]
  IIIIIiI = re . compile ( '<td>(.+?)</td>' ) . findall ( OooOOOo0 ) [ 4 ]
  i11I1iIiII = i11I1iIiII . strip ( )
  oo0oooooO0 = oo0oooooO0 . strip ( )
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + ' :: [COLOR yellow]' + O0O0o0o0o + '[COLOR aqua] :: [COLOR yellow]' + IIIIIiI + ' Kbps[/COLOR]' , oo0oooooO0 , 2 , Iii111II , Oo , '' )
  if 80 - 80: iIii1I11I1II1 * oOo0 % iI1 % ooo0Oo0
def OooOO0o0 ( ) :
 if 91 - 91: OOo0o0 + OoooooooOO - i1IIi
 oo0oooooO0 = 'http://acestreamchannel.blogspot.co.uk/'
 I1I = oOO00oOO ( oo0oooooO0 )
 I1I1I = re . compile ( '<tr>(.+?)</tr>' ) . findall ( I1I )
 for ii11i1 in I1I1I :
  try :
   i11I1iIiII = re . compile ( '<td>(.+?)</td>' ) . findall ( ii11i1 ) [ 0 ]
   if len ( i11I1iIiII ) < 40 :
    oo0oooooO0 = re . compile ( 'href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
    i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 2 , Iii111II , Oo , '' )
  except : pass
def o000 ( ) :
 if 94 - 94: i1IIi11111i + O0 / iI1 . iiI1iIiI + OOoOoo00oo . iIii1I11I1II1
 oo0oooooO0 = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<td>(.+?)</td>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i1Ii11i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://www.livefootballol.me' + oo0oooooO0
  iiii11I ( "[COLOR aqua]" + i1Ii11i1i + "[/COLOR]" , oo0oooooO0 , 74 , Iii111II , Oo , '' )
  if 62 - 62: Oooo0000 / iiI1iIiI - o000o0o00o0Oo - iiI1iIiI + i11iIiiIii + i1IIi
def I1i11II ( url ) :
 if 31 - 31: OOo0o0 / I1iiiiI1iII * i1IIi11111i . i11Ii11I1Ii1i
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<a href="(.+?)"' ) . findall ( I1I )
 oooOO0OO0O = 0
 for OO0OoO0o00 in OoOo :
  if 'acestream' in OO0OoO0o00 :
   if 'http' in OO0OoO0o00 :
    oooOO0OO0O += 1
    i11I1iIiII = '[COLOR aqua]Link :: ' + str ( oooOO0OO0O ) + '[/COLOR]'
    i1IiIiiI ( i11I1iIiII , OO0OoO0o00 , 75 , Iii111II , Oo , '' )
 if oooOO0OO0O == 0 :
  i1IiIiiI ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , Iii111II , Oo , '' )
  if 78 - 78: OOooO / i11Ii11I1Ii1i % Oooo0000
def oO00OoOO ( url ) :
 if 18 - 18: i1Ii - Oooo0000 % i1IIi + O0 + i11iIiiIii + i1IIi
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( I1I ) [ 0 ]
 ii ( OOO0OOO00oo , url , Iii111II )
 if 91 - 91: Oooo0000 + i1Ii . iiI1iIiI
def O0oOoOOO0OO ( url , getphp ) :
 IiII1 = urllib2 . Request ( url )
 IiII1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 IiII1 . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 I1iIi1iIiiIiI = urllib2 . urlopen ( IiII1 , timeout = 10 )
 I1I = I1iIi1iIiiIiI . read ( )
 I1iIi1iIiiIiI . close ( )
 return I1I
 if 91 - 91: I1iiiiI1iII + Oooo0000 + i1IIi11111i - iIii1I11I1II1
 if 17 - 17: OOo0o0
 if 22 - 22: iI1 + iIii1I11I1II1
def IIIii1iiIi ( ) :
 if 63 - 63: o000o0o00o0Oo
 oo0oooooO0 = 'http://m4ufree.com/?sort=key_top&page=1&='
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( './' , '' )
  oo0oooooO0 = 'http://m4ufree.com/' + ooOO0O0ooOooO
  if not re . search ( '\d+' , i11I1iIiII ) :
   iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 42 , I1IiI , Oo )
   if 6 - 6: i1Ii / o000o0o00o0Oo
   if 57 - 57: iI1
   if 67 - 67: i1 . i1Ii
   if 87 - 87: OOo0o0 % OOooO
   if 83 - 83: i11Ii11I1Ii1i - iI1
   if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
   if 86 - 86: iIii1I11I1II1 + Oooo0000 . i11iIiiIii - OOooO
   if 51 - 51: Oooo0000
   if 14 - 14: I1iiiiI1iII % OOo0o0 % ooo0Oo0 - i11iIiiIii
   if 53 - 53: OOooO % ooo0Oo0
def OOoOO0o0o0 ( text ) :
 if 59 - 59: OOoOoo00oo % iIii1I11I1II1 . i1IIi + i11Ii11I1Ii1i * I1iiiiI1iII
 text = str ( text )
 text = text . replace ( '\\r' , '' )
 text = text . replace ( '\\n' , '' )
 text = text . replace ( '\\t' , '' )
 text = text . replace ( '\\' , '' )
 text = text . replace ( '<br />' , '\n' )
 text = text . replace ( '<hr />' , '' )
 text = text . replace ( '&#039;' , "'" )
 text = text . replace ( '&#39;' , "'" )
 text = text . replace ( '&quot;' , '"' )
 text = text . replace ( '&rsquo;' , "'" )
 text = text . replace ( '&amp;' , "&" )
 text = text . replace ( '&#8211;' , "&" )
 text = text . replace ( '&#8217;' , "'" )
 text = text . replace ( '&#038;' , "&" )
 text = text . replace ( '&#8211;' , "-" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 if 41 - 41: OOooO % o000o0o00o0Oo
 return text
 if 12 - 12: OOoOoo00oo
def ooOo0O ( ) :
 if 37 - 37: OOooO % i1
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 O0O0ooOOO = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 iIiiiiI1II1I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 83 - 83: i1IIi + OOoO00o - i11iIiiIii / o000o0o00o0Oo
 oooo = 0
 for ( IIIII1iii11 , IIi1I , iii ) in os . walk ( O0O0ooOOO ) :
  for file in iii :
   O00O00O000OOO = os . path . join ( IIIII1iii11 , file )
   oooo += os . path . getsize ( O00O00O000OOO )
 Ii11Ii1I = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oooo / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 3 - 3: O0
 oooo = 0
 for ( IIIII1iii11 , IIi1I , iii ) in os . walk ( oOooO0 ) :
  for file in iii :
   O00O00O000OOO = os . path . join ( IIIII1iii11 , file )
   oooo += os . path . getsize ( O00O00O000OOO )
 Ii11Ii1I = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oooo / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 64 - 64: i1IIi % i1Ii / i11iIiiIii - i1IIi % OOoOoo00oo . OOoO00o
 oooo = 0
 for ( IIIII1iii11 , IIi1I , iii ) in os . walk ( O0o ) :
  for file in iii :
   O00O00O000OOO = os . path . join ( IIIII1iii11 , file )
   oooo += os . path . getsize ( O00O00O000OOO )
 Ii11Ii1I = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oooo / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 8 - 8: ooo0Oo0 + i11Ii11I1Ii1i * OOoOoo00oo * Oooo0000 * iI1 / I1iiiiI1iII
 oooo = 0
 for ( IIIII1iii11 , IIi1I , iii ) in os . walk ( iIiiiiI1II1I1 ) :
  for file in iii :
   O00O00O000OOO = os . path . join ( IIIII1iii11 , file )
   oooo += os . path . getsize ( O00O00O000OOO )
 Ii11Ii1I = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oooo / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 21 - 21: OOo0o0 / OoooooooOO
 i1IiIiiI ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 i1IiIiiI ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 11 - 11: OOoOoo00oo % OOooO - i11iIiiIii - OOo0o0 + i1Ii + I1iiiiI1iII
def ii ( name , url , iconimage ) :
 if 87 - 87: oOo0 * i1IIi / o000o0o00o0Oo
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import resolveurl
 if 6 - 6: i1IIi11111i + ooo0Oo0 - OoooooooOO % OOoOoo00oo * Oooo0000
 if 69 - 69: i1IIi
 if 59 - 59: i11Ii11I1Ii1i - i1IIi11111i
 if 24 - 24: ooo0Oo0 - i1IIi + iI1
 if 'acestream' in url :
  ooOO0O0ooOooO = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  OO . setPath ( url )
  xbmc . Player ( ) . play ( ooOO0O0ooOooO , OO , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
  OO = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OO . setPath ( I1iI )
  xbmc . Player ( ) . play ( I1iI , OO , False )
  time . sleep ( 2 )
  quit ( )
 else :
  I1iI = url
  OO = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OO . setPath ( I1iI )
  xbmc . Player ( ) . play ( I1iI , OO , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 38 - 38: OoooooooOO / o000o0o00o0Oo . O0 / i1IIi / ooo0Oo0 + iIii1I11I1II1
def ooO00O00oOO ( name , url , iconimage ) :
 if 40 - 40: OOoO00o . OOo0o0 + iiI1iIiI + o000o0o00o0Oo + oOo0
 OOoOoo , i11 = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 OOoOoo += urllib . unquote_plus ( i11 )
 url = regex . resolve ( OOoOoo )
 if 20 - 20: OoooooooOO - ooo0Oo0 % Oooo0000 % iI1
 PLAYREGEX ( name , url , iconimage )
 if 89 - 89: OOo0o0 / OoooooooOO . OOoO00o
def oooOo0OOOoo0 ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 34 - 34: OOoO00o - OoooooooOO . iiI1iIiI / i11Ii11I1Ii1i
def II1II ( heading , text ) :
 if 97 - 97: i11iIiiIii / OOoOoo00oo % oOo0
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 ooo0 = xbmcgui . Window ( id )
 o0oooO = 50
 while ( o0oooO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   o0oooO -= 1
   ooo0 . getControl ( 1 ) . setLabel ( heading )
   ooo0 . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 89 - 89: i11Ii11I1Ii1i / OOo0o0
  if 14 - 14: OOoOoo00oo . iiI1iIiI * i1Ii + i11Ii11I1Ii1i - i1Ii + OOoOoo00oo
def oOO00oOO ( url ) :
 try :
  IiII1 = urllib2 . Request ( url )
  IiII1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  I1iIi1iIiiIiI = urllib2 . urlopen ( IiII1 , timeout = 5 )
  I1I = I1iIi1iIiiIiI . read ( )
  I1iIi1iIiiIiI . close ( )
  I1I = I1I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return I1I
 except : quit ( )
 if 18 - 18: OOo0o0 - i1IIi11111i - iiI1iIiI - iiI1iIiI
def OoO0o ( url ) :
 try :
  IiII1 = urllib2 . Request ( url )
  IiII1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  I1iIi1iIiiIiI = urllib2 . urlopen ( IiII1 , timeout = 5 )
  I1I = I1iIi1iIiiIiI . read ( )
  I1iIi1iIiiIiI . close ( )
  I1I = I1I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return I1I
 except : quit ( )
 if 54 - 54: ooo0Oo0 + iiI1iIiI / OOoO00o . iiI1iIiI * Oooo0000
def i1IiIiiI ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IIiIiiiIIIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIi11 = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 81 - 81: iI1 / i1 % OoooooooOO * OOo0o0 / OOo0o0
 iIi11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIiiiIIIIi1 , listitem = OO , isFolder = False )
 return iIi11
 if 28 - 28: i11iIiiIii / i1IIi11111i . iIii1I11I1II1 / i11Ii11I1Ii1i
def I111Ii111 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IIiIiiiIIIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIi11 = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 72 - 72: OoooooooOO / iiI1iIiI + OOooO / Oooo0000 * OOooO
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 34 - 34: O0 * O0 % OoooooooOO + OOoO00o * iIii1I11I1II1 % OOooO
 iIi11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIiiiIIIIi1 , listitem = OO , isFolder = False )
 return iIi11
 if 25 - 25: iI1 + Oooo0000 . i1IIi11111i % Oooo0000 * OOoOoo00oo
def ii1IiIi11 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 iiiii1ii1 = [ ]
 IiiiI1 = [ ]
 OOOo0 = [ ]
 I1I = oOO00oOO ( url )
 OO0OoO0o00 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OO0OoO0o00 ) [ 0 ]
 ii11i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( OO0OoO0o00 )
 if len ( ii11i1 ) < 1 :
  ii11i1 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OO0OoO0o00 )
 oO0000OOo00 = 1
 for OOo0Oo0OOo0 in ii11i1 :
  i1i11I = OOo0Oo0OOo0
  if '(' in OOo0Oo0OOo0 :
   OOo0Oo0OOo0 = OOo0Oo0OOo0 . split ( '(' ) [ 0 ]
   iiIiIi1 = str ( i1i11I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiiii1ii1 . append ( OOo0Oo0OOo0 )
   IiiiI1 . append ( iiIiIi1 )
  else :
   iiiii1ii1 . append ( OOo0Oo0OOo0 )
   IiiiI1 . append ( '[COLOR aqua]Link ' + str ( oO0000OOo00 ) + '[/COLOR]' )
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oOOOOOOOoO = Iii1ii1II11i . select ( name , IiiiI1 )
 if oOOOOOOOoO < 0 :
  quit ( )
 else :
  url = iiiii1ii1 [ oOOOOOOOoO ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : I1iI = liveresolver . resolve ( url )
  else : I1iI = url
  OO = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  OO . setPath ( I1iI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( I1iI )
  if 12 - 12: OOoO00o . I1iiiiI1iII . Oooo0000 / O0
def OO0oOOo0o ( name , url , iconimage ) :
 if 50 - 50: OOoO00o . o000o0o00o0Oo . i1 * iI1 + i11Ii11I1Ii1i % i11iIiiIii
 i1i1IiIiIi1Ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iiiii1ii1 = [ ]
 IiiiI1 = [ ]
 OOOo0 = [ ]
 oO0ooOO = [ ]
 I1I = oOO00oOO ( url )
 OO0OoO0o00 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 ii11i1 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OO0OoO0o00 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OO0OoO0o00 ) [ 0 ]
 oO0000OOo00 = 1
 if 16 - 16: ooo0Oo0 + i1Ii / ooo0Oo0 / i1 % OOo0o0 % o000o0o00o0Oo
 for OOo0Oo0OOo0 in ii11i1 :
  i1i11I = OOo0Oo0OOo0
  if '(' in OOo0Oo0OOo0 :
   OOo0Oo0OOo0 = OOo0Oo0OOo0 . split ( '(' ) [ 0 ]
   iiIiIi1 = str ( i1i11I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiiii1ii1 . append ( OOo0Oo0OOo0 )
   IiiiI1 . append ( iiIiIi1 )
   oO0ooOO . append ( 'Stream ' + str ( oO0000OOo00 ) )
  else :
   iiiii1ii1 . append ( OOo0Oo0OOo0 )
   IiiiI1 . append ( 'Link ' + str ( oO0000OOo00 ) )
   if 22 - 22: i11Ii11I1Ii1i * i1 * iI1 + o000o0o00o0Oo * i1IIi11111i
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oOOOOOOOoO = Iii1ii1II11i . select ( name , IiiiI1 )
 if oOOOOOOOoO < 0 :
  quit ( )
 else :
  O0iII = IiiiI1 [ oOOOOOOOoO ]
  o0 = "/"
  if not O0iII . endswith ( o0 ) :
   ooOooo000oOO = O0iII + "/"
  else :
   ooOooo000oOO = O0iII
  url = i1i1IiIiIi1Ii + iiiii1ii1 [ oOOOOOOOoO ] + "%26referer=" + ooOooo000oOO
  print url
  if 100 - 100: i1IIi / I1iiiiI1iII
  xbmc . Player ( ) . play ( url )
  if 3 - 3: i11Ii11I1Ii1i % o000o0o00o0Oo - OoooooooOO * ooo0Oo0 . iIii1I11I1II1
def IIII ( string ) :
 I1iIO0o00O0Oo0 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 58 - 58: O0
 return '' . join ( I1iIO0o00O0Oo0 )
 if 78 - 78: i1 % I1iiiiI1iII * i1IIi
def iiii11I ( name , url , mode , iconimage , fanart , description = '' ) :
 if 66 - 66: OOooO . iiI1iIiI + i1IIi11111i . iIii1I11I1II1
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 IIiIiiiIIIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iIi11 = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 iIi11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIiiiIIIIi1 , listitem = OO , isFolder = True )
 return iIi11
 if 51 - 51: iI1 . ooo0Oo0
def IiiIiiIi ( name , url , iconimage ) :
 iIi11 = True
 OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIi11 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OO )
 xbmc . Player ( ) . play ( url , OO , False )
 if 40 - 40: i1IIi11111i
def oOOo0oo0o0o0 ( ) :
 if 43 - 43: o000o0o00o0Oo / iiI1iIiI . i1Ii
 oOooO0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 O0O0ooOOO = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 62 - 62: iIii1I11I1II1 + OOoO00o . ooo0Oo0 / I1iiiiI1iII % O0 . oOo0
 oO0000OOo00 = [ ( oOooO0 , 'Cache' ) , ( O0O0ooOOO , 'Thumbnails' ) , ( O0o , 'Packages' ) ]
 if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + i1IIi11111i / i1IIi11111i / i11Ii11I1Ii1i
 I1iOo = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if I1iOo :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for OOoOoo in oO0000OOo00 :
   if 29 - 29: O0 - i11iIiiIii - i11Ii11I1Ii1i + OOoOoo00oo * I1iiiiI1iII
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 1 )
   if 2 - 2: i1IIi - i1Ii + iiI1iIiI . i1IIi11111i * i1IIi11111i / Oooo0000
   for oOOOiIi1I1 , IIi1I , iii in os . walk ( OOoOoo [ 0 ] ) :
    for o00O00O0O0O in iii :
     if ( o00O00O0O0O . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( oOOOiIi1I1 , o00O00O0O0O ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 63 - 63: OOoO00o * o000o0o00o0Oo . OoooooooOO / OOoOoo00oo * ooo0Oo0 . i1Ii
def Ooo0 ( url , mode , name , iconimage , fanart ) :
 if 91 - 91: i1IIi - iIii1I11I1II1
 with open ( I11i , "a" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 55 - 55: iiI1iIiI * i1IIi11111i % i1Ii . iIii1I11I1II1 * oOo0
def o0oo0000 ( ) :
 if 42 - 42: oOo0 + oOo0 * i11Ii11I1Ii1i
 with open ( I11i , "a" ) as oo0000ooooO0o :
  o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  o0O0 = open ( o0Oo ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0 )
  i1IiIiiI ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  if len ( OoOo ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  for OooOOOo0 in OoOo :
   i11I1iIiII = re . compile ( '<title>(.+?)</title>' ) . findall ( OooOOOo0 ) [ 0 ]
   oo0oooooO0 = re . compile ( '<url>(.+?)</url>' ) . findall ( OooOOOo0 ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OooOOOo0 ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OooOOOo0 ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + i11I1iIiII + '[/COLOR]' , oo0oooooO0 , 2 , I1IiI , I1ii11iIi11i )
   if 48 - 48: iI1 - I1iiiiI1iII + iIii1I11I1II1 + OoooooooOO
 i1IiIiiI ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , Iii111II , Oo )
 if 4 - 4: i11Ii11I1Ii1i . iI1 + OOooO * oOo0 . i1Ii
def oOoOo ( ) :
 if 74 - 74: OOo0o0 / o000o0o00o0Oo % i1IIi11111i
 with open ( IiII , "a" ) as oo0000ooooO0o :
  o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  o0O0 = open ( o0Oo ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0 )
  i1IiIiiI ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  if len ( OoOo ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  for OooOOOo0 in OoOo :
   i11I1iIiII = re . compile ( '<title>(.+?)</title>' ) . findall ( OooOOOo0 ) [ 0 ]
   oo0oooooO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( OooOOOo0 ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OooOOOo0 ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OooOOOo0 ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + i11I1iIiII + '[/COLOR]' , oo0oooooO0 , 2 , I1IiI , I1ii11iIi11i )
   if 88 - 88: Oooo0000 - i11iIiiIii % i1IIi11111i * iI1 + o000o0o00o0Oo
 i1IiIiiI ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , Iii111II , Oo )
 if 52 - 52: i11Ii11I1Ii1i . iiI1iIiI + Oooo0000 % i1
def oo0O0o00 ( ) :
 if 70 - 70: i1
 with open ( I11i , "w" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 46 - 46: iI1 - i1IIi
def i111iiIIII ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 80 - 80: ooo0Oo0 * OOooO + o000o0o00o0Oo * OOoOoo00oo
 if 16 - 16: iI1 / iiI1iIiI + i1 % iIii1I11I1II1 - i1IIi . OOo0o0
 if 26 - 26: i1IIi11111i * I1iiiiI1iII . i1IIi
def III1ii1iII ( ) :
 if 59 - 59: O0 + i1IIi - i1IIi11111i
 if 62 - 62: i11iIiiIii % OOoOoo00oo . I1iiiiI1iII . OOoOoo00oo
 ooOo0O0O0oOO0 = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iIiIIi = re . compile ( '<pin>(.+?)</pin>' ) . findall ( ooOo0O0O0oOO0 ) [ 0 ]
  if iIiIIi == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   i1Ii1i1I11Iii = ''
   I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   I1i1i1 . doModal ( )
   if I1i1i1 . isConfirmed ( ) :
    i1Ii1i1I11Iii = I1i1i1 . getText ( )
    if len ( i1Ii1i1I11Iii ) > 1 :
     OoO0O00O0oo0O = i1Ii1i1I11Iii . title ( )
     with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
      o00O00O0O0O . write ( "<pin>" + OoO0O00O0oo0O + "</pin>" )
     III1ii1iII ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in iIiIIi :
   III1I = re . compile ( '<pin>(.+?)</pin>' ) . findall ( ooOo0O0O0oOO0 ) [ 0 ]
   I1I111iIi = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % III1I )
   I1I = oOO00oOO ( I1I111iIi )
   if len ( I1I ) < 1 or 'Pin Expired' in I1I :
    with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
     o00O00O0O0O . write ( '<pin>EXPIRED</pin>' )
    III1ii1iII ( )
   else :
    global baseurl
    baseurl = I1I
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
   o00O00O0O0O . write ( "<pin>EXPIRED</pin>\n" )
  III1ii1iII ( )
  if 53 - 53: iIii1I11I1II1 + i1IIi11111i - Oooo0000 - OOo0o0 / i1Ii % i11iIiiIii
  if 3 - 3: OOoO00o . i1Ii % iiI1iIiI + o000o0o00o0Oo
  if 64 - 64: i1IIi
  if 29 - 29: i1IIi11111i / i11iIiiIii / iiI1iIiI % OOo0o0 % i11iIiiIii
def i111II ( url , iconimage , fanart ) :
 if 63 - 63: iiI1iIiI - i1 % OOoO00o % iI1 / i1IIi11111i / i1IIi
 try :
  i1Ii1i1I11Iii = ''
  I1i1i1 = xbmc . Keyboard ( i1Ii1i1I11Iii , 'Enter Name To Save File As' )
  I1i1i1 . doModal ( )
  if I1i1i1 . isConfirmed ( ) :
   i1Ii1i1I11Iii = I1i1i1 . getText ( )
   if len ( i1Ii1i1I11Iii ) > 1 :
    OoO0O00O0oo0O = i1Ii1i1I11Iii . title ( )
   else : quit ( )
  import resolveurl
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   I1iI = resolveurl . HostedMediaFile ( url ) . resolve ( )
   url = I1iI
  OO0oo0O0OOO0 = url . split ( '/' ) [ - 1 ]
  IIiIiiiIIIIi1 = urllib2 . urlopen ( url )
  OoOOo = os . path . join ( o0OOO , OoO0O00O0oo0O )
  o00O00O0O0O = open ( OoOOo , 'wb' )
  if 46 - 46: iiI1iIiI / OOooO . oOo0 % i11iIiiIii + i1IIi11111i + OoooooooOO
  O0o0000o = IIiIiiiIIIIi1 . info ( )
  oOo00OoOoO = int ( O0o0000o . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( OoO0O00O0oo0O , oOo00OoOoO ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 66 - 66: iiI1iIiI - I1iiiiI1iII
  iiIii = 0
  iIiIii1ii = 8192
  while True :
   buffer = IIiIiiiIIIIi1 . read ( iIiIii1ii )
   if not buffer :
    break
    if 8 - 8: i1 + Oooo0000 . iIii1I11I1II1 % O0
   iiIii += len ( buffer )
   o00O00O0O0O . write ( buffer )
   iI11Ii111 = "[%3.2f%%]" % ( iiIii * 100. / oOo00OoOoO )
   iI11Ii111 = iI11Ii111 + chr ( 8 ) * ( len ( iI11Ii111 ) + 1 )
   iIiiiI . update ( iiIii , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( iI11Ii111 , OoO0O00O0oo0O ) )
   if 54 - 54: Oooo0000 % OOoO00o . Oooo0000 * OOoOoo00oo + Oooo0000 % i1IIi
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as oo0000ooooO0o :
   oo0000ooooO0o . write ( '<item>\n<title>' + OoO0O00O0oo0O + '</title>\n<link>' + OoOOo + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 23 - 23: oOo0 - OOoOoo00oo + OOooO - Oooo0000 * Oooo0000 . ooo0Oo0
  o00O00O0O0O . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 47 - 47: OOo0o0 % iIii1I11I1II1
  if 11 - 11: iiI1iIiI % OOooO - i1 - OOo0o0 + i1IIi11111i
  if 98 - 98: OOoO00o + OOooO - i1
  if 79 - 79: OOoOoo00oo / oOo0 . Oooo0000 - o000o0o00o0Oo
def Ii1ii11IIIi ( ) :
 OOoooOOOo0oO = [ ]
 oO0Ooo0OooOOo = sys . argv [ 2 ]
 if len ( oO0Ooo0OooOOo ) >= 2 :
  O00o0O = sys . argv [ 2 ]
  iIIIiI = O00o0O . replace ( '?' , '' )
  if ( O00o0O [ len ( O00o0O ) - 1 ] == '/' ) :
   O00o0O = O00o0O [ 0 : len ( O00o0O ) - 2 ]
  O00i1 = iIIIiI . split ( '&' )
  OOoooOOOo0oO = { }
  for oO0000OOo00 in range ( len ( O00i1 ) ) :
   iiIII1IIiIIII = { }
   iiIII1IIiIIII = O00i1 [ oO0000OOo00 ] . split ( '=' )
   if ( len ( iiIII1IIiIIII ) ) == 2 :
    OOoooOOOo0oO [ iiIII1IIiIIII [ 0 ] ] = iiIII1IIiIIII [ 1 ]
 return OOoooOOOo0oO
 if 19 - 19: OOoO00o - i1IIi11111i / i1IIi11111i + ooo0Oo0
O00o0O = Ii1ii11IIIi ( ) ; oo0oooooO0 = None ; OOO0OOO00oo = None ; OoO0o0000O = None ; II1 = None ; Iii111II = None ; o0ooO0OOO = None
try : II1 = urllib . unquote_plus ( O00o0O [ "site" ] )
except : pass
try : oo0oooooO0 = urllib . unquote_plus ( O00o0O [ "url" ] )
except : pass
try : OOO0OOO00oo = urllib . unquote_plus ( O00o0O [ "name" ] )
except : pass
try : OoO0o0000O = int ( O00o0O [ "mode" ] )
except : pass
try : Iii111II = urllib . unquote_plus ( O00o0O [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( O00o0O [ "fanart" ] )
except : pass
try : o0ooO0OOO = urllib . unquote_plus ( O00o0O [ "description" ] )
except : pass
if 74 - 74: OOooO * i11iIiiIii / oOo0
if OoO0o0000O == None or oo0oooooO0 == None or len ( oo0oooooO0 ) < 1 : ii11i1iIII ( )
if 75 - 75: O0 - OoooooooOO + i1Ii . OOo0o0 % i11Ii11I1Ii1i
if 9 - 9: i11Ii11I1Ii1i * i11Ii11I1Ii1i . i11iIiiIii * iIii1I11I1II1
if 18 - 18: i1 . i11Ii11I1Ii1i % Oooo0000 % OOooO
if 87 - 87: iIii1I11I1II1 . OoooooooOO * Oooo0000
if 100 - 100: i1 / i1IIi - iiI1iIiI % OOooO - iIii1I11I1II1
elif OoO0o0000O == 1 : oO0OOoO0 ( OOO0OOO00oo , oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 2 : ii ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif OoO0o0000O == 3 : ii1IiIi11 ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
if 17 - 17: iI1 / i1IIi11111i % ooo0Oo0
if 71 - 71: I1iiiiI1iII . oOo0 . i1
if 68 - 68: i11iIiiIii % OOo0o0 * i1 * I1iiiiI1iII * i11Ii11I1Ii1i + O0
elif OoO0o0000O == 4 : i1i ( oo0oooooO0 )
elif OoO0o0000O == 5 : Ii1I1IIii1II ( oo0oooooO0 )
elif OoO0o0000O == 6 : oOo0oO ( )
elif OoO0o0000O == 7 : iiI1Ii1iI1 ( oo0oooooO0 )
elif OoO0o0000O == 8 : oOo0O0o00o ( oo0oooooO0 )
elif OoO0o0000O == 9 : o0iI11I1II ( oo0oooooO0 )
elif OoO0o0000O == 10 : oooOo0OOOoo0 ( oo0oooooO0 )
elif OoO0o0000O == 11 : oOo00oOoO000 ( )
elif OoO0o0000O == 12 : O00o0OO0 ( oo0oooooO0 )
elif OoO0o0000O == 13 : oOOo0 ( oo0oooooO0 )
elif OoO0o0000O == 14 : o0oooOOoOo0 ( oo0oooooO0 )
elif OoO0o0000O == 15 : OOOoOo ( )
elif OoO0o0000O == 16 : OO0oOOo0o ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif OoO0o0000O == 17 : iIIi1i1 ( oo0oooooO0 )
elif OoO0o0000O == 18 : oooo0O0 ( oo0oooooO0 )
elif OoO0o0000O == 19 : i11111IIIII ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 20 : OOO ( )
elif OoO0o0000O == 21 : oOooOo0 ( oo0oooooO0 )
elif OoO0o0000O == 22 : o0O0o0 ( oo0oooooO0 )
elif OoO0o0000O == 23 : I1111i ( )
elif OoO0o0000O == 24 : O0OooOo0o ( oo0oooooO0 )
elif OoO0o0000O == 25 : IIiIiI ( oo0oooooO0 , Iii111II )
elif OoO0o0000O == 26 : o0OoOo00o0o ( oo0oooooO0 )
elif OoO0o0000O == 27 : IiiiiI1i1Iii ( oo0oooooO0 , Iii111II )
elif OoO0o0000O == 28 : iIiii1iI1 ( )
elif OoO0o0000O == 29 : IiIiII1 ( oo0oooooO0 )
elif OoO0o0000O == 30 : i1II ( oo0oooooO0 )
elif OoO0o0000O == 31 : II1Iiiiii ( oo0oooooO0 )
elif OoO0o0000O == 32 : I111i1i1111 ( oo0oooooO0 )
elif OoO0o0000O == 33 : O0oOOoooOO0O ( oo0oooooO0 )
elif OoO0o0000O == 34 : ooo ( oo0oooooO0 )
elif OoO0o0000O == 35 : oOooo0O0o ( )
elif OoO0o0000O == 36 : ooi1i1I ( oo0oooooO0 )
elif OoO0o0000O == 37 : oo0OOo0O ( oo0oooooO0 , Iii111II )
elif OoO0o0000O == 38 : i1i1IIii1i1 ( )
elif OoO0o0000O == 39 : oO00O0 ( oo0oooooO0 )
elif OoO0o0000O == 40 : OOO ( )
elif OoO0o0000O == 41 : oOooOo0 ( oo0oooooO0 )
elif OoO0o0000O == 42 : OO0o ( oo0oooooO0 )
elif OoO0o0000O == 43 : II11iIiiI1111 ( oo0oooooO0 , Iii111II )
elif OoO0o0000O == 44 : IIIii1iiIi ( )
if 66 - 66: iI1 % o000o0o00o0Oo % OoooooooOO
elif OoO0o0000O == 45 : ooo0O ( )
elif OoO0o0000O == 46 : iiI1ii11i1 ( oo0oooooO0 )
elif OoO0o0000O == 47 : Oo0ooo ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif OoO0o0000O == 48 : iI111i1II ( )
elif OoO0o0000O == 49 : Oo000ooOOO ( oo0oooooO0 )
elif OoO0o0000O == 50 : Ii1ii1IiIII ( oo0oooooO0 )
elif OoO0o0000O == 51 : OooO0ooo0o ( oo0oooooO0 )
elif OoO0o0000O == 52 : o0oO00 ( oo0oooooO0 )
elif OoO0o0000O == 53 : IIii11II11II1 ( oo0oooooO0 )
elif OoO0o0000O == 54 : oOOo ( oo0oooooO0 , Iii111II )
if 34 - 34: i1IIi11111i / OOoO00o % O0 . i1 . i1IIi
if 29 - 29: O0 . oOo0
if 66 - 66: OOo0o0 * iIii1I11I1II1 % iIii1I11I1II1 * I1iiiiI1iII - i1Ii - I1iiiiI1iII
elif OoO0o0000O == 59 : oOOO0oo0 ( )
elif OoO0o0000O == 60 : IIi ( oo0oooooO0 )
elif OoO0o0000O == 61 : IIioOoO00oo0O ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
if 70 - 70: oOo0 + OOo0o0
elif OoO0o0000O == 66 : O00oOo00o0o ( )
elif OoO0o0000O == 67 : ii1 ( oo0oooooO0 )
elif OoO0o0000O == 68 : I1Iiiiiii ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 69 : O0Oo00O ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 70 : OOooOOOOOOooo ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 71 : oO0oOOoo00000 ( )
elif OoO0o0000O == 72 : OO00 ( )
elif OoO0o0000O == 73 : o000 ( )
elif OoO0o0000O == 74 : I1i11II ( oo0oooooO0 )
elif OoO0o0000O == 75 : oO00OoOO ( oo0oooooO0 )
elif OoO0o0000O == 76 : OOoO000O00oO ( )
elif OoO0o0000O == 77 : OooOO0o0 ( )
if 93 - 93: oOo0 + OOooO
if 33 - 33: O0
elif OoO0o0000O == 884 : ooOo0O ( )
elif OoO0o0000O == 885 : i111iiIIII ( )
elif OoO0o0000O == 886 : oOoOo ( )
elif OoO0o0000O == 887 : i111II ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 888 : oooO ( )
elif OoO0o0000O == 889 : Ooo0 ( oo0oooooO0 , OoO0o0000O , OOO0OOO00oo , Iii111II , I1ii11iIi11i )
elif OoO0o0000O == 890 : o0oo0000 ( )
elif OoO0o0000O == 891 : oo0O0o00 ( )
elif OoO0o0000O == 892 : oOOo0oo0o0o0 ( )
ooIiII1I1i1i1ii ( )
III1ii1iII ( )
if OoO0o0000O == None or oo0oooooO0 == None or len ( oo0oooooO0 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 78 - 78: O0 / i11Ii11I1Ii1i * i1
if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % oOo0 - iIii1I11I1II1 % O0
if 58 - 58: I1iiiiI1iII + iIii1I11I1II1
if 65 - 65: i11Ii11I1Ii1i - oOo0 % i1IIi11111i - Oooo0000 * OOoO00o + OOooO
if 79 - 79: i1Ii . Oooo0000 % oOo0 - ooo0Oo0
if 69 - 69: i1Ii - i1IIi11111i . i1Ii
if 9 - 9: OOo0o0 % i11iIiiIii / ooo0Oo0
if 20 - 20: OOo0o0 * O0 + iI1 - OoooooooOO . iI1
if 60 - 60: i1IIi11111i . i1IIi11111i / OOoO00o
if 45 - 45: O0 . i11iIiiIii % OOoO00o . Oooo0000 % I1iiiiI1iII % iIii1I11I1II1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
