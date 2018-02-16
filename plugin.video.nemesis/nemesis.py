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
import webbrowser
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
 o0o0OOO0o0 = ooOOOo0oo0O0 ( )
 if o0o0OOO0o0 == 'android' :
  o0 = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://pinsystem.co.uk' ) )
 else :
  o0 = webbrowser . open ( 'https://pinsystem.co.uk' )
  if 9 - 9: OOooO + OOo0o0 % OOooO + i1IIi . OOoOoo00oo
def ooOOOo0oo0O0 ( ) :
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
  if 31 - 31: i1IIi11111i + iI1 + iI1 / i11Ii11I1Ii1i
def iiI1 ( ) :
 if 19 - 19: iI1 + i1Ii
 ooIiII1I1i1i1ii ( )
 ooo ( )
 IiiiI1II1I1 ( )
 ii1I1i1I = i1iII1IiiIiI1
 OOoo0O0 = ii1I1i1I
 iiiIi1i1I = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( iiiIi1i1I >= 0000 ) and ( iiiIi1i1I <= 1159 ) : oOO00oOO = "Morning"
 elif ( iiiIi1i1I >= 1200 ) and ( iiiIi1i1I <= 1759 ) : oOO00oOO = "Afternoon"
 else : oOO00oOO = "Evening"
 OoOo ( '[COLOR yellow]Good[COLOR aqua] ' + str ( oOO00oOO ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 OoOo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  iI = o00O ( i1iII1IiiIiI1 )
  OOO0OOO00oo = re . compile ( '<item>(.+?)</item>' ) . findall ( iI )
  for Iii111II in OOO0OOO00oo :
   try :
    if '<m3u>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 11 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<mamahdsports>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 14 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<atc>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<atc>(.+?)</atc>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 6 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<scanner>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 11 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<cartoons>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 29 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<Adult>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 38 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<Anime>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 51 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<audiobooks>' in Iii111II :
     iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     ii1I1i1I = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( Iii111II ) [ 0 ]
     ii11i1 ( iiii11I , ii1I1i1I , 59 , Ooo0OO0oOO , I1ii11iIi11i )
    elif '<folder>' in Iii111II :
     IIIii1II1II = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Iii111II )
     for iiii11I , ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i in IIIii1II1II :
      ii11i1 ( iiii11I , ii1I1i1I , 1 , Ooo0OO0oOO , I1ii11iIi11i )
    else :
     i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( Iii111II )
     if len ( i1I1iI ) == 1 :
      IIIii1II1II = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Iii111II )
      oo0OooOOo0 = len ( OOO0OOO00oo )
      for iiii11I , ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i in IIIii1II1II :
       if 'youtube.com/playlist' in ii1I1i1I :
        ii11i1 ( iiii11I , ii1I1i1I , 2 , Ooo0OO0oOO , I1ii11iIi11i )
       else :
        OoOo ( iiii11I , ii1I1i1I , 2 , Ooo0OO0oOO , I1ii11iIi11i )
     elif len ( i1I1iI ) > 1 :
      iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
      Ooo0OO0oOO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
      OoOo ( iiii11I , OOoo0O0 , 3 , Ooo0OO0oOO , I1ii11iIi11i )
   except : pass
   if 92 - 92: OOoO00o . iI1 + i1IIi11111i
  OoOo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.resolveurl/settings.xml" )
   oOO00oOO = open ( file ) . read ( )
   IiII1I11i1I1I = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( oOO00oOO ) [ 0 ]
   IiII1I11i1I1I = IiII1I11i1I1I . strip ( )
   ii1I1i1I = 'plugin://script.module.resolveurl/?mode=auth_rd'
   if 'value=""' in IiII1I11i1I1I :
    oO0Oo = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    OoOo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( oO0Oo ) + '[/COLOR]' , ii1I1i1I , 2 , I1IiI , Oo )
   else :
    oO0Oo = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    OoOo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( oO0Oo ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  oOOoo0Oo = 'https://i.imgur.com/o2Wvut7.jpg'
  ii11i1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , oOOoo0Oo , Oo )
  o00OO00OoO = 'https://i.imgur.com/SxZzRX9.jpg'
  ii11i1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , o00OO00OoO , Oo )
  OOOO0OOoO0O0 = 'https://i.imgur.com/zme6vuj.jpg'
  ii11i1 ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , OOOO0OOoO0O0 , Oo )
 except :
  O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if O0Oo000ooO00 == 0 :
   OoOo ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   ii11i1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if O0Oo000ooO00 == 1 :
   quit ( )
   if 75 - 75: OOo0o0 . i1 * OOoOoo00oo
 iii11iII ( )
 if 91 - 91: OOooO
def iII ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OOoo0O0 = url
 iI = o00O ( url )
 IiiiI1II1I1 ( )
 OOO0OOO00oo = re . compile ( '<item>(.+?)</item>' ) . findall ( iI )
 for Iii111II in OOO0OOO00oo :
  try :
   if '<image>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 23 , iconimage , fanart )
   elif '<American>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 77 , iconimage , fanart )
   elif '<lordjd>' in Iii111II :
    i1I1iI = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( Iii111II )
    if len ( i1I1iI ) == 1 :
     IIIii1II1II = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Iii111II )
     oo0OooOOo0 = len ( OOO0OOO00oo )
     for name , url , iconimage , fanart in IIIii1II1II :
      if 'youtube.com/playlist' in url :
       ii11i1 ( name , url , 2 , iconimage , fanart )
      else :
       o0ooOooo000oOO ( name , url , 2 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     o0ooOooo000oOO ( name , OOoo0O0 , 3 , iconimage , fanart )
   elif '<reddit>' in Iii111II :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( Iii111II ) [ 0 ]
    ii11i1 ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in Iii111II :
    i1I1iI = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Iii111II )
    if len ( i1I1iI ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Iii111II ) [ 0 ]
     Oo0oOOo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Iii111II ) [ 0 ]
     Oo0OoO00oOO0o = Oo0oOOo
     OOO00O = "/"
     if not Oo0OoO00oOO0o . endswith ( OOO00O ) :
      OOoOO0oo0ooO = Oo0OoO00oOO0o + "/"
     else :
      OOoOO0oo0ooO = Oo0OoO00oOO0o
     iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = iI + '%26referer=' + OOoOO0oo0ooO
     OoOo ( name , url , 10 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     OoOo ( name , OOoo0O0 , 16 , iconimage , fanart )
     if 98 - 98: OOoO00o * OOoO00o / OOoO00o + iI1
   elif '<folder>' in Iii111II :
    IIIii1II1II = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Iii111II )
    for name , url , iconimage , fanart in IIIii1II1II :
     ii11i1 ( name , url , 1 , iconimage , fanart )
     if 34 - 34: i1Ii
   else :
    i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( Iii111II )
    if len ( i1I1iI ) == 1 :
     IIIii1II1II = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Iii111II )
     oo0OooOOo0 = len ( OOO0OOO00oo )
     for name , url , iconimage , fanart in IIIii1II1II :
      if 'youtube.com/playlist' in url :
       ii11i1 ( name , url , 2 , iconimage , fanart )
      else :
       OoOo ( name , url , 2 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Iii111II ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii111II ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Iii111II ) [ 0 ]
     OoOo ( name , OOoo0O0 , 3 , iconimage , fanart )
  except : pass
  if 15 - 15: iI1 * i1Ii * ooo0Oo0 % i11iIiiIii % Oooo0000 - OOoOoo00oo
 iii11iII ( )
 if 68 - 68: oOo0 % i1IIi . I1iiiiI1iII . o000o0o00o0Oo
 if 92 - 92: OOoO00o . oOo0
 if 31 - 31: oOo0 . Oooo0000 / O0
 if 89 - 89: Oooo0000
 if 68 - 68: i1 * OoooooooOO % O0 + i1 + i1Ii
 if 4 - 4: i1Ii + O0 * OOoOoo00oo
 if 55 - 55: ooo0Oo0 + iIii1I11I1II1 / Oooo0000 * OOo0o0 - i11iIiiIii - OOooO
 if 25 - 25: o000o0o00o0Oo
