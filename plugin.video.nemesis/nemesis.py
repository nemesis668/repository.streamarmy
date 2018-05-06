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
oo00 = 'https://pastebin.com/raw/XK6h1Qur'
if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
def i1I1Iiii1111 ( ) :
 if 22 - 22: OOo000 . O0I11i1i11i1I
 if 31 - 31: i11iI / Oo0o0ooO0oOOO + I1 - OOoOoo00oo - iiI11
 if not os . path . exists ( os . path . dirname ( o0OOO ) ) :
  try :
   os . makedirs ( os . path . dirname ( o0OOO ) )
   with open ( iI1Ii11111iIi , "w" ) as OOooO :
    OOooO . write ( "<date>000</date>" )
  except OSError as OOoO00o :
   if OOoO00o . errno != errno . EEXIST :
    raise
i1I1Iiii1111 ( )
if 9 - 9: I1iiiiI1iII - oOo0 / i1Ii % I111I11
def O0O00Ooo ( ) :
 if 64 - 64: ooiii11iII - i1IIi + I111I11 + OOoOoo00oo - i1Ii
 oO = OO0OOooOoO0Oo ( oo00 )
 if len ( oO ) > 1 :
  iiIIiIiIi = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  i1I11 = os . path . join ( os . path . join ( iiIIiIiIi , '' ) , 'compare.txt' )
  iI = open ( i1I11 )
  o0O00oooo = iI . read ( )
  if o0O00oooo == oO : pass
  else :
   O00o ( '[B][COLOR aqua]N[COLOR yellow]emesis[COLOR aqua] I[COLOR yellow]nformation[/COLOR][/B]' , oO )
   O00 = open ( i1I11 , "w" )
   O00 . write ( oO )
   O00 . close ( )
def OO0OOooOoO0Oo ( url ) :
 try :
  i11I1 = urllib2 . Request ( url )
  i11I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ii11Ii11I = urllib2 . urlopen ( i11I1 , timeout = 5 )
  iI11i1I1 = Ii11Ii11I . read ( )
  Ii11Ii11I . close ( )
  if 71 - 71: ooiii11iII % oOo0 / i11iI
  return iI11i1I1
 except : quit ( )
 if 49 - 49: O0Oo0oO0o % oOo0 * O0
def oOOo0oo ( ) :
 if 80 - 80: iiI11 * i11iIiiIii / I111I11
 I11II1i = xbmc . getInfoLabel ( "System.BuildVersion" )
 IIIII = float ( I11II1i [ : 4 ] )
 if IIIII >= 11.0 and IIIII <= 11.9 :
  ooooooO0oo = 'Eden'
 elif IIIII >= 12.0 and IIIII <= 12.9 :
  ooooooO0oo = 'Frodo'
 elif IIIII >= 13.0 and IIIII <= 13.9 :
  ooooooO0oo = 'Gotham'
 elif IIIII >= 14.0 and IIIII <= 14.9 :
  ooooooO0oo = 'Helix'
 elif IIIII >= 15.0 and IIIII <= 15.9 :
  ooooooO0oo = 'Isengard'
 elif IIIII >= 16.0 and IIIII <= 16.9 :
  ooooooO0oo = 'Jarvis'
 elif IIIII >= 17.0 and IIIII <= 17.9 :
  ooooooO0oo = 'Krypton'
 elif IIIII >= 18.0 and IIIII <= 18.9 :
  ooooooO0oo = 'Leia'
 else : ooooooO0oo = "Decline"
 if 49 - 49: i11iI * iIii1I11I1II1 / i1IIi / i11iIiiIii / i11iI
 if ooooooO0oo == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif ooooooO0oo == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif ooooooO0oo == "Leia" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 28 - 28: OOoOoo00oo - i1Ii . i1Ii + O0I11i1i11i1I - OoooooooOO + O0
def oOoOooOo0o0 ( ) :
 if 61 - 61: i11iI / OOo000 + ooiii11iII * I1 / I1
 OoOo = [ 'plugin.video.jenexporter' ]
 iIo00O = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in OoOo )
 OOO0OOO00oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.jenexporter' ) )
 if iIo00O :
  import shutil
  shutil . rmtree ( OOO0OOO00oo )
  os . _exit ( 1 )
 else :
  return
  if 31 - 31: O0Oo0oO0o - OOoOoo00oo . I111I11 % O0I11i1i11i1I - O0
def iii11 ( ) :
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
  if 58 - 58: OOoOoo00oo * i11iIiiIii / O0I11i1i11i1I % I111I11 - Oo0o0ooO0oOOO / I1
def ii11i1 ( ) :
 if 29 - 29: Oo0o0ooO0oOOO % II1iI + ooiii11iII / i11iI + OOoOoo00oo * i11iI
 i1I1iI ( )
 oOoOooOo0o0 ( )
 oo0OooOOo0 = baseurl
 o0O = oo0OooOOo0
 O0O00Ooo ( )
 O00oO = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( O00oO >= 0000 ) and ( O00oO <= 1159 ) : I11i1I1I = "Morning"
 elif ( O00oO >= 1200 ) and ( O00oO <= 1759 ) : I11i1I1I = "Afternoon"
 else : I11i1I1I = "Evening"
 oO0Oo ( '[COLOR yellow]Good[COLOR aqua] ' + str ( I11i1I1I ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 oO0Oo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  iI11i1I1 = oOOoo0Oo ( baseurl )
  o00OO00OoO = re . compile ( '<item>(.+?)</item>' ) . findall ( iI11i1I1 )
  for OOOO0OOoO0O0 in o00OO00OoO :
   try :
    if '<m3u>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 11 , oO0 , I1ii11iIi11i )
    elif '<mamahdsports>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 14 , oO0 , I1ii11iIi11i )
    elif '<atc>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<atc>(.+?)</atc>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 6 , oO0 , I1ii11iIi11i )
    elif '<scanner>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 11 , oO0 , I1ii11iIi11i )
    elif '<cartoons>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 29 , oO0 , I1ii11iIi11i )
    elif '<Adult>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 38 , oO0 , I1ii11iIi11i )
    elif '<Anime>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 51 , oO0 , I1ii11iIi11i )
    elif '<audiobooks>' in OOOO0OOoO0O0 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oo0OooOOo0 = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 59 , oO0 , I1ii11iIi11i )
    elif '<folder>' in OOOO0OOoO0O0 :
     ooOooo000oOO = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 )
     for O0Oo000ooO00 , oo0OooOOo0 , oO0 , I1ii11iIi11i in ooOooo000oOO :
      Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 1 , oO0 , I1ii11iIi11i )
    else :
     Oo0oOOo = re . compile ( '<link>(.+?)</link>' ) . findall ( OOOO0OOoO0O0 )
     if len ( Oo0oOOo ) == 1 :
      ooOooo000oOO = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 )
      Oo0OoO00oOO0o = len ( o00OO00OoO )
      for O0Oo000ooO00 , oo0OooOOo0 , oO0 , I1ii11iIi11i in ooOooo000oOO :
       if 'youtube.com/playlist' in oo0OooOOo0 :
        Ii1iIiII1ii1 ( O0Oo000ooO00 , oo0OooOOo0 , 2 , oO0 , I1ii11iIi11i )
       else :
        oO0Oo ( O0Oo000ooO00 , oo0OooOOo0 , 2 , oO0 , I1ii11iIi11i )
     elif len ( Oo0oOOo ) > 1 :
      O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
      oO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
      oO0Oo ( O0Oo000ooO00 , o0O , 3 , oO0 , I1ii11iIi11i )
   except : pass
   if 80 - 80: I1 + OOoOoo00oo - OOoOoo00oo % oOo0
  oO0Oo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.resolveurl/settings.xml" )
   I11i1I1I = open ( file ) . read ( )
   OoOO0oo0o = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( I11i1I1I ) [ 0 ]
   OoOO0oo0o = OoOO0oo0o . strip ( )
   oo0OooOOo0 = 'plugin://script.module.resolveurl/?mode=auth_rd'
   if 'value=""' in OoOO0oo0o :
    II11i1I11Ii1i = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    oO0Oo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( II11i1I11Ii1i ) + '[/COLOR]' , oo0OooOOo0 , 2 , I1IiI , Oo )
   else :
    II11i1I11Ii1i = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    oO0Oo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( II11i1I11Ii1i ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  O000O0oOO0 = 'https://i.imgur.com/o2Wvut7.jpg'
  Ii1iIiII1ii1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , O000O0oOO0 , Oo )
  O0ooo0O0oo0 = 'https://i.imgur.com/SxZzRX9.jpg'
  Ii1iIiII1ii1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , O0ooo0O0oo0 , Oo )
  oo0oOo = 'https://i.imgur.com/zme6vuj.jpg'
  Ii1iIiII1ii1 ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , oo0oOo , Oo )
 except :
  o000O0o = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if o000O0o == 0 :
   oO0Oo ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   Ii1iIiII1ii1 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if o000O0o == 1 :
   quit ( )
   if 42 - 42: O0I11i1i11i1I
 oOOo0oo ( )
 if 41 - 41: i1iIii1Ii1II . ooiii11iII + O0 * i11iI % i1iIii1Ii1II * i1iIii1Ii1II
