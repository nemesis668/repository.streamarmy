#########################################
############CODE BY @NEMZZY668###########
#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , uuid , os , re , sys , base64 , json , time , shutil , random , liveresolver , hashlib , datetime , smtplib , requests
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
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'plugin.video.nemesis'
iIiiiI1IiI1I1 = Addon ( IiII1IiiIiI1 , sys . argv )
o0OoOoOO00 = base64 . b64decode ( b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L0ZjcHQyNTN4' )
I11i = xbmcaddon . Addon ( id = IiII1IiiIiI1 )
O0O = '[COLOR aqua][B]Nemesis[/B][/COLOR]'
Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'favs.xml' ) )
I1ii11iIi11i = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.nemesis' )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'fanart.jpg' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'fanart.jpg' ) )
iIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'icon.png' ) )
Iii1ii1II11i = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads/' ) )
iI111iI = xbmcgui . DialogProgress ( )
IiII = xbmcgui . Dialog ( )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'intro.txt' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'download.xml' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'settings.xml' ) )
I1i1iiI1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'adult.txt' ) )
iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.SportsDevil' ) )
o0oO0 = base64 . b64decode ( b'NTEzNTMzNGRhYTMzMjUxYmM0MDdlNWYyNGNiMWM2YTU=' )
oo00 = [ 'program.plexus' ]
o00 = ''
Oo0oO0ooo = 'https://pastebin.com/raw/XK6h1Qur'
if 56 - 56: ooO00oOoo - O0OOo
if 8 - 8: Oooo0000 * i1IIi11111i / I11i1i11i1I % oo / OOO0O / oo0ooO0oOOOOo
def oO000OoOoo00o ( ) :
 if 31 - 31: i111IiI + iIIIiI11 . iII111ii
 i1iIIi1 = ii11iIi1I ( Oo0oO0ooo )
 if len ( i1iIIi1 ) > 1 :
  iI111I11I1I1 = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  OOooO0OOoo = os . path . join ( os . path . join ( iI111I11I1I1 , '' ) , 'compare.txt' )
  iIii1 = open ( OOooO0OOoo )
  oOOoO0 = iIii1 . read ( )
  if oOOoO0 == i1iIIi1 : pass
  else :
   O0OoO000O0OO ( '[B][COLOR aqua]N[COLOR yellow]emesis[COLOR aqua] I[COLOR yellow]nformation[/COLOR][/B]' , i1iIIi1 )
   iiI1IiI = open ( OOooO0OOoo , "w" )
   iiI1IiI . write ( i1iIIi1 )
   iiI1IiI . close ( )
def ii11iIi1I ( url ) :
 try :
  II = urllib2 . Request ( url )
  II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  ooOoOoo0O = urllib2 . urlopen ( II , timeout = 5 )
  OooO0 = ooOoOoo0O . read ( )
  ooOoOoo0O . close ( )
  if 35 - 35: Ooooo0Oo00oO0 % Ooo . oo0Oo00Oo0 % iIIIiI11
  return OooO0
 except : quit ( )
 if 35 - 35: I11i1i11i1I + iII111ii + iII111ii
def I11I11i1I ( ) :
 if 49 - 49: II111iiii % iII111ii * O0
 oOOo0oo = xbmc . getInfoLabel ( "System.BuildVersion" )
 o0oo0o0O00OO = float ( oOOo0oo [ : 4 ] )
 if o0oo0o0O00OO >= 11.0 and o0oo0o0O00OO <= 11.9 :
  o0oO = 'Eden'
 elif o0oo0o0O00OO >= 12.0 and o0oo0o0O00OO <= 12.9 :
  o0oO = 'Frodo'
 elif o0oo0o0O00OO >= 13.0 and o0oo0o0O00OO <= 13.9 :
  o0oO = 'Gotham'
 elif o0oo0o0O00OO >= 14.0 and o0oo0o0O00OO <= 14.9 :
  o0oO = 'Helix'
 elif o0oo0o0O00OO >= 15.0 and o0oo0o0O00OO <= 15.9 :
  o0oO = 'Isengard'
 elif o0oo0o0O00OO >= 16.0 and o0oo0o0O00OO <= 16.9 :
  o0oO = 'Jarvis'
 elif o0oo0o0O00OO >= 17.0 and o0oo0o0O00OO <= 17.9 :
  o0oO = 'Krypton'
 elif o0oo0o0O00OO >= 18.0 and o0oo0o0O00OO <= 18.9 :
  o0oO = 'Leia'
 else : o0oO = "Decline"
 if 48 - 48: i111IiI + i111IiI / II111iiii / iIii1I11I1II1
 if o0oO == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif o0oO == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif o0oO == "Leia" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 20 - 20: I11i1i11i1I
def oO00 ( ) :
 if 53 - 53: OoooooooOO . i1IIi
 ii1I1i1I = [ 'plugin.video.jenexporter' ]
 OOoo0O0 = any ( xbmc . getCondVisibility ( 'System.HasAddon(%s)' % ( addon ) ) for addon in ii1I1i1I )
 iiiIi1i1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.jenexporter' ) )
 if OOoo0O0 :
  import shutil
  shutil . rmtree ( iiiIi1i1I )
  os . _exit ( 1 )
 else :
  return
  if 80 - 80: i1IIi11111i - Oooo0000
def OOO00 ( ) :
 if 21 - 21: OoooooooOO - OoooooooOO
 iIii11I ( )
 oO00 ( )
 OOO0OOO00oo = baseurl
 Iii111II = OOO0OOO00oo
 oO000OoOoo00o ( )
 iiii11I = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( iiii11I >= 0000 ) and ( iiii11I <= 1159 ) : Ooo0OO0oOO = "Morning"
 elif ( iiii11I >= 1200 ) and ( iiii11I <= 1759 ) : Ooo0OO0oOO = "Afternoon"
 else : Ooo0OO0oOO = "Evening"
 ii11i1 ( '[COLOR yellow]Good[COLOR aqua] ' + str ( Ooo0OO0oOO ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , iIiiiI , I1IiI )
 ii11i1 ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , iIiiiI , I1IiI )
 try :
  OooO0 = IIIii1II1II ( baseurl )
  i1I1iI = re . compile ( '<item>(.+?)</item>' ) . findall ( OooO0 )
  for oo0OooOOo0 in i1I1iI :
   try :
    if '<m3u>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 11 , O00oO , o0OOO )
    elif '<mamahdsports>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 14 , O00oO , o0OOO )
    elif '<atc>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<atc>(.+?)</atc>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 6 , O00oO , o0OOO )
    elif '<scanner>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 11 , O00oO , o0OOO )
    elif '<cartoons>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 29 , O00oO , o0OOO )
    elif '<Adult>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 38 , O00oO , o0OOO )
    elif '<Anime>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 51 , O00oO , o0OOO )
    elif '<audiobooks>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 59 , O00oO , o0OOO )
    elif '<WORLDCUP>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<WORLDCUP>(.+?)</WORLDCUP>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 100 , O00oO , o0OOO )
    elif '<247shows>' in oo0OooOOo0 :
     o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     OOO0OOO00oo = re . compile ( '<247shows>(.+?)</247shows>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     I11i1I1I ( o0O , OOO0OOO00oo , 103 , O00oO , o0OOO )
    elif '<folder>' in oo0OooOOo0 :
     oO0Oo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 )
     for o0O , OOO0OOO00oo , O00oO , o0OOO in oO0Oo :
      I11i1I1I ( o0O , OOO0OOO00oo , 1 , O00oO , o0OOO )
    else :
     oOOoo0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oo0OooOOo0 )
     if len ( oOOoo0Oo ) == 1 :
      oO0Oo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 )
      o00OO00OoO = len ( i1I1iI )
      for o0O , OOO0OOO00oo , O00oO , o0OOO in oO0Oo :
       if 'youtube.com/playlist' in OOO0OOO00oo :
        I11i1I1I ( o0O , OOO0OOO00oo , 2 , O00oO , o0OOO )
       else :
        ii11i1 ( o0O , OOO0OOO00oo , 2 , O00oO , o0OOO )
     elif len ( oOOoo0Oo ) > 1 :
      o0O = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
      O00oO = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
      o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
      ii11i1 ( o0O , Iii111II , 3 , O00oO , o0OOO )
   except : pass
   if 60 - 60: Oooo0000 * i1IIi11111i - Oooo0000 % OoooooooOO - oo0Oo00Oo0 + ooO00oOoo
  ii11i1 ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , iIiiiI , I1IiI )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.resolveurl/settings.xml" )
   Ooo0OO0oOO = open ( file ) . read ( )
   O00Oo000ooO0 = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( Ooo0OO0oOO ) [ 0 ]
   O00Oo000ooO0 = O00Oo000ooO0 . strip ( )
   OOO0OOO00oo = 'plugin://script.module.resolveurl/?mode=auth_rd'
   if 'value=""' in O00Oo000ooO0 :
    OoO0O00 = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    ii11i1 ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( OoO0O00 ) + '[/COLOR]' , OOO0OOO00oo , 2 , iIiiiI , I1IiI )
   else :
    OoO0O00 = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    ii11i1 ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( OoO0O00 ) + '[/COLOR]' , 'url' , 999 , iIiiiI , I1IiI )
  except : pass
  IIiII = 'https://i.imgur.com/o2Wvut7.jpg'
  I11i1I1I ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , IIiII , I1IiI )
  o0 = 'https://i.imgur.com/SxZzRX9.jpg'
  I11i1I1I ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , o0 , I1IiI )
  ooOooo000oOO = 'https://i.imgur.com/zme6vuj.jpg'
  I11i1I1I ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , ooOooo000oOO , I1IiI )
 except :
  Oo0oOOo = IiII . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if Oo0oOOo == 0 :
   ii11i1 ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , iIiiiI , I1IiI )
   I11i1I1I ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , iIiiiI , I1IiI )
  if Oo0oOOo == 1 :
   quit ( )
   if 58 - 58: II111iiii * oo0ooO0oOOOOo * oo / oo0ooO0oOOOOo
   if 75 - 75: OOO0O
   if 50 - 50: iIIIiI11 / O0OOo - OOO0O - i111IiI % iII111ii - OOO0O
def OOO0o ( name , url , iconimage , fanart ) :
 IiII = xbmcgui . Dialog ( )
 Iii111II = url
 OooO0 = IIIii1II1II ( url )
 oO00 ( )
 i1I1iI = re . compile ( '<item>(.+?)</item>' ) . findall ( OooO0 )
 for oo0OooOOo0 in i1I1iI :
  try :
   if '<image>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 23 , iconimage , fanart )
   elif '<American>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 73 , iconimage , fanart )
   elif '<acechans>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<acechans>(.+?)</acechans>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 76 , iconimage , fanart )
   elif '<acechanstwo>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<acechanstwo>(.+?)</acechanstwo>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 77 , iconimage , fanart )
   elif '<acechansthree>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<acechansthree>(.+?)</acechansthree>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 78 , iconimage , fanart )
   elif '<acechansfour>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<acechansfour>(.+?)</acechansfour>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 79 , iconimage , fanart )
   elif '<bollywood>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<bollywood>(.+?)</bollywood>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 80 , iconimage , fanart )
   elif '<HDFLIX>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<HDFLIX>(.+?)</HDFLIX>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 83 , iconimage , fanart )
   elif '<RDMOVIES>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<RDMOVIES>(.+?)</RDMOVIES>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 85 , iconimage , fanart )
   elif '<NEWS>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<NEWS>(.+?)</NEWS>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 87 , iconimage , fanart )
   elif '<animemovie>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<animemovie>(.+?)</animemovie>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 88 , iconimage , fanart )
   elif '<animeshows>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<animeshows>(.+?)</animeshows>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 93 , iconimage , fanart )
   elif '<lordjd>' in oo0OooOOo0 :
    oOOoo0Oo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( oo0OooOOo0 )
    if len ( oOOoo0Oo ) == 1 :
     oO0Oo = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 )
     o00OO00OoO = len ( i1I1iI )
     for name , url , iconimage , fanart in oO0Oo :
      if 'youtube.com/playlist' in url :
       I11i1I1I ( name , url , 2 , iconimage , fanart )
      else :
       IiI1 ( name , url , 2 , iconimage , fanart )
    elif len ( oOOoo0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     IiI1 ( name , Iii111II , 3 , iconimage , fanart )
   elif '<reddit>' in oo0OooOOo0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( oo0OooOOo0 ) [ 0 ]
    I11i1I1I ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in oo0OooOOo0 :
    oOOoo0Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oo0OooOOo0 )
    if len ( oOOoo0Oo ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     Oo0O00Oo0o0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     O00O0oOO00O00 = Oo0O00Oo0o0
     i1 = "/"
     if not O00O0oOO00O00 . endswith ( i1 ) :
      Oo00 = O00O0oOO00O00 + "/"
     else :
      Oo00 = O00O0oOO00O00
     OooO0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = OooO0 + '%26referer=' + Oo00
     ii11i1 ( name , url , 10 , iconimage , fanart )
    elif len ( oOOoo0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     ii11i1 ( name , Iii111II , 16 , iconimage , fanart )
     if 31 - 31: Ooo . i1IIi11111i / O0
   elif '<folder>' in oo0OooOOo0 :
    oO0Oo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 )
    for name , url , iconimage , fanart in oO0Oo :
     I11i1I1I ( name , url , 1 , iconimage , fanart )
     if 89 - 89: i1IIi11111i
   else :
    oOOoo0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oo0OooOOo0 )
    if len ( oOOoo0Oo ) == 1 :
     oO0Oo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 )
     o00OO00OoO = len ( i1I1iI )
     for name , url , iconimage , fanart in oO0Oo :
      if 'youtube.com/playlist' in url :
       I11i1I1I ( name , url , 2 , iconimage , fanart )
      else :
       ii11i1 ( name , url , 2 , iconimage , fanart )
    elif len ( oOOoo0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oo0OooOOo0 ) [ 0 ]
     ii11i1 ( name , Iii111II , 3 , iconimage , fanart )
  except : pass
  if 68 - 68: Oooo0000 * OoooooooOO % O0 + Oooo0000 + oo0Oo00Oo0
 I11I11i1I ( )
 if 4 - 4: oo0Oo00Oo0 + O0 * oo0ooO0oOOOOo
 if 55 - 55: O0OOo + iIii1I11I1II1 / i1IIi11111i * OOO0O - i11iIiiIii - iIIIiI11
 if 25 - 25: oo
 if 7 - 7: i1IIi / ooO00oOoo * Ooo . Ooooo0Oo00oO0 . iIii1I11I1II1
 if 13 - 13: oo0ooO0oOOOOo / i11iIiiIii
 if 2 - 2: ooO00oOoo / O0 / I11i1i11i1I % i1IIi11111i % iIIIiI11
 if 52 - 52: I11i1i11i1I
 if 95 - 95: iIIIiI11
def O0oOO0O ( url ) :
 if 91 - 91: O0
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  try :
   oOOo0 = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
   url = 'https://www.reddit.com' + url
   iIiiiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   I11i1I1I ( "[COLOR skyblue]" + oOOo0 + "[/COLOR]" , url , 5 , iIiiiI , o0OOO )
  except : pass
  if 54 - 54: O0 - Ooooo0Oo00oO0 % oo0ooO0oOOOOo
def OOoO ( url ) :
 if 46 - 46: Oooo0000 . O0OOo - OoooooooOO
 ooo00OOOooO = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 O00OOOoOoo0O = [ "yalla" , "mlbstreams" , "livetvleak" ]
 iIiiiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 ii11i1 ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , iIiiiI , o0OOO )
 OooO0 = IIIii1II1II ( url )
 oOOoo0Oo = 0
 O000OOo00oo = re . compile ( 'href="([^"]+)' ) . findall ( OooO0 )
 for url in O000OOo00oo :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in ooo00OOOooO ) :
    oOOoo0Oo += 1
    oOOo0 = "Link " + str ( oOOoo0Oo ) + " :: "
    iIiiiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    oo0OOo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     ii11i1 ( "[COLOR skyblue]" + oOOo0 + url + "[/COLOR]" , url , 2 , iIiiiI , o0OOO )
    elif any ( x in url . lower ( ) for x in O00OOOoOoo0O ) :
     ii11i1 ( "[COLOR yellow]" + oOOo0 + url + "[/COLOR]" , oo0OOo , 2 , iIiiiI , o0OOO )
    else :
     ii11i1 ( "[COLOR skyblue]" + oOOo0 + url + "[/COLOR]" , oo0OOo , 2 , iIiiiI , o0OOO )
     if 64 - 64: i111IiI
     if 22 - 22: O0OOo + iIIIiI11 % oo
     if 9 - 9: OoooooooOO