def Ii1i ( url ) :
 if 15 - 15: I1iiiiI1iII . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - OOooO . i1IIi
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  try :
   i1O0OoO0o = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   ii11i1 ( "[COLOR skyblue]" + i1O0OoO0o + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 79 - 79: Oooo0000 - O0 * i1 + Oooo0000 % O0 * O0
def oOOo0 ( url ) :
 if 54 - 54: O0 - I1iiiiI1iII % OOoOoo00oo
 OOoO = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 iIIii1ii11IIIiiI = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 OoOo ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 iI = o00O ( url )
 i1I1iI = 0
 O00OOOoOoo0O = re . compile ( 'href="([^"]+)' ) . findall ( iI )
 for url in O00OOOoOoo0O :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in OOoO ) :
    i1I1iI += 1
    i1O0OoO0o = "Link " + str ( i1I1iI ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    O000OOo00oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     OoOo ( "[COLOR skyblue]" + i1O0OoO0o + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in iIIii1ii11IIIiiI ) :
     OoOo ( "[COLOR yellow]" + i1O0OoO0o + url + "[/COLOR]" , O000OOo00oo , 2 , I1IiI , I1ii11iIi11i )
    else :
     OoOo ( "[COLOR skyblue]" + i1O0OoO0o + url + "[/COLOR]" , O000OOo00oo , 2 , I1IiI , I1ii11iIi11i )
     if 71 - 71: i11iIiiIii + I1iiiiI1iII
     if 57 - 57: OOo0o0 . iI1 . i1IIi
     if 42 - 42: iI1 + o000o0o00o0Oo % O0
def i1iIIIi1i ( url ) :
 if 43 - 43: Oooo0000 % OOoOoo00oo
 if url == 'Football' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  iiiiiiii1 = o00O ( 'http://wizhdsports.is/sport/Cricket' )
 iI11i1ii11 = dom_parser2 . parse_dom ( iiiiiiii1 , 'div' , { 'class' : 'card' } )
 iI11i1ii11 = [ ( dom_parser2 . parse_dom ( OOooo0O00o , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( OOooo0O00o , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( OOooo0O00o , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( OOooo0O00o , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for OOooo0O00o in iI11i1ii11 ]
 if len ( iI11i1ii11 ) < 1 :
  OoOo ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , Ooo0OO0oOO , Oo , '' )
 iI11i1ii11 = [ ( OOooo0O00o [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , OOooo0O00o [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , OOooo0O00o [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , OOooo0O00o [ 2 ] [ 0 ] . content ) if OOooo0O00o [ 2 ] else 'Upcoming' , OOooo0O00o [ 3 ] [ 0 ] . content ) for OOooo0O00o in iI11i1ii11 ]
 if 85 - 85: i1IIi11111i - ooo0Oo0
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - i1IIi11111i
 if 91 - 91: OOoO00o % i1IIi % iIii1I11I1II1
 if 20 - 20: OOoOoo00oo % OOooO / OOooO + OOooO
 iI11i1ii11 = [ ( OOooo0O00o [ 0 ] , OOooo0O00o [ 1 ] , OOooo0O00o [ 2 ] , OOooo0O00o [ 3 ] , OOooo0O00o [ 4 ] ) for OOooo0O00o in iI11i1ii11 ]
 III1IiiI = 0
 iIi1 = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for OOooo0O00o in iI11i1ii11 :
  IIIII11I1IiI = OOooo0O00o [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( III1IiiI ) )
  III1IiiI += 1
  time . sleep ( 0.10 )
  IIIII11I1IiI = i1I ( IIIII11I1IiI )
  OoOO = OOooo0O00o [ 1 ]
  ooOOO0 = OOooo0O00o [ 3 ]
  if 'Match Over' in ooOOO0 :
   iIi1 += 1
  o0o = dom_parser2 . parse_dom ( OOooo0O00o [ 4 ] , 'a' )
  for iiiiiiii1 in o0o :
   O0OOoO00OO0o = re . sub ( '<.+?>' , '' , iiiiiiii1 . content )
   iI = iiiiiiii1 . attrs [ 'href' ]
   iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + iI
   if not 'Match Over' in ooOOO0 :
    OoOo ( '[COLOR aqua]' + IIIII11I1IiI + '[COLOR yellow]' + ' ' + ooOOO0 + '[/COLOR]' , iI , 2 , Ooo0OO0oOO , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( III1IiiI ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( iIi1 ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 38 - 38: OOoOoo00oo % iI1 % i1IIi11111i % i1 - ooo0Oo0
def i1Iiii111iI1iIi1 ( url ) :
 if 78 - 78: i1 . OOoOoo00oo + i1 / iI1 / i1
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = re . compile ( 'title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  if 54 - 54: Oooo0000 % OOoO00o
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 37 - 37: Oooo0000 * ooo0Oo0 / i1Ii - OOoO00o % i11Ii11I1Ii1i . OOo0o0
 try :
  O00I1iI1 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( iI ) [ 0 ]
  I1IiI = Ooo0OO0oOO
  ii11i1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , O00I1iI1 , 18 , Ooo0OO0oOO , Oo , '' )
 except : pass
 if 23 - 23: i11iIiiIii + i1IIi11111i . i1IIi
def o0Ooo00o0Oooo ( url , iconimage , fanart ) :
 if 84 - 84: i1IIi11111i % i11Ii11I1Ii1i . i11iIiiIii / i1
 OoOo ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( iI )
 if 80 - 80: oOo0 . i11iIiiIii - i1IIi11111i
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  O000OOo00oo = str . lower ( url )
  if '1e' in O000OOo00oo :
   i1O0OoO0o = '1st Half'
  else :
   i1O0OoO0o = '2nd Half'
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 25 - 25: i1
def oOo0oO ( ) :
 if 51 - 51: ooo0Oo0 - OOo0o0 + i11Ii11I1Ii1i * OOooO . iI1 + OOo0o0
 ii1I1i1I = 'http://www.goalsarena.org/en/'
 iI = o00O ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for oO0o0Ooooo , OOo0oO00ooO00 in OoO0o :
  ii11i1 ( "[COLOR skyblue]" + OOo0oO00ooO00 + "[/COLOR]" , oO0o0Ooooo , 21 , I1IiI , Oo , '' )
  if 90 - 90: Oooo0000 * oOo0 + i1IIi11111i
def OO ( url ) :
 if 83 - 83: O0 / iiI1iIiI - i1 - OOoOoo00oo
 if 36 - 36: I1iiiiI1iII
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if O0Oo000ooO00 == 0 :
  try :
   OOO0OOO00oo = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in OOO0OOO00oo :
   I11iI ( iiii11I , OOO0OOO00oo , Ooo0OO0oOO )
  I1iI1ii1II = o00O ( OOO0OOO00oo )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
  url = 'https:' + url
  O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = Ooo0OO0oOO , thumbnailImage = Ooo0OO0oOO )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  quit ( 0 )
 if O0Oo000ooO00 == 1 :
  try :
   OOO0OOO00oo = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   OO ( url )
  I1iI1ii1II = o00O ( OOO0OOO00oo )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
  url = 'https:' + url
  O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = Ooo0OO0oOO , thumbnailImage = Ooo0OO0oOO )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  quit ( 0 )
  if 74 - 74: o000o0o00o0Oo + i11Ii11I1Ii1i / i1
def oOo0O0Oo00oO ( ) :
 if 7 - 7: I1iiiiI1iII * oOo0 % OOooO - i1IIi11111i
 ii1I1i1I = 'http://m.liveatc.net/feeds/'
 iI = i1i ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://m.liveatc.net' + ii1I1i1I
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 7 , I1IiI , Oo , '' )
  if 56 - 56: o000o0o00o0Oo % O0 - iiI1iIiI
def O00o0OO0 ( url ) :
 if 35 - 35: OOo0o0 % i1Ii / oOo0 + iIii1I11I1II1 . OoooooooOO . iiI1iIiI
 if 71 - 71: I1iiiiI1iII * i11Ii11I1Ii1i * OOo0o0
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 56 - 56: iiI1iIiI
def O0oO ( url ) :
 url = url . replace ( ' ' , '%20' )
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li>(.+?)</a>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '(.+?)</li>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 73 - 73: o000o0o00o0Oo * i11iIiiIii % OOo0o0 . o000o0o00o0Oo
def OOOOo0 ( url ) :
 if 49 - 49: i11Ii11I1Ii1i % O0 . Oooo0000 + OOo0o0 / iiI1iIiI
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  try :
   i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   OoOo ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 72 - 72: i1Ii * ooo0Oo0 . iiI1iIiI - i11Ii11I1Ii1i + i1IIi
def iIi1ii ( ) :
 if 58 - 58: Oooo0000 % i1IIi11111i
 ii11i1 ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 ii1I1i1I = 'http://m.broadcastify.com/?a=la&coid=1'
 iI = i1i ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://m.broadcastify.com' + ii1I1i1I
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 12 , I1IiI , Oo , '' )
  if 50 - 50: oOo0 . i1IIi11111i
def ooO0OO ( url ) :
 if 54 - 54: I1iiiiI1iII + OOooO % i1 + OoooooooOO - O0 - i1IIi11111i
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 77 - 77: OOoOoo00oo * iIii1I11I1II1
def oO00oOOoooO ( url ) :
 if 46 - 46: iiI1iIiI - OoooooooOO - iI1 * i11Ii11I1Ii1i
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 34 - 34: iI1 - OOoO00o / OOoOoo00oo + o000o0o00o0Oo * OOooO
def OOOO0OoOO0o0o ( url ) :
 if 95 - 95: i11iIiiIii
 iI = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  OOO0OOO00oo = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( iI ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 iI1111iiii ( OOO0OOO00oo )
 if 67 - 67: OoooooooOO / iiI1iIiI * OOooO + iI1
def OooOo0ooo ( ) :
 if 71 - 71: oOo0 + OOooO
 ii1I1i1I = 'http://m.broadcastify.com/?a=top25'
 iI = i1i ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  iI1111ii1I = i1O0OoO0o . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  i1O0OoO0o = i1O0OoO0o . split ( ')' ) [ - 1 ] . strip ( )
  ii1I1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://m.broadcastify.com' + ii1I1i1I
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[COLOR yellow] :: " + iI1111ii1I + " Listening" + "[/COLOR]" , ii1I1i1I , 14 , I1IiI , Oo , '' )
  if 45 - 45: i1IIi + i1IIi11111i
def OOO ( url ) :
 if 25 - 25: OOo0o0 - i1 . iIii1I11I1II1 % i11iIiiIii % o000o0o00o0Oo
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in i1O0OoO0o :
    O000OOo00oo = 'https://www.youtube.com' + url
    OoOo ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , O000OOo00oo , 2 , I1IiI , I1ii11iIi11i )
    if 92 - 92: OoooooooOO * oOo0
def o0000oO ( ) :
 if 11 - 11: i1Ii / Oooo0000 - I1iiiiI1iII * OoooooooOO + OoooooooOO . Oooo0000
 ii1I1i1I = 'http://burningwhee1s.blogspot.co.uk/'
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for iI , i1O0OoO0o in OoO0o :
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , iI , 24 , I1IiI , Oo , '' )
  if 26 - 26: OOooO % o000o0o00o0Oo
def o00Oo0oooooo ( url ) :
 if 76 - 76: iI1 / OOoOoo00oo . O0 % iiI1iIiI . i1IIi11111i + I1iiiiI1iII
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 71 - 71: oOo0 . i11Ii11I1Ii1i
def oo0 ( url , iconimage ) :
 if 61 - 61: Oooo0000 - OOoOoo00oo - i1IIi
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( OOO0OOO00oo )
 try :
  for i1I1iI in OoO0o :
   i1O0OoO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    IiI1iIiIIIii = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     IiI1iIiIIIii = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     IiI1iIiIIIii = ''
   i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
   IiI1iIiIIIii = o0Oo0oO0oOO00 ( IiI1iIiIIIii )
   oOoO = re . compile ( '<option value="(.+?)"' ) . findall ( i1I1iI ) [ 1 ]
   OoOo ( "[COLOR aqua]" + i1O0OoO0o + "  " + IiI1iIiIIIii + "[/COLOR]" , oOoO , 2 , I1IiI , Oo , '' )
 except :
  OoOo ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 81 - 81: Oooo0000 - Oooo0000 . OOoO00o
def o0OoOo00o0o ( ) :
 if 41 - 41: i1Ii % i1 - ooo0Oo0 * oOo0 * ooo0Oo0
 if 69 - 69: OOoOoo00oo - OoooooooOO + i1IIi11111i - iI1
 ii1I1i1I = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 iI = o00O ( ii1I1i1I )
 IIIii1II1II = json . loads ( iI )
 ii = IIIii1II1II [ 'results' ]
 for O0oOo00o in ii :
  o0ooooO0o0O = 'https://image.tmdb.org/t/p/original'
  i1O0OoO0o = O0oOo00o [ 'title' ]
  I1IiI = O0oOo00o [ 'poster_path' ]
  iiIi11iI1iii = O0oOo00o [ 'id' ]
  I1IiI = o0ooooO0o0O + I1IiI
  I1ii11iIi11i = O0oOo00o [ 'backdrop_path' ]
  I1ii11iIi11i = o0ooooO0o0O + I1ii11iIi11i
  oo000 = O0oOo00o [ 'overview' ]
  iiIi11iI1iii = str ( iiIi11iI1iii )
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , i1O0OoO0o , 33 , I1IiI , I1ii11iIi11i , oo000 )
  if 63 - 63: i1Ii + OOoOoo00oo * OOooO
def iI1I111I ( url ) :
 if 97 - 97: i1IIi . OOo0o0 / OOoO00o * O0
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = re . compile ( '<i>(.+?)</i>' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = i1O0OoO0o . strip ( )
  ii11i1 ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o0O0o = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( iI ) [ 0 ]
  OO0o0o00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  ii11i1 ( '[COLOR yellow]Next Page >>[/COLOR]' , o0O0o , 26 , OO0o0o00 , I1ii11iIi11i )
 except : pass
 if 12 - 12: i1IIi + i1IIi - o000o0o00o0Oo * ooo0Oo0 % ooo0Oo0 - i11Ii11I1Ii1i
def o0O ( url , iconimage ) :
 if 84 - 84: i1 + i1IIi - i11Ii11I1Ii1i . o000o0o00o0Oo * OoooooooOO + iiI1iIiI
 iI = o00O ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( iI ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 OOO0OOO00oo = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( iI )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 OOooo0O00o = 1
 II1i11I = [ ]
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  II1i11I . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( OOooo0O00o ) )
  time . sleep ( 0.02 )
  OOooo0O00o += 1
  i1O0OoO0o = re . compile ( '(.+?)</p>' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'Server' , '' )
  i1O0OoO0o = i1O0OoO0o . strip ( )
 ii1I1IIii11 = 1
 oOO00oOO = 0
 O0o0oO = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 38 - 38: OOo0o0 % Oooo0000 + o000o0o00o0Oo . i11iIiiIii
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if oOO00oOO > len ( II1i11I ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 53 - 53: i11iIiiIii * OOoO00o
  if O0o0oO == 0 :
   oOO00oOO += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( oOO00oOO ) + "[/COLOR]" , '' )
   try :
    iI = o00O ( II1i11I [ oOO00oOO ] )
    OoO0o = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( iI ) [ 0 ]
    OooooO0oOOOO = base64 . b64decode ( OoO0o )
    url = re . compile ( 'src="(.+?)"' ) . findall ( OooooO0oOOOO ) [ 0 ]
    o0O00oOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    i1I1iIi = open ( o0O00oOOoo ) . read ( )
    IIii11Ii1i1I = re . compile ( '<url>(.+?)</url>' ) . findall ( i1I1iIi )
    for Oooo0O in IIii11Ii1i1I :
     oo00O0oO0O0 = re . compile ( '<bad>(.+?)<bad>' ) . findall ( Oooo0O ) [ 0 ]
     if url == oo00O0oO0O0 :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( oOO00oOO ) )
      time . sleep ( 0.5 )
      O0o0oO = 5
      pass
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     ooo0OO0O0Oo = liveresolver . resolve ( url )
    else : ooo0OO0O0Oo = url
    O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( oOO00oOO ) )
    time . sleep ( 0.5 )
    O0o0oO = 5
    pass
  if O0o0oO == 5 :
   O0o0oO = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   O0o0oO += 1
   if 62 - 62: O0 % iI1 . iI1 - iIii1I11I1II1 / i11iIiiIii
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 o0O00oOOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 Oo0OoO00oOO0o = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if Oo0OoO00oOO0o :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( o0O00oOOoo , "a" ) as iiiII :
   iiiII . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 41 - 41: ooo0Oo0
def IIiIi ( url ) :
 if 91 - 91: o000o0o00o0Oo * ooo0Oo0 / iiI1iIiI . O0 + i1 + Oooo0000
 if 8 - 8: OOo0o0 / o000o0o00o0Oo
 if url == 'search' :
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Search Term' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1 . lower ( )
    if 55 - 55: i1Ii - iI1 + i11Ii11I1Ii1i + OOoO00o % OOooO
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , Ooo0OO0oOO , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , Ooo0OO0oOO , 5000 )
   quit ( )
  ooO0OoOO = ooO0OoOO . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + ooO0OoOO + '.html'
  iiI11i1II ( url , I1IiI )
  if 51 - 51: i1IIi11111i % ooo0Oo0 % i1IIi11111i * O0 - OOoOoo00oo % ooo0Oo0
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  iiI11i1II ( url , I1IiI )
  if 65 - 65: i1Ii
def iiI11i1II ( url , icon ) :
 if 68 - 68: i1Ii % i11iIiiIii + i11Ii11I1Ii1i
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = re . compile ( '<i>(.+?)</i>' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii11i1 ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 52 - 52: o000o0o00o0Oo - ooo0Oo0 + o000o0o00o0Oo % i1IIi11111i
def iI1IiI ( ) :
 if 21 - 21: i1 + iiI1iIiI % iiI1iIiI
 ii1I1i1I = 'http://www.genti.stream/'
 iI = o00O ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  oO0o0oooO0oO = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ] . strip ( )
  IiIiII1 = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( i1I1iI ) [ 1 ] . strip ( )
  ii1I1i1I = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://www.genti.stream/' + ii1I1i1I
  OoOo ( "[COLOR aqua]" + oO0o0oooO0oO + "[COLOR yellow] vs [COLOR aqua]" + IiIiII1 + "[/COLOR]" , ii1I1i1I , 39 , I1IiI , I1ii11iIi11i )
  if 21 - 21: O0 % I1iiiiI1iII . iiI1iIiI / i11Ii11I1Ii1i + I1iiiiI1iII
def OOOO0O00o ( url ) :
 if 62 - 62: iIii1I11I1II1
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1II = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( iI ) [ 0 ]
 if not 'http' in i1II :
  i1II = 'http://www.genti.stream' + i1II
 oO0o0Ooooo = o00O ( i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI1I = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( oO0o0Ooooo ) [ 0 ]
 I1iI1ii1II = o00O ( iI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( I1iI1ii1II ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( I1iI1ii1II ) [ 0 ]
 except : pass
 if 100 - 100: iIii1I11I1II1 + Oooo0000 / ooo0Oo0 . i11iIiiIii
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , Ooo0OO0oOO , 5000 )
  quit ( )
 I11iI ( iiii11I , url , Ooo0OO0oOO )
 if 14 - 14: i1IIi11111i * OOoOoo00oo + OOoO00o + O0 + i11iIiiIii
 if 77 - 77: i1IIi11111i / OoooooooOO
def IIii11I1i1I ( url ) :
 if 99 - 99: OOoO00o
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 OOoo0O0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( OOoo0O0 ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for url , i1O0OoO0o in OoO0o :
  url = 'http://kimcartoon.me/CartoonList' + url
  ii11i1 ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 17 - 17: i1IIi
def iiIi1i ( url ) :
 if 27 - 27: OOoOoo00oo * i1Ii . oOo0 % I1iiiiI1iII * I1iiiiI1iII . i1IIi
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 OOoo0O0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( OOoo0O0 )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   O0OOoOOO0oO = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( i1I1iI ) [ 0 ]
   O0OOoOOO0oO = o0Oo0oO0oOO00 ( O0OOoOOO0oO )
  except IndexError :
   O0OOoOOO0oO = ''
  ii11i1 ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , O0OOoOOO0oO )
  if 28 - 28: i1Ii + i11iIiiIii / iI1 % Oooo0000 % ooo0Oo0 - O0
 try :
  ooo0OOO = re . compile ( '<li>(.+?)Next' ) . findall ( OOoo0O0 )
  for i1I1iI in ooo0OOO :
   o0O0o = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ - 1 ]
   iii1Ii1Ii1 = 'http://kimcartoon.me' + o0O0o
   IIi = 'https://i.imgur.com/pOefPvV.jpg'
   ii11i1 ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , iii1Ii1Ii1 , 30 , IIi , I1ii11iIi11i )
 except : pass
 if 94 - 94: i11Ii11I1Ii1i - ooo0Oo0
def oo0oO0 ( url ) :
 if 1 - 1: i1IIi . i11iIiiIii % OOoOoo00oo
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 OOoo0O0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<td>(.+?)</td>' ) . findall ( OOoo0O0 )
 for i1I1iI in OOO0OOO00oo :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   i1O0OoO0o = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   OoOo ( "[COLOR aqua][B]" + i1O0OoO0o + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 82 - 82: iIii1I11I1II1 + ooo0Oo0 . iIii1I11I1II1 % I1iiiiI1iII / OOooO . OOooO
def IIioOoO00oo0O ( url ) :
 if 39 - 39: iIii1I11I1II1 / O0 / OOo0o0 - OOooO - OOoO00o % OOoOoo00oo
 O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if O0Oo000ooO00 == 0 :
  url = url + '&s=rapidvideo'
  oOO0O00o0OO0O = cfscrape . create_scraper ( )
  OOoo0O0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   OoO0o = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( OOoo0O0 )
   for iI in OoO0o :
    url = re . compile ( 'src="(.+?)"' ) . findall ( iI ) [ 0 ]
    if 'rapidvideo' in url :
     I11iI ( iiii11I , url , Ooo0OO0oOO )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if O0Oo000ooO00 == 1 :
  url = url + '&s=openload'
  oOO0O00o0OO0O = cfscrape . create_scraper ( )
  OOoo0O0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   OoO0o = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( OOoo0O0 )
   for iI in OoO0o :
    url = re . compile ( 'src="(.+?)"' ) . findall ( iI ) [ 0 ]
    I11iI ( iiii11I , url , Ooo0OO0oOO )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 31 - 31: iI1 - O0 / i1Ii * Oooo0000
   if 12 - 12: i1IIi11111i - i1Ii * oOo0
def II1111ii ( ) :
 if 27 - 27: O0
 ii1I1i1I = "http://www.loyalbooks.com/genre-menu"
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( iI )
 for Iii111II in OOO0OOO00oo :
  if "paid" not in Iii111II :
   oO0o0Ooooo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
   I1iI1ii1II = "http://www.loyalbooks.com" + oO0o0Ooooo
   iiii11I = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
   ii11i1 ( "[COLOR aqua]" + iiii11I + "[/COLOR]" , I1iI1ii1II , 60 , I1IiI , Oo , '' )
   if 79 - 79: i1IIi11111i - iI1 + i1IIi11111i . OOo0o0
def ii1III11 ( url ) :
 if 7 - 7: OOoO00o % O0 . Oooo0000 + iiI1iIiI - iI1
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( iI ) [ 0 ]
 o0o0O00oo0 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( OOO0OOO00oo )
 for Iii111II in o0o0O00oo0 :
  O000OOo00oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  I1iI1ii1II = "http://www.loyalbooks.com" + O000OOo00oo
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  Ooo0OO0oOO = "http://www.loyalbooks.com" + I1IiI
  iiii11I = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  ii11i1 ( "[COLOR aqua]" + iiii11I + "[/COLOR]" , I1iI1ii1II , 61 , Ooo0OO0oOO , Oo , '' )
 try :
  iI = o00O ( url )
  O00I1iI1 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( iI ) [ 0 ]
  I1IiI = 'https://i.imgur.com/pOefPvV.jpg'
  ii11i1 ( "[COLOR yellow]Next Page -->[/COLOR]" , O00I1iI1 , 60 , I1IiI , Oo , '' )
 except : pass
 if 27 - 27: i11iIiiIii % i11Ii11I1Ii1i % iI1 . O0 - ooo0Oo0 + Oooo0000
 if 57 - 57: iIii1I11I1II1 / iI1 - i1IIi
def ooOOo00O00Oo ( name , url , iconimage ) :
 if 42 - 42: O0 / i1IIi11111i + OoooooooOO * i1Ii % i1Ii
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( iI )
 for Iii111II in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  O000OOo00oo = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , O000OOo00oo , 10 , iconimage , Oo , '' )
  if 7 - 7: OOoO00o / o000o0o00o0Oo / i11iIiiIii
def IIIII ( ) :
 if 78 - 78: OOooO * i1IIi
 ii1I1i1I = 'http://www.shadownet.me/'
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for ii1I1i1I , i1O0OoO0o in OoO0o :
  i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
  if 'P2P' not in i1O0OoO0o :
   ii11i1 ( "[COLOR skyblue]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 49 , I1IiI , Oo , '' )
   if 1 - 1: iiI1iIiI / I1iiiiI1iII * i1Ii
   if 1 - 1: iI1 * i1IIi11111i . Oooo0000 / O0
def O00O0ooo0 ( url ) :
 if 8 - 8: i1Ii + i11Ii11I1Ii1i / OOoO00o / iI1
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for i1I1iI in OoO0o :
  i1O0OoO0o = re . compile ( 'alt="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  OoOo ( "[COLOR skyblue]" + i1O0OoO0o + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o0O0o = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( iI ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  ii11i1 ( "[COLOR orange]Next Page --->[/COLOR]" , o0O0o , 49 , I1IiI , Oo , '' )
 except : pass
 if 74 - 74: O0 / i1IIi
def OoO ( url ) :
 if 41 - 41: i1IIi * i11Ii11I1Ii1i / OoooooooOO . OOoOoo00oo
 def O0iII1 ( url ) :
  IIII1i = urllib2 . Request ( url )
  IIII1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  IIII1i . add_header ( 'Referer' , url )
  Ii1IIIIi1ii1I = urllib2 . urlopen ( IIII1i , timeout = 5 )
  iI = Ii1IIIIi1ii1I . read ( )
  Ii1IIIIi1ii1I . close ( )
  return iI
  if 13 - 13: iiI1iIiI % Oooo0000 . o000o0o00o0Oo / ooo0Oo0 % OOoOoo00oo . OoooooooOO
 iI = O0iII1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  OOO0OOO00oo = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( iI ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in OOO0OOO00oo :
  url = OOO0OOO00oo
  I11iI ( iiii11I , url , Ooo0OO0oOO )
 I1iI1ii1II = O0iII1 ( OOO0OOO00oo )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 22 - 22: I1iiiiI1iII / i11iIiiIii
 import liveresolver
 import resolveurl
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = Ooo0OO0oOO , thumbnailImage = Ooo0OO0oOO )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = Ooo0OO0oOO , thumbnailImage = Ooo0OO0oOO )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
 else :
  if '.m3u8' in url :
   O000OOo00oo = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + iiii11I + '&amp;url=' + url + '&amp;iconImage=' + Ooo0OO0oOO
  elif '.ts' in url :
   O000OOo00oo = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + iiii11I + '&amp;url=' + url + '&amp;iconImage=' + Ooo0OO0oOO
  else :
   O000OOo00oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 62 - 62: i1 / o000o0o00o0Oo
  O0O0OOOOoo = xbmcgui . ListItem ( iiii11I , iconImage = Ooo0OO0oOO , thumbnailImage = Ooo0OO0oOO )
  O0O0OOOOoo . setPath ( url )
  if 7 - 7: OoooooooOO . I1iiiiI1iII
  xbmc . Player ( ) . play ( O000OOo00oo , O0O0OOOOoo , False )
  if 53 - 53: OOooO % OOooO * i1IIi11111i + Oooo0000
  if 92 - 92: OoooooooOO + i1IIi / OOooO * O0
def O00oOo00o0o ( ) :
 if 85 - 85: OOoO00o + OoooooooOO * OOoO00o - oOo0 % i11iIiiIii
 ii1I1i1I = 'https://m.skylinewebcams.com/en/webcam'
 iI = o00O ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoO0o = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 OOo00OoO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoO0o )
 for ii1I1i1I , i1O0OoO0o in OOo00OoO :
  if 'http|https' not in ii1I1i1I :
   ii1I1i1I = 'https://m.skylinewebcams.com' + ii1I1i1I
   ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 46 , I1IiI , Oo , '' )
   if 10 - 10: i1IIi11111i / i11iIiiIii
def o00 ( url ) :
 if 85 - 85: o000o0o00o0Oo . oOo0
 iI = o00O ( url )
 OoO0o = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( iI )
 for url , I1IiI , i1O0OoO0o in OoO0o :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 78 - 78: i1Ii * oOo0 + iIii1I11I1II1 + iIii1I11I1II1 / oOo0 . OOooO
  if 97 - 97: i1Ii / oOo0 % i1IIi % o000o0o00o0Oo
def ii111I11iI ( name , url , iconimage ) :
 if 93 - 93: o000o0o00o0Oo / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * iI1
 iI = o00O ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  OOO0OOO00oo = re . compile ( '<amp-video src="(.+?)"' ) . findall ( iI ) [ 0 ]
  url = 'https:' + OOO0OOO00oo
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  if 64 - 64: i11Ii11I1Ii1i + O0 / iIii1I11I1II1 / ooo0Oo0 . i1Ii % I1iiiiI1iII
 except : pass
 quit ( 0 )
 if 50 - 50: iIii1I11I1II1 - I1iiiiI1iII + OOoOoo00oo
def o0iiiI1I1iIIIi1 ( ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / iI1 % i11Ii11I1Ii1i % i1IIi / i11iIiiIii
 ii1I1i1I = 'http://www.watchepisodeseries.com/home/schedule'
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for ii1I1i1I , OOOIiiiii1iI , IIiooOooo0 in OoO0o :
  ii11i1 ( "[COLOR aqua]" + OOOIiiiii1iI + "  " + IIiooOooo0 + "[/COLOR]" , ii1I1i1I , 67 , I1IiI , I1ii11iIi11i )
  if 67 - 67: iiI1iIiI
  if 55 - 55: o000o0o00o0Oo - OOoO00o * i1IIi11111i + Oooo0000 * Oooo0000 * O0
def O000Oo0o ( url ) :
 if 99 - 99: iIii1I11I1II1 % i1Ii + i1Ii + OOoO00o - oOo0 / oOo0
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 1 ]
  i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  Ooo0OO0oOO = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 68 , Ooo0OO0oOO , I1ii11iIi11i )
  if 7 - 7: iiI1iIiI + Oooo0000 / I1iiiiI1iII
  if 79 - 79: i1 - iIii1I11I1II1 + OOooO - oOo0