def iIIIIi1iiIi1 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 o0O = url
 iI11i1I1 = oOOoo0Oo ( url )
 oOoOooOo0o0 ( )
 o00OO00OoO = re . compile ( '<item>(.+?)</item>' ) . findall ( iI11i1I1 )
 for OOOO0OOoO0O0 in o00OO00OoO :
  try :
   if '<image>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 23 , iconimage , fanart )
   elif '<American>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 77 , iconimage , fanart )
   elif '<acechansthree>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<acechansthree>(.+?)</acechansthree>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 78 , iconimage , fanart )
   elif '<acechansfour>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<acechansfour>(.+?)</acechansfour>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 79 , iconimage , fanart )
   elif '<bollywood>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<bollywood>(.+?)</bollywood>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 80 , iconimage , fanart )
   elif '<lordjd>' in OOOO0OOoO0O0 :
    Oo0oOOo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OOOO0OOoO0O0 )
    if len ( Oo0oOOo ) == 1 :
     ooOooo000oOO = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 )
     Oo0OoO00oOO0o = len ( o00OO00OoO )
     for name , url , iconimage , fanart in ooOooo000oOO :
      if 'youtube.com/playlist' in url :
       Ii1iIiII1ii1 ( name , url , 2 , iconimage , fanart )
      else :
       iii1i1iiiiIi ( name , url , 2 , iconimage , fanart )
    elif len ( Oo0oOOo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     iii1i1iiiiIi ( name , o0O , 3 , iconimage , fanart )
   elif '<reddit>' in OOOO0OOoO0O0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
    Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in OOOO0OOoO0O0 :
    Oo0oOOo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OOOO0OOoO0O0 )
    if len ( Oo0oOOo ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     Iiii = re . compile ( '<referer>(.+?)</referer>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     OO0OoO0o00 = Iiii
     ooOO0O0ooOooO = "/"
     if not OO0OoO0o00 . endswith ( ooOO0O0ooOooO ) :
      oOOOo00O00oOo = OO0OoO0o00 + "/"
     else :
      oOOOo00O00oOo = OO0OoO0o00
     iI11i1I1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = iI11i1I1 + '%26referer=' + oOOOo00O00oOo
     oO0Oo ( name , url , 10 , iconimage , fanart )
    elif len ( Oo0oOOo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0Oo ( name , o0O , 16 , iconimage , fanart )
     if 34 - 34: O0 + OOoOoo00oo + i1iIii1Ii1II
   elif '<folder>' in OOOO0OOoO0O0 :
    ooOooo000oOO = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 )
    for name , url , iconimage , fanart in ooOooo000oOO :
     Ii1iIiII1ii1 ( name , url , 1 , iconimage , fanart )
     if 16 - 16: oOo0 . O0 . oOo0 % Oo0o0ooO0oOOO - II1iI - iIii1I11I1II1
   else :
    Oo0oOOo = re . compile ( '<link>(.+?)</link>' ) . findall ( OOOO0OOoO0O0 )
    if len ( Oo0oOOo ) == 1 :
     ooOooo000oOO = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 )
     Oo0OoO00oOO0o = len ( o00OO00OoO )
     for name , url , iconimage , fanart in ooOooo000oOO :
      if 'youtube.com/playlist' in url :
       Ii1iIiII1ii1 ( name , url , 2 , iconimage , fanart )
      else :
       oO0Oo ( name , url , 2 , iconimage , fanart )
    elif len ( Oo0oOOo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
     oO0Oo ( name , o0O , 3 , iconimage , fanart )
  except : pass
  if 36 - 36: i1Ii % ooiii11iII % i1iIii1Ii1II - Oo0o0ooO0oOOO
 oOOo0oo ( )
 if 22 - 22: iIii1I11I1II1 / i1iIii1Ii1II * Oo0o0ooO0oOOO % oOo0
 if 85 - 85: I1 % i11iIiiIii - oOo0 * OoooooooOO / II1iI % II1iI
 if 1 - 1: OOo000 - I1 . iiI11 . OOo000 / i1iIii1Ii1II + iiI11
 if 78 - 78: O0 . I1 . O0Oo0oO0o % OOoOoo00oo
 if 49 - 49: I1iiiiI1iII / OOo000 . O0Oo0oO0o
 if 68 - 68: i11iIiiIii % Oo0o0ooO0oOOO + i11iIiiIii
 if 31 - 31: O0Oo0oO0o . II1iI
 if 1 - 1: i1iIii1Ii1II / i11iI % oOo0 * i1Ii . i11iIiiIii
def III1Iiii1I11 ( url ) :
 if 9 - 9: Oo0o0ooO0oOOO / i1iIii1Ii1II - II1iI / OoooooooOO / iIii1I11I1II1 - i11iI
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  try :
   o00oooO0Oo = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   Ii1iIiII1ii1 ( "[COLOR skyblue]" + o00oooO0Oo + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 78 - 78: I1iiiiI1iII % I111I11 + Oo0o0ooO0oOOO
def OOooOoooOoOo ( url ) :
 if 84 - 84: i1Ii
 OOO00O0O = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 iii = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 oO0Oo ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 iI11i1I1 = oOOoo0Oo ( url )
 Oo0oOOo = 0
 oOooOOOoOo = re . compile ( 'href="([^"]+)' ) . findall ( iI11i1I1 )
 for url in oOooOOOoOo :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in OOO00O0O ) :
    Oo0oOOo += 1
    o00oooO0Oo = "Link " + str ( Oo0oOOo ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    i1Iii1i1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     oO0Oo ( "[COLOR skyblue]" + o00oooO0Oo + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in iii ) :
     oO0Oo ( "[COLOR yellow]" + o00oooO0Oo + url + "[/COLOR]" , i1Iii1i1I , 2 , I1IiI , I1ii11iIi11i )
    else :
     oO0Oo ( "[COLOR skyblue]" + o00oooO0Oo + url + "[/COLOR]" , i1Iii1i1I , 2 , I1IiI , I1ii11iIi11i )
     if 91 - 91: Oo0o0ooO0oOOO + II1iI . OOoOoo00oo * Oo0o0ooO0oOOO + II1iI * i1iIii1Ii1II
     if 80 - 80: oOo0 % OOoOoo00oo % I1 - i1iIii1Ii1II + i1iIii1Ii1II
     if 19 - 19: O0I11i1i11i1I * i1IIi
def ii111iI1iIi1 ( url ) :
 if 78 - 78: OOo000 . OOoOoo00oo + OOo000 / iiI11 / OOo000
 if url == 'Football' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  oO0O00OoOO0 = oOOoo0Oo ( 'http://wizhdsports.is/sport/Cricket' )
 iI = dom_parser2 . parse_dom ( oO0O00OoOO0 , 'div' , { 'class' : 'card' } )
 iI = [ ( dom_parser2 . parse_dom ( OoO , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( OoO , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( OoO , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( OoO , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for OoO in iI ]
 if len ( iI ) < 1 :
  oO0Oo ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , oO0 , Oo , '' )
 iI = [ ( OoO [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , OoO [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , OoO [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , OoO [ 2 ] [ 0 ] . content ) if OoO [ 2 ] else 'Upcoming' , OoO [ 3 ] [ 0 ] . content ) for OoO in iI ]
 if 88 - 88: oOo0 . O0Oo0oO0o * O0Oo0oO0o % I111I11
 if 15 - 15: i1IIi * II1iI + i11iIiiIii
 if 6 - 6: ooiii11iII / i11iIiiIii + oOo0 * I1
 if 80 - 80: O0Oo0oO0o
 iI = [ ( OoO [ 0 ] , OoO [ 1 ] , OoO [ 2 ] , OoO [ 3 ] , OoO [ 4 ] ) for OoO in iI ]
 O0Oi1I1I = 0
 iiI1I = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for OoO in iI :
  IiIiiIIiI = OoO [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( O0Oi1I1I ) )
  O0Oi1I1I += 1
  time . sleep ( 0.10 )
  IiIiiIIiI = ooOO0OOOO0oo0 ( IiIiiIIiI )
  I11iiI1i1 = OoO [ 1 ]
  I1i1Iiiii = OoO [ 3 ]
  if 'Match Over' in I1i1Iiiii :
   iiI1I += 1
  OOo0oO00ooO00 = dom_parser2 . parse_dom ( OoO [ 4 ] , 'a' )
  for oO0O00OoOO0 in OOo0oO00ooO00 :
   oOO0O00oO0Ooo = re . sub ( '<.+?>' , '' , oO0O00OoOO0 . content )
   iI11i1I1 = oO0O00OoOO0 . attrs [ 'href' ]
   iI11i1I1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + iI11i1I1
   if not 'Match Over' in I1i1Iiiii :
    oO0Oo ( '[COLOR aqua]' + IiIiiIIiI + '[COLOR yellow]' + ' ' + I1i1Iiiii + '[/COLOR]' , iI11i1I1 , 2 , oO0 , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( O0Oi1I1I ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( iiI1I ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 67 - 67: OOo000 - OOoOoo00oo
def iI1i11iII111 ( url ) :
 if 15 - 15: i11iIiiIii % I1iiiiI1iII . i1iIii1Ii1II + Oo0o0ooO0oOOO
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 o00OO00OoO = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = re . compile ( 'title="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  if 61 - 61: i1iIii1Ii1II * Oo0o0ooO0oOOO % i1iIii1Ii1II - i1IIi - iIii1I11I1II1
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 74 - 74: Oo0o0ooO0oOOO + O0Oo0oO0o / OOo000
 try :
  oOo0O0Oo00oO = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( iI11i1I1 ) [ 0 ]
  I1IiI = oO0
  Ii1iIiII1ii1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , oOo0O0Oo00oO , 18 , oO0 , Oo , '' )
 except : pass
 if 7 - 7: i1Ii * I111I11 % I1iiiiI1iII - i11iI
def i1i ( url , iconimage , fanart ) :
 if 56 - 56: Oo0o0ooO0oOOO % O0 - II1iI
 oO0Oo ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 o00OO00OoO = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( iI11i1I1 )
 if 100 - 100: I1iiiiI1iII - O0 % I1 * OOoOoo00oo + II1iI
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( Oo0oOOo ) [ 0 ]
  i1Iii1i1I = str . lower ( url )
  if '1e' in i1Iii1i1I :
   o00oooO0Oo = '1st Half'
  else :
   o00oooO0Oo = '2nd Half'
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 88 - 88: OoooooooOO - OOo000 * O0 * OoooooooOO . OoooooooOO
def I111iI ( ) :
 if 56 - 56: II1iI
 oo0OooOOo0 = 'http://www.goalsarena.org/en/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o00OO00OoO = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for OO0ooOOO0OOO , oO00oooOOoOo0 in O0oO :
  Ii1iIiII1ii1 ( "[COLOR skyblue]" + oO00oooOOoOo0 + "[/COLOR]" , OO0ooOOO0OOO , 21 , I1IiI , Oo , '' )
  if 74 - 74: iIii1I11I1II1 * Oo0o0ooO0oOOO + O0I11i1i11i1I / i1IIi / O0Oo0oO0o . i1iIii1Ii1II
def oooOo0OOOoo0 ( url ) :
 if 51 - 51: i1iIii1Ii1II / O0I11i1i11i1I . OOoOoo00oo * i11iI + OOo000 * i1Ii
 if 73 - 73: OOo000 + OoooooooOO - O0 - I1iiiiI1iII - O0Oo0oO0o
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o000O0o = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if o000O0o == 0 :
  try :
   o00OO00OoO = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in o00OO00OoO :
   O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , o00OO00OoO , oO0 )
  o0oO0O0o0O00O = oOOoo0Oo ( o00OO00OoO )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
  url = 'https:' + url
  OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = oO0 , thumbnailImage = oO0 )
  xbmc . Player ( ) . play ( url , OoO000O0Oo , False )
  quit ( 0 )
 if o000O0o == 1 :
  try :
   o00OO00OoO = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI11i1I1 ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   oooOo0OOOoo0 ( url )
  o0oO0O0o0O00O = oOOoo0Oo ( o00OO00OoO )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
  url = 'https:' + url
  OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = oO0 , thumbnailImage = oO0 )
  xbmc . Player ( ) . play ( url , OoO000O0Oo , False )
  quit ( 0 )
  if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
def iI1111iiii ( ) :
 if 67 - 67: OoooooooOO / II1iI * I1iiiiI1iII + iiI11
 oo0OooOOo0 = 'http://m.liveatc.net/feeds/'
 iI11i1I1 = OooOo0ooo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li>(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://m.liveatc.net' + oo0OooOOo0
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 7 , I1IiI , Oo , '' )
  if 71 - 71: I111I11 + I1iiiiI1iII
def iI1111ii1I ( url ) :
 if 45 - 45: i1IIi + i11iI
 if 94 - 94: I1 . i1IIi - i11iI % O0 - OOo000
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li>(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 72 - 72: I1iiiiI1iII
def II11Ii1iI1iII ( url ) :
 url = url . replace ( ' ' , '%20' )
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li>(.+?)</a>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '(.+?)</li>' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 73 - 73: OoooooooOO * OoooooooOO * ooiii11iII * O0I11i1i11i1I + ooiii11iII * I111I11
def oo0o0OO0 ( url ) :
 if 86 - 86: iIii1I11I1II1 / O0I11i1i11i1I . O0Oo0oO0o
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li>(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  try :
   o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
   oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   oO0Oo ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 19 - 19: Oo0o0ooO0oOOO % OoooooooOO % i1Ii * i11iI % O0
def ooo ( ) :
 if 27 - 27: ooiii11iII % II1iI
 Ii1iIiII1ii1 ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 oo0OooOOo0 = 'http://m.broadcastify.com/?a=la&coid=1'
 iI11i1I1 = OooOo0ooo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://m.broadcastify.com' + oo0OooOOo0
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 12 , I1IiI , Oo , '' )
  if 73 - 73: OOoOoo00oo
def ooO ( url ) :
 if 51 - 51: II1iI % I111I11 . I1 / iIii1I11I1II1 / iiI11 . I1
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 42 - 42: i11iI + i1IIi - I1iiiiI1iII / i1Ii
def iiIiIIIiiI ( url ) :
 if 12 - 12: O0 - i11iI
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 81 - 81: O0I11i1i11i1I - O0I11i1i11i1I . oOo0
def o0OoOo00o0o ( url ) :
 if 41 - 41: ooiii11iII % OOo000 - i1iIii1Ii1II * I111I11 * i1iIii1Ii1II
 iI11i1I1 = OooOo0ooo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  o00OO00OoO = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 OOOoOO0o ( o00OO00OoO )
 if 1 - 1: O0Oo0oO0o
def O0oOo00o ( ) :
 if 81 - 81: i1Ii % i1IIi . iIii1I11I1II1
 oo0OooOOo0 = 'http://m.broadcastify.com/?a=top25'
 iI11i1I1 = OooOo0ooo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  Ii1Iii1iIi = o00oooO0Oo . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  o00oooO0Oo = o00oooO0Oo . split ( ')' ) [ - 1 ] . strip ( )
  oo0OooOOo0 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://m.broadcastify.com' + oo0OooOOo0
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[COLOR yellow] :: " + Ii1Iii1iIi + " Listening" + "[/COLOR]" , oo0OooOOo0 , 14 , I1IiI , Oo , '' )
  if 82 - 82: Oo0o0ooO0oOOO / II1iI % iIii1I11I1II1 / i1IIi - II1iI
def I1III1111iIi ( url ) :
 if 38 - 38: oOo0 + iiI11 / I111I11 % ooiii11iII - Oo0o0ooO0oOOO
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = iI11 ( o00oooO0Oo )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( Oo0oOOo ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( Oo0oOOo ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in o00oooO0Oo :
    i1Iii1i1I = 'https://www.youtube.com' + url
    oO0Oo ( "[COLOR aqua][B]" + o00oooO0Oo + "[/B][/COLOR]" , i1Iii1i1I , 2 , I1IiI , I1ii11iIi11i )
    if 10 - 10: O0Oo0oO0o / I1 % OoooooooOO * iiI11 % Oo0o0ooO0oOOO
def I1i11 ( ) :
 if 12 - 12: i1IIi + i1IIi - Oo0o0ooO0oOOO * i1iIii1Ii1II % i1iIii1Ii1II - O0Oo0oO0o
 oo0OooOOo0 = 'http://burningwhee1s.blogspot.co.uk/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( o00OO00OoO )
 for iI11i1I1 , o00oooO0Oo in O0oO :
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , iI11i1I1 , 24 , I1IiI , Oo , '' )
  if 52 - 52: ooiii11iII . oOo0 + I111I11
def iiii1IIi ( url ) :
 if 33 - 33: O0I11i1i11i1I * OOoOoo00oo - O0Oo0oO0o
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( Oo0oOOo ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 83 - 83: O0I11i1i11i1I - I1iiiiI1iII / iiI11 / I111I11 + I1 - O0
def I11I1i1iIII1I ( url , iconimage ) :
 if 49 - 49: Oo0o0ooO0oOOO . i11iI . O0Oo0oO0o
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( o00OO00OoO )
 try :
  for Oo0oOOo in O0oO :
   o00oooO0Oo = re . compile ( '<b>(.+?)</b>' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    o000ooooO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( Oo0oOOo ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     o000ooooO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( Oo0oOOo ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     o000ooooO0o = ''
   o00oooO0Oo = iI11 ( o00oooO0Oo )
   o000ooooO0o = iI11 ( o000ooooO0o )
   iI1i11 = re . compile ( '<option value="(.+?)"' ) . findall ( Oo0oOOo ) [ 1 ]
   oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "  " + o000ooooO0o + "[/COLOR]" , iI1i11 , 2 , I1IiI , Oo , '' )
 except :
  oO0Oo ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 66 - 66: O0 % Oo0o0ooO0oOOO + i11iIiiIii . O0I11i1i11i1I / I1iiiiI1iII + Oo0o0ooO0oOOO
def ooo00Ooo ( ) :
 if 93 - 93: i11iIiiIii - II1iI * Oo0o0ooO0oOOO * iiI11 % O0 + OoooooooOO
 if 25 - 25: i1Ii + I1iiiiI1iII / ooiii11iII . i11iI % O0 * OOo000
 oo0OooOOo0 = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 ooOooo000oOO = json . loads ( iI11i1I1 )
 o0O0oo0OO0O = ooOooo000oOO [ 'results' ]
 for OO0 in o0O0oo0OO0O :
  o0Oooo = 'https://image.tmdb.org/t/p/original'
  o00oooO0Oo = OO0 [ 'title' ]
  I1IiI = OO0 [ 'poster_path' ]
  iiI = OO0 [ 'id' ]
  I1IiI = o0Oooo + I1IiI
  I1ii11iIi11i = OO0 [ 'backdrop_path' ]
  I1ii11iIi11i = o0Oooo + I1ii11iIi11i
  oOIIiIi = OO0 [ 'overview' ]
  iiI = str ( iiI )
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , o00oooO0Oo , 33 , I1IiI , I1ii11iIi11i , oOIIiIi )
  if 91 - 91: Oo0o0ooO0oOOO * i1iIii1Ii1II / II1iI . O0 + OOo000 + O0I11i1i11i1I
def iIIi ( url ) :
 if 11 - 11: II1iI * I1
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = re . compile ( '<i>(.+?)</i>' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = o00oooO0Oo . strip ( )
  Ii1iIiII1ii1 ( "[COLOR aqua][B]" + o00oooO0Oo + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o000oo = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( iI11i1I1 ) [ 0 ]
  o00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  Ii1iIiII1ii1 ( '[COLOR yellow]Next Page >>[/COLOR]' , o000oo , 26 , o00o0 , I1ii11iIi11i )
 except : pass
 if 50 - 50: i1iIii1Ii1II / i1iIii1Ii1II % Oo0o0ooO0oOOO . Oo0o0ooO0oOOO
def O0O0Oo00 ( url , iconimage ) :
 if 80 - 80: I1 + OOoOoo00oo / iiI11
 iI11i1I1 = oOOoo0Oo ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( iI11i1I1 ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 o00OO00OoO = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( iI11i1I1 )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 OoO = 1
 oOOO00O0O0OOo = [ ]
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oOOO00O0O0OOo . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( OoO ) )
  time . sleep ( 0.02 )
  OoO += 1
  o00oooO0Oo = re . compile ( '(.+?)</p>' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( 'Server' , '' )
  o00oooO0Oo = o00oooO0Oo . strip ( )
 OOo00O = 1
 I11i1I1I = 0
 OooOOOO = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 45 - 45: Oo0o0ooO0oOOO % II1iI - i11iIiiIii
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if I11i1I1I > len ( oOOO00O0O0OOo ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * II1iI
  if OooOOOO == 0 :
   I11i1I1I += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( I11i1I1I ) + "[/COLOR]" , '' )
   try :
    iI11i1I1 = oOOoo0Oo ( oOOO00O0O0OOo [ I11i1I1I ] )
    O0oO = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
    iII1ii1 = base64 . b64decode ( O0oO )
    url = re . compile ( 'src="(.+?)"' ) . findall ( iII1ii1 ) [ 0 ]
    I1i1iiiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    iIIioO0o00oo0 = open ( I1i1iiiI1 ) . read ( )
    ii1IIII = re . compile ( '<url>(.+?)</url>' ) . findall ( iIIioO0o00oo0 )
    for oO00oOooooo0 in ii1IIII :
     oOo = re . compile ( '<bad>(.+?)<bad>' ) . findall ( oO00oOooooo0 ) [ 0 ]
     if url == oOo :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( I11i1I1I ) )
      time . sleep ( 0.5 )
      OooOOOO = 5
      pass
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     O0OOooOoO = liveresolver . resolve ( url )
    else : O0OOooOoO = url
    OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( O0OOooOoO , OoO000O0Oo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( I11i1I1I ) )
    time . sleep ( 0.5 )
    OooOOOO = 5
    pass
  if OooOOOO == 5 :
   OooOOOO = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   OooOOOO += 1
   if 1 - 1: oOo0
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 I1i1iiiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 OO0OoO0o00 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if OO0OoO0o00 :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( I1i1iiiI1 , "a" ) as O0O0Ooo :
   O0O0Ooo . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 77 - 77: i11iI / OoooooooOO
def IIii11I1i1I ( url ) :
 if 99 - 99: oOo0
 if 76 - 76: OOo000 * II1iI
 if url == 'search' :
  o0o0OO0Oooooo = ''
  ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , 'Enter Search Term' )
  ii1ii111 . doModal ( )
  if ii1ii111 . isConfirmed ( ) :
   o0o0OO0Oooooo = ii1ii111 . getText ( )
   if len ( o0o0OO0Oooooo ) > 1 :
    I111i1i1111 = o0o0OO0Oooooo . lower ( )
    if 49 - 49: OOo000 / I1 + O0 * i11iI
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , oO0 , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , oO0 , 5000 )
   quit ( )
  I111i1i1111 = I111i1i1111 . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + I111i1i1111 + '.html'
  I1ii11 ( url , I1IiI )
  if 74 - 74: i1iIii1Ii1II - i11iI . i1IIi
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  I1ii11 ( url , I1IiI )
  if 43 - 43: oOo0 / II1iI
def I1ii11 ( url , icon ) :
 if 58 - 58: II1iI + i11iIiiIii % I1iiiiI1iII . O0I11i1i11i1I
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = re . compile ( '<i>(.+?)</i>' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = iI11 ( o00oooO0Oo )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua][B]" + o00oooO0Oo + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - O0Oo0oO0o * OOoOoo00oo
def iiIi1iI1iIii ( ) :
 if 68 - 68: OOoOoo00oo
 oo0OooOOo0 = 'http://www.genti.stream/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  OooO0oo = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ] . strip ( )
  o0o0oOoOO0O = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 1 ] . strip ( )
  oo0OooOOo0 = re . compile ( 'href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://www.genti.stream/' + oo0OooOOo0
  oO0Oo ( "[COLOR aqua]" + OooO0oo + "[COLOR yellow] vs [COLOR aqua]" + o0o0oOoOO0O + "[/COLOR]" , oo0OooOOo0 , 39 , I1IiI , I1ii11iIi11i )
  if 16 - 16: i1Ii % iIii1I11I1II1 . I1iiiiI1iII
def oooooOOO000Oo ( url ) :
 if 52 - 52: O0Oo0oO0o % i1Ii . O0I11i1i11i1I * iIii1I11I1II1
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1II = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
 if not 'http' in I111i1II :
  I111i1II = 'http://www.genti.stream' + I111i1II
 OO0ooOOO0OOO = oOOoo0Oo ( I111i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0ooooo0OOOO0 = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OO0ooOOO0OOO ) [ 0 ]
 o0oO0O0o0O00O = oOOoo0Oo ( O0ooooo0OOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( o0oO0O0o0O00O ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( o0oO0O0o0O00O ) [ 0 ]
 except : pass
 if 9 - 9: O0Oo0oO0o - i11iI / oOo0 / i11iI
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , oO0 , 5000 )
  quit ( )
 O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , url , oO0 )
 if 40 - 40: OOoOoo00oo * OOoOoo00oo . oOo0 % O0
 if 9 - 9: I1 + iiI11 / iiI11
def Ii1I11ii1i ( url ) :
 if 89 - 89: oOo0 . O0 / Oo0o0ooO0oOOO % O0I11i1i11i1I . i1iIii1Ii1II
 url = 'http://www.toonget.net/cartoon'
 iI11i1I1 = oOOoo0Oo ( url )
 O0oO = re . compile ( '<td><a href="(.+?)">(.+?)</a>' ) . findall ( iI11i1I1 )
 for url , o00oooO0Oo in O0oO :
  Ii1iIiII1ii1 ( "[COLOR aqua][B]" + o00oooO0Oo + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 50 - 50: O0Oo0oO0o + Oo0o0ooO0oOOO . i1IIi % i11iI
def IIIi ( url ) :
 if 94 - 94: I111I11 - OOo000 % OOo000 / O0Oo0oO0o % i1iIii1Ii1II . i11iI
 iI11i1I1 = oOOoo0Oo ( url )
 try :
  I1IiI = re . compile ( '<div class="left_col">.+?<img src="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
 except :
  I1IiI = oO0
 try :
  o00oOo0oOoo = re . compile ( '<span>Description:</span>.+?<div>(.+?)</div>' ) . findall ( iI11i1I1 ) [ 0 ] . strip ( )
 except :
  o00oOo0oOoo = 'No Description Found'
 o00OO00OoO = re . compile ( '<div id="videos">(.+?)</div>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<li>.+?<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for url , o00oooO0Oo in O0oO :
  Ii1iIiII1ii1 ( "[COLOR aqua][B]" + o00oooO0Oo + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , o00oOo0oOoo )
  if 57 - 57: O0I11i1i11i1I - Oo0o0ooO0oOOO
 try :
  I11iiI11 = re . compile ( '<ul class="pagination">(.+?)</ul>' ) . findall ( iI11i1I1 ) [ 0 ] . strip ( )
  o00oOoOo0 = re . compile ( 'href="(.+?)"' ) . findall ( I11iiI11 ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , o00oOoOo0 , 30 , oO0 , I1ii11iIi11i )
 except : pass
 if 72 - 72: I111I11
def OO0ooo0oOO ( url ) :
 if 97 - 97: II1iI / oOo0
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI11i1I1 )
 OoO = 0
 for Oooo0 in o00OO00OoO :
  OoO += 1
  o00oooO0Oo = 'Stream : ' + str ( OoO )
  oO0Oo ( o00oooO0Oo , Oooo0 , 32 , oO0 , I1ii11iIi11i )
  if 59 - 59: OoooooooOO
def i1iiiii1 ( url ) :
 if 83 - 83: oOo0 . O0 / i1iIii1Ii1II / OOoOoo00oo - O0Oo0oO0o
 iI11i1I1 = oOOoo0Oo ( url )
 if 'easyvideome' in url or 'videozoo' in url :
  oO0oO0 = re . compile ( 'file:.+?"(.+?)"' ) . findall ( iI11i1I1 ) [ 1 ]
  O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , oO0oO0 , oO0 )
 elif 'playpandanet' in url :
  oO0oO0 = re . compile ( """url:.+?'(.+?)'""" ) . findall ( iI11i1I1 ) [ 0 ]
  O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , oO0oO0 , oO0 )
 else :
  Iii1ii1II11i . notification ( o0OoOoOO00 , 'Sorry This Link Is Down, Try Another' , oO0 , 4000 )
  if 14 - 14: oOo0
  if 99 - 99: oOo0
def IIi1ii1Ii ( ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + oOo0 - i11iIiiIii + OOoOoo00oo
 oo0OooOOo0 = "http://www.loyalbooks.com/genre-menu"
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( iI11i1I1 )
 for OOOO0OOoO0O0 in o00OO00OoO :
  if "paid" not in OOOO0OOoO0O0 :
   OO0ooOOO0OOO = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
   o0oO0O0o0O00O = "http://www.loyalbooks.com" + OO0ooOOO0OOO
   O0Oo000ooO00 = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
   Ii1iIiII1ii1 ( "[COLOR aqua]" + O0Oo000ooO00 + "[/COLOR]" , o0oO0O0o0O00O , 60 , I1IiI , Oo , '' )
   if 18 - 18: O0Oo0oO0o / i1Ii
def IiIIii1 ( url ) :
 if 53 - 53: I1iiiiI1iII % I1iiiiI1iII * i11iI + O0I11i1i11i1I
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( iI11i1I1 ) [ 0 ]
 Oooo00 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( o00OO00OoO )
 for OOOO0OOoO0O0 in Oooo00 :
  i1Iii1i1I = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
  o0oO0O0o0O00O = "http://www.loyalbooks.com" + i1Iii1i1I
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
  oO0 = "http://www.loyalbooks.com" + I1IiI
  O0Oo000ooO00 = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua]" + O0Oo000ooO00 + "[/COLOR]" , o0oO0O0o0O00O , 61 , oO0 , Oo , '' )
 try :
  iI11i1I1 = oOOoo0Oo ( url )
  oOo0O0Oo00oO = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( iI11i1I1 ) [ 0 ]
  I1IiI = 'https://i.imgur.com/pOefPvV.jpg'
  Ii1iIiII1ii1 ( "[COLOR yellow]Next Page -->[/COLOR]" , oOo0O0Oo00oO , 60 , I1IiI , Oo , '' )
 except : pass
 if 6 - 6: I1iiiiI1iII - ooiii11iII * OOoOoo00oo . oOo0 / O0 * ooiii11iII
 if 22 - 22: i1iIii1Ii1II % oOo0 * Oo0o0ooO0oOOO / OOoOoo00oo % i11iIiiIii * iiI11
def Oo00OoOo ( name , url , iconimage ) :
 if 24 - 24: i11iIiiIii - I111I11
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( iI11i1I1 )
 for OOOO0OOoO0O0 in o00OO00OoO :
  o00oooO0Oo = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
  i1Iii1i1I = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( OOOO0OOoO0O0 ) [ 0 ]
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , i1Iii1i1I , 10 , iconimage , Oo , '' )
  if 21 - 21: iiI11
def OoO00 ( ) :
 if 85 - 85: i1iIii1Ii1II * i1iIii1Ii1II * II1iI . OoooooooOO . I1iiiiI1iII * ooiii11iII
 oo0OooOOo0 = 'http://www.shadownet.me/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( o00OO00OoO )
 for oo0OooOOo0 , o00oooO0Oo in O0oO :
  o00oooO0Oo = iI11 ( o00oooO0Oo )
  if 'P2P' not in o00oooO0Oo :
   Ii1iIiII1ii1 ( "[COLOR skyblue]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 49 , I1IiI , Oo , '' )
   if 65 - 65: OOoOoo00oo * I111I11
   if 79 - 79: OoooooooOO - II1iI
def o00O00oO00 ( url ) :
 if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * i1Ii
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( o00OO00OoO )
 for Oo0oOOo in O0oO :
  o00oooO0Oo = re . compile ( 'alt="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oO0Oo ( "[COLOR skyblue]" + o00oooO0Oo + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o000oo = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( iI11i1I1 ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  Ii1iIiII1ii1 ( "[COLOR orange]Next Page --->[/COLOR]" , o000oo , 49 , I1IiI , Oo , '' )
 except : pass
 if 9 - 9: i1Ii - O0Oo0oO0o + O0 / iIii1I11I1II1 / i11iIiiIii
def I1IIIiI1I1ii1 ( url ) :
 if 30 - 30: O0 * OoooooooOO
 def I1iIIIi1 ( url ) :
  i11I1 = urllib2 . Request ( url )
  i11I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  i11I1 . add_header ( 'Referer' , url )
  Ii11Ii11I = urllib2 . urlopen ( i11I1 , timeout = 5 )
  iI11i1I1 = Ii11Ii11I . read ( )
  Ii11Ii11I . close ( )
  return iI11i1I1
  if 17 - 17: iIii1I11I1II1 . OoooooooOO / iiI11 % O0Oo0oO0o % i1IIi / i11iIiiIii
 iI11i1I1 = I1iIIIi1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  o00OO00OoO = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( iI11i1I1 ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in o00OO00OoO :
  url = o00OO00OoO
  O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , url , oO0 )
 o0oO0O0o0O00O = I1iIIIi1 ( o00OO00OoO )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 58 - 58: i1iIii1Ii1II . O0Oo0oO0o + I1 - i11iIiiIii / O0Oo0oO0o / O0
 import liveresolver
 import resolveurl
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
  OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = oO0 , thumbnailImage = oO0 )
  OoO000O0Oo . setPath ( O0OOooOoO )
  xbmc . Player ( ) . play ( O0OOooOoO , OoO000O0Oo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = oO0 , thumbnailImage = oO0 )
  OoO000O0Oo . setPath ( O0OOooOoO )
  xbmc . Player ( ) . play ( O0OOooOoO , OoO000O0Oo , False )
 else :
  if '.m3u8' in url :
   i1Iii1i1I = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + O0Oo000ooO00 + '&amp;url=' + url + '&amp;iconImage=' + oO0
  elif '.ts' in url :
   i1Iii1i1I = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + O0Oo000ooO00 + '&amp;url=' + url + '&amp;iconImage=' + oO0
  else :
   i1Iii1i1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 85 - 85: O0I11i1i11i1I + OOoOoo00oo
  OoO000O0Oo = xbmcgui . ListItem ( O0Oo000ooO00 , iconImage = oO0 , thumbnailImage = oO0 )
  OoO000O0Oo . setPath ( url )
  if 10 - 10: i1Ii / OOo000 + O0I11i1i11i1I / i1IIi
  xbmc . Player ( ) . play ( i1Iii1i1I , OoO000O0Oo , False )
  if 27 - 27: I1iiiiI1iII
  if 67 - 67: II1iI
def OO00OO0O0 ( ) :
 if 48 - 48: I111I11
 oo0OooOOo0 = 'https://m.skylinewebcams.com/en/webcam'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0oO = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( iI11i1I1 ) [ 0 ]
 O00Oo0o000oO = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0oO )
 for oo0OooOOo0 , o00oooO0Oo in O00Oo0o000oO :
  if 'http|https' not in oo0OooOOo0 :
   oo0OooOOo0 = 'https://m.skylinewebcams.com' + oo0OooOOo0
   Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 46 , I1IiI , Oo , '' )
   if 99 - 99: I1 * O0Oo0oO0o * I111I11
def oOooO0 ( url ) :
 if 79 - 79: OOo000 - iIii1I11I1II1 + I1iiiiI1iII - I111I11
 iI11i1I1 = oOOoo0Oo ( url )
 O0oO = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( iI11i1I1 )
 for url , I1IiI , o00oooO0Oo in O0oO :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 93 - 93: O0Oo0oO0o . II1iI - i1iIii1Ii1II + O0I11i1i11i1I
  if 61 - 61: O0Oo0oO0o
def Ii1ii111i1 ( name , url , iconimage ) :
 if 31 - 31: OOoOoo00oo + O0
 iI11i1I1 = oOOoo0Oo ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  o00OO00OoO = re . compile ( '<amp-video src="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
  url = 'https:' + o00OO00OoO
  OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , OoO000O0Oo , False )
  if 87 - 87: ooiii11iII
 except : pass
 quit ( 0 )
 if 45 - 45: OOo000 / OoooooooOO - oOo0 / I1iiiiI1iII % i1Ii
def OoOIii11iI11i1I ( ) :
 if 64 - 64: i11iIiiIii
 oo0OooOOo0 = 'http://www.watchepisodeseries.com/home/schedule'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( o00OO00OoO )
 for oo0OooOOo0 , I1II , I1iIiI11I1 in O0oO :
  Ii1iIiII1ii1 ( "[COLOR aqua]" + I1II + "  " + I1iIiI11I1 + "[/COLOR]" , oo0OooOOo0 , 67 , I1IiI , I1ii11iIi11i )
  if 27 - 27: I1iiiiI1iII . i11iIiiIii % I111I11
  if 65 - 65: O0Oo0oO0o . II1iI % I1 * OOo000
def iI11I ( url ) :
 if 11 - 11: oOo0 - I1 + O0Oo0oO0o - iIii1I11I1II1
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 1 ]
  o00oooO0Oo = iI11 ( o00oooO0Oo )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oO0 = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( Oo0oOOo ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( Oo0oOOo ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 68 , oO0 , I1ii11iIi11i )
  if 7 - 7: i1Ii - iiI11 / O0Oo0oO0o * I1iiiiI1iII . oOo0 * oOo0
  if 61 - 61: iiI11 % ooiii11iII - OOo000 / i1iIii1Ii1II
def Ii1iI111 ( url , iconimage , fanart ) :
 if 51 - 51: i1Ii * O0 / O0Oo0oO0o . I1iiiiI1iII % OOoOoo00oo / II1iI
 iI11i1I1 = oOOoo0Oo ( url )
 ii1iii1I1I = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in ii1iii1I1I :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
 o00OO00OoO = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( iI11i1I1 )
 OoO = datetime . now ( )
 for Oo0oOOo in o00OO00OoO :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
   o00oooO0Oo = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ]
   o00oooO0Oo = iI11 ( o00oooO0Oo )
   oO0Ooo0ooOO0 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ]
   i1IIiIii1i = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ]
   I1II = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in I1II :
    I1II = I1II . strip ( )
    I1II = time . strptime ( I1II , "%d/%m/%Y" )
    ooOOO0OooOo = ( "%s/%s/%s" % ( OoO . day , OoO . month , OoO . year ) )
    ooOOO0OooOo = time . strptime ( ooOOO0OooOo , "%d/%m/%Y" )
    if ( ooOOO0OooOo < I1II ) :
     o00oooO0Oo = '[COLOR yellow]' + ( o00oooO0Oo ) + ' - Not Aired Yet' + '[/COLOR]'
     i1IIiIii1i = '[COLOR yellow]' + ( i1IIiIii1i ) + '[/COLOR]'
     oO0Ooo0ooOO0 = '[COLOR yellow]' + ( oO0Ooo0ooOO0 ) + '[/COLOR]'
     if 33 - 33: OOoOoo00oo / i1IIi - II1iI % i1iIii1Ii1II . Oo0o0ooO0oOOO
    if not 'Season 0' in oO0Ooo0ooOO0 :
     Ii1iIiII1ii1 ( "[COLOR aqua]" + oO0Ooo0ooOO0 + " " + i1IIiIii1i + " " + o00oooO0Oo + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 17 - 17: O0Oo0oO0o / Oo0o0ooO0oOOO % i1Ii + II1iI * I111I11
  if 36 - 36: I111I11 * OOo000
def I1I ( url , iconimage , fanart ) :
 if 17 - 17: i11iIiiIii - O0Oo0oO0o * i11iI
 if 5 - 5: OOoOoo00oo - OOoOoo00oo . i1iIii1Ii1II + O0I11i1i11i1I - OOoOoo00oo . I1
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  try :
   o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
   o00oooO0Oo = o00oooO0Oo . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
   if not 'Lolzor.Com' in o00oooO0Oo :
    if not 'Videoplayer.Gq' in o00oooO0Oo :
     if not 'Vidbaba.Com' in o00oooO0Oo :
      if not 'Gagomatic.Com' in o00oooO0Oo :
       if not 'Favour.Me' in o00oooO0Oo :
        if not 'Funblr.Com' in o00oooO0Oo :
         if not 'Vid.Ag' in o00oooO0Oo :
          if not 'Mycollection.Net' in o00oooO0Oo :
           if not 'Adhqmedia.Com' in o00oooO0Oo :
            if not 'Filenuke.Com' in o00oooO0Oo :
             if not 'Mrfile.Me' in o00oooO0Oo :
              oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 31 - 31: O0Oo0oO0o - iIii1I11I1II1 - iIii1I11I1II1 % iiI11
  if 12 - 12: iIii1I11I1II1
def iIi1i ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  url = re . compile ( 'href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  import resolveurl
  try :
   if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
    O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    O0OOooOoO = liveresolver . resolve ( url )
   else : O0OOooOoO = url
   OoO000O0Oo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   OoO000O0Oo . setPath ( O0OOooOoO )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO000O0Oo )
   xbmc . Player ( ) . play ( O0OOooOoO )
   if 4 - 4: I111I11 / i11iIiiIii / OOoOoo00oo
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 91 - 91: iIii1I11I1II1 % i11iI . iIii1I11I1II1 % i1IIi / O0Oo0oO0o * O0I11i1i11i1I
def ii ( ) :
 if 81 - 81: O0 % I1iiiiI1iII
 o0o0OO0Oooooo = ''
 ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , 'Enter Search Term' )
 ii1ii111 . doModal ( )
 if ii1ii111 . isConfirmed ( ) :
  o0o0OO0Oooooo = ii1ii111 . getText ( )
  if len ( o0o0OO0Oooooo ) > 1 :
   I111i1i1111 = o0o0OO0Oooooo . lower ( )
   I111i1i1111 = I111i1i1111 . replace ( ' ' , '%20' )
   if 5 - 5: OoooooooOO - OOo000 + i1Ii - oOo0 . OOo000 / ooiii11iII
  else : quit ( )
 else : I111i1i1111 = urllib . unquote_plus ( oo0OooOOo0 ) . lower ( ) ; o0o0OO0Oooooo = urllib . unquote_plus ( oo0OooOOo0 )
 oo0OooOOo0 = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + I111i1i1111
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '"series"(.+?)"series_id"' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'original_name":"(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  i1Iii1i1I = re . compile ( '"seo_name":"(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://www.watchepisodeseries.com/' + i1Iii1i1I
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + i1Iii1i1I + '.jpg'
  Ii1iIiII1ii1 ( o00oooO0Oo , oo0OooOOo0 , 68 , I1IiI , I1ii11iIi11i , '' )
  if 28 - 28: I1iiiiI1iII * I1iiiiI1iII - iIii1I11I1II1
def ooOO00oOOo000 ( ) :
 if 14 - 14: OOo000 . O0Oo0oO0o . iiI11 / I1iiiiI1iII % Oo0o0ooO0oOOO - ooiii11iII
 oo0OooOOo0 = 'http://www.watchepisodeseries.com/home/popular-series'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<div title="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  o00oooO0Oo = iI11 ( o00oooO0Oo )
  oo0OooOOo0 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  Ii1iIiII1ii1 ( '[COLOR aqua]' + o00oooO0Oo + '[/COLOR]' , oo0OooOOo0 , 68 , I1IiI , I1ii11iIi11i )
  if 67 - 67: iiI11 - OOoOoo00oo . i1IIi
  if 35 - 35: oOo0 + ooiii11iII - I1 . oOo0 . i1Ii
def oo0ooOO ( ) :
 if 24 - 24: OOo000 % OOo000 * iIii1I11I1II1
 try :
  III = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o0o0OO0Oooooo = ''
  ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  ii1ii111 . doModal ( )
  if ii1ii111 . isConfirmed ( ) :
   o0o0OO0Oooooo = ii1ii111 . getText ( )
   if len ( o0o0OO0Oooooo ) > 1 :
    I111i1i1111 = o0o0OO0Oooooo
   else : quit ( )
  if I111i1i1111 == III :
   iIiIi11Ii ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  o0o0OO0Oooooo = ''
  ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , 'Enter The Password You Set' )
  ii1ii111 . doModal ( )
  if ii1ii111 . isConfirmed ( ) :
   o0o0OO0Oooooo = ii1ii111 . getText ( )
   if len ( o0o0OO0Oooooo ) > 1 :
    I111i1i1111 = o0o0OO0Oooooo
   else : quit ( )
  with open ( i1i1II , "w" ) as O0O0Ooo :
   O0O0Ooo . write ( I111i1i1111 )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 23 - 23: I1 - OOoOoo00oo + iiI11
   if 12 - 12: II1iI / ooiii11iII % i11iI / i11iIiiIii % OoooooooOO
   if 15 - 15: iIii1I11I1II1 % OoooooooOO - i1iIii1Ii1II * I1iiiiI1iII + iiI11
def iIiIi11Ii ( ) :
 if 11 - 11: oOo0 * I1iiiiI1iII - O0I11i1i11i1I
 OOO = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 III1iI1iII1I = '[COLOR aqua]Asian Special Porn[/COLOR]'
 Ii1iIiII1ii1 ( III1iI1iII1I , OOO , 1 , I1IiI , Oo , '' )
 oo0OooOOo0 = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<li class="">(.+?)</li>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<strong>(.+?)</strong>' ) . findall ( Oo0oOOo ) [ 0 ]
  I1i11IiI11i1 = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( Oo0oOOo ) [ 0 ]
  i1Iii1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'https://www.eporner.com' + i1Iii1i1I
  if not 'All' in o00oooO0Oo :
   if not 'Homemade' in o00oooO0Oo :
    Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "  " + "[COLOR yellow]" + I1i11IiI11i1 + "[/COLOR]" , oo0OooOOo0 , 36 , I1IiI , Oo , '' )
    if 87 - 87: I1 * I1 / II1iI / ooiii11iII % OOoOoo00oo
def OooOOO0O00 ( url ) :
 if 29 - 29: i11iI % iIii1I11I1II1 . OoooooooOO % OoooooooOO % O0Oo0oO0o / oOo0
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'title="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  i1Iii1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = 'https://www.eporner.com' + i1Iii1i1I
  Ii1iIiII1ii1 ( "[COLOR skyblue]" + o00oooO0Oo + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 70 - 70: i11iIiiIii % oOo0
 try :
  o000oo = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( iI11i1I1 ) [ 0 ]
  oOo0O0Oo00oO = 'https://www.eporner.com' + o000oo
  o00o0 = 'http://imgur.com/3eNoY0p'
  Ii1iIiII1ii1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , oOo0O0Oo00oO , 36 , o00o0 , Oo , '' )
 except : pass
 if 11 - 11: i1Ii % Oo0o0ooO0oOOO % I1iiiiI1iII / O0Oo0oO0o % I111I11 - i1iIii1Ii1II
def OOooOO00O0OO00oo ( url , iconimage ) :
 if 69 - 69: i11iI / i1iIii1Ii1II
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 oO0oO0 = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( oO0oO0 )
 for IIi , iI11i1I1 in O0oO :
  IIi = IIi . replace ( ':' , '' )
  url = 'https://www.eporner.com' + iI11i1I1
  oO0Oo ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + IIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 34 - 34: OoooooooOO . O0 / I1 * O0I11i1i11i1I - Oo0o0ooO0oOOO
def IiiiI ( url ) :
 if 42 - 42: i1IIi . II1iI / i1IIi + I1iiiiI1iII
 url = 'https://ww1.soul-anime.us/anime-list.html'
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<ul id="genre">(.*?)</ul>' ) . findall ( iI11i1I1 ) [ 0 ]
 O0oO = re . compile ( '<a rel=.*?href="(.*?)">(.*?)</a>' ) . findall ( o00OO00OoO )
 for iI11i1I1 , o00oooO0Oo in O0oO :
  Ii1iIiII1ii1 ( "[COLOR cyan]" + o00oooO0Oo + "[/COLOR]" , iI11i1I1 , 52 , I1IiI , Oo , '' )
 oOOo0oo ( )
def O0o0O0OO00o ( url ) :
 if 92 - 92: i11iI + I111I11 / i1iIii1Ii1II % OOo000 % i1Ii . OoooooooOO
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="lt">(.*?)<div class="tags"' ) . findall ( iI11i1I1 )
 for O0Oo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'alt="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  o00oOo0oOoo = re . compile ( '<p>(.*?)</p>' ) . findall ( O0Oo ) [ 0 ]
  I1IiI111I11 = re . compile ( '<span class=".*?">(.*?)</span>' ) . findall ( O0Oo ) [ 0 ]
  if 'Completed' in I1IiI111I11 :
   I1IiI111I11 = '[COLOR red]' + I1IiI111I11 + '[/COLOR]'
  else :
   I1IiI111I11 = '[COLOR lime]' + I1IiI111I11 + '[/COLOR]'
  Ii1iIiII1ii1 ( "[COLOR cyan]" + o00oooO0Oo + " :: " + I1IiI111I11 + "[/COLOR]" , url , 53 , I1IiI , Oo , o00oOo0oOoo )
 oOOo0oo ( )
 if 16 - 16: O0 / I1iiiiI1iII . Oo0o0ooO0oOOO
def oOOOo ( url ) :
 if 68 - 68: I1 - Oo0o0ooO0oOOO % O0 % I111I11
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<div class="img_box">(.*?)</span>' ) . findall ( iI11i1I1 )
 for O0Oo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<div class="ep">(.*?)</div>' ) . findall ( O0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  oO0Oo ( "[COLOR cyan]" + o00oooO0Oo + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
 oOOo0oo ( )
 if 11 - 11: O0 / OOo000 % OOoOoo00oo + i11iI + iIii1I11I1II1
def I1i1111I ( url , iconimage ) :
 if 95 - 95: iIii1I11I1II1 - Oo0o0ooO0oOOO . I111I11 - II1iI
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . compile ( '<iframe name="stream".*?src="(.*?)"' ) . findall ( iI11i1I1 ) [ 0 ]
 o0oO0O0o0O00O = oOOoo0Oo ( o00OO00OoO )
 try :
  oO0oO0 = re . compile ( '<iframe.*?src="(.*?)"' ) . findall ( o0oO0O0o0O00O ) [ 0 ]
  O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , oO0oO0 , iconimage )
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Source Link Is Down[/COLOR]' , iconimage , 5000 )
  if 75 - 75: OOo000 + i11iI - i1IIi . OoooooooOO * I1iiiiI1iII / i1Ii
def OOOooo0OooOoO ( url ) :
 if 91 - 91: I1 + II1iI
 url = 'http://m4ufree.io/'
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'title="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( './' , '/' )
  if not 'http://' in url :
   url = 'http://m4ufree.io/' + url
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  IIi = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( Oo0oOOo ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[COLOR yellow] " + IIi + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 59 - 59: II1iI + i11iIiiIii + i1IIi / iiI11
 try :
  oOo0O0Oo00oO = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( iI11i1I1 ) [ 0 ]
  o000oo = re . compile ( '<a.+?href="(.+?)"' ) . findall ( oOo0O0Oo00oO ) [ 5 ]
  if 'genre' in o000oo :
   I11 = I11 . replace ( '.com' , '.com/' )
  iIiI1 = I1IiI
  Ii1iIiII1ii1 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , o000oo , 42 , iIiI1 , Oo , description = '' )
 except : pass
 if 86 - 86: i11iI
def Ii ( url , iconimage ) :
 if 2 - 2: Oo0o0ooO0oOOO . Oo0o0ooO0oOOO + Oo0o0ooO0oOOO * i11iI
 import requests
 oOo00oOOOOO = url
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOOo0O00 = re . compile ( 'data="(.+?)"' ) . findall ( iI11i1I1 )
 iIiI = 'http://m4ufree.io/ajax_new.php'
 for ooOooo000oOO in OoOOo0O00 :
  try :
   iIiI = 'http://m4ufree.io/ajax_new.php'
   iIIIi1i1I11i = requests . post ( iIiI , data = { 'm4u' : ooOooo000oOO } )
   json = ( iIIIi1i1I11i . text )
   oOO0OO0OO = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
   oOOoooO = re . compile ( '{(.+?)}' ) . findall ( oOO0OO0OO )
   i1ii11 = 0
   for OoO in oOOoooO :
    i1ii11 += 1
    o00oooO0Oo = 'Link ' + str ( i1ii11 )
    try :
     IIi = re . compile ( '''"label":"(.+?)"''' ) . findall ( OoO ) [ 0 ]
     o0O = re . compile ( '''"file":"(.+?)"''' ) . findall ( OoO ) [ 0 ]
     url = 'http://m4ufree.io/' + o0O + '|referer=' + oOo00oOOOOO
     oO0Oo ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + IIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
    except :
     IIi = re . compile ( """label:.+?'(.+?)'""" ) . findall ( OoO ) [ 0 ]
     o0O = re . compile ( '''file: "(.+?)"''' ) . findall ( OoO ) [ 0 ]
     url = 'http://m4ufree.io/' + o0O + '|referer=' + oOo00oOOOOO
     oO0Oo ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + IIi + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except : pass
  if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
  if 58 - 58: I1
def IiIIi1IiiI1 ( ) :
 if 87 - 87: I1 % I1iiiiI1iII
 oo0OooOOo0 = 'https://www.livefootballol.me/acestream-channel-list-2017.html'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 O0oO = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI11i1I1 )
 for O0Oo in O0oO :
  o00oooO0Oo = re . compile ( '<strong>(.+?)</strong>' ) . findall ( O0Oo ) [ 0 ]
  if len ( o00oooO0Oo ) == 1 or '&nbsp;' in o00oooO0Oo :
   o00oooO0Oo = re . compile ( '<strong>(.+?)</strong>' ) . findall ( O0Oo ) [ 1 ]
  if len ( o00oooO0Oo ) > 40 :
   o00oooO0Oo = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( O0Oo ) [ 0 ]
  oo0OooOOo0 = re . compile ( '<td>(.+?)</td>' ) . findall ( O0Oo ) [ 2 ]
  oo0OOOoOo = re . compile ( '<td>(.+?)</td>' ) . findall ( O0Oo ) [ 3 ]
  IIiiIIi1 = re . compile ( '<td>(.+?)</td>' ) . findall ( O0Oo ) [ 4 ]
  o00oooO0Oo = o00oooO0Oo . strip ( )
  oo0OooOOo0 = oo0OooOOo0 . strip ( )
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + ' :: [COLOR yellow]' + oo0OOOoOo + '[COLOR aqua] :: [COLOR yellow]' + IIiiIIi1 + ' Kbps[/COLOR]' , oo0OooOOo0 , 2 , oO0 , Oo , '' )
  if 51 - 51: O0I11i1i11i1I
def I11IIIiIi11 ( ) :
 if 39 - 39: I1iiiiI1iII % O0 % O0I11i1i11i1I . i1IIi
 oo0OooOOo0 = 'http://acestreamchannel.blogspot.co.uk/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 O0oO = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in O0oO :
  try :
   o00oooO0Oo = re . compile ( '<td>(.+?)</td>' ) . findall ( Oo0oOOo ) [ 0 ]
   if len ( o00oooO0Oo ) < 40 :
    oo0OooOOo0 = re . compile ( 'href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
    oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 2 , oO0 , Oo , '' )
  except : pass
  if 86 - 86: OOo000 * OoooooooOO
def OooO0oOo ( ) :
 if 66 - 66: OOo000 * i1iIii1Ii1II
 oo0OooOOo0 = 'https://acestreamid.com/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<li class="collection-item acestreamidID ">(.*?)</li>' ) . findall ( iI11i1I1 )
 for O0Oo in o00OO00OoO :
  o00oooO0Oo = re . compile ( 'title="(.*?)"' ) . findall ( O0Oo ) [ 0 ]
  if 'Broken' in o00oooO0Oo :
   o00oooO0Oo = re . compile ( '<span class="font-small grey-text truncate content">(.*?)</span>' ) . findall ( O0Oo ) [ 0 ] . strip ( )
  iI11i1I1 = re . compile ( '<div class="content wrap">(.*?)</div>' ) . findall ( O0Oo ) [ 0 ]
  iI11i1I1 = 'acestream://' + iI11i1I1
  I1IiI111I11 = re . compile ( 'title="(.*?)"' ) . findall ( O0Oo ) [ 1 ]
  try :
   II1IIIiiI11 = re . findall ( r'\d+' , I1IiI111I11 ) [ 0 ]
  except IndexError :
   II1IIIiiI11 = 0
  oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + " [COLOR yellow]Down Reports :: " + str ( II1IIIiiI11 ) + "[/COLOR]" , iI11i1I1 , 2 , oO0 , Oo , '' )
  if 86 - 86: OOo000 % OoooooooOO % OOo000 / II1iI
def Oo0ooo0Ooo ( ) :
 oo0OooOOo0 = 'http://jkarakizi.com/updated-acestream-channels-for-2018/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 )
 o00OO00OoO = re . compile ( '<tr>(.*?)</tr>' ) . findall ( iI11i1I1 )
 for O0Oo in o00OO00OoO :
  try :
   o00oooO0Oo = re . compile ( '<td class=".+?">(.*?)</td>' ) . findall ( O0Oo ) [ 0 ]
   iI11i1I1 = re . compile ( '<td class="tg-yw4l">(.*?)</td>' ) . findall ( O0Oo ) [ 1 ]
   iI11i1I1 = 'acestream://' + iI11i1I1
   oO0Oo ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , iI11i1I1 , 2 , oO0 , Oo , '' )
  except : pass
  if 9 - 9: i1iIii1Ii1II