def OOOOo ( url ) :
 if 76 - 76: Oooo0000
 if url == 'Football' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  I1iIIii = IIIii1II1II ( 'http://wizhdsports.is/sport/Cricket' )
 iIii1 = dom_parser2 . parse_dom ( I1iIIii , 'div' , { 'class' : 'card' } )
 iIii1 = [ ( dom_parser2 . parse_dom ( iii1i , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( iii1i , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( iii1i , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( iii1i , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for iii1i in iIii1 ]
 if len ( iIii1 ) < 1 :
  ii11i1 ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , O00oO , I1IiI , '' )
 iIii1 = [ ( iii1i [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , iii1i [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , iii1i [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , iii1i [ 2 ] [ 0 ] . content ) if iii1i [ 2 ] else 'Upcoming' , iii1i [ 3 ] [ 0 ] . content ) for iii1i in iIii1 ]
 if 39 - 39: iII111ii - O0 % i11iIiiIii * Ooo . Ooooo0Oo00oO0
 if 58 - 58: Oooo0000 % i11iIiiIii . iII111ii / OOO0O
 if 84 - 84: iII111ii . oo / O0OOo - ooO00oOoo / OoooooooOO / I11i1i11i1I
 if 12 - 12: ooO00oOoo * iII111ii % i1IIi % iIii1I11I1II1
 iIii1 = [ ( iii1i [ 0 ] , iii1i [ 1 ] , iii1i [ 2 ] , iii1i [ 3 ] , iii1i [ 4 ] ) for iii1i in iIii1 ]
 IIi1I11I1II = 0
 OooOoooOo = 0
 iI111iI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iI111iI . update ( 0 )
 for iii1i in iIii1 :
  ii11IIII11I = iii1i [ 0 ]
  iI111iI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( IIi1I11I1II ) )
  IIi1I11I1II += 1
  time . sleep ( 0.10 )
  ii11IIII11I = OOooo ( ii11IIII11I )
  oOooOOOoOo = iii1i [ 1 ]
  i1Iii1i1I = iii1i [ 3 ]
  if 'Match Over' in i1Iii1i1I :
   OooOoooOo += 1
  OOoO00 = dom_parser2 . parse_dom ( iii1i [ 4 ] , 'a' )
  for I1iIIii in OOoO00 :
   IiI111111IIII = re . sub ( '<.+?>' , '' , I1iIIii . content )
   OooO0 = I1iIIii . attrs [ 'href' ]
   OooO0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + OooO0
   if not 'Match Over' in i1Iii1i1I :
    ii11i1 ( '[COLOR aqua]' + ii11IIII11I + '[COLOR yellow]' + ' ' + i1Iii1i1I + '[/COLOR]' , OooO0 , 2 , O00oO , o0OOO )
 iI111iI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( IIi1I11I1II ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( OooOoooOo ) )
 time . sleep ( 3 )
 iI111iI . close ( )
 if 37 - 37: Ooo / i1IIi11111i
def i1I1iI1iIi111i ( url ) :
 if 44 - 44: i1IIi % II111iiii + i111IiI
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 i1I1iI = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = re . compile ( 'title="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  iIiiiI = re . compile ( 'src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  if 45 - 45: iII111ii / iII111ii + Ooo + oo0Oo00Oo0
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 19 , iIiiiI , I1IiI , '' )
  if 47 - 47: I11i1i11i1I + oo0Oo00Oo0
 try :
  OoO = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( OooO0 ) [ 0 ]
  iIiiiI = O00oO
  I11i1I1I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 18 , O00oO , I1IiI , '' )
 except : pass
 if 88 - 88: iII111ii . II111iiii * II111iiii % Ooo
def iiIIiiIi1Ii11 ( url , iconimage , fanart ) :
 if 65 - 65: II111iiii . oo0ooO0oOOOOo % i111IiI . i11iIiiIii + O0
 ii11i1 ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , iIiiiI , fanart , '' )
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 i1I1iI = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( OooO0 )
 if 26 - 26: i111IiI - iIii1I11I1II1 - ooO00oOoo / Oooo0000 . i1IIi11111i % iIii1I11I1II1
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oOOoo0Oo ) [ 0 ]
  oo0OOo = str . lower ( url )
  if '1e' in oo0OOo :
   oOOo0 = '1st Half'
  else :
   oOOo0 = '2nd Half'
  ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 2 , iIiiiI , fanart , '' )
  if 91 - 91: I11i1i11i1I . iIii1I11I1II1 / OOO0O + i1IIi
def I1i ( ) :
 if 53 - 53: oo * i1IIi11111i + oo0Oo00Oo0 - II111iiii
 OOO0OOO00oo = 'http://www.goalsarena.org/en/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1I1iI = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( i1I1iI )
 for Ii1I1I1i1Ii , i1Oo0oO00o in I1I11i :
  I11i1I1I ( "[COLOR skyblue]" + i1Oo0oO00o + "[/COLOR]" , Ii1I1I1i1Ii , 21 , iIiiiI , I1IiI , '' )
  if 13 - 13: i111IiI * O0OOo * oo0Oo00Oo0
def iI11iI1IiiIiI ( url ) :
 if 43 - 43: i11iIiiIii + O0OOo * II111iiii * Ooo * O0
 if 64 - 64: oo0ooO0oOOOOo % iIii1I11I1II1 * OOO0O
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Oo0oOOo = IiII . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if Oo0oOOo == 0 :
  try :
   i1I1iI = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
  except IndexError :
   IiII . notification ( O0O , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , iIiiiI , 9000 )
   quit ( )
  if 'ok.ru' in i1I1iI :
   o0iI11I1II ( o0O , i1I1iI , O00oO )
  Ii1I = IIIii1II1II ( i1I1iI )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ii1I ) [ 0 ]
  url = 'https:' + url
  IiI1i = xbmcgui . ListItem ( o0O , iconImage = O00oO , thumbnailImage = O00oO )
  xbmc . Player ( ) . play ( url , IiI1i , False )
  quit ( 0 )
 if Oo0oOOo == 1 :
  try :
   i1I1iI = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0 ) [ 1 ]
  except IndexError :
   IiII . notification ( O0O , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , iIiiiI , 9000 )
   time . sleep ( 2 )
   iI11iI1IiiIiI ( url )
  Ii1I = IIIii1II1II ( i1I1iI )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ii1I ) [ 0 ]
  url = 'https:' + url
  IiI1i = xbmcgui . ListItem ( o0O , iconImage = O00oO , thumbnailImage = O00oO )
  xbmc . Player ( ) . play ( url , IiI1i , False )
  quit ( 0 )
  if 92 - 92: Ooooo0Oo00oO0 . Ooooo0Oo00oO0 + Oooo0000
def IiIiI1111I1I ( ) :
 if 13 - 13: iIIIiI11 . i11iIiiIii
 OOO0OOO00oo = 'http://m.liveatc.net/feeds/'
 OooO0 = oOOoo00O00o ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'http://m.liveatc.net' + OOO0OOO00oo
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 7 , iIiiiI , I1IiI , '' )
  if 98 - 98: oo0ooO0oOOOOo + Ooooo0Oo00oO0 + OOO0O % OoooooooOO
def oooooo0O000o ( url ) :
 if 64 - 64: ooO00oOoo . I11i1i11i1I - Ooo / OoooooooOO
 if 66 - 66: iII111ii - iII111ii - i11iIiiIii . oo - oo0ooO0oOOOOo
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 8 , iIiiiI , I1IiI , '' )
  if 77 - 77: i1IIi11111i - II111iiii - oo0Oo00Oo0
def IiiiIIiIi1 ( url ) :
 url = url . replace ( ' ' , '%20' )
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li>(.+?)</a>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '(.+?)</li>' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 9 , iIiiiI , I1IiI , '' )
  if 74 - 74: iIii1I11I1II1 * oo + i1IIi11111i / i1IIi / II111iiii . O0OOo
def oooOo0OOOoo0 ( url ) :
 if 51 - 51: O0OOo / i1IIi11111i . oo0ooO0oOOOOo * I11i1i11i1I + Oooo0000 * Ooooo0Oo00oO0
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li>(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  try :
   oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
   ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 10 , iIiiiI , I1IiI , '' )
  except :
   ii11i1 ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , iIiiiI , I1IiI , '' )
   if 73 - 73: Oooo0000 + OoooooooOO - O0 - iIIIiI11 - II111iiii
def O0Oo0oOOoooOOOOo ( ) :
 if 62 - 62: oo0Oo00Oo0
 I11i1I1I ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , iIiiiI , I1IiI , '' )
 OOO0OOO00oo = 'http://m.broadcastify.com/?a=la&coid=1'
 OooO0 = oOOoo00O00o ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'http://m.broadcastify.com' + OOO0OOO00oo
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 12 , iIiiiI , I1IiI , '' )
  if 74 - 74: iII111ii + I11i1i11i1I
def oO00O000oO0 ( url ) :
 if 79 - 79: i111IiI - OoooooooOO - OOO0O - iIii1I11I1II1 * oo0ooO0oOOOOo
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 13 , iIiiiI , I1IiI , '' )
  if 4 - 4: i11iIiiIii . OoooooooOO / Oooo0000 % Ooo % i111IiI * O0
def iIIii ( url ) :
 if 92 - 92: iIIIiI11 + OOO0O % oo0ooO0oOOOOo
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 14 , iIiiiI , I1IiI , '' )
  if 62 - 62: oo / i1IIi
def oo0oO ( url ) :
 if 94 - 94: iIii1I11I1II1 / O0OOo % iII111ii * iII111ii * II111iiii
 OooO0 = oOOoo00O00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  i1I1iI = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
 except :
  IiII . notification ( O0O , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , iIiiiI , 5000 )
 IIiIiI ( i1I1iI )
 if 94 - 94: OOO0O . i1IIi - I11i1i11i1I % O0 - Oooo0000
def ooO0O00Oo0o ( ) :
 if 65 - 65: oo . i111IiI - Ooo * Ooooo0Oo00oO0 / Ooo / oo0Oo00Oo0
 OOO0OOO00oo = 'http://m.broadcastify.com/?a=top25'
 OooO0 = oOOoo00O00o ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  i111iIi1i1II1 = oOOo0 . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  oOOo0 = oOOo0 . split ( ')' ) [ - 1 ] . strip ( )
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'http://m.broadcastify.com' + OOO0OOO00oo
  ii11i1 ( "[COLOR aqua]" + oOOo0 + "[COLOR yellow] :: " + i111iIi1i1II1 + " Listening" + "[/COLOR]" , OOO0OOO00oo , 14 , iIiiiI , I1IiI , '' )
  if 86 - 86: iIii1I11I1II1 / i1IIi11111i . II111iiii
def II1i111Ii1i ( url ) :
 if 15 - 15: II111iiii / i1IIi
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  iIiiiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  o0OOO = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in oOOo0 :
    oo0OOo = 'https://www.youtube.com' + url
    ii11i1 ( "[COLOR aqua][B]" + oOOo0 + "[/B][/COLOR]" , oo0OOo , 2 , iIiiiI , o0OOO )
    if 7 - 7: ooO00oOoo
def I1ii1iIiii1I ( ) :
 if 42 - 42: I11i1i11i1I + i1IIi - iIIIiI11 / Ooooo0Oo00oO0
 OOO0OOO00oo = 'http://burningwhee1s.blogspot.co.uk/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( i1I1iI )
 for OooO0 , oOOo0 in I1I11i :
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OooO0 , 24 , iIiiiI , I1IiI , '' )
  if 9 - 9: O0 % O0 - I11i1i11i1I
def OoOiiI1IIIi ( url ) :
 if 47 - 47: O0OOo % i111IiI % i11iIiiIii - O0 + oo0Oo00Oo0
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  iIiiiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( oOOoo0Oo ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 25 , iIiiiI , I1IiI , '' )
  if 94 - 94: Ooo
