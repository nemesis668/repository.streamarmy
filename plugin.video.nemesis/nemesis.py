#########################################
############CODE BY @NEMZZY668###########
#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , uuid , os , re , sys , base64 , json , time , shutil , urlresolver , random , liveresolver , hashlib , datetime , smtplib
from resources . libs . modules import cfscrape
from resources . libs . common_addon import Addon
from metahandler import metahandlers
from HTMLParser import HTMLParser
from datetime import datetime
from resources . libs . modules import devilcheck
from resources . libs . modules import dom_parser2
from resources . libs . modules import regex
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.nemesis'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = base64 . b64decode ( b'aHR0cDovL3Bhc3RlYmluLmNvbS9yYXcvMEVWUWRLeXg=' )
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
if 80 - 80: i1iII1I1i1i1 . i1iIIII
if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
if 50 - 50: IiIi1Iii1I1 - i1iIIII
if 99 - 99: IiiIII111ii * O00OoOoo00 - oooOOOOO - i1IIi11111i
if 90 - 90: i11Ii11I1Ii1i + i1iII1I1i1i1 / i1IIi11111i % i11Ii11I1Ii1i - O0
if 29 - 29: i1IIi11111i / iIii1I11I1II1
if 24 - 24: O0 % i1IIi11111i + i1IIi + i1iIIi1 + o000o0o00o0Oo
if 70 - 70: ooo0Oo0 % ooo0Oo0 . IiiIII111ii % i1 * i1IIi11111i % i1iII1I1i1i1
if 23 - 23: i11iIiiIii + iiI1iIiI
if 68 - 68: Oooo0000 . i1iII1I1i1i1 . i11iIiiIii
if 40 - 40: i1iII1I1i1i1 . Oooo0000 . ooo0Oo0 . i1IIi
if 33 - 33: iiiI11 + i11Ii11I1Ii1i % i11iIiiIii . IiIi1Iii1I1 - iiI1iIiI
if 66 - 66: iiiI11 - OoooooooOO * OoooooooOO . i1iIIII . o000o0o00o0Oo
if 22 - 22: OoooooooOO % O00OoOoo00 - oooOOOOO . iIii1I11I1II1 * i11iIiiIii
if 32 - 32: ooo0Oo0 * O0 % i1iII1I1i1i1 % iiiI11 . IiiIII111ii
if 61 - 61: IiIi1Iii1I1
if 79 - 79: ooo0Oo0 + iiI1iIiI - oooOOOOO
if 83 - 83: IiIi1Iii1I1
def OO00o0OOO0 ( ) :
 if 27 - 27: O0 % i1IIi * i1iII1I1i1i1 + i11iIiiIii + OoooooooOO * i1IIi
 if 80 - 80: O00OoOoo00 * i11iIiiIii / i1iIIi1
 if not os . path . exists ( os . path . dirname ( o0OOO ) ) :
  try :
   os . makedirs ( os . path . dirname ( o0OOO ) )
   with open ( iI1Ii11111iIi , "w" ) as I11II1i :
    I11II1i . write ( "<date>000</date>" )
  except OSError as IIIII :
   if IIIII . errno != errno . EEXIST :
    raise
    if 75 - 75: i11Ii11I1Ii1i % i11Ii11I1Ii1i
def iI1 ( ) :
 if 19 - 19: O00OoOoo00 + IiIi1Iii1I1
 ooo = xbmc . getInfoLabel ( "System.BuildVersion" )
 ii1I1i1I = float ( ooo [ : 4 ] )
 if ii1I1i1I >= 11.0 and ii1I1i1I <= 11.9 :
  OOoo0O0 = 'Eden'
 elif ii1I1i1I >= 12.0 and ii1I1i1I <= 12.9 :
  OOoo0O0 = 'Frodo'
 elif ii1I1i1I >= 13.0 and ii1I1i1I <= 13.9 :
  OOoo0O0 = 'Gotham'
 elif ii1I1i1I >= 14.0 and ii1I1i1I <= 14.9 :
  OOoo0O0 = 'Helix'
 elif ii1I1i1I >= 15.0 and ii1I1i1I <= 15.9 :
  OOoo0O0 = 'Isengard'
 elif ii1I1i1I >= 16.0 and ii1I1i1I <= 16.9 :
  OOoo0O0 = 'Jarvis'
 elif ii1I1i1I >= 17.0 and ii1I1i1I <= 17.9 :
  OOoo0O0 = 'Krypton'
 else : OOoo0O0 = "Decline"
 if 41 - 41: i1iII1I1i1i1
 if OOoo0O0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif OOoo0O0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 6 - 6: o000o0o00o0Oo
def I1I ( ) :
 if 80 - 80: Oooo0000 - i1
 OOO00 = [ 'plugin.video.ghostshader' ]
 iiiiiIIii = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in OOO00 )
 O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.ghostshader' ) )
 if iiiiiIIii :
  import shutil
  Iii1ii1II11i . ok ( o0OoOoOO00 , "Sorry We Have Detected You Using An Addon That Steals Content From Us, Ghostshader is not supported by Nemesis and will be removed" )
  shutil . rmtree ( O000OO0 )
  os . _exit ( 1 )
 else :
  return
  if 43 - 43: i1iIIi1 - O0 % iiI1iIiI . O00OoOoo00
def o00 ( ) :
 if 95 - 95: O0 + i1 . i11Ii11I1Ii1i / O0
 OO00o0OOO0 ( )
 O000oo0O ( )
 I1I ( )
 OOOO = i1iII1IiiIiI1
 i11i1 = OOOO
 IIIii1II1II = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( IIIii1II1II >= 0000 ) and ( IIIii1II1II <= 1159 ) : i1I1iI = "Morning"
 elif ( IIIii1II1II >= 1200 ) and ( IIIii1II1II <= 1759 ) : i1I1iI = "Afternoon"
 else : i1I1iI = "Evening"
 oo0OooOOo0 ( '[COLOR yellow]Good[COLOR aqua] ' + str ( i1I1iI ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 oo0OooOOo0 ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  o0O = O00oO ( i1iII1IiiIiI1 )
  I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O )
  for oO0Oo in I11i1I1I :
   try :
    if '<m3u>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 11 , o00OO00OoO , I1ii11iIi11i )
    elif '<mamahdsports>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 14 , o00OO00OoO , I1ii11iIi11i )
    elif '<atc>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<atc>(.+?)</atc>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 6 , o00OO00OoO , I1ii11iIi11i )
    elif '<scanner>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 11 , o00OO00OoO , I1ii11iIi11i )
    elif '<cartoons>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 29 , o00OO00OoO , I1ii11iIi11i )
    elif '<Adult>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 38 , o00OO00OoO , I1ii11iIi11i )
    elif '<Anime>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 51 , o00OO00OoO , I1ii11iIi11i )
    elif '<audiobooks>' in oO0Oo :
     oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( oO0Oo ) [ 0 ]
     OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 59 , o00OO00OoO , I1ii11iIi11i )
    elif '<folder>' in oO0Oo :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     for oOOoo0Oo , OOOO , o00OO00OoO , I1ii11iIi11i in O0Oo000ooO00 :
      OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 1 , o00OO00OoO , I1ii11iIi11i )
    else :
     oO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
     if len ( oO0 ) == 1 :
      O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
      Ii1iIiII1ii1 = len ( I11i1I1I )
      for oOOoo0Oo , OOOO , o00OO00OoO , I1ii11iIi11i in O0Oo000ooO00 :
       if 'youtube.com/playlist' in OOOO :
        OOOO0OOoO0O0 ( oOOoo0Oo , OOOO , 2 , o00OO00OoO , I1ii11iIi11i )
       else :
        oo0OooOOo0 ( oOOoo0Oo , OOOO , 2 , o00OO00OoO , I1ii11iIi11i )
     elif len ( oO0 ) > 1 :
      oOOoo0Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
      o00OO00OoO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
      oo0OooOOo0 ( oOOoo0Oo , i11i1 , 3 , o00OO00OoO , I1ii11iIi11i )
   except : pass
   if 62 - 62: iIii1I11I1II1 * Oooo0000
  oo0OooOOo0 ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.urlresolver/settings.xml" )
   i1I1iI = open ( file ) . read ( )
   i1OOO = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( i1I1iI ) [ 0 ]
   i1OOO = i1OOO . strip ( )
   OOOO = 'plugin://script.module.urlresolver/?mode=auth_rd'
   if 'value=""' in i1OOO :
    Oo0oOOo = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    oo0OooOOo0 ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( Oo0oOOo ) + '[/COLOR]' , OOOO , 2 , I1IiI , Oo )
   else :
    Oo0oOOo = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    oo0OooOOo0 ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( Oo0oOOo ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  Oo0OoO00oOO0o = 'https://i.imgur.com/4Pzgdwu.png'
  OOOO0OOoO0O0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , Oo0OoO00oOO0o , Oo )
  OOO00O = 'https://i.imgur.com/Om0Lq7V.png'
  OOOO0OOoO0O0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , OOO00O , Oo )
  OOoOO0oo0ooO = 'https://i.imgur.com/klnhdFx.png'
  OOOO0OOoO0O0 ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , OOoOO0oo0ooO , Oo )
 except :
  O0o0O00Oo0o0 = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if O0o0O00Oo0o0 == 0 :
   oo0OooOOo0 ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   OOOO0OOoO0O0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if O0o0O00Oo0o0 == 1 :
   quit ( )
   if 87 - 87: IiIi1Iii1I1 * ooo0Oo0 % i11iIiiIii % Oooo0000 - i1iIIII
 iI1 ( )
 if 68 - 68: i1iIIi1 % i1IIi . IiiIII111ii . o000o0o00o0Oo
