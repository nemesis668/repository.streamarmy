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
 if 71 - 71: i1Ii % OOoO00o / i1IIi11111i
 ooIiII1I1i1i1ii ( )
 ii11i1iIII ( )
 IiiiI1II1I1 ( )
 Ii1I = i1iII1IiiIiI1
 Oo0o0 = Ii1I
 III1ii1iII = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( III1ii1iII >= 0000 ) and ( III1ii1iII <= 1159 ) : oo0oooooO0 = "Morning"
 elif ( III1ii1iII >= 1200 ) and ( III1ii1iII <= 1759 ) : oo0oooooO0 = "Afternoon"
 else : oo0oooooO0 = "Evening"
 i11Iiii ( '[COLOR yellow]Good[COLOR aqua] ' + str ( oo0oooooO0 ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 i11Iiii ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  iI = I1i1I1II ( i1iII1IiiIiI1 )
  i1IiIiiI = re . compile ( '<item>(.+?)</item>' ) . findall ( iI )
  for I1I in i1IiIiiI :
   try :
    if '<m3u>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 11 , OoOo , I1ii11iIi11i )
    elif '<mamahdsports>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 14 , OoOo , I1ii11iIi11i )
    elif '<atc>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<atc>(.+?)</atc>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 6 , OoOo , I1ii11iIi11i )
    elif '<scanner>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 11 , OoOo , I1ii11iIi11i )
    elif '<cartoons>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 29 , OoOo , I1ii11iIi11i )
    elif '<Adult>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 38 , OoOo , I1ii11iIi11i )
    elif '<Anime>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 51 , OoOo , I1ii11iIi11i )
    elif '<audiobooks>' in I1I :
     oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     Ii1I = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( I1I ) [ 0 ]
     iIo00O ( oOO00oOO , Ii1I , 59 , OoOo , I1ii11iIi11i )
    elif '<folder>' in I1I :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( I1I )
     for oOO00oOO , Ii1I , OoOo , I1ii11iIi11i in OOO0OOO00oo :
      iIo00O ( oOO00oOO , Ii1I , 1 , OoOo , I1ii11iIi11i )
    else :
     Iii111II = re . compile ( '<link>(.+?)</link>' ) . findall ( I1I )
     if len ( Iii111II ) == 1 :
      OOO0OOO00oo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( I1I )
      iiii11I = len ( i1IiIiiI )
      for oOO00oOO , Ii1I , OoOo , I1ii11iIi11i in OOO0OOO00oo :
       if 'youtube.com/playlist' in Ii1I :
        iIo00O ( oOO00oOO , Ii1I , 2 , OoOo , I1ii11iIi11i )
       else :
        i11Iiii ( oOO00oOO , Ii1I , 2 , OoOo , I1ii11iIi11i )
     elif len ( Iii111II ) > 1 :
      oOO00oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
      OoOo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
      i11Iiii ( oOO00oOO , Oo0o0 , 3 , OoOo , I1ii11iIi11i )
   except : pass
   if 96 - 96: i11Ii11I1Ii1i % OOooO . OOoOoo00oo + OoooooooOO * OOo0o0 - Oooo0000
  i11Iiii ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.urlresolver/settings.xml" )
   oo0oooooO0 = open ( file ) . read ( )
   i11i1 = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( oo0oooooO0 ) [ 0 ]
   i11i1 = i11i1 . strip ( )
   Ii1I = 'plugin://script.module.urlresolver/?mode=auth_rd'
   if 'value=""' in i11i1 :
    IIIii1II1II = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    i11Iiii ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( IIIii1II1II ) + '[/COLOR]' , Ii1I , 2 , I1IiI , Oo )
   else :
    IIIii1II1II = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    i11Iiii ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( IIIii1II1II ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  i1I1iI = 'https://i.imgur.com/4Pzgdwu.png'
  iIo00O ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , i1I1iI , Oo )
  oo0OooOOo0 = 'https://i.imgur.com/Om0Lq7V.png'
  iIo00O ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , oo0OooOOo0 , Oo )
  o0O = 'https://i.imgur.com/klnhdFx.png'
  iIo00O ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , o0O , Oo )
 except :
  O00oO = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if O00oO == 0 :
   i11Iiii ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   iIo00O ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if O00oO == 1 :
   quit ( )
   if 39 - 39: I1iiiiI1iII - i11Ii11I1Ii1i * i1 % i1IIi11111i * i11Ii11I1Ii1i % i11Ii11I1Ii1i
 iii11iII ( )
 if 59 - 59: iIii1I11I1II1 + iiI1iIiI - i1IIi11111i - iiI1iIiI + OOoOoo00oo / o000o0o00o0Oo