def i11II1I11I1 ( url , iconimage ) :
 if 67 - 67: ooO00oOoo - I11i1i11i1I / i111IiI - i1IIi
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( i1I1iI )
 try :
  for oOOoo0Oo in I1I11i :
   oOOo0 = re . compile ( '<b>(.+?)</b>' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    i1II1 = re . compile ( '<b>(.+?)</b>' ) . findall ( oOOoo0Oo ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     i1II1 = re . compile ( '<b>(.+?)</b>' ) . findall ( oOOoo0Oo ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     i1II1 = ''
   oOOo0 = O0oO0 ( oOOo0 )
   i1II1 = O0oO0 ( i1II1 )
   i11i1 = re . compile ( '<option value="(.+?)"' ) . findall ( oOOoo0Oo ) [ 1 ]
   ii11i1 ( "[COLOR aqua]" + oOOo0 + "  " + i1II1 + "[/COLOR]" , i11i1 , 2 , iIiiiI , I1IiI , '' )
 except :
  ii11i1 ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , iIiiiI , I1IiI , '' )
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / oo . i11iIiiIii % i111IiI
def i1iI ( ) :
 if 29 - 29: ooO00oOoo % oo0ooO0oOOOOo - ooO00oOoo / oo0ooO0oOOOOo . i1IIi
 OOO0OOO00oo = 'https://api.themoviedb.org/3/movie/popular?api_key=' + o0oO0 + '&language=en-US&page=1'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 oO0Oo = json . loads ( OooO0 )
 i11III1111iIi = oO0Oo [ 'results' ]
 for I1i111I in i11III1111iIi :
  try :
   OooOo0oo0O0o00O = 'https://image.tmdb.org/t/p/original'
   oOOo0 = I1i111I [ 'title' ]
   iIiiiI = I1i111I [ 'poster_path' ]
   I1i11 = I1i111I [ 'id' ]
   iIiiiI = OooOo0oo0O0o00O + iIiiiI
   o0OOO = I1i111I [ 'backdrop_path' ]
   o0OOO = OooOo0oo0O0o00O + o0OOO
   IiIi1I1 = I1i111I [ 'overview' ]
   I1i11 = str ( I1i11 )
   I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , oOOo0 , 33 , iIiiiI , o0OOO , IiIi1I1 )
  except : pass
  if 39 - 39: II111iiii + i1IIi11111i - oo0Oo00Oo0 . i1IIi11111i
def OOOooo ( url ) :
 if 94 - 94: OoooooooOO + O0OOo / i1IIi11111i * oo0ooO0oOOOOo
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  iIiiiI = re . compile ( '<img src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  o0OOO = re . compile ( '<img src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = re . compile ( '<i>(.+?)</i>' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = oOOo0 . strip ( )
  I11i1I1I ( "[COLOR aqua][B]" + oOOo0 + "[/B][/COLOR]" , url , 27 , iIiiiI , o0OOO , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( OooO0 ) [ 0 ]
  o0OO0o0oOOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'nextpage.png' ) )
  I11i1I1I ( '[COLOR yellow]Next Page >>[/COLOR]' , o0OOo0o0O0O , 26 , o0OO0o0oOOO0O , o0OOO )
 except : pass
 if 49 - 49: oo . I11i1i11i1I . II111iiii
def o000ooooO0o ( url , iconimage ) :
 if 40 - 40: oo + i1IIi * oo0ooO0oOOOOo
 OooO0 = IIIii1II1II ( url )
 iIiiiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( OooO0 ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 i1I1iI = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( OooO0 )
 iI111iI . create ( O0O , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iI111iI . update ( 0 )
 iii1i = 1
 O0oOOoooOO0O = [ ]
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  O0oOOoooOO0O . append ( url )
  iI111iI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( iii1i ) )
  time . sleep ( 0.02 )
  iii1i += 1
  oOOo0 = re . compile ( '(.+?)</p>' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( 'Server' , '' )
  oOOo0 = oOOo0 . strip ( )
 ooo00Ooo = 1
 Ooo0OO0oOO = 0
 Oo0o0O00 = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 40 - 40: OoooooooOO
  if iI111iI . iscanceled ( ) :
   iI111iI . close ( )
   quit ( )
  if Ooo0OO0oOO > len ( O0oOOoooOO0O ) :
   IiII . notification ( O0O , "[COLOR yellow]None of the links played![/COLOR]" , iIiiiI , 50 )
   quit ( )
   if 25 - 25: Ooooo0Oo00oO0 + iIIIiI11 / oo0Oo00Oo0 . I11i1i11i1I % O0 * Oooo0000
  if Oo0o0O00 == 0 :
   Ooo0OO0oOO += 1
   iI111iI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( Ooo0OO0oOO ) + "[/COLOR]" , '' )
   try :
    OooO0 = IIIii1II1II ( O0oOOoooOO0O [ Ooo0OO0oOO ] )
    I1I11i = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( OooO0 ) [ 0 ]
    o0O0oo0OO0O = base64 . b64decode ( I1I11i )
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O0oo0OO0O ) [ 0 ]
    OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'blacklist.txt' ) )
    o0Oooo = open ( OO0 ) . read ( )
    iiI = re . compile ( '<url>(.+?)</url>' ) . findall ( o0Oooo )
    for oO in iiI :
     IIiIi = re . compile ( '<bad>(.+?)<bad>' ) . findall ( oO ) [ 0 ]
     if url == IIiIi :
      url = 'bad'
      iI111iI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( Ooo0OO0oOO ) )
      time . sleep ( 0.5 )
      Oo0o0O00 = 5
      pass
    import resolveurl
    if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
     OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     OOoOooOoOOOoo = liveresolver . resolve ( url )
    else : OOoOooOoOOOoo = url
    IiI1i = xbmcgui . ListItem ( o0O , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( OOoOooOoOOOoo , IiI1i , False )
   except :
    iI111iI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( Ooo0OO0oOO ) )
    time . sleep ( 0.5 )
    Oo0o0O00 = 5
    pass
  if Oo0o0O00 == 5 :
   Oo0o0O00 = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   Oo0o0O00 += 1
   if 25 - 25: OoooooooOO - ooO00oOoo . ooO00oOoo * OOO0O
 try : iI111iI . close ( )
 except : pass
 time . sleep ( 15 )
 OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'blacklist.txt' ) )
 O00O0oOO00O00 = xbmcgui . Dialog ( ) . yesno ( O0O , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if O00O0oOO00O00 :
  IiII . notification ( O0O , "[COLOR aqua]Enjoy Your Content![/COLOR]" , iIiiiI , 500 )
  quit ( )
 else :
  with open ( OO0 , "a" ) as o000oo :
   o000oo . write ( '<url><bad>' + url + '<bad></url>\n' )
   IiII . notification ( O0O , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , iIiiiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 95 - 95: oo0Oo00Oo0 / oo0Oo00Oo0
def IIiI1Ii ( url ) :
 if 57 - 57: oo0ooO0oOOOOo - oo0Oo00Oo0 - i111IiI + Oooo0000
 if 30 - 30: iIIIiI11 % i1IIi11111i + i1IIi - i111IiI - iIIIiI11
 if url == 'search' :
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Search Term' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1 . lower ( )
    if 52 - 52: oo - O0OOo + oo % I11i1i11i1I
   else :
    IiII . notification ( O0O , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , O00oO , 5000 )
    quit ( )
  else :
   IiII . notification ( O0O , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , O00oO , 5000 )
   quit ( )
  O00Ooo = O00Ooo . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + O00Ooo + '.html'
  iI1 ( url , iIiiiI )
  if 12 - 12: ooO00oOoo . i1IIi + i1IIi11111i + oo0ooO0oOOOOo + ooO00oOoo / iII111ii
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  iI1 ( url , iIiiiI )
  if 12 - 12: oo0ooO0oOOOOo - oo0Oo00Oo0 . OoooooooOO / oo . i1IIi * Oooo0000
def iI1 ( url , icon ) :
 if 19 - 19: i11iIiiIii + OoooooooOO - O0OOo - i111IiI
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = re . compile ( '<i>(.+?)</i>' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  I11i1I1I ( "[COLOR aqua][B]" + oOOo0 + "[/B][/COLOR]" , url , 27 , icon , o0OOO )
  if 21 - 21: O0 % Ooooo0Oo00oO0 . ooO00oOoo / II111iiii + Ooooo0Oo00oO0
def OOOO0O00o ( ) :
 if 62 - 62: iIii1I11I1II1
 OOO0OOO00oo = 'http://www.genti.stream/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  i1II = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ] . strip ( )
  iI1I = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 1 ] . strip ( )
  OOO0OOO00oo = re . compile ( 'href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'http://www.genti.stream/' + OOO0OOO00oo
  ii11i1 ( "[COLOR aqua]" + i1II + "[COLOR yellow] vs [COLOR aqua]" + iI1I + "[/COLOR]" , OOO0OOO00oo , 39 , iIiiiI , o0OOO )
  if 100 - 100: iIii1I11I1II1 + i1IIi11111i / O0OOo . i11iIiiIii
def III1I1Iii1iiI ( url ) :
 if 17 - 17: iIIIiI11 % iIii1I11I1II1 - iIii1I11I1II1
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0o0O0 = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
 if not 'http' in O0o0O0 :
  O0o0O0 = 'http://www.genti.stream' + O0o0O0
 Ii1I1I1i1Ii = IIIii1II1II ( O0o0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ii1II1I11i1 = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( Ii1I1I1i1Ii ) [ 0 ]
 Ii1I = IIIii1II1II ( Ii1II1I11i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( Ii1I ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( Ii1I ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( Ii1I ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( Ii1I ) [ 0 ]
 except : pass
 if 59 - 59: OOO0O % iIii1I11I1II1 . i1IIi
 if 'http' not in url :
  IiII . notification ( O0O , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , O00oO , 5000 )
  quit ( )
 o0iI11I1II ( o0O , url , O00oO )
 if 21 - 21: O0OOo
 if 29 - 29: i111IiI / II111iiii / oo0Oo00Oo0 * oo0ooO0oOOOOo
def I111i1i1111 ( url ) :
 if 49 - 49: Oooo0000 / OOO0O + O0 * I11i1i11i1I
 url = 'http://www.toonget.net/cartoon'
 OooO0 = IIIii1II1II ( url )
 I1I11i = re . compile ( '<td><a href="(.+?)">(.+?)</a>' ) . findall ( OooO0 )
 for url , oOOo0 in I1I11i :
  I11i1I1I ( "[COLOR aqua][B]" + oOOo0 + "[/B][/COLOR]" , url , 30 , iIiiiI , o0OOO , '' )
  if 28 - 28: oo0Oo00Oo0 + i11iIiiIii / i111IiI % i1IIi11111i % O0OOo - O0
def ooo0OOO ( url ) :
 if 49 - 49: i11iIiiIii % iIIIiI11 . i1IIi11111i
 OooO0 = IIIii1II1II ( url )
 try :
  iIiiiI = re . compile ( '<div class="left_col">.+?<img src="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
 except :
  iIiiiI = O00oO
 try :
  Ii1i1iI = re . compile ( '<span>Description:</span>.+?<div>(.+?)</div>' ) . findall ( OooO0 ) [ 0 ] . strip ( )
 except :
  Ii1i1iI = 'No Description Found'
 i1I1iI = re . compile ( '<div id="videos">(.+?)</div>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<li>.+?<a href="(.+?)">(.+?)</a>' ) . findall ( i1I1iI )
 for url , oOOo0 in I1I11i :
  I11i1I1I ( "[COLOR aqua][B]" + oOOo0 + "[/B][/COLOR]" , url , 31 , iIiiiI , o0OOO , Ii1i1iI )
  if 16 - 16: oo0ooO0oOOOOo / O0OOo / OoooooooOO * ooO00oOoo + i1IIi % oo0ooO0oOOOOo
 try :
  ooo0o00 = re . compile ( '<ul class="pagination">(.+?)</ul>' ) . findall ( OooO0 ) [ 0 ] . strip ( )
  ooO = re . compile ( 'href="(.+?)"' ) . findall ( ooo0o00 ) [ 0 ]
  I11i1I1I ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , ooO , 30 , O00oO , o0OOO )
 except : pass
 if 74 - 74: ooO00oOoo
def o0o0oOoOO0O ( url ) :
 if 16 - 16: Ooooo0Oo00oO0 % iIii1I11I1II1 . iIIIiI11
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<iframe src="(.+?)"' ) . findall ( OooO0 )
 iii1i = 0
 for oooooOOO000Oo in i1I1iI :
  iii1i += 1
  oOOo0 = 'Stream : ' + str ( iii1i )
  ii11i1 ( oOOo0 , oooooOOO000Oo , 32 , O00oO , o0OOO )
  if 52 - 52: II111iiii % Ooooo0Oo00oO0 . i1IIi11111i * iIii1I11I1II1
def I111i1II ( url ) :
 if 69 - 69: iIIIiI11 * O0 . i11iIiiIii / iIIIiI11 . I11i1i11i1I
 OooO0 = IIIii1II1II ( url )
 if 'easyvideome' in url or 'videozoo' in url :
  O0oOOo = re . compile ( 'file:.+?"(.+?)"' ) . findall ( OooO0 ) [ 1 ]
  o0iI11I1II ( o0O , O0oOOo , O00oO )
 elif 'playpandanet' in url :
  O0oOOo = re . compile ( """url:.+?'(.+?)'""" ) . findall ( OooO0 ) [ 0 ]
  o0iI11I1II ( o0O , O0oOOo , O00oO )
 else :
  IiII . notification ( O0O , 'Sorry This Link Is Down, Try Another' , O00oO , 4000 )
  if 31 - 31: iII111ii / O0OOo - iII111ii - oo0ooO0oOOOOo
  if 7 - 7: iII111ii % O0 . i1IIi11111i + ooO00oOoo - i111IiI
def o0o0O00oo0 ( ) :
 if 27 - 27: i11iIiiIii % II111iiii % i111IiI . O0 - O0OOo + i1IIi11111i
 OOO0OOO00oo = "http://www.loyalbooks.com/genre-menu"
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( OooO0 )
 for oo0OooOOo0 in i1I1iI :
  if "paid" not in oo0OooOOo0 :
   Ii1I1I1i1Ii = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
   Ii1I = "http://www.loyalbooks.com" + Ii1I1I1i1Ii
   o0O = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
   I11i1I1I ( "[COLOR aqua]" + o0O + "[/COLOR]" , Ii1I , 60 , iIiiiI , I1IiI , '' )
   if 57 - 57: iIii1I11I1II1 / i111IiI - i1IIi
def ooOOo00O00Oo ( url ) :
 if 42 - 42: O0 / I11i1i11i1I + OoooooooOO * oo0Oo00Oo0 % oo0Oo00Oo0
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( OooO0 ) [ 0 ]
 i1iIi = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( i1I1iI )
 for oo0OooOOo0 in i1iIi :
  oo0OOo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
  Ii1I = "http://www.loyalbooks.com" + oo0OOo
  iIiiiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
  O00oO = "http://www.loyalbooks.com" + iIiiiI
  o0O = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + o0O + "[/COLOR]" , Ii1I , 61 , O00oO , I1IiI , '' )
 try :
  OooO0 = IIIii1II1II ( url )
  OoO = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( OooO0 ) [ 0 ]
  iIiiiI = 'https://i.imgur.com/pOefPvV.jpg'
  I11i1I1I ( "[COLOR yellow]Next Page -->[/COLOR]" , OoO , 60 , iIiiiI , I1IiI , '' )
 except : pass
 if 21 - 21: OOO0O / oo + iIIIiI11 + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + iII111ii + oo0Oo00Oo0 * i11iIiiIii
def OoOoOo00o0 ( name , url , iconimage ) :
 if 90 - 90: O0OOo % O0 * iIii1I11I1II1 . iII111ii
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( OooO0 )
 for oo0OooOOo0 in i1I1iI :
  oOOo0 = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
  oo0OOo = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( oo0OooOOo0 ) [ 0 ]
  ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , oo0OOo , 10 , iconimage , I1IiI , '' )
  if 8 - 8: oo0Oo00Oo0 + II111iiii / iII111ii / i111IiI
def ooo0O ( ) :
 if 16 - 16: i1IIi11111i
 OOO0OOO00oo = 'http://www.shadownet.me/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( i1I1iI )
 for OOO0OOO00oo , oOOo0 in I1I11i :
  oOOo0 = O0oO0 ( oOOo0 )
  if 'P2P' not in oOOo0 :
   I11i1I1I ( "[COLOR skyblue]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 49 , iIiiiI , I1IiI , '' )
   if 41 - 41: i1IIi * II111iiii / OoooooooOO . oo0ooO0oOOOOo
   if 83 - 83: iII111ii . O0 / O0OOo / oo0ooO0oOOOOo - II111iiii
def oO0oO0 ( url ) :
 if 14 - 14: iII111ii
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( i1I1iI )
 for oOOoo0Oo in I1I11i :
  oOOo0 = re . compile ( 'alt="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  iIiiiI = re . compile ( '<img src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  ii11i1 ( "[COLOR skyblue]" + oOOo0 + "[/COLOR]" , url , 50 , iIiiiI , I1IiI , '' )
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( OooO0 ) [ 0 ]
  iIiiiI = 'http://i.imgur.com/CIZ8oYV.png'
  I11i1I1I ( "[COLOR orange]Next Page --->[/COLOR]" , o0OOo0o0O0O , 49 , iIiiiI , I1IiI , '' )
 except : pass
 if 99 - 99: iII111ii
def IIi1ii1Ii ( url ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + iII111ii - i11iIiiIii + oo0ooO0oOOOOo
 def ii1i ( url ) :
  II = urllib2 . Request ( url )
  II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  II . add_header ( 'Referer' , url )
  ooOoOoo0O = urllib2 . urlopen ( II , timeout = 5 )
  OooO0 = ooOoOoo0O . read ( )
  ooOoOoo0O . close ( )
  return OooO0
  if 62 - 62: Oooo0000 / oo
 OooO0 = ii1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  i1I1iI = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( OooO0 ) [ 0 ]
 except IndexError :
  IiII . notification ( O0O , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , iIiiiI , 5000 )
  quit ( )
 if 'youtube' in i1I1iI :
  url = i1I1iI
  o0iI11I1II ( o0O , url , O00oO )
 Ii1I = ii1i ( i1I1iI )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( Ii1I ) [ 0 ]
 if 'http://thepk.co' in url :
  IiII . notification ( O0O , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , iIiiiI , 5000 )
  quit ( )
 IiII . notification ( O0O , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , iIiiiI , 5000 )
 if 7 - 7: OoooooooOO . Ooooo0Oo00oO0
 import liveresolver
 import resolveurl
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  IiI1i = xbmcgui . ListItem ( o0O , iconImage = O00oO , thumbnailImage = O00oO )
  IiI1i . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , IiI1i , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  IiI1i = xbmcgui . ListItem ( o0O , iconImage = O00oO , thumbnailImage = O00oO )
  IiI1i . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , IiI1i , False )
 else :
  if '.m3u8' in url :
   oo0OOo = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + o0O + '&amp;url=' + url + '&amp;iconImage=' + O00oO
  elif '.ts' in url :
   oo0OOo = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + o0O + '&amp;url=' + url + '&amp;iconImage=' + O00oO
  else :
   oo0OOo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 53 - 53: iIIIiI11 % iIIIiI11 * I11i1i11i1I + i1IIi11111i
  IiI1i = xbmcgui . ListItem ( o0O , iconImage = O00oO , thumbnailImage = O00oO )
  IiI1i . setPath ( url )
  if 92 - 92: OoooooooOO + i1IIi / iIIIiI11 * O0
  xbmc . Player ( ) . play ( oo0OOo , IiI1i , False )
  if 100 - 100: oo0Oo00Oo0 % iIii1I11I1II1 * II111iiii - iII111ii
  if 92 - 92: oo0Oo00Oo0
def II11iI111i1 ( ) :
 if 95 - 95: OoooooooOO - Ooooo0Oo00oO0 * ooO00oOoo + i1IIi11111i
 OOO0OOO00oo = 'https://m.skylinewebcams.com/en/webcam'
 OooO0 = IIIii1II1II ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I11i = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( OooO0 ) [ 0 ]
 iIi1 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I11i )
 for OOO0OOO00oo , oOOo0 in iIi1 :
  if 'http|https' not in OOO0OOO00oo :
   OOO0OOO00oo = 'https://m.skylinewebcams.com' + OOO0OOO00oo
   I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 46 , iIiiiI , I1IiI , '' )
   if 21 - 21: i111IiI
def OoO00 ( url ) :
 if 85 - 85: O0OOo * O0OOo * ooO00oOoo . OoooooooOO . iIIIiI11 * oo0Oo00Oo0
 OooO0 = IIIii1II1II ( url )
 I1I11i = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( OooO0 )
 for url , iIiiiI , oOOo0 in I1I11i :
  if 'https:' not in iIiiiI :
   iIiiiI = 'https:' + iIiiiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 47 , iIiiiI , I1IiI , '' )
  if 65 - 65: oo0ooO0oOOOOo * Ooo
  if 79 - 79: OoooooooOO - ooO00oOoo
def o00O00oO00 ( name , url , iconimage ) :
 if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * Ooooo0Oo00oO0
 OooO0 = IIIii1II1II ( url )
 try :
  IiII . notification ( O0O , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , iIiiiI , 5000 )
  i1I1iI = re . compile ( '<amp-video src="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
  url = 'https:' + i1I1iI
  IiI1i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , IiI1i , False )
  if 9 - 9: Ooooo0Oo00oO0 - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 except : pass
 quit ( 0 )
 if 39 - 39: Ooooo0Oo00oO0 * O0OOo + iIii1I11I1II1 - Ooooo0Oo00oO0 + oo0ooO0oOOOOo
def o0iiiI1I1iIIIi1 ( ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / i111IiI % II111iiii % i1IIi / i11iIiiIii
 OOO0OOO00oo = 'https://watchepisodeseries.unblocked.vet/home/schedule'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( i1I1iI )
 for OOO0OOO00oo , OOO , Iiiiii1iI in I1I11i :
  I11i1I1I ( "[COLOR aqua]" + OOO + "  " + Iiiiii1iI + "[/COLOR]" , OOO0OOO00oo , 67 , iIiiiI , o0OOO )
  if 49 - 49: I11i1i11i1I . Ooooo0Oo00oO0 / Oooo0000 + II111iiii
  if 47 - 47: O0 / iIIIiI11
def oO0OO0 ( url ) :
 if 82 - 82: Ooooo0Oo00oO0 - Ooooo0Oo00oO0 + i1IIi11111i
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 1 ]
  oOOo0 = O0oO0 ( oOOo0 )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  O00oO = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oOOoo0Oo ) [ 0 ]
  o0OOO = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oOOoo0Oo ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 68 , O00oO , o0OOO )
  if 8 - 8: I11i1i11i1I % iII111ii * OOO0O % iIIIiI11 . oo0Oo00Oo0 / oo0Oo00Oo0
  if 81 - 81: Oooo0000
def oO0o00oOOooO0 ( url , iconimage , fanart ) :
 if 79 - 79: Oooo0000 - iIii1I11I1II1 + iIIIiI11 - Ooo
 OooO0 = IIIii1II1II ( url )
 OoOiIIiii = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in OoOiIIiii :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
 i1I1iI = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( OooO0 )
 iii1i = datetime . now ( )
 for oOOoo0Oo in i1I1iI :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '////' , '//' )
   oOOo0 = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ]
   oOOo0 = O0oO0 ( oOOo0 )
   O0i11i1iiI1i = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ]
   oO0oOOoo00000 = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ]
   OOO = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in OOO :
    OOO = OOO . strip ( )
    OOO = time . strptime ( OOO , "%d/%m/%Y" )
    oOo00 = ( "%s/%s/%s" % ( iii1i . day , iii1i . month , iii1i . year ) )
    oOo00 = time . strptime ( oOo00 , "%d/%m/%Y" )
    if ( oOo00 < OOO ) :
     oOOo0 = '[COLOR yellow]' + ( oOOo0 ) + ' - Not Aired Yet' + '[/COLOR]'
     oO0oOOoo00000 = '[COLOR yellow]' + ( oO0oOOoo00000 ) + '[/COLOR]'
     O0i11i1iiI1i = '[COLOR yellow]' + ( O0i11i1iiI1i ) + '[/COLOR]'
     if 3 - 3: iII111ii % i1IIi
    if not 'Season 0' in O0i11i1iiI1i :
     I11i1I1I ( "[COLOR aqua]" + O0i11i1iiI1i + " " + oO0oOOoo00000 + " " + oOOo0 + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 46 - 46: II111iiii % I11i1i11i1I % iIii1I11I1II1 - O0OOo . OoooooooOO - Ooooo0Oo00oO0
  if 59 - 59: Ooooo0Oo00oO0 . oo0ooO0oOOOOo % II111iiii
def i11I1iIi ( url , iconimage , fanart ) :
 if 79 - 79: Ooo . OOO0O - II111iiii . ooO00oOoo % oo0Oo00Oo0
 if 65 - 65: ooO00oOoo + i1IIi11111i / oo0ooO0oOOOOo
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  try :
   oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
   oOOo0 = oOOo0 . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
   if not 'Lolzor.Com' in oOOo0 :
    if not 'Videoplayer.Gq' in oOOo0 :
     if not 'Vidbaba.Com' in oOOo0 :
      if not 'Gagomatic.Com' in oOOo0 :
       if not 'Favour.Me' in oOOo0 :
        if not 'Funblr.Com' in oOOo0 :
         if not 'Vid.Ag' in oOOo0 :
          if not 'Mycollection.Net' in oOOo0 :
           if not 'Adhqmedia.Com' in oOOo0 :
            if not 'Filenuke.Com' in oOOo0 :
             if not 'Mrfile.Me' in oOOo0 :
              ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 83 - 83: I11i1i11i1I . iII111ii - O0OOo
  if 65 - 65: iIii1I11I1II1 / oo0Oo00Oo0 . Ooooo0Oo00oO0 - II111iiii
def Oo000 ( url , iconimage , fanart ) :
 IiII . notification ( O0O , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , iIiiiI , 5000 )
 url = url . replace ( '////' , '//' )
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  url = re . compile ( 'href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  import resolveurl
  try :
   if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
    OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    OOoOooOoOOOoo = liveresolver . resolve ( url )
   else : OOoOooOoOOOoo = url
   IiI1i = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   IiI1i . setPath ( OOoOooOoOOOoo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI1i )
   xbmc . Player ( ) . play ( OOoOooOoOOOoo )
   if 81 - 81: oo0ooO0oOOOOo - oo0ooO0oOOOOo % II111iiii * Oooo0000
  except :
   IiII . notification ( O0O , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , iIiiiI , 5000 )
   if 39 - 39: i111IiI
def ooO000O000 ( ) :
 if 19 - 19: iIii1I11I1II1
 III11I1 = ''
 IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Search Term' )
 IIi1IIIi . doModal ( )
 if IIi1IIIi . isConfirmed ( ) :
  III11I1 = IIi1IIIi . getText ( )
  if len ( III11I1 ) > 1 :
   O00Ooo = III11I1 . lower ( )
   O00Ooo = O00Ooo . replace ( ' ' , '%20' )
   if 26 - 26: OoooooooOO % ooO00oOoo % O0OOo . ooO00oOoo % iIIIiI11
  else : quit ( )
 else : O00Ooo = urllib . unquote_plus ( OOO0OOO00oo ) . lower ( ) ; III11I1 = urllib . unquote_plus ( OOO0OOO00oo )
 OOO0OOO00oo = base64 . b64decode ( b'aHR0cHM6Ly93YXRjaGVwaXNvZGVzZXJpZXMuYnlwYXNzZWQuZXUvaG9tZS9zZWFyY2g/cT0=' ) + O00Ooo
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '"series"(.+?)"series_id"' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( 'original_name":"(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oo0OOo = re . compile ( '"seo_name":"(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'https://watchepisodeseries.bypassed.eu/' + oo0OOo
  iIiiiI = 'https://watchepisodeseries.bypassed.eu/series_images/' + oo0OOo + '.jpg'
  I11i1I1I ( oOOo0 , OOO0OOO00oo , 68 , iIiiiI , o0OOO , '' )
  if 34 - 34: Ooooo0Oo00oO0 / i1IIi11111i
def Oo0O0Ooo0ooOO ( ) :
 if 91 - 91: i111IiI / i1IIi11111i % OOO0O
 OOO0OOO00oo = 'https://watchepisodeseries.bypassed.eu/home/popular-series'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<div title="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( '////' , '//' )
  iIiiiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  o0OOO = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I11i1I1I ( '[COLOR aqua]' + oOOo0 + '[/COLOR]' , OOO0OOO00oo , 68 , iIiiiI , o0OOO )
  if 18 - 18: II111iiii . OoooooooOO % i1IIi11111i % iIIIiI11
  if 9 - 9: Oooo0000 - O0OOo * OoooooooOO . O0OOo
def ii1Ii1IiIIi ( ) :
 if 83 - 83: i111IiI / oo
 try :
  II1Ii11Ii1i1I = open ( I1i1iiI1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1
   else : quit ( )
  if O00Ooo == II1Ii11Ii1i1I :
   ii1iIi1II ( )
  else :
   IiII . notification ( O0O , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , iIiiiI , 5000 )
   OOO00 ( )
 except IOError :
  IiII . ok ( O0O , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter The Password You Set' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1
   else : quit ( )
  with open ( I1i1iiI1 , "w" ) as o000oo :
   o000oo . write ( O00Ooo )
   IiII . notification ( O0O , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , iIiiiI , 5000 )
   OOO00 ( )
   if 2 - 2: O0OOo + i1IIi11111i - oo0ooO0oOOOOo . ooO00oOoo - oo0ooO0oOOOOo
   if 67 - 67: iIii1I11I1II1 - iII111ii
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - i111IiI
def ii1iIi1II ( ) :
 if 30 - 30: i1IIi11111i
 Ii111 = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 oO0 = '[COLOR aqua]Asian Special Porn[/COLOR]'
 I11i1I1I ( oO0 , Ii111 , 1 , iIiiiI , I1IiI , '' )
 OOO0OOO00oo = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<li class="">(.+?)</li>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oOOoo0Oo ) [ 0 ]
  i1iIii = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( oOOoo0Oo ) [ 0 ]
  oo0OOo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'https://www.eporner.com' + oo0OOo
  if not 'All' in oOOo0 :
   if not 'Homemade' in oOOo0 :
    I11i1I1I ( "[COLOR aqua]" + oOOo0 + "  " + "[COLOR yellow]" + i1iIii + "[/COLOR]" , OOO0OOO00oo , 36 , iIiiiI , I1IiI , '' )
    if 81 - 81: O0 % iIIIiI11
def IiIII1i1i ( url ) :
 if 41 - 41: O0OOo / iIIIiI11 * iIIIiI11 - oo0ooO0oOOOOo . Ooo . OoooooooOO
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  oOOo0 = re . compile ( 'title="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  oo0OOo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  iIiiiI = re . compile ( 'src="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  url = 'https://www.eporner.com' + oo0OOo
  I11i1I1I ( "[COLOR skyblue]" + oOOo0 + "[/COLOR]" , url , 37 , iIiiiI , I1IiI , '' )
  if 42 - 42: oo0ooO0oOOOOo % O0OOo / i11iIiiIii + oo0ooO0oOOOOo
 try :
  o0OOo0o0O0O = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( OooO0 ) [ 0 ]
  OoO = 'https://www.eporner.com' + o0OOo0o0O0O
  o0OO0o0oOOO0O = 'http://imgur.com/3eNoY0p'
  I11i1I1I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 36 , o0OO0o0oOOO0O , I1IiI , '' )
 except : pass
 if 84 - 84: Ooo . Oooo0000 . II111iiii . i111IiI / iIIIiI11 % oo
def OOO0oOoO0O ( url , iconimage ) :
 if 84 - 84: O0 * OoooooooOO - Ooooo0Oo00oO0 * Ooooo0Oo00oO0
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0oOOo = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( O0oOOo )
 for i1ii , OooO0 in I1I11i :
  i1ii = i1ii . replace ( ':' , '' )
  url = 'https://www.eporner.com' + OooO0
  ii11i1 ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + i1ii + "[/COLOR]" , url , 2 , iconimage , I1IiI , '' )
  if 65 - 65: i1IIi11111i / Oooo0000 % Ooooo0Oo00oO0
def iIiIIii ( url ) :
 IiII . ok ( "HERE" , str ( url ) )
 url = 'https://ww3.soul-anime.us/anime-list.html'
 IiII . ok ( "HERE" , str ( url ) )
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<ul id="genre">(.*?)</ul>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . compile ( '<a rel=.*?href="(.*?)">(.*?)</a>' ) . findall ( i1I1iI )
 for OooO0 , oOOo0 in I1I11i :
  I11i1I1I ( "[COLOR cyan]" + oOOo0 + "[/COLOR]" , OooO0 , 52 , iIiiiI , I1IiI , '' )
 I11I11i1I ( )
 if 61 - 61: I11i1i11i1I / oo0ooO0oOOOOo / O0OOo * O0
def iIII1i1i ( url ) :
 if 35 - 35: II111iiii * i111IiI - OoooooooOO . i111IiI . i111IiI
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="lt">(.*?)<div class="tags"' ) . findall ( OooO0 )
 for I1II in i1I1iI :
  oOOo0 = re . compile ( 'alt="(.*?)"' ) . findall ( I1II ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( I1II ) [ 0 ]
  iIiiiI = re . compile ( 'data-original="(.*?)"' ) . findall ( I1II ) [ 0 ]
  Ii1i1iI = re . compile ( '<p>(.*?)</p>' ) . findall ( I1II ) [ 0 ]
  OO0OOO0oOOo00O = re . compile ( '<span class=".*?">(.*?)</span>' ) . findall ( I1II ) [ 0 ]
  if 'Completed' in OO0OOO0oOOo00O :
   OO0OOO0oOOo00O = '[COLOR red]' + OO0OOO0oOOo00O + '[/COLOR]'
  else :
   OO0OOO0oOOo00O = '[COLOR lime]' + OO0OOO0oOOo00O + '[/COLOR]'
  I11i1I1I ( "[COLOR cyan]" + oOOo0 + " :: " + OO0OOO0oOOo00O + "[/COLOR]" , url , 53 , iIiiiI , I1IiI , Ii1i1iI )
 I11I11i1I ( )
 if 51 - 51: oo / iIii1I11I1II1 % OOO0O + I11i1i11i1I * oo0Oo00Oo0 + Ooo
def o0OoO00o0000O ( url ) :
 if 21 - 21: ooO00oOoo / oo0Oo00Oo0 % oo0Oo00Oo0 - I11i1i11i1I
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<div class="img_box">(.*?)</span>' ) . findall ( OooO0 )
 for I1II in i1I1iI :
  oOOo0 = re . compile ( '<div class="ep">(.*?)</div>' ) . findall ( I1II ) [ 0 ]
  url = re . compile ( '<a href="(.*?)"' ) . findall ( I1II ) [ 0 ]
  iIiiiI = re . compile ( 'data-original="(.*?)"' ) . findall ( I1II ) [ 0 ]
  ii11i1 ( "[COLOR cyan]" + oOOo0 + "[/COLOR]" , url , 54 , iIiiiI , I1IiI , '' )
 I11I11i1I ( )
 if 70 - 70: O0OOo . i1IIi11111i
def O00o00O ( url , iconimage ) :
 if 3 - 3: oo0ooO0oOOOOo
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . compile ( '<iframe name="stream".*?src="(.*?)"' ) . findall ( OooO0 ) [ 0 ]
 Ii1I = IIIii1II1II ( i1I1iI )
 try :
  O0oOOo = re . compile ( '<iframe.*?src="(.*?)"' ) . findall ( Ii1I ) [ 0 ]
  o0iI11I1II ( o0O , O0oOOo , iconimage )
 except IndexError :
  IiII . notification ( O0O , '[COLOR aqua]Sorry Source Link Is Down[/COLOR]' , iconimage , 5000 )
  if 20 - 20: II111iiii . iII111ii / II111iiii % i11iIiiIii % iII111ii
def I11Ii11iI1 ( url ) :
 if 39 - 39: ooO00oOoo * i11iIiiIii - OOO0O / Ooooo0Oo00oO0 % Ooo % i111IiI
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . findall ( '<div class="item">(.*?)</li>' , OooO0 )
 for iii1i in i1I1iI :
  oOOo0 = re . findall ( 'alt="(.*?)"' , iii1i ) [ 0 ]
  oo0OOo = re . findall ( '<a href="(.*?)"' , iii1i ) [ 0 ]
  OO00oo0o = re . findall ( '<img src="(.*?)"' , iii1i ) [ 0 ]
  Ii1i1iI = re . findall ( """</div>(.*?)'""" , iii1i ) [ 0 ]
  Ii1i1iI = OOooo ( Ii1i1iI )
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR] " , oo0OOo , 43 , OO00oo0o , I1IiI , Ii1i1iI )
  if 18 - 18: Oooo0000 + iIii1I11I1II1 - II111iiii - ooO00oOoo
 try :
  OoO = re . findall ( '<a class="pagecurrent".+?>(.*?)</a>' , OooO0 ) [ 0 ]
  OoO = int ( OoO )
  OoO = OoO + 1
  url = url . replace ( '.html' , '' )
  OoO = ( url + '/page-%s.html' % ( OoO ) )
  I11i1I1I ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoO , 42 , iIiiiI , I1IiI , description = 'Next Page' )
 except : pass
 if 71 - 71: OoooooooOO
def iIIIII1iiiiII ( url , iconimage ) :
 if 54 - 54: i1IIi
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii1I11 = re . findall ( '<p\s+class="server_servername">(.*?)<.+?href="(.*?)"' , OooO0 )
 for oOOo0 , url in ii1I11 :
  ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 82 , iconimage , I1IiI , '' )
  if 99 - 99: oo0ooO0oOOOOo
def II11i11II ( url , iconimage ) :
 if 29 - 29: O0OOo % Oooo0000 % Ooooo0Oo00oO0 . I11i1i11i1I / OoooooooOO * oo0Oo00Oo0
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O0oOOo = re . findall ( '<script type="text/javascript">document.write\(Base64.decode\("(.*?)"' , OooO0 ) [ 0 ]
 O0oOOo = base64 . b64decode ( O0oOOo )
 O0oOOo = re . findall ( 'src="(.*?)"' , O0oOOo ) [ 0 ]
 o0iI11I1II ( o0O , O0oOOo , iconimage )
 I11I11i1I ( )
 if 54 - 54: O0
def OOoO000O00oO ( ) :
 if 34 - 34: O0
 OOO0OOO00oo = 'https://www.livefootballol.me/acestream-channel-list-2018.html'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 I1I11i = re . compile ( '<tr>(.+?)</tr>' ) . findall ( OooO0 )
 for I1II in I1I11i :
  oOOo0 = re . compile ( '<strong>(.+?)</strong>' ) . findall ( I1II ) [ 0 ]
  if len ( oOOo0 ) == 1 or '&nbsp;' in oOOo0 :
   oOOo0 = re . compile ( '<strong>(.+?)</strong>' ) . findall ( I1II ) [ 1 ]
  if len ( oOOo0 ) > 40 :
   oOOo0 = re . compile ( '<a.+?>(.+?)</a>' ) . findall ( I1II ) [ 0 ]
  OOO0OOO00oo = re . compile ( '<td>(.+?)</td>' ) . findall ( I1II ) [ 2 ]
  OooOOOo0 = re . compile ( '<td>(.+?)</td>' ) . findall ( I1II ) [ 3 ]
  O0O0o0o0o = re . compile ( '<td>(.+?)</td>' ) . findall ( I1II ) [ 4 ]
  oOOo0 = oOOo0 . strip ( )
  OOO0OOO00oo = OOO0OOO00oo . strip ( )
  ii11i1 ( "[COLOR aqua]" + oOOo0 + ' :: [COLOR yellow]' + OooOOOo0 + '[COLOR aqua] :: [COLOR yellow]' + O0O0o0o0o + ' Kbps[/COLOR]' , OOO0OOO00oo , 2 , O00oO , I1IiI , '' )
  if 9 - 9: O0OOo + i1IIi11111i - iIii1I11I1II1 - iIIIiI11 + I11i1i11i1I
def o000O0OOoo ( ) :
 if 60 - 60: ooO00oOoo * Ooo % Oooo0000 + OOO0O
 OOO0OOO00oo = 'http://acestreamchannel.blogspot.co.uk/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 I1I11i = re . compile ( '<tr>(.+?)</tr>' ) . findall ( OooO0 )
 for oOOoo0Oo in I1I11i :
  try :
   oOOo0 = re . compile ( '<td>(.+?)</td>' ) . findall ( oOOoo0Oo ) [ 0 ]
   if len ( oOOo0 ) < 40 :
    OOO0OOO00oo = re . compile ( 'href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
    ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 2 , O00oO , I1IiI , '' )
  except : pass
  if 52 - 52: i1IIi
def o000 ( ) :
 if 94 - 94: I11i1i11i1I + O0 / i111IiI . ooO00oOoo + oo0ooO0oOOOOo . iIii1I11I1II1
 OOO0OOO00oo = 'https://acestreamid.com/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<li class="collection-item acestreamidID ">(.*?)</li>' ) . findall ( OooO0 )
 for I1II in i1I1iI :
  oOOo0 = re . compile ( 'title="(.*?)"' ) . findall ( I1II ) [ 0 ]
  if 'Broken' in oOOo0 :
   oOOo0 = re . compile ( '<span class="font-small grey-text truncate content">(.*?)</span>' ) . findall ( I1II ) [ 0 ] . strip ( )
  OooO0 = re . compile ( '<div class="content wrap">(.*?)</div>' ) . findall ( I1II ) [ 0 ]
  OooO0 = 'acestream://' + OooO0
  OO0OOO0oOOo00O = re . compile ( 'title="(.*?)"' ) . findall ( I1II ) [ 1 ]
  try :
   OOOoO = re . findall ( r'\d+' , OO0OOO0oOOo00O ) [ 0 ]
  except IndexError :
   OOOoO = 0
  ii11i1 ( "[COLOR aqua]" + oOOo0 + " [COLOR yellow]Down Reports :: " + str ( OOOoO ) + "[/COLOR]" , OooO0 , 2 , O00oO , I1IiI , '' )
  if 57 - 57: Oooo0000 / i1IIi . i1IIi