def O0O00OOo ( ) :
 if 66 - 66: i11iIiiIii / i11iI - OoooooooOO / i1IIi . i11iIiiIii
 oo0OooOOo0 = 'http://www.livefootballol.me/streaming/english-premier-league-2018/'
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<td>(.+?)</td>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  oo0OooOOo0 = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ]
  oO00oooOOoOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  oo0OooOOo0 = 'http://www.livefootballol.me' + oo0OooOOo0
  Ii1iIiII1ii1 ( "[COLOR aqua]" + oO00oooOOoOo0 + "[/COLOR]" , oo0OooOOo0 , 74 , oO0 , Oo , '' )
  if 16 - 16: i1iIii1Ii1II % Oo0o0ooO0oOOO + iiI11 - O0 . oOo0 / I111I11
def IIi1I ( url ) :
 if 27 - 27: O0 . I111I11 / oOo0
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<a href="(.+?)"' ) . findall ( iI11i1I1 )
 OO00O000OOO = 0
 for oOooOOOoOo in o00OO00OoO :
  if 'acestream' in oOooOOOoOo :
   if 'http' in oOooOOOoOo :
    OO00O000OOO += 1
    o00oooO0Oo = '[COLOR aqua]Link :: ' + str ( OO00O000OOO ) + '[/COLOR]'
    oO0Oo ( o00oooO0Oo , oOooOOOoOo , 75 , oO0 , Oo , '' )
 if OO00O000OOO == 0 :
  oO0Oo ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , oO0 , Oo , '' )
  if 3 - 3: O0