def I1 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 Oo0o0 = url
 iI = I1i1I1II ( url )
 IiiiI1II1I1 ( )
 ii11i1iIII ( )
 i1IiIiiI = re . compile ( '<item>(.+?)</item>' ) . findall ( iI )
 for I1I in i1IiIiiI :
  try :
   if '<image>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 23 , iconimage , fanart )
   elif '<American>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 77 , iconimage , fanart )
   elif '<lordjd>' in I1I :
    Iii111II = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( I1I )
    if len ( Iii111II ) == 1 :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( I1I )
     iiii11I = len ( i1IiIiiI )
     for name , url , iconimage , fanart in OOO0OOO00oo :
      if 'youtube.com/playlist' in url :
       iIo00O ( name , url , 2 , iconimage , fanart )
      else :
       OO00Oo ( name , url , 2 , iconimage , fanart )
    elif len ( Iii111II ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     OO00Oo ( name , Oo0o0 , 3 , iconimage , fanart )
   elif '<reddit>' in I1I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( I1I ) [ 0 ]
    iIo00O ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in I1I :
    Iii111II = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( I1I )
    if len ( Iii111II ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( I1I ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<referer>(.+?)</referer>' ) . findall ( I1I ) [ 0 ]
     O00Oo000ooO0 = O0OOO0OOoO0O
     OoO0O00 = "/"
     if not O00Oo000ooO0 . endswith ( OoO0O00 ) :
      IIiII = O00Oo000ooO0 + "/"
     else :
      IIiII = O00Oo000ooO0
     iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = iI + '%26referer=' + IIiII
     i11Iiii ( name , url , 10 , iconimage , fanart )
    elif len ( Iii111II ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     i11Iiii ( name , Oo0o0 , 16 , iconimage , fanart )
     if 80 - 80: I1iiiiI1iII . OOo0o0
   elif '<folder>' in I1I :
    OOO0OOO00oo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( I1I )
    for name , url , iconimage , fanart in OOO0OOO00oo :
     iIo00O ( name , url , 1 , iconimage , fanart )
     if 25 - 25: Oooo0000 . i11Ii11I1Ii1i / OOoO00o . OOoOoo00oo * i1 . iiI1iIiI
   else :
    Iii111II = re . compile ( '<link>(.+?)</link>' ) . findall ( I1I )
    if len ( Iii111II ) == 1 :
     OOO0OOO00oo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( I1I )
     iiii11I = len ( i1IiIiiI )
     for name , url , iconimage , fanart in OOO0OOO00oo :
      if 'youtube.com/playlist' in url :
       iIo00O ( name , url , 2 , iconimage , fanart )
      else :
       i11Iiii ( name , url , 2 , iconimage , fanart )
    elif len ( Iii111II ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( I1I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1I ) [ 0 ]
     i11Iiii ( name , Oo0o0 , 3 , iconimage , fanart )
  except : pass
  if 59 - 59: i11Ii11I1Ii1i + OoooooooOO * Oooo0000 + i1IIi
 iii11iII ( )
 if 58 - 58: i11Ii11I1Ii1i * OOoOoo00oo * o000o0o00o0Oo / OOoOoo00oo
 if 75 - 75: OOo0o0
 if 50 - 50: OOooO / ooo0Oo0 - OOo0o0 - iI1 % OOoO00o - OOo0o0
 if 91 - 91: i1 / iI1 - i11Ii11I1Ii1i . iI1
 if 18 - 18: i1IIi11111i
 if 98 - 98: OOoO00o * OOoO00o / OOoO00o + iI1
 if 34 - 34: i1Ii
 if 15 - 15: iI1 * i1Ii * ooo0Oo0 % i11iIiiIii % Oooo0000 - OOoOoo00oo
def O0ooo0O0oo0 ( url ) :
 if 91 - 91: iIii1I11I1II1 + oOo0
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  try :
   i1i = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   iIo00O ( "[COLOR skyblue]" + i1i + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 46 - 46: oOo0 % iI1 + i1 . Oooo0000 . i1
def oO00o0 ( url ) :
 if 55 - 55: ooo0Oo0 + iIii1I11I1II1 / Oooo0000 * OOo0o0 - i11iIiiIii - OOooO
 ii1ii1ii = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 oooooOoo0ooo = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 i11Iiii ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 iI = I1i1I1II ( url )
 Iii111II = 0
 I1I1IiI1 = re . compile ( 'href="([^"]+)' ) . findall ( iI )
 for url in I1I1IiI1 :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in ii1ii1ii ) :
    Iii111II += 1
    i1i = "Link " + str ( Iii111II ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    III1iII1I1ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     i11Iiii ( "[COLOR skyblue]" + i1i + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in oooooOoo0ooo ) :
     i11Iiii ( "[COLOR yellow]" + i1i + url + "[/COLOR]" , III1iII1I1ii , 2 , I1IiI , I1ii11iIi11i )
    else :
     i11Iiii ( "[COLOR skyblue]" + i1i + url + "[/COLOR]" , III1iII1I1ii , 2 , I1IiI , I1ii11iIi11i )
     if 61 - 61: i11Ii11I1Ii1i
     if 64 - 64: i1Ii / Oooo0000 - O0 - iI1
     if 86 - 86: iI1 % Oooo0000 / iiI1iIiI / Oooo0000
def iIIi1i1 ( url ) :
 if 10 - 10: iI1
 if url == 'Football' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  OOooOO000 = I1i1I1II ( 'http://wizhdsports.is/sport/Cricket' )
 OOoOoo = dom_parser2 . parse_dom ( OOooOO000 , 'div' , { 'class' : 'card' } )
 OOoOoo = [ ( dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( oO0000OOo00 , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for oO0000OOo00 in OOoOoo ]
 if len ( OOoOoo ) < 1 :
  i11Iiii ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , OoOo , Oo , '' )
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
   iI = OOooOO000 . attrs [ 'href' ]
   iI = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + iI
   if not 'Match Over' in o00oooO0Oo :
    i11Iiii ( '[COLOR aqua]' + O0i1II1Iiii1I11 + '[COLOR yellow]' + ' ' + o00oooO0Oo + '[/COLOR]' , iI , 2 , OoOo , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( ooOOoooooo ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( II1I ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 86 - 86: Oooo0000 - OOooO - i1 * OOoO00o
def oooo0O0 ( url ) :
 if 51 - 51: i1 / i1
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i1i = re . compile ( 'title="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  if 53 - 53: ooo0Oo0
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 29 - 29: o000o0o00o0Oo + OOo0o0 % O0
 try :
  I1I11 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( iI ) [ 0 ]
  I1IiI = OoOo
  iIo00O ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1I11 , 18 , OoOo , Oo , '' )
 except : pass
 if 34 - 34: iiI1iIiI . OOoOoo00oo * o000o0o00o0Oo + oOo0
def i11111IIIII ( url , iconimage , fanart ) :
 if 19 - 19: Oooo0000 * i1IIi
 i11Iiii ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( iI )
 if 14 - 14: OOoO00o
 for Iii111II in i1IiIiiI :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  III1iII1I1ii = str . lower ( url )
  if '1e' in III1iII1I1ii :
   i1i = '1st Half'
  else :
   i1i = '2nd Half'
  i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 11 - 11: I1iiiiI1iII * iiI1iIiI . iIii1I11I1II1 % OoooooooOO + OOoO00o
def OOO ( ) :
 if 68 - 68: i11Ii11I1Ii1i + iI1
 Ii1I = 'http://www.goalsarena.org/en/'
 iI = I1i1I1II ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( i1IiIiiI )
 for OoOO000 , i1Ii11i1i in I1I1I :
  iIo00O ( "[COLOR skyblue]" + i1Ii11i1i + "[/COLOR]" , OoOO000 , 21 , I1IiI , Oo , '' )
  if 91 - 91: i1
def oOooOo0 ( url ) :
 if 38 - 38: oOo0
 if 84 - 84: iIii1I11I1II1 % OOoO00o / iIii1I11I1II1 % iI1
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O00oO = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if O00oO == 0 :
  try :
   i1IiIiiI = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in i1IiIiiI :
   ii ( oOO00oOO , i1IiIiiI , OoOo )
  OOooooO0Oo = I1i1I1II ( i1IiIiiI )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = 'https:' + url
  OO = xbmcgui . ListItem ( oOO00oOO , iconImage = OoOo , thumbnailImage = OoOo )
  xbmc . Player ( ) . play ( url , OO , False )
  quit ( 0 )
 if O00oO == 1 :
  try :
   i1IiIiiI = re . compile ( '<iframe src="(.+?)"' ) . findall ( iI ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   oOooOo0 ( url )
  OOooooO0Oo = I1i1I1II ( i1IiIiiI )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
  url = 'https:' + url
  OO = xbmcgui . ListItem ( oOO00oOO , iconImage = OoOo , thumbnailImage = OoOo )
  xbmc . Player ( ) . play ( url , OO , False )
  quit ( 0 )
  if 25 - 25: i1
def oOo0oO ( ) :
 if 51 - 51: ooo0Oo0 - OOo0o0 + i11Ii11I1Ii1i * OOooO . iI1 + OOo0o0
 Ii1I = 'http://m.liveatc.net/feeds/'
 iI = OoO0o ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://m.liveatc.net' + Ii1I
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , Ii1I , 7 , I1IiI , Oo , '' )
  if 78 - 78: OOo0o0 % O0 % OOooO
def iiI1Ii1iI1 ( url ) :
 if 87 - 87: ooo0Oo0 . I1iiiiI1iII
 if 75 - 75: i1Ii + Oooo0000 + i1IIi11111i * iI1 % OOo0o0 . OOoO00o
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 55 - 55: OOoOoo00oo . iiI1iIiI
def oOo0O0o00o ( url ) :
 url = url . replace ( ' ' , '%20' )
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li>(.+?)</a>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '(.+?)</li>' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 64 - 64: OOoOoo00oo % iIii1I11I1II1 * OOo0o0
def o0 ( url ) :
 if 37 - 37: OOo0o0 - oOo0 % ooo0Oo0
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li>(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  try :
   i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
   i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   i11Iiii ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 77 - 77: ooo0Oo0 - i1IIi - iI1 . Oooo0000
def IiI1i ( ) :
 if 92 - 92: I1iiiiI1iII . I1iiiiI1iII + i1
 iIo00O ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 Ii1I = 'http://m.broadcastify.com/?a=la&coid=1'
 iI = OoO0o ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://m.broadcastify.com' + Ii1I
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , Ii1I , 12 , I1IiI , Oo , '' )
  if 9 - 9: iiI1iIiI * O0 + I1iiiiI1iII - iI1 * oOo0
def Oooo0oOO ( url ) :
 if 81 - 81: O0 - i1Ii / i1IIi11111i % OOooO
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 83 - 83: i1Ii
def oO00Oo0O0o ( url ) :
 if 13 - 13: OoooooooOO
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 33 - 33: oOo0 + OOoO00o * OOo0o0 / iIii1I11I1II1 - iiI1iIiI
def O0oO ( url ) :
 if 73 - 73: o000o0o00o0Oo * i11iIiiIii % OOo0o0 . o000o0o00o0Oo
 iI = OoO0o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  i1IiIiiI = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( iI ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 OOOOo0 ( i1IiIiiI )
 if 49 - 49: i11Ii11I1Ii1i % O0 . Oooo0000 + OOo0o0 / iiI1iIiI
def O0oOOoOooooO ( ) :
 if 62 - 62: OoooooooOO * iiI1iIiI
 Ii1I = 'http://m.broadcastify.com/?a=top25'
 iI = OoO0o ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  oOOOoo0O0oO = i1i . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  i1i = i1i . split ( ')' ) [ - 1 ] . strip ( )
  Ii1I = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://m.broadcastify.com' + Ii1I
  i11Iiii ( "[COLOR aqua]" + i1i + "[COLOR yellow] :: " + oOOOoo0O0oO + " Listening" + "[/COLOR]" , Ii1I , 14 , I1IiI , Oo , '' )
  if 6 - 6: OOoOoo00oo * i1IIi11111i + OOoO00o
def I1IIIiIiI1 ( url ) :
 if 28 - 28: iIii1I11I1II1 % ooo0Oo0 * iiI1iIiI % OOooO * i1IIi11111i / i1IIi11111i
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ]
  i1i = iIIII ( i1i )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( Iii111II ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in i1i :
    III1iII1I1ii = 'https://www.youtube.com' + url
    i11Iiii ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , III1iII1I1ii , 2 , I1IiI , I1ii11iIi11i )
    if 33 - 33: i1Ii . i11Ii11I1Ii1i % OOoO00o + i1IIi11111i
def oO00O000oO0 ( ) :
 if 79 - 79: iI1 - OoooooooOO - OOo0o0 - iIii1I11I1II1 * OOoOoo00oo
 Ii1I = 'http://burningwhee1s.blogspot.co.uk/'
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( i1IiIiiI )
 for iI , i1i in I1I1I :
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , iI , 24 , I1IiI , Oo , '' )
  if 4 - 4: i11iIiiIii . OoooooooOO / i1 % oOo0 % iI1 * O0
def iIIii ( url ) :
 if 92 - 92: OOooO + OOo0o0 % OOoOoo00oo
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( Iii111II ) [ 0 ]
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 62 - 62: o000o0o00o0Oo / i1IIi
def oo0oO ( url , iconimage ) :
 if 94 - 94: iIii1I11I1II1 / ooo0Oo0 % OOoO00o * OOoO00o * i11Ii11I1Ii1i
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( i1IiIiiI )
 try :
  for Iii111II in I1I1I :
   i1i = re . compile ( '<b>(.+?)</b>' ) . findall ( Iii111II ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    IIiIiI = re . compile ( '<b>(.+?)</b>' ) . findall ( Iii111II ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     IIiIiI = re . compile ( '<b>(.+?)</b>' ) . findall ( Iii111II ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     IIiIiI = ''
   i1i = iIIII ( i1i )
   IIiIiI = iIIII ( IIiIiI )
   OOOIIiI1i1i = re . compile ( '<option value="(.+?)"' ) . findall ( Iii111II ) [ 1 ]
   i11Iiii ( "[COLOR aqua]" + i1i + "  " + IIiIiI + "[/COLOR]" , OOOIIiI1i1i , 2 , I1IiI , Oo , '' )
 except :
  i11Iiii ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 56 - 56: oOo0 + Oooo0000 * i1Ii / OOo0o0 / O0 * o000o0o00o0Oo
def O0o0o00OO0000 ( ) :
 if 1 - 1: i1Ii . i1Ii / Oooo0000 - oOo0
 if 86 - 86: iIii1I11I1II1 / Oooo0000 . i11Ii11I1Ii1i
 Ii1I = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 iI = I1i1I1II ( Ii1I )
 OOO0OOO00oo = json . loads ( iI )
 II1i111Ii1i = OOO0OOO00oo [ 'results' ]
 for iii1 in II1i111Ii1i :
  ooO0oooOO0 = 'https://image.tmdb.org/t/p/w640'
  i1i = iii1 [ 'title' ]
  I1IiI = iii1 [ 'poster_path' ]
  o0o = iii1 [ 'id' ]
  I1IiI = ooO0oooOO0 + I1IiI
  I1ii11iIi11i = iii1 [ 'backdrop_path' ]
  I1ii11iIi11i = ooO0oooOO0 + I1ii11iIi11i
  oo0 = iii1 [ 'overview' ]
  o0o = str ( o0o )
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , i1i , 33 , I1IiI , I1ii11iIi11i , oo0 )
  if 61 - 61: Oooo0000 - OOoOoo00oo - i1IIi
def IiI1iIiIIIii ( url ) :
 if 53 - 53: i1IIi
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i1i = re . compile ( '<i>(.+?)</i>' ) . findall ( Iii111II ) [ 0 ]
  i1i = i1i . strip ( )
  iIo00O ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o0OOOoO0 = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( iI ) [ 0 ]
  o0OoOo00o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  iIo00O ( '[COLOR yellow]Next Page >>[/COLOR]' , o0OOOoO0 , 26 , o0OoOo00o0o , I1ii11iIi11i )
 except : pass
 if 41 - 41: i1Ii % i1 - ooo0Oo0 * oOo0 * ooo0Oo0
def OOOoOO0o ( url , iconimage ) :
 if 1 - 1: i11Ii11I1Ii1i
 iI = I1i1I1II ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( iI ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 i1IiIiiI = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( iI )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 oO0000OOo00 = 1
 O0oOo00o = [ ]
 for Iii111II in i1IiIiiI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  O0oOo00o . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( oO0000OOo00 ) )
  time . sleep ( 0.02 )
  oO0000OOo00 += 1
  i1i = re . compile ( '(.+?)</p>' ) . findall ( Iii111II ) [ 0 ] . replace ( 'Server' , '' )
  i1i = i1i . strip ( )
 o0ooooO0o0O = 1
 oo0oooooO0 = 0
 iiIi11iI1iii = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 67 - 67: O0 / oOo0
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if oo0oooooO0 > len ( O0oOo00o ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 88 - 88: i1 - i1Ii + OOoOoo00oo * iiI1iIiI % iIii1I11I1II1 + ooo0Oo0
  if iiIi11iI1iii == 0 :
   oo0oooooO0 += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( oo0oooooO0 ) + "[/COLOR]" , '' )
   try :
    iI = I1i1I1II ( O0oOo00o [ oo0oooooO0 ] )
    I1I1I = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( iI ) [ 0 ]
    oo000O0OoooO = base64 . b64decode ( I1I1I )
    url = re . compile ( 'src="(.+?)"' ) . findall ( oo000O0OoooO ) [ 0 ]
    O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    I1i11II1i = open ( O0o ) . read ( )
    o0o0OoOo0O0OO = re . compile ( '<url>(.+?)</url>' ) . findall ( I1i11II1i )
    for iIi1I11I in o0o0OoOo0O0OO :
     Iii1 = re . compile ( '<bad>(.+?)<bad>' ) . findall ( iIi1I11I ) [ 0 ]
     if url == Iii1 :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( oo0oooooO0 ) )
      time . sleep ( 0.5 )
      iiIi11iI1iii = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     ooO = liveresolver . resolve ( url )
    else : ooO = url
    OO = xbmcgui . ListItem ( oOO00oOO , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( ooO , OO , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( oo0oooooO0 ) )
    time . sleep ( 0.5 )
    iiIi11iI1iii = 5
    pass
  if iiIi11iI1iii == 5 :
   iiIi11iI1iii = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   iiIi11iI1iii += 1
   if 84 - 84: OOoOoo00oo - OOoO00o / i1Ii
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 O00Oo000ooO0 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if O00Oo000ooO0 :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( O0o , "a" ) as o0o0 :
   o0o0 . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 49 - 49: OOo0o0 - i11iIiiIii . oOo0 * OOooO % OOoO00o + i1IIi
def oOO0OOOo ( url ) :
 if 56 - 56: i1IIi11111i
 if 28 - 28: OOoO00o . OOoO00o % iIii1I11I1II1 * iIii1I11I1II1 . i1IIi11111i / OOoO00o
 if url == 'search' :
  iII1i1 = ''
  O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , 'Enter Search Term' )
  O0oOOoooOO0O . doModal ( )
  if O0oOOoooOO0O . isConfirmed ( ) :
   iII1i1 = O0oOOoooOO0O . getText ( )
   if len ( iII1i1 ) > 1 :
    ooo00Ooo = iII1i1 . lower ( )
    if 93 - 93: i11iIiiIii - iiI1iIiI * o000o0o00o0Oo * iI1 % O0 + OoooooooOO
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , OoOo , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , OoOo , 5000 )
   quit ( )
  ooo00Ooo = ooo00Ooo . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + ooo00Ooo + '.html'
  I1i1i1 ( url , I1IiI )
  if 73 - 73: O0 * OOoO00o + OOooO + i1Ii
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  I1i1i1 ( url , I1IiI )
  if 40 - 40: i11Ii11I1Ii1i . Oooo0000 * oOo0 + OOoOoo00oo + OOoOoo00oo
def I1i1i1 ( url , icon ) :
 if 9 - 9: iI1 % OoooooooOO . OOo0o0 % iI1
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i1i = re . compile ( '<i>(.+?)</i>' ) . findall ( Iii111II ) [ 0 ]
  i1i = iIIII ( i1i )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  iIo00O ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 32 - 32: i11iIiiIii
def iiiII ( ) :
 if 41 - 41: ooo0Oo0
 Ii1I = 'http://www.genti.stream/'
 iI = I1i1I1II ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  IIiIi = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ] . strip ( )
  OOoOooOoOOOoo = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( Iii111II ) [ 1 ] . strip ( )
  Ii1I = re . compile ( 'href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://www.genti.stream/' + Ii1I
  i11Iiii ( "[COLOR aqua]" + IIiIi + "[COLOR yellow] vs [COLOR aqua]" + OOoOooOoOOOoo + "[/COLOR]" , Ii1I , 39 , I1IiI , I1ii11iIi11i )
  if 25 - 25: OoooooooOO - iiI1iIiI . iiI1iIiI * OOo0o0
def o000oo ( url ) :
 if 95 - 95: i1Ii / i1Ii
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIiI1Ii = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( iI ) [ 0 ]
 if not 'http' in IIiI1Ii :
  IIiI1Ii = 'http://www.genti.stream' + IIiI1Ii
 OoOO000 = I1i1I1II ( IIiI1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0O0O0Oo = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OoOO000 ) [ 0 ]
 OOooooO0Oo = I1i1I1II ( O0O0O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
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
 if 70 - 70: i1 % OOo0o0 + OOoOoo00oo / OOooO % O0
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , OoOo , 5000 )
  quit ( )
 ii ( oOO00oOO , url , OoOo )
 if 100 - 100: i1IIi11111i + OOoOoo00oo * i1IIi11111i
 if 80 - 80: i1IIi11111i * O0 - OOooO
def oo00O00Oo ( url ) :
 if 26 - 26: o000o0o00o0Oo - i1 - OOooO + o000o0o00o0Oo
 ooI1i = cfscrape . create_scraper ( )
 Oo0o0 = ooI1i . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( Oo0o0 ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1IiIiiI )
 for url , i1i in I1I1I :
  url = 'http://kimcartoon.me/CartoonList' + url
  iIo00O ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 32 - 32: Oooo0000 / i1 + OOoOoo00oo
def ii1I1i1iiiI ( url ) :
 if 96 - 96: OoooooooOO + OOo0o0
 ooI1i = cfscrape . create_scraper ( )
 Oo0o0 = ooI1i . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( Oo0o0 )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   iiII1i11i = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( Iii111II ) [ 0 ]
   iiII1i11i = iIIII ( iiII1i11i )
  except IndexError :
   iiII1i11i = ''
  iIo00O ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , iiII1i11i )
  if 11 - 11: iiI1iIiI / i11Ii11I1Ii1i + i1IIi11111i * o000o0o00o0Oo - o000o0o00o0Oo - iiI1iIiI
 try :
  O0oOooooo0O = re . compile ( '<li>(.+?)Next' ) . findall ( Oo0o0 )
  for Iii111II in O0oOooooo0O :
   o0OOOoO0 = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ - 1 ]
   iiI1I1 = 'http://kimcartoon.me' + o0OOOoO0
   ooOii = 'https://i.imgur.com/mjCRjXT.png'
   iIo00O ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , iiI1I1 , 30 , ooOii , I1ii11iIi11i )
 except : pass
 if 82 - 82: Oooo0000 - i1 % Oooo0000 * i11iIiiIii . i11Ii11I1Ii1i % i11Ii11I1Ii1i
def o00Ooo0 ( url ) :
 if 83 - 83: i11iIiiIii % i1IIi11111i % i1Ii
 ooI1i = cfscrape . create_scraper ( )
 Oo0o0 = ooI1i . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<td>(.+?)</td>' ) . findall ( Oo0o0 )
 for Iii111II in i1IiIiiI :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
   i1i = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   i11Iiii ( "[COLOR aqua][B]" + i1i + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 11 - 11: i11Ii11I1Ii1i % i1 * OOoO00o + i1Ii + OOooO
def II1Iiiiii ( url ) :
 if 36 - 36: iiI1iIiI - iI1
 O00oO = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if O00oO == 0 :
  url = url + '&s=rapidvideo'
  ooI1i = cfscrape . create_scraper ( )
  Oo0o0 = ooI1i . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1I1I = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( Oo0o0 )
   for iI in I1I1I :
    url = re . compile ( 'src="(.+?)"' ) . findall ( iI ) [ 0 ]
    if 'rapidvideo' in url :
     ii ( oOO00oOO , url , OoOo )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if O00oO == 1 :
  url = url + '&s=openload'
  ooI1i = cfscrape . create_scraper ( )
  Oo0o0 = ooI1i . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1I1I = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( Oo0o0 )
   for iI in I1I1I :
    url = re . compile ( 'src="(.+?)"' ) . findall ( iI ) [ 0 ]
    ii ( oOO00oOO , url , OoOo )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 29 - 29: i1Ii * OOoOoo00oo
   if 10 - 10: oOo0 % I1iiiiI1iII * I1iiiiI1iII . iI1 / OOooO % OOoOoo00oo
def IIII1 ( ) :
 if 10 - 10: oOo0 / i1Ii + i11iIiiIii / OOooO
 Ii1I = "http://www.loyalbooks.com/genre-menu"
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( iI )
 for I1I in i1IiIiiI :
  if "paid" not in I1I :
   OoOO000 = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
   OOooooO0Oo = "http://www.loyalbooks.com" + OoOO000
   oOO00oOO = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
   iIo00O ( "[COLOR aqua]" + oOO00oOO + "[/COLOR]" , OOooooO0Oo , 60 , I1IiI , Oo , '' )
   if 74 - 74: OOoOoo00oo + O0 + i1IIi - i1IIi + i11Ii11I1Ii1i
def oOOO0oo0 ( url ) :
 if 46 - 46: I1iiiiI1iII
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( iI ) [ 0 ]
 ii1iIi1iIiI1i = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( i1IiIiiI )
 for I1I in ii1iIi1iIiI1i :
  III1iII1I1ii = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  OOooooO0Oo = "http://www.loyalbooks.com" + III1iII1I1ii
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  OoOo = "http://www.loyalbooks.com" + I1IiI
  oOO00oOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  iIo00O ( "[COLOR aqua]" + oOO00oOO + "[/COLOR]" , OOooooO0Oo , 61 , OoOo , Oo , '' )
 try :
  iI = I1i1I1II ( url )
  I1I11 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( iI ) [ 0 ]
  I1IiI = 'https://i.imgur.com/mjCRjXT.png'
  iIo00O ( "[COLOR yellow]Next Page -->[/COLOR]" , I1I11 , 60 , I1IiI , Oo , '' )
 except : pass
 if 40 - 40: i1IIi % OOoOoo00oo
 if 71 - 71: Oooo0000
def ii111IiiI1 ( name , url , iconimage ) :
 if 11 - 11: iIii1I11I1II1 * OOooO
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( iI )
 for I1I in i1IiIiiI :
  i1i = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  III1iII1I1ii = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( I1I ) [ 0 ]
  i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , III1iII1I1ii , 10 , iconimage , Oo , '' )
  if 76 - 76: i1Ii
def IIIiI11ii1I ( ) :
 if 39 - 39: iIii1I11I1II1 / O0 / OOo0o0 - OOooO - OOoO00o % OOoOoo00oo
 Ii1I = 'http://www.shadownet.me/'
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1IiIiiI )
 for Ii1I , i1i in I1I1I :
  i1i = iIIII ( i1i )
  if 'P2P' not in i1i :
   iIo00O ( "[COLOR skyblue]" + i1i + "[/COLOR]" , Ii1I , 49 , I1IiI , Oo , '' )
   if 31 - 31: iI1 - O0 / i1Ii * Oooo0000
   if 12 - 12: i1IIi11111i - i1Ii * oOo0
def II1111ii ( url ) :
 if 27 - 27: O0
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( i1IiIiiI )
 for Iii111II in I1I1I :
  i1i = re . compile ( 'alt="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i11Iiii ( "[COLOR skyblue]" + i1i + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o0OOOoO0 = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( iI ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  iIo00O ( "[COLOR orange]Next Page --->[/COLOR]" , o0OOOoO0 , 49 , I1IiI , Oo , '' )
 except : pass
 if 79 - 79: i1IIi11111i - iI1 + i1IIi11111i . OOo0o0
def ii1III11 ( url ) :
 if 7 - 7: OOoO00o % O0 . Oooo0000 + iiI1iIiI - iI1
 def o0o0O00oo0 ( url ) :
  Ii1ii1IiIII = urllib2 . Request ( url )
  Ii1ii1IiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ii1ii1IiIII . add_header ( 'Referer' , url )
  ooO0o = urllib2 . urlopen ( Ii1ii1IiIII , timeout = 5 )
  iI = ooO0o . read ( )
  ooO0o . close ( )
  return iI
  if 51 - 51: I1iiiiI1iII
 iI = o0o0O00oo0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  i1IiIiiI = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( iI ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in i1IiIiiI :
  url = i1IiIiiI
  ii ( oOO00oOO , url , OoOo )
 OOooooO0Oo = o0o0O00oo0 ( i1IiIiiI )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( OOooooO0Oo ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 25 - 25: OoooooooOO + I1iiiiI1iII * o000o0o00o0Oo
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
  OO = xbmcgui . ListItem ( oOO00oOO , iconImage = OoOo , thumbnailImage = OoOo )
  OO . setPath ( ooO )
  xbmc . Player ( ) . play ( ooO , OO , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  OO = xbmcgui . ListItem ( oOO00oOO , iconImage = OoOo , thumbnailImage = OoOo )
  OO . setPath ( ooO )
  xbmc . Player ( ) . play ( ooO , OO , False )
 else :
  if '.m3u8' in url :
   III1iII1I1ii = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + oOO00oOO + '&amp;url=' + url + '&amp;iconImage=' + OoOo
  elif '.ts' in url :
   III1iII1I1ii = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + oOO00oOO + '&amp;url=' + url + '&amp;iconImage=' + OoOo
  else :
   III1iII1I1ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 92 - 92: iiI1iIiI + iI1 + O0 / i1IIi11111i + oOo0
  OO = xbmcgui . ListItem ( oOO00oOO , iconImage = OoOo , thumbnailImage = OoOo )
  OO . setPath ( url )
  if 18 - 18: i1Ii * Oooo0000 . OOoO00o / o000o0o00o0Oo / i11iIiiIii
  xbmc . Player ( ) . play ( III1iII1I1ii , OO , False )
  if 21 - 21: OOo0o0 / o000o0o00o0Oo + OOooO + OoooooooOO
  if 91 - 91: i11iIiiIii / i1IIi + OOoO00o + i1Ii * i11iIiiIii
def OoOoOo00o0 ( ) :
 if 90 - 90: ooo0Oo0 % O0 * iIii1I11I1II1 . OOoO00o
 Ii1I = 'https://m.skylinewebcams.com/en/webcam'
 iI = I1i1I1II ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I1I = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 I1iii11 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I1I )
 for Ii1I , i1i in I1iii11 :
  if 'http|https' not in Ii1I :
   Ii1I = 'https://m.skylinewebcams.com' + Ii1I
   iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , Ii1I , 46 , I1IiI , Oo , '' )
   if 74 - 74: O0 / i1IIi
def OoO ( url ) :
 if 41 - 41: i1IIi * i11Ii11I1Ii1i / OoooooooOO . OOoOoo00oo
 iI = I1i1I1II ( url )
 I1I1I = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( iI )
 for url , I1IiI , i1i in I1I1I :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 83 - 83: OOoO00o . O0 / ooo0Oo0 / OOoOoo00oo - i11Ii11I1Ii1i
  if 100 - 100: i1
def II1i ( name , url , iconimage ) :
 if 2 - 2: iIii1I11I1II1 * ooo0Oo0 % OOo0o0 - i11Ii11I1Ii1i - OOoO00o
 iI = I1i1I1II ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  i1IiIiiI = re . compile ( '<amp-video src="(.+?)"' ) . findall ( iI ) [ 0 ]
  url = 'https:' + i1IiIiiI
  OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , OO , False )
  if 3 - 3: oOo0
 except : pass
 quit ( 0 )
 if 45 - 45: oOo0
def oO ( ) :
 if 17 - 17: ooo0Oo0 % OOoOoo00oo . i1IIi / OoooooooOO
 Ii1I = 'http://www.watchepisodeseries.com/home/schedule'
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( i1IiIiiI )
 for Ii1I , IIiIiiii , O0000OOO0 in I1I1I :
  iIo00O ( "[COLOR aqua]" + IIiIiiii + "  " + O0000OOO0 + "[/COLOR]" , Ii1I , 67 , I1IiI , I1ii11iIi11i )
  if 51 - 51: iiI1iIiI / I1iiiiI1iII / OOooO
  if 6 - 6: OOooO - i1Ii * OOoOoo00oo . OOoO00o / O0 * i1Ii
def II11iI111i1 ( url ) :
 if 95 - 95: OoooooooOO - I1iiiiI1iII * iiI1iIiI + Oooo0000
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 1 ]
  i1i = iIIII ( i1i )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  OoOo = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( Iii111II ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( Iii111II ) [ 0 ]
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 68 , OoOo , I1ii11iIi11i )
  if 10 - 10: i1IIi11111i / i11iIiiIii
  if 92 - 92: iI1 . oOo0
def oOO00O0Ooooo00 ( url , iconimage , fanart ) :
 if 97 - 97: i1Ii / oOo0 % i1IIi % o000o0o00o0Oo
 iI = I1i1I1II ( url )
 ii111I11iI = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( iI )
 for Iii111II in ii111I11iI :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
 i1IiIiiI = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( iI )
 oO0000OOo00 = datetime . now ( )
 for Iii111II in i1IiIiiI :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
   i1i = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ]
   i1i = iIIII ( i1i )
   OO0o = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ]
   oo0o0O0Oooooo = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ]
   IIiIiiii = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in IIiIiiii :
    IIiIiiii = IIiIiiii . strip ( )
    IIiIiiii = time . strptime ( IIiIiiii , "%d/%m/%Y" )
    i11IIIiI1I = ( "%s/%s/%s" % ( oO0000OOo00 . day , oO0000OOo00 . month , oO0000OOo00 . year ) )
    i11IIIiI1I = time . strptime ( i11IIIiI1I , "%d/%m/%Y" )
    if ( i11IIIiI1I < IIiIiiii ) :
     i1i = '[COLOR yellow]' + ( i1i ) + ' - Not Aired Yet' + '[/COLOR]'
     oo0o0O0Oooooo = '[COLOR yellow]' + ( oo0o0O0Oooooo ) + '[/COLOR]'
     OO0o = '[COLOR yellow]' + ( OO0o ) + '[/COLOR]'
     if 69 - 69: O0
    if not 'Season 0' in OO0o :
     iIo00O ( "[COLOR aqua]" + OO0o + " " + oo0o0O0Oooooo + " " + i1i + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 85 - 85: i1Ii / O0
  if 18 - 18: i1IIi11111i % O0 * o000o0o00o0Oo
def o0Iii ( url , iconimage , fanart ) :
 if 19 - 19: iI1 % i11Ii11I1Ii1i / i11iIiiIii / OOoO00o - OoooooooOO
 if 37 - 37: OOoOoo00oo / OoooooooOO - i11iIiiIii
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  try :
   i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
   i1i = i1i . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
   if not 'Lolzor.Com' in i1i :
    if not 'Videoplayer.Gq' in i1i :
     if not 'Vidbaba.Com' in i1i :
      if not 'Gagomatic.Com' in i1i :
       if not 'Favour.Me' in i1i :
        if not 'Funblr.Com' in i1i :
         if not 'Vid.Ag' in i1i :
          if not 'Mycollection.Net' in i1i :
           if not 'Adhqmedia.Com' in i1i :
            if not 'Filenuke.Com' in i1i :
             if not 'Mrfile.Me' in i1i :
              i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 18 - 18: OOoO00o . iiI1iIiI
  if 40 - 40: O0 - OoooooooOO - I1iiiiI1iII
def iIiii ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  url = re . compile ( 'href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    ooO = liveresolver . resolve ( url )
   else : ooO = url
   OO = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   OO . setPath ( ooO )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO )
   xbmc . Player ( ) . play ( ooO )
   if 76 - 76: iiI1iIiI . i1Ii - o000o0o00o0Oo - OOoO00o * i1
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 54 - 54: I1iiiiI1iII + O0 + iI1 * oOo0 - OOoOoo00oo % OOo0o0
def I111 ( ) :
 if 13 - 13: i1 * OOo0o0 * OOoO00o
 iII1i1 = ''
 O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , 'Enter Search Term' )
 O0oOOoooOO0O . doModal ( )
 if O0oOOoooOO0O . isConfirmed ( ) :
  iII1i1 = O0oOOoooOO0O . getText ( )
  if len ( iII1i1 ) > 1 :
   ooo00Ooo = iII1i1 . lower ( )
   ooo00Ooo = ooo00Ooo . replace ( ' ' , '%20' )
   if 26 - 26: O0 * ooo0Oo0 + i11Ii11I1Ii1i / I1iiiiI1iII + OOo0o0 % i1IIi11111i
  else : quit ( )
 else : ooo00Ooo = urllib . unquote_plus ( Ii1I ) . lower ( ) ; iII1i1 = urllib . unquote_plus ( Ii1I )
 Ii1I = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + ooo00Ooo
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '"series"(.+?)"series_id"' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( 'original_name":"(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  III1iII1I1ii = re . compile ( '"seo_name":"(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://www.watchepisodeseries.com/' + III1iII1I1ii
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + III1iII1I1ii + '.jpg'
  iIo00O ( i1i , Ii1I , 68 , I1IiI , I1ii11iIi11i , '' )
  if 42 - 42: o000o0o00o0Oo . oOo0 % oOo0
def oOOOO ( ) :
 if 49 - 49: i11Ii11I1Ii1i . OOo0o0 . i11iIiiIii % I1iiiiI1iII
 Ii1I = 'http://www.watchepisodeseries.com/home/popular-series'
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<div title="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i1i = iIIII ( i1i )
  Ii1I = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( Iii111II ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( Iii111II ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  iIo00O ( '[COLOR aqua]' + i1i + '[/COLOR]' , Ii1I , 68 , I1IiI , I1ii11iIi11i )
  if 34 - 34: oOo0 % I1iiiiI1iII
  if 3 - 3: i11Ii11I1Ii1i / OOoOoo00oo + I1iiiiI1iII . i1Ii . i1
def oOoo000 ( ) :
 if 87 - 87: OoooooooOO - i1IIi11111i / I1iiiiI1iII . i11iIiiIii * OoooooooOO
 try :
  OO00 = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iII1i1 = ''
  O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  O0oOOoooOO0O . doModal ( )
  if O0oOOoooOO0O . isConfirmed ( ) :
   iII1i1 = O0oOOoooOO0O . getText ( )
   if len ( iII1i1 ) > 1 :
    ooo00Ooo = iII1i1
   else : quit ( )
  if ooo00Ooo == OO00 :
   IIiiIIi1 ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  iII1i1 = ''
  O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , 'Enter The Password You Set' )
  O0oOOoooOO0O . doModal ( )
  if O0oOOoooOO0O . isConfirmed ( ) :
   iII1i1 = O0oOOoooOO0O . getText ( )
   if len ( iII1i1 ) > 1 :
    ooo00Ooo = iII1i1
   else : quit ( )
  with open ( i1i1II , "w" ) as o0o0 :
   o0o0 . write ( ooo00Ooo )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 59 - 59: I1iiiiI1iII . OOoOoo00oo % i11Ii11I1Ii1i
   if 39 - 39: o000o0o00o0Oo
   if 97 - 97: OOoOoo00oo - i1 / OOooO . i11iIiiIii % OOo0o0 * OOo0o0
def IIiiIIi1 ( ) :
 if 1 - 1: iiI1iIiI % i1Ii
 oOoO00 = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 iI1IIIii = '[COLOR aqua]Asian Special Porn[/COLOR]'
 iIo00O ( iI1IIIii , oOoO00 , 1 , I1IiI , Oo , '' )
 Ii1I = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 iI = I1i1I1II ( Ii1I )
 i1IiIiiI = re . compile ( '<li class="">(.+?)</li>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<strong>(.+?)</strong>' ) . findall ( Iii111II ) [ 0 ]
  I1i11ii11 = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( Iii111II ) [ 0 ]
  III1iII1I1ii = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'https://www.eporner.com' + III1iII1I1ii
  if not 'All' in i1i :
   if not 'Homemade' in i1i :
    iIo00O ( "[COLOR aqua]" + i1i + "  " + "[COLOR yellow]" + I1i11ii11 + "[/COLOR]" , Ii1I , 36 , I1IiI , Oo , '' )
    if 81 - 81: OOoOoo00oo - iI1 % i1Ii - i1 / ooo0Oo0
def Ii1iI111 ( url ) :
 if 51 - 51: I1iiiiI1iII * O0 / i11Ii11I1Ii1i . OOooO % OOoOoo00oo / iiI1iIiI
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( 'title="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  III1iII1I1ii = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = 'https://www.eporner.com' + III1iII1I1ii
  iIo00O ( "[COLOR skyblue]" + i1i + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 9 - 9: iiI1iIiI % iiI1iIiI % i11Ii11I1Ii1i
 try :
  o0OOOoO0 = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( iI ) [ 0 ]
  I1I11 = 'https://www.eporner.com' + o0OOOoO0
  o0OoOo00o0o = 'http://imgur.com/3eNoY0p'
  iIo00O ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1I11 , 36 , o0OoOo00o0o , Oo , '' )
 except : pass
 if 30 - 30: I1iiiiI1iII + oOo0 - I1iiiiI1iII . I1iiiiI1iII - i11Ii11I1Ii1i + O0
def oOO0 ( url , iconimage ) :
 if 46 - 46: OOooO % Oooo0000
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 ooo0o0O0o = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( ooo0o0O0o )
 for O0OooO , iI in I1I1I :
  O0OooO = O0OooO . replace ( ':' , '' )
  url = 'https://www.eporner.com' + iI
  i11Iiii ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + O0OooO + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 2 - 2: OoooooooOO % OOoOoo00oo
def oOoOOo0oo0 ( url ) :
 if 60 - 60: i1Ii * oOo0 + ooo0Oo0
 i11Iiii ( "[COLOR yellow]Anime Catergories[/COLOR]" , url , 999 , I1IiI , Oo , '' )
 iI = I1i1I1II ( url )
 i1IiIiiI = re . compile ( '<ul class="nav nav-pills nav-stacked"><li>(.+?)</ul>' ) . findall ( iI ) [ 1 ]
 I1I1I = re . compile ( '<a href="(.+?)" title="(.+?)">.+?</a>' ) . findall ( i1IiIiiI )
 for url , i1i in I1I1I :
  i1i = i1i . strip ( )
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 52 , I1IiI , Oo , '' )
  if 19 - 19: i1 * iI1 / iI1 . OoooooooOO - OOoOoo00oo + i11iIiiIii
def oo0OOo0O ( url ) :
 if 39 - 39: OoooooooOO + OOo0o0 % OOoOoo00oo / OOoOoo00oo
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IiIiiI = re . compile ( '<th class="st-sort-descent">(.+?)</table>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '<a href="(.+?)".+?>(.+?)</a>' ) . findall ( i1IiIiiI )
 for url , i1i in I1I1I :
  iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 27 - 27: OOoO00o . iI1 . iIii1I11I1II1 . iIii1I11I1II1
def iIi1i ( url ) :
 if 4 - 4: oOo0 / i11iIiiIii / OOoOoo00oo
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1IiI = re . compile ( '''<div class=\"col-md-3\">.+?url\('(.+?)'\)''' ) . findall ( iI ) [ 0 ]
 except :
  I1IiI = OoOo
 i1IiIiiI = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( iI ) [ 0 ]
 I1I1I = re . compile ( '''<a class="black" href='(.+?)'>(.+?)</a>''' ) . findall ( i1IiIiiI )
 i11Iiii ( "[COLOR yellow]Links Can Take Up To 45 Secs To Play, Be Patient![/COLOR]" , url , 54 , I1IiI , Oo , '' )
 for url , i1i in I1I1I :
  i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  if 91 - 91: iIii1I11I1II1 % i1IIi11111i . iIii1I11I1II1 % i1IIi / i11Ii11I1Ii1i * Oooo0000
def iioo0o0OoOOO ( url , iconimage ) :
 if 88 - 88: OOoO00o
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOOIIiI1i1i = re . compile ( '<source src="(.+?)"' ) . findall ( iI ) [ 0 ]
 ii ( oOO00oOO , OOOIIiI1i1i , iconimage )
 if 19 - 19: i11Ii11I1Ii1i * I1iiiiI1iII + OOooO
 if 65 - 65: OOoOoo00oo . oOo0 . i1 . OOoO00o - OOoOoo00oo
 if 19 - 19: i11iIiiIii + OOoO00o % i1Ii
 if 14 - 14: i1 . i11Ii11I1Ii1i . iI1 / OOooO % o000o0o00o0Oo - i1Ii
 if 67 - 67: iI1 - OOoOoo00oo . i1IIi
 if 35 - 35: OOoO00o + i1Ii - OOo0o0 . OOoO00o . I1iiiiI1iII
 if 87 - 87: Oooo0000
 if 25 - 25: i1IIi . i1 - Oooo0000 / i1 % i1 * iIii1I11I1II1
def III ( url ) :
 if 1 - 1: OOo0o0
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( 'title="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ] . replace ( './' , '/' )
  if 62 - 62: i1IIi - OOoOoo00oo
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  O0OooO = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( Iii111II ) [ 0 ]
  iIo00O ( "[COLOR aqua]" + i1i + "[COLOR yellow] " + O0OooO + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 96 - 96: i1IIi . o000o0o00o0Oo + OOo0o0
 try :
  I1I11 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( iI ) [ 0 ]
  o0OOOoO0 = re . compile ( '<a.+?href="(.+?)"' ) . findall ( I1I11 ) [ 5 ]
  Ii1iI11iI1 = 'http://m4ufree.com' + o0OOOoO0
  if 'genre' in Ii1iI11iI1 :
   Ii1iI11iI1 = Ii1iI11iI1 . replace ( '.com' , '.com/' )
  i11 = 'https://i.imgur.com/mjCRjXT.png'
  iIo00O ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , Ii1iI11iI1 , 42 , i11 , Oo , '' )
 except : pass
 if 11 - 11: oOo0 / Oooo0000 + iI1 % iIii1I11I1II1
def II1II1iIIi11 ( url , iconimage ) :
 if 49 - 49: OoooooooOO * iI1 - ooo0Oo0 . OOo0o0
 import requests
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O000o0 = re . compile ( 'data="(.+?)"' ) . findall ( iI ) [ 0 ]
 oO0 = 'http://m4ufree.com/ajax_new.php'
 o000OoOoO0 = requests . post ( oO0 , data = { 'm4u' : O000o0 } )
 json = ( o000OoOoO0 . text )
 OO0ooOOO0O00o = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 Ooo0o0oo = re . compile ( '{(.+?)}' ) . findall ( OO0ooOOO0O00o )
 Ii1i1i1111 = 0
 for oO0000OOo00 in Ooo0o0oo :
  try :
   Ii1i1i1111 += 1
   i1i = 'Link ' + str ( Ii1i1i1111 )
   O0OooO = re . compile ( '''"label":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( oO0000OOo00 ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   i11Iiii ( "[COLOR aqua]" + i1i + " | [COLOR yellow] " + O0OooO + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( oO0000OOo00 ) [ 0 ]
   url = 'http://m4ufree.com/' + url
   O0OooO = re . compile ( """label:.+?'(.+?)'""" ) . findall ( oO0000OOo00 ) [ 0 ]
   i11Iiii ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + O0OooO + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 57 - 57: OOooO % i11Ii11I1Ii1i
def O00oOo ( ) :
 if 26 - 26: I1iiiiI1iII % oOo0 % OOo0o0 % OOooO
 Ii1I = 'https://www.livefootballol.me/acestream-channel-list-2017.html'
 iI = I1i1I1II ( Ii1I )
 I1I1I = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI )
 for O0oo0ooOOOO in I1I1I :
  i1i = re . compile ( '<strong>(.+?)</strong>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
  if len ( i1i ) == 1 or '&nbsp;' in i1i :
   i1i = re . compile ( '<strong>(.+?)</strong>' ) . findall ( O0oo0ooOOOO ) [ 1 ]
  if len ( i1i ) > 40 :
   i1i = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
  Ii1I = re . compile ( '<td>(.+?)</td>' ) . findall ( O0oo0ooOOOO ) [ 2 ]
  Ii1ii = re . compile ( '<td>(.+?)</td>' ) . findall ( O0oo0ooOOOO ) [ 3 ]
  iIIIII1iiiiII = re . compile ( '<td>(.+?)</td>' ) . findall ( O0oo0ooOOOO ) [ 4 ]
  i1i = i1i . strip ( )
  Ii1I = Ii1I . strip ( )
  i11Iiii ( "[COLOR aqua]" + i1i + ' :: [COLOR yellow]' + Ii1ii + '[COLOR aqua] :: [COLOR yellow]' + iIIIII1iiiiII + ' Kbps[/COLOR]' , Ii1I , 2 , OoOo , Oo , '' )
  if 54 - 54: i1IIi
def ii1I11 ( ) :
 if 99 - 99: OOoOoo00oo
 Ii1I = 'http://acestreamchannel.blogspot.co.uk/'
 iI = I1i1I1II ( Ii1I )
 I1I1I = re . compile ( '<tr>(.+?)</tr>' ) . findall ( iI )
 for Iii111II in I1I1I :
  try :
   i1i = re . compile ( '<td>(.+?)</td>' ) . findall ( Iii111II ) [ 0 ]
   if len ( i1i ) < 40 :
    Ii1I = re . compile ( 'href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
    i11Iiii ( "[COLOR aqua]" + i1i + "[/COLOR]" , Ii1I , 2 , OoOo , Oo , '' )
  except : pass
def II11i11II ( ) :
 if 29 - 29: ooo0Oo0 % i1 % I1iiiiI1iII . i1IIi11111i / OoooooooOO * i1Ii
 Ii1I = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 iI = I1i1I1II ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<td>(.+?)</td>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  Ii1I = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ]
  i1Ii11i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  Ii1I = 'http://www.livefootballol.me' + Ii1I
  iIo00O ( "[COLOR aqua]" + i1Ii11i1i + "[/COLOR]" , Ii1I , 74 , OoOo , Oo , '' )
  if 54 - 54: O0
def OOoO000O00oO ( url ) :
 if 34 - 34: O0
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<a href="(.+?)"' ) . findall ( iI )
 OooOOOo0 = 0
 for I1I1IiI1 in i1IiIiiI :
  if 'acestream' in I1I1IiI1 :
   if 'http' in I1I1IiI1 :
    OooOOOo0 += 1
    i1i = '[COLOR aqua]Link :: ' + str ( OooOOOo0 ) + '[/COLOR]'
    i11Iiii ( i1i , I1I1IiI1 , 75 , OoOo , Oo , '' )
 if OooOOOo0 == 0 :
  i11Iiii ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , OoOo , Oo , '' )
  if 54 - 54: OOooO - iI1 - oOo0 . iIii1I11I1II1
def o0OIIiI1I1 ( url ) :
 if 15 - 15: OOooO * ooo0Oo0 % o000o0o00o0Oo * iIii1I11I1II1 - i11iIiiIii
 iI = I1i1I1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( iI ) [ 0 ]
 ii ( oOO00oOO , url , OoOo )
 if 60 - 60: iiI1iIiI * oOo0 % i1 + OOo0o0
def o0oo ( url , getphp ) :
 Ii1ii1IiIII = urllib2 . Request ( url )
 Ii1ii1IiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 Ii1ii1IiIII . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 ooO0o = urllib2 . urlopen ( Ii1ii1IiIII , timeout = 10 )
 iI = ooO0o . read ( )
 ooO0o . close ( )
 return iI
 if 80 - 80: oOo0 * Oooo0000 * i11Ii11I1Ii1i - O0 . Oooo0000 % iiI1iIiI
 if 13 - 13: OOo0o0 . iiI1iIiI * OOo0o0 + iiI1iIiI
 if 59 - 59: iiI1iIiI + i11iIiiIii + i1IIi / iI1
def I11 ( ) :
 if 47 - 47: o000o0o00o0Oo / OOo0o0 / OOoO00o
 Ii1I = 'http://m4ufree.com/?sort=key_top&page=1&='
 iI = I1i1I1II ( Ii1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IiIiiI = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( iI )
 for Iii111II in i1IiIiiI :
  i1i = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( Iii111II ) [ 0 ]
  III1iII1I1ii = re . compile ( '<a href="(.+?)"' ) . findall ( Iii111II ) [ 0 ] . replace ( './' , '' )
  Ii1I = 'http://m4ufree.com/' + III1iII1I1ii
  if not re . search ( '\d+' , i1i ) :
   iIo00O ( "[COLOR aqua]" + i1i + "[/COLOR]" , Ii1I , 42 , I1IiI , Oo )
   if 86 - 86: i1IIi11111i
   if 27 - 27: O0 . i1IIi11111i . o000o0o00o0Oo . o000o0o00o0Oo + o000o0o00o0Oo * i1IIi11111i
   if 100 - 100: ooo0Oo0 % OOooO / iI1
   if 30 - 30: ooo0Oo0 - OOoOoo00oo - OOoO00o
   if 81 - 81: i1IIi11111i . OoooooooOO + OOoOoo00oo * i1Ii
   if 74 - 74: i1IIi + O0 + ooo0Oo0
   if 5 - 5: ooo0Oo0 * Oooo0000
   if 46 - 46: i1Ii
   if 33 - 33: OOoO00o - i11Ii11I1Ii1i * OoooooooOO - ooo0Oo0 - OOoOoo00oo
   if 84 - 84: oOo0 + ooo0Oo0 - Oooo0000 * Oooo0000
def iIIII ( text ) :
 if 61 - 61: OoooooooOO . OOo0o0 . OoooooooOO / ooo0Oo0
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
 if 72 - 72: i1IIi
 return text
 if 82 - 82: Oooo0000 + OoooooooOO / i11iIiiIii * o000o0o00o0Oo . OoooooooOO
def oooo0OOo ( ) :
 if 72 - 72: O0 / i1Ii + OoooooooOO * OOoO00o
 OoOo0OOOoOo = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IIiiIIi1ooO000O = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 oOIII111iiIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 Ii11Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 1 - 1: iiI1iIiI % OoooooooOO + i11Ii11I1Ii1i - I1iiiiI1iII
 i11I1iiiI111I = 0
 for ( oooOOO00o0 , i1I , iiII1I11IIi ) in os . walk ( IIiiIIi1ooO000O ) :
  for file in iiII1I11IIi :
   OoOOo = os . path . join ( oooOOO00o0 , file )
   i11I1iiiI111I += os . path . getsize ( OoOOo )
 IIIii1II1II = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i11I1iiiI111I / ( 1024 * 1024.0 ) )
 i11Iiii ( IIIii1II1II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 17 - 17: i1IIi
 i11I1iiiI111I = 0
 for ( oooOOO00o0 , i1I , iiII1I11IIi ) in os . walk ( OoOo0OOOoOo ) :
  for file in iiII1I11IIi :
   OoOOo = os . path . join ( oooOOO00o0 , file )
   i11I1iiiI111I += os . path . getsize ( OoOOo )
 IIIii1II1II = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i11I1iiiI111I / ( 1024 * 1024.0 ) )
 i11Iiii ( IIIii1II1II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 1 - 1: i1Ii
 i11I1iiiI111I = 0
 for ( oooOOO00o0 , i1I , iiII1I11IIi ) in os . walk ( oOIII111iiIi1 ) :
  for file in iiII1I11IIi :
   OoOOo = os . path . join ( oooOOO00o0 , file )
   i11I1iiiI111I += os . path . getsize ( OoOOo )
 IIIii1II1II = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i11I1iiiI111I / ( 1024 * 1024.0 ) )
 i11Iiii ( IIIii1II1II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 78 - 78: o000o0o00o0Oo + iI1 - O0
 i11I1iiiI111I = 0
 for ( oooOOO00o0 , i1I , iiII1I11IIi ) in os . walk ( Ii11Ii ) :
  for file in iiII1I11IIi :
   OoOOo = os . path . join ( oooOOO00o0 , file )
   i11I1iiiI111I += os . path . getsize ( OoOOo )
 IIIii1II1II = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( i11I1iiiI111I / ( 1024 * 1024.0 ) )
 i11Iiii ( IIIii1II1II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 10 - 10: oOo0 % iiI1iIiI
 i11Iiii ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 i11Iiii ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 97 - 97: OoooooooOO - oOo0
def ii ( name , url , iconimage ) :
 if 58 - 58: iIii1I11I1II1 + O0
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import urlresolver
 if 30 - 30: i1Ii % OOoO00o * OOoOoo00oo - o000o0o00o0Oo * OOooO % i1Ii
 if 46 - 46: i11iIiiIii - O0 . OOo0o0
 if 100 - 100: iiI1iIiI / i1IIi11111i * OOoO00o . O0 / OOoOoo00oo
 if 83 - 83: oOo0
 if 'acestream' in url :
  III1iII1I1ii = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  OO . setPath ( url )
  xbmc . Player ( ) . play ( III1iII1I1ii , OO , False )
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
  OO = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OO . setPath ( ooO )
  xbmc . Player ( ) . play ( ooO , OO , False )
  time . sleep ( 2 )
  quit ( )
 else :
  ooO = url
  OO = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OO . setPath ( ooO )
  xbmc . Player ( ) . play ( ooO , OO , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 48 - 48: i11Ii11I1Ii1i * OOoOoo00oo * oOo0
def i1iiiIii11 ( name , url , iconimage ) :
 if 67 - 67: i1IIi11111i % Oooo0000 . Oooo0000 - i1Ii
 OOoOoo , O00ooOo = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 OOoOoo += urllib . unquote_plus ( O00ooOo )
 url = regex . resolve ( OOoOoo )
 if 80 - 80: i1IIi11111i - OOoOoo00oo + OoooooooOO
 PLAYREGEX ( name , url , iconimage )
 if 98 - 98: OOoOoo00oo + i1IIi . iiI1iIiI - i11Ii11I1Ii1i - i1IIi11111i
def OOOOo0 ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 24 - 24: ooo0Oo0 - i1IIi + iI1
def IiiIi ( heading , text ) :
 if 10 - 10: i1 / ooo0Oo0
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 I1i = xbmcgui . Window ( id )
 II11iIII1i1I = 50
 while ( II11iIII1i1I > 0 ) :
  try :
   xbmc . sleep ( 10 )
   II11iIII1i1I -= 1
   I1i . getControl ( 1 ) . setLabel ( heading )
   I1i . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 63 - 63: ooo0Oo0 + oOo0 - i11Ii11I1Ii1i
  if 2 - 2: I1iiiiI1iII
def I1i1I1II ( url ) :
 try :
  Ii1ii1IiIII = urllib2 . Request ( url )
  Ii1ii1IiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  ooO0o = urllib2 . urlopen ( Ii1ii1IiIII , timeout = 5 )
  iI = ooO0o . read ( )
  ooO0o . close ( )
  iI = iI . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI
 except : quit ( )
 if 97 - 97: OOo0o0 - OoooooooOO
def OoO0o ( url ) :
 try :
  Ii1ii1IiIII = urllib2 . Request ( url )
  Ii1ii1IiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  ooO0o = urllib2 . urlopen ( Ii1ii1IiIII , timeout = 5 )
  iI = ooO0o . read ( )
  ooO0o . close ( )
  iI = iI . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return iI
 except : quit ( )
 if 79 - 79: Oooo0000 % I1iiiiI1iII % ooo0Oo0
def i11Iiii ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 Ii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 I1iiiiii = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 65 - 65: I1iiiiI1iII + ooo0Oo0
 I1iiiiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1 , listitem = OO , isFolder = False )
 return I1iiiiii
 if 59 - 59: OoooooooOO + iI1 . oOo0 - O0 % iIii1I11I1II1 / O0
def OO00Oo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 Ii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 I1iiiiii = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 88 - 88: ooo0Oo0 . O0 % OoooooooOO / OOoOoo00oo
 OO . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 89 - 89: i11Ii11I1Ii1i / OOo0o0
 I1iiiiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1 , listitem = OO , isFolder = False )
 return I1iiiiii
 if 14 - 14: OOoOoo00oo . iiI1iIiI * i1Ii + i11Ii11I1Ii1i - i1Ii + OOoOoo00oo
def IIIIIiII1 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 iii11 = [ ]
 i1oO = [ ]
 iIIi1IIi = [ ]
 iI = I1i1I1II ( url )
 I1I1IiI1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I1IiI1 ) [ 0 ]
 Iii111II = re . compile ( '<link>(.+?)</link>' ) . findall ( I1I1IiI1 )
 if len ( Iii111II ) < 1 :
  Iii111II = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( I1I1IiI1 )
 oO0000OOo00 = 1
 for i111i11I1ii in Iii111II :
  OOooo = i111i11I1ii
  if '(' in i111i11I1ii :
   i111i11I1ii = i111i11I1ii . split ( '(' ) [ 0 ]
   oo0oOO = str ( OOooo . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iii11 . append ( i111i11I1ii )
   i1oO . append ( oo0oOO )
  else :
   iii11 . append ( i111i11I1ii )
   i1oO . append ( '[COLOR aqua]Link ' + str ( oO0000OOo00 ) + '[/COLOR]' )
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 II1i11i1iIi11 = Iii1ii1II11i . select ( name , i1oO )
 if II1i11i1iIi11 < 0 :
  quit ( )
 else :
  url = iii11 [ II1i11i1iIi11 ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : ooO = liveresolver . resolve ( url )
  else : ooO = url
  OO = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  OO . setPath ( ooO )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( ooO )
  if 83 - 83: OOooO
def I1iI1I1 ( name , url , iconimage ) :
 if 48 - 48: iiI1iIiI / i11iIiiIii - i1IIi11111i * OOo0o0 / OoooooooOO
 OoOoi1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iii11 = [ ]
 i1oO = [ ]
 iIIi1IIi = [ ]
 IIIiiiI = [ ]
 iI = I1i1I1II ( url )
 I1I1IiI1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( iI ) [ 0 ]
 Iii111II = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( I1I1IiI1 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1I1IiI1 ) [ 0 ]
 oO0000OOo00 = 1
 if 94 - 94: O0 - iI1 - iIii1I11I1II1 % i1Ii / OOooO % OOoO00o
 for i111i11I1ii in Iii111II :
  OOooo = i111i11I1ii
  if '(' in i111i11I1ii :
   i111i11I1ii = i111i11I1ii . split ( '(' ) [ 0 ]
   oo0oOO = str ( OOooo . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iii11 . append ( i111i11I1ii )
   i1oO . append ( oo0oOO )
   IIIiiiI . append ( 'Stream ' + str ( oO0000OOo00 ) )
  else :
   iii11 . append ( i111i11I1ii )
   i1oO . append ( 'Link ' + str ( oO0000OOo00 ) )
   if 44 - 44: ooo0Oo0 % iIii1I11I1II1
  oO0000OOo00 = oO0000OOo00 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 II1i11i1iIi11 = Iii1ii1II11i . select ( name , i1oO )
 if II1i11i1iIi11 < 0 :
  quit ( )
 else :
  O00Oo000ooO0 = i1oO [ II1i11i1iIi11 ]
  OoO0O00 = "/"
  if not O00Oo000ooO0 . endswith ( OoO0O00 ) :
   IIiII = O00Oo000ooO0 + "/"
  else :
   IIiII = O00Oo000ooO0
  url = OoOoi1i + iii11 [ II1i11i1iIi11 ] + "%26referer=" + IIiII
  print url
  if 90 - 90: i11Ii11I1Ii1i + OoooooooOO % OoooooooOO
  xbmc . Player ( ) . play ( url )
  if 35 - 35: OOoO00o / o000o0o00o0Oo * OoooooooOO . i11Ii11I1Ii1i / ooo0Oo0
def IIII ( string ) :
 Iii11i = ( c for c in string if 0 < ord ( c ) < 127 )
 if 73 - 73: ooo0Oo0 - Oooo0000 - OOo0o0 - iiI1iIiI
 return '' . join ( Iii11i )
 if 65 - 65: i1IIi11111i
def iIo00O ( name , url , mode , iconimage , fanart , description = '' ) :
 if 7 - 7: I1iiiiI1iII . Oooo0000 / o000o0o00o0Oo . OOoOoo00oo * iI1 - i11Ii11I1Ii1i
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 Ii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iiiiii = True
 OO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 OO . setProperty ( "fanart_Image" , fanart )
 OO . setProperty ( "icon_Image" , iconimage )
 OO . setInfo ( 'video' , { 'Plot' : description } )
 I1iiiiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1 , listitem = OO , isFolder = True )
 return I1iiiiii
 if 37 - 37: oOo0 . Oooo0000 / O0 * OOoO00o
def III11iiii11i1 ( name , url , iconimage ) :
 I1iiiiii = True
 OO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I1iiiiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OO )
 xbmc . Player ( ) . play ( url , OO , False )
 if 54 - 54: i1IIi - OOo0o0
def IiIIII ( ) :
 if 89 - 89: i1 / iiI1iIiI
 OoOo0OOOoOo = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IIiiIIi1ooO000O = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 oOIII111iiIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 16 - 16: ooo0Oo0 + i1Ii / ooo0Oo0 / i1 % OOo0o0 % o000o0o00o0Oo
 oO0000OOo00 = [ ( OoOo0OOOoOo , 'Cache' ) , ( IIiiIIi1ooO000O , 'Thumbnails' ) , ( oOIII111iiIi1 , 'Packages' ) ]
 if 22 - 22: i11Ii11I1Ii1i * i1 * iI1 + o000o0o00o0Oo * i1IIi11111i
 oo0o0 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if oo0o0 :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for OOoOoo in oO0000OOo00 :
   if 69 - 69: o000o0o00o0Oo - oOo0
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 1 )
   if 16 - 16: ooo0Oo0
   for ii1iI111 , i1I , iiII1I11IIi in os . walk ( OOoOoo [ 0 ] ) :
    for o00O00O0O0O in iiII1I11IIi :
     if ( o00O00O0O0O . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( ii1iI111 , o00O00O0O0O ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % OOoOoo [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 80 - 80: OOoOoo00oo % o000o0o00o0Oo
def O0Ooo ( url , mode , name , iconimage , fanart ) :
 if 78 - 78: i1 % I1iiiiI1iII * i1IIi
 with open ( I11i , "a" ) as o0o0 :
  o0o0 . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 66 - 66: OOooO . iiI1iIiI + i1IIi11111i . iIii1I11I1II1
def o0iIiiIiiIi ( ) :
 if 40 - 40: i1IIi11111i
 with open ( I11i , "a" ) as o0o0 :
  oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  o0oo0o0o0 = open ( oOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IiIiiI = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oo0o0o0 )
  i11Iiii ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  i11Iiii ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  if len ( i1IiIiiI ) < 1 :
   i11Iiii ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  for O0oo0ooOOOO in i1IiIiiI :
   i1i = re . compile ( '<title>(.+?)</title>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   Ii1I = re . compile ( '<url>(.+?)</url>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   i11Iiii ( '[COLOR skyblue]' + i1i + '[/COLOR]' , Ii1I , 2 , I1IiI , I1ii11iIi11i )
   if 43 - 43: o000o0o00o0Oo / iiI1iIiI . i1Ii
 i11Iiii ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , OoOo , Oo )
 if 62 - 62: iIii1I11I1II1 + OOoO00o . ooo0Oo0 / I1iiiiI1iII % O0 . oOo0
def Oo0oOooOoOo ( ) :
 if 49 - 49: OOoOoo00oo . o000o0o00o0Oo . i11iIiiIii - i11Ii11I1Ii1i / OOooO
 with open ( IiII , "a" ) as o0o0 :
  oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  o0oo0o0o0 = open ( oOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IiIiiI = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oo0o0o0 )
  i11Iiii ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  i11Iiii ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  if len ( i1IiIiiI ) < 1 :
   i11Iiii ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , OoOo , Oo )
  for O0oo0ooOOOO in i1IiIiiI :
   i1i = re . compile ( '<title>(.+?)</title>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   Ii1I = re . compile ( '<link>(.+?)</link>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0oo0ooOOOO ) [ 0 ]
   i11Iiii ( '[COLOR skyblue]' + i1i + '[/COLOR]' , Ii1I , 2 , I1IiI , I1ii11iIi11i )
   if 62 - 62: OOoOoo00oo
 i11Iiii ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , OoOo , Oo )
 if 1 - 1: I1iiiiI1iII / I1iiiiI1iII - i11iIiiIii
def OO0oIiII1iiI ( ) :
 if 34 - 34: iiI1iIiI . OOo0o0 + i1IIi
 with open ( I11i , "w" ) as o0o0 :
  o0o0 . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 98 - 98: OOo0o0 % I1iiiiI1iII * i11iIiiIii % o000o0o00o0Oo
def iIiI1IIiii11 ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as o0o0 :
  o0o0 . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 33 - 33: iIii1I11I1II1 / OOoO00o - iiI1iIiI * iI1
 if 53 - 53: i1Ii
 if 98 - 98: oOo0
def ii11i1iIII ( ) :
 if 92 - 92: oOo0 - iIii1I11I1II1
 if 32 - 32: OOooO % i1 * i1 + I1iiiiI1iII * i11Ii11I1Ii1i * OOooO
 iIiIii1I1II = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  O0Oooo = re . compile ( '<pin>(.+?)</pin>' ) . findall ( iIiIii1I1II ) [ 0 ]
  if O0Oooo == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   iII1i1 = ''
   O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   O0oOOoooOO0O . doModal ( )
   if O0oOOoooOO0O . isConfirmed ( ) :
    iII1i1 = O0oOOoooOO0O . getText ( )
    if len ( iII1i1 ) > 1 :
     ooo00Ooo = iII1i1 . title ( )
     with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
      o00O00O0O0O . write ( "<pin>" + ooo00Ooo + "</pin>" )
     ii11i1iIII ( )
    else : quit ( )
   else : quit ( )
  if not 'EXPIRED' in O0Oooo :
   oO000 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( iIiIii1I1II ) [ 0 ]
   I1IiIiIi1IiI1 = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % oO000 )
   iI = I1i1I1II ( I1IiIiIi1IiI1 )
   if 'Pin Verified' in iI :
    pass
   else :
    with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
     o00O00O0O0O . write ( '<pin>EXPIRED</pin>' )
     ii11i1iIII ( )
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as o00O00O0O0O :
   o00O00O0O0O . write ( "<pin>EXPIRED</pin>\n" )
  ii11i1iIII ( )
  if 60 - 60: OOooO * Oooo0000 - i11iIiiIii % i1Ii
  if 52 - 52: o000o0o00o0Oo % OOo0o0 - i11iIiiIii
  if 30 - 30: OOoO00o / i1 + OOo0o0
  if 6 - 6: OOoO00o . iI1 + OOooO . oOo0
def oOoO0o ( url , iconimage , fanart ) :
 if 46 - 46: oOo0 % OOooO
 try :
  iII1i1 = ''
  O0oOOoooOO0O = xbmc . Keyboard ( iII1i1 , 'Enter Name To Save File As' )
  O0oOOoooOO0O . doModal ( )
  if O0oOOoooOO0O . isConfirmed ( ) :
   iII1i1 = O0oOOoooOO0O . getText ( )
   if len ( iII1i1 ) > 1 :
    ooo00Ooo = iII1i1 . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   ooO = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = ooO
  oOOoO0OO00OOo0 = url . split ( '/' ) [ - 1 ]
  Ii1 = urllib2 . urlopen ( url )
  Ii1IIii = os . path . join ( o0OOO , ooo00Ooo )
  o00O00O0O0O = open ( Ii1IIii , 'wb' )
  if 21 - 21: Oooo0000 / i1IIi11111i * I1iiiiI1iII . i1IIi
  ooOoOO = Ii1 . info ( )
  Ooo00o0oOo0O0O = int ( ooOoOO . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( ooo00Ooo , Ooo00o0oOo0O0O ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 79 - 79: o000o0o00o0Oo + oOo0
  iIiIIi = 0
  III1I = 8192
  while True :
   buffer = Ii1 . read ( III1I )
   if not buffer :
    break
    if 11 - 11: i1Ii - OOoOoo00oo + i1Ii * OOo0o0 / iiI1iIiI
   iIiIIi += len ( buffer )
   o00O00O0O0O . write ( buffer )
   OoOOOO = "[%3.2f%%]" % ( iIiIIi * 100. / Ooo00o0oOo0O0O )
   OoOOOO = OoOOOO + chr ( 8 ) * ( len ( OoOOOO ) + 1 )
   iIiiiI . update ( iIiIIi , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( OoOOOO , ooo00Ooo ) )
   if 18 - 18: i1Ii % i11iIiiIii . iIii1I11I1II1 - OOoO00o
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as o0o0 :
   o0o0 . write ( '<item>\n<title>' + ooo00Ooo + '</title>\n<link>' + Ii1IIii + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 80 - 80: iiI1iIiI + OOo0o0 - i1IIi . OOooO / i1IIi11111i / iiI1iIiI
  o00O00O0O0O . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 1 - 1: iI1 + i11iIiiIii - iiI1iIiI / OOoOoo00oo + oOo0
  if 80 - 80: OOo0o0 + i1IIi11111i * OOooO + i1
  if 75 - 75: iI1 / i1IIi11111i / OOoOoo00oo / I1iiiiI1iII % i1Ii + i11Ii11I1Ii1i
  if 4 - 4: OOoO00o - ooo0Oo0 - I1iiiiI1iII - iI1 % i11iIiiIii / i1
def i1iii11 ( ) :
 oOo0O0o0000o0O0 = [ ]
 o0OoOoOOoOo0o = sys . argv [ 2 ]
 if len ( o0OoOoOOoOo0o ) >= 2 :
  iIiiiIiIii1ii = sys . argv [ 2 ]
  IIiI1i = iIiiiIiIii1ii . replace ( '?' , '' )
  if ( iIiiiIiIii1ii [ len ( iIiiiIiIii1ii ) - 1 ] == '/' ) :
   iIiiiIiIii1ii = iIiiiIiIii1ii [ 0 : len ( iIiiiIiIii1ii ) - 2 ]
  iII1 = IIiI1i . split ( '&' )
  oOo0O0o0000o0O0 = { }
  for oO0000OOo00 in range ( len ( iII1 ) ) :
   O000O = { }
   O000O = iII1 [ oO0000OOo00 ] . split ( '=' )
   if ( len ( O000O ) ) == 2 :
    oOo0O0o0000o0O0 [ O000O [ 0 ] ] = O000O [ 1 ]
 return oOo0O0o0000o0O0
 if 98 - 98: iIii1I11I1II1 + oOo0 % Oooo0000 + iI1 % Oooo0000
iIiiiIiIii1ii = i1iii11 ( ) ; Ii1I = None ; oOO00oOO = None ; iI1I1I11IiII = None ; iIii11iI1II = None ; OoOo = None ; I1II1I1I = None
try : iIii11iI1II = urllib . unquote_plus ( iIiiiIiIii1ii [ "site" ] )
except : pass
try : Ii1I = urllib . unquote_plus ( iIiiiIiIii1ii [ "url" ] )
except : pass
try : oOO00oOO = urllib . unquote_plus ( iIiiiIiIii1ii [ "name" ] )
except : pass
try : iI1I1I11IiII = int ( iIiiiIiIii1ii [ "mode" ] )
except : pass
try : OoOo = urllib . unquote_plus ( iIiiiIiIii1ii [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( iIiiiIiIii1ii [ "fanart" ] )
except : pass
try : I1II1I1I = urllib . unquote_plus ( iIiiiIiIii1ii [ "description" ] )
except : pass
if 79 - 79: OOoOoo00oo / oOo0 . Oooo0000 - o000o0o00o0Oo
if iI1I1I11IiII == None or Ii1I == None or len ( Ii1I ) < 1 : iI11i1I1 ( )
if 47 - 47: OoooooooOO % O0 * OOoO00o . OOooO
if 38 - 38: O0 - I1iiiiI1iII % oOo0
if 64 - 64: iIii1I11I1II1
if 15 - 15: o000o0o00o0Oo + OOoOoo00oo / o000o0o00o0Oo / oOo0
if 31 - 31: i1Ii + O0 + i1Ii . iIii1I11I1II1 + ooo0Oo0 / i1IIi11111i
elif iI1I1I11IiII == 1 : I1 ( oOO00oOO , Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 2 : ii ( oOO00oOO , Ii1I , OoOo )
elif iI1I1I11IiII == 3 : IIIIIiII1 ( oOO00oOO , Ii1I , OoOo )
if 6 - 6: ooo0Oo0 % I1iiiiI1iII * iI1 / iiI1iIiI + ooo0Oo0
if 39 - 39: Oooo0000 - ooo0Oo0 / OOoO00o * OoooooooOO
if 100 - 100: O0 . iI1 . i1 + O0 * OOo0o0
elif iI1I1I11IiII == 4 : O0ooo0O0oo0 ( Ii1I )
elif iI1I1I11IiII == 5 : oO00o0 ( Ii1I )
elif iI1I1I11IiII == 6 : oOo0oO ( )
elif iI1I1I11IiII == 7 : iiI1Ii1iI1 ( Ii1I )
elif iI1I1I11IiII == 8 : oOo0O0o00o ( Ii1I )
elif iI1I1I11IiII == 9 : o0 ( Ii1I )
elif iI1I1I11IiII == 10 : OOOOo0 ( Ii1I )
elif iI1I1I11IiII == 11 : IiI1i ( )
elif iI1I1I11IiII == 12 : Oooo0oOO ( Ii1I )
elif iI1I1I11IiII == 13 : oO00Oo0O0o ( Ii1I )
elif iI1I1I11IiII == 14 : O0oO ( Ii1I )
elif iI1I1I11IiII == 15 : O0oOOoOooooO ( )
elif iI1I1I11IiII == 16 : I1iI1I1 ( oOO00oOO , Ii1I , OoOo )
elif iI1I1I11IiII == 17 : iIIi1i1 ( Ii1I )
elif iI1I1I11IiII == 18 : oooo0O0 ( Ii1I )
elif iI1I1I11IiII == 19 : i11111IIIII ( Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 20 : OOO ( )
elif iI1I1I11IiII == 21 : oOooOo0 ( Ii1I )
elif iI1I1I11IiII == 22 : I1IIIiIiI1 ( Ii1I )
elif iI1I1I11IiII == 23 : oO00O000oO0 ( )
elif iI1I1I11IiII == 24 : iIIii ( Ii1I )
elif iI1I1I11IiII == 25 : oo0oO ( Ii1I , OoOo )
elif iI1I1I11IiII == 26 : IiI1iIiIIIii ( Ii1I )
elif iI1I1I11IiII == 27 : OOOoOO0o ( Ii1I , OoOo )
elif iI1I1I11IiII == 28 : iiiII ( )
elif iI1I1I11IiII == 29 : oo00O00Oo ( Ii1I )
elif iI1I1I11IiII == 30 : ii1I1i1iiiI ( Ii1I )
elif iI1I1I11IiII == 31 : o00Ooo0 ( Ii1I )
elif iI1I1I11IiII == 32 : II1Iiiiii ( Ii1I )
elif iI1I1I11IiII == 33 : oOO0OOOo ( Ii1I )
elif iI1I1I11IiII == 34 : I1i1i1 ( Ii1I )
elif iI1I1I11IiII == 35 : IIiiIIi1 ( )
elif iI1I1I11IiII == 36 : Ii1iI111 ( Ii1I )
elif iI1I1I11IiII == 37 : oOO0 ( Ii1I , OoOo )
elif iI1I1I11IiII == 38 : oOoo000 ( )
elif iI1I1I11IiII == 39 : o000oo ( Ii1I )
elif iI1I1I11IiII == 40 : OOO ( )
elif iI1I1I11IiII == 41 : oOooOo0 ( Ii1I )
elif iI1I1I11IiII == 42 : III ( Ii1I )
elif iI1I1I11IiII == 43 : II1II1iIIi11 ( Ii1I , OoOo )
elif iI1I1I11IiII == 44 : I11 ( )
if 42 - 42: OOo0o0 % OoooooooOO + i1IIi11111i
elif iI1I1I11IiII == 45 : OoOoOo00o0 ( )
elif iI1I1I11IiII == 46 : OoO ( Ii1I )
elif iI1I1I11IiII == 47 : II1i ( oOO00oOO , Ii1I , OoOo )
elif iI1I1I11IiII == 48 : IIIiI11ii1I ( )
elif iI1I1I11IiII == 49 : II1111ii ( Ii1I )
elif iI1I1I11IiII == 50 : ii1III11 ( Ii1I )
elif iI1I1I11IiII == 51 : oOoOOo0oo0 ( Ii1I )
elif iI1I1I11IiII == 52 : oo0OOo0O ( Ii1I )
elif iI1I1I11IiII == 53 : iIi1i ( Ii1I )
elif iI1I1I11IiII == 54 : iioo0o0OoOOO ( Ii1I , OoOo )
if 56 - 56: OoooooooOO + o000o0o00o0Oo - OOoO00o
if 24 - 24: i1IIi11111i + i1Ii + iI1 - iIii1I11I1II1
if 49 - 49: iI1 . i1Ii * Oooo0000 % I1iiiiI1iII . O0
elif iI1I1I11IiII == 59 : IIII1 ( )
elif iI1I1I11IiII == 60 : oOOO0oo0 ( Ii1I )
elif iI1I1I11IiII == 61 : ii111IiiI1 ( oOO00oOO , Ii1I , OoOo )
if 48 - 48: O0 * OOooO - O0 / OOooO + Oooo0000
elif iI1I1I11IiII == 66 : oO ( )
elif iI1I1I11IiII == 67 : II11iI111i1 ( Ii1I )
elif iI1I1I11IiII == 68 : oOO00O0Ooooo00 ( Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 69 : o0Iii ( Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 70 : iIiii ( Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 71 : I111 ( )
elif iI1I1I11IiII == 72 : oOOOO ( )
elif iI1I1I11IiII == 73 : II11i11II ( )
elif iI1I1I11IiII == 74 : OOoO000O00oO ( Ii1I )
elif iI1I1I11IiII == 75 : o0OIIiI1I1 ( Ii1I )
elif iI1I1I11IiII == 76 : O00oOo ( )
elif iI1I1I11IiII == 77 : ii1I11 ( )
if 52 - 52: i1 % OOooO * i11Ii11I1Ii1i
if 4 - 4: iI1 % O0 - OoooooooOO + i1Ii . OOo0o0 % i11Ii11I1Ii1i
elif iI1I1I11IiII == 884 : oooo0OOo ( )
elif iI1I1I11IiII == 885 : iIiI1IIiii11 ( )
elif iI1I1I11IiII == 886 : Oo0oOooOoOo ( )
elif iI1I1I11IiII == 887 : oOoO0o ( Ii1I , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 888 : O0o0o00OO0000 ( )
elif iI1I1I11IiII == 889 : O0Ooo ( Ii1I , iI1I1I11IiII , oOO00oOO , OoOo , I1ii11iIi11i )
elif iI1I1I11IiII == 890 : o0iIiiIiiIi ( )
elif iI1I1I11IiII == 891 : OO0oIiII1iiI ( )
elif iI1I1I11IiII == 892 : IiIIII ( )
if 9 - 9: i11Ii11I1Ii1i * i11Ii11I1Ii1i . i11iIiiIii * iIii1I11I1II1
if iI1I1I11IiII == None or Ii1I == None or len ( Ii1I ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
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
