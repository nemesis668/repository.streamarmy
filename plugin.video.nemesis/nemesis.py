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
ooIiII1I1i1i1ii ( )
def iiiIi ( ) :
 if 24 - 24: O0 % i1IIi11111i + i1IIi + oOo0 + o000o0o00o0Oo
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
 O00o = [ 'plugin.video.jenexporter' ]
 O00 = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in O00o )
 i11I1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.jenexporter' ) )
 if O00 :
  import shutil
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
 iiiIi ( )
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
 iiiIi ( )
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
 url = 'http://www.toonget.net/cartoon'
 I1I = oOO00oOO ( url )
 I1I1I = re . compile ( '<td><a href="(.+?)">(.+?)</a>' ) . findall ( I1I )
 for url , i11I1iIiII in I1I1I :
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 53 - 53: OOo0o0 - iiI1iIiI - OOo0o0 * OOoO00o
def oooooo0OO ( url ) :
 if 14 - 14: OOo0o0 / OOo0o0 % i1Ii
 I1I = oOO00oOO ( url )
 try :
  I1IiI = re . compile ( '<div class="left_col">.+?<img src="(.+?)"' ) . findall ( I1I ) [ 0 ]
 except :
  I1IiI = Iii111II
 try :
  ooO = re . compile ( '<span>Description:</span>.+?<div>(.+?)</div>' ) . findall ( I1I ) [ 0 ] . strip ( )
 except :
  ooO = 'No Description Found'
 OoOo = re . compile ( '<div id="videos">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<li>.+?<a href="(.+?)">(.+?)</a>' ) . findall ( OoOo )
 for url , i11I1iIiII in I1I1I :
  iiii11I ( "[COLOR aqua][B]" + i11I1iIiII + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , ooO )
  if 6 - 6: iIii1I11I1II1 . i1Ii % i1IIi11111i
 try :
  I1Iii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' ) . findall ( I1I ) [ 0 ] . strip ( )
  iiI11Iii = re . compile ( 'href="(.+?)"' ) . findall ( I1Iii1 ) [ 0 ]
  iiii11I ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , iiI11Iii , 30 , Iii111II , I1ii11iIi11i )
 except : pass
 if 78 - 78: OOoO00o + iI1 . i1Ii - OOoO00o . OOooO
def II1I11i ( url ) :
 if 82 - 82: iI1 + OoooooooOO - i1IIi . i1IIi
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<iframe src="(.+?)"' ) . findall ( I1I )
 oO0000OOo00 = 0
 for iIi1i in OoOo :
  oO0000OOo00 += 1
  i11I1iIiII = 'Stream : ' + str ( oO0000OOo00 )
  i1IiIiiI ( i11I1iIiII , iIi1i , 32 , Iii111II , I1ii11iIi11i )
  if 27 - 27: OOoOoo00oo * i1Ii . oOo0 % I1iiiiI1iII * I1iiiiI1iII . i1IIi
def O0OOoOOO0oO ( url ) :
 if 28 - 28: i1Ii + i11iIiiIii / iI1 % Oooo0000 % ooo0Oo0 - O0
 I1I = oOO00oOO ( url )
 if 'easyvideome' in url or 'videozoo' in url :
  ooo0OOO = re . compile ( 'file:.+?"(.+?)"' ) . findall ( I1I ) [ 1 ]
  ii ( OOO0OOO00oo , ooo0OOO , Iii111II )
 elif 'playpandanet' in url :
  ooo0OOO = re . compile ( """url:.+?'(.+?)'""" ) . findall ( I1I ) [ 0 ]
  ii ( OOO0OOO00oo , ooo0OOO , Iii111II )
 else :
  Iii1ii1II11i . notification ( o0OoOoOO00 , 'Sorry This Link Is Down, Try Another' , Iii111II , 4000 )
  if 49 - 49: i11iIiiIii % OOooO . Oooo0000
  if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - i11Ii11I1Ii1i * OOoOoo00oo
def iiIi1iI1iIii ( ) :
 if 68 - 68: OOoOoo00oo
 oo0oooooO0 = "http://www.loyalbooks.com/genre-menu"
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( I1I )
 for iIo00O in OoOo :
  if "paid" not in iIo00O :
   OoOO000 = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
   OOooooO0Oo = "http://www.loyalbooks.com" + OoOO000
   OOO0OOO00oo = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
   iiii11I ( "[COLOR aqua]" + OOO0OOO00oo + "[/COLOR]" , OOooooO0Oo , 60 , I1IiI , Oo , '' )
   if 82 - 82: iIii1I11I1II1 + ooo0Oo0 . iIii1I11I1II1 % I1iiiiI1iII / OOooO . OOooO
def IIi ( url ) :
 if 66 - 66: OOo0o0 % i1 . OOoOoo00oo
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 o0O = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( OoOo )
 for iIo00O in o0O :
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
 if 39 - 39: iIii1I11I1II1 / O0 / OOo0o0 - OOooO - OOoO00o % OOoOoo00oo
 if 31 - 31: iI1 - O0 / i1Ii * Oooo0000
def iI111i1II ( name , url , iconimage ) :
 if 69 - 69: OOooO * O0 . i11iIiiIii / OOooO . i1IIi11111i
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( I1I )
 for iIo00O in OoOo :
  i11I1iIiII = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( iIo00O ) [ 0 ]
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , ooOO0O0ooOooO , 10 , iconimage , Oo , '' )
  if 63 - 63: iI1 + i1IIi11111i . i11Ii11I1Ii1i - iiI1iIiI