def Ooo0Oo0oo0 ( url ) :
 if 83 - 83: I111I11
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( iI11i1I1 ) [ 0 ]
 O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , url , oO0 )
 if 48 - 48: O0Oo0oO0o * OOoOoo00oo * I111I11
def i1iiiIii11 ( url ) :
 if 67 - 67: i11iI % O0I11i1i11i1I . O0I11i1i11i1I - ooiii11iII
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00ooOo = 'https://yo-movies.com/'
 iI11i1I1 = oOOoo0Oo ( url )
 o00OO00OoO = re . findall ( 'class="ml-item">(.*?)</a>' , iI11i1I1 )
 for OoO in o00OO00OoO :
  o00oooO0Oo = re . findall ( 'oldtitle="(.*?)"' , OoO ) [ 0 ]
  o0O = re . findall ( '<a href="(.*?)"' , OoO ) [ 0 ]
  if not O00ooOo in o0O : o0O = O00ooOo + o0O
  I1IiI = re . findall ( '<img data-original="(.*?)"' , OoO ) [ 0 ] . strip ( ) . replace ( 'w185' , 'original' )
  IIi = re . findall ( '<span class="mli-quality">(.*?)</span>' , OoO ) [ 0 ]
  Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + ' | ' + '[COLOR yellow]' + IIi + "[/COLOR]" , o0O , 81 , I1IiI , I1IiI , '' )
 try :
  oOO0o00O = 6
  oOOoooO = 'page'
  oOoO = url . split ( oOOoooO , 1 ) [ - 1 ]
  IIII = oOoO . replace ( '/' , '' )
  oOoO = int ( IIII )
  if oOoO < oOO0o00O :
   oOoO = oOoO + 1
   oOo0O0Oo00oO = 'https://yo-movies.com/genre/bollywood/page/' + str ( oOoO ) + '/'
  Ii1iIiII1ii1 ( "[COLOR yellow]Next Page --->[/COLOR]" , oOo0O0Oo00oO , 80 , oO0 , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 50 - 50: i1iIii1Ii1II % i1Ii
def iIi ( url , iconimage ) :
 if 10 - 10: OOo000 / i1iIii1Ii1II
 iI11i1I1 = oOOoo0Oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . findall ( '<div class="btn-group btn-group-justified embed-selector"\s+>(.*?)</div>' , iI11i1I1 ) [ 0 ]
 I1i = r'''<a\s+href=['"]([^'"]+)['"].+?Download'''
 oOooOOOoOo = re . findall ( I1i , o00OO00OoO )
 I1i11IiI11i1 = 0
 for Oo0oOOo in oOooOOOoOo :
  I1i11IiI11i1 += 1
  o000ooooO0o = 'Link' + ' | ' + str ( I1i11IiI11i1 )
  oO0Oo ( "[COLOR aqua]" + o000ooooO0o + "[/COLOR]" , Oo0oOOo , 2 , iconimage , iconimage , '' )
  if 50 - 50: i11iI * I1iiiiI1iII % Oo0o0ooO0oOOO / i1iIii1Ii1II - O0 % oOo0
def IIII1ii ( url , getphp ) :
 i11I1 = urllib2 . Request ( url )
 i11I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 i11I1 . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 Ii11Ii11I = urllib2 . urlopen ( i11I1 , timeout = 10 )
 iI11i1I1 = Ii11Ii11I . read ( )
 Ii11Ii11I . close ( )
 return iI11i1I1
 if 13 - 13: OoooooooOO * I1 - I1iiiiI1iII / OOoOoo00oo + iiI11 + i1Ii
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: Oo0o0ooO0oOOO - O0 * OoooooooOO
def iiIiI ( ) :
 if 87 - 87: ooiii11iII - OoooooooOO + i11iIiiIii
 oo0OooOOo0 = 'http://m4ufree.com/?sort=key_top&page=1&='
 iI11i1I1 = oOOoo0Oo ( oo0OooOOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o00OO00OoO = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( iI11i1I1 )
 for Oo0oOOo in o00OO00OoO :
  o00oooO0Oo = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Oo0oOOo ) [ 0 ]
  i1Iii1i1I = re . compile ( '<a href="(.+?)"' ) . findall ( Oo0oOOo ) [ 0 ] . replace ( './' , '' )
  oo0OooOOo0 = 'http://m4ufree.com/' + i1Iii1i1I
  if not re . search ( '\d+' , o00oooO0Oo ) :
   Ii1iIiII1ii1 ( "[COLOR aqua]" + o00oooO0Oo + "[/COLOR]" , oo0OooOOo0 , 42 , I1IiI , Oo )
   if 73 - 73: iiI11 * OoooooooOO . O0 . i1Ii
   if 55 - 55: i1iIii1Ii1II
   if 77 - 77: O0Oo0oO0o
   if 16 - 16: II1iI * O0Oo0oO0o / iIii1I11I1II1 - oOo0
   if 3 - 3: II1iI * ooiii11iII + O0Oo0oO0o - OOo000
   if 97 - 97: Oo0o0ooO0oOOO / I1 - i11iI - II1iI - II1iI
   if 54 - 54: i1iIii1Ii1II + II1iI / oOo0 . II1iI * O0I11i1i11i1I
   if 1 - 1: O0I11i1i11i1I * OOo000 . i1IIi / i1iIii1Ii1II . Oo0o0ooO0oOOO + i1iIii1Ii1II
   if 17 - 17: i1iIii1Ii1II + OOo000 / I1iiiiI1iII / oOo0 * OOoOoo00oo
   if 29 - 29: OOo000 % OoooooooOO * I1 / O0Oo0oO0o - I1
def iI11 ( text ) :
 if 19 - 19: i11iIiiIii
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
 if 54 - 54: O0Oo0oO0o . iiI11
 return text
 if 73 - 73: O0I11i1i11i1I . II1iI
def II1i11i1iIi11 ( ) :
 if 83 - 83: I1iiiiI1iII
 I1iI1I1 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IiIi1 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 oo00ooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 iii1IIIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 94 - 94: O0 - iiI11 - iIii1I11I1II1 % ooiii11iII / I1iiiiI1iII % oOo0
 iIi1IIi1ii = 0
 for ( iiIIiIiIi , I11Ii , iIiII ) in os . walk ( IiIi1 ) :
  for file in iIiII :
   i1i1IIIIIIIi = os . path . join ( iiIIiIiIi , file )
   iIi1IIi1ii += os . path . getsize ( i1i1IIIIIIIi )
 II11i1I11Ii1i = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( iIi1IIi1ii / ( 1024 * 1024.0 ) )
 oO0Oo ( II11i1I11Ii1i , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 65 - 65: i11iI
 iIi1IIi1ii = 0
 for ( iiIIiIiIi , I11Ii , iIiII ) in os . walk ( I1iI1I1 ) :
  for file in iIiII :
   i1i1IIIIIIIi = os . path . join ( iiIIiIiIi , file )
   iIi1IIi1ii += os . path . getsize ( i1i1IIIIIIIi )
 II11i1I11Ii1i = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( iIi1IIi1ii / ( 1024 * 1024.0 ) )
 oO0Oo ( II11i1I11Ii1i , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 7 - 7: i1Ii . O0I11i1i11i1I / Oo0o0ooO0oOOO . OOoOoo00oo * iiI11 - O0Oo0oO0o
 iIi1IIi1ii = 0
 for ( iiIIiIiIi , I11Ii , iIiII ) in os . walk ( oo00ooOoo ) :
  for file in iIiII :
   i1i1IIIIIIIi = os . path . join ( iiIIiIiIi , file )
   iIi1IIi1ii += os . path . getsize ( i1i1IIIIIIIi )
 II11i1I11Ii1i = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( iIi1IIi1ii / ( 1024 * 1024.0 ) )
 oO0Oo ( II11i1I11Ii1i , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 37 - 37: I111I11 . O0I11i1i11i1I / O0 * oOo0
 iIi1IIi1ii = 0
 for ( iiIIiIiIi , I11Ii , iIiII ) in os . walk ( iii1IIIiiiI ) :
  for file in iIiII :
   i1i1IIIIIIIi = os . path . join ( iiIIiIiIi , file )
   iIi1IIi1ii += os . path . getsize ( i1i1IIIIIIIi )
 II11i1I11Ii1i = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( iIi1IIi1ii / ( 1024 * 1024.0 ) )
 oO0Oo ( II11i1I11Ii1i , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 7 - 7: OOo000 * iiI11 + O0Oo0oO0o % i11iIiiIii
 oO0Oo ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 oO0Oo ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 8 - 8: ooiii11iII * O0
def O0Oo0oOOoooOOOOo ( name , url , iconimage ) :
 if 73 - 73: i11iI / I1 / iiI11 / OOo000
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import resolveurl
 if 'acestream' in url :
  i1Iii1i1I = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  OoO000O0Oo . setPath ( url )
  xbmc . Player ( ) . play ( i1Iii1i1I , OoO000O0Oo , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
  OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OoO000O0Oo . setPath ( O0OOooOoO )
  xbmc . Player ( ) . play ( O0OOooOoO , OoO000O0Oo , False )
  time . sleep ( 2 )
  quit ( )
 else :
  O0OOooOoO = url
  OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OoO000O0Oo . setPath ( O0OOooOoO )
  xbmc . Player ( ) . play ( O0OOooOoO , OoO000O0Oo , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 11 - 11: O0I11i1i11i1I + i1Ii - OoooooooOO / OOo000
def iIIi1iI1I1IIi ( name , url , iconimage ) :
 if 77 - 77: ooiii11iII / i1iIii1Ii1II + ooiii11iII % i11iI - II1iI * II1iI
 iI , I1oO0ooOoO = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 iI += urllib . unquote_plus ( I1oO0ooOoO )
 url = regex . resolve ( iI )
 if 59 - 59: O0 % i1iIii1Ii1II
 PLAYREGEX ( name , url , iconimage )
 if 92 - 92: I1iiiiI1iII % oOo0 / Oo0o0ooO0oOOO % Oo0o0ooO0oOOO * II1iI
def OOOoOO0o ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 74 - 74: O0 . II1iI % OOo000 % i1Ii
def O00o ( heading , text ) :
 if 87 - 87: I1 - i11iIiiIii
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 ooOoO = xbmcgui . Window ( id )
 iIIIIiiIii = 50
 while ( iIIIIiiIii > 0 ) :
  try :
   xbmc . sleep ( 10 )
   iIIIIiiIii -= 1
   ooOoO . getControl ( 1 ) . setLabel ( heading )
   ooOoO . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 58 - 58: i1iIii1Ii1II
  if 9 - 9: iIii1I11I1II1 % Oo0o0ooO0oOOO . OOoOoo00oo + OoooooooOO
def oOOoo0Oo ( url ) :
 try :
  i11I1 = urllib2 . Request ( url )
  i11I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ii11Ii11I = urllib2 . urlopen ( i11I1 , timeout = 5 )
  iI11i1I1 = Ii11Ii11I . read ( )
  Ii11Ii11I . close ( )
  iI11i1I1 = iI11i1I1 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI11i1I1
 except : quit ( )
 if 62 - 62: O0 / II1iI % O0 * OOo000 % II1iI
def OooOo0ooo ( url ) :
 try :
  i11I1 = urllib2 . Request ( url )
  i11I1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  Ii11Ii11I = urllib2 . urlopen ( i11I1 , timeout = 5 )
  iI11i1I1 = Ii11Ii11I . read ( )
  Ii11Ii11I . close ( )
  iI11i1I1 = iI11i1I1 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI11i1I1
 except : quit ( )
 if 33 - 33: II1iI . I1 * OOo000 * iIii1I11I1II1
def oO0Oo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 II11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1iIiiIiI = True
 OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OoO000O0Oo . setProperty ( "fanart_Image" , fanart )
 OoO000O0Oo . setProperty ( "icon_Image" , iconimage )
 OoO000O0Oo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OoO000O0Oo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 26 - 26: iIii1I11I1II1 % i11iIiiIii % Oo0o0ooO0oOOO
 i111i1iIiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = OoO000O0Oo , isFolder = False )
 return i111i1iIiiIiI
 if 67 - 67: OoooooooOO
def iii1i1iiiiIi ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 II11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1iIiiIiI = True
 OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OoO000O0Oo . setProperty ( "fanart_Image" , fanart )
 OoO000O0Oo . setProperty ( "icon_Image" , iconimage )
 OoO000O0Oo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 29 - 29: O0 - i11iIiiIii - O0Oo0oO0o + OOoOoo00oo * i1Ii
 OoO000O0Oo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 2 - 2: i1IIi - ooiii11iII + II1iI . i11iI * i11iI / O0I11i1i11i1I
 i111i1iIiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = OoO000O0Oo , isFolder = False )
 return i111i1iIiiIiI
 if 93 - 93: i1IIi
def ooOOOo ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OO000oOoo0O = [ ]
 iIIiii11iIiiI = [ ]
 O0Oo0 = [ ]
 iI11i1I1 = oOOoo0Oo ( url )
 oOooOOOoOo = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI11i1I1 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOooOOOoOo ) [ 0 ]
 Oo0oOOo = re . compile ( '<link>(.+?)</link>' ) . findall ( oOooOOOoOo )
 if len ( Oo0oOOo ) < 1 :
  Oo0oOOo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( oOooOOOoOo )
 OoO = 1
 for o0oO0oo0000OO in Oo0oOOo :
  I1i1ii1IiIii = o0oO0oo0000OO
  if '(' in o0oO0oo0000OO :
   o0oO0oo0000OO = o0oO0oo0000OO . split ( '(' ) [ 0 ]
   oOOO0O0Ooo = str ( I1i1ii1IiIii . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OO000oOoo0O . append ( o0oO0oo0000OO )
   iIIiii11iIiiI . append ( oOOO0O0Ooo )
  else :
   OO000oOoo0O . append ( o0oO0oo0000OO )
   iIIiii11iIiiI . append ( '[COLOR aqua]Link ' + str ( OoO ) + '[/COLOR]' )
  OoO = OoO + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 IiI1i111IiIiIi1 = Iii1ii1II11i . select ( name , iIIiii11iIiiI )
 if IiI1i111IiIiIi1 < 0 :
  quit ( )
 else :
  url = OO000oOoo0O [ IiI1i111IiIiIi1 ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : O0OOooOoO = liveresolver . resolve ( url )
  else : O0OOooOoO = url
  OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  OoO000O0Oo . setPath ( O0OOooOoO )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoO000O0Oo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( O0OOooOoO )
  if 39 - 39: iiI11 - Oo0o0ooO0oOOO
def OOO0o0OO0OO ( name , url , iconimage ) :
 if 64 - 64: O0Oo0oO0o
 iIIIiIi1I1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 OO000oOoo0O = [ ]
 iIIiii11iIiiI = [ ]
 O0Oo0 = [ ]
 OoOOoO0oOo = [ ]
 iI11i1I1 = oOOoo0Oo ( url )
 oOooOOOoOo = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI11i1I1 ) [ 0 ]
 Oo0oOOo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOooOOOoOo )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOooOOOoOo ) [ 0 ]
 OoO = 1
 if 70 - 70: iiI11 % iIii1I11I1II1 . i1iIii1Ii1II + i1iIii1Ii1II - i11iI % I111I11
 for o0oO0oo0000OO in Oo0oOOo :
  I1i1ii1IiIii = o0oO0oo0000OO
  if '(' in o0oO0oo0000OO :
   o0oO0oo0000OO = o0oO0oo0000OO . split ( '(' ) [ 0 ]
   oOOO0O0Ooo = str ( I1i1ii1IiIii . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OO000oOoo0O . append ( o0oO0oo0000OO )
   iIIiii11iIiiI . append ( oOOO0O0Ooo )
   OoOOoO0oOo . append ( 'Stream ' + str ( OoO ) )
  else :
   OO000oOoo0O . append ( o0oO0oo0000OO )
   iIIiii11iIiiI . append ( 'Link ' + str ( OoO ) )
   if 38 - 38: I111I11 % OOoOoo00oo - OoooooooOO
  OoO = OoO + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 IiI1i111IiIiIi1 = Iii1ii1II11i . select ( name , iIIiii11iIiiI )
 if IiI1i111IiIiIi1 < 0 :
  quit ( )
 else :
  OO0OoO0o00 = iIIiii11iIiiI [ IiI1i111IiIiIi1 ]
  ooOO0O0ooOooO = "/"
  if not OO0OoO0o00 . endswith ( ooOO0O0ooOooO ) :
   oOOOo00O00oOo = OO0OoO0o00 + "/"
  else :
   oOOOo00O00oOo = OO0OoO0o00
  url = iIIIiIi1I1i + OO000oOoo0O [ IiI1i111IiIiIi1 ] + "%26referer=" + oOOOo00O00oOo
  print url
  if 87 - 87: OOo000 % II1iI
  xbmc . Player ( ) . play ( url )
  if 77 - 77: iIii1I11I1II1 - i1IIi . I1
def ooOO0OOOO0oo0 ( string ) :
 iIi1iIIIiIiI = ( c for c in string if 0 < ord ( c ) < 127 )
 if 62 - 62: i11iIiiIii % OOoOoo00oo . i1Ii . OOoOoo00oo
 return '' . join ( iIi1iIIIiIiI )
 if 84 - 84: i11iIiiIii * OOo000
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 18 - 18: OOoOoo00oo - I1iiiiI1iII - O0I11i1i11i1I / I111I11 - O0
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 II11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i111i1iIiiIiI = True
 OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 OoO000O0Oo . setProperty ( "fanart_Image" , fanart )
 OoO000O0Oo . setProperty ( "icon_Image" , iconimage )
 OoO000O0Oo . setInfo ( 'video' , { 'Plot' : description } )
 i111i1iIiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II11 , listitem = OoO000O0Oo , isFolder = True )
 return i111i1iIiiIiI
 if 30 - 30: O0 + Oo0o0ooO0oOOO + O0Oo0oO0o
def III1I ( name , url , iconimage ) :
 i111i1iIiiIiI = True
 OoO000O0Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OoO000O0Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i111i1iIiiIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OoO000O0Oo )
 xbmc . Player ( ) . play ( url , OoO000O0Oo , False )
 if 11 - 11: ooiii11iII - OOoOoo00oo + ooiii11iII * I1 / II1iI
def OoOOOO ( ) :
 if 18 - 18: ooiii11iII % i11iIiiIii . iIii1I11I1II1 - oOo0
 I1iI1I1 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IiIi1 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 oo00ooOoo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 80 - 80: II1iI + I1 - i1IIi . I1iiiiI1iII / i11iI / II1iI
 OoO = [ ( I1iI1I1 , 'Cache' ) , ( IiIi1 , 'Thumbnails' ) , ( oo00ooOoo , 'Packages' ) ]
 if 1 - 1: iiI11 + i11iIiiIii - II1iI / OOoOoo00oo + I111I11
 OO0OO0O = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if OO0OO0O :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for iI in OoO :
   if 75 - 75: iiI11 / i11iI / OOoOoo00oo / i1Ii % ooiii11iII + O0Oo0oO0o
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % iI [ 1 ] )
   time . sleep ( 1 )
   if 4 - 4: oOo0 - i1iIii1Ii1II - i1Ii - iiI11 % i11iIiiIii / OOo000
   for i1iii11 , I11Ii , iIiII in os . walk ( iI [ 0 ] ) :
    for OOooO in iIiII :
     if ( OOooO . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( i1iii11 , OOooO ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % iI [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 92 - 92: O0I11i1i11i1I . OoooooooOO - I111I11
def Oo0000o0O0O ( url , mode , name , iconimage , fanart ) :
 if 1 - 1: Oo0o0ooO0oOOO % O0I11i1i11i1I . i11iI . II1iI - II1iI - i1Ii
 with open ( I11i , "a" ) as O0O0Ooo :
  O0O0Ooo . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 33 - 33: II1iI / OOo000
def iiIIi ( ) :
 if 36 - 36: iiI11 . O0Oo0oO0o
 with open ( I11i , "a" ) as O0O0Ooo :
  iIIiI1iiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  I11Ii111I = open ( iIIiI1iiI ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00OO00OoO = re . compile ( '<item>(.+?)</item>' ) . findall ( I11Ii111I )
  oO0Oo ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  oO0Oo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  if len ( o00OO00OoO ) < 1 :
   oO0Oo ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  for O0Oo in o00OO00OoO :
   o00oooO0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0Oo ) [ 0 ]
   oo0OooOOo0 = re . compile ( '<url>(.+?)</url>' ) . findall ( O0Oo ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0Oo ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0Oo ) [ 0 ]
   oO0Oo ( '[COLOR skyblue]' + o00oooO0Oo + '[/COLOR]' , oo0OooOOo0 , 2 , I1IiI , I1ii11iIi11i )
   if 98 - 98: iIii1I11I1II1 + I111I11 % O0I11i1i11i1I + iiI11 % O0I11i1i11i1I
 oO0Oo ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , oO0 , Oo )
 if 24 - 24: I1 * I111I11
def I11IiIIIi ( ) :
 if 77 - 77: iIii1I11I1II1 . I1iiiiI1iII % I1 / I1iiiiI1iII
 with open ( IiII , "a" ) as O0O0Ooo :
  iIIiI1iiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  I11Ii111I = open ( iIIiI1iiI ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o00OO00OoO = re . compile ( '<item>(.+?)</item>' ) . findall ( I11Ii111I )
  oO0Oo ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  oO0Oo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  if len ( o00OO00OoO ) < 1 :
   oO0Oo ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , oO0 , Oo )
  for O0Oo in o00OO00OoO :
   o00oooO0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0Oo ) [ 0 ]
   oo0OooOOo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( O0Oo ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0Oo ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0Oo ) [ 0 ]
   oO0Oo ( '[COLOR skyblue]' + o00oooO0Oo + '[/COLOR]' , oo0OooOOo0 , 2 , I1IiI , I1ii11iIi11i )
   if 54 - 54: I1 + ooiii11iII - i1iIii1Ii1II
 oO0Oo ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , oO0 , Oo )
 if 35 - 35: I1iiiiI1iII - I1iiiiI1iII + i1IIi - O0 - I111I11
def oOO0o0oo0 ( ) :
 if 78 - 78: OOoOoo00oo + oOo0 . i1Ii
 with open ( I11i , "w" ) as O0O0Ooo :
  O0O0Ooo . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 91 - 91: iIii1I11I1II1 . i11iI . Oo0o0ooO0oOOO + OoooooooOO
def o0o0O0Oo ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as O0O0Ooo :
  O0O0Ooo . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 1 - 1: iIii1I11I1II1 + i1iIii1Ii1II / O0 - oOo0 % i1Ii + i1Ii
 if 24 - 24: II1iI + i1iIii1Ii1II + OOoOoo00oo - OoooooooOO + i1iIii1Ii1II
 if 93 - 93: ooiii11iII . iIii1I11I1II1 % i11iIiiIii . O0I11i1i11i1I % ooiii11iII + O0
def i1I1iI ( ) :
 if 65 - 65: I1iiiiI1iII + OOo000 - OoooooooOO
 if 51 - 51: i1iIii1Ii1II + I1 / oOo0 - i1IIi
 oO0O0oO0 = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I11Ii1iI11iI1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oO0O0oO0 ) [ 0 ]
  if I11Ii1iI11iI1 == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   o0o0OO0Oooooo = ''
   ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   ii1ii111 . doModal ( )
   if ii1ii111 . isConfirmed ( ) :
    o0o0OO0Oooooo = ii1ii111 . getText ( )
    if len ( o0o0OO0Oooooo ) > 1 :
     I111i1i1111 = o0o0OO0Oooooo . title ( )
     with open ( iI1Ii11111iIi , "w" ) as OOooO :
      OOooO . write ( "<pin>" + I111i1i1111 + "</pin>" )
     i1I1iI ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in I11Ii1iI11iI1 :
   i1III1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oO0O0oO0 ) [ 0 ]
   Iii111IiIii = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % i1III1 )
   iI11i1I1 = oOOoo0Oo ( Iii111IiIii )
   if len ( iI11i1I1 ) < 1 or 'Pin Expired' in iI11i1I1 :
    with open ( iI1Ii11111iIi , "w" ) as OOooO :
     OOooO . write ( '<pin>EXPIRED</pin>' )
    i1I1iI ( )
   else :
    global baseurl
    baseurl = iI11i1I1
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as OOooO :
   OOooO . write ( "<pin>EXPIRED</pin>\n" )
  i1I1iI ( )
  if 100 - 100: O0Oo0oO0o - i11iI . O0Oo0oO0o * O0Oo0oO0o . i1Ii
  if 2 - 2: OoooooooOO
  if 60 - 60: OOo000
  if 81 - 81: O0I11i1i11i1I % I1iiiiI1iII