def o0 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i11i1 = url
 o0O = O00oO ( url )
 I1I ( )
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O )
 for oO0Oo in I11i1I1I :
  try :
   if '<image>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 23 , iconimage , fanart )
   elif '<American>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 73 , iconimage , fanart )
   elif '<lordjd>' in oO0Oo :
    oO0 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( oO0Oo )
    if len ( oO0 ) == 1 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     Ii1iIiII1ii1 = len ( I11i1I1I )
     for name , url , iconimage , fanart in O0Oo000ooO00 :
      if 'youtube.com/playlist' in url :
       OOOO0OOoO0O0 ( name , url , 2 , iconimage , fanart )
      else :
       oo0oOo ( name , url , 2 , iconimage , fanart )
    elif len ( oO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo ( name , i11i1 , 3 , iconimage , fanart )
   elif '<reddit>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( oO0Oo ) [ 0 ]
    OOOO0OOoO0O0 ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in oO0Oo :
    oO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( oO0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     o000O0o = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     iI1iII1 = o000O0o
     oO0OOoo0OO = "/"
     if not iI1iII1 . endswith ( oO0OOoo0OO ) :
      O0ii1ii1ii = iI1iII1 + "/"
     else :
      O0ii1ii1ii = iI1iII1
     o0O = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O + '%26referer=' + O0ii1ii1ii
     oo0OooOOo0 ( name , url , 10 , iconimage , fanart )
    elif len ( oO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oo0OooOOo0 ( name , i11i1 , 16 , iconimage , fanart )
     if 91 - 91: IiiIII111ii
   elif '<folder>' in oO0Oo :
    O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in O0Oo000ooO00 :
     OOOO0OOoO0O0 ( name , url , 1 , iconimage , fanart )
     if 15 - 15: i11Ii11I1Ii1i
   else :
    oO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( oO0 ) == 1 :
     O0Oo000ooO00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     Ii1iIiII1ii1 = len ( I11i1I1I )
     for name , url , iconimage , fanart in O0Oo000ooO00 :
      if 'youtube.com/playlist' in url :
       OOOO0OOoO0O0 ( name , url , 2 , iconimage , fanart )
      else :
       oo0OooOOo0 ( name , url , 2 , iconimage , fanart )
    elif len ( oO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oo0OooOOo0 ( name , i11i1 , 3 , iconimage , fanart )
  except : pass
  if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 iI1 ( )
 if 75 - 75: Oooo0000 % i1IIi11111i % i1IIi11111i . i1iIIi1
 if 5 - 5: i1IIi11111i * IiIi1Iii1I1 + Oooo0000 . i1iIIII + Oooo0000
 if 91 - 91: O0
 if 61 - 61: i11Ii11I1Ii1i
 if 64 - 64: IiIi1Iii1I1 / Oooo0000 - O0 - O00OoOoo00
 if 86 - 86: O00OoOoo00 % Oooo0000 / iiI1iIiI / Oooo0000
 if 42 - 42: i1
 if 67 - 67: i1iIIi1 . oooOOOOO . O0
def IIIIiiII111 ( url ) :
 if 97 - 97: o000o0o00o0Oo + i1iIIII / iIii1I11I1II1 / oooOOOOO
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  try :
   I1111IIi = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   OOOO0OOoO0O0 ( "[COLOR skyblue]" + I1111IIi + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 93 - 93: OoooooooOO / iiI1iIiI % i11iIiiIii + o000o0o00o0Oo * i1
def I1 ( url ) :
 if 22 - 22: ooo0Oo0 + iiiI11 % o000o0o00o0Oo
 iI1IIi1iIi = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 ooOOoooooo = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 oo0OooOOo0 ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 o0O = O00oO ( url )
 oO0 = 0
 II1I = re . compile ( 'href="([^"]+)' ) . findall ( o0O )
 for url in II1I :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in iI1IIi1iIi ) :
    oO0 += 1
    I1111IIi = "Link " + str ( oO0 ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    O0i1II1Iiii1I11 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     oo0OooOOo0 ( "[COLOR skyblue]" + I1111IIi + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in ooOOoooooo ) :
     oo0OooOOo0 ( "[COLOR yellow]" + I1111IIi + url + "[/COLOR]" , O0i1II1Iiii1I11 , 2 , I1IiI , I1ii11iIi11i )
    else :
     oo0OooOOo0 ( "[COLOR skyblue]" + I1111IIi + url + "[/COLOR]" , O0i1II1Iiii1I11 , 2 , I1IiI , I1ii11iIi11i )
     if 9 - 9: o000o0o00o0Oo / ooo0Oo0 - iiI1iIiI / OoooooooOO / iIii1I11I1II1 - i1IIi11111i
     if 91 - 91: oooOOOOO % i1IIi % iIii1I11I1II1
     if 20 - 20: i1iIIII % iiiI11 / iiiI11 + iiiI11
def III1IiiI ( url ) :
 if 31 - 31: i1IIi11111i . iiI1iIiI
 if url == 'Football' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  ii11IIII11I = O00oO ( 'http://wizhdsports.is/sport/Cricket' )
 OOooo = dom_parser2 . parse_dom ( ii11IIII11I , 'div' , { 'class' : 'card' } )
 OOooo = [ ( dom_parser2 . parse_dom ( oOooOOOoOo , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( oOooOOOoOo , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( oOooOOOoOo , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( oOooOOOoOo , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for oOooOOOoOo in OOooo ]
 if len ( OOooo ) < 1 :
  oo0OooOOo0 ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , o00OO00OoO , Oo , '' )
 OOooo = [ ( oOooOOOoOo [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , oOooOOOoOo [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , oOooOOOoOo [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , oOooOOOoOo [ 2 ] [ 0 ] . content ) if oOooOOOoOo [ 2 ] else 'Upcoming' , oOooOOOoOo [ 3 ] [ 0 ] . content ) for oOooOOOoOo in OOooo ]
 if 41 - 41: iiiI11 - O0 - O0
 if 68 - 68: i1iIIII % i1iIIi1
 if 88 - 88: iIii1I11I1II1 - IiIi1Iii1I1 + i1iIIII
 if 40 - 40: iiI1iIiI * iiiI11 + i1iIIII % oooOOOOO
 OOooo = [ ( oOooOOOoOo [ 0 ] , oOooOOOoOo [ 1 ] , oOooOOOoOo [ 2 ] , oOooOOOoOo [ 3 ] , oOooOOOoOo [ 4 ] ) for oOooOOOoOo in OOooo ]
 OOOOOoo0 = 0
 ii1 = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for oOooOOOoOo in OOooo :
  I1iI1iIi111i = oOooOOOoOo [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( OOOOOoo0 ) )
  OOOOOoo0 += 1
  time . sleep ( 0.10 )
  I1iI1iIi111i = iiIi1IIi1I ( I1iI1iIi111i )
  o0OoOO000ooO0 = oOooOOOoOo [ 1 ]
  o0o0o0oO0oOO = oOooOOOoOo [ 3 ]
  if 'Match Over' in o0o0o0oO0oOO :
   ii1 += 1
  ii1Ii11I = dom_parser2 . parse_dom ( oOooOOOoOo [ 4 ] , 'a' )
  for ii11IIII11I in ii1Ii11I :
   o00o0 = re . sub ( '<.+?>' , '' , ii11IIII11I . content )
   o0O = ii11IIII11I . attrs [ 'href' ]
   o0O = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + o0O
   if not 'Match Over' in o0o0o0oO0oOO :
    oo0OooOOo0 ( '[COLOR aqua]' + I1iI1iIi111i + '[COLOR yellow]' + ' ' + o0o0o0oO0oOO + '[/COLOR]' , o0O , 2 , o00OO00OoO , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( OOOOOoo0 ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( ii1 ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 45 - 45: O0
def I1IiiiiI ( url ) :
 if 80 - 80: i1iIIi1 . i11iIiiIii - i1IIi11111i
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = re . compile ( 'title="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  if 25 - 25: i1
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 62 - 62: i1iIIII + O0
 try :
  oO0OOOO0 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( o0O ) [ 0 ]
  I1IiI = o00OO00OoO
  OOOO0OOoO0O0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , oO0OOOO0 , 18 , o00OO00OoO , Oo , '' )
 except : pass
 if 26 - 26: iiiI11
def I11iiI1i1 ( url , iconimage , fanart ) :
 if 47 - 47: oooOOOOO - iiiI11 . i11Ii11I1Ii1i + OoooooooOO . i11iIiiIii
 oo0OooOOo0 ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( o0O )
 if 94 - 94: i1IIi11111i * iiiI11 / ooo0Oo0 / iiiI11
 for oO0 in I11i1I1I :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0 ) [ 0 ]
  O0i1II1Iiii1I11 = str . lower ( url )
  if '1e' in O0i1II1Iiii1I11 :
   I1111IIi = '1st Half'
  else :
   I1111IIi = '2nd Half'
  oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 87 - 87: ooo0Oo0 . IiiIII111ii
def O0OO0O ( ) :
 if 81 - 81: i1iII1I1i1i1 . i1IIi11111i % O0 / iiI1iIiI - i1iII1I1i1i1
 OOOO = 'http://www.goalsarena.org/en/'
 o0O = O00oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for OO , I1iI1ii1II in Ii1I1i :
  OOOO0OOoO0O0 ( "[COLOR skyblue]" + I1iI1ii1II + "[/COLOR]" , OO , 21 , I1IiI , Oo , '' )
  if 57 - 57: i1iIIi1 % iiiI11 + i1IIi11111i - ooo0Oo0
def o0OIiI1i ( url ) :
 if 92 - 92: IiiIII111ii . IiiIII111ii + i1
 if 9 - 9: iiI1iIiI * O0 + IiiIII111ii - O00OoOoo00 * i1iIIi1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0o0O00Oo0o0 = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if O0o0O00Oo0o0 == 0 :
  try :
   I11i1I1I = re . compile ( '<iframe src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in I11i1I1I :
   Oooo0oOO ( oOOoo0Oo , I11i1I1I , o00OO00OoO )
  Ooo00O00o = O00oO ( I11i1I1I )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ooo00O00o ) [ 0 ]
  url = 'https:' + url
  O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = o00OO00OoO , thumbnailImage = o00OO00OoO )
  xbmc . Player ( ) . play ( url , O0O00Oo , False )
  quit ( 0 )
 if O0o0O00Oo0o0 == 1 :
  try :
   I11i1I1I = re . compile ( '<iframe src="(.+?)"' ) . findall ( o0O ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   o0OIiI1i ( url )
  Ooo00O00o = O00oO ( I11i1I1I )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ooo00O00o ) [ 0 ]
  url = 'https:' + url
  O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = o00OO00OoO , thumbnailImage = o00OO00OoO )
  xbmc . Player ( ) . play ( url , O0O00Oo , False )
  quit ( 0 )
  if 97 - 97: O0 * OoooooooOO . OoooooooOO
def I111iI ( ) :
 if 56 - 56: iiI1iIiI
 OOOO = 'http://m.liveatc.net/feeds/'
 o0O = O0oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  OOOO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://m.liveatc.net' + OOOO
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , OOOO , 7 , I1IiI , Oo , '' )
  if 73 - 73: o000o0o00o0Oo * i11iIiiIii % i1iII1I1i1i1 . o000o0o00o0Oo
def OOOOo0 ( url ) :
 if 49 - 49: i11Ii11I1Ii1i % O0 . Oooo0000 + i1iII1I1i1i1 / iiI1iIiI
 if 72 - 72: IiIi1Iii1I1 * ooo0Oo0 . iiI1iIiI - i11Ii11I1Ii1i + i1IIi
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 10 - 10: i1iII1I1i1i1 + i1IIi
def oOo0O ( url ) :
 url = url . replace ( ' ' , '%20' )
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li>(.+?)</a>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '(.+?)</li>' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 52 - 52: i11iIiiIii / i1IIi11111i * IiIi1Iii1I1
def iI ( url ) :
 if 89 - 89: i1IIi11111i + i1 * O00OoOoo00 * iiiI11
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  try :
   I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
   oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   oo0OooOOo0 ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 37 - 37: OoooooooOO - O0 - i1IIi11111i
def o0o0O0O00oOOo ( ) :
 if 14 - 14: Oooo0000 + i1iII1I1i1i1
 OOOO0OOoO0O0 ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 OOOO = 'http://m.broadcastify.com/?a=la&coid=1'
 o0O = O0oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  OOOO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://m.broadcastify.com' + OOOO
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , OOOO , 12 , I1IiI , Oo , '' )
  if 52 - 52: OoooooooOO - IiIi1Iii1I1
def o0O0o0 ( url ) :
 if 37 - 37: o000o0o00o0Oo * O00OoOoo00 % i11iIiiIii % IiIi1Iii1I1 + iiiI11
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 78 - 78: o000o0o00o0Oo % i1iII1I1i1i1 / oooOOOOO - iIii1I11I1II1
def ooooo0O0000oo ( url ) :
 if 21 - 21: i1IIi11111i - iiI1iIiI
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 18 - 18: ooo0Oo0 + O00OoOoo00 % i1iIIII - OoooooooOO - o000o0o00o0Oo / i1IIi
def oo0oO ( url ) :
 if 94 - 94: iIii1I11I1II1 / ooo0Oo0 % oooOOOOO * oooOOOOO * i11Ii11I1Ii1i
 o0O = O0oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  I11i1I1I = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( o0O ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 IIiIiI ( I11i1I1I )
 if 94 - 94: i1iII1I1i1i1 . i1IIi - i1IIi11111i % O0 - i1
def ooO0O00Oo0o ( ) :
 if 65 - 65: o000o0o00o0Oo . O00OoOoo00 - i1iIIi1 * IiiIII111ii / i1iIIi1 / IiIi1Iii1I1
 OOOO = 'http://m.broadcastify.com/?a=top25'
 o0O = O0oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  i111iIi1i1II1 = I1111IIi . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  I1111IIi = I1111IIi . split ( ')' ) [ - 1 ] . strip ( )
  OOOO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://m.broadcastify.com' + OOOO
  oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[COLOR yellow] :: " + i111iIi1i1II1 + " Listening" + "[/COLOR]" , OOOO , 14 , I1IiI , Oo , '' )
  if 86 - 86: iIii1I11I1II1 / Oooo0000 . i11Ii11I1Ii1i
def II1i111Ii1i ( url ) :
 if 15 - 15: i11Ii11I1Ii1i / i1IIi
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( oO0 ) [ 0 ]
  I1111IIi = O0oO0 ( I1111IIi )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0 ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0 ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in I1111IIi :
    O0i1II1Iiii1I11 = 'https://www.youtube.com' + url
    oo0OooOOo0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , O0i1II1Iiii1I11 , 2 , I1IiI , I1ii11iIi11i )
    if 7 - 7: iiI1iIiI
def I1ii1iIiii1I ( ) :
 if 42 - 42: i1IIi11111i + i1IIi - iiiI11 / IiiIII111ii
 OOOO = 'http://burningwhee1s.blogspot.co.uk/'
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( I11i1I1I )
 for o0O , I1111IIi in Ii1I1i :
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , o0O , 24 , I1IiI , Oo , '' )
  if 9 - 9: O0 % O0 - i1IIi11111i
def OoO ( url ) :
 if 12 - 12: O0 - i1IIi11111i
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( oO0 ) [ 0 ]
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 81 - 81: Oooo0000 - Oooo0000 . oooOOOOO
def o0OoOo00o0o ( url , iconimage ) :
 if 41 - 41: IiIi1Iii1I1 % i1 - ooo0Oo0 * i1iIIi1 * ooo0Oo0
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( I11i1I1I )
 try :
  for oO0 in Ii1I1i :
   I1111IIi = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0 ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    OOOoOO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0 ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     OOOoOO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0 ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     OOOoOO0o = ''
   I1111IIi = O0oO0 ( I1111IIi )
   OOOoOO0o = O0oO0 ( OOOoOO0o )
   i1II1 = re . compile ( '<option value="(.+?)"' ) . findall ( oO0 ) [ 1 ]
   oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "  " + OOOoOO0o + "[/COLOR]" , i1II1 , 2 , I1IiI , Oo , '' )
 except :
  oo0OooOOo0 ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 25 - 25: i1iIIi1 / iIii1I11I1II1 % oooOOOOO
def IiiiiI1i1Iii ( ) :
 if 87 - 87: i1IIi11111i
 if 29 - 29: iiI1iIiI % i1iIIII - iiI1iIiI / i1iIIII . i1IIi
 OOOO = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 o0O = O00oO ( OOOO )
 O0Oo000ooO00 = json . loads ( o0O )
 i11III1111iIi = O0Oo000ooO00 [ 'results' ]
 for I1i111I in i11III1111iIi :
  Ooo = 'https://image.tmdb.org/t/p/w640'
  I1111IIi = I1i111I [ 'title' ]
  I1IiI = I1i111I [ 'poster_path' ]
  Oo0oo0O0o00O = I1i111I [ 'id' ]
  I1IiI = Ooo + I1IiI
  I1ii11iIi11i = I1i111I [ 'backdrop_path' ]
  I1ii11iIi11i = Ooo + I1ii11iIi11i
  I1i11 = I1i111I [ 'overview' ]
  Oo0oo0O0o00O = str ( Oo0oo0O0o00O )
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , I1111IIi , 33 , I1IiI , I1ii11iIi11i , I1i11 )
  if 12 - 12: i1IIi + i1IIi - o000o0o00o0Oo * ooo0Oo0 % ooo0Oo0 - i11Ii11I1Ii1i
def o0OOOOooo ( url ) :
 if 94 - 94: OoooooooOO + ooo0Oo0 / Oooo0000 * i1iIIII
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = re . compile ( '<i>(.+?)</i>' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = I1111IIi . strip ( )
  OOOO0OOoO0O0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( o0O ) [ 0 ]
  o0OO0o0oOOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  OOOO0OOoO0O0 ( '[COLOR yellow]Next Page >>[/COLOR]' , o0OOo0o0O0O , 26 , o0OO0o0oOOO0O , I1ii11iIi11i )
 except : pass
 if 49 - 49: o000o0o00o0Oo . i1IIi11111i . i11Ii11I1Ii1i
def o000ooooO0o ( url , iconimage ) :
 if 40 - 40: o000o0o00o0Oo + i1IIi * i1iIIII
 o0O = O00oO ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( o0O ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 I11i1I1I = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( o0O )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 oOooOOOoOo = 1
 O0oOOoooOO0O = [ ]
 for oO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  O0oOOoooOO0O . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( oOooOOOoOo ) )
  time . sleep ( 0.02 )
  oOooOOOoOo += 1
  I1111IIi = re . compile ( '(.+?)</p>' ) . findall ( oO0 ) [ 0 ] . replace ( 'Server' , '' )
  I1111IIi = I1111IIi . strip ( )
 ooo00Ooo = 1
 i1I1iI = 0
 Oo0o0O00 = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 40 - 40: OoooooooOO
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if i1I1iI > len ( O0oOOoooOO0O ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 25 - 25: IiiIII111ii + iiiI11 / IiIi1Iii1I1 . i1IIi11111i % O0 * i1
  if Oo0o0O00 == 0 :
   i1I1iI += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( i1I1iI ) + "[/COLOR]" , '' )
   try :
    o0O = O00oO ( O0oOOoooOO0O [ i1I1iI ] )
    Ii1I1i = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( o0O ) [ 0 ]
    o0O0oo0OO0O = base64 . b64decode ( Ii1I1i )
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O0oo0OO0O ) [ 0 ]
    OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    o0Oooo = open ( OO0 ) . read ( )
    iiI = re . compile ( '<url>(.+?)</url>' ) . findall ( o0Oooo )
    for oO in iiI :
     IIiIi = re . compile ( '<bad>(.+?)<bad>' ) . findall ( oO ) [ 0 ]
     if url == IIiIi :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( i1I1iI ) )
      time . sleep ( 0.5 )
      Oo0o0O00 = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     OOoOooOoOOOoo = liveresolver . resolve ( url )
    else : OOoOooOoOOOoo = url
    O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( OOoOooOoOOOoo , O0O00Oo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( i1I1iI ) )
    time . sleep ( 0.5 )
    Oo0o0O00 = 5
    pass
  if Oo0o0O00 == 5 :
   Oo0o0O00 = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   Oo0o0O00 += 1
   if 25 - 25: OoooooooOO - iiI1iIiI . iiI1iIiI * i1iII1I1i1i1
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 iI1iII1 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if iI1iII1 :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( OO0 , "a" ) as o000oo :
   o000oo . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 95 - 95: IiIi1Iii1I1 / IiIi1Iii1I1
def IIiI1Ii ( url ) :
 if 57 - 57: i1iIIII - IiIi1Iii1I1 - O00OoOoo00 + i1
 if 30 - 30: iiiI11 % Oooo0000 + i1IIi - O00OoOoo00 - iiiI11
 if url == 'search' :
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Search Term' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1 . lower ( )
    if 52 - 52: o000o0o00o0Oo - ooo0Oo0 + o000o0o00o0Oo % i1IIi11111i
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o00OO00OoO , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o00OO00OoO , 5000 )
   quit ( )
  O00Ooo = O00Ooo . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + O00Ooo + '.html'
  iI1IiI ( url , I1IiI )
  if 21 - 21: i1 + iiI1iIiI % iiI1iIiI
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  iI1IiI ( url , I1IiI )
  if 82 - 82: oooOOOOO
def iI1IiI ( url , icon ) :
 if 65 - 65: IiIi1Iii1I1 . OoooooooOO / o000o0o00o0Oo . i1IIi * i1
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = re . compile ( '<i>(.+?)</i>' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = O0oO0 ( I1111IIi )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO0OOoO0O0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 19 - 19: i11iIiiIii + OoooooooOO - ooo0Oo0 - O00OoOoo00
def Iii1iiIi1II ( ) :
 if 60 - 60: iiI1iIiI - i1iII1I1i1i1 * O00OoOoo00 % i11Ii11I1Ii1i
 OOOO = 'http://www.genti.stream/'
 o0O = O00oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  oooIIiIiI1I = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0 ) [ 0 ] . strip ( )
  OooOoOo = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0 ) [ 1 ] . strip ( )
  OOOO = re . compile ( 'href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://www.genti.stream/' + OOOO
  oo0OooOOo0 ( "[COLOR aqua]" + oooIIiIiI1I + "[COLOR yellow] vs [COLOR aqua]" + OooOoOo + "[/COLOR]" , OOOO , 39 , I1IiI , I1ii11iIi11i )
  if 14 - 14: i1IIi11111i * i1iIIII + oooOOOOO + O0 + i11iIiiIii
def oOoO0 ( url ) :
 if 77 - 77: iIii1I11I1II1 . oooOOOOO % oooOOOOO + i11iIiiIii
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo00o0OO0O00o = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( o0O ) [ 0 ]
 if not 'http' in Oo00o0OO0O00o :
  Oo00o0OO0O00o = 'http://www.genti.stream' + Oo00o0OO0O00o
 OO = O00oO ( Oo00o0OO0O00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0Oooo = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OO ) [ 0 ]
 Ooo00O00o = O00oO ( O0Oooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( Ooo00O00o ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( Ooo00O00o ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( Ooo00O00o ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( Ooo00O00o ) [ 0 ]
 except : pass
 if 21 - 21: ooo0Oo0
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , o00OO00OoO , 5000 )
  quit ( )
 Oooo0oOO ( oOOoo0Oo , url , o00OO00OoO )
 if 29 - 29: O00OoOoo00 / i11Ii11I1Ii1i / IiIi1Iii1I1 * i1iIIII
 if 10 - 10: i1iIIi1 % IiiIII111ii * IiiIII111ii . O00OoOoo00 / iiiI11 % i1iIIII
def IIII1 ( url ) :
 if 10 - 10: i1iIIi1 / IiIi1Iii1I1 + i11iIiiIii / iiiI11
 OOOoOoO = cfscrape . create_scraper ( )
 i11i1 = OOOoOoO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( i11i1 ) [ 0 ]
 Ii1I1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for url , I1111IIi in Ii1I1i :
  url = 'http://kimcartoon.me/CartoonList' + url
  OOOO0OOoO0O0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 22 - 22: iiI1iIiI % o000o0o00o0Oo
def o0oo0O ( url ) :
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - i11Ii11I1Ii1i * i1iIIII
 OOOoOoO = cfscrape . create_scraper ( )
 i11i1 = OOOoOoO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( i11i1 )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   iiIi1iI1iIii = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( oO0 ) [ 0 ]
   iiIi1iI1iIii = O0oO0 ( iiIi1iI1iIii )
  except IndexError :
   iiIi1iI1iIii = ''
  OOOO0OOoO0O0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , iiIi1iI1iIii )
  if 68 - 68: i1iIIII
 try :
  OooO0oo = re . compile ( '<li>(.+?)Next' ) . findall ( i11i1 )
  for oO0 in OooO0oo :
   o0OOo0o0O0O = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ - 1 ]
   o0o0oOoOO0O = 'http://kimcartoon.me' + o0OOo0o0O0O
   i1ii1II1ii = 'https://i.imgur.com/mjCRjXT.png'
   OOOO0OOoO0O0 ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , o0o0oOoOO0O , 30 , i1ii1II1ii , I1ii11iIi11i )
 except : pass
 if 28 - 28: o000o0o00o0Oo
def O00OoOO0oo0 ( url ) :
 if 96 - 96: Oooo0000 . i1IIi11111i - IiIi1Iii1I1
 OOOoOoO = cfscrape . create_scraper ( )
 i11i1 = OOOoOoO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<td>(.+?)</td>' ) . findall ( i11i1 )
 for oO0 in I11i1I1I :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
   I1111IIi = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   oo0OooOOo0 ( "[COLOR aqua][B]" + I1111IIi + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 99 - 99: IiiIII111ii . ooo0Oo0 - iiiI11 % iiiI11 * O0 . i11Ii11I1Ii1i
def iIIII1iIIii ( url ) :
 if 52 - 52: i1IIi11111i % ooo0Oo0
 O0o0O00Oo0o0 = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if O0o0O00Oo0o0 == 0 :
  url = url + '&s=rapidvideo'
  OOOoOoO = cfscrape . create_scraper ( )
  i11i1 = OOOoOoO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   Ii1I1i = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i11i1 )
   for o0O in Ii1I1i :
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O ) [ 0 ]
    if 'rapidvideo' in url :
     Oooo0oOO ( oOOoo0Oo , url , o00OO00OoO )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if O0o0O00Oo0o0 == 1 :
  url = url + '&s=openload'
  OOOoOoO = cfscrape . create_scraper ( )
  i11i1 = OOOoOoO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   Ii1I1i = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i11i1 )
   for o0O in Ii1I1i :
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O ) [ 0 ]
    Oooo0oOO ( oOOoo0Oo , url , o00OO00OoO )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 64 - 64: O0 % O00OoOoo00 % O0 * i1 . i1iII1I1i1i1 + iiI1iIiI
   if 75 - 75: O00OoOoo00 . OoooooooOO % i1IIi11111i * O00OoOoo00 % OoooooooOO
def I11i1 ( ) :
 if 28 - 28: O00OoOoo00
 OOOO = "http://www.loyalbooks.com/genre-menu"
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( o0O )
 for oO0Oo in I11i1I1I :
  if "paid" not in oO0Oo :
   OO = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   Ooo00O00o = "http://www.loyalbooks.com" + OO
   oOOoo0Oo = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   OOOO0OOoO0O0 ( "[COLOR aqua]" + oOOoo0Oo + "[/COLOR]" , Ooo00O00o , 60 , I1IiI , Oo , '' )
   if 58 - 58: Oooo0000
def iIiiI1iI ( url ) :
 if 5 - 5: Oooo0000 / OoooooooOO + IiiIII111ii * i1iIIi1 - i1 % iiI1iIiI
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( o0O ) [ 0 ]
 IiII1 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( I11i1I1I )
 for oO0Oo in IiII1 :
  O0i1II1Iiii1I11 = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  Ooo00O00o = "http://www.loyalbooks.com" + O0i1II1Iiii1I11
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  o00OO00OoO = "http://www.loyalbooks.com" + I1IiI
  oOOoo0Oo = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  OOOO0OOoO0O0 ( "[COLOR aqua]" + oOOoo0Oo + "[/COLOR]" , Ooo00O00o , 61 , o00OO00OoO , Oo , '' )
 try :
  o0O = O00oO ( url )
  oO0OOOO0 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( o0O ) [ 0 ]
  I1IiI = 'https://i.imgur.com/mjCRjXT.png'
  OOOO0OOoO0O0 ( "[COLOR yellow]Next Page -->[/COLOR]" , oO0OOOO0 , 60 , I1IiI , Oo , '' )
 except : pass
 if 18 - 18: IiIi1Iii1I1 * Oooo0000 . oooOOOOO / o000o0o00o0Oo / i11iIiiIii
 if 21 - 21: i1iII1I1i1i1 / o000o0o00o0Oo + iiiI11 + OoooooooOO
def OoOo ( name , url , iconimage ) :
 if 35 - 35: IiIi1Iii1I1 * i1iIIII . O00OoOoo00 * i1IIi11111i . Oooo0000 / O0
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( o0O )
 for oO0Oo in I11i1I1I :
  I1111IIi = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  O0i1II1Iiii1I11 = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , O0i1II1Iiii1I11 , 10 , iconimage , Oo , '' )
  if 100 - 100: i1iIIi1 . i1IIi11111i * ooo0Oo0 % O0 * O0