def OoOiIIiii ( url , iconimage , fanart ) :
 if 61 - 61: I1iiiiI1iII . i1IIi / oOo0 % i11iIiiIii * OOoO00o
 iI = o00O ( url )
 i1i1i1I = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in i1i1i1I :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
 OOO0OOO00oo = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( iI )
 OOooo0O00o = datetime . now ( )
 for i1I1iI in OOO0OOO00oo :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   i1O0OoO0o = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
   oOoo000 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   OooOo00o = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   OOOIiiiii1iI = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in OOOIiiiii1iI :
    OOOIiiiii1iI = OOOIiiiii1iI . strip ( )
    OOOIiiiii1iI = time . strptime ( OOOIiiiii1iI , "%d/%m/%Y" )
    IiI11i1IIiiI = ( "%s/%s/%s" % ( OOooo0O00o . day , OOooo0O00o . month , OOooo0O00o . year ) )
    IiI11i1IIiiI = time . strptime ( IiI11i1IIiiI , "%d/%m/%Y" )
    if ( IiI11i1IIiiI < OOOIiiiii1iI ) :
     i1O0OoO0o = '[COLOR yellow]' + ( i1O0OoO0o ) + ' - Not Aired Yet' + '[/COLOR]'
     OooOo00o = '[COLOR yellow]' + ( OooOo00o ) + '[/COLOR]'
     oOoo000 = '[COLOR yellow]' + ( oOoo000 ) + '[/COLOR]'
     if 60 - 60: o000o0o00o0Oo * iiI1iIiI
    if not 'Season 0' in oOoo000 :
     ii11i1 ( "[COLOR aqua]" + oOoo000 + " " + OooOo00o + " " + i1O0OoO0o + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 17 - 17: OOoOoo00oo % ooo0Oo0 / o000o0o00o0Oo . I1iiiiI1iII * OOoOoo00oo - i11Ii11I1Ii1i
  if 41 - 41: OOooO
def oOOoo0o0OOOO ( url , iconimage , fanart ) :
 if 26 - 26: OOoO00o % iIii1I11I1II1 + i1IIi11111i
 if 67 - 67: OOo0o0 + i11Ii11I1Ii1i - O0 . OOo0o0 * i11Ii11I1Ii1i * iI1
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  try :
   i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   i1O0OoO0o = i1O0OoO0o . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   if not 'Lolzor.Com' in i1O0OoO0o :
    if not 'Videoplayer.Gq' in i1O0OoO0o :
     if not 'Vidbaba.Com' in i1O0OoO0o :
      if not 'Gagomatic.Com' in i1O0OoO0o :
       if not 'Favour.Me' in i1O0OoO0o :
        if not 'Funblr.Com' in i1O0OoO0o :
         if not 'Vid.Ag' in i1O0OoO0o :
          if not 'Mycollection.Net' in i1O0OoO0o :
           if not 'Adhqmedia.Com' in i1O0OoO0o :
            if not 'Filenuke.Com' in i1O0OoO0o :
             if not 'Mrfile.Me' in i1O0OoO0o :
              OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 90 - 90: OOooO . I1iiiiI1iII
  if 81 - 81: OOoOoo00oo - iI1 % i1Ii - i1 / ooo0Oo0
def Ii1iI111 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  url = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  import resolveurl
  try :
   if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
    ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    ooo0OO0O0Oo = liveresolver . resolve ( url )
   else : ooo0OO0O0Oo = url
   O0O0OOOOoo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
   xbmc . Player ( ) . play ( ooo0OO0O0Oo )
   if 51 - 51: I1iiiiI1iII * O0 / i11Ii11I1Ii1i . OOooO % OOoOoo00oo / iiI1iIiI
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 9 - 9: iiI1iIiI % iiI1iIiI % i11Ii11I1Ii1i
def I1I1i1I ( ) :
 if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
 i1iI1 = ''
 i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Search Term' )
 i11ii1ii11i . doModal ( )
 if i11ii1ii11i . isConfirmed ( ) :
  i1iI1 = i11ii1ii11i . getText ( )
  if len ( i1iI1 ) > 1 :
   ooO0OoOO = i1iI1 . lower ( )
   ooO0OoOO = ooO0OoOO . replace ( ' ' , '%20' )
   if 41 - 41: Oooo0000 * iI1 / Oooo0000 % OOo0o0
  else : quit ( )
 else : ooO0OoOO = urllib . unquote_plus ( ii1I1i1I ) . lower ( ) ; i1iI1 = urllib . unquote_plus ( ii1I1i1I )
 ii1I1i1I = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + ooO0OoOO
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '"series"(.+?)"series_id"' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( 'original_name":"(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  O000OOo00oo = re . compile ( '"seo_name":"(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://www.watchepisodeseries.com/' + O000OOo00oo
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + O000OOo00oo + '.jpg'
  ii11i1 ( i1O0OoO0o , ii1I1i1I , 68 , I1IiI , I1ii11iIi11i , '' )
  if 18 - 18: i11Ii11I1Ii1i . OoooooooOO % Oooo0000 % OOooO
def II1IiiIii ( ) :
 if 84 - 84: OOo0o0 % i1IIi
 ii1I1i1I = 'http://www.watchepisodeseries.com/home/popular-series'
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<div title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  i1O0OoO0o = o0Oo0oO0oOO00 ( i1O0OoO0o )
  ii1I1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  ii11i1 ( '[COLOR aqua]' + i1O0OoO0o + '[/COLOR]' , ii1I1i1I , 68 , I1IiI , I1ii11iIi11i )
  if 70 - 70: ooo0Oo0 . OoooooooOO - OOoO00o
  if 30 - 30: o000o0o00o0Oo % iiI1iIiI
def O0Oo00 ( ) :
 if 41 - 41: iIii1I11I1II1 % iI1
 try :
  oOo0oOIIi1IIIIi = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1
   else : quit ( )
  if ooO0OoOO == oOo0oOIIi1IIIIi :
   OOOoO ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter The Password You Set' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1
   else : quit ( )
  with open ( i1i1II , "w" ) as iiiII :
   iiiII . write ( ooO0OoOO )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 14 - 14: iI1 . iIii1I11I1II1 . OoooooooOO . i11Ii11I1Ii1i / i1IIi11111i
   if 21 - 21: i11iIiiIii / i1IIi + iiI1iIiI * OOoOoo00oo . oOo0
   if 84 - 84: O0 . iI1 - i11Ii11I1Ii1i . i1Ii / i11Ii11I1Ii1i
def OOOoO ( ) :
 if 47 - 47: OoooooooOO
 ii1i1i1IiII = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 O0o = '[COLOR aqua]Asian Special Porn[/COLOR]'
 ii11i1 ( O0o , ii1i1i1IiII , 1 , I1IiI , Oo , '' )
 ii1I1i1I = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 iI = o00O ( ii1I1i1I )
 OOO0OOO00oo = re . compile ( '<li class="">(.+?)</li>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<strong>(.+?)</strong>' ) . findall ( i1I1iI ) [ 0 ]
  II11I = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
  O000OOo00oo = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'https://www.eporner.com' + O000OOo00oo
  if not 'All' in i1O0OoO0o :
   if not 'Homemade' in i1O0OoO0o :
    ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "  " + "[COLOR yellow]" + II11I + "[/COLOR]" , ii1I1i1I , 36 , I1IiI , Oo , '' )
    if 80 - 80: OOoOoo00oo
def III ( url ) :
 if 81 - 81: ooo0Oo0 / i11iIiiIii + OOoO00o % iIii1I11I1II1 * oOo0
 iI = o00O ( url )
 OOO0OOO00oo = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( 'title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  O000OOo00oo = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'https://www.eporner.com' + O000OOo00oo
  ii11i1 ( "[COLOR skyblue]" + i1O0OoO0o + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 12 - 12: i11Ii11I1Ii1i . iI1 / OOoOoo00oo
 try :
  o0O0o = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( iI ) [ 0 ]
  O00I1iI1 = 'https://www.eporner.com' + o0O0o
  OO0o0o00 = 'http://imgur.com/3eNoY0p'
  ii11i1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , O00I1iI1 , 36 , OO0o0o00 , Oo , '' )
 except : pass
 if 77 - 77: i1Ii - iiI1iIiI % iI1 - O0
def o0O0O0 ( url , iconimage ) :
 if 6 - 6: OOoO00o . I1iiiiI1iII * Oooo0000 . i1IIi
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 oOOo = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( oOOo )
 for I1IiIIi , iI in OoO0o :
  I1IiIIi = I1IiIIi . replace ( ':' , '' )
  url = 'https://www.eporner.com' + iI
  OoOo ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + I1IiIIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 42 - 42: O0 . OOo0o0 - i1IIi11111i / i1IIi
def OooOOO ( url ) :
 if 48 - 48: iIii1I11I1II1 % i1IIi % OOoO00o + i1Ii
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 iI = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoOo ( "[COLOR yellow]Anime Catergories[/COLOR]" , url , 999 , I1IiI , Oo , '' )
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . iI1 % iIii1I11I1II1
 OOO0OOO00oo = re . compile ( '<ul class="nav nav-pills nav-stacked">(.+?)</ul>' ) . findall ( iI ) [ 1 ]
 OoO0o = re . compile ( '<a href="(.+?)" title="(.+?)">.+?</a>' ) . findall ( OOO0OOO00oo )
 for url , i1O0OoO0o in OoO0o :
  i1O0OoO0o = i1O0OoO0o . strip ( )
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 52 , I1IiI , Oo , '' )
  if 62 - 62: ooo0Oo0 * Oooo0000
def OO0 ( url ) :
 if 84 - 84: Oooo0000 % i1Ii - Oooo0000 . i1IIi11111i
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 iI = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOO0OOO00oo = re . compile ( '<th class="st-sort-descent">(.+?)</table>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)".+?>(.+?)</a>' ) . findall ( OOO0OOO00oo )
 for url , i1O0OoO0o in OoO0o :
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 5 - 5: Oooo0000 * oOo0 - o000o0o00o0Oo / iIii1I11I1II1 % OOo0o0 + I1iiiiI1iII
def o00o00OoO00o0 ( url ) :
 if 87 - 87: OOo0o0 * OOo0o0 / iiI1iIiI / i1Ii % OOoOoo00oo
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 iI = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1IiI = re . compile ( '''<div class=\"col-md-3\">.+?url\('(.+?)'\)''' ) . findall ( iI ) [ 0 ]
 except :
  I1IiI = Ooo0OO0oOO
 OOO0OOO00oo = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( iI ) [ 0 ]
 OoO0o = re . compile ( '''<a class=".*?window.location='(.*?)'.*?>(.*?)<''' ) . findall ( OOO0OOO00oo )
 OoOo ( "[COLOR yellow]Links Can Take Up To 45 Secs To Play, Be Patient![/COLOR]" , url , 54 , I1IiI , Oo , '' )
 for url , i1O0OoO0o in OoO0o :
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  if 96 - 96: iiI1iIiI % ooo0Oo0 . o000o0o00o0Oo + OOoOoo00oo
def Ii11Iii1i1ii ( url , iconimage ) :
 if 26 - 26: i11Ii11I1Ii1i % i11iIiiIii % iIii1I11I1II1 % iI1 * iI1 * o000o0o00o0Oo
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 iI = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 oOoO = re . compile ( '<source src="(.+?)"' ) . findall ( iI ) [ 0 ]
 I11iI ( iiii11I , oOoO , iconimage )
 if 24 - 24: i11Ii11I1Ii1i % oOo0 - i1Ii + iiI1iIiI * o000o0o00o0Oo
 if 2 - 2: OOooO - I1iiiiI1iII
 if 83 - 83: OOo0o0 % i1IIi11111i % OOooO - i11Ii11I1Ii1i * OOoOoo00oo / OoooooooOO
 if 18 - 18: i1 + iIii1I11I1II1 - i11Ii11I1Ii1i - iiI1iIiI
 if 71 - 71: OoooooooOO
 if 33 - 33: oOo0
 if 62 - 62: o000o0o00o0Oo + OOooO + i1IIi / OoooooooOO
 if 7 - 7: i1IIi11111i + i1IIi . iiI1iIiI / ooo0Oo0
def I111i1I1 ( url ) :
 if 62 - 62: OOoOoo00oo * oOo0 / ooo0Oo0 * i1IIi11111i
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( 'title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( './' , '/' )
  if 29 - 29: ooo0Oo0 % i1 % I1iiiiI1iII . i1IIi11111i / OoooooooOO * i1Ii
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiIIi = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( i1I1iI ) [ 0 ]
  ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[COLOR yellow] " + I1IiIIi + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 54 - 54: O0
 try :
  O00I1iI1 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( iI ) [ 0 ]
  o0O0o = re . compile ( '<a.+?href="(.+?)"' ) . findall ( O00I1iI1 ) [ 5 ]
  OOoO000O00oO = 'http://m4ufree.com' + o0O0o
  if 'genre' in OOoO000O00oO :
   OOoO000O00oO = OOoO000O00oO . replace ( '.com' , '.com/' )
  i1OoOO = 'https://i.imgur.com/pOefPvV.jpg'
  ii11i1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OOoO000O00oO , 42 , i1OoOO , Oo , '' )
 except : pass
 if 44 - 44: OOoOoo00oo
def O0O0o0o0o ( url , iconimage ) :
 if 9 - 9: ooo0Oo0 + Oooo0000 - iIii1I11I1II1 - OOooO + i1IIi11111i
 import requests
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o000O0OOoo = re . compile ( 'data="(.+?)"' ) . findall ( iI ) [ 0 ]
 Oo00OOOOoo0oo = 'http://m4ufree.com/ajax_new.php'
 O00OOooo0Ooo = requests . post ( Oo00OOOOoo0oo , data = { 'm4u' : o000O0OOoo } )
 json = ( O00OOooo0Ooo . text )
 o0oOOoOOO = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 iiI1i11II = re . compile ( '{(.+?)}' ) . findall ( o0oOOoOOO )
 II11 = 0
 for OOooo0O00o in iiI1i11II :
  try :
   II11 += 1
   i1O0OoO0o = 'Link ' + str ( II11 )
   I1IiIIi = re . compile ( '''"label":"(.+?)"''' ) . findall ( OOooo0O00o ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( OOooo0O00o ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   OoOo ( "[COLOR aqua]" + i1O0OoO0o + " | [COLOR yellow] " + I1IiIIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( OOooo0O00o ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   I1IiIIi = re . compile ( """label:.+?'(.+?)'""" ) . findall ( OOooo0O00o ) [ 0 ]
   OoOo ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + I1IiIIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 15 - 15: I1iiiiI1iII / O0 . i1IIi11111i . i11iIiiIii
def o0OO0O0Oo ( ) :
 if 78 - 78: Oooo0000 / ooo0Oo0 - OOoOoo00oo - OOoO00o * OOo0o0
 ii1I1i1I = 'https://www.livefootballol.me/acestream-channel-list-2017.html'
 iI = o00O ( ii1I1i1I )
 OoO0o = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI )
 for Ii1I11I in OoO0o :
  i1O0OoO0o = re . compile ( '<strong>(.+?)</strong>' ) . findall ( Ii1I11I ) [ 0 ]
  if len ( i1O0OoO0o ) == 1 or '&nbsp;' in i1O0OoO0o :
   i1O0OoO0o = re . compile ( '<strong>(.+?)</strong>' ) . findall ( Ii1I11I ) [ 1 ]
  if len ( i1O0OoO0o ) > 40 :
   i1O0OoO0o = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( Ii1I11I ) [ 0 ]
  ii1I1i1I = re . compile ( '<td>(.+?)</td>' ) . findall ( Ii1I11I ) [ 2 ]
  iiIii1I = re . compile ( '<td>(.+?)</td>' ) . findall ( Ii1I11I ) [ 3 ]
  i1I11iIiII = re . compile ( '<td>(.+?)</td>' ) . findall ( Ii1I11I ) [ 4 ]
  i1O0OoO0o = i1O0OoO0o . strip ( )
  ii1I1i1I = ii1I1i1I . strip ( )
  OoOo ( "[COLOR aqua]" + i1O0OoO0o + ' :: [COLOR yellow]' + iiIii1I + '[COLOR aqua] :: [COLOR yellow]' + i1I11iIiII + ' Kbps[/COLOR]' , ii1I1i1I , 2 , Ooo0OO0oOO , Oo , '' )
  if 66 - 66: ooo0Oo0 - i1IIi11111i * I1iiiiI1iII + Oooo0000 + i1IIi11111i - iIii1I11I1II1
def iiiI1ii11 ( ) :
 if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
 ii1I1i1I = 'http://acestreamchannel.blogspot.co.uk/'
 iI = o00O ( ii1I1i1I )
 OoO0o = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI )
 for i1I1iI in OoO0o :
  try :
   i1O0OoO0o = re . compile ( '<td>(.+?)</td>' ) . findall ( i1I1iI ) [ 0 ]
   if len ( i1O0OoO0o ) < 40 :
    ii1I1i1I = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
    OoOo ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 2 , Ooo0OO0oOO , Oo , '' )
  except : pass
def ooOooo0OO ( ) :
 if 2 - 2: i11Ii11I1Ii1i - i1 . I1iiiiI1iII * OOoO00o / OOo0o0
 ii1I1i1I = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 iI = o00O ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<td>(.+?)</td>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  ii1I1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  OOo0oO00ooO00 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  ii1I1i1I = 'http://www.livefootballol.me' + ii1I1i1I
  ii11i1 ( "[COLOR aqua]" + OOo0oO00ooO00 + "[/COLOR]" , ii1I1i1I , 74 , Ooo0OO0oOO , Oo , '' )
  if 80 - 80: OOoOoo00oo / iI1 / Oooo0000 + i1IIi - ooo0Oo0
def iIIiiIIi1IiI ( url ) :
 if 14 - 14: I1iiiiI1iII % OOo0o0 % ooo0Oo0 - i11iIiiIii
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( iI )
 o0OO000ooOo = 0
 for O00OOOoOoo0O in OOO0OOO00oo :
  if 'acestream' in O00OOOoOoo0O :
   if 'http' in O00OOOoOoo0O :
    o0OO000ooOo += 1
    i1O0OoO0o = '[COLOR aqua]Link :: ' + str ( o0OO000ooOo ) + '[/COLOR]'
    OoOo ( i1O0OoO0o , O00OOOoOoo0O , 75 , Ooo0OO0oOO , Oo , '' )
 if o0OO000ooOo == 0 :
  OoOo ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , Ooo0OO0oOO , Oo , '' )
  if 86 - 86: i1 * OoooooooOO
def OooO0oOo ( url ) :
 if 66 - 66: i1 * ooo0Oo0
 iI = o00O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( iI ) [ 0 ]
 I11iI ( iiii11I , url , Ooo0OO0oOO )
 if 28 - 28: i1 % Oooo0000 % o000o0o00o0Oo + iiI1iIiI / iiI1iIiI
def OO0O0ooOOO00 ( url , getphp ) :
 IIII1i = urllib2 . Request ( url )
 IIII1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 IIII1i . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 Ii1IIIIi1ii1I = urllib2 . urlopen ( IIII1i , timeout = 10 )
 iI = Ii1IIIIi1ii1I . read ( )
 Ii1IIIIi1ii1I . close ( )
 return iI
 if 17 - 17: O0 . oOo0 . O0 + O0 / ooo0Oo0 . i1Ii
 if 62 - 62: o000o0o00o0Oo % OOoO00o * i1 - i1IIi
 if 66 - 66: i11iIiiIii / i1IIi11111i - OoooooooOO / i1IIi . i11iIiiIii
def IIIII1iii11 ( ) :
 if 35 - 35: OOo0o0 / oOo0 / i11Ii11I1Ii1i - iIii1I11I1II1 + i11Ii11I1Ii1i . oOo0
 ii1I1i1I = 'http://m4ufree.com/?sort=key_top&page=1&='
 iI = o00O ( ii1I1i1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOO0OOO00oo = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( iI )
 for i1I1iI in OOO0OOO00oo :
  i1O0OoO0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  O000OOo00oo = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( './' , '' )
  ii1I1i1I = 'http://m4ufree.com/' + O000OOo00oo
  if not re . search ( '\d+' , i1O0OoO0o ) :
   ii11i1 ( "[COLOR aqua]" + i1O0OoO0o + "[/COLOR]" , ii1I1i1I , 42 , I1IiI , Oo )
   if 81 - 81: OOoO00o * OOoOoo00oo - o000o0o00o0Oo * OOooO % Oooo0000 * Oooo0000
   if 59 - 59: iIii1I11I1II1
   if 7 - 7: OOoOoo00oo * iiI1iIiI / i1IIi11111i * i11iIiiIii
   if 84 - 84: OOoOoo00oo . OOoO00o
   if 8 - 8: ooo0Oo0 + i11Ii11I1Ii1i * OOoOoo00oo * Oooo0000 * iI1 / I1iiiiI1iII
   if 21 - 21: OOo0o0 / OoooooooOO
   if 11 - 11: OOoOoo00oo % OOooO - i11iIiiIii - OOo0o0 + i1Ii + I1iiiiI1iII
   if 87 - 87: oOo0 * i1IIi / o000o0o00o0Oo
   if 6 - 6: i1IIi11111i + ooo0Oo0 - OoooooooOO % OOoOoo00oo * Oooo0000
   if 69 - 69: i1IIi
def o0Oo0oO0oOO00 ( text ) :
 if 59 - 59: i11Ii11I1Ii1i - i1IIi11111i
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
 if 24 - 24: ooo0Oo0 - i1IIi + iI1
 return text
 if 38 - 38: OoooooooOO / o000o0o00o0Oo . O0 / i1IIi / ooo0Oo0 + iIii1I11I1II1
def ooO00O00oOO ( ) :
 if 40 - 40: OOoO00o . OOo0o0 + iiI1iIiI + o000o0o00o0Oo + oOo0
 i11 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 Ii1I1I11I = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 I1iiiiii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 65 - 65: I1iiiiI1iII + ooo0Oo0
 Ooo0O0 = 0
 for ( ooo0 , o0oooO , ooOo ) in os . walk ( Ii1I1I11I ) :
  for file in ooOo :
   o0oO0OoO0 = os . path . join ( ooo0 , file )
   Ooo0O0 += os . path . getsize ( o0oO0OoO0 )
 oO0Oo = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( Ooo0O0 / ( 1024 * 1024.0 ) )
 OoOo ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 70 - 70: OOo0o0 - OOo0o0
 Ooo0O0 = 0
 for ( ooo0 , o0oooO , ooOo ) in os . walk ( i11 ) :
  for file in ooOo :
   o0oO0OoO0 = os . path . join ( ooo0 , file )
   Ooo0O0 += os . path . getsize ( o0oO0OoO0 )
 oO0Oo = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( Ooo0O0 / ( 1024 * 1024.0 ) )
 OoOo ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 57 - 57: iiI1iIiI - i1IIi11111i + i1 % ooo0Oo0
 Ooo0O0 = 0
 for ( ooo0 , o0oooO , ooOo ) in os . walk ( Ii1 ) :
  for file in ooOo :
   o0oO0OoO0 = os . path . join ( ooo0 , file )
   Ooo0O0 += os . path . getsize ( o0oO0OoO0 )
 oO0Oo = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( Ooo0O0 / ( 1024 * 1024.0 ) )
 OoOo ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 26 - 26: OOoO00o . OOoO00o
 Ooo0O0 = 0
 for ( ooo0 , o0oooO , ooOo ) in os . walk ( I1iiiiii ) :
  for file in ooOo :
   o0oO0OoO0 = os . path . join ( ooo0 , file )
   Ooo0O0 += os . path . getsize ( o0oO0OoO0 )
 oO0Oo = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( Ooo0O0 / ( 1024 * 1024.0 ) )
 OoOo ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 35 - 35: oOo0 . Oooo0000 * i11iIiiIii
 OoOo ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 OoOo ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 44 - 44: i11iIiiIii / ooo0Oo0
def I11iI ( name , url , iconimage ) :
 if 42 - 42: OoooooooOO + ooo0Oo0 % i11Ii11I1Ii1i + i1
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import resolveurl
 if 24 - 24: OOoO00o * i11Ii11I1Ii1i % OOoO00o % I1iiiiI1iII + OoooooooOO
 if 29 - 29: i11Ii11I1Ii1i - OoooooooOO - i11iIiiIii . i1IIi11111i
 if 19 - 19: i11Ii11I1Ii1i
 if 72 - 72: OoooooooOO / iiI1iIiI + OOooO / Oooo0000 * OOooO
 if 'acestream' in url :
  O000OOo00oo = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  O0O0OOOOoo . setPath ( url )
  xbmc . Player ( ) . play ( O000OOo00oo , O0O0OOOOoo , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
  time . sleep ( 2 )
  quit ( )
 else :
  ooo0OO0O0Oo = url
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 34 - 34: O0 * O0 % OoooooooOO + OOoO00o * iIii1I11I1II1 % OOooO
def I1iI1I1 ( name , url , iconimage ) :
 if 48 - 48: iiI1iIiI / i11iIiiIii - i1IIi11111i * OOo0o0 / OoooooooOO
 iI11i1ii11 , OoOoi1i = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 iI11i1ii11 += urllib . unquote_plus ( OoOoi1i )
 url = regex . resolve ( iI11i1ii11 )
 if 5 - 5: o000o0o00o0Oo + O0 + O0 . oOo0 - i1Ii
 PLAYREGEX ( name , url , iconimage )
 if 63 - 63: OOo0o0
def iI1111iiii ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 71 - 71: i1IIi . OOooO * OOoO00o % OoooooooOO + OOoOoo00oo
def iIIi1iiI1i11 ( heading , text ) :
 if 56 - 56: OoooooooOO
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 iiIIii = xbmcgui . Window ( id )
 O0OO = 50
 while ( O0OO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   O0OO -= 1
   iiIIii . getControl ( 1 ) . setLabel ( heading )
   iiIIii . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 39 - 39: o000o0o00o0Oo + iiI1iIiI - iIii1I11I1II1 - i1IIi11111i
  if 7 - 7: I1iiiiI1iII . Oooo0000 / o000o0o00o0Oo . OOoOoo00oo * iI1 - i11Ii11I1Ii1i
def o00O ( url ) :
 try :
  IIII1i = urllib2 . Request ( url )
  IIII1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ii1IIIIi1ii1I = urllib2 . urlopen ( IIII1i , timeout = 5 )
  iI = Ii1IIIIi1ii1I . read ( )
  Ii1IIIIi1ii1I . close ( )
  iI = iI . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI
 except : quit ( )
 if 37 - 37: oOo0 . Oooo0000 / O0 * OOoO00o
def i1i ( url ) :
 try :
  IIII1i = urllib2 . Request ( url )
  IIII1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  Ii1IIIIi1ii1I = urllib2 . urlopen ( IIII1i , timeout = 5 )
  iI = Ii1IIIIi1ii1I . read ( )
  Ii1IIIIi1ii1I . close ( )
  iI = iI . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI
 except : quit ( )
 if 7 - 7: i1 * iI1 + i11Ii11I1Ii1i % i11iIiiIii
def OoOo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 i1i1IiIiIi1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 16 - 16: ooo0Oo0 + i1Ii / ooo0Oo0 / i1 % OOo0o0 % o000o0o00o0Oo
 oO0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1IiIiIi1Ii , listitem = O0O0OOOOoo , isFolder = False )
 return oO0ooOO
 if 22 - 22: i11Ii11I1Ii1i * i1 * iI1 + o000o0o00o0Oo * i1IIi11111i
def o0ooOooo000oOO ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 i1i1IiIiIi1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 100 - 100: i1IIi / I1iiiiI1iII
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 3 - 3: i11Ii11I1Ii1i % o000o0o00o0Oo - OoooooooOO * ooo0Oo0 . iIii1I11I1II1
 oO0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1IiIiIi1Ii , listitem = O0O0OOOOoo , isFolder = False )
 return oO0ooOO
 if 37 - 37: OOoO00o / ooo0Oo0 . iI1 * iI1
def o0O0Oo0Ooo0 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 I11iII = [ ]
 IiiIiI = [ ]
 iIIIIiiIii = [ ]
 iI = o00O ( url )
 O00OOOoOoo0O = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O00OOOoOoo0O ) [ 0 ]
 i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( O00OOOoOoo0O )
 if len ( i1I1iI ) < 1 :
  i1I1iI = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( O00OOOoOoo0O )
 OOooo0O00o = 1
 for ooO0oo in i1I1iI :
  ooO0oo0o0 = ooO0oo
  if '(' in ooO0oo :
   ooO0oo = ooO0oo . split ( '(' ) [ 0 ]
   IIiIii1 = str ( ooO0oo0o0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   I11iII . append ( ooO0oo )
   IiiIiI . append ( IIiIii1 )
  else :
   I11iII . append ( ooO0oo )
   IiiIiI . append ( '[COLOR aqua]Link ' + str ( OOooo0O00o ) + '[/COLOR]' )
  OOooo0O00o = OOooo0O00o + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 Ooo0oO0 = Iii1ii1II11i . select ( name , IiiIiI )
 if Ooo0oO0 < 0 :
  quit ( )
 else :
  url = I11iII [ Ooo0oO0 ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : ooo0OO0O0Oo = liveresolver . resolve ( url )
  else : ooo0OO0O0Oo = url
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo )
  if 86 - 86: O0
def O0o0oOooOoOo ( name , url , iconimage ) :
 if 49 - 49: OOoOoo00oo . o000o0o00o0Oo . i11iIiiIii - i11Ii11I1Ii1i / OOooO
 ooOo0O0o0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 I11iII = [ ]
 IiiIiI = [ ]
 iIIIIiiIii = [ ]
 o0oo0O = [ ]
 iI = o00O ( url )
 O00OOOoOoo0O = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI ) [ 0 ]
 i1I1iI = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( O00OOOoOoo0O )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O00OOOoOoo0O ) [ 0 ]
 OOooo0O00o = 1
 if 19 - 19: oOo0 + i1IIi . iiI1iIiI - ooo0Oo0
 for ooO0oo in i1I1iI :
  ooO0oo0o0 = ooO0oo
  if '(' in ooO0oo :
   ooO0oo = ooO0oo . split ( '(' ) [ 0 ]
   IIiIii1 = str ( ooO0oo0o0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   I11iII . append ( ooO0oo )
   IiiIiI . append ( IIiIii1 )
   o0oo0O . append ( 'Stream ' + str ( OOooo0O00o ) )
  else :
   I11iII . append ( ooO0oo )
   IiiIiI . append ( 'Link ' + str ( OOooo0O00o ) )
   if 16 - 16: OOo0o0 + i1Ii / i1IIi11111i
  OOooo0O00o = OOooo0O00o + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 Ooo0oO0 = Iii1ii1II11i . select ( name , IiiIiI )
 if Ooo0oO0 < 0 :
  quit ( )
 else :
  Oo0OoO00oOO0o = IiiIiI [ Ooo0oO0 ]
  OOO00O = "/"
  if not Oo0OoO00oOO0o . endswith ( OOO00O ) :
   OOoOO0oo0ooO = Oo0OoO00oOO0o + "/"
  else :
   OOoOO0oo0ooO = Oo0OoO00oOO0o
  url = ooOo0O0o0 + I11iII [ Ooo0oO0 ] + "%26referer=" + OOoOO0oo0ooO
  print url
  if 82 - 82: I1iiiiI1iII * i11iIiiIii % i11Ii11I1Ii1i - OoooooooOO
  xbmc . Player ( ) . play ( url )
  if 90 - 90: ooo0Oo0 . OOo0o0 * i1IIi - i1IIi
def i1I ( string ) :
 IiIiiI11i1Ii = ( c for c in string if 0 < ord ( c ) < 127 )
 if 100 - 100: oOo0 . iiI1iIiI * oOo0 - iiI1iIiI . iI1 * OOooO
 return '' . join ( IiIiiI11i1Ii )
 if 89 - 89: i1 + I1iiiiI1iII * oOo0
def ii11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 28 - 28: OoooooooOO . OOo0o0 % o000o0o00o0Oo / i1IIi / OOoOoo00oo
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 i1i1IiIiIi1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 oO0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1i1IiIiIi1Ii , listitem = O0O0OOOOoo , isFolder = True )
 return oO0ooOO
 if 36 - 36: i1IIi11111i + iI1 - I1iiiiI1iII + iIii1I11I1II1 + OoooooooOO