def oo00OOoOoO00 ( ) :
 OOO0OOO00oo = 'http://jkarakizi.com/updated-acestream-channels-for-2018/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . compile ( '<tr>(.*?)</tr>' ) . findall ( OooO0 )
 for I1II in i1I1iI :
  try :
   oOOo0 = re . compile ( '<td class=".+?">(.*?)</td>' ) . findall ( I1II ) [ 0 ]
   OooO0 = re . compile ( '<td class="tg-yw4l">(.*?)</td>' ) . findall ( I1II ) [ 1 ]
   OooO0 = 'acestream://' + OooO0
   ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OooO0 , 2 , O00oO , I1IiI , '' )
  except : pass
  if 15 - 15: Ooooo0Oo00oO0 / O0 . I11i1i11i1I . i11iIiiIii
def o0OO0O0Oo ( ) :
 if 78 - 78: i1IIi11111i / O0OOo - oo0ooO0oOOOOo - iII111ii * OOO0O
 OOO0OOO00oo = 'http://www.livefootballol.me/streaming/english-premier-league-2018/'
 OooO0 = IIIii1II1II ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<td>(.+?)</td>' ) . findall ( OooO0 )
 for oOOoo0Oo in i1I1iI :
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  i1Oo0oO00o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = 'http://www.livefootballol.me' + OOO0OOO00oo
  I11i1I1I ( "[COLOR aqua]" + i1Oo0oO00o + "[/COLOR]" , OOO0OOO00oo , 74 , O00oO , I1IiI , '' )
  if 17 - 17: OoooooooOO + oo0ooO0oOOOOo * i111IiI * i1IIi11111i