def II ( ) :
 if 44 - 44: i11Ii11I1Ii1i / oooOOOOO / O00OoOoo00 % i11Ii11I1Ii1i / i1IIi . iiiI11
 OOOO = 'http://www.shadownet.me/'
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for OOOO , I1111IIi in Ii1I1i :
  I1111IIi = O0oO0 ( I1111IIi )
  if 'P2P' not in I1111IIi :
   OOOO0OOoO0O0 ( "[COLOR skyblue]" + I1111IIi + "[/COLOR]" , OOOO , 49 , I1IiI , Oo , '' )
   if 59 - 59: OoooooooOO
   if 47 - 47: IiIi1Iii1I1 - iiI1iIiI / i11Ii11I1Ii1i
def i11i1iiiII ( url ) :
 if 68 - 68: i11iIiiIii * i1
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( I11i1I1I )
 for oO0 in Ii1I1i :
  I1111IIi = re . compile ( 'alt="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  oo0OooOOo0 ( "[COLOR skyblue]" + I1111IIi + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( o0O ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  OOOO0OOoO0O0 ( "[COLOR orange]Next Page --->[/COLOR]" , o0OOo0o0O0O , 49 , I1IiI , Oo , '' )
 except : pass
 if 46 - 46: Oooo0000 / iIii1I11I1II1 % oooOOOOO . iIii1I11I1II1 * oooOOOOO
def IIi1ii1Ii ( url ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + oooOOOOO - i11iIiiIii + i1iIIII
 def ii1i ( url ) :
  oOOoo = urllib2 . Request ( url )
  oOOoo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  oOOoo . add_header ( 'Referer' , url )
  iII1111III1I = urllib2 . urlopen ( oOOoo , timeout = 5 )
  o0O = iII1111III1I . read ( )
  iII1111III1I . close ( )
  return o0O
  if 39 - 39: i1IIi / IiiIII111ii
 o0O = ii1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I11i1I1I = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( o0O ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in I11i1I1I :
  url = I11i1I1I
  Oooo0oOO ( oOOoo0Oo , url , o00OO00OoO )
 Ooo00O00o = ii1i ( I11i1I1I )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( Ooo00O00o ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 78 - 78: IiIi1Iii1I1
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = o00OO00OoO , thumbnailImage = o00OO00OoO )
  O0O00Oo . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , O0O00Oo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = o00OO00OoO , thumbnailImage = o00OO00OoO )
  O0O00Oo . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , O0O00Oo , False )
 else :
  if '.m3u8' in url :
   O0i1II1Iiii1I11 = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + oOOoo0Oo + '&amp;url=' + url + '&amp;iconImage=' + o00OO00OoO
  elif '.ts' in url :
   O0i1II1Iiii1I11 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + oOOoo0Oo + '&amp;url=' + url + '&amp;iconImage=' + o00OO00OoO
  else :
   O0i1II1Iiii1I11 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 53 - 53: IiIi1Iii1I1 * i1iIIII . oooOOOOO / O0 * IiIi1Iii1I1
  O0O00Oo = xbmcgui . ListItem ( oOOoo0Oo , iconImage = o00OO00OoO , thumbnailImage = o00OO00OoO )
  O0O00Oo . setPath ( url )
  if 22 - 22: ooo0Oo0 % oooOOOOO * o000o0o00o0Oo / i1iIIII % i11iIiiIii * O00OoOoo00
  xbmc . Player ( ) . play ( O0i1II1Iiii1I11 , O0O00Oo , False )
  if 95 - 95: OoooooooOO - IiiIII111ii * iiI1iIiI + Oooo0000
  if 10 - 10: i1IIi11111i / i11iIiiIii
def o00oO ( ) :
 if 92 - 92: IiiIII111ii * ooo0Oo0 * ooo0Oo0 * iiI1iIiI . iIii1I11I1II1
 OOOO = 'https://m.skylinewebcams.com/en/webcam'
 o0O = O00oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Ii1I1i = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
 I1Ii1111iIi = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Ii1I1i )
 for OOOO , I1111IIi in I1Ii1111iIi :
  if 'http|https' not in OOOO :
   OOOO = 'https://m.skylinewebcams.com' + OOOO
   OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , OOOO , 46 , I1IiI , Oo , '' )
   if 31 - 31: O00OoOoo00 . i1iIIi1 * IiIi1Iii1I1 + i11iIiiIii * i1iII1I1i1i1