def Ii ( name , url , iconimage ) :
 oO0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; O0O0OOOOoo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = O0O0OOOOoo )
 xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
 if 42 - 42: OOooO * oOo0 . I1iiiiI1iII * iiI1iIiI + Oooo0000
def i1i1II11II1 ( ) :
 if 5 - 5: ooo0Oo0 - o000o0o00o0Oo % OOo0o0 - i11Ii11I1Ii1i . iiI1iIiI + OOoO00o
 i11 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 Ii1I1I11I = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 47 - 47: O0 - iIii1I11I1II1 - OOoO00o
 OOooo0O00o = [ ( i11 , 'Cache' ) , ( Ii1I1I11I , 'Thumbnails' ) , ( Ii1 , 'Packages' ) ]
 if 46 - 46: OOooO . OOoOoo00oo * i1 . OoooooooOO + o000o0o00o0Oo
 oo0000o = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if oo0000o :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for iI11i1ii11 in OOooo0O00o :
   if 12 - 12: i1IIi11111i + OOooO + i1IIi11111i
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % iI11i1ii11 [ 1 ] )
   time . sleep ( 1 )
   if 95 - 95: OOooO + o000o0o00o0Oo * OOoOoo00oo
   for I1Ii , o0oooO , ooOo in os . walk ( iI11i1ii11 [ 0 ] ) :
    for o00O00O0O0O in ooOo :
     if ( o00O00O0O0O . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( I1Ii , o00O00O0O0O ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % iI11i1ii11 [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 77 - 77: iIii1I11I1II1 - i1IIi . OOo0o0
def iIi1iIIIiIiI ( url , mode , name , iconimage , fanart ) :
 if 62 - 62: i11iIiiIii % OOoOoo00oo . I1iiiiI1iII . OOoOoo00oo
 with open ( I11i , "a" ) as iiiII :
  iiiII . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 84 - 84: i11iIiiIii * i1
def I1I1iII1i ( ) :
 if 30 - 30: O0 + o000o0o00o0Oo + i11Ii11I1Ii1i
 with open ( I11i , "a" ) as iiiII :
  III1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  I1I111iIi = open ( III1I ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OOO0OOO00oo = re . compile ( '<item>(.+?)</item>' ) . findall ( I1I111iIi )
  OoOo ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  OoOo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  if len ( OOO0OOO00oo ) < 1 :
   OoOo ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  for Ii1I11I in OOO0OOO00oo :
   i1O0OoO0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii1I11I ) [ 0 ]
   ii1I1i1I = re . compile ( '<url>(.+?)</url>' ) . findall ( Ii1I11I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii1I11I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii1I11I ) [ 0 ]
   OoOo ( '[COLOR skyblue]' + i1O0OoO0o + '[/COLOR]' , ii1I1i1I , 2 , I1IiI , I1ii11iIi11i )
   if 53 - 53: iIii1I11I1II1 + i1IIi11111i - Oooo0000 - OOo0o0 / i1Ii % i11iIiiIii
 OoOo ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , Ooo0OO0oOO , Oo )
 if 3 - 3: OOoO00o . i1Ii % iiI1iIiI + o000o0o00o0Oo
def oo0o ( ) :
 if 51 - 51: OOoOoo00oo . iiI1iIiI
 with open ( IiII , "a" ) as iiiII :
  III1I = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  I1I111iIi = open ( III1I ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OOO0OOO00oo = re . compile ( '<item>(.+?)</item>' ) . findall ( I1I111iIi )
  OoOo ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  OoOo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  if len ( OOO0OOO00oo ) < 1 :
   OoOo ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , Ooo0OO0oOO , Oo )
  for Ii1I11I in OOO0OOO00oo :
   i1O0OoO0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii1I11I ) [ 0 ]
   ii1I1i1I = re . compile ( '<link>(.+?)</link>' ) . findall ( Ii1I11I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii1I11I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii1I11I ) [ 0 ]
   OoOo ( '[COLOR skyblue]' + i1O0OoO0o + '[/COLOR]' , ii1I1i1I , 2 , I1IiI , I1ii11iIi11i )
   if 73 - 73: OoooooooOO . iiI1iIiI / oOo0 % OOooO
 OoOo ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , Ooo0OO0oOO , Oo )
 if 65 - 65: I1iiiiI1iII - iiI1iIiI - OOooO