def iiIii1I ( url ) :
 if 47 - 47: oo0Oo00Oo0 . i111IiI / I11i1i11i1I
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<a href="(.+?)"' ) . findall ( OooO0 )
 OOoOO = 0
 for O000OOo00oo in i1I1iI :
  if 'acestream' in O000OOo00oo :
   if 'http' in O000OOo00oo :
    OOoOO += 1
    oOOo0 = '[COLOR aqua]Link :: ' + str ( OOoOO ) + '[/COLOR]'
    ii11i1 ( oOOo0 , O000OOo00oo , 75 , O00oO , I1IiI , '' )
 if OOoOO == 0 :
  ii11i1 ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , O00oO , I1IiI , '' )
  if 66 - 66: O0OOo - I11i1i11i1I * Ooooo0Oo00oO0 + i1IIi11111i + I11i1i11i1I - iIii1I11I1II1
def iiiI1ii11 ( url ) :
 if 49 - 49: OoooooooOO / i11iIiiIii * i11iIiiIii
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( OooO0 ) [ 0 ]
 o0iI11I1II ( o0O , url , O00oO )
 if 58 - 58: OOO0O
 if 4 - 4: II111iiii . oo0Oo00Oo0 / oo - i11iIiiIii
 if 72 - 72: O0 / oo0Oo00Oo0 + OoooooooOO * iII111ii
 if 61 - 61: OoooooooOO % II111iiii - ooO00oOoo % oo + i1IIi
def i1IIiIi1IiI ( url ) :
 if 14 - 14: Ooooo0Oo00oO0 % OOO0O % O0OOo - i11iIiiIii
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0OO000ooOo = 'https://yo-movies.com/'
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( 'class="ml-item">(.*?)</a>' , OooO0 )
 for iii1i in i1I1iI :
  oOOo0 = re . findall ( 'oldtitle="(.*?)"' , iii1i ) [ 0 ]
  Iii111II = re . findall ( '<a href="(.*?)"' , iii1i ) [ 0 ]
  if not o0OO000ooOo in Iii111II : Iii111II = o0OO000ooOo + Iii111II
  iIiiiI = re . findall ( '<img data-original="(.*?)"' , iii1i ) [ 0 ] . strip ( ) . replace ( 'w185' , 'original' )
  i1ii = re . findall ( '<span class="mli-quality">(.*?)</span>' , iii1i ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + ' | ' + '[COLOR yellow]' + i1ii + "[/COLOR]" , Iii111II , 81 , iIiiiI , iIiiiI , '' )
 try :
  oOo00OooO0oO = 6
  I1IIi = 'page'
  O0OOOo = url . split ( I1IIi , 1 ) [ - 1 ]
  i11I1I1iiI = O0OOOo . replace ( '/' , '' )
  O0OOOo = int ( i11I1I1iiI )
  if O0OOOo < oOo00OooO0oO :
   O0OOOo = O0OOOo + 1
   OoO = 'https://yo-movies.com/genre/bollywood/page/' + str ( O0OOOo ) + '/'
  I11i1I1I ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 80 , O00oO , o0OOO , 'Next Page' )
 except : pass
 if 34 - 34: i111IiI % oo0Oo00Oo0 . O0 . iIii1I11I1II1
def ooi1II1I ( url , iconimage ) :
 if 95 - 95: Oooo0000 - oo0ooO0oOOOOo / II111iiii % oo . I11i1i11i1I
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . findall ( '<div class="btn-group btn-group-justified embed-selector"\s+>(.*?)</div>' , OooO0 ) [ 0 ]
 ii = r'''<a\s+href=['"]([^'"]+)['"].+?Download'''
 O000OOo00oo = re . findall ( ii , i1I1iI )
 i1iIii = 0
 for oOOoo0Oo in O000OOo00oo :
  i1iIii += 1
  i1II1 = 'Link' + ' | ' + str ( i1iIii )
  ii11i1 ( "[COLOR aqua]" + i1II1 + "[/COLOR]" , oOOoo0Oo , 2 , iconimage , iconimage , '' )
  if 1 - 1: oo0Oo00Oo0
def oOO0oo ( url ) :
 if 29 - 29: ooO00oOoo * II111iiii * OoooooooOO - oo * II111iiii
 OooO0 = IIIii1II1II ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . findall ( 'class="item">(.*?)<div class="typepost">' , OooO0 , flags = re . DOTALL )
 for iii1i in i1I1iI :
  oOOo0 = re . findall ( '<span class="tt">(.*?)</span>' , iii1i , flags = re . DOTALL ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  url = re . findall ( '<a href="(.*?)">' , iii1i , flags = re . DOTALL ) [ 0 ]
  iIiiiI = re . findall ( '<img src="(.*?)"' , iii1i , flags = re . DOTALL ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 84 , iIiiiI , I1IiI , '' )
  if 41 - 41: O0
 try :
  ii = '''<a\s*href=['"]([^'"]+)['"]\s*>Next<'''
  OoO = re . findall ( ii , OooO0 ) [ 0 ]
  I11i1I1I ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 83 , O00oO , o0OOO , 'Next Page' )
 except : pass
 if 30 - 30: oo0Oo00Oo0 % iII111ii * oo0ooO0oOOOOo - oo * iIIIiI11 % oo0Oo00Oo0
def iiiiI11ii ( url , iconimage ) :
 if 96 - 96: iII111ii . O0 / iII111ii % O0
 OooO0 = IIIii1II1II ( url )
 o0o000 = re . findall ( '''<script>eid =\s+'(.*?)'.+?</script>''' , OooO0 ) [ 0 ]
 i1iiiIii11 = ( 'https://asap2bypass.streamcr.com/ajax/movie/get_sources/%s' % o0o000 )
 Ii1I = IIIii1II1II ( i1iiiIii11 )
 OOoOOO000O0 = '''"file":['"]([^'"]+)['"]\s*.+?"label":"(\d+)p"'''
 oOOoo0Oo = re . findall ( OOoOOO000O0 , Ii1I )
 for url , i1ii in oOOoo0Oo :
  url = url . replace ( '\\' , '' )
  ii11i1 ( "[COLOR aqua]Link Quality : " + i1ii + "[/COLOR]" , url , 2 , iconimage , I1IiI , '' )
  if 92 - 92: oo / O0
def oOO0o00O ( url , getphp ) :
 II = urllib2 . Request ( url )
 II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 II . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 ooOoOoo0O = urllib2 . urlopen ( II , timeout = 10 )
 OooO0 = ooOoOoo0O . read ( )
 ooOoOoo0O . close ( )
 return OooO0
 if 69 - 69: i1IIi
 if 59 - 59: II111iiii - I11i1i11i1I
 if 24 - 24: O0OOo - i1IIi + i111IiI
def IiiIi ( ) :
 if 10 - 10: Oooo0000 / O0OOo
 OOO0OOO00oo = 'http://www1.putlockers.gs/genres.html'
 OooO0 = IIIii1II1II ( OOO0OOO00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1I1iI = re . compile ( '<ul class="dropdown">(.+?)</ul>' ) . findall ( OooO0 ) [ 0 ]
 I1I11i = re . findall ( '<li>(.*?)</li>' , i1I1iI )
 for oOOoo0Oo in I1I11i :
  oOOo0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oOOoo0Oo ) [ 0 ]
  OOO0OOO00oo = re . compile ( '<a href="(.+?)"' ) . findall ( oOOoo0Oo ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 42 , iIiiiI , I1IiI )
  if 15 - 15: iII111ii . i1IIi11111i / iII111ii * i111IiI - ooO00oOoo % oo
def oo0OOOOOO0 ( url ) :
 if 26 - 26: iIii1I11I1II1
 OooO0 = IIIii1II1II ( url )
 I1I11i = re . findall ( '<div class="postHeader">(.*?)<div class="post">' , OooO0 )
 for iii1i in I1I11i :
  oOOo0 = re . findall ( 'title="(.*?)"' , iii1i ) [ 0 ] . replace ( 'Permalink to' , '' ) . strip ( )
  url = re . findall ( '<a href="(.*?)"' , iii1i ) [ 0 ]
  iIiiiI = re . findall ( 'src="(.*?)"' , iii1i ) [ 1 ]
  o0OOO = re . findall ( '<img class="aligncenter"\s+src="(.*?)"' , iii1i ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 86 , iIiiiI , o0OOO , '' )
  if 87 - 87: oo / OoooooooOO - O0OOo % i1IIi11111i % Ooooo0Oo00oO0 % O0OOo
 try :
  ii = '''<a\s*href=['"]([^'"]+)['"]\s*>Older'''
  OoO = re . findall ( ii , OooO0 ) [ 0 ]
  I11i1I1I ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 85 , O00oO , o0OOO , 'Next Page' )
 except : pass
 if 29 - 29: OoooooooOO . ooO00oOoo % oo - iII111ii
 if 8 - 8: i1IIi
def iIiI1 ( url , iconimage , fanart ) :
 if 37 - 37: Oooo0000 * i11iIiiIii / oo0ooO0oOOOOo % Ooo
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( '<strong>Download:</strong>(.*?)</div>' , OooO0 ) [ 0 ]
 ii = '''<a\s+href=['"]([^'"]+)['"]>([^'"]+)</a>'''
 oOOoo0Oo = re . findall ( ii , i1I1iI )
 ooo0 = [ 'uploadgig' , 'rapidgator' ]
 o0oooO = 0
 for url , oOOo0 in oOOoo0Oo :
  if any ( x in url . lower ( ) for x in ooo0 ) :
   o0oooO += 1
   if 'uploadgig' in url :
    oOOo0 = oOOo0 + '[COLOR yellow] (Not Great With RD)[/COLOR]'
   ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 2 , iconimage , I1IiI , '' )
 if o0oooO == 0 :
  ii11i1 ( "[COLOR yellow]No Links Found[/COLOR]" , url , 2 , iconimage , I1IiI , '' )
  if 89 - 89: II111iiii / OOO0O
def IIo0OoO00 ( url ) :
 if 18 - 18: OOO0O - I11i1i11i1I - ooO00oOoo - ooO00oOoo
 OooO0 = IIIii1II1II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( """<div\s+id='genre'\s+class="options\s+">(.*?)</div>""" , OooO0 ) [ 0 ]
 OOooo00 = re . findall ( '<a href="(.*?)">(.*?)</a>' , i1I1iI )
 for url , oOOo0 in OOooo00 :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 90 , iIiiiI , o0OOO , '' )
  if 35 - 35: Ooo . i1IIi11111i * i11iIiiIii
  if 44 - 44: i11iIiiIii / O0OOo
  if 42 - 42: OoooooooOO + O0OOo % II111iiii + Oooo0000
def I11i11I1iiII ( url ) :
 if 28 - 28: i11iIiiIii / I11i1i11i1I . iIii1I11I1II1 / II111iiii
 OooO0 = IIIii1II1II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 i1I1iI = re . findall ( '<div class="imagefilm">(.*?)</a>' , OooO0 )
 OoOO = 0
 for iii1i in i1I1iI :
  OoOO += 1
  oOOo0 = re . findall ( 'title="(.*?)"' , iii1i ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  url = re . findall ( '<a href="(.*?)"' , iii1i ) [ 0 ]
  iIiiiI = re . findall ( '<img src="(.*?)"' , iii1i ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 91 , iIiiiI , o0OOO , '' )
  if 32 - 32: i1IIi11111i * ooO00oOoo % oo0Oo00Oo0 * iIIIiI11 . O0
 if OoOO == 0 :
  ii11i1 ( "[COLOR yellow]No Content Found For This Catergory[/COLOR]" , url , 999 , O00oO , I1IiI , '' )
  if 48 - 48: iII111ii * iII111ii
 try :
  ii = '''<a href=['"]([^'"]+)['"]>Next'''
  OoO = re . findall ( ii , OooO0 ) [ 0 ]
  if not o0OO000ooOo in OoO : OoO = o0OO000ooOo + OoO
  I11i1I1I ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 90 , O00oO , o0OOO , 'Next Page' )
 except : pass
 if 13 - 13: iIIIiI11 / i111IiI + i1IIi11111i . I11i1i11i1I % oo0Oo00Oo0