def OO0o ( url ) :
 if 75 - 75: OoooooooOO * IiiIII111ii
 o0O = O00oO ( url )
 Ii1I1i = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( o0O )
 for url , I1IiI , I1111IIi in Ii1I1i :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 9 - 9: IiiIII111ii - i11Ii11I1Ii1i + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: IiiIII111ii * ooo0Oo0 + iIii1I11I1II1 - IiiIII111ii + i1iIIII
def o0iiiI1I1iIIIi1 ( name , url , iconimage ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / O00OoOoo00 % i11Ii11I1Ii1i % i1IIi / i11iIiiIii
 o0O = O00oO ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  I11i1I1I = re . compile ( '<amp-video src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'https:' + I11i1I1I
  O0O00Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , O0O00Oo , False )
  if 58 - 58: ooo0Oo0 . i11Ii11I1Ii1i + i1iII1I1i1i1 - i11iIiiIii / i11Ii11I1Ii1i / O0
 except : pass
 quit ( 0 )
 if 85 - 85: Oooo0000 + i1iIIII
def I1II ( ) :
 if 27 - 27: i11Ii11I1Ii1i / iiiI11 . i1iIIII
 OOOO = 'http://www.watchepisodeseries.com/home/schedule'
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( I11i1I1I )
 for OOOO , i1II11II , oOo00O000Oo0 in Ii1I1i :
  OOOO0OOoO0O0 ( "[COLOR aqua]" + i1II11II + "  " + oOo00O000Oo0 + "[/COLOR]" , OOOO , 67 , I1IiI , I1ii11iIi11i )
  if 18 - 18: oooOOOOO * i1 . i1 * i1iII1I1i1i1 * i11Ii11I1Ii1i * i1iIIi1
  if 92 - 92: ooo0Oo0
def iI11I ( url ) :
 if 53 - 53: iIii1I11I1II1 + iiiI11 - i1iIIi1
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 1 ]
  I1111IIi = O0oO0 ( I1111IIi )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  o00OO00OoO = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0 ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0 ) [ 0 ]
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 68 , o00OO00OoO , I1ii11iIi11i )
  if 93 - 93: i11Ii11I1Ii1i . iiI1iIiI - ooo0Oo0 + Oooo0000
  if 61 - 61: i11Ii11I1Ii1i