def Ii1iIi111I1i ( ) :
 if 4 - 4: OOoO00o - ooo0Oo0 - I1iiiiI1iII - iI1 % i11iIiiIii / i1
 with open ( I11i , "w" ) as iiiII :
  iiiII . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 50 - 50: i1Ii + i1IIi
def i11IiIIi11I ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as iiiII :
  iiiII . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 78 - 78: I1iiiiI1iII
 if 83 - 83: iIii1I11I1II1 % Oooo0000 % i1IIi11111i % oOo0 . o000o0o00o0Oo % O0
 if 47 - 47: i1IIi11111i
def ooo ( ) :
 if 66 - 66: iiI1iIiI - I1iiiiI1iII
 ooOOOo0oo0O0 ( )
 iiIii = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iIiIii1ii = re . compile ( '<pin>(.+?)</pin>' ) . findall ( iiIii ) [ 0 ]
  if iIiIii1ii == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   i1iI1 = ''
   i11ii1ii11i = xbmc . Keyboard ( i1iI1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   i11ii1ii11i . doModal ( )
   if i11ii1ii11i . isConfirmed ( ) :
    i1iI1 = i11ii1ii11i . getText ( )
    if len ( i1iI1 ) > 1 :
     ooO0OoOO = i1iI1 . title ( )
     with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
      o00O00O0O0O . write ( "<pin>" + ooO0OoOO + "</pin>" )
     ooo ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in iIiIii1ii :
   IIiI1i = re . compile ( '<pin>(.+?)</pin>' ) . findall ( iiIii ) [ 0 ]
   iII1 = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % IIiI1i )
   iI = o00O ( iII1 )
   if 'Pin Verified' in iI :
    pass
   else :
    with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
     o00O00O0O0O . write ( '<pin>EXPIRED</pin>' )
     ooo ( )
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
   o00O00O0O0O . write ( "<pin>EXPIRED</pin>\n" )
  ooo ( )
  if 70 - 70: OOoO00o / OOoOoo00oo % i1Ii - OOooO
  if 47 - 47: OOoO00o
  if 92 - 92: OOoOoo00oo + Oooo0000 % i1IIi
  if 23 - 23: oOo0 - OOoOoo00oo + OOooO - Oooo0000 * Oooo0000 . ooo0Oo0