def IiIi1 ( url ) :
 if 53 - 53: OoooooooOO - Ooooo0Oo00oO0
 OooO0 = IIIii1II1II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( """<div\s+id='genre'\s+class="options\s+">(.*?)</div>""" , OooO0 ) [ 0 ]
 OOooo00 = re . findall ( '<a href="(.*?)">(.*?)</a>' , i1I1iI )
 for url , oOOo0 in OOooo00 :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 94 , iIiiiI , o0OOO , '' )
  if 87 - 87: OOO0O . ooO00oOoo
  if 17 - 17: iIIIiI11 . i11iIiiIii
  if 5 - 5: oo + O0 + O0 . Ooo - oo0Oo00Oo0
def o00oo0000 ( url ) :
 if 44 - 44: O0OOo % iIii1I11I1II1
 OooO0 = IIIii1II1II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 i1I1iI = re . findall ( '<div class="imagefilm">(.*?)</a>' , OooO0 )
 OoOO = 0
 for iii1i in i1I1iI :
  OoOO += 1
  oOOo0 = re . findall ( 'title="(.*?)"' , iii1i ) [ 0 ]
  oOOo0 = O0oO0 ( oOOo0 )
  url = re . findall ( '<a href="(.*?)"' , iii1i ) [ 0 ]
  iIiiiI = re . findall ( '<img src="(.*?)"' , iii1i ) [ 0 ]
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 95 , iIiiiI , o0OOO , '' )
  if 90 - 90: II111iiii + OoooooooOO % OoooooooOO
 if OoOO == 0 :
  ii11i1 ( "[COLOR yellow]No Content Found For This Catergory[/COLOR]" , url , 999 , O00oO , I1IiI , '' )
  if 35 - 35: iII111ii / oo * OoooooooOO . II111iiii / O0OOo
 try :
  ii = '''<a href=['"]([^'"]+)['"]>Next'''
  OoO = re . findall ( ii , OooO0 ) [ 0 ]
  if not o0OO000ooOo in OoO : OoO = o0OO000ooOo + OoO
  I11i1I1I ( "[COLOR yellow]Next Page --->[/COLOR]" , OoO , 90 , O00oO , o0OOO , 'Next Page' )
 except : pass
 if 1 - 1: OoooooooOO + Ooooo0Oo00oO0 . i1IIi % i111IiI
def OOOOOo ( url ) :
 if 65 - 65: I11i1i11i1I
 OooO0 = IIIii1II1II ( url )
 o0OO000ooOo = 'http://watchanime.info'
 i1I1iI = re . findall ( '<div class="list-episodes"(.*?)</div>' , OooO0 ) [ 0 ]
 I1ii1II1iII = re . findall ( '<a href="(.*?)">(.*?)</a>' , i1I1iI )
 for url , oOOo0 in I1ii1II1iII :
  if not o0OO000ooOo in url : url = o0OO000ooOo + url
  I11i1I1I ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , url , 91 , iIiiiI , o0OOO , '' )
  if 8 - 8: i1IIi11111i / O0 * O0 % Ooo - O0OOo + i111IiI
def ooIi1IiIiIi1IiI ( url , iconimage ) :
 if 36 - 36: Ooooo0Oo00oO0 - OoooooooOO / Oooo0000
 OooO0 = IIIii1II1II ( url )
 ii = '''<option\s+value=['"]([^'"]+)['"]'''
 iIIi1iI1I1IIi = re . findall ( ii , OooO0 )
 O0OO0 = re . findall ( 'var\s+filmId\s+=\s+"(.*?)"' , OooO0 ) [ 0 ]
 for ooo0 in iIIi1iI1I1IIi :
  ooo0 = ooo0 . title ( )
  ii11i1 ( "[COLOR aqua]" + ooo0 + "[/COLOR]" , O0OO0 , 92 , iconimage , I1IiI , '' )
  if 99 - 99: oo0Oo00Oo0 - ooO00oOoo / Ooooo0Oo00oO0 / i11iIiiIii
def OOO0oiII ( name , url ) :
 if 24 - 24: O0OOo . i111IiI * iIIIiI11 % iII111ii / oo0ooO0oOOOOo
 name = name . replace ( '[COLOR aqua]' , '' ) . replace ( '[/COLOR]' , '' )
 name = name . lower ( )
 Oo0Ooo0O0 = ( 'http://watchanime.info/ajax-get-link-stream/?server=%s&filmId=%s' % ( name , url ) )
 OooO0 = IIIii1II1II ( Oo0Ooo0O0 )
 if 'streaming.php' in OooO0 :
  OooO0 = 'http:' + OooO0
 name = '[COLOR yellow]Nemesis Anime[/COLOR]'
 o0iI11I1II ( name , OooO0 , O00oO )
 if 42 - 42: i1IIi * OOO0O - iIIIiI11 . ooO00oOoo + I11i1i11i1I . iIii1I11I1II1
 if 51 - 51: i111IiI . O0OOo
def IiiIiiIi ( url ) :
 if 40 - 40: I11i1i11i1I
 OooO0 = IIIii1II1II ( url )
 oO0Oo = json . loads ( OooO0 )
 try :
  OoO = oO0Oo [ 'nextPageToken' ]
 except : pass
 I1I11i = oO0Oo [ 'items' ]
 for iii1i in I1I11i :
  try :
   oOOo0 = iii1i [ 'snippet' ] [ 'title' ]
   oOOo0 = oOO ( oOOo0 )
   o0oo0o0o0 = iii1i [ 'snippet' ] [ 'description' ]
   iIiiiI = iii1i [ 'snippet' ] [ 'thumbnails' ] [ 'default' ] [ 'url' ]
   iIiiiI = iIiiiI . replace ( 'default' , 'hqdefault' )
   oo0OOo = iii1i [ 'id' ] [ 'videoId' ]
   Iii111II = 'https://www.youtube.com/watch?v=' + oo0OOo
   ii11i1 ( "[COLOR aqua]" + oOOo0 + "[/COLOR]" , Iii111II , 2 , iIiiiI , iIiiiI , o0oo0o0o0 )
  except : pass
  if 43 - 43: oo / ooO00oOoo . oo0Oo00Oo0
 try :
  if '&pageToken=' in url :
   Ooo0oO0 = url . split ( "&pageToken=" , 1 ) [ 0 ]
   o0Oo0oOooOoOo = Ooo0oO0 + '&pageToken=' + OoO
   xbmc . log ( Ooo0oO0 )
   o0OO0o0oOOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'icon.png' ) )
   I11i1I1I ( "[COLOR yellow]Next Page --------->[/COLOR]" , o0Oo0oOooOoOo , 87 , o0OO0o0oOOO0O , o0OOO )
  else :
   Ooo0oO0 = url + '&pageToken=' + OoO
   o0OO0o0oOOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'icon.png' ) )
   I11i1I1I ( "[COLOR yellow]Next Page --------->[/COLOR]" , Ooo0oO0 , 87 , o0OO0o0oOOO0O , o0OOO )
 except : pass
 if 49 - 49: oo0ooO0oOOOOo . oo . i11iIiiIii - II111iiii / iIIIiI11
def ooOo0O0o0 ( ) :
 if 65 - 65: oo0Oo00Oo0 + O0
 OOO0OOO00oo = 'https://www.livefootballol.me/streaming/world-cup-2018/'
 o0OO000ooOo = 'https://www.livefootballol.me'
 OooO0 = IIIii1II1II ( OOO0OOO00oo )
 i1I1iI = re . findall ( '<tbody>(.*?)</tbody>' , OooO0 ) [ 0 ]
 IiII1iiI = re . findall ( '<a href="(.*?)">(.*?)</a>' , i1I1iI )
 for OOO0OOO00oo , oOOo0 in IiII1iiI :
  oOOo0 = oOOo0 . replace ( '-' , 'Vs' )
  if not o0OO000ooOo in OOO0OOO00oo : OOO0OOO00oo = o0OO000ooOo + OOO0OOO00oo
  iIiiiI = 'http://a2.espncdn.com/combiner/i?img=%2Fi%2Fleaguelogos%2Fsoccer%2F500%2F4.png'
  o0OOO = 'https://i.pinimg.com/originals/15/9d/1a/159d1aae7e7f272fad2aa430a5839631.jpg'
  I11i1I1I ( "[COLOR gold]" + oOOo0 + "[/COLOR]" , OOO0OOO00oo , 101 , iIiiiI , o0OOO , '' )
  if 34 - 34: ooO00oOoo . OOO0O + i1IIi
def OO000oOoo0O ( url ) :
 if 9 - 9: OOO0O * i1IIi - i1IIi
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( '<tbody>(.*?)</tbody>' , OooO0 ) [ 1 ]
 ii = '''<a\s+href=['"]([^'"]+)['"]>(.*?)<'''
 IiIiiI11i1Ii = re . findall ( ii , i1I1iI )
 for OooO0 , O00 in IiIiiI11i1Ii :
  I11i1I1I ( "[COLOR gold]" + O00 + "[/COLOR]" , OooO0 , 102 , iIiiiI , o0OOO , '' )
  if 32 - 32: iIii1I11I1II1 * Ooooo0Oo00oO0 / iIIIiI11 % Ooooo0Oo00oO0
def i111i1i ( url ) :
 if 19 - 19: II111iiii - i1IIi - oo0ooO0oOOOOo / oo0ooO0oOOOOo + i1IIi11111i
 OooO0 = IIIii1II1II ( url )
 i1I1iI = re . findall ( '<table class="uk-table"(.+?)</table>' , OooO0 ) [ 0 ]
 ii = '''<td>Bitrate<.+?<td>(.*?)<.+?</tr>.+?</tr>.+?<.+?</td><td>(.+?)<.+?href=['"]([^'"]+)['"]'''
 IiIiiI11i1Ii = re . findall ( ii , i1I1iI )
 for i1ii , OooOOOo0 , OooO0 in IiIiiI11i1Ii :
  ii11i1 ( "[COLOR gold]" + i1ii + ' | ' + OooOOOo0 + "[/COLOR]" , OooO0 , 2 , iIiiiI , o0OOO , '' )
  if 51 - 51: O0OOo % i1IIi11111i * OoooooooOO . i11iIiiIii
def oO000 ( url ) :
 if 7 - 7: Ooooo0Oo00oO0 * ooO00oOoo + i1IIi + i11iIiiIii + O0OOo % ooO00oOoo
 OooO0 = requests . get ( url )
 ii = '''<span><img src=.+?title=['"](.*?)['"].+?<a\s+href=['"](.*?)['"]'''
 OO00OO0o0 = re . findall ( ii , OooO0 . content , flags = re . DOTALL )
 for oOOo0 , Ii1I in OO00OO0o0 :
  if not 'http://ibrod.tv' in Ii1I :
   Ii1I = 'http://ibrod.tv/' + Ii1I
  ii11i1 ( oOOo0 , Ii1I , 104 , O00oO , o0OOO , description = '' )
  if 52 - 52: oo % OOO0O - i11iIiiIii
 try :
  i1III = '''<a\s*href=['"]([^'"]+)['"]>Next'''
  OoO = re . findall ( i1III , OooO0 . content ) [ 0 ]
  if not 'http://www.ibrod.tv/' in OoO :
   OoO = 'http://www.ibrod.tv/' + OoO
  I11i1I1I ( '[COLOR yellow]Next Page --->[/COLOR]' , OoO , 103 , O00oO , o0OOO , description = '' )
 except : pass
 if 6 - 6: iII111ii . i111IiI + iIIIiI11 . Ooo
def oOoO0o ( name , url , iconimage ) :
 if 46 - 46: Ooo % iIIIiI11
 OooO0 = requests . get ( url )
 ii = '''div class="player">.+?src=['"](.*?)['"]'''
 OO00OO0o0 = re . findall ( ii , OooO0 . content , flags = re . DOTALL ) [ 0 ]
 Ii1I = requests . get ( OO00OO0o0 )
 oOOoO0OO00OOo0 = '''file:\s+['"](.*?)['"]'''
 OO00OO0o0 = re . findall ( oOOoO0OO00OOo0 , Ii1I . content , flags = re . DOTALL ) [ 0 ]
 o0iI11I1II ( name , OO00OO0o0 , iconimage )
 if 18 - 18: ooO00oOoo + Oooo0000 % iIii1I11I1II1 - i1IIi . OOO0O
 if 26 - 26: I11i1i11i1I * Ooooo0Oo00oO0 . i1IIi
 if 59 - 59: O0 + i1IIi - I11i1i11i1I
 if 62 - 62: i11iIiiIii % oo0ooO0oOOOOo . Ooooo0Oo00oO0 . oo0ooO0oOOOOo
 if 84 - 84: i11iIiiIii * Oooo0000
def oOO ( input ) :
 if type ( input ) != unicode :
  input = input . decode ( 'utf-8' )
  return input
 else :
  return input
  if 18 - 18: oo0ooO0oOOOOo - iIIIiI11 - i1IIi11111i / Ooo - O0
def O0oO0 ( text ) :
 if 30 - 30: O0 + oo + II111iiii
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
 if 14 - 14: I11i1i11i1I / oo0ooO0oOOOOo - iIii1I11I1II1 - OOO0O % oo0Oo00Oo0
 return text
 if 49 - 49: oo0Oo00Oo0 * OOO0O / I11i1i11i1I / O0OOo * iIii1I11I1II1
def OOoO00ooO ( ) :
 if 12 - 12: oo0Oo00Oo0 % ooO00oOoo + OOO0O - i1IIi . iIIIiI11 / ooO00oOoo
 o0IiiiI111I = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 III1I11i1iIi = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 OO0oo0O0OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 OoOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 46 - 46: ooO00oOoo / iIIIiI11 . Ooo % i11iIiiIii + I11i1i11i1I + OoooooooOO
 O0o0000o = 0
 for ( iI111I11I1I1 , oOo00OoOoO , oo0ooooO ) in os . walk ( III1I11i1iIi ) :
  for file in oo0ooooO :
   iiIIi = os . path . join ( iI111I11I1I1 , file )
   O0o0000o += os . path . getsize ( iiIIi )
 OoO0O00 = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( O0o0000o / ( 1024 * 1024.0 ) )
 ii11i1 ( OoO0O00 , 'url2' , 999 , iIiiiI , o0OOO )
 if 36 - 36: i111IiI . II111iiii
 O0o0000o = 0
 for ( iI111I11I1I1 , oOo00OoOoO , oo0ooooO ) in os . walk ( o0IiiiI111I ) :
  for file in oo0ooooO :
   iiIIi = os . path . join ( iI111I11I1I1 , file )
   O0o0000o += os . path . getsize ( iiIIi )
 OoO0O00 = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( O0o0000o / ( 1024 * 1024.0 ) )
 ii11i1 ( OoO0O00 , 'url2' , 999 , iIiiiI , o0OOO )
 if 25 - 25: OOO0O
 O0o0000o = 0
 for ( iI111I11I1I1 , oOo00OoOoO , oo0ooooO ) in os . walk ( OO0oo0O0OOO0 ) :
  for file in oo0ooooO :
   iiIIi = os . path . join ( iI111I11I1I1 , file )
   O0o0000o += os . path . getsize ( iiIIi )
 OoO0O00 = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( O0o0000o / ( 1024 * 1024.0 ) )
 ii11i1 ( OoO0O00 , 'url2' , 999 , iIiiiI , o0OOO )
 if 34 - 34: i1IIi11111i . iIii1I11I1II1 % O0
 O0o0000o = 0
 for ( iI111I11I1I1 , oOo00OoOoO , oo0ooooO ) in os . walk ( OoOOo ) :
  for file in oo0ooooO :
   iiIIi = os . path . join ( iI111I11I1I1 , file )
   O0o0000o += os . path . getsize ( iiIIi )
 OoO0O00 = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( O0o0000o / ( 1024 * 1024.0 ) )
 ii11i1 ( OoO0O00 , 'url2' , 999 , iIiiiI , o0OOO )
 if 43 - 43: oo - iII111ii
 ii11i1 ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , iIiiiI , o0OOO )
 ii11i1 ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , iIiiiI , o0OOO )
 if 70 - 70: iII111ii / oo0ooO0oOOOOo % oo0Oo00Oo0 - iIIIiI11
def o0iI11I1II ( name , url , iconimage ) :
 if 47 - 47: iII111ii
 IiII . notification ( O0O , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , iIiiiI , 5000 )
 import resolveurl
 if 'acestream' in url :
  oo0OOo = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  IiI1i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  IiI1i . setPath ( url )
  xbmc . Player ( ) . play ( oo0OOo , IiI1i , False )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  IiI1i = xbmcgui . ListItem ( name , iconImage = iIiiiI , thumbnailImage = iIiiiI )
  IiI1i . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , IiI1i , False )
  time . sleep ( 2 )
  quit ( )
 else :
  OOoOooOoOOOoo = url
  IiI1i = xbmcgui . ListItem ( name , iconImage = iIiiiI , thumbnailImage = iIiiiI )
  IiI1i . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , IiI1i , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  IiII . notification ( O0O , '[COLOR red]Link Dead, Please try another[/COLOR]' , iIiiiI , 5000 )
  if 92 - 92: oo0ooO0oOOOOo + i1IIi11111i % i1IIi
