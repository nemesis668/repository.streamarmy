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
try :
 import webbrowser
except : pass
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
if 1 - 1: O0Oooo00
def Ooo0 ( ) :
 if 89 - 89: I111i1i1111i - Ii1Ii1iiii11 % I1I1i1
 IiI1i = OOo0o0 ( oo00 )
 if len ( IiI1i ) > 1 :
  O0OoOoo00o = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  iiiI11 = os . path . join ( os . path . join ( O0OoOoo00o , '' ) , 'compare.txt' )
  OOooO = open ( iiiI11 )
  OOoO00o = OOooO . read ( )
  if OOoO00o == IiI1i : pass
  else :
   II111iiii ( '[B][COLOR aqua]N[COLOR yellow]emesis[COLOR aqua] I[COLOR yellow]nformation[/COLOR][/B]' , IiI1i )
   II = open ( iiiI11 , "w" )
   II . write ( IiI1i )
   II . close ( )
def OOo0o0 ( url ) :
 try :
  oOoOo00oOo = urllib2 . Request ( url )
  oOoOo00oOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ooo00O00O0O0O = urllib2 . urlopen ( oOoOo00oOo , timeout = 5 )
  OooO0OO = Ooo00O00O0O0O . read ( )
  Ooo00O00O0O0O . close ( )
  if 28 - 28: iIii1
  return OooO0OO
 except : quit ( )
 if 71 - 71: IiI1I1
def OoO000 ( ) :
 if 42 - 42: oOoO - iiIiIIi % iI - I11iii / OO0O00
 ii1 = xbmc . getInfoLabel ( "System.BuildVersion" )
 o0oO0o00oo = float ( ii1 [ : 4 ] )
 if o0oO0o00oo >= 11.0 and o0oO0o00oo <= 11.9 :
  II1i1Ii11Ii11 = 'Eden'
 elif o0oO0o00oo >= 12.0 and o0oO0o00oo <= 12.9 :
  II1i1Ii11Ii11 = 'Frodo'
 elif o0oO0o00oo >= 13.0 and o0oO0o00oo <= 13.9 :
  II1i1Ii11Ii11 = 'Gotham'
 elif o0oO0o00oo >= 14.0 and o0oO0o00oo <= 14.9 :
  II1i1Ii11Ii11 = 'Helix'
 elif o0oO0o00oo >= 15.0 and o0oO0o00oo <= 15.9 :
  II1i1Ii11Ii11 = 'Isengard'
 elif o0oO0o00oo >= 16.0 and o0oO0o00oo <= 16.9 :
  II1i1Ii11Ii11 = 'Jarvis'
 elif o0oO0o00oo >= 17.0 and o0oO0o00oo <= 17.9 :
  II1i1Ii11Ii11 = 'Krypton'
 elif o0oO0o00oo >= 18.0 and o0oO0o00oo <= 18.9 :
  II1i1Ii11Ii11 = 'Leia'
 else : II1i1Ii11Ii11 = "Decline"
 if 35 - 35: o0o0O00O00o0 + I111i1i1111i - O0Oooo00
 if II1i1Ii11Ii11 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif II1i1Ii11Ii11 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif II1i1Ii11Ii11 == "Leia" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 74 - 74: iI * O0
def oOOo0oo ( ) :
 if 80 - 80: oOoO * i11iIiiIii / OO0O00
 I11II1i = [ 'plugin.video.jenexporter' ]
 IIIII = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in I11II1i )
 ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.jenexporter' ) )
 if IIIII :
  import shutil
  shutil . rmtree ( ooooooO0oo )
  os . _exit ( 1 )
 else :
  return
  if 49 - 49: Ii1Ii1iiii11 * iIii1I11I1II1 / i1IIi / i11iIiiIii / Ii1Ii1iiii11
def I1i1I1II ( ) :
 if 45 - 45: OO0O00 . I111i1i1111i
 oO ( )
 oOOo0oo ( )
 ii1i1I1i = baseurl
 o00oOO0 = ii1i1I1i
 Ooo0 ( )
 oOoo = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( oOoo >= 0000 ) and ( oOoo <= 1159 ) : iIii11I = "Morning"
 elif ( oOoo >= 1200 ) and ( oOoo <= 1759 ) : iIii11I = "Afternoon"
 else : iIii11I = "Evening"
 OOO0OOO00oo ( '[COLOR yellow]Good[COLOR aqua] ' + str ( iIii11I ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 OOO0OOO00oo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  OooO0OO = Iii111II ( baseurl )
  iiii11I = re . compile ( '<item>(.+?)</item>' ) . findall ( OooO0OO )
  for Ooo0OO0oOO in iiii11I :
   try :
    if '<m3u>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 11 , IIIii1II1II , I1ii11iIi11i )
    elif '<mamahdsports>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 14 , IIIii1II1II , I1ii11iIi11i )
    elif '<atc>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<atc>(.+?)</atc>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 6 , IIIii1II1II , I1ii11iIi11i )
    elif '<scanner>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 11 , IIIii1II1II , I1ii11iIi11i )
    elif '<cartoons>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 29 , IIIii1II1II , I1ii11iIi11i )
    elif '<Adult>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 38 , IIIii1II1II , I1ii11iIi11i )
    elif '<Anime>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 51 , IIIii1II1II , I1ii11iIi11i )
    elif '<audiobooks>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 59 , IIIii1II1II , I1ii11iIi11i )
    elif '<WORLDCUP>' in Ooo0OO0oOO :
     ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     ii1i1I1i = re . compile ( '<WORLDCUP>(.+?)</WORLDCUP>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     i1I1iI ( ii11i1 , ii1i1I1i , 100 , IIIii1II1II , I1ii11iIi11i )
    elif '<folder>' in Ooo0OO0oOO :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO )
     for ii11i1 , ii1i1I1i , IIIii1II1II , I1ii11iIi11i in oo0OooOOo0 :
      i1I1iI ( ii11i1 , ii1i1I1i , 1 , IIIii1II1II , I1ii11iIi11i )
    else :
     o0O = re . compile ( '<link>(.+?)</link>' ) . findall ( Ooo0OO0oOO )
     if len ( o0O ) == 1 :
      oo0OooOOo0 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO )
      O00oO = len ( iiii11I )
      for ii11i1 , ii1i1I1i , IIIii1II1II , I1ii11iIi11i in oo0OooOOo0 :
       if 'youtube.com/playlist' in ii1i1I1i :
        i1I1iI ( ii11i1 , ii1i1I1i , 2 , IIIii1II1II , I1ii11iIi11i )
       else :
        OOO0OOO00oo ( ii11i1 , ii1i1I1i , 2 , IIIii1II1II , I1ii11iIi11i )
     elif len ( o0O ) > 1 :
      ii11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
      IIIii1II1II = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
      OOO0OOO00oo ( ii11i1 , o00oOO0 , 3 , IIIii1II1II , I1ii11iIi11i )
   except : pass
   if 39 - 39: I11iii - O0Oo0oO0o * O0Oooo00 % Ii1Ii1iiii11 * O0Oo0oO0o % O0Oo0oO0o
  OOO0OOO00oo ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.resolveurl/settings.xml" )
   iIii11I = open ( file ) . read ( )
   OoOOOOO = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( iIii11I ) [ 0 ]
   OoOOOOO = OoOOOOO . strip ( )
   ii1i1I1i = 'plugin://script.module.resolveurl/?mode=auth_rd'
   if 'value=""' in OoOOOOO :
    iIi1i111II = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    OOO0OOO00oo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( iIi1i111II ) + '[/COLOR]' , ii1i1I1i , 2 , I1IiI , Oo )
   else :
    iIi1i111II = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    OOO0OOO00oo ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( iIi1i111II ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  OoOO00O = 'https://i.imgur.com/o2Wvut7.jpg'
  i1I1iI ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , OoOO00O , Oo )
  oOOoO0O0O0 = 'https://i.imgur.com/SxZzRX9.jpg'
  i1I1iI ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , oOOoO0O0O0 , Oo )
  Oo000o = 'https://i.imgur.com/zme6vuj.jpg'
  i1I1iI ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , Oo000o , Oo )
 except :
  I11IiI1I11i1i = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if I11IiI1I11i1i == 0 :
   OOO0OOO00oo ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   i1I1iI ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if I11IiI1I11i1i == 1 :
   quit ( )
   if 38 - 38: Ii1Ii1iiii11
   if 57 - 57: O0 / iIii1 * OO0O00 / I111i1i1111i . O0Oo0oO0o
   if 26 - 26: iI
def OOO ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 o00oOO0 = url
 OooO0OO = Iii111II ( url )
 oOOo0oo ( )
 iiii11I = re . compile ( '<item>(.+?)</item>' ) . findall ( OooO0OO )
 for Ooo0OO0oOO in iiii11I :
  try :
   if '<image>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 23 , iconimage , fanart )
   elif '<American>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 77 , iconimage , fanart )
   elif '<acechansthree>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<acechansthree>(.+?)</acechansthree>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 78 , iconimage , fanart )
   elif '<acechansfour>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<acechansfour>(.+?)</acechansfour>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 79 , iconimage , fanart )
   elif '<bollywood>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<bollywood>(.+?)</bollywood>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 80 , iconimage , fanart )
   elif '<HDFLIX>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<HDFLIX>(.+?)</HDFLIX>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 83 , iconimage , fanart )
   elif '<RDMOVIES>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<RDMOVIES>(.+?)</RDMOVIES>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 85 , iconimage , fanart )
   elif '<NEWS>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<NEWS>(.+?)</NEWS>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 87 , iconimage , fanart )
   elif '<animemovie>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<animemovie>(.+?)</animemovie>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 88 , iconimage , fanart )
   elif '<animeshows>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<animeshows>(.+?)</animeshows>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 93 , iconimage , fanart )
   elif '<lordjd>' in Ooo0OO0oOO :
    o0O = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( Ooo0OO0oOO )
    if len ( o0O ) == 1 :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO )
     O00oO = len ( iiii11I )
     for name , url , iconimage , fanart in oo0OooOOo0 :
      if 'youtube.com/playlist' in url :
       i1I1iI ( name , url , 2 , iconimage , fanart )
      else :
       Oo0oOOo ( name , url , 2 , iconimage , fanart )
    elif len ( o0O ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     Oo0oOOo ( name , o00oOO0 , 3 , iconimage , fanart )
   elif '<reddit>' in Ooo0OO0oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
    i1I1iI ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in Ooo0OO0oOO :
    o0O = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ooo0OO0oOO )
    if len ( o0O ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     Oo0OoO00oOO0o = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     OOO00O = Oo0OoO00oOO0o
     OOoOO0oo0ooO = "/"
     if not OOO00O . endswith ( OOoOO0oo0ooO ) :
      O0o0O00Oo0o0 = OOO00O + "/"
     else :
      O0o0O00Oo0o0 = OOO00O
     OooO0OO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = OooO0OO + '%26referer=' + O0o0O00Oo0o0
     OOO0OOO00oo ( name , url , 10 , iconimage , fanart )
    elif len ( o0O ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     OOO0OOO00oo ( name , o00oOO0 , 16 , iconimage , fanart )
     if 87 - 87: o0o0O00O00o0 * i1iIii1Ii1II % i11iIiiIii % I111i1i1111i - IiI1I1
   elif '<folder>' in Ooo0OO0oOO :
    oo0OooOOo0 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO )
    for name , url , iconimage , fanart in oo0OooOOo0 :
     i1I1iI ( name , url , 1 , iconimage , fanart )
     if 68 - 68: OO0O00 % i1IIi . I11iii . I1I1i1
   else :
    o0O = re . compile ( '<link>(.+?)</link>' ) . findall ( Ooo0OO0oOO )
    if len ( o0O ) == 1 :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO )
     O00oO = len ( iiii11I )
     for name , url , iconimage , fanart in oo0OooOOo0 :
      if 'youtube.com/playlist' in url :
       i1I1iI ( name , url , 2 , iconimage , fanart )
      else :
       OOO0OOO00oo ( name , url , 2 , iconimage , fanart )
    elif len ( o0O ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0OO0oOO ) [ 0 ]
     OOO0OOO00oo ( name , o00oOO0 , 3 , iconimage , fanart )
  except : pass
  if 92 - 92: iI . OO0O00
 OoO000 ( )
 if 31 - 31: OO0O00 . I111i1i1111i / O0
 if 89 - 89: I111i1i1111i
 if 68 - 68: O0Oooo00 * OoooooooOO % O0 + O0Oooo00 + o0o0O00O00o0
 if 4 - 4: o0o0O00O00o0 + O0 * IiI1I1
 if 55 - 55: i1iIii1Ii1II + iIii1I11I1II1 / I111i1i1111i * iIii1 - i11iIiiIii - iiIiIIi
 if 25 - 25: I1I1i1
 if 7 - 7: i1IIi / II1iI * OO0O00 . I11iii . iIii1I11I1II1
 if 13 - 13: IiI1I1 / i11iIiiIii