def Ii1ii111i1 ( url , iconimage , fanart ) :
 if 31 - 31: i1iIIII + O0
 o0O = O00oO ( url )
 oO0oOOoo00000 = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( o0O )
 for oO0 in oO0oOOoo00000 :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
 I11i1I1I = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( o0O )
 oOooOOOoOo = datetime . now ( )
 for oO0 in I11i1I1I :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
   I1111IIi = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( oO0 ) [ 0 ]
   I1111IIi = O0oO0 ( I1111IIi )
   oOo00 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( oO0 ) [ 0 ]
   i1iI11i1IIi = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( oO0 ) [ 0 ]
   i1II11II = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( oO0 ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in i1II11II :
    i1II11II = i1II11II . strip ( )
    i1II11II = time . strptime ( i1II11II , "%d/%m/%Y" )
    ii1IIi111 = ( "%s/%s/%s" % ( oOooOOOoOo . day , oOooOOOoOo . month , oOooOOOoOo . year ) )
    ii1IIi111 = time . strptime ( ii1IIi111 , "%d/%m/%Y" )
    if ( ii1IIi111 < i1II11II ) :
     I1111IIi = '[COLOR yellow]' + ( I1111IIi ) + ' - Not Aired Yet' + '[/COLOR]'
     i1iI11i1IIi = '[COLOR yellow]' + ( i1iI11i1IIi ) + '[/COLOR]'
     oOo00 = '[COLOR yellow]' + ( oOo00 ) + '[/COLOR]'
     if 29 - 29: o000o0o00o0Oo . IiiIII111ii * i1iII1I1i1i1
    if not 'Season 0' in oOo00 :
     OOOO0OOoO0O0 ( "[COLOR aqua]" + oOo00 + " " + i1iI11i1IIi + " " + I1111IIi + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 68 - 68: i11iIiiIii + iiiI11
  if 77 - 77: i1iIIi1
def OooOOOOoO00OoOO ( url , iconimage , fanart ) :
 if 85 - 85: i1iII1I1i1i1 - iIii1I11I1II1 / O0
 if 99 - 99: i11Ii11I1Ii1i * IiiIII111ii % iIii1I11I1II1 / iiiI11
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  try :
   I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
   I1111IIi = I1111IIi . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
   if not 'Lolzor.Com' in I1111IIi :
    if not 'Videoplayer.Gq' in I1111IIi :
     if not 'Vidbaba.Com' in I1111IIi :
      if not 'Gagomatic.Com' in I1111IIi :
       if not 'Favour.Me' in I1111IIi :
        if not 'Funblr.Com' in I1111IIi :
         if not 'Vid.Ag' in I1111IIi :
          if not 'Mycollection.Net' in I1111IIi :
           if not 'Adhqmedia.Com' in I1111IIi :
            if not 'Filenuke.Com' in I1111IIi :
             if not 'Mrfile.Me' in I1111IIi :
              oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 90 - 90: i1iII1I1i1i1 % i1iIIII - i1iIIII % i11Ii11I1Ii1i * i1
  if 39 - 39: O00OoOoo00
def ooO000O000 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    OOoOooOoOOOoo = liveresolver . resolve ( url )
   else : OOoOooOoOOOoo = url
   O0O00Oo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   O0O00Oo . setPath ( OOoOooOoOOOoo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O00Oo )
   xbmc . Player ( ) . play ( OOoOooOoOOOoo )
   if 19 - 19: iIii1I11I1II1
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 26 - 26: OoooooooOO % iiI1iIiI % ooo0Oo0 . iiI1iIiI % iiiI11
def i1I1I ( ) :
 if 95 - 95: IiiIII111ii
 III11I1 = ''
 IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Search Term' )
 IIi1IIIi . doModal ( )
 if IIi1IIIi . isConfirmed ( ) :
  III11I1 = IIi1IIIi . getText ( )
  if len ( III11I1 ) > 1 :
   O00Ooo = III11I1 . lower ( )
   O00Ooo = O00Ooo . replace ( ' ' , '%20' )
   if 51 - 51: i11Ii11I1Ii1i + IiiIII111ii . i1IIi . o000o0o00o0Oo + Oooo0000 * iiI1iIiI
  else : quit ( )
 else : O00Ooo = urllib . unquote_plus ( OOOO ) . lower ( ) ; III11I1 = urllib . unquote_plus ( OOOO )
 OOOO = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + O00Ooo
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '"series"(.+?)"series_id"' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( 'original_name":"(.+?)"' ) . findall ( oO0 ) [ 0 ]
  O0i1II1Iiii1I11 = re . compile ( '"seo_name":"(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://www.watchepisodeseries.com/' + O0i1II1Iiii1I11
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + O0i1II1Iiii1I11 + '.jpg'
  OOOO0OOoO0O0 ( I1111IIi , OOOO , 68 , I1IiI , I1ii11iIi11i , '' )
  if 72 - 72: i1iII1I1i1i1 + i1iII1I1i1i1 / i11Ii11I1Ii1i . OoooooooOO % iiiI11
def III ( ) :
 if 41 - 41: i11iIiiIii + ooo0Oo0 / iiI1iIiI . OoooooooOO % i1iII1I1i1i1 % i1IIi
 OOOO = 'http://www.watchepisodeseries.com/home/popular-series'
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<div title="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1111IIi = O0oO0 ( I1111IIi )
  OOOO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  OOOO0OOoO0O0 ( '[COLOR aqua]' + I1111IIi + '[/COLOR]' , OOOO , 68 , I1IiI , I1ii11iIi11i )
  if 70 - 70: ooo0Oo0 . OoooooooOO - oooOOOOO
  if 30 - 30: o000o0o00o0Oo % iiI1iIiI
def O0Oo00 ( ) :
 if 41 - 41: iIii1I11I1II1 % O00OoOoo00
 try :
  oOo0oO = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1
   else : quit ( )
  if O00Ooo == oOo0oO :
   IIi1IIIIi ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter The Password You Set' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1
   else : quit ( )
  with open ( i1i1II , "w" ) as o000oo :
   o000oo . write ( O00Ooo )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 70 - 70: i1iIIII / i11Ii11I1Ii1i - iIii1I11I1II1 - oooOOOOO
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . i11Ii11I1Ii1i / i1IIi - O00OoOoo00
   if 30 - 30: Oooo0000
def IIi1IIIIi ( ) :
 if 21 - 21: i11iIiiIii / i1iIIi1 % i1iIIII * O0 . O00OoOoo00 - iIii1I11I1II1
 iiIiiii1i1i1i = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 OOOOooO0oO00O0o = '[COLOR aqua]Asian Special Porn[/COLOR]'
 OOOO0OOoO0O0 ( OOOOooO0oO00O0o , iiIiiii1i1i1i , 1 , I1IiI , Oo , '' )
 OOOO = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 o0O = O00oO ( OOOO )
 I11i1I1I = re . compile ( '<li class="">(.+?)</li>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oO0 ) [ 0 ]
  ooOO00oOOo000 = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( oO0 ) [ 0 ]
  O0i1II1Iiii1I11 = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'https://www.eporner.com' + O0i1II1Iiii1I11
  if not 'All' in I1111IIi :
   if not 'Homemade' in I1111IIi :
    OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "  " + "[COLOR yellow]" + ooOO00oOOo000 + "[/COLOR]" , OOOO , 36 , I1IiI , Oo , '' )
    if 14 - 14: i1 . i11Ii11I1Ii1i . O00OoOoo00 / iiiI11 % o000o0o00o0Oo - IiIi1Iii1I1
def o0oOoO0O ( url ) :
 if 84 - 84: O0 * OoooooooOO - IiiIII111ii * IiiIII111ii
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( 'title="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  O0i1II1Iiii1I11 = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = 'https://www.eporner.com' + O0i1II1Iiii1I11
  OOOO0OOoO0O0 ( "[COLOR skyblue]" + I1111IIi + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 8 - 8: IiIi1Iii1I1 / i1IIi . i1iII1I1i1i1
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( o0O ) [ 0 ]
  oO0OOOO0 = 'https://www.eporner.com' + o0OOo0o0O0O
  o0OO0o0oOOO0O = 'http://imgur.com/3eNoY0p'
  OOOO0OOoO0O0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , oO0OOOO0 , 36 , o0OO0o0oOOO0O , Oo , '' )
 except : pass
 if 41 - 41: oooOOOOO + i1
def oOO ( url , iconimage ) :
 if 11 - 11: i11iIiiIii - i1iII1I1i1i1 . i1iII1I1i1i1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11I = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( I11I )
 for iIIII1i , o0O in Ii1I1i :
  iIIII1i = iIIII1i . replace ( ':' , '' )
  url = 'https://www.eporner.com' + o0O
  oo0OooOOo0 ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + iIIII1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 76 - 76: oooOOOOO + IiIi1Iii1I1
def Iiii11iIi1 ( url ) :
 if 40 - 40: O00OoOoo00 % i1 . i1iIIi1
 oo0OooOOo0 ( "[COLOR yellow]Anime Catergories[/COLOR]" , url , 999 , I1IiI , Oo , '' )
 o0O = O00oO ( url )
 I11i1I1I = re . compile ( '<ul class="nav nav-pills nav-stacked"><li>(.+?)</ul>' ) . findall ( o0O ) [ 1 ]
 Ii1I1i = re . compile ( '<a href="(.+?)" title="(.+?)">.+?</a>' ) . findall ( I11i1I1I )
 for url , I1111IIi in Ii1I1i :
  I1111IIi = I1111IIi . strip ( )
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 52 , I1IiI , Oo , '' )
  if 84 - 84: Oooo0000 % IiIi1Iii1I1 - Oooo0000 . i1IIi11111i
def III1iI1iII1I ( url ) :
 if 39 - 39: iiiI11 * IiIi1Iii1I1 / Oooo0000 * i1 . O00OoOoo00 % i11Ii11I1Ii1i
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<th class="st-sort-descent">(.+?)</table>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '<a href="(.+?)".+?>(.+?)</a>' ) . findall ( I11i1I1I )
 for url , I1111IIi in Ii1I1i :
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 71 - 71: i1iIIi1 % i1IIi - i11Ii11I1Ii1i - i1iIIII + i1iIIII * IiIi1Iii1I1
def OoOOO ( url ) :
 if 67 - 67: oooOOOOO % oooOOOOO / oooOOOOO
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1IiI = re . compile ( '''<div class=\"col-md-3\">.+?url\('(.+?)'\)''' ) . findall ( o0O ) [ 0 ]
 except :
  I1IiI = o00OO00OoO
 I11i1I1I = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( o0O ) [ 0 ]
 Ii1I1i = re . compile ( '''<a class="black" href='(.+?)'>(.+?)</a>''' ) . findall ( I11i1I1I )
 oo0OooOOo0 ( "[COLOR yellow]Links Can Take Up To 45 Secs To Play, Be Patient![/COLOR]" , url , 54 , I1IiI , Oo , '' )
 for url , I1111IIi in Ii1I1i :
  oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  if 53 - 53: iIii1I11I1II1
def oooo00o0o0o ( url , iconimage ) :
 if 87 - 87: O00OoOoo00 * i1IIi - iiiI11 % i1iIIII / i1iIIi1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1II1 = re . compile ( '<source src="(.+?)"' ) . findall ( o0O ) [ 0 ]
 Oooo0oOO ( oOOoo0Oo , i1II1 , iconimage )
 if 39 - 39: iiI1iIiI * i11iIiiIii - i1iII1I1i1i1 / IiiIII111ii % i1iIIi1 % O00OoOoo00
 if 65 - 65: i1iII1I1i1i1 - IiIi1Iii1I1 % OoooooooOO / OoooooooOO % OoooooooOO
 if 52 - 52: o000o0o00o0Oo + o000o0o00o0Oo . i11Ii11I1Ii1i
 if 34 - 34: OoooooooOO . O0 / i1iII1I1i1i1 * Oooo0000 - o000o0o00o0Oo
 if 36 - 36: i1IIi / O0 / i1 - O0 - i1IIi
 if 22 - 22: i1IIi + iiiI11
 if 54 - 54: IiIi1Iii1I1 % i1iIIII . i1iIIi1 + i1iII1I1i1i1 - i1iIIII * iiI1iIiI
 if 92 - 92: i1IIi11111i + i1iIIi1 / ooo0Oo0 % i1 % IiiIII111ii . OoooooooOO
def O0Oo ( url ) :
 if 7 - 7: IiiIII111ii % iIii1I11I1II1 + O00OoOoo00 - iiiI11 * i1iII1I1i1i1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( 'title="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ] . replace ( './' , '/' )
  if 94 - 94: Oooo0000 . O0 / iiiI11 . o000o0o00o0Oo - i1IIi
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  iIIII1i = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( oO0 ) [ 0 ]
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[COLOR yellow] " + iIIII1i + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 26 - 26: i1 - i1iIIII . i1IIi11111i
 try :
  oO0OOOO0 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( o0O ) [ 0 ]
  o0OOo0o0O0O = re . compile ( '<a.+?href="(.+?)"' ) . findall ( oO0OOOO0 ) [ 5 ]
  OO0o0o0oo0O = 'http://m4ufree.com' + o0OOo0o0O0O
  if 'genre' in OO0o0o0oo0O :
   OO0o0o0oo0O = OO0o0o0oo0O . replace ( '.com' , '.com/' )
  IIiI1I1 = 'https://i.imgur.com/mjCRjXT.png'
  OOOO0OOoO0O0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OO0o0o0oo0O , 42 , IIiI1I1 , Oo , '' )
 except : pass
 if 15 - 15: iiiI11 * ooo0Oo0 % o000o0o00o0Oo * iIii1I11I1II1 - i11iIiiIii
def Oo00OOOOoo0oo ( url , iconimage ) :
 if 80 - 80: i1iIIi1 * Oooo0000 * i11Ii11I1Ii1i - O0 . Oooo0000 % iiI1iIiI
 import requests
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 II1 = re . compile ( 'data="(.+?)"' ) . findall ( o0O ) [ 0 ]
 iiIIIiIii = 'http://m4ufree.com/ajax_new.php'
 I1i11II = requests . post ( iiIIIiIii , data = { 'm4u' : II1 } )
 json = ( I1i11II . text )
 II11 = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 I1iii = re . compile ( '{(.+?)}' ) . findall ( II11 )
 oOO0OO0O = 0
 for oOooOOOoOo in I1iii :
  try :
   oOO0OO0O += 1
   I1111IIi = 'Link ' + str ( oOO0OO0O )
   iIIII1i = re . compile ( '''"label":"(.+?)"''' ) . findall ( oOooOOOoOo ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( oOooOOOoOo ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   oo0OooOOo0 ( "[COLOR aqua]" + I1111IIi + " | [COLOR yellow] " + iIIII1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( oOooOOOoOo ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   iIIII1i = re . compile ( """label:.+?'(.+?)'""" ) . findall ( oOooOOOoOo ) [ 0 ]
   oo0OooOOo0 ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + iIIII1i + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 78 - 78: iiiI11 / i11Ii11I1Ii1i % Oooo0000
def oO00OoOO ( ) :
 if 18 - 18: IiIi1Iii1I1 - Oooo0000 % i1IIi + O0 + i11iIiiIii + i1IIi
 OOOO = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 o0O = O00oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<td>(.+?)</td>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  OOOO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ]
  I1iI1ii1II = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  OOOO = 'http://www.livefootballol.me' + OOOO
  OOOO0OOoO0O0 ( "[COLOR aqua]" + I1iI1ii1II + "[/COLOR]" , OOOO , 74 , o00OO00OoO , Oo , '' )
  if 91 - 91: Oooo0000 + IiIi1Iii1I1 . iiI1iIiI
def O0oOoOOO0OO ( url ) :
 if 91 - 91: IiiIII111ii + Oooo0000 + i1IIi11111i - iIii1I11I1II1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<a href="(.+?)"' ) . findall ( o0O )
 iiiI1ii11 = 0
 for II1I in I11i1I1I :
  if 'acestream' in II1I :
   if 'http' in II1I :
    iiiI1ii11 += 1
    I1111IIi = '[COLOR aqua]Link :: ' + str ( iiiI1ii11 ) + '[/COLOR]'
    oo0OooOOo0 ( I1111IIi , II1I , 75 , o00OO00OoO , Oo , '' )
 if iiiI1ii11 == 0 :
  oo0OooOOo0 ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , o00OO00OoO , Oo , '' )
  if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
def ooOooo0OO ( url ) :
 if 2 - 2: i11Ii11I1Ii1i - i1 . IiiIII111ii * oooOOOOO / i1iII1I1i1i1
 o0O = O00oO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
 Oooo0oOO ( oOOoo0Oo , url , o00OO00OoO )
 if 80 - 80: i1iIIII / O00OoOoo00 / Oooo0000 + i1IIi - ooo0Oo0
def iIIiiIIi1IiI ( url , getphp ) :
 oOOoo = urllib2 . Request ( url )
 oOOoo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 oOOoo . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 iII1111III1I = urllib2 . urlopen ( oOOoo , timeout = 10 )
 o0O = iII1111III1I . read ( )
 iII1111III1I . close ( )
 return o0O
 if 14 - 14: IiiIII111ii % i1iII1I1i1i1 % ooo0Oo0 - i11iIiiIii
 if 53 - 53: iiiI11 % ooo0Oo0
 if 59 - 59: i1iIIII % iIii1I11I1II1 . i1IIi + i11Ii11I1Ii1i * IiiIII111ii
def i1IiiI1iIi ( ) :
 if 66 - 66: i1 * ooo0Oo0
 OOOO = 'http://m4ufree.com/?sort=key_top&page=1&='
 o0O = O00oO ( OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( o0O )
 for oO0 in I11i1I1I :
  I1111IIi = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0 ) [ 0 ]
  O0i1II1Iiii1I11 = re . compile ( '<a href="(.+?)"' ) . findall ( oO0 ) [ 0 ] . replace ( './' , '' )
  OOOO = 'http://m4ufree.com/' + O0i1II1Iiii1I11
  if not re . search ( '\d+' , I1111IIi ) :
   OOOO0OOoO0O0 ( "[COLOR aqua]" + I1111IIi + "[/COLOR]" , OOOO , 42 , I1IiI , Oo )
   if 28 - 28: i1 % Oooo0000 % o000o0o00o0Oo + iiI1iIiI / iiI1iIiI
   if 71 - 71: i1iIIII * i1 % OoooooooOO % i1 / iiI1iIiI
   if 56 - 56: OoooooooOO % i11iIiiIii * iIii1I11I1II1 . i1 * O0
   if 23 - 23: i11iIiiIii
   if 39 - 39: i1IIi11111i - o000o0o00o0Oo % oooOOOOO * i1 - i1iIIII / oooOOOOO
   if 29 - 29: o000o0o00o0Oo
   if 52 - 52: i11iIiiIii / i1IIi
   if 1 - 1: IiIi1Iii1I1
   if 78 - 78: o000o0o00o0Oo + O00OoOoo00 - O0
   if 10 - 10: i1iIIi1 % iiI1iIiI
def O0oO0 ( text ) :
 if 97 - 97: OoooooooOO - i1iIIi1
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
 if 58 - 58: iIii1I11I1II1 + O0
 return text
 if 30 - 30: IiIi1Iii1I1 % oooOOOOO * i1iIIII - o000o0o00o0Oo * iiiI11 % IiIi1Iii1I1
def iiiiI11ii ( ) :
 if 96 - 96: oooOOOOO . O0 / oooOOOOO % O0
 o0o000 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 i1iiiIii11 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 OOoOOO000O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 oOo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 48 - 48: ooo0Oo0 - OoooooooOO % i1iIIII * Oooo0000
 oOoO = 0
 for ( IIII , iI1iiiIiii , ii1i1i ) in os . walk ( i1iiiIii11 ) :
  for file in ii1i1i :
   II11iIII1i1I = os . path . join ( IIII , file )
   oOoO += os . path . getsize ( II11iIII1i1I )
 Oo0oOOo = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoO / ( 1024 * 1024.0 ) )
 oo0OooOOo0 ( Oo0oOOo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 63 - 63: ooo0Oo0 + i1iIIi1 - i11Ii11I1Ii1i
 oOoO = 0
 for ( IIII , iI1iiiIiii , ii1i1i ) in os . walk ( o0o000 ) :
  for file in ii1i1i :
   II11iIII1i1I = os . path . join ( IIII , file )
   oOoO += os . path . getsize ( II11iIII1i1I )
 Oo0oOOo = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoO / ( 1024 * 1024.0 ) )
 oo0OooOOo0 ( Oo0oOOo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 2 - 2: IiiIII111ii
 oOoO = 0
 for ( IIII , iI1iiiIiii , ii1i1i ) in os . walk ( OOoOOO000O0 ) :
  for file in ii1i1i :
   II11iIII1i1I = os . path . join ( IIII , file )
   oOoO += os . path . getsize ( II11iIII1i1I )
 Oo0oOOo = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoO / ( 1024 * 1024.0 ) )
 oo0OooOOo0 ( Oo0oOOo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 97 - 97: i1iII1I1i1i1 - OoooooooOO
 oOoO = 0
 for ( IIII , iI1iiiIiii , ii1i1i ) in os . walk ( oOo0 ) :
  for file in ii1i1i :
   II11iIII1i1I = os . path . join ( IIII , file )
   oOoO += os . path . getsize ( II11iIII1i1I )
 Oo0oOOo = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoO / ( 1024 * 1024.0 ) )
 oo0OooOOo0 ( Oo0oOOo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 79 - 79: Oooo0000 % IiiIII111ii % ooo0Oo0
 oo0OooOOo0 ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 oo0OooOOo0 ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 29 - 29: OoooooooOO . iiI1iIiI % o000o0o00o0Oo - oooOOOOO
def Oooo0oOO ( name , url , iconimage ) :
 if 8 - 8: i1IIi
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import urlresolver
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
 if 'acestream' in url :
  O0i1II1Iiii1I11 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  O0O00Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  O0O00Oo . setPath ( url )
  xbmc . Player ( ) . play ( O0i1II1Iiii1I11 , O0O00Oo , False )
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  O0O00Oo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O00Oo . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , O0O00Oo , False )
  time . sleep ( 2 )
  quit ( )
 else :
  OOoOooOoOOOoo = url
  O0O00Oo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O00Oo . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , O0O00Oo , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 32 - 32: i1iII1I1i1i1 / i11Ii11I1Ii1i
def II1Iii ( name , url , iconimage ) :
 if 73 - 73: O00OoOoo00 * OoooooooOO . O0 . IiiIII111ii
 OOooo , o0oooO = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 OOooo += urllib . unquote_plus ( o0oooO )
 url = regex . resolve ( OOooo )
 if 89 - 89: i11Ii11I1Ii1i / i1iII1I1i1i1
 PLAYREGEX ( name , url , iconimage )
 if 14 - 14: i1iIIII . iiI1iIiI * IiIi1Iii1I1 + i11Ii11I1Ii1i - IiIi1Iii1I1 + i1iIIII
def IIiIiI ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 18 - 18: i1iII1I1i1i1 - i1IIi11111i - iiI1iIiI - iiI1iIiI
def OOooo00 ( heading , text ) :
 if 35 - 35: i1iIIi1 . Oooo0000 * i11iIiiIii
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 iiII = xbmcgui . Window ( id )
 o0Oii1111i = 50
 while ( o0Oii1111i > 0 ) :
  try :
   xbmc . sleep ( 10 )
   o0Oii1111i -= 1
   iiII . getControl ( 1 ) . setLabel ( heading )
   iiII . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 75 - 75: IiiIII111ii + i11Ii11I1Ii1i / i1iII1I1i1i1 - i1iII1I1i1i1 / OoooooooOO
  if 2 - 2: i1IIi11111i
def O00oO ( url ) :
 try :
  oOOoo = urllib2 . Request ( url )
  oOOoo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iII1111III1I = urllib2 . urlopen ( oOOoo , timeout = 5 )
  o0O = iII1111III1I . read ( )
  iII1111III1I . close ( )
  o0O = o0O . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return o0O
 except : quit ( )
 if 19 - 19: i11Ii11I1Ii1i
def O0oO ( url ) :
 try :
  oOOoo = urllib2 . Request ( url )
  oOOoo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  iII1111III1I = urllib2 . urlopen ( oOOoo , timeout = 5 )
  o0O = iII1111III1I . read ( )
  iII1111III1I . close ( )
  o0O = o0O . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return o0O
 except : quit ( )
 if 72 - 72: OoooooooOO / iiI1iIiI + iiiI11 / Oooo0000 * iiiI11
def oo0OooOOo0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 Ii1iIi111i1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 IIOO0ooOo0OoOo0 = True
 O0O00Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O00Oo . setProperty ( "fanart_Image" , fanart )
 O0O00Oo . setProperty ( "icon_Image" , iconimage )
 O0O00Oo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0O00Oo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 87 - 87: i1iII1I1i1i1 . iiI1iIiI
 IIOO0ooOo0OoOo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1iIi111i1i1 , listitem = O0O00Oo , isFolder = False )
 return IIOO0ooOo0OoOo0
 if 17 - 17: iiiI11 . i11iIiiIii
def oo0oOo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 Ii1iIi111i1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 IIOO0ooOo0OoOo0 = True
 O0O00Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O00Oo . setProperty ( "fanart_Image" , fanart )
 O0O00Oo . setProperty ( "icon_Image" , iconimage )
 O0O00Oo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 5 - 5: o000o0o00o0Oo + O0 + O0 . i1iIIi1 - IiIi1Iii1I1
 O0O00Oo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 63 - 63: i1iII1I1i1i1
 IIOO0ooOo0OoOo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1iIi111i1i1 , listitem = O0O00Oo , isFolder = False )
 return IIOO0ooOo0OoOo0
 if 71 - 71: i1IIi . iiiI11 * oooOOOOO % OoooooooOO + i1iIIII
def iIIi1iiI1i11 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oooiIii11i1I = [ ]
 oOOOoOoO = [ ]
 I1i = [ ]
 o0O = O00oO ( url )
 II1I = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II1I ) [ 0 ]
 oO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( II1I )
 if len ( oO0 ) < 1 :
  oO0 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( II1I )
 oOooOOOoOo = 1
 for i1II1iII in oO0 :
  II1i = i1II1iII
  if '(' in i1II1iII :
   i1II1iII = i1II1iII . split ( '(' ) [ 0 ]
   o0OO00oo = str ( II1i . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   oooiIii11i1I . append ( i1II1iII )
   oOOOoOoO . append ( o0OO00oo )
  else :
   oooiIii11i1I . append ( i1II1iII )
   oOOOoOoO . append ( '[COLOR aqua]Link ' + str ( oOooOOOoOo ) + '[/COLOR]' )
  oOooOOOoOo = oOooOOOoOo + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i1i1IiIiIi1Ii = Iii1ii1II11i . select ( name , oOOOoOoO )
 if i1i1IiIiIi1Ii < 0 :
  quit ( )
 else :
  url = oooiIii11i1I [ i1i1IiIiIi1Ii ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : OOoOooOoOOOoo = liveresolver . resolve ( url )
  else : OOoOooOoOOOoo = url
  O0O00Oo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  O0O00Oo . setPath ( OOoOooOoOOOoo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O00Oo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo )
  if 64 - 64: i1iIIII + OoooooooOO * OoooooooOO
def i1I ( name , url , iconimage ) :
 if 36 - 36: iiI1iIiI * ooo0Oo0
 oOOo00o0OO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 oooiIii11i1I = [ ]
 oOOOoOoO = [ ]
 I1i = [ ]
 OO0ooo0o0 = [ ]
 o0O = O00oO ( url )
 II1I = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O ) [ 0 ]
 oO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( II1I )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II1I ) [ 0 ]
 oOooOOOoOo = 1
 if 69 - 69: o000o0o00o0Oo - i1iIIi1
 for i1II1iII in oO0 :
  II1i = i1II1iII
  if '(' in i1II1iII :
   i1II1iII = i1II1iII . split ( '(' ) [ 0 ]
   o0OO00oo = str ( II1i . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   oooiIii11i1I . append ( i1II1iII )
   oOOOoOoO . append ( o0OO00oo )
   OO0ooo0o0 . append ( 'Stream ' + str ( oOooOOOoOo ) )
  else :
   oooiIii11i1I . append ( i1II1iII )
   oOOOoOoO . append ( 'Link ' + str ( oOooOOOoOo ) )
   if 16 - 16: ooo0Oo0
  oOooOOOoOo = oOooOOOoOo + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i1i1IiIiIi1Ii = Iii1ii1II11i . select ( name , oOOOoOoO )
 if i1i1IiIiIi1Ii < 0 :
  quit ( )
 else :
  iI1iII1 = oOOOoOoO [ i1i1IiIiIi1Ii ]
  oO0OOoo0OO = "/"
  if not iI1iII1 . endswith ( oO0OOoo0OO ) :
   O0ii1ii1ii = iI1iII1 + "/"
  else :
   O0ii1ii1ii = iI1iII1
  url = oOOo00o0OO + oooiIii11i1I [ i1i1IiIiIi1Ii ] + "%26referer=" + O0ii1ii1ii
  print url
  if 14 - 14: i1IIi - O0 % ooo0Oo0
  xbmc . Player ( ) . play ( url )
  if 92 - 92: iiiI11 % oooOOOOO / o000o0o00o0Oo % o000o0o00o0Oo * iiI1iIiI
def iiIi1IIi1I ( string ) :
 OooO00oOOo0Oo = ( c for c in string if 0 < ord ( c ) < 127 )
 if 5 - 5: i1IIi11111i . O0 / ooo0Oo0 % i1
 return '' . join ( OooO00oOOo0Oo )
 if 60 - 60: i11Ii11I1Ii1i / iIii1I11I1II1 + o000o0o00o0Oo . i11iIiiIii
def OOOO0OOoO0O0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 40 - 40: i1IIi11111i
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 Ii1iIi111i1i1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIOO0ooOo0OoOo0 = True
 O0O00Oo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 O0O00Oo . setProperty ( "fanart_Image" , fanart )
 O0O00Oo . setProperty ( "icon_Image" , iconimage )
 O0O00Oo . setInfo ( 'video' , { 'Plot' : description } )
 IIOO0ooOo0OoOo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1iIi111i1i1 , listitem = O0O00Oo , isFolder = True )
 return IIOO0ooOo0OoOo0
 if 78 - 78: iIii1I11I1II1