def I1I1I11Ii ( name , url , iconimage ) :
 if 48 - 48: OoooooooOO + OOO0O % iIii1I11I1II1
 iIii1 , IiI1IIIII1I = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 iIii1 += urllib . unquote_plus ( IiI1IIIII1I )
 url = regex . resolve ( iIii1 )
 if 35 - 35: iIIIiI11 - iIIIiI11 + i1IIi - O0 - Ooo
 PLAYREGEX ( name , url , iconimage )
 if 58 - 58: i1IIi11111i - iII111ii - OoooooooOO
def IIiIiI ( url ) :
 IiII . notification ( O0O , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , iIiiiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 96 - 96: iIii1I11I1II1
def O0OoO000O0OO ( heading , text ) :
 if 82 - 82: i1IIi11111i + O0 - Ooooo0Oo00oO0 % OOO0O * i11iIiiIii
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 iIIi1iI1 = xbmcgui . Window ( id )
 I1Iii1I = 50
 while ( I1Iii1I > 0 ) :
  try :
   xbmc . sleep ( 10 )
   I1Iii1I -= 1
   iIIi1iI1 . getControl ( 1 ) . setLabel ( heading )
   iIIi1iI1 . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 13 - 13: I11i1i11i1I + O0
  if 71 - 71: Ooooo0Oo00oO0 + i1IIi * O0OOo % O0OOo / O0OOo
def IIIii1II1II ( url ) :
 try :
  II = urllib2 . Request ( url )
  II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  ooOoOoo0O = urllib2 . urlopen ( II , timeout = 5 )
  OooO0 = ooOoOoo0O . read ( )
  ooOoOoo0O . close ( )
  OooO0 = OooO0 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OooO0
 except : quit ( )
 if 55 - 55: OoooooooOO + Ooo + OoooooooOO * oo0Oo00Oo0
def oOOoo00O00o ( url ) :
 try :
  II = urllib2 . Request ( url )
  II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  ooOoOoo0O = urllib2 . urlopen ( II , timeout = 5 )
  OooO0 = ooOoOoo0O . read ( )
  ooOoOoo0O . close ( )
  OooO0 = OooO0 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OooO0
 except : quit ( )
 if 68 - 68: O0
def ii11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = iIiiiI
 if not "http" in fanart :
  fanart = I1IiI
 II1iIII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OoOOOOo = True
 IiI1i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 IiI1i . setProperty ( "fanart_Image" , fanart )
 IiI1i . setProperty ( "icon_Image" , iconimage )
 IiI1i . setInfo ( 'video' , { 'Plot' : description } )
 Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 Iii1ii1II11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 IiI1i . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + Oo + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + Iii1ii1II11i + ')' ) ] )
 if 61 - 61: i1IIi * Oooo0000 - O0OOo - oo0Oo00Oo0
 OoOOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1iIII , listitem = IiI1i , isFolder = False )
 return OoOOOOo
 if 57 - 57: i1IIi11111i . iIii1I11I1II1 % oo0Oo00Oo0 % iIIIiI11 * i1IIi11111i
def IiI1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = iIiiiI
 if not "http" in fanart :
  fanart = I1IiI
 II1iIII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OoOOOOo = True
 IiI1i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 IiI1i . setProperty ( "fanart_Image" , fanart )
 IiI1i . setProperty ( "icon_Image" , iconimage )
 IiI1i . setInfo ( 'video' , { 'Plot' : description } )
 Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 8 - 8: i1IIi11111i . oo0Oo00Oo0 % OOO0O . ooO00oOoo % ooO00oOoo . iIIIiI11
 IiI1i . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + Oo + ')' ) ] )
 if 47 - 47: i111IiI + oo0Oo00Oo0 + II111iiii % i11iIiiIii
 OoOOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1iIII , listitem = IiI1i , isFolder = False )
 return OoOOOOo
 if 93 - 93: oo % i1IIi11111i . O0 / iII111ii * OOO0O
def i1iii1ii ( name , url , iconimage ) :
 IiII = xbmcgui . Dialog ( )
 II1 = [ ]
 I11Iii1 = [ ]
 i1iIIi1II1iiI = [ ]
 OooO0 = IIIii1II1II ( url )
 O000OOo00oo = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OooO0 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O000OOo00oo ) [ 0 ]
 oOOoo0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( O000OOo00oo )
 if len ( oOOoo0Oo ) < 1 :
  oOOoo0Oo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( O000OOo00oo )
 iii1i = 1
 for III1Ii1i1I1 in oOOoo0Oo :
  O0O00OooO = III1Ii1i1I1
  if '(' in III1Ii1i1I1 :
   III1Ii1i1I1 = III1Ii1i1I1 . split ( '(' ) [ 0 ]
   I1IiI1iI11 = str ( O0O00OooO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   II1 . append ( III1Ii1i1I1 )
   I11Iii1 . append ( I1IiI1iI11 )
  else :
   II1 . append ( III1Ii1i1I1 )
   I11Iii1 . append ( '[COLOR aqua]Link ' + str ( iii1i ) + '[/COLOR]' )
  iii1i = iii1i + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 IiII = xbmcgui . Dialog ( )
 iIi = IiII . select ( name , I11Iii1 )
 if iIi < 0 :
  quit ( )
 else :
  url = II1 [ iIi ]
  print url
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) : OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : OOoOooOoOOOoo = liveresolver . resolve ( url )
  else : OOoOooOoOOOoo = url
  IiI1i = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  IiI1i . setPath ( OOoOooOoOOOoo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI1i )
  IiII . notification ( O0O , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , iIiiiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo )
  if 29 - 29: O0 . Ooo
def OO0o0oO0O000o ( name , url , iconimage ) :
 if 47 - 47: Ooo - Oooo0000 / iIIIiI11 * OoooooooOO / iIIIiI11 . O0OOo
 iiII1IiIi1iI1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 II1 = [ ]
 I11Iii1 = [ ]
 i1iIIi1II1iiI = [ ]
 oOiiI1Ii11II1I = [ ]
 OooO0 = IIIii1II1II ( url )
 O000OOo00oo = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OooO0 ) [ 0 ]
 oOOoo0Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( O000OOo00oo )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O000OOo00oo ) [ 0 ]
 iii1i = 1
 if 44 - 44: iIIIiI11 % i11iIiiIii - iII111ii * oo + O0OOo * oo0ooO0oOOOOo
 for III1Ii1i1I1 in oOOoo0Oo :
  O0O00OooO = III1Ii1i1I1
  if '(' in III1Ii1i1I1 :
   III1Ii1i1I1 = III1Ii1i1I1 . split ( '(' ) [ 0 ]
   I1IiI1iI11 = str ( O0O00OooO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   II1 . append ( III1Ii1i1I1 )
   I11Iii1 . append ( I1IiI1iI11 )
   oOiiI1Ii11II1I . append ( 'Stream ' + str ( iii1i ) )
  else :
   II1 . append ( III1Ii1i1I1 )
   I11Iii1 . append ( 'Link ' + str ( iii1i ) )
   if 41 - 41: O0 * oo0Oo00Oo0 - i1IIi11111i . iIIIiI11
  iii1i = iii1i + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 IiII = xbmcgui . Dialog ( )
 iIi = IiII . select ( name , I11Iii1 )
 if iIi < 0 :
  quit ( )
 else :
  O00O0oOO00O00 = I11Iii1 [ iIi ]
  i1 = "/"
  if not O00O0oOO00O00 . endswith ( i1 ) :
   Oo00 = O00O0oOO00O00 + "/"
  else :
   Oo00 = O00O0oOO00O00
  url = iiII1IiIi1iI1 + II1 [ iIi ] + "%26referer=" + Oo00
  print url
  if 65 - 65: O0OOo . OoooooooOO
  xbmc . Player ( ) . play ( url )
  if 70 - 70: O0OOo - OOO0O . iIii1I11I1II1 % i111IiI / i1IIi11111i - O0
def OOooo ( string ) :
 o0O0oo0o = ( c for c in string if 0 < ord ( c ) < 127 )
 if 12 - 12: i1IIi11111i % Ooooo0Oo00oO0 % oo . i11iIiiIii * iIii1I11I1II1
 return '' . join ( o0O0oo0o )
 if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
def I11i1I1I ( name , url , mode , iconimage , fanart , description = '' ) :
 if 5 - 5: i1IIi11111i % OoooooooOO
 if not "http" in iconimage :
  iconimage = iIiiiI
 if not "http" in fanart :
  fanart = I1IiI
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 II1iIII = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOOOOo = True
 IiI1i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 IiI1i . setProperty ( "fanart_Image" , fanart )
 IiI1i . setProperty ( "icon_Image" , iconimage )
 IiI1i . setInfo ( 'video' , { 'Plot' : description } )
 OoOOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1iIII , listitem = IiI1i , isFolder = True )
 return OoOOOOo
 if 60 - 60: i1IIi11111i . i1IIi % Oooo0000 % oo0Oo00Oo0 % oo0ooO0oOOOOo
def Ii111IIi ( name , url , iconimage ) :
 OoOOOOo = True
 IiI1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; IiI1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OoOOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = IiI1i )
 xbmc . Player ( ) . play ( url , IiI1i , False )
 if 15 - 15: oo % Ooo + i11iIiiIii
def I1iIiiiI1 ( ) :
 if 42 - 42: oo0ooO0oOOOOo % OOO0O / Oooo0000 - OOO0O * i11iIiiIii
 o0IiiiI111I = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 III1I11i1iIi = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 OO0oo0O0OOO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 19 - 19: OOO0O * ooO00oOoo % i11iIiiIii
 iii1i = [ ( o0IiiiI111I , 'Cache' ) , ( III1I11i1iIi , 'Thumbnails' ) , ( OO0oo0O0OOO0 , 'Packages' ) ]
 if 24 - 24: I11i1i11i1I
 iIi1Iii111I = xbmcgui . Dialog ( ) . yesno ( O0O , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if iIi1Iii111I :
  iI111iI . create ( O0O , '' , '' , '' )
  iI111iI . update ( 0 )
  for iIii1 in iii1i :
   if 18 - 18: OOO0O . Oooo0000 / iII111ii + i11iIiiIii % i111IiI
   iI111iI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % iIii1 [ 1 ] )
   time . sleep ( 1 )
   if 93 - 93: i1IIi11111i % iIii1I11I1II1
   for Ooo0o0oo0 , oOo00OoOoO , oo0ooooO in os . walk ( iIii1 [ 0 ] ) :
    for oOO0 in oo0ooooO :
     if ( oOO0 . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( Ooo0o0oo0 , oOO0 ) )
     except : pass
   iI111iI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % iIii1 [ 1 ] )
   time . sleep ( 3 )
  iI111iI . close ( )
  IiII . notification ( O0O , '[COLOR skyblue]Maintenance Completed[/COLOR]' , iIiiiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 15 - 15: O0OOo + i111IiI . oo0Oo00Oo0 - iIii1I11I1II1 / O0 % iIii1I11I1II1
def oO0O ( url , mode , name , iconimage , fanart ) :
 if 79 - 79: OoooooooOO - Ooooo0Oo00oO0 * Ooooo0Oo00oO0 . i1IIi11111i
 with open ( Oo , "a" ) as o000oo :
  o000oo . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  IiII . notification ( O0O , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , iIiiiI , 5000 )
  if 100 - 100: II111iiii * i111IiI % ooO00oOoo / oo
def OOo ( ) :
 if 99 - 99: i1IIi11111i
 with open ( Oo , "a" ) as o000oo :
  oO00OoOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'favs.xml' ) )
  OoOi111i = open ( oO00OoOo ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1I1iI = re . compile ( '<item>(.+?)</item>' ) . findall ( OoOi111i )
  ii11i1 ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  ii11i1 ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  if len ( i1I1iI ) < 1 :
   ii11i1 ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  for I1II in i1I1iI :
   oOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( I1II ) [ 0 ]
   OOO0OOO00oo = re . compile ( '<url>(.+?)</url>' ) . findall ( I1II ) [ 0 ]
   iIiiiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1II ) [ 0 ]
   o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1II ) [ 0 ]
   ii11i1 ( '[COLOR skyblue]' + oOOo0 + '[/COLOR]' , OOO0OOO00oo , 2 , iIiiiI , o0OOO )
   if 46 - 46: Oooo0000 * O0OOo % OOO0O + O0 * Ooooo0Oo00oO0
 ii11i1 ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , O00oO , I1IiI )
 if 34 - 34: Oooo0000
def I11i11i1 ( ) :
 if 68 - 68: O0OOo . O0OOo - oo / i111IiI . oo0Oo00Oo0 / i1IIi
 with open ( i1i1II , "a" ) as o000oo :
  oO00OoOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + IiII1IiiIiI1 , 'download.xml' ) )
  OoOi111i = open ( oO00OoOo ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1I1iI = re . compile ( '<item>(.+?)</item>' ) . findall ( OoOi111i )
  ii11i1 ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  ii11i1 ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  if len ( i1I1iI ) < 1 :
   ii11i1 ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , O00oO , I1IiI )
  for I1II in i1I1iI :
   oOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( I1II ) [ 0 ]
   OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( I1II ) [ 0 ]
   iIiiiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1II ) [ 0 ]
   o0OOO = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1II ) [ 0 ]
   ii11i1 ( '[COLOR skyblue]' + oOOo0 + '[/COLOR]' , OOO0OOO00oo , 2 , iIiiiI , o0OOO )
   if 12 - 12: oo * i1IIi * i111IiI
 ii11i1 ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , O00oO , I1IiI )
 if 23 - 23: oo0ooO0oOOOOo / O0 / ooO00oOoo