def Iiii ( url ) :
 if 75 - 75: I111i1i1111i % Ii1Ii1iiii11 % Ii1Ii1iiii11 . OO0O00
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  try :
   III1iII1I1ii = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( o0O ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( o0O ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   i1I1iI ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 61 - 61: O0Oo0oO0o
def O0OOO ( url ) :
 if 10 - 10: IiI1I1 * oOoO % I111i1i1111i / II1iI / I111i1i1111i
 iIIi1i1 = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 i1IIIiiII1 = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 OOO0OOO00oo ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 OooO0OO = Iii111II ( url )
 o0O = 0
 OOOOoOoo0O0O0 = re . compile ( 'href="([^"]+)' ) . findall ( OooO0OO )
 for url in OOOOoOoo0O0O0 :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in iIIi1i1 ) :
    o0O += 1
    III1iII1I1ii = "Link " + str ( o0O ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    OOOo00oo0oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     OOO0OOO00oo ( "[COLOR skyblue]" + III1iII1I1ii + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in i1IIIiiII1 ) :
     OOO0OOO00oo ( "[COLOR yellow]" + III1iII1I1ii + url + "[/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
    else :
     OOO0OOO00oo ( "[COLOR skyblue]" + III1iII1I1ii + url + "[/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
     if 1 - 1: O0Oooo00 - iIii1 . oOoO . O0Oooo00 / i1iIii1Ii1II + oOoO
     if 78 - 78: O0 . iIii1 . O0Oo0oO0o % IiI1I1
     if 49 - 49: iiIiIIi / O0Oooo00 . O0Oo0oO0o
def ooOOoooooo ( url ) :
 if 1 - 1: i1iIii1Ii1II / Ii1Ii1iiii11 % iI * I11iii . i11iIiiIii
 if url == 'Football' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  III1Iiii1I11 = Iii111II ( 'http://wizhdsports.is/sport/Cricket' )
 OOooO = dom_parser2 . parse_dom ( III1Iiii1I11 , 'div' , { 'class' : 'card' } )
 OOooO = [ ( dom_parser2 . parse_dom ( IIII , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( IIII , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( IIII , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( IIII , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for IIII in OOooO ]
 if len ( OOooO ) < 1 :
  OOO0OOO00oo ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , IIIii1II1II , Oo , '' )
 OOooO = [ ( IIII [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , IIII [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , IIII [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , IIII [ 2 ] [ 0 ] . content ) if IIII [ 2 ] else 'Upcoming' , IIII [ 3 ] [ 0 ] . content ) for IIII in OOooO ]
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - Ii1Ii1iiii11
 if 91 - 91: iI % i1IIi % iIii1I11I1II1
 if 20 - 20: IiI1I1 % iiIiIIi / iiIiIIi + iiIiIIi
 if 45 - 45: iIii1 - I11iii - OoooooooOO - O0Oooo00 . O0Oo0oO0o / O0
 OOooO = [ ( IIII [ 0 ] , IIII [ 1 ] , IIII [ 2 ] , IIII [ 3 ] , IIII [ 4 ] ) for IIII in OOooO ]
 oo0o00O = 0
 o00O0OoO = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for IIII in OOooO :
  i1I = IIII [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( oo0o00O ) )
  oo0o00O += 1
  time . sleep ( 0.10 )
  i1I = OoOO ( i1I )
  ooOOO0 = IIII [ 1 ]
  o0o = IIII [ 3 ]
  if 'Match Over' in o0o :
   o00O0OoO += 1
  O0OOoO00OO0o = dom_parser2 . parse_dom ( IIII [ 4 ] , 'a' )
  for III1Iiii1I11 in O0OOoO00OO0o :
   I1111IIIIIi = re . sub ( '<.+?>' , '' , III1Iiii1I11 . content )
   OooO0OO = III1Iiii1I11 . attrs [ 'href' ]
   OooO0OO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + OooO0OO
   if not 'Match Over' in o0o :
    OOO0OOO00oo ( '[COLOR aqua]' + i1I + '[COLOR yellow]' + ' ' + o0o + '[/COLOR]' , OooO0OO , 2 , IIIii1II1II , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( oo0o00O ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( o00O0OoO ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * iI % i11iIiiIii * II1iI
def oo000o ( url ) :
 if 44 - 44: i1IIi % O0Oo0oO0o + oOoO
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 iiii11I = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( o0O ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  if 45 - 45: iI / iI + OO0O00 + o0o0O00O00o0
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 47 - 47: Ii1Ii1iiii11 + o0o0O00O00o0
 try :
  OoO = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( OooO0OO ) [ 0 ]
  I1IiI = IIIii1II1II
  i1I1iI ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 18 , IIIii1II1II , Oo , '' )
 except : pass
 if 88 - 88: iI . O0Oo0oO0o * O0Oo0oO0o % OO0O00
def iiIIiiIi1Ii11 ( url , iconimage , fanart ) :
 if 65 - 65: O0Oo0oO0o . IiI1I1 % oOoO . i11iIiiIii + O0
 OOO0OOO00oo ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 iiii11I = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( OooO0OO )
 if 26 - 26: oOoO - iIii1I11I1II1 - II1iI / O0Oooo00 . I111i1i1111i % iIii1I11I1II1
 for o0O in iiii11I :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( o0O ) [ 0 ]
  OOOo00oo0oO = str . lower ( url )
  if '1e' in OOOo00oo0oO :
   III1iII1I1ii = '1st Half'
  else :
   III1iII1I1ii = '2nd Half'
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 91 - 91: Ii1Ii1iiii11 . iIii1I11I1II1 / iIii1 + i1IIi
def I1i ( ) :
 if 53 - 53: I1I1i1 * I111i1i1111i + o0o0O00O00o0 - O0Oo0oO0o
 ii1i1I1i = 'http://www.goalsarena.org/en/'
 OooO0OO = Iii111II ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiii11I = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( iiii11I )
 for Ii1I1I1i1Ii , i1 in I1I11i :
  i1I1iI ( "[COLOR skyblue]" + i1 + "[/COLOR]" , Ii1I1I1i1Ii , 21 , I1IiI , Oo , '' )
  if 52 - 52: O0Oo0oO0o - OoooooooOO % iiIiIIi + II1iI * i1iIii1Ii1II . I11iii
def O0OO0O ( url ) :
 if 81 - 81: iIii1 . Ii1Ii1iiii11 % O0 / II1iI - iIii1
 if 43 - 43: i11iIiiIii + i1iIii1Ii1II * O0Oo0oO0o * OO0O00 * O0
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11IiI1I11i1i = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if I11IiI1I11i1i == 0 :
  try :
   iiii11I = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in iiii11I :
   o00oO0oo0OO ( ii11i1 , iiii11I , IIIii1II1II )
  O0O0OOOOoo = Iii111II ( iiii11I )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
  url = 'https:' + url
  oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = IIIii1II1II , thumbnailImage = IIIii1II1II )
  xbmc . Player ( ) . play ( url , oOooO0 , False )
  quit ( 0 )
 if I11IiI1I11i1i == 1 :
  try :
   iiii11I = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0OO ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   O0OO0O ( url )
  O0O0OOOOoo = Iii111II ( iiii11I )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
  url = 'https:' + url
  oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = IIIii1II1II , thumbnailImage = IIIii1II1II )
  xbmc . Player ( ) . play ( url , oOooO0 , False )
  quit ( 0 )
  if 29 - 29: iIii1I11I1II1 + I111i1i1111i * O0Oooo00 * IiI1I1 . II1iI * II1iI
def I111I1Iiii1i ( ) :
 if 56 - 56: I1I1i1 % O0 - II1iI
 ii1i1I1i = 'http://m.liveatc.net/feeds/'
 OooO0OO = O00o0OO0 ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'http://m.liveatc.net' + ii1i1I1i
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 7 , I1IiI , Oo , '' )
  if 35 - 35: iIii1 % o0o0O00O00o0 / OO0O00 + iIii1I11I1II1 . OoooooooOO . II1iI
def o00oOOooOOo0o ( url ) :
 if 66 - 66: iI - iI - i11iIiiIii . I1I1i1 - IiI1I1
 if 77 - 77: I111i1i1111i - O0Oo0oO0o - o0o0O00O00o0
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 49 - 49: O0Oo0oO0o % O0 . I111i1i1111i + iIii1 / II1iI
def O0oOOoOooooO ( url ) :
 url = url . replace ( ' ' , '%20' )
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li>(.+?)</a>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '(.+?)</li>' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 62 - 62: OoooooooOO * II1iI
def oOOOoo0O0oO ( url ) :
 if 6 - 6: IiI1I1 * Ii1Ii1iiii11 + iI
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  try :
   III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
   OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   OOO0OOO00oo ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 44 - 44: iiIiIIi % O0Oooo00 + OoooooooOO - O0 - iiIiIIi - O0Oo0oO0o
def O0Oo0oOOoooOOOOo ( ) :
 if 62 - 62: o0o0O00O00o0
 i1I1iI ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 ii1i1I1i = 'http://m.broadcastify.com/?a=la&coid=1'
 OooO0OO = O00o0OO0 ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'http://m.broadcastify.com' + ii1i1I1i
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 12 , I1IiI , Oo , '' )
  if 74 - 74: iI + Ii1Ii1iiii11
def oO00O000oO0 ( url ) :
 if 79 - 79: oOoO - OoooooooOO - iIii1 - iIii1I11I1II1 * IiI1I1
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 4 - 4: i11iIiiIii . OoooooooOO / O0Oooo00 % OO0O00 % oOoO * O0
def iIIii ( url ) :
 if 92 - 92: iiIiIIi + iIii1 % IiI1I1
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 62 - 62: I1I1i1 / i1IIi
def oo0oO ( url ) :
 if 94 - 94: iIii1I11I1II1 / i1iIii1Ii1II % iI * iI * O0Oo0oO0o
 OooO0OO = O00o0OO0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  iiii11I = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 IIiIiI ( iiii11I )
 if 94 - 94: iIii1 . i1IIi - Ii1Ii1iiii11 % O0 - O0Oooo00
def ooO0O00Oo0o ( ) :
 if 65 - 65: I1I1i1 . oOoO - OO0O00 * I11iii / OO0O00 / o0o0O00O00o0
 ii1i1I1i = 'http://m.broadcastify.com/?a=top25'
 OooO0OO = O00o0OO0 ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  i111iIi1i1II1 = III1iII1I1ii . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  III1iII1I1ii = III1iII1I1ii . split ( ')' ) [ - 1 ] . strip ( )
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'http://m.broadcastify.com' + ii1i1I1i
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[COLOR yellow] :: " + i111iIi1i1II1 + " Listening" + "[/COLOR]" , ii1i1I1i , 14 , I1IiI , Oo , '' )
  if 86 - 86: iIii1I11I1II1 / I111i1i1111i . O0Oo0oO0o
def II1i111Ii1i ( url ) :
 if 15 - 15: O0Oo0oO0o / i1IIi
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( o0O ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( o0O ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in III1iII1I1ii :
    OOOo00oo0oO = 'https://www.youtube.com' + url
    OOO0OOO00oo ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
    if 7 - 7: II1iI
def I1ii1iIiii1I ( ) :
 if 42 - 42: Ii1Ii1iiii11 + i1IIi - iiIiIIi / I11iii
 ii1i1I1i = 'http://burningwhee1s.blogspot.co.uk/'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( iiii11I )
 for OooO0OO , III1iII1I1ii in I1I11i :
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OooO0OO , 24 , I1IiI , Oo , '' )
  if 9 - 9: O0 % O0 - Ii1Ii1iiii11
def OoOiiI1IIIi ( url ) :
 if 47 - 47: i1iIii1Ii1II % oOoO % i11iIiiIii - O0 + o0o0O00O00o0
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( o0O ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 94 - 94: OO0O00
def i11II1I11I1 ( url , iconimage ) :
 if 67 - 67: II1iI - Ii1Ii1iiii11 / oOoO - i1IIi
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( iiii11I )
 try :
  for o0O in I1I11i :
   III1iII1I1ii = re . compile ( '<b>(.+?)</b>' ) . findall ( o0O ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    i1II1 = re . compile ( '<b>(.+?)</b>' ) . findall ( o0O ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     i1II1 = re . compile ( '<b>(.+?)</b>' ) . findall ( o0O ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     i1II1 = ''
   III1iII1I1ii = O0oO0 ( III1iII1I1ii )
   i1II1 = O0oO0 ( i1II1 )
   i11i1 = re . compile ( '<option value="(.+?)"' ) . findall ( o0O ) [ 1 ]
   OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "  " + i1II1 + "[/COLOR]" , i11i1 , 2 , I1IiI , Oo , '' )
 except :
  OOO0OOO00oo ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1I1i1 . i11iIiiIii % oOoO
def i1iI ( ) :
 if 29 - 29: II1iI % IiI1I1 - II1iI / IiI1I1 . i1IIi
 ii1i1I1i = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 OooO0OO = Iii111II ( ii1i1I1i )
 oo0OooOOo0 = json . loads ( OooO0OO )
 i11III1111iIi = oo0OooOOo0 [ 'results' ]
 for I1i111I in i11III1111iIi :
  try :
   Ooo = 'https://image.tmdb.org/t/p/original'
   III1iII1I1ii = I1i111I [ 'title' ]
   I1IiI = I1i111I [ 'poster_path' ]
   Oo0oo0O0o00O = I1i111I [ 'id' ]
   I1IiI = Ooo + I1IiI
   I1ii11iIi11i = I1i111I [ 'backdrop_path' ]
   I1ii11iIi11i = Ooo + I1ii11iIi11i
   I1i11 = I1i111I [ 'overview' ]
   Oo0oo0O0o00O = str ( Oo0oo0O0o00O )
   i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , III1iII1I1ii , 33 , I1IiI , I1ii11iIi11i , I1i11 )
  except : pass
  if 12 - 12: i1IIi + i1IIi - I1I1i1 * i1iIii1Ii1II % i1iIii1Ii1II - O0Oo0oO0o
def o0OOOOooo ( url ) :
 if 94 - 94: OoooooooOO + i1iIii1Ii1II / I111i1i1111i * IiI1I1
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = re . compile ( '<i>(.+?)</i>' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = III1iII1I1ii . strip ( )
  i1I1iI ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( OooO0OO ) [ 0 ]
  o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  i1I1iI ( '[COLOR yellow]Next Page >>[/COLOR]' , o0OOo0o0O0O , 26 , o0 , I1ii11iIi11i )
 except : pass
 if 95 - 95: O0Oooo00 % i1IIi * i11iIiiIii % i1iIii1Ii1II - iIii1
def OOoOoOo ( url , iconimage ) :
 if 98 - 98: iI
 OooO0OO = Iii111II ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( OooO0OO ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 iiii11I = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( OooO0OO )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 IIII = 1
 OooooO0oOOOO = [ ]
 for o0O in iiii11I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  OooooO0oOOOO . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( IIII ) )
  time . sleep ( 0.02 )
  IIII += 1
  III1iII1I1ii = re . compile ( '(.+?)</p>' ) . findall ( o0O ) [ 0 ] . replace ( 'Server' , '' )
  III1iII1I1ii = III1iII1I1ii . strip ( )
 o0O00oOOoo = 1
 iIii11I = 0
 i1I1iIi = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 22 - 22: I111i1i1111i * O0 . I11iii * i11iIiiIii - II1iI * o0o0O00O00o0
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if iIii11I > len ( OooooO0oOOOO ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 59 - 59: i1iIii1Ii1II % OoooooooOO . iI / I11iii + II1iI
  if i1I1iIi == 0 :
   iIii11I += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( iIii11I ) + "[/COLOR]" , '' )
   try :
    OooO0OO = Iii111II ( OooooO0oOOOO [ iIii11I ] )
    I1I11i = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
    o0O0oO0O00O0o = base64 . b64decode ( I1I11i )
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O0oO0O00O0o ) [ 0 ]
    II1I1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    Ooo0O0oooo = open ( II1I1Ii ) . read ( )
    iiI = re . compile ( '<url>(.+?)</url>' ) . findall ( Ooo0O0oooo )
    for oOIIiIi in iiI :
     OOoOooOoOOOoo = re . compile ( '<bad>(.+?)<bad>' ) . findall ( oOIIiIi ) [ 0 ]
     if url == OOoOooOoOOOoo :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( iIii11I ) )
      time . sleep ( 0.5 )
      i1I1iIi = 5
      pass
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     Iiii1iI1i = liveresolver . resolve ( url )
    else : Iiii1iI1i = url
    oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( Iiii1iI1i , oOooO0 , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( iIii11I ) )
    time . sleep ( 0.5 )
    i1I1iIi = 5
    pass
  if i1I1iIi == 5 :
   i1I1iIi = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   i1I1iIi += 1
   if 34 - 34: o0o0O00O00o0 * II1iI . i1IIi * o0o0O00O00o0 / o0o0O00O00o0
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 II1I1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 OOO00O = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if OOO00O :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( II1I1Ii , "a" ) as IIiI1Ii :
   IIiI1Ii . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 57 - 57: IiI1I1 - o0o0O00O00o0 - oOoO + O0Oooo00
def I1IIIiI11i1 ( url ) :
 if 48 - 48: OO0O00 - Ii1Ii1iiii11 % iiIiIIi
 if 36 - 36: iIii1 - iiIiIIi . i1iIii1Ii1II - i11iIiiIii - IiI1I1 * i1iIii1Ii1II
 if url == 'search' :
  OooOOOO = ''
  iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , 'Enter Search Term' )
  iIIIiiI1i1i . doModal ( )
  if iIIIiiI1i1i . isConfirmed ( ) :
   OooOOOO = iIIIiiI1i1i . getText ( )
   if len ( OooOOOO ) > 1 :
    iIII = OooOOOO . lower ( )
    if 70 - 70: iI / iIii1I11I1II1
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , IIIii1II1II , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , IIIii1II1II , 5000 )
   quit ( )
  iIII = iIII . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + iIII + '.html'
  Oo0oooO0oO ( url , I1IiI )
  if 19 - 19: i11iIiiIii + OoooooooOO - i1iIii1Ii1II - oOoO
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  Oo0oooO0oO ( url , I1IiI )
  if 21 - 21: O0 % I11iii . II1iI / O0Oo0oO0o + I11iii
def Oo0oooO0oO ( url , icon ) :
 if 53 - 53: iIii1 - II1iI - iIii1 * iI
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = re . compile ( '<i>(.+?)</i>' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  i1I1iI ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 71 - 71: O0 - iIii1I11I1II1
def i1II ( ) :
 if 14 - 14: iIii1 / iIii1 % o0o0O00O00o0
 ii1i1I1i = 'http://www.genti.stream/'
 OooO0OO = Iii111II ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  ooO = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( o0O ) [ 0 ] . strip ( )
  ii = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( o0O ) [ 1 ] . strip ( )
  ii1i1I1i = re . compile ( 'href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'http://www.genti.stream/' + ii1i1I1i
  OOO0OOO00oo ( "[COLOR aqua]" + ooO + "[COLOR yellow] vs [COLOR aqua]" + ii + "[/COLOR]" , ii1i1I1i , 39 , I1IiI , I1ii11iIi11i )
  if 82 - 82: I111i1i1111i - O0Oooo00 % I111i1i1111i * i11iIiiIii . O0Oo0oO0o % O0Oo0oO0o
def o00Ooo0 ( url ) :
 if 83 - 83: i11iIiiIii % Ii1Ii1iiii11 % o0o0O00O00o0
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1II1I11i1 = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
 if not 'http' in Ii1II1I11i1 :
  Ii1II1I11i1 = 'http://www.genti.stream' + Ii1II1I11i1
 Ii1I1I1i1Ii = Iii111II ( Ii1II1I11i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oOoooooOoO = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( Ii1I1I1i1Ii ) [ 0 ]
 O0O0OOOOoo = Iii111II ( oOoooooOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( O0O0OOOOoo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( O0O0OOOOoo ) [ 0 ]
 except : pass
 if 33 - 33: O0Oo0oO0o / o0o0O00O00o0 * O0 % iiIiIIi * OO0O00
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , IIIii1II1II , 5000 )
  quit ( )
 o00oO0oo0OO ( ii11i1 , url , IIIii1II1II )
 if 100 - 100: I11iii . oOoO / iiIiIIi % I111i1i1111i % O0Oo0oO0o - O0Oooo00
 if 46 - 46: O0 * O0Oo0oO0o - i1iIii1Ii1II * o0o0O00O00o0
def i11IIIiIiIi ( url ) :
 if 27 - 27: I1I1i1 + I111i1i1111i - IiI1I1 + O0 . iiIiIIi
 url = 'http://www.toonget.net/cartoon'
 OooO0OO = Iii111II ( url )
 I1I11i = re . compile ( '<td><a href="(.+?)">(.+?)</a>' ) . findall ( OooO0OO )
 for url , III1iII1I1ii in I1I11i :
  i1I1iI ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 46 - 46: I11iii
def ii1iIi1iIiI1i ( url ) :
 if 40 - 40: i1IIi % IiI1I1
 OooO0OO = Iii111II ( url )
 try :
  I1IiI = re . compile ( '<div class="left_col">.+?<img src="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
 except :
  I1IiI = IIIii1II1II
 try :
  ooo0o00 = re . compile ( '<span>Description:</span>.+?<div>(.+?)</div>' ) . findall ( OooO0OO ) [ 0 ] . strip ( )
 except :
  ooo0o00 = 'No Description Found'
 iiii11I = re . compile ( '<div id="videos">(.+?)</div>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<li>.+?<a href="(.+?)">(.+?)</a>' ) . findall ( iiii11I )
 for url , III1iII1I1ii in I1I11i :
  i1I1iI ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , ooo0o00 )
  if 99 - 99: O0 . oOoO + iIii1I11I1II1
 try :
  I11 = re . compile ( '<ul class="pagination">(.+?)</ul>' ) . findall ( OooO0OO ) [ 0 ] . strip ( )
  IIi = re . compile ( 'href="(.+?)"' ) . findall ( I11 ) [ 0 ]
  i1I1iI ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , IIi , 30 , IIIii1II1II , I1ii11iIi11i )
 except : pass
 if 66 - 66: iIii1 % O0Oooo00 . IiI1I1
def o0OIiiiI ( url ) :
 if 61 - 61: IiI1I1 % IiI1I1 * Ii1Ii1iiii11 / Ii1Ii1iiii11
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0OO )
 IIII = 0
 for o0oOO in iiii11I :
  IIII += 1
  III1iII1I1ii = 'Stream : ' + str ( IIII )
  OOO0OOO00oo ( III1iII1I1ii , o0oOO , 32 , IIIii1II1II , I1ii11iIi11i )
  if 53 - 53: OO0O00 * I11iii . i1iIii1Ii1II - iiIiIIi % iiIiIIi * i11iIiiIii
def iiOOO0oOOoo ( url ) :
 if 52 - 52: Ii1Ii1iiii11 % i1iIii1Ii1II
 OooO0OO = Iii111II ( url )
 if 'easyvideome' in url or 'videozoo' in url :
  Oo000ooOOO = re . compile ( 'file:.+?"(.+?)"' ) . findall ( OooO0OO ) [ 1 ]
  o00oO0oo0OO ( ii11i1 , Oo000ooOOO , IIIii1II1II )
 elif 'playpandanet' in url :
  Oo000ooOOO = re . compile ( """url:.+?'(.+?)'""" ) . findall ( OooO0OO ) [ 0 ]
  o00oO0oo0OO ( ii11i1 , Oo000ooOOO , IIIii1II1II )
 else :
  Iii1ii1II11i . notification ( o0OoOoOO00 , 'Sorry This Link Is Down, Try Another' , IIIii1II1II , 4000 )
  if 31 - 31: iIii1I11I1II1 % oOoO % o0o0O00O00o0 . iiIiIIi - oOoO
  if 17 - 17: iiIiIIi
def Ii1ii1IiIII ( ) :
 if 57 - 57: iIii1I11I1II1 / oOoO - i1IIi
 ii1i1I1i = "http://www.loyalbooks.com/genre-menu"
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( OooO0OO )
 for Ooo0OO0oOO in iiii11I :
  if "paid" not in Ooo0OO0oOO :
   Ii1I1I1i1Ii = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
   O0O0OOOOoo = "http://www.loyalbooks.com" + Ii1I1I1i1Ii
   ii11i1 = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
   i1I1iI ( "[COLOR aqua]" + ii11i1 + "[/COLOR]" , O0O0OOOOoo , 60 , I1IiI , Oo , '' )
   if 51 - 51: I11iii
def ii11I1 ( url ) :
 if 75 - 75: O0Oooo00 / O0Oo0oO0o % O0
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( OooO0OO ) [ 0 ]
 Ii111iIi1iIi = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( iiii11I )
 for Ooo0OO0oOO in Ii111iIi1iIi :
  OOOo00oo0oO = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
  O0O0OOOOoo = "http://www.loyalbooks.com" + OOOo00oo0oO
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
  IIIii1II1II = "http://www.loyalbooks.com" + I1IiI
  ii11i1 = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + ii11i1 + "[/COLOR]" , O0O0OOOOoo , 61 , IIIii1II1II , Oo , '' )
 try :
  OooO0OO = Iii111II ( url )
  OoO = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( OooO0OO ) [ 0 ]
  I1IiI = 'https://i.imgur.com/pOefPvV.jpg'
  i1I1iI ( "[COLOR yellow]Next Page -->[/COLOR]" , OoO , 60 , I1IiI , Oo , '' )
 except : pass
 if 21 - 21: iIii1 / I1I1i1 + iiIiIIi + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + iI + o0o0O00O00o0 * i11iIiiIii
def OoOoOo00o0 ( name , url , iconimage ) :
 if 90 - 90: i1iIii1Ii1II % O0 * iIii1I11I1II1 . iI
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( OooO0OO )
 for Ooo0OO0oOO in iiii11I :
  III1iII1I1ii = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
  OOOo00oo0oO = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( Ooo0OO0oOO ) [ 0 ]
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OOOo00oo0oO , 10 , iconimage , Oo , '' )
  if 8 - 8: o0o0O00O00o0 + O0Oo0oO0o / iI / oOoO
def ooo0O ( ) :
 if 16 - 16: I111i1i1111i
 ii1i1I1i = 'http://www.shadownet.me/'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( iiii11I )
 for ii1i1I1i , III1iII1I1ii in I1I11i :
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  if 'P2P' not in III1iII1I1ii :
   i1I1iI ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 49 , I1IiI , Oo , '' )
   if 41 - 41: i1IIi * O0Oo0oO0o / OoooooooOO . IiI1I1
   if 83 - 83: iI . O0 / i1iIii1Ii1II / IiI1I1 - O0Oo0oO0o
def oO0oO0 ( url ) :
 if 14 - 14: iI
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( iiii11I )
 for o0O in I1I11i :
  III1iII1I1ii = re . compile ( 'alt="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  OOO0OOO00oo ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( OooO0OO ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  i1I1iI ( "[COLOR orange]Next Page --->[/COLOR]" , o0OOo0o0O0O , 49 , I1IiI , Oo , '' )
 except : pass
 if 99 - 99: iI
def IIi1ii1Ii ( url ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + iI - i11iIiiIii + IiI1I1
 def ii1i ( url ) :
  oOoOo00oOo = urllib2 . Request ( url )
  oOoOo00oOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  oOoOo00oOo . add_header ( 'Referer' , url )
  Ooo00O00O0O0O = urllib2 . urlopen ( oOoOo00oOo , timeout = 5 )
  OooO0OO = Ooo00O00O0O0O . read ( )
  Ooo00O00O0O0O . close ( )
  return OooO0OO
  if 62 - 62: O0Oooo00 / I1I1i1
 OooO0OO = ii1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iiii11I = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( OooO0OO ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in iiii11I :
  url = iiii11I
  o00oO0oo0OO ( ii11i1 , url , IIIii1II1II )
 O0O0OOOOoo = ii1i ( iiii11I )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 7 - 7: OoooooooOO . I11iii
 import liveresolver
 import resolveurl
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
  oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = IIIii1II1II , thumbnailImage = IIIii1II1II )
  oOooO0 . setPath ( Iiii1iI1i )
  xbmc . Player ( ) . play ( Iiii1iI1i , oOooO0 , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = IIIii1II1II , thumbnailImage = IIIii1II1II )
  oOooO0 . setPath ( Iiii1iI1i )
  xbmc . Player ( ) . play ( Iiii1iI1i , oOooO0 , False )
 else :
  if '.m3u8' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + ii11i1 + '&amp;url=' + url + '&amp;iconImage=' + IIIii1II1II
  elif '.ts' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + ii11i1 + '&amp;url=' + url + '&amp;iconImage=' + IIIii1II1II
  else :
   OOOo00oo0oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 53 - 53: iiIiIIi % iiIiIIi * Ii1Ii1iiii11 + I111i1i1111i
  oOooO0 = xbmcgui . ListItem ( ii11i1 , iconImage = IIIii1II1II , thumbnailImage = IIIii1II1II )
  oOooO0 . setPath ( url )
  if 92 - 92: OoooooooOO + i1IIi / iiIiIIi * O0
  xbmc . Player ( ) . play ( OOOo00oo0oO , oOooO0 , False )
  if 100 - 100: o0o0O00O00o0 % iIii1I11I1II1 * O0Oo0oO0o - iI
  if 92 - 92: o0o0O00O00o0
def II11iI111i1 ( ) :
 if 95 - 95: OoooooooOO - I11iii * II1iI + I111i1i1111i
 ii1i1I1i = 'https://m.skylinewebcams.com/en/webcam'
 OooO0OO = Iii111II ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I11i = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( OooO0OO ) [ 0 ]
 iIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I11i )
 for ii1i1I1i , III1iII1I1ii in iIi1 :
  if 'http|https' not in ii1i1I1i :
   ii1i1I1i = 'https://m.skylinewebcams.com' + ii1i1I1i
   i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 46 , I1IiI , Oo , '' )
   if 21 - 21: oOoO
def OoO00 ( url ) :
 if 85 - 85: i1iIii1Ii1II * i1iIii1Ii1II * II1iI . OoooooooOO . iiIiIIi * o0o0O00O00o0
 OooO0OO = Iii111II ( url )
 I1I11i = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( OooO0OO )
 for url , I1IiI , III1iII1I1ii in I1I11i :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 65 - 65: IiI1I1 * OO0O00
  if 79 - 79: OoooooooOO - II1iI
def o00O00oO00 ( name , url , iconimage ) :
 if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * I11iii
 OooO0OO = Iii111II ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  iiii11I = re . compile ( '<amp-video src="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
  url = 'https:' + iiii11I
  oOooO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , oOooO0 , False )
  if 9 - 9: I11iii - O0Oo0oO0o + O0 / iIii1I11I1II1 / i11iIiiIii
 except : pass
 quit ( 0 )
 if 39 - 39: I11iii * i1iIii1Ii1II + iIii1I11I1II1 - I11iii + IiI1I1
def o0iiiI1I1iIIIi1 ( ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / oOoO % O0Oo0oO0o % i1IIi / i11iIiiIii
 ii1i1I1i = 'https://watchepisodeseries.unblocked.vet/home/schedule'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( iiii11I )
 for ii1i1I1i , OOOIiiiii1iI , IIiooOooo0 in I1I11i :
  i1I1iI ( "[COLOR aqua]" + OOOIiiiii1iI + "  " + IIiooOooo0 + "[/COLOR]" , ii1i1I1i , 67 , I1IiI , I1ii11iIi11i )
  if 67 - 67: II1iI
  if 55 - 55: I1I1i1 - iI * Ii1Ii1iiii11 + I111i1i1111i * I111i1i1111i * O0
def O000Oo0o ( url ) :
 if 99 - 99: iIii1I11I1II1 % o0o0O00O00o0 + o0o0O00O00o0 + iI - OO0O00 / OO0O00
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 1 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  IIIii1II1II = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( o0O ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( o0O ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 68 , IIIii1II1II , I1ii11iIi11i )
  if 7 - 7: II1iI + I111i1i1111i / I11iii
  if 79 - 79: O0Oooo00 - iIii1I11I1II1 + iiIiIIi - OO0O00
def OoOiIIiii ( url , iconimage , fanart ) :
 if 61 - 61: I11iii . i1IIi / OO0O00 % i11iIiiIii * iI
 OooO0OO = Iii111II ( url )
 i1i1i1I = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in i1i1i1I :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( o0O ) [ 0 ]
 iiii11I = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( OooO0OO )
 IIII = datetime . now ( )
 for o0O in iiii11I :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ] . replace ( '////' , '//' )
   III1iII1I1ii = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
   III1iII1I1ii = O0oO0 ( III1iII1I1ii )
   oOoo000 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
   OooOo00o = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
   OOOIiiiii1iI = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( o0O ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in OOOIiiiii1iI :
    OOOIiiiii1iI = OOOIiiiii1iI . strip ( )
    OOOIiiiii1iI = time . strptime ( OOOIiiiii1iI , "%d/%m/%Y" )
    IiI11i1IIiiI = ( "%s/%s/%s" % ( IIII . day , IIII . month , IIII . year ) )
    IiI11i1IIiiI = time . strptime ( IiI11i1IIiiI , "%d/%m/%Y" )
    if ( IiI11i1IIiiI < OOOIiiiii1iI ) :
     III1iII1I1ii = '[COLOR yellow]' + ( III1iII1I1ii ) + ' - Not Aired Yet' + '[/COLOR]'
     OooOo00o = '[COLOR yellow]' + ( OooOo00o ) + '[/COLOR]'
     oOoo000 = '[COLOR yellow]' + ( oOoo000 ) + '[/COLOR]'
     if 60 - 60: I1I1i1 * II1iI
    if not 'Season 0' in oOoo000 :
     i1I1iI ( "[COLOR aqua]" + oOoo000 + " " + OooOo00o + " " + III1iII1I1ii + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 17 - 17: IiI1I1 % i1iIii1Ii1II / I1I1i1 . I11iii * IiI1I1 - O0Oo0oO0o
  if 41 - 41: iiIiIIi
def oOOoo0o0OOOO ( url , iconimage , fanart ) :
 if 26 - 26: iI % iIii1I11I1II1 + Ii1Ii1iiii11
 if 67 - 67: iIii1 + O0Oo0oO0o - O0 . iIii1 * O0Oo0oO0o * oOoO
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  try :
   III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
   III1iII1I1ii = III1iII1I1ii . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
   if not 'Lolzor.Com' in III1iII1I1ii :
    if not 'Videoplayer.Gq' in III1iII1I1ii :
     if not 'Vidbaba.Com' in III1iII1I1ii :
      if not 'Gagomatic.Com' in III1iII1I1ii :
       if not 'Favour.Me' in III1iII1I1ii :
        if not 'Funblr.Com' in III1iII1I1ii :
         if not 'Vid.Ag' in III1iII1I1ii :
          if not 'Mycollection.Net' in III1iII1I1ii :
           if not 'Adhqmedia.Com' in III1iII1I1ii :
            if not 'Filenuke.Com' in III1iII1I1ii :
             if not 'Mrfile.Me' in III1iII1I1ii :
              OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 90 - 90: iiIiIIi . I11iii
  if 81 - 81: IiI1I1 - oOoO % o0o0O00O00o0 - O0Oooo00 / i1iIii1Ii1II
def Ii1iI111 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 url = url . replace ( '////' , '//' )
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  import resolveurl
  try :
   if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
    Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    Iiii1iI1i = liveresolver . resolve ( url )
   else : Iiii1iI1i = url
   oOooO0 = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   oOooO0 . setPath ( Iiii1iI1i )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOooO0 )
   xbmc . Player ( ) . play ( Iiii1iI1i )
   if 51 - 51: I11iii * O0 / O0Oo0oO0o . iiIiIIi % IiI1I1 / II1iI
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 9 - 9: II1iI % II1iI % O0Oo0oO0o
def I1I1i1I ( ) :
 if 87 - 87: O0 / iIii1I11I1II1 * i1IIi
 OooOOOO = ''
 iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , 'Enter Search Term' )
 iIIIiiI1i1i . doModal ( )
 if iIIIiiI1i1i . isConfirmed ( ) :
  OooOOOO = iIIIiiI1i1i . getText ( )
  if len ( OooOOOO ) > 1 :
   iIII = OooOOOO . lower ( )
   iIII = iIII . replace ( ' ' , '%20' )
   if 41 - 41: I111i1i1111i * oOoO / I111i1i1111i % iIii1
  else : quit ( )
 else : iIII = urllib . unquote_plus ( ii1i1I1i ) . lower ( ) ; OooOOOO = urllib . unquote_plus ( ii1i1I1i )
 ii1i1I1i = base64 . b64decode ( b'aHR0cHM6Ly93YXRjaGVwaXNvZGVzZXJpZXMuYnlwYXNzZWQuZXUvaG9tZS9zZWFyY2g/cT0=' ) + iIII
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '"series"(.+?)"series_id"' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( 'original_name":"(.+?)"' ) . findall ( o0O ) [ 0 ]
  OOOo00oo0oO = re . compile ( '"seo_name":"(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'https://watchepisodeseries.bypassed.eu/' + OOOo00oo0oO
  I1IiI = 'https://watchepisodeseries.bypassed.eu/series_images/' + OOOo00oo0oO + '.jpg'
  i1I1iI ( III1iII1I1ii , ii1i1I1i , 68 , I1IiI , I1ii11iIi11i , '' )
  if 18 - 18: O0Oo0oO0o . OoooooooOO % I111i1i1111i % iiIiIIi
def II1IiiIii ( ) :
 if 84 - 84: iIii1 % i1IIi
 ii1i1I1i = 'https://watchepisodeseries.bypassed.eu/home/popular-series'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<div title="(.+?)"' ) . findall ( o0O ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ] . replace ( '////' , '//' )
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( o0O ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( o0O ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  i1I1iI ( '[COLOR aqua]' + III1iII1I1ii + '[/COLOR]' , ii1i1I1i , 68 , I1IiI , I1ii11iIi11i )
  if 70 - 70: i1iIii1Ii1II . OoooooooOO - iI
  if 30 - 30: I1I1i1 % II1iI
def O0Oo00 ( ) :
 if 41 - 41: iIii1I11I1II1 % oOoO
 try :
  oOo0oO = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OooOOOO = ''
  iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  iIIIiiI1i1i . doModal ( )
  if iIIIiiI1i1i . isConfirmed ( ) :
   OooOOOO = iIIIiiI1i1i . getText ( )
   if len ( OooOOOO ) > 1 :
    iIII = OooOOOO
   else : quit ( )
  if iIII == oOo0oO :
   IIi1IIIIi ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   I1i1I1II ( )
 except IOError :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  OooOOOO = ''
  iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , 'Enter The Password You Set' )
  iIIIiiI1i1i . doModal ( )
  if iIIIiiI1i1i . isConfirmed ( ) :
   OooOOOO = iIIIiiI1i1i . getText ( )
   if len ( OooOOOO ) > 1 :
    iIII = OooOOOO
   else : quit ( )
  with open ( i1i1II , "w" ) as IIiI1Ii :
   IIiI1Ii . write ( iIII )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   I1i1I1II ( )
   if 70 - 70: IiI1I1 / O0Oo0oO0o - iIii1I11I1II1 - iI
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . O0Oo0oO0o / i1IIi - oOoO
   if 30 - 30: I111i1i1111i
def IIi1IIIIi ( ) :
 if 21 - 21: i11iIiiIii / OO0O00 % IiI1I1 * O0 . oOoO - iIii1I11I1II1
 iiIiiii1i1i1i = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 OOOO = '[COLOR aqua]Asian Special Porn[/COLOR]'
 i1I1iI ( OOOO , iiIiiii1i1i1i , 1 , I1IiI , Oo , '' )
 ii1i1I1i = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<li class="">(.+?)</li>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( o0O ) [ 0 ]
  ooO0oO00O0o = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( o0O ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'https://www.eporner.com' + OOOo00oo0oO
  if not 'All' in III1iII1I1ii :
   if not 'Homemade' in III1iII1I1ii :
    i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "  " + "[COLOR yellow]" + ooO0oO00O0o + "[/COLOR]" , ii1i1I1i , 36 , I1IiI , Oo , '' )
    if 70 - 70: OO0O00
def i11iIIi11 ( url ) :
 if 98 - 98: OO0O00
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( o0O ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( o0O ) [ 0 ]
  url = 'https://www.eporner.com' + OOOo00oo0oO
  i1I1iI ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 12 - 12: O0Oo0oO0o . oOoO / IiI1I1
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( OooO0OO ) [ 0 ]
  OoO = 'https://www.eporner.com' + o0OOo0o0O0O
  o0 = 'http://imgur.com/3eNoY0p'
  i1I1iI ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 36 , o0 , Oo , '' )
 except : pass
 if 77 - 77: o0o0O00O00o0 - II1iI % oOoO - O0
def o0O0O0 ( url , iconimage ) :
 if 6 - 6: iI . I11iii * I111i1i1111i . i1IIi
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Oo000ooOOO = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( Oo000ooOOO )
 for oOOo , OooO0OO in I1I11i :
  oOOo = oOOo . replace ( ':' , '' )
  url = 'https://www.eporner.com' + OooO0OO
  OOO0OOO00oo ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + oOOo + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 46 - 46: I11iii + iIii1I11I1II1 + IiI1I1 + O0Oooo00 . I1I1i1
def iIiIi11Ii ( url ) :
 Iii1ii1II11i . ok ( "HERE" , str ( url ) )
 url = 'https://ww3.soul-anime.us/anime-list.html'
 Iii1ii1II11i . ok ( "HERE" , str ( url ) )
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<ul id="genre">(.*?)</ul>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . compile ( '<a rel=.*?href="(.*?)">(.*?)</a>' ) . findall ( iiii11I )
 for OooO0OO , III1iII1I1ii in I1I11i :
  i1I1iI ( "[COLOR cyan]" + III1iII1I1ii + "[/COLOR]" , OooO0OO , 52 , I1IiI , Oo , '' )
 OoO000 ( )
 if 23 - 23: iIii1 - IiI1I1 + oOoO
def II11 ( url ) :
 if 30 - 30: i11iIiiIii % iIii1I11I1II1 . oOoO % iIii1I11I1II1
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="lt">(.*?)<div class="tags"' ) . findall ( OooO0OO )
 for oOO00oO00O0OO in iiii11I :
  III1iII1I1ii = re . compile ( 'alt="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  ooo0o00 = re . compile ( '<p>(.*?)</p>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  oOo00OO = re . compile ( '<span class=".*?">(.*?)</span>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  if 'Completed' in oOo00OO :
   oOo00OO = '[COLOR red]' + oOo00OO + '[/COLOR]'
  else :
   oOo00OO = '[COLOR lime]' + oOo00OO + '[/COLOR]'
  i1I1iI ( "[COLOR cyan]" + III1iII1I1ii + " :: " + oOo00OO + "[/COLOR]" , url , 53 , I1IiI , Oo , ooo0o00 )
 OoO000 ( )
 if 93 - 93: oOoO - iIii1I11I1II1
def III111i11IiI ( url ) :
 if 71 - 71: oOoO / oOoO * iIii1 * iIii1 / O0Oo0oO0o
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<div class="img_box">(.*?)</span>' ) . findall ( OooO0OO )
 for oOO00oO00O0OO in iiii11I :
  III1iII1I1ii = re . compile ( '<div class="ep">(.*?)</div>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  I1IiI = re . compile ( 'data-original="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  OOO0OOO00oo ( "[COLOR cyan]" + III1iII1I1ii + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
 OoO000 ( )
 if 35 - 35: IiI1I1 * Ii1Ii1iiii11 * II1iI % i1iIii1Ii1II . I111i1i1111i
def O00o00O ( url , iconimage ) :
 if 3 - 3: IiI1I1
 OooO0OO = Iii111II ( url )
 iiii11I = re . compile ( '<iframe name="stream".*?src="(.*?)"' ) . findall ( OooO0OO ) [ 0 ]
 O0O0OOOOoo = Iii111II ( iiii11I )
 try :
  Oo000ooOOO = re . compile ( '<iframe.*?src="(.*?)"' ) . findall ( O0O0OOOOoo ) [ 0 ]
  o00oO0oo0OO ( ii11i1 , Oo000ooOOO , iconimage )
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Source Link Is Down[/COLOR]' , iconimage , 5000 )
  if 20 - 20: O0Oo0oO0o . iI / O0Oo0oO0o % i11iIiiIii % iI
def I11Ii11iI1 ( url ) :
 if 39 - 39: II1iI * i11iIiiIii - iIii1 / I11iii % OO0O00 % oOoO
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . findall ( '<div class="item">(.*?)</li>' , OooO0OO )
 for IIII in iiii11I :
  III1iII1I1ii = re . findall ( 'alt="(.*?)"' , IIII ) [ 0 ]
  OOOo00oo0oO = re . findall ( '<a href="(.*?)"' , IIII ) [ 0 ]
  OO00oo0o = re . findall ( '<img src="(.*?)"' , IIII ) [ 0 ]
  ooo0o00 = re . findall ( """</div>(.*?)'""" , IIII ) [ 0 ]
  ooo0o00 = OoOO ( ooo0o00 )
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR] " , OOOo00oo0oO , 43 , OO00oo0o , Oo , ooo0o00 )
  if 18 - 18: O0Oooo00 + iIii1I11I1II1 - O0Oo0oO0o - II1iI
 try :
  OoO = re . findall ( '<a class="pagecurrent".+?>(.*?)</a>' , OooO0OO ) [ 0 ]
  OoO = int ( OoO )
  OoO = OoO + 1
  url = url . replace ( '.html' , '' )
  OoO = ( url + '/page-%s.html' % ( OoO ) )
  i1I1iI ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 42 , I1IiI , Oo , description = 'Next Page' )
 except : pass
 if 71 - 71: OoooooooOO
def iIIIII1iiiiII ( url , iconimage ) :
 if 54 - 54: i1IIi
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii1I11 = re . findall ( '<p\s+class="server_servername">(.*?)<.+?href="(.*?)"' , OooO0OO )
 for III1iII1I1ii , url in ii1I11 :
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 82 , iconimage , Oo , '' )
  if 99 - 99: IiI1I1
def II11i11II ( url , iconimage ) :
 if 29 - 29: i1iIii1Ii1II % O0Oooo00 % I11iii . Ii1Ii1iiii11 / OoooooooOO * o0o0O00O00o0
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Oo000ooOOO = re . findall ( '<script type="text/javascript">document.write\(Base64.decode\("(.*?)"' , OooO0OO ) [ 0 ]
 Oo000ooOOO = base64 . b64decode ( Oo000ooOOO )
 Oo000ooOOO = re . findall ( 'src="(.*?)"' , Oo000ooOOO ) [ 0 ]
 o00oO0oo0OO ( ii11i1 , Oo000ooOOO , iconimage )
 OoO000 ( )
 if 54 - 54: O0
def OOoO000O00oO ( ) :
 if 34 - 34: O0
 ii1i1I1i = 'https://www.livefootballol.me/acestream-channel-list-2018.html'
 OooO0OO = Iii111II ( ii1i1I1i )
 I1I11i = re . compile ( '<tr>(.+?)</tr>' ) . findall ( OooO0OO )
 for oOO00oO00O0OO in I1I11i :
  III1iII1I1ii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  if len ( III1iII1I1ii ) == 1 or '&nbsp;' in III1iII1I1ii :
   III1iII1I1ii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oOO00oO00O0OO ) [ 1 ]
  if len ( III1iII1I1ii ) > 40 :
   III1iII1I1ii = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  ii1i1I1i = re . compile ( '<td>(.+?)</td>' ) . findall ( oOO00oO00O0OO ) [ 2 ]
  OooOOOo0 = re . compile ( '<td>(.+?)</td>' ) . findall ( oOO00oO00O0OO ) [ 3 ]
  O0O0o0o0o = re . compile ( '<td>(.+?)</td>' ) . findall ( oOO00oO00O0OO ) [ 4 ]
  III1iII1I1ii = III1iII1I1ii . strip ( )
  ii1i1I1i = ii1i1I1i . strip ( )
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + ' :: [COLOR yellow]' + OooOOOo0 + '[COLOR aqua] :: [COLOR yellow]' + O0O0o0o0o + ' Kbps[/COLOR]' , ii1i1I1i , 2 , IIIii1II1II , Oo , '' )
  if 9 - 9: i1iIii1Ii1II + I111i1i1111i - iIii1I11I1II1 - iiIiIIi + Ii1Ii1iiii11
def o000O0OOoo ( ) :
 if 60 - 60: II1iI * OO0O00 % O0Oooo00 + iIii1
 ii1i1I1i = 'http://acestreamchannel.blogspot.co.uk/'
 OooO0OO = Iii111II ( ii1i1I1i )
 I1I11i = re . compile ( '<tr>(.+?)</tr>' ) . findall ( OooO0OO )
 for o0O in I1I11i :
  try :
   III1iII1I1ii = re . compile ( '<td>(.+?)</td>' ) . findall ( o0O ) [ 0 ]
   if len ( III1iII1I1ii ) < 40 :
    ii1i1I1i = re . compile ( 'href="(.+?)"' ) . findall ( o0O ) [ 0 ]
    OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 2 , IIIii1II1II , Oo , '' )
  except : pass
  if 52 - 52: i1IIi
def o000 ( ) :
 if 94 - 94: Ii1Ii1iiii11 + O0 / oOoO . II1iI + IiI1I1 . iIii1I11I1II1
 ii1i1I1i = 'https://acestreamid.com/'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<li class="collection-item acestreamidID ">(.*?)</li>' ) . findall ( OooO0OO )
 for oOO00oO00O0OO in iiii11I :
  III1iII1I1ii = re . compile ( 'title="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  if 'Broken' in III1iII1I1ii :
   III1iII1I1ii = re . compile ( '<span class="font-small grey-text truncate content">(.*?)</span>' ) . findall ( oOO00oO00O0OO ) [ 0 ] . strip ( )
  OooO0OO = re . compile ( '<div class="content wrap">(.*?)</div>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
  OooO0OO = 'acestream://' + OooO0OO
  oOo00OO = re . compile ( 'title="(.*?)"' ) . findall ( oOO00oO00O0OO ) [ 1 ]
  try :
   OOOoO = re . findall ( r'\d+' , oOo00OO ) [ 0 ]
  except IndexError :
   OOOoO = 0
  OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + " [COLOR yellow]Down Reports :: " + str ( OOOoO ) + "[/COLOR]" , OooO0OO , 2 , IIIii1II1II , Oo , '' )
  if 57 - 57: O0Oooo00 / i1IIi . i1IIi
def oo00OOoOoO00 ( ) :
 ii1i1I1i = 'http://jkarakizi.com/updated-acestream-channels-for-2018/'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . compile ( '<tr>(.*?)</tr>' ) . findall ( OooO0OO )
 for oOO00oO00O0OO in iiii11I :
  try :
   III1iII1I1ii = re . compile ( '<td class=".+?">(.*?)</td>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   OooO0OO = re . compile ( '<td class="tg-yw4l">(.*?)</td>' ) . findall ( oOO00oO00O0OO ) [ 1 ]
   OooO0OO = 'acestream://' + OooO0OO
   OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OooO0OO , 2 , IIIii1II1II , Oo , '' )
  except : pass
  if 15 - 15: I11iii / O0 . Ii1Ii1iiii11 . i11iIiiIii
def o0OO0O0Oo ( ) :
 if 78 - 78: I111i1i1111i / i1iIii1Ii1II - IiI1I1 - iI * iIii1
 ii1i1I1i = 'http://www.livefootballol.me/streaming/english-premier-league-2018/'
 OooO0OO = Iii111II ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<td>(.+?)</td>' ) . findall ( OooO0OO )
 for o0O in iiii11I :
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  i1 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = 'http://www.livefootballol.me' + ii1i1I1i
  i1I1iI ( "[COLOR aqua]" + i1 + "[/COLOR]" , ii1i1I1i , 74 , IIIii1II1II , Oo , '' )
  if 17 - 17: OoooooooOO + IiI1I1 * oOoO * I111i1i1111i
def iiIii1I ( url ) :
 if 47 - 47: o0o0O00O00o0 . oOoO / Ii1Ii1iiii11
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<a href="(.+?)"' ) . findall ( OooO0OO )
 OOoOO = 0
 for OOOOoOoo0O0O0 in iiii11I :
  if 'acestream' in OOOOoOoo0O0O0 :
   if 'http' in OOOOoOoo0O0O0 :
    OOoOO += 1
    III1iII1I1ii = '[COLOR aqua]Link :: ' + str ( OOoOO ) + '[/COLOR]'
    OOO0OOO00oo ( III1iII1I1ii , OOOOoOoo0O0O0 , 75 , IIIii1II1II , Oo , '' )
 if OOoOO == 0 :
  OOO0OOO00oo ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , IIIii1II1II , Oo , '' )
  if 66 - 66: i1iIii1Ii1II - Ii1Ii1iiii11 * I11iii + I111i1i1111i + Ii1Ii1iiii11 - iIii1I11I1II1
def iiiI1ii11 ( url ) :
 if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( OooO0OO ) [ 0 ]
 o00oO0oo0OO ( ii11i1 , url , IIIii1II1II )
 if 58 - 58: iIii1
 if 4 - 4: O0Oo0oO0o . o0o0O00O00o0 / I1I1i1 - i11iIiiIii
 if 72 - 72: O0 / o0o0O00O00o0 + OoooooooOO * iI
 if 61 - 61: OoooooooOO % O0Oo0oO0o - II1iI % I1I1i1 + i1IIi
def i1IIiIi1IiI ( url ) :
 if 14 - 14: I11iii % iIii1 % i1iIii1Ii1II - i11iIiiIii
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0OO000ooOo = 'https://yo-movies.com/'
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( 'class="ml-item">(.*?)</a>' , OooO0OO )
 for IIII in iiii11I :
  III1iII1I1ii = re . findall ( 'oldtitle="(.*?)"' , IIII ) [ 0 ]
  o00oOO0 = re . findall ( '<a href="(.*?)"' , IIII ) [ 0 ]
  if not o0OO000ooOo in o00oOO0 : o00oOO0 = o0OO000ooOo + o00oOO0
  I1IiI = re . findall ( '<img data-original="(.*?)"' , IIII ) [ 0 ] . strip ( ) . replace ( 'w185' , 'original' )
  oOOo = re . findall ( '<span class="mli-quality">(.*?)</span>' , IIII ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + ' | ' + '[COLOR yellow]' + oOOo + "[/COLOR]" , o00oOO0 , 81 , I1IiI , I1IiI , '' )
 try :
  oOo00OooO0oO = 6
  I1IIi = 'page'
  O0OOOo = url . split ( I1IIi , 1 ) [ - 1 ]
  i11I1I1iiI = O0OOOo . replace ( '/' , '' )
  O0OOOo = int ( i11I1I1iiI )
  if O0OOOo < oOo00OooO0oO :
   O0OOOo = O0OOOo + 1
   OoO = 'https://yo-movies.com/genre/bollywood/page/' + str ( O0OOOo ) + '/'
  i1I1iI ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 80 , IIIii1II1II , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 34 - 34: oOoO % o0o0O00O00o0 . O0 . iIii1I11I1II1
def ooi1II1I ( url , iconimage ) :
 if 95 - 95: O0Oooo00 - IiI1I1 / O0Oo0oO0o % I1I1i1 . Ii1Ii1iiii11
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . findall ( '<div class="btn-group btn-group-justified embed-selector"\s+>(.*?)</div>' , OooO0OO ) [ 0 ]
 iii1IIII1iii11I = r'''<a\s+href=['"]([^'"]+)['"].+?Download'''
 OOOOoOoo0O0O0 = re . findall ( iii1IIII1iii11I , iiii11I )
 ooO0oO00O0o = 0
 for o0O in OOOOoOoo0O0O0 :
  ooO0oO00O0o += 1
  i1II1 = 'Link' + ' | ' + str ( ooO0oO00O0o )
  OOO0OOO00oo ( "[COLOR aqua]" + i1II1 + "[/COLOR]" , o0O , 2 , iconimage , iconimage , '' )
  if 97 - 97: OoooooooOO - OO0O00
def oooo00 ( url ) :
 if 96 - 96: I1I1i1 % o0o0O00O00o0 % iiIiIIi - o0o0O00O00o0 % I111i1i1111i + I1I1i1
 OooO0OO = Iii111II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . findall ( 'class="item">(.*?)<div class="typepost">' , OooO0OO , flags = re . DOTALL )
 for IIII in iiii11I :
  III1iII1I1ii = re . findall ( '<span class="tt">(.*?)</span>' , IIII , flags = re . DOTALL ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  url = re . findall ( '<a href="(.*?)">' , IIII , flags = re . DOTALL ) [ 0 ]
  I1IiI = re . findall ( '<img src="(.*?)"' , IIII , flags = re . DOTALL ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 84 , I1IiI , Oo , '' )
  if 3 - 3: O0
 try :
  iii1IIII1iii11I = '''<a\s*href=['"]([^'"]+)['"]\s*>Next<'''
  OoO = re . findall ( iii1IIII1iii11I , OooO0OO ) [ 0 ]
  i1I1iI ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 83 , IIIii1II1II , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 64 - 64: i1IIi % o0o0O00O00o0 / i11iIiiIii - i1IIi % IiI1I1 . iI
def II1i111 ( url , iconimage ) :
 if 50 - 50: I11iii % i1IIi
 OooO0OO = Iii111II ( url )
 iii11II1I = re . findall ( '''<script>eid =\s+'(.*?)'.+?</script>''' , OooO0OO ) [ 0 ]
 iI111I11i = ( 'https://asap2bypass.streamcr.com/ajax/movie/get_sources/%s' % iii11II1I )
 O0O0OOOOoo = Iii111II ( iI111I11i )
 I1 = '''"file":['"]([^'"]+)['"]\s*.+?"label":"(\d+)p"'''
 o0O = re . findall ( I1 , O0O0OOOOoo )
 for url , oOOo in o0O :
  url = url . replace ( '\\' , '' )
  OOO0OOO00oo ( "[COLOR aqua]Link Quality : " + oOOo + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 48 - 48: i1iIii1Ii1II - OoooooooOO % IiI1I1 * I111i1i1111i
def oOoOIIII ( url , getphp ) :
 oOoOo00oOo = urllib2 . Request ( url )
 oOoOo00oOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 oOoOo00oOo . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 Ooo00O00O0O0O = urllib2 . urlopen ( oOoOo00oOo , timeout = 10 )
 OooO0OO = Ooo00O00O0O0O . read ( )
 Ooo00O00O0O0O . close ( )
 return OooO0OO
 if 50 - 50: i1iIii1Ii1II % I11iii
 if 28 - 28: I1I1i1 . i1IIi
 if 10 - 10: O0Oooo00 / i1iIii1Ii1II
def I1iII11iIII1i1I ( ) :
 if 63 - 63: i1iIii1Ii1II + OO0O00 - O0Oo0oO0o
 ii1i1I1i = 'http://www1.putlockers.gs/genres.html'
 OooO0OO = Iii111II ( ii1i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiii11I = re . compile ( '<ul class="dropdown">(.+?)</ul>' ) . findall ( OooO0OO ) [ 0 ]
 I1I11i = re . findall ( '<li>(.*?)</li>' , iiii11I )
 for o0O in I1I11i :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( o0O ) [ 0 ]
  ii1i1I1i = re . compile ( '<a href="(.+?)"' ) . findall ( o0O ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 42 , I1IiI , Oo )
  if 2 - 2: I11iii
def oOo0O0O0 ( url ) :
 if 89 - 89: iIii1 / OoooooooOO . iI
 OooO0OO = Iii111II ( url )
 I1I11i = re . findall ( '<div class="postHeader">(.*?)<div class="post">' , OooO0OO )
 for IIII in I1I11i :
  III1iII1I1ii = re . findall ( 'title="(.*?)"' , IIII ) [ 0 ] . replace ( 'Permalink to' , '' ) . strip ( )
  url = re . findall ( '<a href="(.*?)"' , IIII ) [ 0 ]
  I1IiI = re . findall ( 'src="(.*?)"' , IIII ) [ 1 ]
  I1ii11iIi11i = re . findall ( '<img class="aligncenter"\s+src="(.*?)"' , IIII ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 86 , I1IiI , I1ii11iIi11i , '' )
  if 34 - 34: iI - OoooooooOO . II1iI / O0Oo0oO0o
 try :
  iii1IIII1iii11I = '''<a\s*href=['"]([^'"]+)['"]\s*>Older'''
  OoO = re . findall ( iii1IIII1iii11I , OooO0OO ) [ 0 ]
  i1I1iI ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 85 , IIIii1II1II , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 27 - 27: O0Oooo00 / i1iIii1Ii1II * o0o0O00O00o0 - O0Oooo00
 if 19 - 19: oOoO
def Ooooo0OoO0 ( url , iconimage , fanart ) :
 if 9 - 9: IiI1I1 . I11iii
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( '<strong>Download:</strong>(.*?)</div>' , OooO0OO ) [ 0 ]
 iii1IIII1iii11I = '''<a\s+href=['"]([^'"]+)['"]>([^'"]+)</a>'''
 o0O = re . findall ( iii1IIII1iii11I , iiii11I )
 iIi1i = [ 'uploadgig' , 'rapidgator' ]
 OO0Oo = 0
 for url , III1iII1I1ii in o0O :
  if any ( x in url . lower ( ) for x in iIi1i ) :
   OO0Oo += 1
   if 'uploadgig' in url :
    III1iII1I1ii = III1iII1I1ii + '[COLOR yellow] (Not Great With RD)[/COLOR]'
   OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
 if OO0Oo == 0 :
  OOO0OOO00oo ( "[COLOR yellow]No Links Found[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 45 - 45: OoooooooOO % iIii1 - I1I1i1 - iIii1 - II1iI / Ii1Ii1iiii11
def oooo00i1 ( url ) :
 if 95 - 95: O0Oooo00 . i1IIi / i11iIiiIii
 OooO0OO = Iii111II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( """<div\s+id='genre'\s+class="options\s+">(.*?)</div>""" , OooO0OO ) [ 0 ]
 iIi1IIiI = re . findall ( '<a href="(.*?)">(.*?)</a>' , iiii11I )
 for url , III1iII1I1ii in iIi1IIiI :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 90 , I1IiI , I1ii11iIi11i , '' )
  if 24 - 24: iI * O0Oo0oO0o % iI % I11iii + OoooooooOO
  if 29 - 29: O0Oo0oO0o - OoooooooOO - i11iIiiIii . Ii1Ii1iiii11
  if 19 - 19: O0Oo0oO0o
def OoOOII1i11i1iIi11 ( url ) :
 if 83 - 83: iiIiIIi
 OooO0OO = Iii111II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 iiii11I = re . findall ( '<div class="imagefilm">(.*?)</a>' , OooO0OO )
 I1iI1I1 = 0
 for IIII in iiii11I :
  I1iI1I1 += 1
  III1iII1I1ii = re . findall ( 'title="(.*?)"' , IIII ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  url = re . findall ( '<a href="(.*?)"' , IIII ) [ 0 ]
  I1IiI = re . findall ( '<img src="(.*?)"' , IIII ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 91 , I1IiI , I1ii11iIi11i , '' )
  if 48 - 48: II1iI / i11iIiiIii - Ii1Ii1iiii11 * iIii1 / OoooooooOO
 if I1iI1I1 == 0 :
  OOO0OOO00oo ( "[COLOR yellow]No Content Found For This Catergory[/COLOR]" , url , 999 , IIIii1II1II , Oo , '' )
  if 89 - 89: iIii1I11I1II1 / II1iI - O0Oo0oO0o / iiIiIIi . i11iIiiIii . iiIiIIi
 try :
  iii1IIII1iii11I = '''<a href=['"]([^'"]+)['"]>Next'''
  OoO = re . findall ( iii1IIII1iii11I , OooO0OO ) [ 0 ]
  if not o0OO000ooOo in OoO : OoO = o0OO000ooOo + OoO
  i1I1iI ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 90 , IIIii1II1II , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 48 - 48: O0 + O0 . OO0O00 - o0o0O00O00o0
def o00oo0000 ( url ) :
 if 44 - 44: i1iIii1Ii1II % iIii1I11I1II1
 OooO0OO = Iii111II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( """<div\s+id='genre'\s+class="options\s+">(.*?)</div>""" , OooO0OO ) [ 0 ]
 iIi1IIiI = re . findall ( '<a href="(.*?)">(.*?)</a>' , iiii11I )
 for url , III1iII1I1ii in iIi1IIiI :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 94 , I1IiI , I1ii11iIi11i , '' )
  if 90 - 90: O0Oo0oO0o + OoooooooOO % OoooooooOO
  if 35 - 35: iI / I1I1i1 * OoooooooOO . O0Oo0oO0o / i1iIii1Ii1II
  if 1 - 1: OoooooooOO + I11iii . i1IIi % oOoO
def OOOOOo ( url ) :
 if 65 - 65: Ii1Ii1iiii11
 OooO0OO = Iii111II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 iiii11I = re . findall ( '<div class="imagefilm">(.*?)</a>' , OooO0OO )
 I1iI1I1 = 0
 for IIII in iiii11I :
  I1iI1I1 += 1
  III1iII1I1ii = re . findall ( 'title="(.*?)"' , IIII ) [ 0 ]
  III1iII1I1ii = O0oO0 ( III1iII1I1ii )
  url = re . findall ( '<a href="(.*?)"' , IIII ) [ 0 ]
  I1IiI = re . findall ( '<img src="(.*?)"' , IIII ) [ 0 ]
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 95 , I1IiI , I1ii11iIi11i , '' )
  if 7 - 7: I11iii . I111i1i1111i / I1I1i1 . IiI1I1 * oOoO - O0Oo0oO0o
 if I1iI1I1 == 0 :
  OOO0OOO00oo ( "[COLOR yellow]No Content Found For This Catergory[/COLOR]" , url , 999 , IIIii1II1II , Oo , '' )
  if 37 - 37: OO0O00 . I111i1i1111i / O0 * iI
 try :
  iii1IIII1iii11I = '''<a href=['"]([^'"]+)['"]>Next'''
  OoO = re . findall ( iii1IIII1iii11I , OooO0OO ) [ 0 ]
  if not o0OO000ooOo in OoO : OoO = o0OO000ooOo + OoO
  i1I1iI ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 90 , IIIii1II1II , I1ii11iIi11i , 'Next Page' )
 except : pass
 if 7 - 7: O0Oooo00 * oOoO + O0Oo0oO0o % i11iIiiIii
def i1i1IiIiIi1Ii ( url ) :
 if 64 - 64: IiI1I1 + OoooooooOO * OoooooooOO
 OooO0OO = Iii111II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 iiii11I = re . findall ( '<div class="list-episodes"(.*?)</div>' , OooO0OO ) [ 0 ]
 i1IiiI1I1IIi11i1 = re . findall ( '<a href="(.*?)">(.*?)</a>' , iiii11I )
 for url , III1iII1I1ii in i1IiiI1I1IIi11i1 :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  i1I1iI ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 91 , I1IiI , I1ii11iIi11i , '' )
  if 45 - 45: o0o0O00O00o0 % Ii1Ii1iiii11 - o0o0O00O00o0
def i1i1 ( url , iconimage ) :
 if 69 - 69: I1I1i1 - OO0O00
 OooO0OO = Iii111II ( url )
 iii1IIII1iii11I = '''<option\s+value=['"]([^'"]+)['"]'''
 iiIIi1 = re . findall ( iii1IIII1iii11I , OooO0OO )
 i111i11I1Ii1I = re . findall ( 'var\s+filmId\s+=\s+"(.*?)"' , OooO0OO ) [ 0 ]
 for iIi1i in iiIIi1 :
  iIi1i = iIi1i . title ( )
  OOO0OOO00oo ( "[COLOR aqua]" + iIi1i + "[/COLOR]" , i111i11I1Ii1I , 92 , iconimage , Oo , '' )
  if 8 - 8: iiIiIIi
def I11iII ( name , url ) :
 if 2 - 2: II1iI + Ii1Ii1iiii11 . Ii1Ii1iiii11 . O0 / oOoO
 name = name . replace ( '[COLOR aqua]' , '' ) . replace ( '[/COLOR]' , '' )
 name = name . lower ( )
 iIiiIiiIi = ( 'http://watchanime.info/ajax-get-link-stream/?server=%s&filmId=%s' % ( name , url ) )
 OooO0OO = Iii111II ( iIiiIiiIi )
 if 'streaming.php' in OooO0OO :
  OooO0OO = 'http:' + OooO0OO
 name = '[COLOR yellow]Nemesis Anime[/COLOR]'
 o00oO0oo0OO ( name , OooO0OO , IIIii1II1II )
 if 40 - 40: Ii1Ii1iiii11
 if 78 - 78: iIii1I11I1II1
def ooO0oo0o0 ( url ) :
 if 9 - 9: II1iI + I1I1i1 / II1iI . iIii1 * o0o0O00O00o0
 OooO0OO = Iii111II ( url )
 oo0OooOOo0 = json . loads ( OooO0OO )
 try :
  OoO = oo0OooOOo0 [ 'nextPageToken' ]
 except : pass
 I1I11i = oo0OooOOo0 [ 'items' ]
 for IIII in I1I11i :
  try :
   III1iII1I1ii = IIII [ 'snippet' ] [ 'title' ]
   III1iII1I1ii = i1i1ii1111i1i ( III1iII1I1ii )
   iIiI = IIII [ 'snippet' ] [ 'description' ]
   I1IiI = IIII [ 'snippet' ] [ 'thumbnails' ] [ 'default' ] [ 'url' ]
   I1IiI = I1IiI . replace ( 'default' , 'hqdefault' )
   OOOo00oo0oO = IIII [ 'id' ] [ 'videoId' ]
   o00oOO0 = 'https://www.youtube.com/watch?v=' + OOOo00oo0oO
   OOO0OOO00oo ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , o00oOO0 , 2 , I1IiI , I1IiI , iIiI )
  except : pass
  if 26 - 26: iIii1I11I1II1 % i11iIiiIii % I1I1i1
 try :
  if '&pageToken=' in url :
   oo0O = url . split ( "&pageToken=" , 1 ) [ 0 ]
   III1i1IiI1i = oo0O + '&pageToken=' + OoO
   xbmc . log ( oo0O )
   o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
   i1I1iI ( "[COLOR yellow]Next Page --------->[/COLOR]" , III1i1IiI1i , 87 , o0 , I1ii11iIi11i )
  else :
   oo0O = url + '&pageToken=' + OoO
   o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
   i1I1iI ( "[COLOR yellow]Next Page --------->[/COLOR]" , oo0O , 87 , o0 , I1ii11iIi11i )
 except : pass
 if 32 - 32: OoooooooOO - I111i1i1111i - i11iIiiIii * Ii1Ii1iiii11 / i1iIii1Ii1II + OoooooooOO
def ii1I1I111 ( ) :
 if 3 - 3: OoooooooOO / IiI1I1 * i1iIii1Ii1II . o0o0O00O00o0
 ii1i1I1i = 'https://www.livefootballol.me/streaming/world-cup-2018/'
 o0OO000ooOo = 'https://www.livefootballol.me'
 OooO0OO = Iii111II ( ii1i1I1i )
 iiii11I = re . findall ( '<tbody>(.*?)</tbody>' , OooO0OO ) [ 0 ]
 Ooo0oooO00o0 = re . findall ( '<a href="(.*?)">(.*?)</a>' , iiii11I )
 for ii1i1I1i , III1iII1I1ii in Ooo0oooO00o0 :
  III1iII1I1ii = III1iII1I1ii . replace ( '-' , 'Vs' )
  if not o0OO000ooOo in ii1i1I1i : ii1i1I1i = o0OO000ooOo + ii1i1I1i
  I1IiI = 'http://a2.espncdn.com/combiner/i?img=%2Fi%2Fleaguelogos%2Fsoccer%2F500%2F4.png'
  I1ii11iIi11i = 'https://i.pinimg.com/originals/15/9d/1a/159d1aae7e7f272fad2aa430a5839631.jpg'
  i1I1iI ( "[COLOR gold]" + III1iII1I1ii + "[/COLOR]" , ii1i1I1i , 101 , I1IiI , I1ii11iIi11i , '' )
  if 53 - 53: o0o0O00O00o0
def o0oO0oo0000OO ( url ) :
 if 45 - 45: OO0O00 * iiIiIIi / OoooooooOO . iIii1 % I1I1i1 / i1IIi
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( '<tbody>(.*?)</tbody>' , OooO0OO ) [ 1 ]
 iii1IIII1iii11I = '''<a\s+href=['"]([^'"]+)['"]>(.*?)<'''
 I1III1 = re . findall ( iii1IIII1iii11I , iiii11I )
 for OooO0OO , Iiii1ii in I1III1 :
  i1I1iI ( "[COLOR gold]" + Iiii1ii + "[/COLOR]" , OooO0OO , 102 , I1IiI , I1ii11iIi11i , '' )
  if 42 - 42: iiIiIIi * OO0O00 . I11iii * II1iI + I111i1i1111i
def i1i1II11II1 ( url ) :
 if 5 - 5: i1iIii1Ii1II - I1I1i1 % iIii1 - O0Oo0oO0o . II1iI + iI
 OooO0OO = Iii111II ( url )
 iiii11I = re . findall ( '<table class="uk-table"(.+?)</table>' , OooO0OO ) [ 0 ]
 iii1IIII1iii11I = '''<td>Bitrate<.+?<td>(.*?)<.+?</tr>.+?</tr>.+?<.+?</td><td>(.+?)<.+?href=['"]([^'"]+)['"]'''
 I1III1 = re . findall ( iii1IIII1iii11I , iiii11I )
 for oOOo , OooOOOo0 , OooO0OO in I1III1 :
  OOO0OOO00oo ( "[COLOR gold]" + oOOo + ' | ' + OooOOOo0 + "[/COLOR]" , OooO0OO , 2 , I1IiI , I1ii11iIi11i , '' )
  if 47 - 47: O0 - iIii1I11I1II1 - iI
  if 46 - 46: iiIiIIi . IiI1I1 * O0Oooo00 . OoooooooOO + I1I1i1
  if 72 - 72: O0Oo0oO0o + IiI1I1
  if 91 - 91: iIii1I11I1II1 % O0Oooo00 . Ii1Ii1iiii11 + iiIiIIi + Ii1Ii1iiii11
  if 95 - 95: iiIiIIi + I1I1i1 * IiI1I1
def i1i1ii1111i1i ( input ) :
 if type ( input ) != unicode :
  input = input . decode ( 'utf-8' )
  return input
 else :
  return input
  if 16 - 16: oOoO / II1iI + O0Oooo00 % iIii1I11I1II1 - i1IIi . iIii1
def O0oO0 ( text ) :
 if 26 - 26: Ii1Ii1iiii11 * I11iii . i1IIi
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
 if 59 - 59: O0 + i1IIi - Ii1Ii1iiii11
 return text
 if 62 - 62: i11iIiiIii % IiI1I1 . I11iii . IiI1I1
def ooOo0O0O0oOO0 ( ) :
 if 10 - 10: i1iIii1Ii1II + O0
 Ii1iI = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 Oo0O0O000 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 II1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 OOoO00ooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 12 - 12: o0o0O00O00o0 % II1iI + iIii1 - i1IIi . iiIiIIi / II1iI
 o0IiiiI111I = 0
 for ( O0OoOoo00o , III1I11i1iIi , OO0oo0O0OOO0 ) in os . walk ( Oo0O0O000 ) :
  for file in OO0oo0O0OOO0 :
   OoOOo = os . path . join ( O0OoOoo00o , file )
   o0IiiiI111I += os . path . getsize ( OoOOo )
 iIi1i111II = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( o0IiiiI111I / ( 1024 * 1024.0 ) )
 OOO0OOO00oo ( iIi1i111II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 46 - 46: II1iI / iiIiIIi . OO0O00 % i11iIiiIii + Ii1Ii1iiii11 + OoooooooOO
 o0IiiiI111I = 0
 for ( O0OoOoo00o , III1I11i1iIi , OO0oo0O0OOO0 ) in os . walk ( Ii1iI ) :
  for file in OO0oo0O0OOO0 :
   OoOOo = os . path . join ( O0OoOoo00o , file )
   o0IiiiI111I += os . path . getsize ( OoOOo )
 iIi1i111II = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( o0IiiiI111I / ( 1024 * 1024.0 ) )
 OOO0OOO00oo ( iIi1i111II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 93 - 93: iiIiIIi - I11iii . OO0O00 % iIii1I11I1II1 % oOoO
 o0IiiiI111I = 0
 for ( O0OoOoo00o , III1I11i1iIi , OO0oo0O0OOO0 ) in os . walk ( II1Ii ) :
  for file in OO0oo0O0OOO0 :
   OoOOo = os . path . join ( O0OoOoo00o , file )
   o0IiiiI111I += os . path . getsize ( OoOOo )
 iIi1i111II = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( o0IiiiI111I / ( 1024 * 1024.0 ) )
 OOO0OOO00oo ( iIi1i111II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 46 - 46: i11iIiiIii - IiI1I1 * O0 - i11iIiiIii + Ii1Ii1iiii11
 o0IiiiI111I = 0
 for ( O0OoOoo00o , III1I11i1iIi , OO0oo0O0OOO0 ) in os . walk ( OOoO00ooO ) :
  for file in OO0oo0O0OOO0 :
   OoOOo = os . path . join ( O0OoOoo00o , file )
   o0IiiiI111I += os . path . getsize ( OoOOo )
 iIi1i111II = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( o0IiiiI111I / ( 1024 * 1024.0 ) )
 OOO0OOO00oo ( iIi1i111II , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 66 - 66: II1iI - I11iii
 OOO0OOO00oo ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 OOO0OOO00oo ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 33 - 33: II1iI / O0Oooo00
def o00oO0oo0OO ( name , url , iconimage ) :
 if 12 - 12: O0Oo0oO0o
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import resolveurl
 if 'acestream' in url :
  OOOo00oo0oO = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  oOooO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  oOooO0 . setPath ( url )
  xbmc . Player ( ) . play ( OOOo00oo0oO , oOooO0 , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
  oOooO0 = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  oOooO0 . setPath ( Iiii1iI1i )
  xbmc . Player ( ) . play ( Iiii1iI1i , oOooO0 , False )
  time . sleep ( 2 )
  quit ( )
 else :
  Iiii1iI1i = url
  oOooO0 = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  oOooO0 . setPath ( Iiii1iI1i )
  xbmc . Player ( ) . play ( Iiii1iI1i , oOooO0 , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 2 - 2: i1IIi - II1iI + oOoO . O0Oo0oO0o
def iIIiI1iiI ( name , url , iconimage ) :
 if 18 - 18: iI - iIii1 % iI / oOoO
 OOooO , O0Oo00OO00Ooo = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 OOooO += urllib . unquote_plus ( O0Oo00OO00Ooo )
 url = regex . resolve ( OOooO )
 if 87 - 87: i1iIii1Ii1II * IiI1I1 % I11iii % I111i1i1111i
 PLAYREGEX ( name , url , iconimage )
 if 4 - 4: I111i1i1111i + iiIiIIi / iIii1
def IIiIiI ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 13 - 13: iI
def II111iiii ( heading , text ) :
 if 80 - 80: iiIiIIi - Ii1Ii1iiii11
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 iI1II1I1I = xbmcgui . Window ( id )
 OOo0 = 50
 while ( OOo0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   OOo0 -= 1
   iI1II1I1I . getControl ( 1 ) . setLabel ( heading )
   iI1II1I1I . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 58 - 58: I111i1i1111i - iI - OoooooooOO
  if 96 - 96: iIii1I11I1II1
def Iii111II ( url ) :
 try :
  oOoOo00oOo = urllib2 . Request ( url )
  oOoOo00oOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  Ooo00O00O0O0O = urllib2 . urlopen ( oOoOo00oOo , timeout = 5 )
  OooO0OO = Ooo00O00O0O0O . read ( )
  Ooo00O00O0O0O . close ( )
  OooO0OO = OooO0OO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OooO0OO
 except : quit ( )
 if 82 - 82: I111i1i1111i + O0 - I11iii % iIii1 * i11iIiiIii
def O00o0OO0 ( url ) :
 try :
  oOoOo00oOo = urllib2 . Request ( url )
  oOoOo00oOo . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  Ooo00O00O0O0O = urllib2 . urlopen ( oOoOo00oOo , timeout = 5 )
  OooO0OO = Ooo00O00O0O0O . read ( )
  Ooo00O00O0O0O . close ( )
  OooO0OO = OooO0OO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OooO0OO
 except : quit ( )
 if 15 - 15: Ii1Ii1iiii11
def OOO0OOO00oo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 I1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0Ooo0OooOOo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOooO0 . setProperty ( "fanart_Image" , fanart )
 oOooO0 . setProperty ( "icon_Image" , iconimage )
 oOooO0 . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOooO0 . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 71 - 71: I11iii + i1IIi * i1iIii1Ii1II % i1iIii1Ii1II / i1iIii1Ii1II
 oO0Ooo0OooOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iI , listitem = oOooO0 , isFolder = False )
 return oO0Ooo0OooOOo
 if 55 - 55: OoooooooOO + OO0O00 + OoooooooOO * o0o0O00O00o0
def Oo0oOOo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 I1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0Ooo0OooOOo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOooO0 . setProperty ( "fanart_Image" , fanart )
 oOooO0 . setProperty ( "icon_Image" , iconimage )
 oOooO0 . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 68 - 68: O0
 oOooO0 . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 2 - 2: O0Oooo00 + O0 * O0Oooo00 - iiIiIIi + iIii1
 oO0Ooo0OooOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iI , listitem = oOooO0 , isFolder = False )
 return oO0Ooo0OooOOo
 if 43 - 43: I1I1i1 - I111i1i1111i
def iI1iIIII1 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OO0 = [ ]
 I11Ii1iI11iI1 = [ ]
 i1III1 = [ ]
 OooO0OO = Iii111II ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OooO0OO ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 o0O = re . compile ( '<link>(.+?)</link>' ) . findall ( OOOOoOoo0O0O0 )
 if len ( o0O ) < 1 :
  o0O = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OOOOoOoo0O0O0 )
 IIII = 1
 for Iii111IiIii in o0O :
  OooO0ooo0 = Iii111IiIii
  if '(' in Iii111IiIii :
   Iii111IiIii = Iii111IiIii . split ( '(' ) [ 0 ]
   iIiIoO00Ooo0oO = str ( OooO0ooo0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OO0 . append ( Iii111IiIii )
   I11Ii1iI11iI1 . append ( iIiIoO00Ooo0oO )
  else :
   OO0 . append ( Iii111IiIii )
   I11Ii1iI11iI1 . append ( '[COLOR aqua]Link ' + str ( IIII ) + '[/COLOR]' )
  IIII = IIII + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OOOo = Iii1ii1II11i . select ( name , I11Ii1iI11iI1 )
 if OOOo < 0 :
  quit ( )
 else :
  url = OO0 [ OOOo ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : Iiii1iI1i = liveresolver . resolve ( url )
  else : Iiii1iI1i = url
  oOooO0 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  oOooO0 . setPath ( Iiii1iI1i )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOooO0 )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( Iiii1iI1i )
  if 74 - 74: iiIiIIi - OoooooooOO . i1iIii1Ii1II
def III1Ii1i1I1 ( name , url , iconimage ) :
 if 97 - 97: OO0O00 . o0o0O00O00o0 - OO0O00 + II1iI * O0Oo0oO0o
 I111Ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 OO0 = [ ]
 I11Ii1iI11iI1 = [ ]
 i1III1 = [ ]
 II11iIi = [ ]
 OooO0OO = Iii111II ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OooO0OO ) [ 0 ]
 o0O = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OOOOoOoo0O0O0 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 IIII = 1
 if 29 - 29: O0 . OO0O00
 for Iii111IiIii in o0O :
  OooO0ooo0 = Iii111IiIii
  if '(' in Iii111IiIii :
   Iii111IiIii = Iii111IiIii . split ( '(' ) [ 0 ]
   iIiIoO00Ooo0oO = str ( OooO0ooo0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OO0 . append ( Iii111IiIii )
   I11Ii1iI11iI1 . append ( iIiIoO00Ooo0oO )
   II11iIi . append ( 'Stream ' + str ( IIII ) )
  else :
   OO0 . append ( Iii111IiIii )
   I11Ii1iI11iI1 . append ( 'Link ' + str ( IIII ) )
   if 66 - 66: iIii1 * iIii1I11I1II1 % iIii1I11I1II1 * I11iii - o0o0O00O00o0 - I11iii
  IIII = IIII + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OOOo = Iii1ii1II11i . select ( name , I11Ii1iI11iI1 )
 if OOOo < 0 :
  quit ( )
 else :
  OOO00O = I11Ii1iI11iI1 [ OOOo ]
  OOoOO0oo0ooO = "/"
  if not OOO00O . endswith ( OOoOO0oo0ooO ) :
   O0o0O00Oo0o0 = OOO00O + "/"
  else :
   O0o0O00Oo0o0 = OOO00O
  url = I111Ii + OO0 [ OOOo ] + "%26referer=" + O0o0O00Oo0o0
  print url
  if 70 - 70: OO0O00 + iIii1
  xbmc . Player ( ) . play ( url )
  if 93 - 93: OO0O00 + iiIiIIi
def OoOO ( string ) :
 i1i1i1IiIi1 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 22 - 22: oOoO * O0 . O0Oo0oO0o - O0Oooo00
 return '' . join ( i1i1i1IiIi1 )
 if 90 - 90: iIii1
def i1I1iI ( name , url , mode , iconimage , fanart , description = '' ) :
 if 94 - 94: oOoO / I1I1i1 * OO0O00 - I111i1i1111i
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 I1iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0Ooo0OooOOo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 oOooO0 . setProperty ( "fanart_Image" , fanart )
 oOooO0 . setProperty ( "icon_Image" , iconimage )
 oOooO0 . setInfo ( 'video' , { 'Plot' : description } )
 oO0Ooo0OooOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1iI , listitem = oOooO0 , isFolder = True )
 return oO0Ooo0OooOOo
 if 44 - 44: iiIiIIi % i11iIiiIii - iI * I1I1i1 + i1iIii1Ii1II * IiI1I1
def IiI1iI1IiiIi1 ( name , url , iconimage ) :
 oO0Ooo0OooOOo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; oOooO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO0Ooo0OooOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oOooO0 )
 xbmc . Player ( ) . play ( url , oOooO0 , False )
 if 90 - 90: O0 + oOoO - OoooooooOO . oOoO
def oOII1ii1ii11I1 ( ) :
 if 88 - 88: I1I1i1
 Ii1iI = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 Oo0O0O000 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 II1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 93 - 93: iIii1I11I1II1
 IIII = [ ( Ii1iI , 'Cache' ) , ( Oo0O0O000 , 'Thumbnails' ) , ( II1Ii , 'Packages' ) ]
 if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
 iIiI1iI1i1I = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if iIiI1iI1i1I :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for OOooO in IIII :
   if 82 - 82: II1iI % I1I1i1 * iI . iiIiIIi % II1iI - iIii1I11I1II1
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % OOooO [ 1 ] )
   time . sleep ( 1 )
   if 15 - 15: I1I1i1 % OO0O00 + i11iIiiIii
   for I1iIiiiI1 , III1I11i1iIi , OO0oo0O0OOO0 in os . walk ( OOooO [ 0 ] ) :
    for I1iIII1IiiI in OO0oo0O0OOO0 :
     if ( I1iIII1IiiI . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( I1iIiiiI1 , I1iIII1IiiI ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % OOooO [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 96 - 96: II1iI % i1IIi . Ii1Ii1iiii11 . O0
def Ii1Iii11 ( url , mode , name , iconimage , fanart ) :
 if 97 - 97: IiI1I1 / iIii1 . O0Oo0oO0o
 with open ( I11i , "a" ) as IIiI1Ii :
  IIiI1Ii . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 44 - 44: iiIiIIi % oOoO . OO0O00
def Ii11Iii ( ) :
 if 68 - 68: II1iI % O0
 with open ( I11i , "a" ) as IIiI1Ii :
  OoOO0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  oo0O0o = open ( OoOO0o ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiii11I = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0O0o )
  OOO0OOO00oo ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  OOO0OOO00oo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  if len ( iiii11I ) < 1 :
   OOO0OOO00oo ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  for oOO00oO00O0OO in iiii11I :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   ii1i1I1i = re . compile ( '<url>(.+?)</url>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   OOO0OOO00oo ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , ii1i1I1i , 2 , I1IiI , I1ii11iIi11i )
   if 13 - 13: iIii1I11I1II1 . I111i1i1111i * II1iI / iIii1 * iiIiIIi
 OOO0OOO00oo ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , IIIii1II1II , Oo )
 if 64 - 64: o0o0O00O00o0 / O0 * I111i1i1111i * o0o0O00O00o0
def O00oo ( ) :
 if 58 - 58: iIii1I11I1II1 - i11iIiiIii - i11iIiiIii * iiIiIIi + Ii1Ii1iiii11 . I111i1i1111i
 with open ( IiII , "a" ) as IIiI1Ii :
  OoOO0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  oo0O0o = open ( OoOO0o ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiii11I = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0O0o )
  OOO0OOO00oo ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  OOO0OOO00oo ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  if len ( iiii11I ) < 1 :
   OOO0OOO00oo ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , IIIii1II1II , Oo )
  for oOO00oO00O0OO in iiii11I :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   ii1i1I1i = re . compile ( '<link>(.+?)</link>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oO00O0OO ) [ 0 ]
   OOO0OOO00oo ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , ii1i1I1i , 2 , I1IiI , I1ii11iIi11i )
   if 80 - 80: i1IIi + i11iIiiIii - OO0O00 % O0Oo0oO0o . iIii1
 OOO0OOO00oo ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , IIIii1II1II , Oo )
 if 10 - 10: oOoO / oOoO * i11iIiiIii
def II1III1i1iiI ( ) :
 if 27 - 27: iiIiIIi - O0 % oOoO * OO0O00 . I11iii % iIii1I11I1II1
 with open ( I11i , "w" ) as IIiI1Ii :
  IIiI1Ii . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 37 - 37: OoooooooOO + O0 - i1IIi % o0o0O00O00o0
def i1I1i1i ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as IIiI1Ii :
  IIiI1Ii . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 36 - 36: O0Oo0oO0o % O0
def ii11IiI1 ( ) :
 if Oo0Oo0o0oo0O0 == 'android' :
  O0OoO = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://pinsystem.co.uk' ) )
 else :
  O0OoO = webbrowser . open ( 'https://pinsystem.co.uk' )
  if 45 - 45: O0 / i1IIi * iIii1 * O0Oooo00
def Oo0Oo0o0oo0O0 ( ) :
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
  if 35 - 35: I1I1i1 / iI % II1iI + iIii1I11I1II1
  if 79 - 79: I111i1i1111i / o0o0O00O00o0
def oO ( ) :
 if 77 - 77: i1iIii1Ii1II
 Oo0Oo0o0oo0O0 ( )
 i1i111Iiiiiii = iIiiiI1IiI1I1 . getSetting ( 'PIN' )
 if i1i111Iiiiiii == 'EXPIRED' :
  OOO00O = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin, would you like to open browser now or enter pin?[/COLOR]' , '' , yeslabel = '[COLOR yellow]Open Browser[/COLOR]' , nolabel = '[COLOR yellow]Enter Pin[/COLOR]' )
  if OOO00O :
   ii11IiI1 ( )
  OooOOOO = ''
  iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
  iIIIiiI1i1i . doModal ( )
  if iIIIiiI1i1i . isConfirmed ( ) :
   OooOOOO = iIIIiiI1i1i . getText ( )
   if len ( OooOOOO ) > 1 :
    iIII = OooOOOO . title ( )
    iIiiiI1IiI1I1 . setSetting ( id = 'PIN' , value = iIII )
    oO ( )
   else : quit ( )
  else :
   quit ( )
 if not 'EXPIRED' in i1i111Iiiiiii :
  Ii = iIiiiI1IiI1I1 . getSetting ( 'PIN' )
  iii1IIiI = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % Ii )
  OooO0OO = Iii111II ( iii1IIiI )
  if len ( OooO0OO ) < 1 or 'Pin Expired' in OooO0OO :
   iIiiiI1IiI1I1 . setSetting ( id = 'PIN' , value = 'EXPIRED' )
   oO ( )
  else :
   global baseurl
   baseurl = OooO0OO
   if 33 - 33: oOoO
def oOo00OoO0O ( url , iconimage , fanart ) :
 if 69 - 69: iIii1I11I1II1 * II1iI - iI + O0 + O0
 try :
  OooOOOO = ''
  iIIIiiI1i1i = xbmc . Keyboard ( OooOOOO , 'Enter Name To Save File As' )
  iIIIiiI1i1i . doModal ( )
  if iIIIiiI1i1i . isConfirmed ( ) :
   OooOOOO = iIIIiiI1i1i . getText ( )
   if len ( OooOOOO ) > 1 :
    iIII = OooOOOO . title ( )
   else : quit ( )
  import resolveurl
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   Iiii1iI1i = resolveurl . HostedMediaFile ( url ) . resolve ( )
   url = Iiii1iI1i
  O0oo = url . split ( '/' ) [ - 1 ]
  I1iI = urllib2 . urlopen ( url )
  ooOooO00Oo = os . path . join ( o0OOO , iIII )
  I1iIII1IiiI = open ( ooOooO00Oo , 'wb' )
  if 86 - 86: O0Oo0oO0o + o0o0O00O00o0 + I11iii
  I11i11I = I1iI . info ( )
  oooO00o00 = int ( I11i11I . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( iIII , oooO00o00 ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 9 - 9: O0Oooo00 * oOoO - iiIiIIi
  iIi11i = 0
  ooIII1II1iii1i = 8192
  while True :
   buffer = I1iI . read ( ooIII1II1iii1i )
   if not buffer :
    break
    if 75 - 75: I11iii - I111i1i1111i - iIii1I11I1II1 % Ii1Ii1iiii11
   iIi11i += len ( buffer )
   I1iIII1IiiI . write ( buffer )
   oOo00OO = "[%3.2f%%]" % ( iIi11i * 100. / oooO00o00 )
   oOo00OO = oOo00OO + chr ( 8 ) * ( len ( oOo00OO ) + 1 )
   iIiiiI . update ( iIi11i , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( oOo00OO , iIII ) )
   if 58 - 58: O0 . I11iii / OoooooooOO . O0Oooo00 / i1iIii1Ii1II * O0Oo0oO0o
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as IIiI1Ii :
   IIiI1Ii . write ( '<item>\n<title>' + iIII + '</title>\n<link>' + ooOooO00Oo + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 53 - 53: iiIiIIi - O0 / Ii1Ii1iiii11 % iI * II1iI % IiI1I1
  I1iIII1IiiI . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 69 - 69: I1I1i1
  if 83 - 83: Ii1Ii1iiii11
  if 38 - 38: OO0O00 + OoooooooOO . i1IIi
  if 19 - 19: iI - Ii1Ii1iiii11 - iiIiIIi - I111i1i1111i . iI . OO0O00
def i11I1I ( ) :
 oo0ooooo00o = [ ]
 OoOo = sys . argv [ 2 ]
 if len ( OoOo ) >= 2 :
  i111i1iIi1 = sys . argv [ 2 ]
  OoO0oO = i111i1iIi1 . replace ( '?' , '' )
  if ( i111i1iIi1 [ len ( i111i1iIi1 ) - 1 ] == '/' ) :
   i111i1iIi1 = i111i1iIi1 [ 0 : len ( i111i1iIi1 ) - 2 ]
  IiiI1iiI1III1i = OoO0oO . split ( '&' )
  oo0ooooo00o = { }
  for IIII in range ( len ( IiiI1iiI1III1i ) ) :
   iii1 = { }
   iii1 = IiiI1iiI1III1i [ IIII ] . split ( '=' )
   if ( len ( iii1 ) ) == 2 :
    oo0ooooo00o [ iii1 [ 0 ] ] = iii1 [ 1 ]
 return oo0ooooo00o
 if 13 - 13: iIii1I11I1II1
i111i1iIi1 = i11I1I ( ) ; ii1i1I1i = None ; ii11i1 = None ; OooooOo0 = None ; I1ii1 = None ; IIIii1II1II = None ; iIiI = None
try : I1ii1 = urllib . unquote_plus ( i111i1iIi1 [ "site" ] )
except : pass
try : ii1i1I1i = urllib . unquote_plus ( i111i1iIi1 [ "url" ] )
except : pass
try : ii11i1 = urllib . unquote_plus ( i111i1iIi1 [ "name" ] )
except : pass
try : OooooOo0 = int ( i111i1iIi1 [ "mode" ] )
except : pass
try : IIIii1II1II = urllib . unquote_plus ( i111i1iIi1 [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( i111i1iIi1 [ "fanart" ] )
except : pass
try : iIiI = urllib . unquote_plus ( i111i1iIi1 [ "description" ] )
except : pass
if 48 - 48: o0o0O00O00o0 / iIii1I11I1II1 + IiI1I1 + iIii1I11I1II1 . O0Oooo00
if OooooOo0 == None or ii1i1I1i == None or len ( ii1i1I1i ) < 1 : I1i1I1II ( )
if 60 - 60: OO0O00
if 98 - 98: o0o0O00O00o0
if 34 - 34: iIii1I11I1II1 * oOoO * oOoO / I1I1i1
if 28 - 28: O0Oooo00 - iIii1 + I111i1i1111i + iiIiIIi / iIii1I11I1II1
if 26 - 26: iIii1I11I1II1 - O0 . O0
elif OooooOo0 == 1 : OOO ( ii11i1 , ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 2 : o00oO0oo0OO ( ii11i1 , ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 3 : iI1iIIII1 ( ii11i1 , ii1i1I1i , IIIii1II1II )
if 68 - 68: IiI1I1 + iIii1 . O0 . iiIiIIi % i1IIi % IiI1I1
if 50 - 50: I11iii + Ii1Ii1iiii11
if 96 - 96: O0Oooo00
elif OooooOo0 == 4 : Iiii ( ii1i1I1i )
elif OooooOo0 == 5 : O0OOO ( ii1i1I1i )
elif OooooOo0 == 6 : I111I1Iiii1i ( )
elif OooooOo0 == 7 : o00oOOooOOo0o ( ii1i1I1i )
elif OooooOo0 == 8 : O0oOOoOooooO ( ii1i1I1i )
elif OooooOo0 == 9 : oOOOoo0O0oO ( ii1i1I1i )
elif OooooOo0 == 10 : IIiIiI ( ii1i1I1i )
elif OooooOo0 == 11 : O0Oo0oOOoooOOOOo ( )
elif OooooOo0 == 12 : oO00O000oO0 ( ii1i1I1i )
elif OooooOo0 == 13 : iIIii ( ii1i1I1i )
elif OooooOo0 == 14 : oo0oO ( ii1i1I1i )
elif OooooOo0 == 15 : ooO0O00Oo0o ( )
elif OooooOo0 == 16 : III1Ii1i1I1 ( ii11i1 , ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 17 : ooOOoooooo ( ii1i1I1i )
elif OooooOo0 == 18 : oo000o ( ii1i1I1i )
elif OooooOo0 == 19 : iiIIiiIi1Ii11 ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 20 : I1i ( )
elif OooooOo0 == 21 : O0OO0O ( ii1i1I1i )
elif OooooOo0 == 22 : II1i111Ii1i ( ii1i1I1i )
elif OooooOo0 == 23 : I1ii1iIiii1I ( )
elif OooooOo0 == 24 : OoOiiI1IIIi ( ii1i1I1i )
elif OooooOo0 == 25 : i11II1I11I1 ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 26 : o0OOOOooo ( ii1i1I1i )
elif OooooOo0 == 27 : OOoOoOo ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 28 : i1II ( )
elif OooooOo0 == 29 : i11IIIiIiIi ( ii1i1I1i )
elif OooooOo0 == 30 : ii1iIi1iIiI1i ( ii1i1I1i )
elif OooooOo0 == 31 : o0OIiiiI ( ii1i1I1i )
elif OooooOo0 == 32 : iiOOO0oOOoo ( ii1i1I1i )
elif OooooOo0 == 33 : I1IIIiI11i1 ( ii1i1I1i )
elif OooooOo0 == 34 : Oo0oooO0oO ( ii1i1I1i )
elif OooooOo0 == 35 : IIi1IIIIi ( )
elif OooooOo0 == 36 : i11iIIi11 ( ii1i1I1i )
elif OooooOo0 == 37 : o0O0O0 ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 38 : O0Oo00 ( )
elif OooooOo0 == 39 : o00Ooo0 ( ii1i1I1i )
elif OooooOo0 == 40 : I1i ( )
elif OooooOo0 == 41 : O0OO0O ( ii1i1I1i )
elif OooooOo0 == 42 : I11Ii11iI1 ( ii1i1I1i )
elif OooooOo0 == 43 : iIIIII1iiiiII ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 44 : I1iII11iIII1i1I ( )
if 92 - 92: i1iIii1Ii1II / i11iIiiIii + I1I1i1
elif OooooOo0 == 45 : II11iI111i1 ( )
elif OooooOo0 == 46 : OoO00 ( ii1i1I1i )
elif OooooOo0 == 47 : o00O00oO00 ( ii11i1 , ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 48 : ooo0O ( )
elif OooooOo0 == 49 : oO0oO0 ( ii1i1I1i )
elif OooooOo0 == 50 : IIi1ii1Ii ( ii1i1I1i )
elif OooooOo0 == 51 : iIiIi11Ii ( ii1i1I1i )
elif OooooOo0 == 52 : II11 ( ii1i1I1i )
elif OooooOo0 == 53 : III111i11IiI ( ii1i1I1i )
elif OooooOo0 == 54 : O00o00O ( ii1i1I1i , IIIii1II1II )
if 87 - 87: I111i1i1111i % iIii1I11I1II1
if 72 - 72: IiI1I1 . IiI1I1 - I1I1i1
if 48 - 48: i1iIii1Ii1II - o0o0O00O00o0 + i1iIii1Ii1II - II1iI * i11iIiiIii . iI
elif OooooOo0 == 59 : Ii1ii1IiIII ( )
elif OooooOo0 == 60 : ii11I1 ( ii1i1I1i )
elif OooooOo0 == 61 : OoOoOo00o0 ( ii11i1 , ii1i1I1i , IIIii1II1II )
if 35 - 35: I11iii . O0 + i1iIii1Ii1II + IiI1I1 + i1IIi
elif OooooOo0 == 66 : o0iiiI1I1iIIIi1 ( )
elif OooooOo0 == 67 : O000Oo0o ( ii1i1I1i )
elif OooooOo0 == 68 : OoOiIIiii ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 69 : oOOoo0o0OOOO ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 70 : Ii1iI111 ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 71 : I1I1i1I ( )
elif OooooOo0 == 72 : II1IiiIii ( )
elif OooooOo0 == 73 : o0OO0O0Oo ( )
elif OooooOo0 == 74 : iiIii1I ( ii1i1I1i )
elif OooooOo0 == 75 : iiiI1ii11 ( ii1i1I1i )
elif OooooOo0 == 76 : OOoO000O00oO ( )
elif OooooOo0 == 77 : o000O0OOoo ( )
elif OooooOo0 == 78 : o000 ( )
elif OooooOo0 == 79 : oo00OOoOoO00 ( )
elif OooooOo0 == 80 : i1IIiIi1IiI ( ii1i1I1i )
elif OooooOo0 == 81 : ooi1II1I ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 82 : II11i11II ( ii1i1I1i , IIIii1II1II )
if 65 - 65: O0 * II1iI / II1iI . I111i1i1111i
elif OooooOo0 == 83 : oooo00 ( ii1i1I1i )
elif OooooOo0 == 84 : II1i111 ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 85 : oOo0O0O0 ( ii1i1I1i )
elif OooooOo0 == 86 : Ooooo0OoO0 ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 87 : ooO0oo0o0 ( ii1i1I1i )
elif OooooOo0 == 88 : oooo00i1 ( ii1i1I1i )
if 87 - 87: O0Oo0oO0o * I1I1i1 % i1iIii1Ii1II * i1iIii1Ii1II
elif OooooOo0 == 90 : OoOOII1i11i1iIi11 ( ii1i1I1i )
elif OooooOo0 == 91 : i1i1 ( ii1i1I1i , IIIii1II1II )
elif OooooOo0 == 92 : I11iII ( ii11i1 , ii1i1I1i )
elif OooooOo0 == 93 : o00oo0000 ( ii1i1I1i )
elif OooooOo0 == 94 : OOOOOo ( ii1i1I1i )
elif OooooOo0 == 95 : i1i1IiIiIi1Ii ( ii1i1I1i )
if 58 - 58: IiI1I1 . Ii1Ii1iiii11 + II1iI % i1iIii1Ii1II - O0Oooo00
elif OooooOo0 == 100 : ii1I1I111 ( )
elif OooooOo0 == 101 : o0oO0oo0000OO ( ii1i1I1i )
elif OooooOo0 == 102 : i1i1II11II1 ( ii1i1I1i )
if 50 - 50: iI % O0Oo0oO0o - o0o0O00O00o0 . i1IIi + O0 % iI
if 10 - 10: iI . i1IIi + iiIiIIi
if 66 - 66: O0Oooo00 % Ii1Ii1iiii11
if 21 - 21: I111i1i1111i - OoooooooOO % i11iIiiIii
if 71 - 71: i1IIi - oOoO * OO0O00 + iIii1 - O0Oooo00 % I1I1i1
elif OooooOo0 == 884 : ooOo0O0O0oOO0 ( )
elif OooooOo0 == 885 : i1I1i1i ( )
elif OooooOo0 == 886 : O00oo ( )
elif OooooOo0 == 887 : oOo00OoO0O ( ii1i1I1i , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 888 : i1iI ( )
elif OooooOo0 == 889 : Ii1Iii11 ( ii1i1I1i , OooooOo0 , ii11i1 , IIIii1II1II , I1ii11iIi11i )
elif OooooOo0 == 890 : Ii11Iii ( )
elif OooooOo0 == 891 : II1III1i1iiI ( )
elif OooooOo0 == 892 : oOII1ii1ii11I1 ( )
if 63 - 63: iIii1I11I1II1 + IiI1I1 . O0Oooo00 / II1iI
oO ( )
if OooooOo0 == None or ii1i1I1i == None or len ( ii1i1I1i ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 84 - 84: i1IIi
if 42 - 42: O0Oo0oO0o - O0Oooo00 - OoooooooOO . iI / I111i1i1111i
if 56 - 56: i11iIiiIii - iIii1I11I1II1 . O0Oo0oO0o
if 81 - 81: I11iii / I111i1i1111i * I11iii . O0
if 61 - 61: O0Oooo00 * IiI1I1 + OO0O00 . iIii1I11I1II1 % oOoO . OO0O00
if 53 - 53: OO0O00 * I11iii / iIii1I11I1II1 / II1iI % I1I1i1
if 39 - 39: O0Oooo00 / OoooooooOO . O0Oooo00 * I1I1i1 / I111i1i1111i
if 38 - 38: O0Oooo00 / o0o0O00O00o0 % OO0O00 * oOoO + i11iIiiIii % o0o0O00O00o0
if 61 - 61: OO0O00 - iiIiIIi % I1I1i1 / o0o0O00O00o0 / iI + iIii1I11I1II1
if 87 - 87: OO0O00 + o0o0O00O00o0 + O0 / i1IIi % I11iii / OO0O00
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