def oo0 ( url , iconimage , fanart ) :
 if 16 - 16: I1iiiiI1iII * OOo000 / I1
 try :
  o0o0OO0Oooooo = ''
  ii1ii111 = xbmc . Keyboard ( o0o0OO0Oooooo , 'Enter Name To Save File As' )
  ii1ii111 . doModal ( )
  if ii1ii111 . isConfirmed ( ) :
   o0o0OO0Oooooo = ii1ii111 . getText ( )
   if len ( o0o0OO0Oooooo ) > 1 :
    I111i1i1111 = o0o0OO0Oooooo . title ( )
   else : quit ( )
  import resolveurl
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   O0OOooOoO = resolveurl . HostedMediaFile ( url ) . resolve ( )
   url = O0OOooOoO
  II1iiI = url . split ( '/' ) [ - 1 ]
  II11 = urllib2 . urlopen ( url )
  III1Ii1i1I1 = os . path . join ( o0OOO , I111i1i1111 )
  OOooO = open ( III1Ii1i1I1 , 'wb' )
  if 97 - 97: I111I11 . ooiii11iII - I111I11 + II1iI * O0Oo0oO0o
  I111Ii = II11 . info ( )
  II11iIi = int ( I111Ii . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( I111i1i1111 , II11iIi ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 29 - 29: O0 . I111I11
  OO0o0oO0O000o = 0
  I1iI11iii = 8192
  while True :
   buffer = II11 . read ( I1iI11iii )
   if not buffer :
    break
    if 78 - 78: O0 / O0Oo0oO0o * OOo000
   OO0o0oO0O000o += len ( buffer )
   OOooO . write ( buffer )
   I1IiI111I11 = "[%3.2f%%]" % ( OO0o0oO0O000o * 100. / II11iIi )
   I1IiI111I11 = I1IiI111I11 + chr ( 8 ) * ( len ( I1IiI111I11 ) + 1 )
   iIiiiI . update ( OO0o0oO0O000o , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( I1IiI111I11 , I111i1i1111 ) )
   if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % I111I11 - iIii1I11I1II1 % O0
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as O0O0Ooo :
   O0O0Ooo . write ( '<item>\n<title>' + I111i1i1111 + '</title>\n<link>' + III1Ii1i1I1 + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 58 - 58: i1Ii + iIii1I11I1II1
  OOooO . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 65 - 65: O0Oo0oO0o - I111I11 % i11iI - O0I11i1i11i1I * oOo0 + I1iiiiI1iII
  if 79 - 79: ooiii11iII . O0I11i1i11i1I % I111I11 - i1iIii1Ii1II
  if 69 - 69: ooiii11iII - i11iI . ooiii11iII
  if 9 - 9: I1 % i11iIiiIii / i1iIii1Ii1II
def IIIiI1ii1IIi ( ) :
 o0O0oo0o = [ ]
 II11iI1iiI = sys . argv [ 2 ]
 if len ( II11iI1iiI ) >= 2 :
  I1ii = sys . argv [ 2 ]
  oO0o = I1ii . replace ( '?' , '' )
  if ( I1ii [ len ( I1ii ) - 1 ] == '/' ) :
   I1ii = I1ii [ 0 : len ( I1ii ) - 2 ]
  I1I1 = oO0o . split ( '&' )
  o0O0oo0o = { }
  for OoO in range ( len ( I1I1 ) ) :
   O0Oo0OOooO0OO0 = { }
   O0Oo0OOooO0OO0 = I1I1 [ OoO ] . split ( '=' )
   if ( len ( O0Oo0OOooO0OO0 ) ) == 2 :
    o0O0oo0o [ O0Oo0OOooO0OO0 [ 0 ] ] = O0Oo0OOooO0OO0 [ 1 ]
 return o0O0oo0o
 if 5 - 5: oOo0
I1ii = IIIiI1ii1IIi ( ) ; oo0OooOOo0 = None ; O0Oo000ooO00 = None ; OO = None ; iI1 = None ; oO0 = None ; I1iIII1IiiI = None
try : iI1 = urllib . unquote_plus ( I1ii [ "site" ] )
except : pass
try : oo0OooOOo0 = urllib . unquote_plus ( I1ii [ "url" ] )
except : pass
try : O0Oo000ooO00 = urllib . unquote_plus ( I1ii [ "name" ] )
except : pass
try : OO = int ( I1ii [ "mode" ] )
except : pass
try : oO0 = urllib . unquote_plus ( I1ii [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( I1ii [ "fanart" ] )
except : pass
try : I1iIII1IiiI = urllib . unquote_plus ( I1ii [ "description" ] )
except : pass
if 96 - 96: II1iI % i1IIi . i11iI . O0
if OO == None or oo0OooOOo0 == None or len ( oo0OooOOo0 ) < 1 : ii11i1 ( )
if 37 - 37: i1IIi - OOoOoo00oo % OoooooooOO / OOoOoo00oo % ooiii11iII
if 48 - 48: i11iIiiIii % I1
if 29 - 29: oOo0 + i11iIiiIii % iiI11
if 93 - 93: O0I11i1i11i1I % iIii1I11I1II1
if 90 - 90: II1iI - OOoOoo00oo / I1iiiiI1iII / O0 / iiI11
elif OO == 1 : iIIIIi1iiIi1 ( O0Oo000ooO00 , oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 2 : O0Oo0oOOoooOOOOo ( O0Oo000ooO00 , oo0OooOOo0 , oO0 )
elif OO == 3 : ooOOOo ( O0Oo000ooO00 , oo0OooOOo0 , oO0 )
if 87 - 87: O0I11i1i11i1I / i1Ii + iIii1I11I1II1
if 93 - 93: iIii1I11I1II1 + I1 % ooiii11iII
if 21 - 21: OOoOoo00oo
elif OO == 4 : III1Iiii1I11 ( oo0OooOOo0 )
elif OO == 5 : OOooOoooOoOo ( oo0OooOOo0 )
elif OO == 6 : iI1111iiii ( )
elif OO == 7 : iI1111ii1I ( oo0OooOOo0 )
elif OO == 8 : II11Ii1iI1iII ( oo0OooOOo0 )
elif OO == 9 : oo0o0OO0 ( oo0OooOOo0 )
elif OO == 10 : OOOoOO0o ( oo0OooOOo0 )
elif OO == 11 : ooo ( )
elif OO == 12 : ooO ( oo0OooOOo0 )
elif OO == 13 : iiIiIIIiiI ( oo0OooOOo0 )
elif OO == 14 : o0OoOo00o0o ( oo0OooOOo0 )
elif OO == 15 : O0oOo00o ( )
elif OO == 16 : OOO0o0OO0OO ( O0Oo000ooO00 , oo0OooOOo0 , oO0 )
elif OO == 17 : ii111iI1iIi1 ( oo0OooOOo0 )
elif OO == 18 : iI1i11iII111 ( oo0OooOOo0 )
elif OO == 19 : i1i ( oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 20 : I111iI ( )
elif OO == 21 : oooOo0OOOoo0 ( oo0OooOOo0 )
elif OO == 22 : I1III1111iIi ( oo0OooOOo0 )
elif OO == 23 : I1i11 ( )
elif OO == 24 : iiii1IIi ( oo0OooOOo0 )
elif OO == 25 : I11I1i1iIII1I ( oo0OooOOo0 , oO0 )
elif OO == 26 : iIIi ( oo0OooOOo0 )
elif OO == 27 : O0O0Oo00 ( oo0OooOOo0 , oO0 )
elif OO == 28 : iiIi1iI1iIii ( )
elif OO == 29 : Ii1I11ii1i ( oo0OooOOo0 )
elif OO == 30 : IIIi ( oo0OooOOo0 )
elif OO == 31 : OO0ooo0oOO ( oo0OooOOo0 )
elif OO == 32 : i1iiiii1 ( oo0OooOOo0 )
elif OO == 33 : IIii11I1i1I ( oo0OooOOo0 )
elif OO == 34 : I1ii11 ( oo0OooOOo0 )
elif OO == 35 : iIiIi11Ii ( )
elif OO == 36 : OooOOO0O00 ( oo0OooOOo0 )
elif OO == 37 : OOooOO00O0OO00oo ( oo0OooOOo0 , oO0 )
elif OO == 38 : oo0ooOO ( )
elif OO == 39 : oooooOOO000Oo ( oo0OooOOo0 )
elif OO == 40 : I111iI ( )
elif OO == 41 : oooOo0OOOoo0 ( oo0OooOOo0 )
elif OO == 42 : OOOooo0OooOoO ( oo0OooOOo0 )
elif OO == 43 : Ii ( oo0OooOOo0 , oO0 )
elif OO == 44 : iiIiI ( )
if 6 - 6: i1Ii
elif OO == 45 : OO00OO0O0 ( )
elif OO == 46 : oOooO0 ( oo0OooOOo0 )
elif OO == 47 : Ii1ii111i1 ( O0Oo000ooO00 , oo0OooOOo0 , oO0 )
elif OO == 48 : OoO00 ( )
elif OO == 49 : o00O00oO00 ( oo0OooOOo0 )
elif OO == 50 : I1IIIiI1I1ii1 ( oo0OooOOo0 )
elif OO == 51 : IiiiI ( oo0OooOOo0 )
elif OO == 52 : O0o0O0OO00o ( oo0OooOOo0 )
elif OO == 53 : oOOOo ( oo0OooOOo0 )
elif OO == 54 : I1i1111I ( oo0OooOOo0 , oO0 )
if 46 - 46: i1Ii + I1
if 79 - 79: OoooooooOO - i1Ii * i1Ii . O0I11i1i11i1I
if 100 - 100: O0Oo0oO0o * iiI11 % II1iI / Oo0o0ooO0oOOO
elif OO == 59 : IIi1ii1Ii ( )
elif OO == 60 : IiIIii1 ( oo0OooOOo0 )
elif OO == 61 : Oo00OoOo ( O0Oo000ooO00 , oo0OooOOo0 , oO0 )
if 90 - 90: Oo0o0ooO0oOOO . ooiii11iII . O0I11i1i11i1I . I1iiiiI1iII
elif OO == 66 : OoOIii11iI11i1I ( )
elif OO == 67 : iI11I ( oo0OooOOo0 )
elif OO == 68 : Ii1iI111 ( oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 69 : I1I ( oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 70 : iIi1i ( oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 71 : ii ( )
elif OO == 72 : ooOO00oOOo000 ( )
elif OO == 73 : O0O00OOo ( )
elif OO == 74 : IIi1I ( oo0OooOOo0 )
elif OO == 75 : Ooo0Oo0oo0 ( oo0OooOOo0 )
elif OO == 76 : IiIIi1IiiI1 ( )
elif OO == 77 : I11IIIiIi11 ( )
elif OO == 78 : OooO0oOo ( )
elif OO == 79 : Oo0ooo0Ooo ( )
elif OO == 80 : i1iiiIii11 ( oo0OooOOo0 )
elif OO == 81 : iIi ( oo0OooOOo0 , oO0 )
if 4 - 4: I1iiiiI1iII + O0I11i1i11i1I % Oo0o0ooO0oOOO / i11iIiiIii
if 74 - 74: O0Oo0oO0o . O0 - II1iI + i1Ii % i11iIiiIii % O0I11i1i11i1I
elif OO == 884 : II1i11i1iIi11 ( )
elif OO == 885 : o0o0O0Oo ( )
elif OO == 886 : I11IiIIIi ( )
elif OO == 887 : oo0 ( oo0OooOOo0 , oO0 , I1ii11iIi11i )
elif OO == 888 : ooo00Ooo ( )
elif OO == 889 : Oo0000o0O0O ( oo0OooOOo0 , OO , O0Oo000ooO00 , oO0 , I1ii11iIi11i )
elif OO == 890 : iiIIi ( )
elif OO == 891 : oOO0o0oo0 ( )
elif OO == 892 : OoOOOO ( )
if 78 - 78: I1iiiiI1iII + O0I11i1i11i1I + i1Ii - i1Ii . i11iIiiIii / OOo000
i1I1iI ( )
if OO == None or oo0OooOOo0 == None or len ( oo0OooOOo0 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 27 - 27: I1iiiiI1iII - O0 % iiI11 * I111I11 . i1Ii % iIii1I11I1II1
if 37 - 37: OoooooooOO + O0 - i1IIi % ooiii11iII
if 24 - 24: O0I11i1i11i1I
if 94 - 94: i1IIi * i1IIi % O0Oo0oO0o + OOoOoo00oo
if 28 - 28: II1iI
if 49 - 49: iiI11 . i11iI % I1 / I1iiiiI1iII
if 95 - 95: O0 * O0I11i1i11i1I * i1Ii . ooiii11iII / iIii1I11I1II1
if 28 - 28: i1Ii + I1 - ooiii11iII / iIii1I11I1II1 - II1iI
if 45 - 45: O0 / i1IIi * I1 * OOo000
if 35 - 35: Oo0o0ooO0oOOO / oOo0 % II1iI + iIii1I11I1II1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