def iIii11iI1II ( url , iconimage , fanart ) :
 if 42 - 42: i1Ii - iiI1iIiI + o000o0o00o0Oo % OOooO
 try :
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Name To Save File As' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1 . title ( )
   else : quit ( )
  import resolveurl
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   ooo0OO0O0Oo = resolveurl . HostedMediaFile ( url ) . resolve ( )
   url = ooo0OO0O0Oo
  IiIi1III = url . split ( '/' ) [ - 1 ]
  i1i1IiIiIi1Ii = urllib2 . urlopen ( url )
  Ii1ii11IIIi = os . path . join ( o0OOO , ooO0OoOO )
  o00O00O0O0O = open ( Ii1ii11IIIi , 'wb' )
  if 82 - 82: OOo0o0 * iIii1I11I1II1 . i1IIi11111i . o000o0o00o0Oo + OOoOoo00oo / iiI1iIiI
  O0O0O = i1i1IiIiIi1Ii . info ( )
  iIiiIIi11I11i = int ( O0O0O . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( ooO0OoOO , iIiiIIi11I11i ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 71 - 71: ooo0Oo0 / i1IIi11111i + OOoOoo00oo
  i11i11 = 0
  i1iiIII1IIiIIII = 8192
  while True :
   buffer = i1i1IiIiIi1Ii . read ( i1iiIII1IIiIIII )
   if not buffer :
    break
    if 19 - 19: OOoO00o - i1IIi11111i / i1IIi11111i + ooo0Oo0
   i11i11 += len ( buffer )
   o00O00O0O0O . write ( buffer )
   OoO0o0000O = "[%3.2f%%]" % ( i11i11 * 100. / iIiiIIi11I11i )
   OoO0o0000O = OoO0o0000O + chr ( 8 ) * ( len ( OoO0o0000O ) + 1 )
   iIiiiI . update ( i11i11 , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( OoO0o0000O , ooO0OoOO ) )
   if 8 - 8: Oooo0000 . i1Ii % OOo0o0 . iiI1iIiI % iiI1iIiI . OOooO
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as iiiII :
   iiiII . write ( '<item>\n<title>' + ooO0OoOO + '</title>\n<link>' + Ii1ii11IIIi + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 47 - 47: iI1 + i1Ii + i11Ii11I1Ii1i % i11iIiiIii
  o00O00O0O0O . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 93 - 93: o000o0o00o0Oo % Oooo0000 . O0 / OOoO00o * OOo0o0
  if 29 - 29: i1IIi11111i
  if 86 - 86: i11Ii11I1Ii1i . I1iiiiI1iII
  if 2 - 2: OoooooooOO
def o0o0O00 ( ) :
 i1iIiIIi1II1ii = [ ]
 i1II1Ii1i1 = sys . argv [ 2 ]
 if len ( i1II1Ii1i1 ) >= 2 :
  I1i1I1I11IiiI = sys . argv [ 2 ]
  I1IiI1iI11 = I1i1I1I11IiiI . replace ( '?' , '' )
  if ( I1i1I1I11IiiI [ len ( I1i1I1I11IiiI ) - 1 ] == '/' ) :
   I1i1I1I11IiiI = I1i1I1I11IiiI [ 0 : len ( I1i1I1I11IiiI ) - 2 ]
  iIi = I1IiI1iI11 . split ( '&' )
  i1iIiIIi1II1ii = { }
  for OOooo0O00o in range ( len ( iIi ) ) :
   iiO0O0o0oO0O00 = { }
   iiO0O0o0oO0O00 = iIi [ OOooo0O00o ] . split ( '=' )
   if ( len ( iiO0O0o0oO0O00 ) ) == 2 :
    i1iIiIIi1II1ii [ iiO0O0o0oO0O00 [ 0 ] ] = iiO0O0o0oO0O00 [ 1 ]
 return i1iIiIIi1II1ii
 if 70 - 70: oOo0 + OOo0o0
I1i1I1I11IiiI = o0o0O00 ( ) ; ii1I1i1I = None ; iiii11I = None ; o00ooo0 = None ; i1i1IiIi1 = None ; Ooo0OO0oOO = None ; I1iiIiI1iI1I = None
try : i1i1IiIi1 = urllib . unquote_plus ( I1i1I1I11IiiI [ "site" ] )
except : pass
try : ii1I1i1I = urllib . unquote_plus ( I1i1I1I11IiiI [ "url" ] )
except : pass
try : iiii11I = urllib . unquote_plus ( I1i1I1I11IiiI [ "name" ] )
except : pass
try : o00ooo0 = int ( I1i1I1I11IiiI [ "mode" ] )
except : pass
try : Ooo0OO0oOO = urllib . unquote_plus ( I1i1I1I11IiiI [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( I1i1I1I11IiiI [ "fanart" ] )
except : pass
try : I1iiIiI1iI1I = urllib . unquote_plus ( I1i1I1I11IiiI [ "description" ] )
except : pass
if 27 - 27: o000o0o00o0Oo * oOo0 - i1 + OOooO * OOooO
if o00ooo0 == None or ii1I1i1I == None or len ( ii1I1i1I ) < 1 : iiI1 ( )
if 55 - 55: i1Ii
if 82 - 82: oOo0 - OOoOoo00oo + i1
if 64 - 64: i1IIi11111i . O0 * OOooO + OoooooooOO - ooo0Oo0 . OoooooooOO
if 70 - 70: ooo0Oo0 - OOo0o0 . iIii1I11I1II1 % iI1 / Oooo0000 - O0
if 55 - 55: OOoO00o - i1
elif o00ooo0 == 1 : iII ( iiii11I , ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 2 : I11iI ( iiii11I , ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 3 : o0O0Oo0Ooo0 ( iiii11I , ii1I1i1I , Ooo0OO0oOO )
if 100 - 100: O0
if 79 - 79: iIii1I11I1II1
if 81 - 81: OOoOoo00oo + iIii1I11I1II1 * oOo0 - iIii1I11I1II1 . OOoOoo00oo
elif o00ooo0 == 4 : Ii1i ( ii1I1i1I )
elif o00ooo0 == 5 : oOOo0 ( ii1I1i1I )
elif o00ooo0 == 6 : oOo0O0Oo00oO ( )
elif o00ooo0 == 7 : O00o0OO0 ( ii1I1i1I )
elif o00ooo0 == 8 : O0oO ( ii1I1i1I )
elif o00ooo0 == 9 : OOOOo0 ( ii1I1i1I )
elif o00ooo0 == 10 : iI1111iiii ( ii1I1i1I )
elif o00ooo0 == 11 : iIi1ii ( )
elif o00ooo0 == 12 : ooO0OO ( ii1I1i1I )
elif o00ooo0 == 13 : oO00oOOoooO ( ii1I1i1I )
elif o00ooo0 == 14 : OOOO0OoOO0o0o ( ii1I1i1I )
elif o00ooo0 == 15 : OooOo0ooo ( )
elif o00ooo0 == 16 : O0o0oOooOoOo ( iiii11I , ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 17 : i1iIIIi1i ( ii1I1i1I )
elif o00ooo0 == 18 : i1Iiii111iI1iIi1 ( ii1I1i1I )
elif o00ooo0 == 19 : o0Ooo00o0Oooo ( ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 20 : oOo0oO ( )
elif o00ooo0 == 21 : OO ( ii1I1i1I )
elif o00ooo0 == 22 : OOO ( ii1I1i1I )
elif o00ooo0 == 23 : o0000oO ( )
elif o00ooo0 == 24 : o00Oo0oooooo ( ii1I1i1I )
elif o00ooo0 == 25 : oo0 ( ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 26 : iI1I111I ( ii1I1i1I )
elif o00ooo0 == 27 : o0O ( ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 28 : iI1IiI ( )
elif o00ooo0 == 29 : IIii11I1i1I ( ii1I1i1I )
elif o00ooo0 == 30 : iiIi1i ( ii1I1i1I )
elif o00ooo0 == 31 : oo0oO0 ( ii1I1i1I )
elif o00ooo0 == 32 : IIioOoO00oo0O ( ii1I1i1I )
elif o00ooo0 == 33 : IIiIi ( ii1I1i1I )
elif o00ooo0 == 34 : iiI11i1II ( ii1I1i1I )
elif o00ooo0 == 35 : OOOoO ( )
elif o00ooo0 == 36 : III ( ii1I1i1I )
elif o00ooo0 == 37 : o0O0O0 ( ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 38 : O0Oo00 ( )
elif o00ooo0 == 39 : OOOO0O00o ( ii1I1i1I )
elif o00ooo0 == 40 : oOo0oO ( )
elif o00ooo0 == 41 : OO ( ii1I1i1I )
elif o00ooo0 == 42 : I111i1I1 ( ii1I1i1I )
elif o00ooo0 == 43 : O0O0o0o0o ( ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 44 : IIIII1iii11 ( )
if 48 - 48: iI1 . OoooooooOO . iiI1iIiI . Oooo0000 % o000o0o00o0Oo / OOoO00o
elif o00ooo0 == 45 : O00oOo00o0o ( )
elif o00ooo0 == 46 : o00 ( ii1I1i1I )
elif o00ooo0 == 47 : ii111I11iI ( iiii11I , ii1I1i1I , Ooo0OO0oOO )
elif o00ooo0 == 48 : IIIII ( )
elif o00ooo0 == 49 : O00O0ooo0 ( ii1I1i1I )
elif o00ooo0 == 50 : OoO ( ii1I1i1I )
elif o00ooo0 == 51 : OooOOO ( ii1I1i1I )
elif o00ooo0 == 52 : OO0 ( ii1I1i1I )
elif o00ooo0 == 53 : o00o00OoO00o0 ( ii1I1i1I )
elif o00ooo0 == 54 : Ii11Iii1i1ii ( ii1I1i1I , Ooo0OO0oOO )
if 11 - 11: i1IIi % i1 % OOoO00o
if 99 - 99: i1Ii / iIii1I11I1II1 - OOooO * o000o0o00o0Oo % iiI1iIiI
if 13 - 13: i1
elif o00ooo0 == 59 : II1111ii ( )
elif o00ooo0 == 60 : ii1III11 ( ii1I1i1I )
elif o00ooo0 == 61 : ooOOo00O00Oo ( iiii11I , ii1I1i1I , Ooo0OO0oOO )
if 70 - 70: oOo0 + O0 . OOo0o0 * OOooO
elif o00ooo0 == 66 : o0iiiI1I1iIIIi1 ( )
elif o00ooo0 == 67 : O000Oo0o ( ii1I1i1I )
elif o00ooo0 == 68 : OoOiIIiii ( ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 69 : oOOoo0o0OOOO ( ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 70 : Ii1iI111 ( ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 71 : I1I1i1I ( )
elif o00ooo0 == 72 : II1IiiIii ( )
elif o00ooo0 == 73 : ooOooo0OO ( )
elif o00ooo0 == 74 : iIIiiIIi1IiI ( ii1I1i1I )
elif o00ooo0 == 75 : OooO0oOo ( ii1I1i1I )
elif o00ooo0 == 76 : o0OO0O0Oo ( )
elif o00ooo0 == 77 : iiiI1ii11 ( )
if 2 - 2: OoooooooOO . OOoOoo00oo . I1iiiiI1iII
if 42 - 42: OOoOoo00oo % OOo0o0 / i1 - OOo0o0 * i11iIiiIii
elif o00ooo0 == 884 : ooO00O00oOO ( )
elif o00ooo0 == 885 : i11IiIIi11I ( )
elif o00ooo0 == 886 : oo0o ( )
elif o00ooo0 == 887 : iIii11iI1II ( ii1I1i1I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 888 : o0OoOo00o0o ( )
elif o00ooo0 == 889 : iIi1iIIIiIiI ( ii1I1i1I , o00ooo0 , iiii11I , Ooo0OO0oOO , I1ii11iIi11i )
elif o00ooo0 == 890 : I1I1iII1i ( )
elif o00ooo0 == 891 : Ii1iIi111I1i ( )
elif o00ooo0 == 892 : i1i1II11II1 ( )
if 19 - 19: OOo0o0 * iiI1iIiI % i11iIiiIii
if o00ooo0 == None or ii1I1i1I == None or len ( ii1I1i1I ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 24 - 24: i1IIi11111i
if 10 - 10: i1IIi11111i % OOooO / OOoOoo00oo
if 28 - 28: OOoOoo00oo % i1Ii
if 48 - 48: i11iIiiIii % OOo0o0
if 29 - 29: OOoO00o + i11iIiiIii % iI1
if 93 - 93: Oooo0000 % iIii1I11I1II1
if 90 - 90: iiI1iIiI - OOoOoo00oo / OOooO / O0 / iI1
if 87 - 87: Oooo0000 / I1iiiiI1iII + iIii1I11I1II1
if 93 - 93: iIii1I11I1II1 + OOo0o0 % i1Ii
if 21 - 21: OOoOoo00oo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