def oOOO00o000o ( ) :
 if 9 - 9: OOo0o0 + iI1 / iI1
 oo0oooooO0 = 'http://www.shadownet.me/'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoOo )
 for oo0oooooO0 , i11I1iIiII in I1I1I :
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  if 'P2P' not in i11I1iIiII :
   iiii11I ( "[COLOR skyblue]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 49 , I1IiI , Oo , '' )
   if 12 - 12: OoooooooOO % i1IIi11111i * iI1 % iIii1I11I1II1 / OOooO
   if 27 - 27: i11iIiiIii % i11Ii11I1Ii1i % iI1 . O0 - ooo0Oo0 + Oooo0000
def ooO0o ( url ) :
 if 51 - 51: I1iiiiI1iII
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
 if 25 - 25: OoooooooOO + I1iiiiI1iII * o000o0o00o0Oo
def OoO0ooO ( url ) :
 if 51 - 51: OOoO00o / i1Ii * Oooo0000 . OOoO00o / o000o0o00o0Oo / i11iIiiIii
 def IIIII ( url ) :
  o0ooOoO000oO = urllib2 . Request ( url )
  o0ooOoO000oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  o0ooOoO000oO . add_header ( 'Referer' , url )
  OOo = urllib2 . urlopen ( o0ooOoO000oO , timeout = 5 )
  I1I = OOo . read ( )
  OOo . close ( )
  return I1I
  if 50 - 50: i1Ii
 I1I = IIIII ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  OoOo = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( I1I ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in OoOo :
  url = OoOo
  ii ( OOO0OOO00oo , url , Iii111II )
 OOooooO0Oo = IIIII ( OoOo )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 72 - 72: oOo0
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
   if 90 - 90: ooo0Oo0 % O0 * iIii1I11I1II1 . OOoO00o
  OO = xbmcgui . ListItem ( OOO0OOO00oo , iconImage = Iii111II , thumbnailImage = Iii111II )
  OO . setPath ( url )
  if 8 - 8: i1Ii + i11Ii11I1Ii1i / OOoO00o / iI1
  xbmc . Player ( ) . play ( ooOO0O0ooOooO , OO , False )
  if 74 - 74: O0 / i1IIi
  if 78 - 78: OoooooooOO . i1 + i1Ii - i1IIi
def ii1 ( ) :
 if 83 - 83: OOoO00o . O0 / ooo0Oo0 / OOoOoo00oo - i11Ii11I1Ii1i
 oo0oooooO0 = 'https://m.skylinewebcams.com/en/webcam'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I1I = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 oO0oO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I1I )
 for oo0oooooO0 , i11I1iIiII in oO0oO0 :
  if 'http|https' not in oo0oooooO0 :
   oo0oooooO0 = 'https://m.skylinewebcams.com' + oo0oooooO0
   iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 46 , I1IiI , Oo , '' )
   if 14 - 14: OOoO00o
def oOOOOo0oo0O ( url ) :
 if 13 - 13: iiI1iIiI % Oooo0000 . o000o0o00o0Oo / ooo0Oo0 % OOoOoo00oo . OoooooooOO
 I1I = oOO00oOO ( url )
 I1I1I = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( I1I )
 for url , I1IiI , i11I1iIiII in I1I1I :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 22 - 22: I1iiiiI1iII / i11iIiiIii
  if 62 - 62: i1 / o000o0o00o0Oo
def ii1O000OOO0OOo ( name , url , iconimage ) :
 if 32 - 32: OOooO * O0
 I1I = oOO00oOO ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  OoOo = re . compile ( '<amp-video src="(.+?)"' ) . findall ( I1I ) [ 0 ]
  url = 'https:' + OoOo
  OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , OO , False )
  if 100 - 100: i1Ii % iIii1I11I1II1 * i11Ii11I1Ii1i - OOoO00o
 except : pass
 quit ( 0 )
 if 92 - 92: i1Ii
def II11iI111i1 ( ) :
 if 95 - 95: OoooooooOO - I1iiiiI1iII * iiI1iIiI + Oooo0000
 oo0oooooO0 = 'http://www.watchepisodeseries.com/home/schedule'
 I1I = oOO00oOO ( oo0oooooO0 )
 OoOo = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( OoOo )
 for oo0oooooO0 , iIi1 , i11iiI1111 in I1I1I :
  iiii11I ( "[COLOR aqua]" + iIi1 + "  " + i11iiI1111 + "[/COLOR]" , oo0oooooO0 , 67 , I1IiI , I1ii11iIi11i )
  if 97 - 97: ooo0Oo0 * iiI1iIiI . iIii1I11I1II1
  if 16 - 16: i1Ii % OoooooooOO - OOoOoo00oo * OOooO * o000o0o00o0Oo / OoooooooOO