def ooO0oo0o0 ( name , url , iconimage ) :
 IIOO0ooOo0OoOo0 = True
 O0O00Oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; O0O00Oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 IIOO0ooOo0OoOo0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = O0O00Oo )
 xbmc . Player ( ) . play ( url , O0O00Oo , False )
 if 9 - 9: iiI1iIiI + o000o0o00o0Oo / iiI1iIiI . i1iII1I1i1i1 * IiIi1Iii1I1
def i1i1ii1111i1i ( ) :
 if 46 - 46: i1IIi
 o0o000 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 i1iiiIii11 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 OOoOOO000O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 54 - 54: i11Ii11I1Ii1i - Oooo0000
 oOooOOOoOo = [ ( o0o000 , 'Cache' ) , ( i1iiiIii11 , 'Thumbnails' ) , ( OOoOOO000O0 , 'Packages' ) ]
 if 73 - 73: i1iIIII
 Iiii1IiIi = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if Iiii1IiIi :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for OOooo in oOooOOOoOo :
   if 39 - 39: i1iIIII * IiiIII111ii
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % OOooo [ 1 ] )
   time . sleep ( 1 )
   if 2 - 2: i1IIi - IiIi1Iii1I1 + iiI1iIiI . i1IIi11111i * i1IIi11111i / Oooo0000
   for oOOO , iI1iiiIiii , ii1i1i in os . walk ( OOooo [ 0 ] ) :
    for I11II1i in ii1i1i :
     if ( I11II1i . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( oOOO , I11II1i ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % OOooo [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 16 - 16: i1iII1I1i1i1 + IiIi1Iii1I1 / i1IIi11111i
def O00oOoo0OoO0 ( url , mode , name , iconimage , fanart ) :
 if 62 - 62: i1IIi / IiIi1Iii1I1 . iiI1iIiI * i1IIi11111i
 with open ( I11i , "a" ) as o000oo :
  o000oo . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 21 - 21: i1IIi11111i
def O0Oo0 ( ) :
 if 98 - 98: i1iIIi1
 with open ( I11i , "a" ) as o000oo :
  o0oo0000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  i111i1i = open ( o0oo0000 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( i111i1i )
  oo0OooOOo0 ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  oo0OooOOo0 ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  if len ( I11i1I1I ) < 1 :
   oo0OooOOo0 ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  for IiIii1I1I in I11i1I1I :
   I1111IIi = re . compile ( '<title>(.+?)</title>' ) . findall ( IiIii1I1I ) [ 0 ]
   OOOO = re . compile ( '<url>(.+?)</url>' ) . findall ( IiIii1I1I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( IiIii1I1I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( IiIii1I1I ) [ 0 ]
   oo0OooOOo0 ( '[COLOR skyblue]' + I1111IIi + '[/COLOR]' , OOOO , 2 , I1IiI , I1ii11iIi11i )
   if 51 - 51: ooo0Oo0 % Oooo0000 * OoooooooOO . i11iIiiIii
 oo0OooOOo0 ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , o00OO00OoO , Oo )
 if 77 - 77: i11Ii11I1Ii1i
def I1i111IiIiIi1 ( ) :
 if 39 - 39: O00OoOoo00 - o000o0o00o0Oo
 with open ( IiII , "a" ) as o000oo :
  o0oo0000 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  i111i1i = open ( o0oo0000 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( i111i1i )
  oo0OooOOo0 ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  oo0OooOOo0 ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  if len ( I11i1I1I ) < 1 :
   oo0OooOOo0 ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , o00OO00OoO , Oo )
  for IiIii1I1I in I11i1I1I :
   I1111IIi = re . compile ( '<title>(.+?)</title>' ) . findall ( IiIii1I1I ) [ 0 ]
   OOOO = re . compile ( '<link>(.+?)</link>' ) . findall ( IiIii1I1I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( IiIii1I1I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( IiIii1I1I ) [ 0 ]
   oo0OooOOo0 ( '[COLOR skyblue]' + I1111IIi + '[/COLOR]' , OOOO , 2 , I1IiI , I1ii11iIi11i )
   if 53 - 53: i1IIi11111i % oooOOOOO + IiIi1Iii1I1 . ooo0Oo0 - o000o0o00o0Oo % i1IIi11111i
 oo0OooOOo0 ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , o00OO00OoO , Oo )
 if 64 - 64: i11Ii11I1Ii1i
def iIIIiIi1I1i ( ) :
 if 78 - 78: iIii1I11I1II1 % Oooo0000 + o000o0o00o0Oo / i1IIi % i11Ii11I1Ii1i + i1iIIII
 with open ( I11i , "w" ) as o000oo :
  o000oo . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 91 - 91: iIii1I11I1II1 % i1 . i1IIi11111i + iiiI11 + i1IIi11111i
def o00OOo ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as o000oo :
  o000oo . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 87 - 87: i1 % iiI1iIiI
 if 77 - 77: iIii1I11I1II1 - i1IIi . i1iII1I1i1i1
 if 26 - 26: i1IIi11111i * IiiIII111ii . i1IIi
def O000oo0O ( ) :
 if 59 - 59: O0 + i1IIi - i1IIi11111i
 if 62 - 62: i11iIiiIii % i1iIIII . IiiIII111ii . i1iIIII
 ooOo0O0O0oOO0 = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iIiIIi = re . compile ( '<pin>(.+?)</pin>' ) . findall ( ooOo0O0O0oOO0 ) [ 0 ]
  if iIiIIi == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   III11I1 = ''
   IIi1IIIi = xbmc . Keyboard ( III11I1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   IIi1IIIi . doModal ( )
   if IIi1IIIi . isConfirmed ( ) :
    III11I1 = IIi1IIIi . getText ( )
    if len ( III11I1 ) > 1 :
     O00Ooo = III11I1 . title ( )
     with open ( iI1Ii11111iIi , "w" ) as I11II1i :
      I11II1i . write ( "<pin>" + O00Ooo + "</pin>" )
     O000oo0O ( )
    else : quit ( )
   else : quit ( )
  if not 'EXPIRED' in iIiIIi :
   III1I = re . compile ( '<pin>(.+?)</pin>' ) . findall ( ooOo0O0O0oOO0 ) [ 0 ]
   I1I111iIi = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % III1I )
   o0O = O00oO ( I1I111iIi )
   if 'Pin Verified' in o0O :
    pass
   else :
    with open ( iI1Ii11111iIi , "w" ) as I11II1i :
     I11II1i . write ( '<pin>EXPIRED</pin>' )
     O000oo0O ( )
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as I11II1i :
   I11II1i . write ( "<pin>EXPIRED</pin>\n" )
  O000oo0O ( )
  if 53 - 53: iIii1I11I1II1 + i1IIi11111i - Oooo0000 - i1iII1I1i1i1 / IiIi1Iii1I1 % i11iIiiIii
  if 3 - 3: oooOOOOO . IiIi1Iii1I1 % iiI1iIiI + o000o0o00o0Oo
  if 64 - 64: i1IIi
  if 29 - 29: i1IIi11111i / i11iIiiIii / iiI1iIiI % i1iII1I1i1i1 % i11iIiiIii
def i111II ( url , iconimage , fanart ) :
 if 63 - 63: iiI1iIiI - i1 % oooOOOOO % O00OoOoo00 / i1IIi11111i / i1IIi
 try :
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Name To Save File As' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1 . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = OOoOooOoOOOoo
  OO0oo0O0OOO0 = url . split ( '/' ) [ - 1 ]
  Ii1iIi111i1i1 = urllib2 . urlopen ( url )
  OoOOo = os . path . join ( o0OOO , O00Ooo )
  I11II1i = open ( OoOOo , 'wb' )
  if 46 - 46: iiI1iIiI / iiiI11 . i1iIIi1 % i11iIiiIii + i1IIi11111i + OoooooooOO
  O0o0000o = Ii1iIi111i1i1 . info ( )
  oOo00OoOoO = int ( O0o0000o . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( O00Ooo , oOo00OoOoO ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 66 - 66: iiI1iIiI - IiiIII111ii
  iiIii = 0
  iIiIii1ii = 8192
  while True :
   buffer = Ii1iIi111i1i1 . read ( iIiIii1ii )
   if not buffer :
    break
    if 8 - 8: i1 + Oooo0000 . iIii1I11I1II1 % O0
   iiIii += len ( buffer )
   I11II1i . write ( buffer )
   iI11Ii111 = "[%3.2f%%]" % ( iiIii * 100. / oOo00OoOoO )
   iI11Ii111 = iI11Ii111 + chr ( 8 ) * ( len ( iI11Ii111 ) + 1 )
   iIiiiI . update ( iiIii , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( iI11Ii111 , O00Ooo ) )
   if 54 - 54: Oooo0000 % oooOOOOO . Oooo0000 * i1iIIII + Oooo0000 % i1IIi
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as o000oo :
   o000oo . write ( '<item>\n<title>' + O00Ooo + '</title>\n<link>' + OoOOo + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 23 - 23: i1iIIi1 - i1iIIII + iiiI11 - Oooo0000 * Oooo0000 . ooo0Oo0
  I11II1i . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 47 - 47: i1iII1I1i1i1 % iIii1I11I1II1
  if 11 - 11: iiI1iIiI % iiiI11 - i1 - i1iII1I1i1i1 + i1IIi11111i
  if 98 - 98: oooOOOOO + iiiI11 - i1
  if 79 - 79: i1iIIII / i1iIIi1 . Oooo0000 - o000o0o00o0Oo
def Ii1ii11IIIi ( ) :
 OOoooOOOo0oO = [ ]
 oO0Ooo0OooOOo = sys . argv [ 2 ]
 if len ( oO0Ooo0OooOOo ) >= 2 :
  O00o0O = sys . argv [ 2 ]
  iIIIiI = O00o0O . replace ( '?' , '' )
  if ( O00o0O [ len ( O00o0O ) - 1 ] == '/' ) :
   O00o0O = O00o0O [ 0 : len ( O00o0O ) - 2 ]
  O00 = iIIIiI . split ( '&' )
  OOoooOOOo0oO = { }
  for oOooOOOoOo in range ( len ( O00 ) ) :
   i1iiIII1IIiIIII = { }
   i1iiIII1IIiIIII = O00 [ oOooOOOoOo ] . split ( '=' )
   if ( len ( i1iiIII1IIiIIII ) ) == 2 :
    OOoooOOOo0oO [ i1iiIII1IIiIIII [ 0 ] ] = i1iiIII1IIiIIII [ 1 ]
 return OOoooOOOo0oO
 if 19 - 19: oooOOOOO - i1IIi11111i / i1IIi11111i + ooo0Oo0
O00o0O = Ii1ii11IIIi ( ) ; OOOO = None ; oOOoo0Oo = None ; OoO0o0000O = None ; II1o0ooO0OOO = None ; o00OO00OoO = None ; o0oo000OoOoo0 = None
try : II1o0ooO0OOO = urllib . unquote_plus ( O00o0O [ "site" ] )
except : pass
try : OOOO = urllib . unquote_plus ( O00o0O [ "url" ] )
except : pass
try : oOOoo0Oo = urllib . unquote_plus ( O00o0O [ "name" ] )
except : pass
try : OoO0o0000O = int ( O00o0O [ "mode" ] )
except : pass
try : o00OO00OoO = urllib . unquote_plus ( O00o0O [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( O00o0O [ "fanart" ] )
except : pass
try : o0oo000OoOoo0 = urllib . unquote_plus ( O00o0O [ "description" ] )
except : pass
if 81 - 81: O0 / IiiIII111ii - iIii1I11I1II1 / i11Ii11I1Ii1i
if OoO0o0000O == None or OOOO == None or len ( OOOO ) < 1 : o00 ( )
if 86 - 86: iIii1I11I1II1
if 18 - 18: i1 . i11Ii11I1Ii1i % Oooo0000 % iiiI11
if 87 - 87: iIii1I11I1II1 . OoooooooOO * Oooo0000
if 100 - 100: i1 / i1IIi - iiI1iIiI % iiiI11 - iIii1I11I1II1
if 17 - 17: O00OoOoo00 / i1IIi11111i % ooo0Oo0
elif OoO0o0000O == 1 : o0 ( oOOoo0Oo , OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 2 : Oooo0oOO ( oOOoo0Oo , OOOO , o00OO00OoO )
elif OoO0o0000O == 3 : iIIi1iiI1i11 ( oOOoo0Oo , OOOO , o00OO00OoO )
if 71 - 71: IiiIII111ii . i1iIIi1 . i1
if 68 - 68: i11iIiiIii % i1iII1I1i1i1 * i1 * IiiIII111ii * i11Ii11I1Ii1i + O0
if 66 - 66: O00OoOoo00 % o000o0o00o0Oo % OoooooooOO
elif OoO0o0000O == 4 : IIIIiiII111 ( OOOO )
elif OoO0o0000O == 5 : I1 ( OOOO )
elif OoO0o0000O == 6 : I111iI ( )
elif OoO0o0000O == 7 : OOOOo0 ( OOOO )
elif OoO0o0000O == 8 : oOo0O ( OOOO )
elif OoO0o0000O == 9 : iI ( OOOO )
elif OoO0o0000O == 10 : IIiIiI ( OOOO )
elif OoO0o0000O == 11 : o0o0O0O00oOOo ( )
elif OoO0o0000O == 12 : o0O0o0 ( OOOO )
elif OoO0o0000O == 13 : ooooo0O0000oo ( OOOO )
elif OoO0o0000O == 14 : oo0oO ( OOOO )
elif OoO0o0000O == 15 : ooO0O00Oo0o ( )
elif OoO0o0000O == 16 : i1I ( oOOoo0Oo , OOOO , o00OO00OoO )
elif OoO0o0000O == 17 : III1IiiI ( OOOO )
elif OoO0o0000O == 18 : I1IiiiiI ( OOOO )
elif OoO0o0000O == 19 : I11iiI1i1 ( OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 20 : O0OO0O ( )
elif OoO0o0000O == 21 : o0OIiI1i ( OOOO )
elif OoO0o0000O == 22 : II1i111Ii1i ( OOOO )
elif OoO0o0000O == 23 : I1ii1iIiii1I ( )
elif OoO0o0000O == 24 : OoO ( OOOO )
elif OoO0o0000O == 25 : o0OoOo00o0o ( OOOO , o00OO00OoO )
elif OoO0o0000O == 26 : o0OOOOooo ( OOOO )
elif OoO0o0000O == 27 : o000ooooO0o ( OOOO , o00OO00OoO )
elif OoO0o0000O == 28 : Iii1iiIi1II ( )
elif OoO0o0000O == 29 : IIII1 ( OOOO )
elif OoO0o0000O == 30 : o0oo0O ( OOOO )
elif OoO0o0000O == 31 : O00OoOO0oo0 ( OOOO )
elif OoO0o0000O == 32 : iIIII1iIIii ( OOOO )
elif OoO0o0000O == 33 : IIiI1Ii ( OOOO )
elif OoO0o0000O == 34 : iI1IiI ( OOOO )
elif OoO0o0000O == 35 : IIi1IIIIi ( )
elif OoO0o0000O == 36 : o0oOoO0O ( OOOO )
elif OoO0o0000O == 37 : oOO ( OOOO , o00OO00OoO )
elif OoO0o0000O == 38 : O0Oo00 ( )
elif OoO0o0000O == 39 : oOoO0 ( OOOO )
elif OoO0o0000O == 40 : O0OO0O ( )
elif OoO0o0000O == 41 : o0OIiI1i ( OOOO )
elif OoO0o0000O == 42 : O0Oo ( OOOO )
elif OoO0o0000O == 43 : Oo00OOOOoo0oo ( OOOO , o00OO00OoO )
elif OoO0o0000O == 44 : i1IiiI1iIi ( )
if 34 - 34: i1IIi11111i / oooOOOOO % O0 . i1 . i1IIi
elif OoO0o0000O == 45 : o00oO ( )
elif OoO0o0000O == 46 : OO0o ( OOOO )
elif OoO0o0000O == 47 : o0iiiI1I1iIIIi1 ( oOOoo0Oo , OOOO , o00OO00OoO )
elif OoO0o0000O == 48 : II ( )
elif OoO0o0000O == 49 : i11i1iiiII ( OOOO )
elif OoO0o0000O == 50 : IIi1ii1Ii ( OOOO )
elif OoO0o0000O == 51 : Iiii11iIi1 ( OOOO )
elif OoO0o0000O == 52 : III1iI1iII1I ( OOOO )
elif OoO0o0000O == 53 : OoOOO ( OOOO )
elif OoO0o0000O == 54 : oooo00o0o0o ( OOOO , o00OO00OoO )
if 29 - 29: O0 . i1iIIi1
if 66 - 66: i1iII1I1i1i1 * iIii1I11I1II1 % iIii1I11I1II1 * IiiIII111ii - IiIi1Iii1I1 - IiiIII111ii
if 70 - 70: i1iIIi1 + i1iII1I1i1i1
elif OoO0o0000O == 59 : I11i1 ( )
elif OoO0o0000O == 60 : iIiiI1iI ( OOOO )
elif OoO0o0000O == 61 : OoOo ( oOOoo0Oo , OOOO , o00OO00OoO )
if 93 - 93: i1iIIi1 + iiiI11
elif OoO0o0000O == 66 : I1II ( )
elif OoO0o0000O == 67 : iI11I ( OOOO )
elif OoO0o0000O == 68 : Ii1ii111i1 ( OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 69 : OooOOOOoO00OoOO ( OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 70 : ooO000O000 ( OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 71 : i1I1I ( )
elif OoO0o0000O == 72 : III ( )
elif OoO0o0000O == 73 : oO00OoOO ( )
elif OoO0o0000O == 74 : O0oOoOOO0OO ( OOOO )
elif OoO0o0000O == 75 : ooOooo0OO ( OOOO )
if 33 - 33: O0
if 78 - 78: O0 / i11Ii11I1Ii1i * i1
elif OoO0o0000O == 884 : iiiiI11ii ( )
elif OoO0o0000O == 885 : o00OOo ( )
elif OoO0o0000O == 886 : I1i111IiIiIi1 ( )
elif OoO0o0000O == 887 : i111II ( OOOO , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 888 : IiiiiI1i1Iii ( )
elif OoO0o0000O == 889 : O00oOoo0OoO0 ( OOOO , OoO0o0000O , oOOoo0Oo , o00OO00OoO , I1ii11iIi11i )
elif OoO0o0000O == 890 : O0Oo0 ( )
elif OoO0o0000O == 891 : iIIIiIi1I1i ( )
elif OoO0o0000O == 892 : i1i1ii1111i1i ( )
if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % i1iIIi1 - iIii1I11I1II1 % O0
if OoO0o0000O == None or OOOO == None or len ( OOOO ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 58 - 58: IiiIII111ii + iIii1I11I1II1
if 65 - 65: i11Ii11I1Ii1i - i1iIIi1 % i1IIi11111i - Oooo0000 * oooOOOOO + iiiI11
if 79 - 79: IiIi1Iii1I1 . Oooo0000 % i1iIIi1 - ooo0Oo0
if 69 - 69: IiIi1Iii1I1 - i1IIi11111i . IiIi1Iii1I1
if 9 - 9: i1iII1I1i1i1 % i11iIiiIii / ooo0Oo0
if 20 - 20: i1iII1I1i1i1 * O0 + O00OoOoo00 - OoooooooOO . O00OoOoo00
if 60 - 60: i1IIi11111i . i1IIi11111i / oooOOOOO
if 45 - 45: O0 . i11iIiiIii % oooOOOOO . Oooo0000 % IiiIII111ii % iIii1I11I1II1
if 58 - 58: iIii1I11I1II1 . Oooo0000 - i11iIiiIii * iIii1I11I1II1 % i11iIiiIii / iiI1iIiI
if 80 - 80: o000o0o00o0Oo / iIii1I11I1II1 % Oooo0000
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