def I11 ( ) :
 if 54 - 54: iIIIiI11 - Ooo
 with open ( Oo , "w" ) as o000oo :
  o000oo . write ( '' )
  IiII . notification ( O0O , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , iIiiiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 81 - 81: Ooooo0Oo00oO0 . O0 + II111iiii * iIii1I11I1II1 * oo0ooO0oOOOOo / i1IIi11111i
def Oo0OoOOOo ( ) :
 shutil . rmtree ( Iii1ii1II11i )
 os . mkdir ( Iii1ii1II11i )
 with open ( i1i1II , "w" ) as o000oo :
  o000oo . write ( '' )
 IiII . notification ( O0O , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , iIiiiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 7 - 7: Ooo / Oooo0000 - OOO0O + oo / iII111ii % Oooo0000
 if 31 - 31: iIIIiI11
 if 18 - 18: oo0Oo00Oo0 + iIIIiI11
 if 5 - 5: OoooooooOO + i111IiI * II111iiii
 if 98 - 98: oo0ooO0oOOOOo % i1IIi . ooO00oOoo . II111iiii . oo / i11iIiiIii
 if 32 - 32: I11i1i11i1I + ooO00oOoo . Ooo
 if 41 - 41: i1IIi11111i . i11iIiiIii / i111IiI
 if 98 - 98: i1IIi11111i % II111iiii
 if 95 - 95: iIii1I11I1II1 - Ooo - oo0ooO0oOOOOo + Ooo % oo . ooO00oOoo
 if 41 - 41: O0 + OOO0O . i1IIi - II111iiii * I11i1i11i1I . Oooo0000
 if 68 - 68: I11i1i11i1I
 if 20 - 20: Ooo - Ooo
 if 37 - 37: Ooooo0Oo00oO0
 if 37 - 37: O0OOo / Ooooo0Oo00oO0 * O0
 if 73 - 73: iII111ii * iII111ii / oo0Oo00Oo0
 if 43 - 43: oo . i1IIi . Ooooo0Oo00oO0 + O0 * iIIIiI11 * O0
 if 41 - 41: oo + iIIIiI11 % OoooooooOO . oo + iII111ii . iII111ii
 if 31 - 31: i11iIiiIii + II111iiii . iII111ii * i1IIi11111i
 if 66 - 66: i1IIi11111i + i1IIi % II111iiii . O0 * oo % oo
 if 87 - 87: oo0ooO0oOOOOo + I11i1i11i1I . iII111ii - OoooooooOO
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
 if 28 - 28: O0OOo * I11i1i11i1I / Ooo
def iIii11I ( ) :
 if 52 - 52: O0 / I11i1i11i1I % iII111ii * ooO00oOoo % oo0ooO0oOOOOo
 if 69 - 69: oo
 oOOO0ooo = I11i . getSetting ( 'PIN' )
 if oOOO0ooo == 'EXPIRED' :
  IiII . ok ( O0O , '[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin, then click ok and enter it[/COLOR]' )
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1 . title ( )
    I11i . setSetting ( id = 'PIN' , value = O00Ooo )
    iIii11I ( )
   else : quit ( )
  else :
   quit ( )
 if not 'EXPIRED' in oOOO0ooo :
  I1III1iIi = I11i . getSetting ( 'PIN' )
  OoO00O0 = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % I1III1iIi )
  OooO0 = IIIii1II1II ( OoO00O0 )
  if len ( OooO0 ) < 1 or 'Pin Expired' in OooO0 :
   I11i . setSetting ( id = 'PIN' , value = 'EXPIRED' )
   iIii11I ( )
  else :
   global baseurl
   baseurl = OooO0
   if 35 - 35: iII111ii . Ooooo0Oo00oO0 / i1IIi . iIii1I11I1II1 . O0
def O0o0O ( url , iconimage , fanart ) :
 if 6 - 6: II111iiii
 try :
  III11I1 = ''
  IIi1IIIi = xbmc . Keyboard ( III11I1 , 'Enter Name To Save File As' )
  IIi1IIIi . doModal ( )
  if IIi1IIIi . isConfirmed ( ) :
   III11I1 = IIi1IIIi . getText ( )
   if len ( III11I1 ) > 1 :
    O00Ooo = III11I1 . title ( )
   else : quit ( )
  import resolveurl
  if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
   OOoOooOoOOOoo = resolveurl . HostedMediaFile ( url ) . resolve ( )
   url = OOoOooOoOOOoo
  I11i1iIi111 = url . split ( '/' ) [ - 1 ]
  II1iIII = urllib2 . urlopen ( url )
  i1iIiIii = os . path . join ( Iii1ii1II11i , O00Ooo )
  oOO0 = open ( i1iIiIii , 'wb' )
  if 20 - 20: I11i1i11i1I * oo0Oo00Oo0
  i1III1iI = II1iIII . info ( )
  ii1ii1IiiiiIi1I = int ( i1III1iI . getheaders ( "Content-Length" ) [ 0 ] )
  iI111iI . create ( O0O , "Starting Download: %s File Size: %s" % ( O00Ooo , ii1ii1IiiiiIi1I ) )
  iI111iI . update ( 0 )
  time . sleep ( 2 )
  if 56 - 56: OoooooooOO * O0
  oo0OoOOooO = 0
  o0o0OO0o00o0O = 8192
  while True :
   buffer = II1iIII . read ( o0o0OO0o00o0O )
   if not buffer :
    break
    if 28 - 28: Oooo0000 - OOO0O + i1IIi11111i + iIIIiI11 / iIii1I11I1II1
   oo0OoOOooO += len ( buffer )
   oOO0 . write ( buffer )
   OO0OOO0oOOo00O = "[%3.2f%%]" % ( oo0OoOOooO * 100. / ii1ii1IiiiiIi1I )
   OO0OOO0oOOo00O = OO0OOO0oOOo00O + chr ( 8 ) * ( len ( OO0OOO0oOOo00O ) + 1 )
   iI111iI . update ( oo0OoOOooO , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( OO0OOO0oOOo00O , O00Ooo ) )
   if 26 - 26: iIii1I11I1II1 - O0 . O0
   if iI111iI . iscanceled ( ) :
    iI111iI . close ( )
    quit ( )
  with open ( i1i1II , "a" ) as o000oo :
   o000oo . write ( '<item>\n<title>' + O00Ooo + '</title>\n<link>' + i1iIiIii + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  IiII . notification ( O0O , '[COLOR skyblue]Download Complete[/COLOR]' , iIiiiI , 5000 )
  if 68 - 68: oo0ooO0oOOOOo + OOO0O . O0 . iIIIiI11 % i1IIi % oo0ooO0oOOOOo
  oOO0 . close ( )
 except :
  IiII . notification ( O0O , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , iIiiiI , 5000 )
  if 50 - 50: Ooooo0Oo00oO0 + I11i1i11i1I
  if 96 - 96: Oooo0000
  if 92 - 92: O0OOo / i11iIiiIii + oo
  if 87 - 87: i1IIi11111i % iIii1I11I1II1
def o0OO0OOO0O ( ) :
 Iii1I = [ ]
 oOoOOOOoOO0o = sys . argv [ 2 ]
 if len ( oOoOOOOoOO0o ) >= 2 :
  iiI1i1I1II = sys . argv [ 2 ]
  O0OOOOOO0 = iiI1i1I1II . replace ( '?' , '' )
  if ( iiI1i1I1II [ len ( iiI1i1I1II ) - 1 ] == '/' ) :
   iiI1i1I1II = iiI1i1I1II [ 0 : len ( iiI1i1I1II ) - 2 ]
  Ooo0Oo0o = O0OOOOOO0 . split ( '&' )
  Iii1I = { }
  for iii1i in range ( len ( Ooo0Oo0o ) ) :
   oo0Oo0 = { }
   oo0Oo0 = Ooo0Oo0o [ iii1i ] . split ( '=' )
   if ( len ( oo0Oo0 ) ) == 2 :
    Iii1I [ oo0Oo0 [ 0 ] ] = oo0Oo0 [ 1 ]
 return Iii1I
 if 66 - 66: Oooo0000 % I11i1i11i1I
iiI1i1I1II = o0OO0OOO0O ( ) ; OOO0OOO00oo = None ; o0O = None ; iI1ii11Ii = None ; O0OO0OO = None ; O00oO = None ; o0oo0o0o0 = None
try : O0OO0OO = urllib . unquote_plus ( iiI1i1I1II [ "site" ] )
except : pass
try : OOO0OOO00oo = urllib . unquote_plus ( iiI1i1I1II [ "url" ] )
except : pass
try : o0O = urllib . unquote_plus ( iiI1i1I1II [ "name" ] )
except : pass
try : iI1ii11Ii = int ( iiI1i1I1II [ "mode" ] )
except : pass
try : O00oO = urllib . unquote_plus ( iiI1i1I1II [ "iconimage" ] )
except : pass
try : o0OOO = urllib . unquote_plus ( iiI1i1I1II [ "fanart" ] )
except : pass
try : o0oo0o0o0 = urllib . unquote_plus ( iiI1i1I1II [ "description" ] )
except : pass
if 63 - 63: iIii1I11I1II1 + oo0ooO0oOOOOo . Oooo0000 / ooO00oOoo
if iI1ii11Ii == None or OOO0OOO00oo == None or len ( OOO0OOO00oo ) < 1 : OOO00 ( )
if 84 - 84: i1IIi
if 42 - 42: II111iiii - Oooo0000 - OoooooooOO . iII111ii / i1IIi11111i
if 56 - 56: i11iIiiIii - iIii1I11I1II1 . II111iiii
if 81 - 81: Ooooo0Oo00oO0 / i1IIi11111i * Ooooo0Oo00oO0 . O0
if 61 - 61: Oooo0000 * oo0ooO0oOOOOo + Ooo . iIii1I11I1II1 % i111IiI . Ooo
elif iI1ii11Ii == 1 : OOO0o ( o0O , OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 2 : o0iI11I1II ( o0O , OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 3 : i1iii1ii ( o0O , OOO0OOO00oo , O00oO )
if 53 - 53: Ooo * Ooooo0Oo00oO0 / iIii1I11I1II1 / ooO00oOoo % oo
if 39 - 39: Oooo0000 / OoooooooOO . Oooo0000 * oo / i1IIi11111i
if 38 - 38: Oooo0000 / oo0Oo00Oo0 % Ooo * i111IiI + i11iIiiIii % oo0Oo00Oo0
elif iI1ii11Ii == 4 : O0oOO0O ( OOO0OOO00oo )
elif iI1ii11Ii == 5 : OOoO ( OOO0OOO00oo )
elif iI1ii11Ii == 6 : IiIiI1111I1I ( )
elif iI1ii11Ii == 7 : oooooo0O000o ( OOO0OOO00oo )
elif iI1ii11Ii == 8 : IiiiIIiIi1 ( OOO0OOO00oo )
elif iI1ii11Ii == 9 : oooOo0OOOoo0 ( OOO0OOO00oo )
elif iI1ii11Ii == 10 : IIiIiI ( OOO0OOO00oo )
elif iI1ii11Ii == 11 : O0Oo0oOOoooOOOOo ( )
elif iI1ii11Ii == 12 : oO00O000oO0 ( OOO0OOO00oo )
elif iI1ii11Ii == 13 : iIIii ( OOO0OOO00oo )
elif iI1ii11Ii == 14 : oo0oO ( OOO0OOO00oo )
elif iI1ii11Ii == 15 : ooO0O00Oo0o ( )
elif iI1ii11Ii == 16 : OO0o0oO0O000o ( o0O , OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 17 : OOOOo ( OOO0OOO00oo )
elif iI1ii11Ii == 18 : i1I1iI1iIi111i ( OOO0OOO00oo )
elif iI1ii11Ii == 19 : iiIIiiIi1Ii11 ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 20 : I1i ( )
elif iI1ii11Ii == 21 : iI11iI1IiiIiI ( OOO0OOO00oo )
elif iI1ii11Ii == 22 : II1i111Ii1i ( OOO0OOO00oo )
elif iI1ii11Ii == 23 : I1ii1iIiii1I ( )
elif iI1ii11Ii == 24 : OoOiiI1IIIi ( OOO0OOO00oo )
elif iI1ii11Ii == 25 : i11II1I11I1 ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 26 : OOOooo ( OOO0OOO00oo )
elif iI1ii11Ii == 27 : o000ooooO0o ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 28 : OOOO0O00o ( )
elif iI1ii11Ii == 29 : I111i1i1111 ( OOO0OOO00oo )
elif iI1ii11Ii == 30 : ooo0OOO ( OOO0OOO00oo )
elif iI1ii11Ii == 31 : o0o0oOoOO0O ( OOO0OOO00oo )
elif iI1ii11Ii == 32 : I111i1II ( OOO0OOO00oo )
elif iI1ii11Ii == 33 : IIiI1Ii ( OOO0OOO00oo )
elif iI1ii11Ii == 34 : iI1 ( OOO0OOO00oo )
elif iI1ii11Ii == 35 : ii1iIi1II ( )
elif iI1ii11Ii == 36 : IiIII1i1i ( OOO0OOO00oo )
elif iI1ii11Ii == 37 : OOO0oOoO0O ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 38 : ii1Ii1IiIIi ( )
elif iI1ii11Ii == 39 : III1I1Iii1iiI ( OOO0OOO00oo )
elif iI1ii11Ii == 40 : I1i ( )
elif iI1ii11Ii == 41 : iI11iI1IiiIiI ( OOO0OOO00oo )
elif iI1ii11Ii == 42 : I11Ii11iI1 ( OOO0OOO00oo )
elif iI1ii11Ii == 43 : iIIIII1iiiiII ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 44 : IiiIi ( )
if 61 - 61: Ooo - iIIIiI11 % oo / oo0Oo00Oo0 / iII111ii + iIii1I11I1II1
elif iI1ii11Ii == 45 : II11iI111i1 ( )
elif iI1ii11Ii == 46 : OoO00 ( OOO0OOO00oo )
elif iI1ii11Ii == 47 : o00O00oO00 ( o0O , OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 48 : ooo0O ( )
elif iI1ii11Ii == 49 : oO0oO0 ( OOO0OOO00oo )
elif iI1ii11Ii == 50 : IIi1ii1Ii ( OOO0OOO00oo )
elif iI1ii11Ii == 51 : iIiIIii ( OOO0OOO00oo )
elif iI1ii11Ii == 52 : iIII1i1i ( OOO0OOO00oo )
elif iI1ii11Ii == 53 : o0OoO00o0000O ( OOO0OOO00oo )
elif iI1ii11Ii == 54 : O00o00O ( OOO0OOO00oo , O00oO )
if 87 - 87: Ooo + oo0Oo00Oo0 + O0 / i1IIi % Ooooo0Oo00oO0 / Ooo
if 64 - 64: Oooo0000 % Ooooo0Oo00oO0 . Ooo % Oooo0000 + i111IiI * Ooooo0Oo00oO0
if 83 - 83: I11i1i11i1I % OOO0O + i111IiI % i11iIiiIii + O0
elif iI1ii11Ii == 59 : o0o0O00oo0 ( )
elif iI1ii11Ii == 60 : ooOOo00O00Oo ( OOO0OOO00oo )
elif iI1ii11Ii == 61 : OoOoOo00o0 ( o0O , OOO0OOO00oo , O00oO )
if 65 - 65: iIii1I11I1II1 % OOO0O + O0 / OoooooooOO
elif iI1ii11Ii == 66 : o0iiiI1I1iIIIi1 ( )
elif iI1ii11Ii == 67 : oO0OO0 ( OOO0OOO00oo )
elif iI1ii11Ii == 68 : oO0o00oOOooO0 ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 69 : i11I1iIi ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 70 : Oo000 ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 71 : ooO000O000 ( )
elif iI1ii11Ii == 72 : Oo0O0Ooo0ooOO ( )
elif iI1ii11Ii == 73 : o0OO0O0Oo ( )
elif iI1ii11Ii == 74 : iiIii1I ( OOO0OOO00oo )
elif iI1ii11Ii == 75 : iiiI1ii11 ( OOO0OOO00oo )
elif iI1ii11Ii == 76 : OOoO000O00oO ( )
elif iI1ii11Ii == 77 : o000O0OOoo ( )
elif iI1ii11Ii == 78 : o000 ( )
elif iI1ii11Ii == 79 : oo00OOoOoO00 ( )
elif iI1ii11Ii == 80 : i1IIiIi1IiI ( OOO0OOO00oo )
elif iI1ii11Ii == 81 : ooi1II1I ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 82 : II11i11II ( OOO0OOO00oo , O00oO )
if 52 - 52: iIIIiI11 % oo0ooO0oOOOOo * ooO00oOoo % i111IiI + oo0ooO0oOOOOo / iII111ii
elif iI1ii11Ii == 83 : oOO0oo ( OOO0OOO00oo )
elif iI1ii11Ii == 84 : iiiiI11ii ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 85 : oo0OOOOOO0 ( OOO0OOO00oo )
elif iI1ii11Ii == 86 : iIiI1 ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 87 : IiiIiiIi ( OOO0OOO00oo )
elif iI1ii11Ii == 88 : IIo0OoO00 ( OOO0OOO00oo )
if 80 - 80: OoooooooOO + Ooooo0Oo00oO0
elif iI1ii11Ii == 90 : I11i11I1iiII ( OOO0OOO00oo )
elif iI1ii11Ii == 91 : ooIi1IiIiIi1IiI ( OOO0OOO00oo , O00oO )
elif iI1ii11Ii == 92 : OOO0oiII ( o0O , OOO0OOO00oo )
elif iI1ii11Ii == 93 : IiIi1 ( OOO0OOO00oo )
elif iI1ii11Ii == 94 : o00oo0000 ( OOO0OOO00oo )
elif iI1ii11Ii == 95 : OOOOOo ( OOO0OOO00oo )
if 95 - 95: Ooo / OOO0O * Ooo - OoooooooOO * OoooooooOO % Oooo0000
elif iI1ii11Ii == 100 : ooOo0O0o0 ( )
elif iI1ii11Ii == 101 : OO000oOoo0O ( OOO0OOO00oo )
elif iI1ii11Ii == 102 : i111i1i ( OOO0OOO00oo )
if 43 - 43: O0OOo . Ooo
elif iI1ii11Ii == 103 : oO000 ( OOO0OOO00oo )
elif iI1ii11Ii == 104 : oOoO0o ( o0O , OOO0OOO00oo , O00oO )
if 12 - 12: Ooo + oo0ooO0oOOOOo + i111IiI . Ooooo0Oo00oO0 / iIIIiI11
if 29 - 29: Ooooo0Oo00oO0 . oo0Oo00Oo0 - II111iiii
if 68 - 68: iIii1I11I1II1 + II111iiii / OOO0O
if 91 - 91: i1IIi11111i % iIii1I11I1II1 . ooO00oOoo
if 70 - 70: i111IiI % II111iiii % O0 . i1IIi / Ooo
elif iI1ii11Ii == 884 : OOoO00ooO ( )
elif iI1ii11Ii == 885 : Oo0OoOOOo ( )
elif iI1ii11Ii == 886 : I11i11i1 ( )
elif iI1ii11Ii == 887 : O0o0O ( OOO0OOO00oo , O00oO , o0OOO )
elif iI1ii11Ii == 888 : i1iI ( )
elif iI1ii11Ii == 889 : oO0O ( OOO0OOO00oo , iI1ii11Ii , o0O , O00oO , o0OOO )
elif iI1ii11Ii == 890 : OOo ( )
elif iI1ii11Ii == 891 : I11 ( )
elif iI1ii11Ii == 892 : I1iIiiiI1 ( )
if 100 - 100: oo * i11iIiiIii % OOO0O / O0OOo / oo0Oo00Oo0 + oo
iIii11I ( )
if iI1ii11Ii == None or OOO0OOO00oo == None or len ( OOO0OOO00oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 59 - 59: Ooo - Ooooo0Oo00oO0
if 14 - 14: iIii1I11I1II1 - iIii1I11I1II1
if 5 - 5: Ooooo0Oo00oO0
if 84 - 84: II111iiii * OOO0O * II111iiii % Ooooo0Oo00oO0 / ooO00oOoo
if 100 - 100: Ooooo0Oo00oO0 . iIIIiI11 - iIii1I11I1II1 . i11iIiiIii / II111iiii
if 71 - 71: Ooo * O0OOo . i111IiI
if 49 - 49: Ooooo0Oo00oO0 * O0 . Ooooo0Oo00oO0
if 19 - 19: II111iiii - Ooooo0Oo00oO0
if 59 - 59: I11i1i11i1I * Oooo0000 - iIIIiI11 . oo0ooO0oOOOOo
if 89 - 89: oo0ooO0oOOOOo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