def I11 ( url ) :
 if 95 - 95: i1Ii * OOo0o0 . oOo0
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 1 ]
  i11I1iIiII = OOoOO0o0o0 ( i11I1iIiII )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  Iii111II = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( ii11i1 ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , url , 68 , Iii111II , I1ii11iIi11i )
  if 97 - 97: oOo0 - iIii1I11I1II1
  if 75 - 75: OoooooooOO * I1iiiiI1iII
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
   iIi1 = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( ii11i1 ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in iIi1 :
    iIi1 = iIi1 . strip ( )
    iIi1 = time . strptime ( iIi1 , "%d/%m/%Y" )
    iIiiiii1i = ( "%s/%s/%s" % ( oO0000OOo00 . day , oO0000OOo00 . month , oO0000OOo00 . year ) )
    iIiiiii1i = time . strptime ( iIiiiii1i , "%d/%m/%Y" )
    if ( iIiiiii1i < iIi1 ) :
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
 ooo0OOO = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( ooo0OOO )
 for I1i , I1I in I1I1I :
  I1i = I1i . replace ( ':' , '' )
  url = 'https://www.eporner.com' + I1I
  i1IiIiiI ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + I1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 72 - 72: iIii1I11I1II1
def iiIi ( url ) :
 if 71 - 71: Oooo0000 . i1IIi
 url = 'https://ww1.soul-anime.us/anime-list.html'
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<ul id="genre">(.*?)</ul>' ) . findall ( I1I ) [ 0 ]
 I1I1I = re . compile ( '<a rel=.*?href="(.*?)">(.*?)</a>' ) . findall ( OoOo )
 for I1I , i11I1iIiII in I1I1I :
  iiii11I ( "[COLOR cyan]" + i11I1iIiII + "[/COLOR]" , I1I , 52 , I1IiI , Oo , '' )
 iiiIi ( )
def o0OooO0ooo0o ( url ) :
 if 47 - 47: OoooooooOO
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="lt">(.*?)<div class="tags"' ) . findall ( I1I )
 for ii1i1i1IiII in OoOo :
  i11I1iIiII = re . compile ( 'alt="(.*?)"' ) . findall ( ii1i1i1IiII ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( ii1i1i1IiII ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( ii1i1i1IiII ) [ 0 ]
  ooO = re . compile ( '<p>(.*?)</p>' ) . findall ( ii1i1i1IiII ) [ 0 ]
  O0o = re . compile ( '<span class=".*?">(.*?)</span>' ) . findall ( ii1i1i1IiII ) [ 0 ]
  if 'Completed' in O0o :
   O0o = '[COLOR red]' + O0o + '[/COLOR]'
  else :
   O0o = '[COLOR lime]' + O0o + '[/COLOR]'
  iiii11I ( "[COLOR cyan]" + i11I1iIiII + " :: " + O0o + "[/COLOR]" , url , 53 , I1IiI , Oo , ooO )
 iiiIi ( )
 if 41 - 41: ooo0Oo0 / OOooO * OOooO - OOoOoo00oo . oOo0 . OoooooooOO
def I1iIIi111i1 ( url ) :
 if 12 - 12: i11Ii11I1Ii1i . iI1 / OOoOoo00oo
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<div class="img_box">(.*?)</span>' ) . findall ( I1I )
 for ii1i1i1IiII in OoOo :
  i11I1iIiII = re . compile ( '<div class="ep">(.*?)</div>' ) . findall ( ii1i1i1IiII ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( ii1i1i1IiII ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( ii1i1i1IiII ) [ 0 ]
  i1IiIiiI ( "[COLOR cyan]" + i11I1iIiII + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
 iiiIi ( )
 if 77 - 77: i1Ii - iiI1iIiI % iI1 - O0
def o0O0O0 ( url , iconimage ) :
 if 6 - 6: OOoO00o . I1iiiiI1iII * Oooo0000 . i1IIi
 I1I = oOO00oOO ( url )
 OoOo = re . compile ( '<iframe name="stream".*?src="(.*?)"' ) . findall ( I1I ) [ 0 ]
 OOooooO0Oo = oOO00oOO ( OoOo )
 try :
  ooo0OOO = re . compile ( '<iframe.*?src="(.*?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
  ii ( OOO0OOO00oo , ooo0OOO , iconimage )
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Source Link Is Down[/COLOR]' , iconimage , 5000 )
  if 98 - 98: i1IIi
def oO0O ( url ) :
 if 86 - 86: Oooo0000 . iIii1I11I1II1 - i1
 url = 'http://m4ufree.io/'
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( 'title="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( './' , '/' )
  if not 'http://' in url :
   url = 'http://m4ufree.io/' + url
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  I1i = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( ii11i1 ) [ 0 ]
  iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[COLOR yellow] " + I1i + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 56 - 56: O0
 try :
  I1I11 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( I1I ) [ 0 ]
  OOOoOO0o = re . compile ( '<a.+?href="(.+?)"' ) . findall ( I1I11 ) [ 5 ]
  if 'genre' in OOOoOO0o :
   OOo00 = OOo00 . replace ( '.com' , '.com/' )
  iIII = I1IiI
  iiii11I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OOOoOO0o , 42 , iIII , Oo , description = '' )
 except : pass
 if 48 - 48: iIii1I11I1II1 % i1IIi % OOoO00o + i1Ii
def Iiii11iIi1 ( url , iconimage ) :
 if 40 - 40: iI1 % i1 . oOo0
 import requests
 OOO0oOOo00O = url
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OO0o = re . compile ( 'data="(.+?)"' ) . findall ( I1I )
 III111i11IiI = 'http://m4ufree.io/ajax_new.php'
 for Ooo0OO0oOO in OO0o :
  try :
   III111i11IiI = 'http://m4ufree.io/ajax_new.php'
   O0000 = requests . post ( III111i11IiI , data = { 'm4u' : Ooo0OO0oOO } )
   json = ( O0000 . text )
   ooO00O0O0 = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
   iII1I1 = re . compile ( '{(.+?)}' ) . findall ( ooO00O0O0 )
   o0Ooo0o0ooo0 = 0
   for oO0000OOo00 in iII1I1 :
    o0Ooo0o0ooo0 += 1
    i11I1iIiII = 'Link ' + str ( o0Ooo0o0ooo0 )
    try :
     I1i = re . compile ( '''"label":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     i11Iiii = re . compile ( '''"file":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     url = 'http://m4ufree.io/' + i11Iiii + '|referer=' + OOO0oOOo00O
     i1IiIiiI ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + I1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
    except :
     I1i = re . compile ( """label:.+?'(.+?)'""" ) . findall ( oO0000OOo00 ) [ 0 ]
     i11Iiii = re . compile ( '''file: "(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
     url = 'http://m4ufree.io/' + i11Iiii + '|referer=' + OOO0oOOo00O
     i1IiIiiI ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + I1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except : pass
  if 70 - 70: i11iIiiIii % OOoO00o
  if 11 - 11: I1iiiiI1iII % o000o0o00o0Oo % OOooO / i11Ii11I1Ii1i % oOo0 - ooo0Oo0
def OOooOO00O0OO00oo ( ) :
 if 69 - 69: i1IIi11111i / ooo0Oo0
 oo0oooooO0 = 'https://www.livefootballol.me/acestream-channel-list-2017.html'
 I1I = oOO00oOO ( oo0oooooO0 )
 I1I1I = re . compile ( '<tr>(.+?)</tr>' ) . findall ( I1I )
 for ii1i1i1IiII in I1I1I :
  i11I1iIiII = re . compile ( '<strong>(.+?)</strong>' ) . findall ( ii1i1i1IiII ) [ 0 ]
  if len ( i11I1iIiII ) == 1 or '&nbsp;' in i11I1iIiII :
   i11I1iIiII = re . compile ( '<strong>(.+?)</strong>' ) . findall ( ii1i1i1IiII ) [ 1 ]
  if len ( i11I1iIiII ) > 40 :
   i11I1iIiII = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( ii1i1i1IiII ) [ 0 ]
  oo0oooooO0 = re . compile ( '<td>(.+?)</td>' ) . findall ( ii1i1i1IiII ) [ 2 ]
  IIiIii = re . compile ( '<td>(.+?)</td>' ) . findall ( ii1i1i1IiII ) [ 3 ]
  IIIII1iii = re . compile ( '<td>(.+?)</td>' ) . findall ( ii1i1i1IiII ) [ 4 ]
  i11I1iIiII = i11I1iIiII . strip ( )
  oo0oooooO0 = oo0oooooO0 . strip ( )
  i1IiIiiI ( "[COLOR aqua]" + i11I1iIiII + ' :: [COLOR yellow]' + IIiIii + '[COLOR aqua] :: [COLOR yellow]' + IIIII1iii + ' Kbps[/COLOR]' , oo0oooooO0 , 2 , Iii111II , Oo , '' )
  if 7 - 7: i1IIi11111i + i1IIi . iiI1iIiI / ooo0Oo0
def I111i1I1 ( ) :
 if 62 - 62: OOoOoo00oo * oOo0 / ooo0Oo0 * i1IIi11111i
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
def II1Ii1iI1i1 ( ) :
 if 54 - 54: O0
 oo0oooooO0 = 'http://www.livefootballol.me/streaming/english-premier-league-2018/'
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<td>(.+?)</td>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  oo0oooooO0 = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ]
  i1Ii11i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  oo0oooooO0 = 'http://www.livefootballol.me' + oo0oooooO0
  iiii11I ( "[COLOR aqua]" + i1Ii11i1i + "[/COLOR]" , oo0oooooO0 , 74 , Iii111II , Oo , '' )
  if 68 - 68: i1 * i1IIi11111i . i1Ii % OOo0o0 % oOo0
def oooo0OO ( url ) :
 if 23 - 23: OOo0o0 + i1
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<a href="(.+?)"' ) . findall ( I1I )
 III1I1i1 = 0
 for OO0OoO0o00 in OoOo :
  if 'acestream' in OO0OoO0o00 :
   if 'http' in OO0OoO0o00 :
    III1I1i1 += 1
    i11I1iIiII = '[COLOR aqua]Link :: ' + str ( III1I1i1 ) + '[/COLOR]'
    i1IiIiiI ( i11I1iIiII , OO0OoO0o00 , 75 , Iii111II , Oo , '' )
 if III1I1i1 == 0 :
  i1IiIiiI ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , Iii111II , Oo , '' )
  if 11 - 11: O0 / i1 % OOoOoo00oo + i1IIi11111i + iIii1I11I1II1
def I1i1111I ( url ) :
 if 95 - 95: iIii1I11I1II1 - o000o0o00o0Oo . oOo0 - iiI1iIiI
 I1I = oOO00oOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( I1I ) [ 0 ]
 ii ( OOO0OOO00oo , url , Iii111II )
 if 75 - 75: i1 + i1IIi11111i - i1IIi . OoooooooOO * OOooO / I1iiiiI1iII
def OOOooo0OooOoO ( url , getphp ) :
 o0ooOoO000oO = urllib2 . Request ( url )
 o0ooOoO000oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 o0ooOoO000oO . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 OOo = urllib2 . urlopen ( o0ooOoO000oO , timeout = 10 )
 I1I = OOo . read ( )
 OOo . close ( )
 return I1I
 if 91 - 91: OOo0o0 + iiI1iIiI
 if 59 - 59: iiI1iIiI + i11iIiiIii + i1IIi / iI1
 if 44 - 44: iI1 . Oooo0000 * iiI1iIiI + OoooooooOO - OOoO00o - I1iiiiI1iII
def I1iii ( ) :
 if 51 - 51: o000o0o00o0Oo
 oo0oooooO0 = 'http://m4ufree.com/?sort=key_top&page=1&='
 I1I = oOO00oOO ( oo0oooooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOo = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( I1I )
 for ii11i1 in OoOo :
  i11I1iIiII = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( ii11i1 ) [ 0 ]
  ooOO0O0ooOooO = re . compile ( '<a href="(.+?)"' ) . findall ( ii11i1 ) [ 0 ] . replace ( './' , '' )
  oo0oooooO0 = 'http://m4ufree.com/' + ooOO0O0ooOooO
  if not re . search ( '\d+' , i11I1iIiII ) :
   iiii11I ( "[COLOR aqua]" + i11I1iIiII + "[/COLOR]" , oo0oooooO0 , 42 , I1IiI , Oo )
   if 41 - 41: o000o0o00o0Oo * i1Ii - OOooO + ooo0Oo0
   if 23 - 23: i11Ii11I1Ii1i % i1IIi11111i + i1IIi11111i + OOoO00o - OOoO00o
   if 62 - 62: i1IIi11111i
   if 45 - 45: OOoOoo00oo * i1Ii
   if 74 - 74: i1IIi + O0 + ooo0Oo0
   if 5 - 5: ooo0Oo0 * Oooo0000
   if 46 - 46: i1Ii
   if 33 - 33: OOoO00o - i11Ii11I1Ii1i * OoooooooOO - ooo0Oo0 - OOoOoo00oo
   if 84 - 84: oOo0 + ooo0Oo0 - Oooo0000 * Oooo0000
   if 61 - 61: OoooooooOO . OOo0o0 . OoooooooOO / ooo0Oo0
def OOoOO0o0o0 ( text ) :
 if 72 - 72: i1IIi
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
 if 82 - 82: Oooo0000 + OoooooooOO / i11iIiiIii * o000o0o00o0Oo . OoooooooOO
 return text
 if 63 - 63: o000o0o00o0Oo
def i1II ( ) :
 if 2 - 2: i11Ii11I1Ii1i - i1 . I1iiiiI1iII * OOoO00o / OOo0o0
 OOo0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 iiIii1IIi = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 ii1IiIiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 OOOoOo00O = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 59 - 59: OOoOoo00oo % iIii1I11I1II1 . i1IIi + i11Ii11I1Ii1i * I1iiiiI1iII
 i1IiiI1iIi = 0
 for ( oOOo00O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( iiIii1IIi ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( oOOo00O0OOOo , file )
   i1IiiI1iIi += os . path . getsize ( iIO0O00OOo )
 Ii11Ii1I = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i1IiiI1iIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 66 - 66: i11iIiiIii / i1IIi11111i - OoooooooOO / i1IIi . i11iIiiIii
 i1IiiI1iIi = 0
 for ( oOOo00O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( OOo0 ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( oOOo00O0OOOo , file )
   i1IiiI1iIi += os . path . getsize ( iIO0O00OOo )
 Ii11Ii1I = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i1IiiI1iIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 16 - 16: ooo0Oo0 % o000o0o00o0Oo + iI1 - O0 . OOoO00o / oOo0
 i1IiiI1iIi = 0
 for ( oOOo00O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( ii1IiIiI1 ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( oOOo00O0OOOo , file )
   i1IiiI1iIi += os . path . getsize ( iIO0O00OOo )
 Ii11Ii1I = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i1IiiI1iIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 35 - 35: OOo0o0 / oOo0 / i11Ii11I1Ii1i - iIii1I11I1II1 + i11Ii11I1Ii1i . oOo0
 i1IiiI1iIi = 0
 for ( oOOo00O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( OOOoOo00O ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( oOOo00O0OOOo , file )
   i1IiiI1iIi += os . path . getsize ( iIO0O00OOo )
 Ii11Ii1I = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i1IiiI1iIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( Ii11Ii1I , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 81 - 81: OOoO00o * OOoOoo00oo - o000o0o00o0Oo * OOooO % Oooo0000 * Oooo0000
 i1IiIiiI ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 i1IiIiiI ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 59 - 59: iIii1I11I1II1
def ii ( name , url , iconimage ) :
 if 7 - 7: OOoOoo00oo * iiI1iIiI / i1IIi11111i * i11iIiiIii
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import resolveurl
 if 84 - 84: OOoOoo00oo . OOoO00o
 if 8 - 8: ooo0Oo0 + i11Ii11I1Ii1i * OOoOoo00oo * Oooo0000 * iI1 / I1iiiiI1iII
 if 21 - 21: OOo0o0 / OoooooooOO
 if 11 - 11: OOoOoo00oo % OOooO - i11iIiiIii - OOo0o0 + i1Ii + I1iiiiI1iII
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
  if 87 - 87: oOo0 * i1IIi / o000o0o00o0Oo
def IIII1i1 ( name , url , iconimage ) :
 if 70 - 70: i11iIiiIii % o000o0o00o0Oo / iiI1iIiI
 OOoOoo , ooOOOOo0 = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 OOoOoo += urllib . unquote_plus ( ooOOOOo0 )
 url = regex . resolve ( OOoOoo )
 if 38 - 38: OoooooooOO / o000o0o00o0Oo . O0 / i1IIi / ooo0Oo0 + iIii1I11I1II1
 PLAYREGEX ( name , url , iconimage )
 if 96 - 96: OOoO00o
def oooOo0OOOoo0 ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 18 - 18: OOoO00o * iI1 - OOooO
def II1i1III ( heading , text ) :
 if 34 - 34: oOo0 - i11iIiiIii / iIii1I11I1II1
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 OOOo = xbmcgui . Window ( id )
 oO00OoOoo0 = 50
 while ( oO00OoOoo0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   oO00OoOoo0 -= 1
   OOOo . getControl ( 1 ) . setLabel ( heading )
   OOOo . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 34 - 34: OOoO00o - OoooooooOO . iiI1iIiI / i11Ii11I1Ii1i
  if 27 - 27: i1 / ooo0Oo0 * i1Ii - i1
def oOO00oOO ( url ) :
 try :
  o0ooOoO000oO = urllib2 . Request ( url )
  o0ooOoO000oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OOo = urllib2 . urlopen ( o0ooOoO000oO , timeout = 5 )
  I1I = OOo . read ( )
  OOo . close ( )
  I1I = I1I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return I1I
 except : quit ( )
 if 19 - 19: iI1
def OoO0o ( url ) :
 try :
  o0ooOoO000oO = urllib2 . Request ( url )
  o0ooOoO000oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  OOo = urllib2 . urlopen ( o0ooOoO000oO , timeout = 5 )
  I1I = OOo . read ( )
  OOo . close ( )
  I1I = I1I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return I1I
 except : quit ( )
 if 67 - 67: O0 % iIii1I11I1II1 / I1iiiiI1iII . i11iIiiIii - OOooO + O0
def i1IiIiiI ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 i1iiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO0Oo = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 45 - 45: OoooooooOO % OOo0o0 - o000o0o00o0Oo - OOo0o0 - iiI1iIiI / i1IIi11111i
 OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1iiiIi1i , listitem = OO , isFolder = False )
 return OO0Oo
 if 81 - 81: i11Ii11I1Ii1i + i11iIiiIii / OOoO00o
def I111Ii111 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 i1iiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO0Oo = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 85 - 85: i11iIiiIii + oOo0 * Oooo0000
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 1 - 1: i1IIi / ooo0Oo0 . i1
 OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1iiiIi1i , listitem = OO , isFolder = False )
 return OO0Oo
 if 57 - 57: iI1 . ooo0Oo0 + i11Ii11I1Ii1i
def i111i11I1ii ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OOooo = [ ]
 oo0 = [ ]
 oOOII1i11i1iIi11 = [ ]
 I1I = oOO00oOO ( url )
 OO0OoO0o00 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OO0OoO0o00 ) [ 0 ]
 ii11i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( OO0OoO0o00 )
 if len ( ii11i1 ) < 1 :
  ii11i1 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OO0OoO0o00 )
 oO0000OOo00 = 1
 for oo0O0oO0O0O in ii11i1 :
  oOo0O = oo0O0oO0O0O
  if '(' in oo0O0oO0O0O :
   oo0O0oO0O0O = oo0O0oO0O0O . split ( '(' ) [ 0 ]
   I11iIiii1 = str ( oOo0O . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OOooo . append ( oo0O0oO0O0O )
   oo0 . append ( I11iIiii1 )
  else :
   OOooo . append ( oo0O0oO0O0O )
   oo0 . append ( '[COLOR aqua]Link ' + str ( oO0000OOo00 ) + '[/COLOR]' )
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 iIIIiiiI11I = Iii1ii1II11i . select ( name , oo0 )
 if iIIIiiiI11I < 0 :
  quit ( )
 else :
  url = OOooo [ iIIIiiiI11I ]
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
  if 6 - 6: OOooO % i1IIi . OOooO * OOooO
def o0Oo ( name , url , iconimage ) :
 if 90 - 90: i11Ii11I1Ii1i + OoooooooOO % OoooooooOO
 I11Ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 OOooo = [ ]
 oo0 = [ ]
 oOOII1i11i1iIi11 = [ ]
 iIiII = [ ]
 I1I = oOO00oOO ( url )
 OO0OoO0o00 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1I ) [ 0 ]
 ii11i1 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OO0OoO0o00 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OO0OoO0o00 ) [ 0 ]
 oO0000OOo00 = 1
 if 19 - 19: I1iiiiI1iII
 for oo0O0oO0O0O in ii11i1 :
  oOo0O = oo0O0oO0O0O
  if '(' in oo0O0oO0O0O :
   oo0O0oO0O0O = oo0O0oO0O0O . split ( '(' ) [ 0 ]
   I11iIiii1 = str ( oOo0O . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OOooo . append ( oo0O0oO0O0O )
   oo0 . append ( I11iIiii1 )
   iIiII . append ( 'Stream ' + str ( oO0000OOo00 ) )
  else :
   OOooo . append ( oo0O0oO0O0O )
   oo0 . append ( 'Link ' + str ( oO0000OOo00 ) )
   if 78 - 78: OOoOoo00oo % i1IIi11111i
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 iIIIiiiI11I = Iii1ii1II11i . select ( name , oo0 )
 if iIIIiiiI11I < 0 :
  quit ( )
 else :
  O0iII = oo0 [ iIIIiiiI11I ]
  o0 = "/"
  if not O0iII . endswith ( o0 ) :
   ooOooo000oOO = O0iII + "/"
  else :
   ooOooo000oOO = O0iII
  url = I11Ii + OOooo [ iIIIiiiI11I ] + "%26referer=" + ooOooo000oOO
  print url
  if 39 - 39: o000o0o00o0Oo + iiI1iIiI - iIii1I11I1II1 - i1IIi11111i
  xbmc . Player ( ) . play ( url )
  if 7 - 7: I1iiiiI1iII . Oooo0000 / o000o0o00o0Oo . OOoOoo00oo * iI1 - i11Ii11I1Ii1i
def IIII ( string ) :
 I1 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 21 - 21: O0 * O0 % o000o0o00o0Oo
 return '' . join ( I1 )
 if 94 - 94: iI1 + i11Ii11I1Ii1i % i11iIiiIii
def iiii11I ( name , url , mode , iconimage , fanart , description = '' ) :
 if 8 - 8: i1Ii * O0
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 i1iiiIi1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO0Oo = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1iiiIi1i , listitem = OO , isFolder = True )
 return OO0Oo
 if 73 - 73: i1IIi11111i / OOo0o0 / iI1 / i1
def III1ii ( name , url , iconimage ) :
 OO0Oo = True
 OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OO )
 xbmc . Player ( ) . play ( url , OO , False )
 if 41 - 41: i1Ii . ooo0Oo0 + iiI1iIiI
def o0O0OO ( ) :
 if 22 - 22: i11Ii11I1Ii1i * i1 * iI1 + o000o0o00o0Oo * i1IIi11111i
 OOo0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 iiIii1IIi = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 ii1IiIiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 100 - 100: i1IIi / I1iiiiI1iII
 oO0000OOo00 = [ ( OOo0 , 'Cache' ) , ( iiIii1IIi , 'Thumbnails' ) , ( ii1IiIiI1 , 'Packages' ) ]
 if 3 - 3: i11Ii11I1Ii1i % o000o0o00o0Oo - OoooooooOO * ooo0Oo0 . iIii1I11I1II1
 I1iIO0o00O0Oo0 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if I1iIO0o00O0Oo0 :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for OOoOoo in oO0000OOo00 :
   if 58 - 58: O0
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 1 )
   if 78 - 78: i1 % I1iiiiI1iII * i1IIi
   for O0iI , i11I1I1iiI , I1i1iii1Ii in os . walk ( OOoOoo [ 0 ] ) :
    for o00O00O0O0O in I1i1iii1Ii :
     if ( o00O00O0O0O . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( O0iI , o00O00O0O0O ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 15 - 15: O0 / ooo0Oo0 % o000o0o00o0Oo + i1IIi11111i
def iiiIiI ( url , mode , name , iconimage , fanart ) :
 if 9 - 9: iIii1I11I1II1 % o000o0o00o0Oo . OOoOoo00oo + OoooooooOO
 with open ( I11i , "a" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 62 - 62: O0 / iiI1iIiI % O0 * i1 % iiI1iIiI
def Ii ( ) :
 if 99 - 99: i1 * i11iIiiIii . OoooooooOO % ooo0Oo0
 with open ( I11i , "a" ) as oo0000ooooO0o :
  Oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  Oo0oOooOoOo = open ( Oo0 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( Oo0oOooOoOo )
  i1IiIiiI ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  if len ( OoOo ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  for ii1i1i1IiII in OoOo :
   i11I1iIiII = re . compile ( '<title>(.+?)</title>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   oo0oooooO0 = re . compile ( '<url>(.+?)</url>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + i11I1iIiII + '[/COLOR]' , oo0oooooO0 , 2 , I1IiI , I1ii11iIi11i )
   if 49 - 49: OOoOoo00oo . o000o0o00o0Oo . i11iIiiIii - i11Ii11I1Ii1i / OOooO
 i1IiIiiI ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , Iii111II , Oo )
 if 62 - 62: OOoOoo00oo
def i1I1i ( ) :
 if 87 - 87: ooo0Oo0 / O0 * I1iiiiI1iII / i1IIi11111i
 with open ( IiII , "a" ) as oo0000ooooO0o :
  Oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  Oo0oOooOoOo = open ( Oo0 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OoOo = re . compile ( '<item>(.+?)</item>' ) . findall ( Oo0oOooOoOo )
  i1IiIiiI ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  if len ( OoOo ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , Iii111II , Oo )
  for ii1i1i1IiII in OoOo :
   i11I1iIiII = re . compile ( '<title>(.+?)</title>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   oo0oooooO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( ii1i1i1IiII ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + i11I1iIiII + '[/COLOR]' , oo0oooooO0 , 2 , I1IiI , I1ii11iIi11i )
   if 19 - 19: oOo0 + i1IIi . iiI1iIiI - ooo0Oo0
 i1IiIiiI ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , Iii111II , Oo )
 if 16 - 16: OOo0o0 + i1Ii / i1IIi11111i
def O00oOoo0OoO0 ( ) :
 if 62 - 62: i1IIi / i1Ii . iiI1iIiI * i1IIi11111i
 with open ( I11i , "w" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 21 - 21: i1IIi11111i
def O0Oo0 ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as oo0000ooooO0o :
  oo0000ooooO0o . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 98 - 98: oOo0
 if 92 - 92: oOo0 - iIii1I11I1II1
 if 32 - 32: OOooO % i1 * i1 + I1iiiiI1iII * i11Ii11I1Ii1i * OOooO
def III1ii1iII ( ) :
 if 11 - 11: OOo0o0 % i11Ii11I1Ii1i
 if 57 - 57: OOoOoo00oo / ooo0Oo0
 oO0O0Ooo = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  IiI1i111IiIiIi1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oO0O0Ooo ) [ 0 ]
  if IiI1i111IiIiIi1 == 'EXPIRED' :
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
  if not 'EXPIRED' in IiI1i111IiIiIi1 :
   i1II11II1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oO0O0Ooo ) [ 0 ]
   II1IIIii = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % i1II11II1 )
   I1I = oOO00oOO ( II1IIIii )
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
  if 40 - 40: Oooo0000 % i1
  if 62 - 62: i1IIi11111i
  if 15 - 15: iI1 + OOooO . OOoOoo00oo * i1 . Oooo0000
  if 18 - 18: i1IIi % i11Ii11I1Ii1i + oOo0 % OOooO
def oOOoO0OO00OOo0 ( url , iconimage , fanart ) :
 if 18 - 18: iiI1iIiI + i1 % iIii1I11I1II1 - i1IIi . OOo0o0
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
  iIi1iIIIiIiI = url . split ( '/' ) [ - 1 ]
  i1iiiIi1i = urllib2 . urlopen ( url )
  OooOo000o0o = os . path . join ( o0OOO , OoO0O00O0oo0O )
  o00O00O0O0O = open ( OooOo000o0o , 'wb' )
  if 42 - 42: OOo0o0 % OOoOoo00oo
  OOO0 = i1iiiIi1i . info ( )
  iIiIIi = int ( OOO0 . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( OoO0O00O0oo0O , iIiIIi ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 14 - 14: i1IIi11111i / OOoOoo00oo - iIii1I11I1II1 - OOo0o0 % i1Ii
  I1iIiI1IiIIII = 0
  I1iiIi111I = 8192
  while True :
   buffer = i1iiiIi1i . read ( I1iiIi111I )
   if not buffer :
    break
    if 34 - 34: i11iIiiIii - i11Ii11I1Ii1i / iiI1iIiI % i1IIi11111i
   I1iIiI1IiIIII += len ( buffer )
   o00O00O0O0O . write ( buffer )
   O0o = "[%3.2f%%]" % ( I1iIiI1IiIIII * 100. / iIiIIi )
   O0o = O0o + chr ( 8 ) * ( len ( O0o ) + 1 )
   iIiiiI . update ( I1iIiI1IiIIII , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( O0o , OoO0O00O0oo0O ) )
   if 33 - 33: OOoOoo00oo
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as oo0000ooooO0o :
   oo0000ooooO0o . write ( '<item>\n<title>' + OoO0O00O0oo0O + '</title>\n<link>' + OooOo000o0o + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 35 - 35: i11iIiiIii - iiI1iIiI / OOoOoo00oo + OOooO * OOo0o0
  o00O00O0O0O . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 49 - 49: i1IIi11111i * OOooO + iI1 + OOoO00o
  if 30 - 30: i1IIi11111i / OOoOoo00oo / I1iiiiI1iII % i1Ii + i11Ii11I1Ii1i
  if 4 - 4: OOoO00o - ooo0Oo0 - I1iiiiI1iII - iI1 % i11iIiiIii / i1
  if 50 - 50: i1Ii + i1IIi
def i11IiIIi11I ( ) :
 o000o0O0Oo00 = [ ]
 ooOOoOo = sys . argv [ 2 ]
 if len ( ooOOoOo ) >= 2 :
  oooOiiIIi = sys . argv [ 2 ]
  i1iiIIiI1iiI = oooOiiIIi . replace ( '?' , '' )
  if ( oooOiiIIi [ len ( oooOiiIIi ) - 1 ] == '/' ) :
   oooOiiIIi = oooOiiIIi [ 0 : len ( oooOiiIIi ) - 2 ]
  I11Ii111I = i1iiIIiI1iiI . split ( '&' )
  o000o0O0Oo00 = { }
  for oO0000OOo00 in range ( len ( I11Ii111I ) ) :
   Oo00OO0 = { }
   Oo00OO0 = I11Ii111I [ oO0000OOo00 ] . split ( '=' )
   if ( len ( Oo00OO0 ) ) == 2 :
    o000o0O0Oo00 [ Oo00OO0 [ 0 ] ] = Oo00OO0 [ 1 ]
 return o000o0O0Oo00
 if 72 - 72: i1IIi / OOo0o0 * oOo0
oooOiiIIi = i11IiIIi11I ( ) ; oo0oooooO0 = None ; OOO0OOO00oo = None ; I11IiIIIi = None ; Oo0o0OOOOO0O = None ; Iii111II = None ; I1I1IiIi1 = None
try : Oo0o0OOOOO0O = urllib . unquote_plus ( oooOiiIIi [ "site" ] )
except : pass
try : oo0oooooO0 = urllib . unquote_plus ( oooOiiIIi [ "url" ] )
except : pass
try : OOO0OOO00oo = urllib . unquote_plus ( oooOiiIIi [ "name" ] )
except : pass
try : I11IiIIIi = int ( oooOiiIIi [ "mode" ] )
except : pass
try : Iii111II = urllib . unquote_plus ( oooOiiIIi [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( oooOiiIIi [ "fanart" ] )
except : pass
try : I1I1IiIi1 = urllib . unquote_plus ( oooOiiIIi [ "description" ] )
except : pass
if 58 - 58: Oooo0000 - OOoO00o - OoooooooOO
if I11IiIIIi == None or oo0oooooO0 == None or len ( oo0oooooO0 ) < 1 : ii11i1iIII ( )
if 96 - 96: iIii1I11I1II1
if 82 - 82: Oooo0000 + O0 - I1iiiiI1iII % OOo0o0 * i11iIiiIii
if 15 - 15: i1IIi11111i
if 39 - 39: OOoOoo00oo / o000o0o00o0Oo / iiI1iIiI * oOo0
if 44 - 44: O0 + i1Ii . iIii1I11I1II1 + ooo0Oo0 / O0 - iI1
elif I11IiIIIi == 1 : oO0OOoO0 ( OOO0OOO00oo , oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 2 : ii ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif I11IiIIIi == 3 : i111i11I1ii ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
if 83 - 83: I1iiiiI1iII * iI1 / ooo0Oo0
if 32 - 32: i1IIi11111i + Oooo0000 - OoooooooOO
if 39 - 39: OoooooooOO * OOoOoo00oo * O0 . iI1 . i1 + i1Ii
elif I11IiIIIi == 4 : i1i ( oo0oooooO0 )
elif I11IiIIIi == 5 : Ii1I1IIii1II ( oo0oooooO0 )
elif I11IiIIIi == 6 : oOo0oO ( )
elif I11IiIIIi == 7 : iiI1Ii1iI1 ( oo0oooooO0 )
elif I11IiIIIi == 8 : oOo0O0o00o ( oo0oooooO0 )
elif I11IiIIIi == 9 : o0iI11I1II ( oo0oooooO0 )
elif I11IiIIIi == 10 : oooOo0OOOoo0 ( oo0oooooO0 )
elif I11IiIIIi == 11 : oOo00oOoO000 ( )
elif I11IiIIIi == 12 : O00o0OO0 ( oo0oooooO0 )
elif I11IiIIIi == 13 : oOOo0 ( oo0oooooO0 )
elif I11IiIIIi == 14 : o0oooOOoOo0 ( oo0oooooO0 )
elif I11IiIIIi == 15 : OOOoOo ( )
elif I11IiIIIi == 16 : o0Oo ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif I11IiIIIi == 17 : iIIi1i1 ( oo0oooooO0 )
elif I11IiIIIi == 18 : oooo0O0 ( oo0oooooO0 )
elif I11IiIIIi == 19 : i11111IIIII ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 20 : OOO ( )
elif I11IiIIIi == 21 : oOooOo0 ( oo0oooooO0 )
elif I11IiIIIi == 22 : o0O0o0 ( oo0oooooO0 )
elif I11IiIIIi == 23 : I1111i ( )
elif I11IiIIIi == 24 : O0OooOo0o ( oo0oooooO0 )
elif I11IiIIIi == 25 : IIiIiI ( oo0oooooO0 , Iii111II )
elif I11IiIIIi == 26 : o0OoOo00o0o ( oo0oooooO0 )
elif I11IiIIIi == 27 : IiiiiI1i1Iii ( oo0oooooO0 , Iii111II )
elif I11IiIIIi == 28 : iIiii1iI1 ( )
elif I11IiIIIi == 29 : IiIiII1 ( oo0oooooO0 )
elif I11IiIIIi == 30 : oooooo0OO ( oo0oooooO0 )
elif I11IiIIIi == 31 : II1I11i ( oo0oooooO0 )
elif I11IiIIIi == 32 : O0OOoOOO0oO ( oo0oooooO0 )
elif I11IiIIIi == 33 : O0oOOoooOO0O ( oo0oooooO0 )
elif I11IiIIIi == 34 : ooo ( oo0oooooO0 )
elif I11IiIIIi == 35 : oOooo0O0o ( )
elif I11IiIIIi == 36 : ooi1i1I ( oo0oooooO0 )
elif I11IiIIIi == 37 : oo0OOo0O ( oo0oooooO0 , Iii111II )
elif I11IiIIIi == 38 : i1i1IIii1i1 ( )
elif I11IiIIIi == 39 : oO00O0 ( oo0oooooO0 )
elif I11IiIIIi == 40 : OOO ( )
elif I11IiIIIi == 41 : oOooOo0 ( oo0oooooO0 )
elif I11IiIIIi == 42 : oO0O ( oo0oooooO0 )
elif I11IiIIIi == 43 : Iiii11iIi1 ( oo0oooooO0 , Iii111II )
elif I11IiIIIi == 44 : I1iii ( )
if 9 - 9: Oooo0000 + OOo0o0 % OoooooooOO + i1IIi11111i
elif I11IiIIIi == 45 : ii1 ( )
elif I11IiIIIi == 46 : oOOOOo0oo0O ( oo0oooooO0 )
elif I11IiIIIi == 47 : ii1O000OOO0OOo ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
elif I11IiIIIi == 48 : oOOO00o000o ( )
elif I11IiIIIi == 49 : ooO0o ( oo0oooooO0 )
elif I11IiIIIi == 50 : OoO0ooO ( oo0oooooO0 )
elif I11IiIIIi == 51 : iiIi ( oo0oooooO0 )
elif I11IiIIIi == 52 : o0OooO0ooo0o ( oo0oooooO0 )
elif I11IiIIIi == 53 : I1iIIi111i1 ( oo0oooooO0 )
elif I11IiIIIi == 54 : o0O0O0 ( oo0oooooO0 , Iii111II )
if 56 - 56: OoooooooOO + o000o0o00o0Oo - OOoO00o
if 24 - 24: i1IIi11111i + i1Ii + iI1 - iIii1I11I1II1
if 49 - 49: iI1 . i1Ii * Oooo0000 % I1iiiiI1iII . O0
elif I11IiIIIi == 59 : iiIi1iI1iIii ( )
elif I11IiIIIi == 60 : IIi ( oo0oooooO0 )
elif I11IiIIIi == 61 : iI111i1II ( OOO0OOO00oo , oo0oooooO0 , Iii111II )
if 48 - 48: O0 * OOooO - O0 / OOooO + Oooo0000
elif I11IiIIIi == 66 : II11iI111i1 ( )
elif I11IiIIIi == 67 : I11 ( oo0oooooO0 )
elif I11IiIIIi == 68 : I1Iiiiiii ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 69 : O0Oo00O ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 70 : OOooOOOOOOooo ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 71 : oO0oOOoo00000 ( )
elif I11IiIIIi == 72 : OO00 ( )
elif I11IiIIIi == 73 : II1Ii1iI1i1 ( )
elif I11IiIIIi == 74 : oooo0OO ( oo0oooooO0 )
elif I11IiIIIi == 75 : I1i1111I ( oo0oooooO0 )
elif I11IiIIIi == 76 : OOooOO00O0OO00oo ( )
elif I11IiIIIi == 77 : I111i1I1 ( )
if 52 - 52: i1 % OOooO * i11Ii11I1Ii1i
if 4 - 4: iI1 % O0 - OoooooooOO + i1Ii . OOo0o0 % i11Ii11I1Ii1i
elif I11IiIIIi == 884 : i1II ( )
elif I11IiIIIi == 885 : O0Oo0 ( )
elif I11IiIIIi == 886 : i1I1i ( )
elif I11IiIIIi == 887 : oOOoO0OO00OOo0 ( oo0oooooO0 , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 888 : oooO ( )
elif I11IiIIIi == 889 : iiiIiI ( oo0oooooO0 , I11IiIIIi , OOO0OOO00oo , Iii111II , I1ii11iIi11i )
elif I11IiIIIi == 890 : Ii ( )
elif I11IiIIIi == 891 : O00oOoo0OoO0 ( )
elif I11IiIIIi == 892 : o0O0OO ( )
if 9 - 9: i11Ii11I1Ii1i * i11Ii11I1Ii1i . i11iIiiIii * iIii1I11I1II1
III1ii1iII ( )
if I11IiIIIi == None or oo0oooooO0 == None or len ( oo0oooooO0 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 18 - 18: i1 . i11Ii11I1Ii1i % Oooo0000 % OOooO
if 87 - 87: iIii1I11I1II1 . OoooooooOO * Oooo0000
if 100 - 100: i1 / i1IIi - iiI1iIiI % OOooO - iIii1I11I1II1
if 17 - 17: iI1 / i1IIi11111i % ooo0Oo0
if 71 - 71: I1iiiiI1iII . oOo0 . i1
if 68 - 68: i11iIiiIii % OOo0o0 * i1 * I1iiiiI1iII * i11Ii11I1Ii1i + O0
if 66 - 66: iI1 % o000o0o00o0Oo % OoooooooOO
if 34 - 34: i1IIi11111i / OOoO00o % O0 . i1 . i1IIi
if 29 - 29: O0 . oOo0
if 66 - 66: OOo0o0 * iIii1I11I1II1 % iIii1I11I1II1 * I1iiiiI1iII - i1Ii - I1iiiiI1iII
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
