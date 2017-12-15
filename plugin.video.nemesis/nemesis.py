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
 o00O00O0O0O = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OooO0OO = re . compile ( '<downloadcounter>(.+?)</downloadcounter>' ) . findall ( o00O00O0O0O ) [ 0 ]
 if OooO0OO == '0' :
  iiiIi = urllib2 . Request ( 'http://streamarmy.co.uk/dapi.php' )
  iiiIi . add_header ( 'User-Agent' , 'StreamArmy' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 30 )
  OoO000 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  if 42 - 42: OOo0o0 - i1IIi / i11iIiiIii + OOoOoo00oo + i1
  with open ( iI1Ii11111iIi , "w" ) as iIi :
   iIi . write ( '<downloadcounter>1</downloadcounter>\n' )
  return OoO000 ;
 else :
  pass
  if 40 - 40: OOo0o0 . Oooo0000 . ooo0Oo0 . i1IIi
def I11iii ( ) :
 if 54 - 54: OOoOoo00oo + OOoOoo00oo % oOo0 % i11iIiiIii / iIii1I11I1II1 . OOoOoo00oo
 if 57 - 57: OOooO % OoooooooOO
 if not os . path . exists ( os . path . dirname ( o0OOO ) ) :
  try :
   os . makedirs ( os . path . dirname ( o0OOO ) )
   with open ( iI1Ii11111iIi , "w" ) as O00 :
    O00 . write ( "<date>000</date>" )
  except OSError as i11I1 :
   if i11I1 . errno != errno . EEXIST :
    raise
    if 8 - 8: iIii1I11I1II1 - I1iiiiI1iII % iIii1I11I1II1 - OOooO * iiI1iIiI
def iI11i1I1 ( ) :
 if 71 - 71: i1Ii % OOoO00o / i1IIi11111i
 ii11i1iIII = xbmc . getInfoLabel ( "System.BuildVersion" )
 Ii1I = float ( ii11i1iIII [ : 4 ] )
 if Ii1I >= 11.0 and Ii1I <= 11.9 :
  Oo0o0 = 'Eden'
 elif Ii1I >= 12.0 and Ii1I <= 12.9 :
  Oo0o0 = 'Frodo'
 elif Ii1I >= 13.0 and Ii1I <= 13.9 :
  Oo0o0 = 'Gotham'
 elif Ii1I >= 14.0 and Ii1I <= 14.9 :
  Oo0o0 = 'Helix'
 elif Ii1I >= 15.0 and Ii1I <= 15.9 :
  Oo0o0 = 'Isengard'
 elif Ii1I >= 16.0 and Ii1I <= 16.9 :
  Oo0o0 = 'Jarvis'
 elif Ii1I >= 17.0 and Ii1I <= 17.9 :
  Oo0o0 = 'Krypton'
 else : Oo0o0 = "Decline"
 if 49 - 49: OOo0o0 % OOooO + i1IIi . iiI1iIiI % o000o0o00o0Oo
 if Oo0o0 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif Oo0o0 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 48 - 48: iI1 + iI1 / i11Ii11I1Ii1i / iIii1I11I1II1
def i1iiI11I ( ) :
 if 29 - 29: OoooooooOO
 I11iii ( )
 iI ( )
 I1i1I1II = i1iII1IiiIiI1
 i1IiIiiI = I1i1I1II
 try :
  iiiIi = urllib2 . Request ( 'http://streamarmy.co.uk/dapi.php' )
  iiiIi . add_header ( 'User-Agent' , 'StreamArmy' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 3 )
  OoO000 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  I1I ( '[COLOR yellow]' + OoO000 + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
 except : pass
 oOO00oOO = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if 75 - 75: i1IIi / OoooooooOO - O0 / Oooo0000 . i11Ii11I1Ii1i - i1IIi
 if 71 - 71: OOoOoo00oo + OOooO * OOoOoo00oo - i1 * i1IIi11111i
 if 65 - 65: O0 % iiI1iIiI . o000o0o00o0Oo % iIii1I11I1II1 / OOoOoo00oo % oOo0
 if 51 - 51: i11iIiiIii . iiI1iIiI + i11Ii11I1Ii1i
 if 10 - 10: o000o0o00o0Oo * i1Ii * i11Ii11I1Ii1i % OOooO . OOoOoo00oo + oOo0
 if 19 - 19: Oooo0000 - iiI1iIiI . OOoOoo00oo / I1iiiiI1iII
 if 33 - 33: oOo0 / o000o0o00o0Oo % iiI1iIiI + i1Ii / i1
 if 52 - 52: i1IIi11111i - OoooooooOO + OOooO + OOooO - i1IIi11111i / oOo0
 if ( oOO00oOO >= 0000 ) and ( oOO00oOO <= 1159 ) : I1IiIi11Ii1 = "Morning"
 elif ( oOO00oOO >= 1200 ) and ( oOO00oOO <= 1759 ) : I1IiIi11Ii1 = "Afternoon"
 else : I1IiIi11Ii1 = "Evening"
 I1I ( '[COLOR yellow]Good[COLOR aqua] ' + str ( I1IiIi11Ii1 ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 I1I ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  Ii11iII1 = Oo0O0O0ooO0O ( i1iII1IiiIiI1 )
  IIIIii = re . compile ( '<item>(.+?)</item>' ) . findall ( Ii11iII1 )
  for O0o0 in IIIIii :
   try :
    if '<m3u>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 11 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<mamahdsports>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 14 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<atc>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<atc>(.+?)</atc>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 6 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<scanner>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 11 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<cartoons>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 29 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<Adult>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 38 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<Anime>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 51 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<audiobooks>' in O0o0 :
     OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1i1I1II = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( O0o0 ) [ 0 ]
     O00Oo000ooO0 ( OO00Oo , I1i1I1II , 59 , O0OOO0OOoO0O , I1ii11iIi11i )
    elif '<folder>' in O0o0 :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
     for OO00Oo , I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i in OoO000 :
      O00Oo000ooO0 ( OO00Oo , I1i1I1II , 1 , O0OOO0OOoO0O , I1ii11iIi11i )
    else :
     OoO0O00 = re . compile ( '<link>(.+?)</link>' ) . findall ( O0o0 )
     if len ( OoO0O00 ) == 1 :
      OoO000 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
      IIiII = len ( IIIIii )
      for OO00Oo , I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i in OoO000 :
       if 'youtube.com/playlist' in I1i1I1II :
        O00Oo000ooO0 ( OO00Oo , I1i1I1II , 2 , O0OOO0OOoO0O , I1ii11iIi11i )
       else :
        I1I ( OO00Oo , I1i1I1II , 2 , O0OOO0OOoO0O , I1ii11iIi11i )
     elif len ( OoO0O00 ) > 1 :
      OO00Oo = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
      O0OOO0OOoO0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
      I1I ( OO00Oo , i1IiIiiI , 3 , O0OOO0OOoO0O , I1ii11iIi11i )
   except : pass
   if 80 - 80: I1iiiiI1iII . OOo0o0
  I1I ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.urlresolver/settings.xml" )
   I1IiIi11Ii1 = open ( file ) . read ( )
   IIi = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( I1IiIi11Ii1 ) [ 0 ]
   IIi = IIi . strip ( )
   I1i1I1II = 'plugin://script.module.urlresolver/?mode=auth_rd'
   if 'value=""' in IIi :
    i11iIIIIIi1 = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    I1I ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( i11iIIIIIi1 ) + '[/COLOR]' , I1i1I1II , 2 , I1IiI , Oo )
   else :
    i11iIIIIIi1 = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    I1I ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( i11iIIIIIi1 ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  iiII1i1 = 'https://i.imgur.com/4Pzgdwu.png'
  O00Oo000ooO0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , iiII1i1 , Oo )
  o00oOO0o = 'https://i.imgur.com/Om0Lq7V.png'
  O00Oo000ooO0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , o00oOO0o , Oo )
  OOO00O = 'https://i.imgur.com/klnhdFx.png'
  O00Oo000ooO0 ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , OOO00O , Oo )
 except :
  OOoOO0oo0ooO = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if OOoOO0oo0ooO == 0 :
   I1I ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   O00Oo000ooO0 ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if OOoOO0oo0ooO == 1 :
   quit ( )
   if 98 - 98: OOoO00o * OOoO00o / OOoO00o + iI1
 iI11i1I1 ( )
 if 34 - 34: i1Ii
def I1111I1iII11 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i1IiIiiI = url
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<item>(.+?)</item>' ) . findall ( Ii11iII1 )
 for O0o0 in IIIIii :
  try :
   if '<image>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 23 , iconimage , fanart )
   elif '<American>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 73 , iconimage , fanart )
   elif '<lordjd>' in O0o0 :
    OoO0O00 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( O0o0 )
    if len ( OoO0O00 ) == 1 :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
     IIiII = len ( IIIIii )
     for name , url , iconimage , fanart in OoO000 :
      if 'youtube.com/playlist' in url :
       O00Oo000ooO0 ( name , url , 2 , iconimage , fanart )
      else :
       Oooo0O0oo00oO ( name , url , 2 , iconimage , fanart )
    elif len ( OoO0O00 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     Oooo0O0oo00oO ( name , i1IiIiiI , 3 , iconimage , fanart )
   elif '<reddit>' in O0o0 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( O0o0 ) [ 0 ]
    O00Oo000ooO0 ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in O0o0 :
    OoO0O00 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( O0o0 )
    if len ( OoO0O00 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( O0o0 ) [ 0 ]
     IIi1i = re . compile ( '<referer>(.+?)</referer>' ) . findall ( O0o0 ) [ 0 ]
     I1I1iIiII1 = IIi1i
     i11i1I1 = "/"
     if not I1I1iIiII1 . endswith ( i11i1I1 ) :
      ii1I = I1I1iIiII1 + "/"
     else :
      ii1I = I1I1iIiII1
     Ii11iII1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = Ii11iII1 + '%26referer=' + ii1I
     I1I ( name , url , 10 , iconimage , fanart )
    elif len ( OoO0O00 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1I ( name , i1IiIiiI , 16 , iconimage , fanart )
     if 67 - 67: i11iIiiIii - i1IIi % o000o0o00o0Oo . O0
   elif '<folder>' in O0o0 :
    OoO000 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
    for name , url , iconimage , fanart in OoO000 :
     O00Oo000ooO0 ( name , url , 1 , iconimage , fanart )
     if 77 - 77: I1iiiiI1iII / iiI1iIiI
   else :
    OoO0O00 = re . compile ( '<link>(.+?)</link>' ) . findall ( O0o0 )
    if len ( OoO0O00 ) == 1 :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( O0o0 )
     IIiII = len ( IIIIii )
     for name , url , iconimage , fanart in OoO000 :
      if 'youtube.com/playlist' in url :
       O00Oo000ooO0 ( name , url , 2 , iconimage , fanart )
      else :
       I1I ( name , url , 2 , iconimage , fanart )
    elif len ( OoO0O00 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( O0o0 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( O0o0 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( O0o0 ) [ 0 ]
     I1I ( name , i1IiIiiI , 3 , iconimage , fanart )
  except : pass
  if 15 - 15: I1iiiiI1iII . iIii1I11I1II1 . OoooooooOO / i11iIiiIii - OOooO . i1IIi
 iI11i1I1 ( )
 if 33 - 33: iI1 . i1IIi11111i
 if 75 - 75: i1IIi11111i % i1IIi11111i . oOo0
 if 5 - 5: i1IIi11111i * i1Ii + Oooo0000 . OOoOoo00oo + Oooo0000
 if 91 - 91: O0
 if 61 - 61: i11Ii11I1Ii1i
 if 64 - 64: i1Ii / Oooo0000 - O0 - iI1
 if 86 - 86: iI1 % Oooo0000 / iiI1iIiI / Oooo0000
 if 42 - 42: i1
def o0o ( url ) :
 if 84 - 84: O0
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   OOOooOO0 = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   O00Oo000ooO0 ( "[COLOR skyblue]" + OOOooOO0 + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 87 - 87: OOo0o0 * o000o0o00o0Oo + OOoOoo00oo / iIii1I11I1II1 / OOoO00o
def I1111IIi ( url ) :
 if 93 - 93: OoooooooOO / iiI1iIiI % i11iIiiIii + o000o0o00o0Oo * i1
 I1 = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 iI11Ii = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 I1I ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 OoO0O00 = 0
 i1iIIIi1i = re . compile ( 'href="([^"]+)' ) . findall ( Ii11iII1 )
 for url in i1iIIIi1i :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in I1 ) :
    OoO0O00 += 1
    OOOooOO0 = "Link " + str ( OoO0O00 ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    iI1iIIiiii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     I1I ( "[COLOR skyblue]" + OOOooOO0 + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in iI11Ii ) :
     I1I ( "[COLOR yellow]" + OOOooOO0 + url + "[/COLOR]" , iI1iIIiiii , 2 , I1IiI , I1ii11iIi11i )
    else :
     I1I ( "[COLOR skyblue]" + OOOooOO0 + url + "[/COLOR]" , iI1iIIiiii , 2 , I1IiI , I1ii11iIi11i )
     if 26 - 26: iI1 . OoooooooOO
     if 39 - 39: OOoO00o - O0 % i11iIiiIii * oOo0 . I1iiiiI1iII
     if 58 - 58: i1 % i11iIiiIii . OOoO00o / OOo0o0
def O0o ( url ) :
 if 59 - 59: iiI1iIiI + iiI1iIiI + i1IIi11111i / iIii1I11I1II1
 if url == 'Football' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  O000oo = Oo0O0O0ooO0O ( 'http://wizhdsports.is/sport/Cricket' )
 IIi1I11I1II = dom_parser2 . parse_dom ( O000oo , 'div' , { 'class' : 'card' } )
 IIi1I11I1II = [ ( dom_parser2 . parse_dom ( OooOoooOo , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( OooOoooOo , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( OooOoooOo , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( OooOoooOo , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for OooOoooOo in IIi1I11I1II ]
 if len ( IIi1I11I1II ) < 1 :
  I1I ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , O0OOO0OOoO0O , Oo , '' )
 IIi1I11I1II = [ ( OooOoooOo [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , OooOoooOo [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , OooOoooOo [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , OooOoooOo [ 2 ] [ 0 ] . content ) if OooOoooOo [ 2 ] else 'Upcoming' , OooOoooOo [ 3 ] [ 0 ] . content ) for OooOoooOo in IIi1I11I1II ]
 if 46 - 46: OOoO00o
 if 8 - 8: OOo0o0 * Oooo0000 - OOooO - i1 * OOoOoo00oo % iiI1iIiI
 if 48 - 48: O0
 if 11 - 11: iI1 + OoooooooOO - i1 / i1IIi11111i + ooo0Oo0 . i11Ii11I1Ii1i
 IIi1I11I1II = [ ( OooOoooOo [ 0 ] , OooOoooOo [ 1 ] , OooOoooOo [ 2 ] , OooOoooOo [ 3 ] , OooOoooOo [ 4 ] ) for OooOoooOo in IIi1I11I1II ]
 i1Iii1i1I = 0
 OOoO00 = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for OooOoooOo in IIi1I11I1II :
  IiI111111IIII = OooOoooOo [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( i1Iii1i1I ) )
  i1Iii1i1I += 1
  time . sleep ( 0.10 )
  IiI111111IIII = i1Iiii111iI1iIi1 ( IiI111111IIII )
  OOO = OooOoooOo [ 1 ]
  oo0OOo0 = OooOoooOo [ 3 ]
  if 'Match Over' in oo0OOo0 :
   OOoO00 += 1
  I11IiI = dom_parser2 . parse_dom ( OooOoooOo [ 4 ] , 'a' )
  for O000oo in I11IiI :
   O0ooO0Oo00o = re . sub ( '<.+?>' , '' , O000oo . content )
   Ii11iII1 = O000oo . attrs [ 'href' ]
   Ii11iII1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + Ii11iII1
   if not 'Match Over' in oo0OOo0 :
    I1I ( '[COLOR aqua]' + IiI111111IIII + '[COLOR yellow]' + ' ' + oo0OOo0 + '[/COLOR]' , Ii11iII1 , 2 , O0OOO0OOoO0O , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( i1Iii1i1I ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( OOoO00 ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 77 - 77: iIii1I11I1II1 * i1
def oOooOo0 ( url ) :
 if 38 - 38: oOo0
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = re . compile ( 'title="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  if 84 - 84: iIii1I11I1II1 % OOoO00o / iIii1I11I1II1 % iI1
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 45 - 45: O0
 try :
  I1IiiiiI = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( Ii11iII1 ) [ 0 ]
  I1IiI = O0OOO0OOoO0O
  O00Oo000ooO0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1IiiiiI , 18 , O0OOO0OOoO0O , Oo , '' )
 except : pass
 if 80 - 80: oOo0 . i11iIiiIii - i1IIi11111i
def iIiIIi1 ( url , iconimage , fanart ) :
 if 7 - 7: i1Ii - ooo0Oo0 - OOo0o0 + i1Ii
 I1I ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( Ii11iII1 )
 if 26 - 26: OOooO
 for OoO0O00 in IIIIii :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( OoO0O00 ) [ 0 ]
  iI1iIIiiii = str . lower ( url )
  if '1e' in iI1iIIiiii :
   OOOooOO0 = '1st Half'
  else :
   OOOooOO0 = '2nd Half'
  I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 35 - 35: OOooO - iiI1iIiI % i1IIi11111i . OoooooooOO % OOooO
def I1i1Iiiii ( ) :
 if 94 - 94: i1IIi11111i * OOooO / ooo0Oo0 / OOooO
 I1i1I1II = 'http://www.goalsarena.org/en/'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( IIIIii )
 for O0OO0O , OO in oO0 :
  O00Oo000ooO0 ( "[COLOR skyblue]" + OO + "[/COLOR]" , O0OO0O , 21 , I1IiI , Oo , '' )
  if 83 - 83: O0 / iiI1iIiI - i1 - OOoOoo00oo
def iI1i11iII111 ( url ) :
 if 15 - 15: i11iIiiIii % OOooO . ooo0Oo0 + o000o0o00o0Oo
 if 61 - 61: ooo0Oo0 * o000o0o00o0Oo % ooo0Oo0 - i1IIi - iIii1I11I1II1
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OOoOO0oo0ooO = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if OOoOO0oo0ooO == 0 :
  try :
   IIIIii = re . compile ( '<iframe src="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in IIIIii :
   oOooO0 ( OO00Oo , IIIIii , O0OOO0OOoO0O )
  Ii1I1Ii = Oo0O0O0ooO0O ( IIIIii )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ii1I1Ii ) [ 0 ]
  url = 'https:' + url
  OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = O0OOO0OOoO0O , thumbnailImage = O0OOO0OOoO0O )
  xbmc . Player ( ) . play ( url , OOoO0 , False )
  quit ( 0 )
 if OOoOO0oo0ooO == 1 :
  try :
   IIIIii = re . compile ( '<iframe src="(.+?)"' ) . findall ( Ii11iII1 ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   iI1i11iII111 ( url )
  Ii1I1Ii = Oo0O0O0ooO0O ( IIIIii )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( Ii1I1Ii ) [ 0 ]
  url = 'https:' + url
  OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = O0OOO0OOoO0O , thumbnailImage = O0OOO0OOoO0O )
  xbmc . Player ( ) . play ( url , OOoO0 , False )
  quit ( 0 )
  if 86 - 86: OOo0o0 * i1IIi11111i % i1IIi . OOooO . i11iIiiIii
def oOOoo00O00o ( ) :
 if 98 - 98: OOoOoo00oo + I1iiiiI1iII + OOo0o0 % OoooooooOO
 I1i1I1II = 'http://m.liveatc.net/feeds/'
 Ii11iII1 = oooooo0O000o ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://m.liveatc.net' + I1i1I1II
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 7 , I1IiI , Oo , '' )
  if 64 - 64: iiI1iIiI . i1IIi11111i - oOo0 / OoooooooOO
def O0O0ooOOO ( url ) :
 if 77 - 77: Oooo0000 - i11Ii11I1Ii1i - i1Ii
 if 49 - 49: i11Ii11I1Ii1i % O0 . Oooo0000 + OOo0o0 / iiI1iIiI
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 72 - 72: i1Ii * ooo0Oo0 . iiI1iIiI - i11Ii11I1Ii1i + i1IIi
def iIi1ii ( url ) :
 url = url . replace ( ' ' , '%20' )
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li>(.+?)</a>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '(.+?)</li>' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 58 - 58: Oooo0000 % i1IIi11111i
def i1OOoO ( url ) :
 if 89 - 89: i1IIi11111i + i1 * iI1 * OOooO
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   I1I ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 37 - 37: OoooooooOO - O0 - i1IIi11111i
def o0o0O0O00oOOo ( ) :
 if 14 - 14: Oooo0000 + OOo0o0
 O00Oo000ooO0 ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 I1i1I1II = 'http://m.broadcastify.com/?a=la&coid=1'
 Ii11iII1 = oooooo0O000o ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://m.broadcastify.com' + I1i1I1II
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 12 , I1IiI , Oo , '' )
  if 52 - 52: OoooooooOO - i1Ii
def o0O0o0 ( url ) :
 if 37 - 37: o000o0o00o0Oo * iI1 % i11iIiiIii % i1Ii + OOooO
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 78 - 78: o000o0o00o0Oo % OOo0o0 / OOoO00o - iIii1I11I1II1
def ooooo0O0000oo ( url ) :
 if 21 - 21: i1IIi11111i - iiI1iIiI
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 18 - 18: ooo0Oo0 + iI1 % OOoOoo00oo - OoooooooOO - o000o0o00o0Oo / i1IIi
def oo0oO ( url ) :
 if 94 - 94: iIii1I11I1II1 / ooo0Oo0 % OOoO00o * OOoO00o * i11Ii11I1Ii1i
 Ii11iII1 = oooooo0O000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  IIIIii = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 IIiIiI ( IIIIii )
 if 94 - 94: OOo0o0 . i1IIi - i1IIi11111i % O0 - i1
def ooO0O00Oo0o ( ) :
 if 65 - 65: o000o0o00o0Oo . iI1 - oOo0 * I1iiiiI1iII / oOo0 / i1Ii
 I1i1I1II = 'http://m.broadcastify.com/?a=top25'
 Ii11iII1 = oooooo0O000o ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  i111iIi1i1II1 = OOOooOO0 . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  OOOooOO0 = OOOooOO0 . split ( ')' ) [ - 1 ] . strip ( )
  I1i1I1II = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://m.broadcastify.com' + I1i1I1II
  I1I ( "[COLOR aqua]" + OOOooOO0 + "[COLOR yellow] :: " + i111iIi1i1II1 + " Listening" + "[/COLOR]" , I1i1I1II , 14 , I1IiI , Oo , '' )
  if 86 - 86: iIii1I11I1II1 / Oooo0000 . i11Ii11I1Ii1i
def II1i111Ii1i ( url ) :
 if 15 - 15: i11Ii11I1Ii1i / i1IIi
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = O0oO0 ( OOOooOO0 )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( OoO0O00 ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( OoO0O00 ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in OOOooOO0 :
    iI1iIIiiii = 'https://www.youtube.com' + url
    I1I ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , iI1iIIiiii , 2 , I1IiI , I1ii11iIi11i )
    if 7 - 7: iiI1iIiI
def I1ii1iIiii1I ( ) :
 if 42 - 42: i1IIi11111i + i1IIi - OOooO / I1iiiiI1iII
 I1i1I1II = 'http://burningwhee1s.blogspot.co.uk/'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( IIIIii )
 for Ii11iII1 , OOOooOO0 in oO0 :
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , Ii11iII1 , 24 , I1IiI , Oo , '' )
  if 9 - 9: O0 % O0 - i1IIi11111i
def OoO ( url ) :
 if 12 - 12: O0 - i1IIi11111i
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( OoO0O00 ) [ 0 ]
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 81 - 81: Oooo0000 - Oooo0000 . OOoO00o
def o0OoOo00o0o ( url , iconimage ) :
 if 41 - 41: i1Ii % i1 - ooo0Oo0 * oOo0 * ooo0Oo0
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( IIIIii )
 try :
  for OoO0O00 in oO0 :
   OOOooOO0 = re . compile ( '<b>(.+?)</b>' ) . findall ( OoO0O00 ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    OOOoOO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( OoO0O00 ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     OOOoOO0o = re . compile ( '<b>(.+?)</b>' ) . findall ( OoO0O00 ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     OOOoOO0o = ''
   OOOooOO0 = O0oO0 ( OOOooOO0 )
   OOOoOO0o = O0oO0 ( OOOoOO0o )
   i1II1 = re . compile ( '<option value="(.+?)"' ) . findall ( OoO0O00 ) [ 1 ]
   I1I ( "[COLOR aqua]" + OOOooOO0 + "  " + OOOoOO0o + "[/COLOR]" , i1II1 , 2 , I1IiI , Oo , '' )
 except :
  I1I ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 25 - 25: oOo0 / iIii1I11I1II1 % OOoO00o
def IiiiiI1i1Iii ( ) :
 if 87 - 87: i1IIi11111i
 if 29 - 29: iiI1iIiI % OOoOoo00oo - iiI1iIiI / OOoOoo00oo . i1IIi
 I1i1I1II = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 OoO000 = json . loads ( Ii11iII1 )
 i11III1111iIi = OoO000 [ 'results' ]
 for I1i111I in i11III1111iIi :
  Ooo = 'https://image.tmdb.org/t/p/w640'
  OOOooOO0 = I1i111I [ 'title' ]
  I1IiI = I1i111I [ 'poster_path' ]
  Oo0oo0O0o00O = I1i111I [ 'id' ]
  I1IiI = Ooo + I1IiI
  I1ii11iIi11i = I1i111I [ 'backdrop_path' ]
  I1ii11iIi11i = Ooo + I1ii11iIi11i
  I1i11 = I1i111I [ 'overview' ]
  Oo0oo0O0o00O = str ( Oo0oo0O0o00O )
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , OOOooOO0 , 33 , I1IiI , I1ii11iIi11i , I1i11 )
  if 12 - 12: i1IIi + i1IIi - o000o0o00o0Oo * ooo0Oo0 % ooo0Oo0 - i11Ii11I1Ii1i
def o0O ( url ) :
 if 84 - 84: i1 + i1IIi - i11Ii11I1Ii1i . o000o0o00o0Oo * OoooooooOO + iiI1iIiI
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = re . compile ( '<i>(.+?)</i>' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = OOOooOO0 . strip ( )
  O00Oo000ooO0 ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  II1i11I = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( Ii11iII1 ) [ 0 ]
  ii1I1IIii11 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  O00Oo000ooO0 ( '[COLOR yellow]Next Page >>[/COLOR]' , II1i11I , 26 , ii1I1IIii11 , I1ii11iIi11i )
 except : pass
 if 67 - 67: OOoO00o + iI1 / i1IIi11111i . OOo0o0 + OOoOoo00oo
def ooOoOo0 ( url , iconimage ) :
 if 2 - 2: OOoO00o % iIii1I11I1II1 * iIii1I11I1II1 . i1IIi11111i / OOoO00o
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( Ii11iII1 ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 IIIIii = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( Ii11iII1 )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 OooOoooOo = 1
 iII1i1 = [ ]
 for OoO0O00 in IIIIii :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  iII1i1 . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( OooOoooOo ) )
  time . sleep ( 0.02 )
  OooOoooOo += 1
  OOOooOO0 = re . compile ( '(.+?)</p>' ) . findall ( OoO0O00 ) [ 0 ] . replace ( 'Server' , '' )
  OOOooOO0 = OOOooOO0 . strip ( )
 O0oOOoooOO0O = 1
 I1IiIi11Ii1 = 0
 ooo00Ooo = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 93 - 93: i11iIiiIii - iiI1iIiI * o000o0o00o0Oo * iI1 % O0 + OoooooooOO
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if I1IiIi11Ii1 > len ( iII1i1 ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 25 - 25: I1iiiiI1iII + OOooO / i1Ii . i1IIi11111i % O0 * i1
  if ooo00Ooo == 0 :
   I1IiIi11Ii1 += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( I1IiIi11Ii1 ) + "[/COLOR]" , '' )
   try :
    Ii11iII1 = Oo0O0O0ooO0O ( iII1i1 [ I1IiIi11Ii1 ] )
    oO0 = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
    o0O0oo0OO0O = base64 . b64decode ( oO0 )
    url = re . compile ( 'src="(.+?)"' ) . findall ( o0O0oo0OO0O ) [ 0 ]
    OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    o0Oooo = open ( OO0 ) . read ( )
    iiI = re . compile ( '<url>(.+?)</url>' ) . findall ( o0Oooo )
    for oO in iiI :
     IIiIi = re . compile ( '<bad>(.+?)<bad>' ) . findall ( oO ) [ 0 ]
     if url == IIiIi :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( I1IiIi11Ii1 ) )
      time . sleep ( 0.5 )
      ooo00Ooo = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     OOoOooOoOOOoo = liveresolver . resolve ( url )
    else : OOoOooOoOOOoo = url
    OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( OOoOooOoOOOoo , OOoO0 , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( I1IiIi11Ii1 ) )
    time . sleep ( 0.5 )
    ooo00Ooo = 5
    pass
  if ooo00Ooo == 5 :
   ooo00Ooo = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   ooo00Ooo += 1
   if 25 - 25: OoooooooOO - iiI1iIiI . iiI1iIiI * OOo0o0
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 I1I1iIiII1 = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if I1I1iIiII1 :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( OO0 , "a" ) as iIi :
   iIi . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 81 - 81: OOoO00o + I1iiiiI1iII
def o0oo0 ( url ) :
 if 97 - 97: Oooo0000 % o000o0o00o0Oo
 if 25 - 25: ooo0Oo0 % o000o0o00o0Oo . o000o0o00o0Oo
 if url == 'search' :
  O0O0Oo00 = ''
  oOoO00o = xbmc . Keyboard ( O0O0Oo00 , 'Enter Search Term' )
  oOoO00o . doModal ( )
  if oOoO00o . isConfirmed ( ) :
   O0O0Oo00 = oOoO00o . getText ( )
   if len ( O0O0Oo00 ) > 1 :
    oO00O0 = O0O0Oo00 . lower ( )
    if 36 - 36: OOo0o0 - OOooO . ooo0Oo0 - i11iIiiIii - OOoOoo00oo * ooo0Oo0
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , O0OOO0OOoO0O , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , O0OOO0OOoO0O , 5000 )
   quit ( )
  oO00O0 = oO00O0 . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + oO00O0 + '.html'
  OooOOOO ( url , I1IiI )
  if 45 - 45: o000o0o00o0Oo % iiI1iIiI - i11iIiiIii
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  OooOOOO ( url , I1IiI )
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * iiI1iIiI
def OooOOOO ( url , icon ) :
 if 46 - 46: Oooo0000 + i1
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = re . compile ( '<i>(.+?)</i>' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = O0oO0 ( OOOooOO0 )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  O00Oo000ooO0 ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 70 - 70: OOoO00o / iIii1I11I1II1
def Oo0oooO0oO ( ) :
 if 19 - 19: i11iIiiIii + OoooooooOO - ooo0Oo0 - iI1
 I1i1I1II = 'http://www.genti.stream/'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  Iii1iiIi1II = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ] . strip ( )
  OO0O00oOo = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( OoO0O00 ) [ 1 ] . strip ( )
  I1i1I1II = re . compile ( 'href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://www.genti.stream/' + I1i1I1II
  I1I ( "[COLOR aqua]" + Iii1iiIi1II + "[COLOR yellow] vs [COLOR aqua]" + OO0O00oOo + "[/COLOR]" , I1i1I1II , 39 , I1IiI , I1ii11iIi11i )
  if 14 - 14: iiI1iIiI
def IIiIiI1I ( url ) :
 if 100 - 100: iIii1I11I1II1 + Oooo0000 / ooo0Oo0 . i11iIiiIii
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III1I1Iii1iiI = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
 if not 'http' in III1I1Iii1iiI :
  III1I1Iii1iiI = 'http://www.genti.stream' + III1I1Iii1iiI
 O0OO0O = Oo0O0O0ooO0O ( III1I1Iii1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1Iii11I1i = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( O0OO0O ) [ 0 ]
 Ii1I1Ii = Oo0O0O0ooO0O ( i1Iii11I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'src : "(.+?)"' ) . findall ( Ii1I1Ii ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "src : '(.+?)'" ) . findall ( Ii1I1Ii ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( Ii1I1Ii ) [ 0 ]
 except : IndexError
 try :
  url = re . compile ( "source: '(.+?)'" ) . findall ( Ii1I1Ii ) [ 0 ]
 except : pass
 if 72 - 72: iIii1I11I1II1 * OOooO % i1Ii / i1
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , O0OOO0OOoO0O , 5000 )
  quit ( )
 oOooO0 ( OO00Oo , url , O0OOO0OOoO0O )
 if 35 - 35: i1Ii + i1IIi % o000o0o00o0Oo % iI1 + OOo0o0
 if 17 - 17: i1IIi
def iiIi1i ( url ) :
 if 27 - 27: OOoOoo00oo * i1Ii . oOo0 % I1iiiiI1iII * I1iiiiI1iII . i1IIi
 O0OOoOOO0oO = cfscrape . create_scraper ( )
 i1IiIiiI = O0OOoOOO0oO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( i1IiIiiI ) [ 0 ]
 oO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIIii )
 for url , OOOooOO0 in oO0 :
  url = 'http://kimcartoon.me/CartoonList' + url
  O00Oo000ooO0 ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 28 - 28: i1Ii + i11iIiiIii / iI1 % Oooo0000 % ooo0Oo0 - O0
def ooo0OOO ( url ) :
 if 49 - 49: i11iIiiIii % OOooO . Oooo0000
 O0OOoOOO0oO = cfscrape . create_scraper ( )
 i1IiIiiI = O0OOoOOO0oO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( i1IiIiiI )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   Ii1i1iI = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( OoO0O00 ) [ 0 ]
   Ii1i1iI = O0oO0 ( Ii1i1iI )
  except IndexError :
   Ii1i1iI = ''
  O00Oo000ooO0 ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , Ii1i1iI )
  if 16 - 16: OOoOoo00oo / ooo0Oo0 / OoooooooOO * iiI1iIiI + i1IIi % OOoOoo00oo
 try :
  ooo0o00 = re . compile ( '<li>(.+?)Next' ) . findall ( i1IiIiiI )
  for OoO0O00 in ooo0o00 :
   II1i11I = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ - 1 ]
   ooO = 'http://kimcartoon.me' + II1i11I
   o0o00 = 'https://i.imgur.com/mjCRjXT.png'
   O00Oo000ooO0 ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , ooO , 30 , o0o00 , I1ii11iIi11i )
 except : pass
 if 14 - 14: i1IIi11111i . OOoOoo00oo . iI1 + OoooooooOO - OOoOoo00oo + I1iiiiI1iII
def iII1iiiiIII ( url ) :
 if 78 - 78: OOoOoo00oo * i1IIi11111i / iI1 - O0 / I1iiiiI1iII
 O0OOoOOO0oO = cfscrape . create_scraper ( )
 i1IiIiiI = O0OOoOOO0oO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( '<td>(.+?)</td>' ) . findall ( i1IiIiiI )
 for OoO0O00 in IIIIii :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   OOOooOO0 = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   I1I ( "[COLOR aqua][B]" + OOOooOO0 + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 96 - 96: Oooo0000 . i1IIi11111i - i1Ii
def O0OI11iiiii1II ( url ) :
 if 51 - 51: O0 % OOo0o0 - i11Ii11I1Ii1i
 OOoOO0oo0ooO = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if OOoOO0oo0ooO == 0 :
  url = url + '&s=rapidvideo'
  O0OOoOOO0oO = cfscrape . create_scraper ( )
  i1IiIiiI = O0OOoOOO0oO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   oO0 = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i1IiIiiI )
   for Ii11iII1 in oO0 :
    url = re . compile ( 'src="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
    if 'rapidvideo' in url :
     oOooO0 ( OO00Oo , url , O0OOO0OOoO0O )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if OOoOO0oo0ooO == 1 :
  url = url + '&s=openload'
  O0OOoOOO0oO = cfscrape . create_scraper ( )
  i1IiIiiI = O0OOoOOO0oO . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   oO0 = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( i1IiIiiI )
   for Ii11iII1 in oO0 :
    url = re . compile ( 'src="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
    oOooO0 ( OO00Oo , url , O0OOO0OOoO0O )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 31 - 31: OOoO00o / ooo0Oo0 - OOoO00o - OOoOoo00oo
   if 7 - 7: OOoO00o % O0 . Oooo0000 + iiI1iIiI - iI1
def o0o0O00oo0 ( ) :
 if 27 - 27: i11iIiiIii % i11Ii11I1Ii1i % iI1 . O0 - ooo0Oo0 + Oooo0000
 I1i1I1II = "http://www.loyalbooks.com/genre-menu"
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( Ii11iII1 )
 for O0o0 in IIIIii :
  if "paid" not in O0o0 :
   O0OO0O = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
   Ii1I1Ii = "http://www.loyalbooks.com" + O0OO0O
   OO00Oo = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
   O00Oo000ooO0 ( "[COLOR aqua]" + OO00Oo + "[/COLOR]" , Ii1I1Ii , 60 , I1IiI , Oo , '' )
   if 57 - 57: iIii1I11I1II1 / iI1 - i1IIi
def ooOOo00O00Oo ( url ) :
 if 42 - 42: O0 / i1IIi11111i + OoooooooOO * i1Ii % i1Ii
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( Ii11iII1 ) [ 0 ]
 i1iIi = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( IIIIii )
 for O0o0 in i1iIi :
  iI1iIIiiii = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
  Ii1I1Ii = "http://www.loyalbooks.com" + iI1iIIiiii
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
  O0OOO0OOoO0O = "http://www.loyalbooks.com" + I1IiI
  OO00Oo = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
  O00Oo000ooO0 ( "[COLOR aqua]" + OO00Oo + "[/COLOR]" , Ii1I1Ii , 61 , O0OOO0OOoO0O , Oo , '' )
 try :
  Ii11iII1 = Oo0O0O0ooO0O ( url )
  I1IiiiiI = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( Ii11iII1 ) [ 0 ]
  I1IiI = 'https://i.imgur.com/mjCRjXT.png'
  O00Oo000ooO0 ( "[COLOR yellow]Next Page -->[/COLOR]" , I1IiiiiI , 60 , I1IiI , Oo , '' )
 except : pass
 if 21 - 21: OOo0o0 / o000o0o00o0Oo + OOooO + OoooooooOO
 if 91 - 91: i11iIiiIii / i1IIi + OOoO00o + i1Ii * i11iIiiIii
def OoOoOo00o0 ( name , url , iconimage ) :
 if 90 - 90: ooo0Oo0 % O0 * iIii1I11I1II1 . OOoO00o
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( Ii11iII1 )
 for O0o0 in IIIIii :
  OOOooOO0 = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
  iI1iIIiiii = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( O0o0 ) [ 0 ]
  I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , iI1iIIiiii , 10 , iconimage , Oo , '' )
  if 8 - 8: i1Ii + i11Ii11I1Ii1i / OOoO00o / iI1
def ooo0O ( ) :
 if 16 - 16: Oooo0000
 I1i1I1II = 'http://www.shadownet.me/'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIIii )
 for I1i1I1II , OOOooOO0 in oO0 :
  OOOooOO0 = O0oO0 ( OOOooOO0 )
  if 'P2P' not in OOOooOO0 :
   O00Oo000ooO0 ( "[COLOR skyblue]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 49 , I1IiI , Oo , '' )
   if 41 - 41: i1IIi * i11Ii11I1Ii1i / OoooooooOO . OOoOoo00oo
   if 83 - 83: OOoO00o . O0 / ooo0Oo0 / OOoOoo00oo - i11Ii11I1Ii1i
def oO0oO0 ( url ) :
 if 14 - 14: OOoO00o
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( IIIIii )
 for OoO0O00 in oO0 :
  OOOooOO0 = re . compile ( 'alt="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1I ( "[COLOR skyblue]" + OOOooOO0 + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  II1i11I = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( Ii11iII1 ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  O00Oo000ooO0 ( "[COLOR orange]Next Page --->[/COLOR]" , II1i11I , 49 , I1IiI , Oo , '' )
 except : pass
 if 99 - 99: OOoO00o
def IIi1ii1Ii ( url ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + OOoO00o - i11iIiiIii + OOoOoo00oo
 def ii1i ( url ) :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iiiIi . add_header ( 'Referer' , url )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11iII1 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  return Ii11iII1
  if 62 - 62: i1 / o000o0o00o0Oo
 Ii11iII1 = ii1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  IIIIii = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( Ii11iII1 ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in IIIIii :
  url = IIIIii
  oOooO0 ( OO00Oo , url , O0OOO0OOoO0O )
 Ii1I1Ii = ii1i ( IIIIii )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( Ii1I1Ii ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 7 - 7: OoooooooOO . I1iiiiI1iII
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = O0OOO0OOoO0O , thumbnailImage = O0OOO0OOoO0O )
  OOoO0 . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , OOoO0 , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = O0OOO0OOoO0O , thumbnailImage = O0OOO0OOoO0O )
  OOoO0 . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , OOoO0 , False )
 else :
  if '.m3u8' in url :
   iI1iIIiiii = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + OO00Oo + '&amp;url=' + url + '&amp;iconImage=' + O0OOO0OOoO0O
  elif '.ts' in url :
   iI1iIIiiii = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + OO00Oo + '&amp;url=' + url + '&amp;iconImage=' + O0OOO0OOoO0O
  else :
   iI1iIIiiii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 53 - 53: OOooO % OOooO * i1IIi11111i + Oooo0000
  OOoO0 = xbmcgui . ListItem ( OO00Oo , iconImage = O0OOO0OOoO0O , thumbnailImage = O0OOO0OOoO0O )
  OOoO0 . setPath ( url )
  if 92 - 92: OoooooooOO + i1IIi / OOooO * O0
  xbmc . Player ( ) . play ( iI1iIIiiii , OOoO0 , False )
  if 100 - 100: i1Ii % iIii1I11I1II1 * i11Ii11I1Ii1i - OOoO00o
  if 92 - 92: i1Ii
def II11iI111i1 ( ) :
 if 95 - 95: OoooooooOO - I1iiiiI1iII * iiI1iIiI + Oooo0000
 I1i1I1II = 'https://www.skylinewebcams.com/en/webcam.html'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<i class="icon-angle-down">(.+?)<i class="icon-angle-down">' ) . findall ( Ii11iII1 ) [ 0 ] . replace ( '<strong>' , '' ) . replace ( '&nbsp;' , '' )
 oO0 = re . compile ( '<a href="(.+?)" class="menu-item">(.+?)<span class="ccnt">(.+?)</span>' ) . findall ( IIIIii )
 for Ii11iII1 , OOOooOO0 , iIi1 in oO0 :
  if 'http' not in Ii11iII1 :
   I1i1I1II = 'https://www.skylinewebcams.com' + Ii11iII1
   O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 46 , I1IiI , Oo , '' )
   if 21 - 21: iI1
def OoO00 ( url ) :
 if 85 - 85: ooo0Oo0 * ooo0Oo0 * iiI1iIiI . OoooooooOO . OOooO * i1Ii
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<li class="webcam">(.+?)</span>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   o000oOoo0o000 = re . compile ( 'data-original="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   if not 'http' in o000oOoo0o000 :
    I1IiI = 'http:' + o000oOoo0o000
    OOOooOO0 = re . compile ( 'alt="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
    IiI11iI1i1i1i = re . compile ( '<a href="(.+?)">' ) . findall ( OoO0O00 ) [ 0 ]
    if not 'http:' in IiI11iI1i1i1i :
     url = 'https://www.skylinewebcams.com' + IiI11iI1i1i1i
     O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  except : pass
  if 89 - 89: iI1
def Ooooooo ( name , url , iconimage ) :
 if 39 - 39: I1iiiiI1iII * ooo0Oo0 + iIii1I11I1II1 - I1iiiiI1iII + OOoOoo00oo
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  IIIIii = re . compile ( '<script type="text/javascript">(.+?)</script>' ) . findall ( Ii11iII1 ) [ 1 ]
  url = re . compile ( "url:'(.+?)'}" ) . findall ( IIIIii ) [ 0 ]
  OOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , OOoO0 , False )
  if 69 - 69: O0
 except : pass
 quit ( 0 )
 if 85 - 85: i1Ii / O0
def iI1iIIIi1i ( ) :
 if 89 - 89: iIii1I11I1II1
 I1i1I1II = 'http://www.watchepisodeseries.com/home/schedule'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( IIIIii )
 for I1i1I1II , i11iiiiI1i , iIIii in oO0 :
  O00Oo000ooO0 ( "[COLOR aqua]" + i11iiiiI1i + "  " + iIIii + "[/COLOR]" , I1i1I1II , 67 , I1IiI , I1ii11iIi11i )
  if 18 - 18: OOoO00o . iiI1iIiI
  if 40 - 40: O0 - OoooooooOO - I1iiiiI1iII
def iIiii ( url ) :
 if 76 - 76: iiI1iIiI . i1Ii - o000o0o00o0Oo - OOoO00o * i1
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 1 ]
  OOOooOO0 = O0oO0 ( OOOooOO0 )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  O0OOO0OOoO0O = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( OoO0O00 ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( OoO0O00 ) [ 0 ]
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 68 , O0OOO0OOoO0O , I1ii11iIi11i )
  if 54 - 54: I1iiiiI1iII + O0 + iI1 * oOo0 - OOoOoo00oo % OOo0o0
  if 13 - 13: i1Ii / OOoO00o * i1 . i1 * i1Ii
def O00oO ( url , iconimage , fanart ) :
 if 40 - 40: Oooo0000 / I1iiiiI1iII
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 OOOoO000 = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in OOOoO000 :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
 IIIIii = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( Ii11iII1 )
 OooOoooOo = datetime . now ( )
 for OoO0O00 in IIIIii :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   OOOooOO0 = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ]
   OOOooOO0 = O0oO0 ( OOOooOO0 )
   oOOOO = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ]
   Ii = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ]
   i11iiiiI1i = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in i11iiiiI1i :
    i11iiiiI1i = i11iiiiI1i . strip ( )
    i11iiiiI1i = time . strptime ( i11iiiiI1i , "%d/%m/%Y" )
    Ii1ii111i1 = ( "%s/%s/%s" % ( OooOoooOo . day , OooOoooOo . month , OooOoooOo . year ) )
    Ii1ii111i1 = time . strptime ( Ii1ii111i1 , "%d/%m/%Y" )
    if ( Ii1ii111i1 < i11iiiiI1i ) :
     OOOooOO0 = '[COLOR yellow]' + ( OOOooOO0 ) + ' - Not Aired Yet' + '[/COLOR]'
     Ii = '[COLOR yellow]' + ( Ii ) + '[/COLOR]'
     oOOOO = '[COLOR yellow]' + ( oOOOO ) + '[/COLOR]'
     if 31 - 31: OOoOoo00oo + O0
    if not 'Season 0' in oOOOO :
     O00Oo000ooO0 ( "[COLOR aqua]" + oOOOO + " " + Ii + " " + OOOooOO0 + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 87 - 87: i1Ii
  if 45 - 45: i1 / OoooooooOO - OOoO00o / OOooO % I1iiiiI1iII
def OoOIii11iI11i1I ( url , iconimage , fanart ) :
 if 64 - 64: i11iIiiIii
 if 38 - 38: I1iiiiI1iII / iiI1iIiI - I1iiiiI1iII . iI1
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
   OOOooOO0 = OOOooOO0 . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
   if not 'Lolzor.Com' in OOOooOO0 :
    if not 'Videoplayer.Gq' in OOOooOO0 :
     if not 'Vidbaba.Com' in OOOooOO0 :
      if not 'Gagomatic.Com' in OOOooOO0 :
       if not 'Favour.Me' in OOOooOO0 :
        if not 'Funblr.Com' in OOOooOO0 :
         if not 'Vid.Ag' in OOOooOO0 :
          if not 'Mycollection.Net' in OOOooOO0 :
           if not 'Adhqmedia.Com' in OOOooOO0 :
            if not 'Filenuke.Com' in OOOooOO0 :
             if not 'Mrfile.Me' in OOOooOO0 :
              I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 69 - 69: OoooooooOO + o000o0o00o0Oo
  if 97 - 97: OOoOoo00oo - i1 / OOooO . i11iIiiIii % OOo0o0 * OOo0o0
def ii1IIIIiI11 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  url = re . compile ( 'href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    OOoOooOoOOOoo = liveresolver . resolve ( url )
   else : OOoOooOoOOOoo = url
   OOoO0 = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   OOoO0 . setPath ( OOoOooOoOOOoo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoO0 )
   xbmc . Player ( ) . play ( OOoOooOoOOOoo )
   if 40 - 40: i1IIi11111i
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 67 - 67: OOo0o0 + i11Ii11I1Ii1i - O0 . OOo0o0 * i11Ii11I1Ii1i * iI1
def o00 ( ) :
 if 81 - 81: OOoOoo00oo - iI1 % i1Ii - i1 / ooo0Oo0
 O0O0Oo00 = ''
 oOoO00o = xbmc . Keyboard ( O0O0Oo00 , 'Enter Search Term' )
 oOoO00o . doModal ( )
 if oOoO00o . isConfirmed ( ) :
  O0O0Oo00 = oOoO00o . getText ( )
  if len ( O0O0Oo00 ) > 1 :
   oO00O0 = O0O0Oo00 . lower ( )
   oO00O0 = oO00O0 . replace ( ' ' , '%20' )
   if 4 - 4: OoooooooOO - i1IIi % OOooO - OOoOoo00oo * i1IIi11111i
  else : quit ( )
 else : oO00O0 = urllib . unquote_plus ( I1i1I1II ) . lower ( ) ; O0O0Oo00 = urllib . unquote_plus ( I1i1I1II )
 I1i1I1II = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + oO00O0
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '"series"(.+?)"series_id"' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( 'original_name":"(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  iI1iIIiiii = re . compile ( '"seo_name":"(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://www.watchepisodeseries.com/' + iI1iIIiiii
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + iI1iIIiiii + '.jpg'
  O00Oo000ooO0 ( OOOooOO0 , I1i1I1II , 68 , I1IiI , I1ii11iIi11i , '' )
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . OOoO00o / OoooooooOO % iiI1iIiI % O0
def I1iii ( ) :
 if 86 - 86: o000o0o00o0Oo * O0 * I1iiiiI1iII
 I1i1I1II = 'http://www.watchepisodeseries.com/home/popular-series'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<div title="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = O0oO0 ( OOOooOO0 )
  I1i1I1II = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( OoO0O00 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( OoO0O00 ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  O00Oo000ooO0 ( '[COLOR aqua]' + OOOooOO0 + '[/COLOR]' , I1i1I1II , 68 , I1IiI , I1ii11iIi11i )
  if 51 - 51: i11Ii11I1Ii1i + I1iiiiI1iII . i1IIi . o000o0o00o0Oo + Oooo0000 * iiI1iIiI
  if 72 - 72: OOo0o0 + OOo0o0 / i11Ii11I1Ii1i . OoooooooOO % OOooO
def III ( ) :
 if 41 - 41: i11iIiiIii + ooo0Oo0 / iiI1iIiI . OoooooooOO % OOo0o0 % i1IIi
 try :
  oOO = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  O0O0Oo00 = ''
  oOoO00o = xbmc . Keyboard ( O0O0Oo00 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  oOoO00o . doModal ( )
  if oOoO00o . isConfirmed ( ) :
   O0O0Oo00 = oOoO00o . getText ( )
   if len ( O0O0Oo00 ) > 1 :
    oO00O0 = O0O0Oo00
   else : quit ( )
  if oO00O0 == oOO :
   Ii1II ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  O0O0Oo00 = ''
  oOoO00o = xbmc . Keyboard ( O0O0Oo00 , 'Enter The Password You Set' )
  oOoO00o . doModal ( )
  if oOoO00o . isConfirmed ( ) :
   O0O0Oo00 = oOoO00o . getText ( )
   if len ( O0O0Oo00 ) > 1 :
    oO00O0 = O0O0Oo00
   else : quit ( )
  with open ( i1i1II , "w" ) as iIi :
   iIi . write ( oO00O0 )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 89 - 89: oOo0 + OoooooooOO + oOo0 * i1IIi + iIii1I11I1II1 % iI1
   if 59 - 59: OOoOoo00oo + i11iIiiIii
   if 88 - 88: i11iIiiIii - i1Ii
def Ii1II ( ) :
 if 67 - 67: OOoOoo00oo . ooo0Oo0 + Oooo0000 - OoooooooOO
 OOOoO = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 I1i = '[COLOR aqua]Asian Special Porn[/COLOR]'
 O00Oo000ooO0 ( I1i , OOOoO , 1 , I1IiI , Oo , '' )
 I1i1I1II = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<li class="">(.+?)</li>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<strong>(.+?)</strong>' ) . findall ( OoO0O00 ) [ 0 ]
  iIi1 = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ]
  iI1iIIiiii = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'https://www.eporner.com' + iI1iIIiiii
  if not 'All' in OOOooOO0 :
   if not 'Homemade' in OOOooOO0 :
    O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "  " + "[COLOR yellow]" + iIi1 + "[/COLOR]" , I1i1I1II , 36 , I1IiI , Oo , '' )
    if 12 - 12: OoooooooOO
def ii1iiIi1 ( url ) :
 if 34 - 34: OOoOoo00oo
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 IIIIii = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( 'title="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  iI1iIIiiii = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = 'https://www.eporner.com' + iI1iIIiiii
  O00Oo000ooO0 ( "[COLOR skyblue]" + OOOooOO0 + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 91 - 91: iIii1I11I1II1 % i1IIi11111i . iIii1I11I1II1 % i1IIi / i11Ii11I1Ii1i * Oooo0000
 try :
  II1i11I = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( Ii11iII1 ) [ 0 ]
  I1IiiiiI = 'https://www.eporner.com' + II1i11I
  ii1I1IIii11 = 'http://imgur.com/3eNoY0p'
  O00Oo000ooO0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I1IiiiiI , 36 , ii1I1IIii11 , Oo , '' )
 except : pass
 if 10 - 10: i11Ii11I1Ii1i . OOoO00o
def I1iOOOO ( url , iconimage ) :
 if 88 - 88: OOoO00o
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 iiI11I1i1i1iI = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( iiI11I1i1i1iI )
 for OoOOo000o0 , Ii11iII1 in oO0 :
  OoOOo000o0 = OoOOo000o0 . replace ( ':' , '' )
  url = 'https://www.eporner.com' + Ii11iII1
  I1I ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + OoOOo000o0 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 12 - 12: i11Ii11I1Ii1i . iI1 / OOoOoo00oo
def O00OO0oO ( ) :
 if 25 - 25: ooo0Oo0 % o000o0o00o0Oo * i1Ii
 I1i1I1II = 'http://animeheaven.eu/dubbed.php'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II )
 IIIIii = re . compile ( '<a class=\'gridvan\'(.+?)</a>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   OOOooOO0 = re . compile ( '<div class=\'gridpg\'>(.+?)</div>' ) . findall ( OoO0O00 ) [ 0 ]
   I1i1I1II = re . compile ( "href='(.+?)'>" ) . findall ( OoO0O00 ) [ 0 ]
   I1i1I1II = 'http://animeheaven.eu/' + I1i1I1II
   O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 52 , I1IiI , Oo , '' )
  except : pass
  if 6 - 6: OOoO00o . I1iiiiI1iII * Oooo0000 . i1IIi
def oOOo ( url ) :
 if 46 - 46: I1iiiiI1iII + iIii1I11I1II1 + OOoOoo00oo + i1 . o000o0o00o0Oo
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( "<div class='lisb'>(.+?)<div class='side'>" ) . findall ( Ii11iII1 ) [ 0 ]
 oO0 = re . compile ( "href='(.+?)'><div class='lis'>(.+?)</div>" ) . findall ( IIIIii )
 for url , OOOooOO0 in oO0 :
  url = url . replace ( ' ' , '%20' )
  url = 'http://animeheaven.eu/' + url
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 1 - 1: OOo0o0
def oo00OooO ( url ) :
 if 57 - 57: OOoOoo00oo + iIii1I11I1II1 % i1IIi % iiI1iIiI
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( "<a(.+?)</a>" ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  try :
   OOOooOO0 = re . compile ( "<div class='infoept2'>(.+?)</div>" ) . findall ( OoO0O00 ) [ 0 ]
   OOOooOO0 = 'Episode ' + OOOooOO0
   url = re . compile ( "href='(.+?)'" ) . findall ( OoO0O00 ) [ 0 ]
   url = url . replace ( ' ' , '%20' )
   url = 'http://animeheaven.eu/' + url
   I1IiI = re . compile ( "<img src='(.+?)'" ) . findall ( Ii11iII1 ) [ 0 ]
   I1IiI = 'http://animeheaven.eu/' + I1IiI
   O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  except : pass
  if 83 - 83: i1IIi11111i / i11iIiiIii % iIii1I11I1II1 . iI1 % OOo0o0 . OoooooooOO
def o00oO00 ( url , iconimage ) :
 if 59 - 59: OOoOoo00oo + iIii1I11I1II1 * i1IIi11111i + oOo0 . OOoO00o
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIIii = re . compile ( "document.write\(\"<a class='an'(.+?)</div>" ) . findall ( Ii11iII1 )
 OooOoooOo = 0
 for OoO0O00 in IIIIii :
  OooOoooOo += 1
  url = re . compile ( "href='(.+?)'" ) . findall ( OoO0O00 ) [ 0 ]
  OOOooOO0 = 'Link ' + str ( OooOoooOo )
  I1I ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 49 - 49: OoooooooOO * iI1 - ooo0Oo0 . OOo0o0
def O000o0 ( url ) :
 if 98 - 98: i1 . iI1 % i11Ii11I1Ii1i
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( 'title="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ] . replace ( './' , '/' )
  url = 'http://m4ufree.com' + url
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OoOOo000o0 = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( OoO0O00 ) [ 0 ]
  O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[COLOR yellow] " + OoOOo000o0 + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 71 - 71: oOo0 % i1IIi - i11Ii11I1Ii1i - OOoOoo00oo + OOoOoo00oo * i1Ii
 try :
  I1IiiiiI = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( Ii11iII1 ) [ 0 ]
  II1i11I = re . compile ( '<a.+?href="(.+?)"' ) . findall ( I1IiiiiI ) [ 5 ]
  OoOOO = 'http://m4ufree.com' + II1i11I
  if 'genre' in OoOOO :
   OoOOO = OoOOO . replace ( '.com' , '.com/' )
  o0o00Ooo0o = 'https://i.imgur.com/mjCRjXT.png'
  O00Oo000ooO0 ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , OoOOO , 42 , o0o00Ooo0o , Oo , '' )
 except : pass
 if 76 - 76: i11Ii11I1Ii1i
def Ii1i1i1111 ( url , iconimage ) :
 if 57 - 57: OOooO % i11Ii11I1Ii1i
 import requests
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 O00oOo = re . compile ( 'data="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
 I1111I1II11 = 'http://m4ufree.com/ajax_new.php'
 iiiIIIIiIi = requests . post ( I1111I1II11 , data = { 'm4u' : O00oOo } )
 json = ( iiiIIIIiIi . text )
 Iii = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 IIIII1iii = re . compile ( '{(.+?)}' ) . findall ( Iii )
 IIiiii = 0
 for OooOoooOo in IIIII1iii :
  try :
   IIiiii += 1
   OOOooOO0 = 'Link ' + str ( IIiiii )
   OoOOo000o0 = re . compile ( '''"label":"(.+?)"''' ) . findall ( OooOoooOo ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( OooOoooOo ) [ 0 ]
   I1I ( "[COLOR aqua]" + OOOooOO0 + " | [COLOR yellow] " + OoOOo000o0 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( OooOoooOo ) [ 0 ]
   OoOOo000o0 = re . compile ( """label:.+?'(.+?)'""" ) . findall ( OooOoooOo ) [ 0 ]
   I1I ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + OoOOo000o0 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 37 - 37: i1IIi11111i % i1Ii
def O0II11i11II ( ) :
 if 29 - 29: ooo0Oo0 % i1 % I1iiiiI1iII . i1IIi11111i / OoooooooOO * i1Ii
 I1i1I1II = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<td>(.+?)</td>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  I1i1I1II = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ]
  OO = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  I1i1I1II = 'http://www.livefootballol.me' + I1i1I1II
  O00Oo000ooO0 ( "[COLOR aqua]" + OO + "[/COLOR]" , I1i1I1II , 74 , O0OOO0OOoO0O , Oo , '' )
  if 54 - 54: O0
def OOoO000O00oO ( url ) :
 if 34 - 34: O0
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<a href="(.+?)"' ) . findall ( Ii11iII1 )
 OooOOOo0 = 0
 for i1iIIIi1i in IIIIii :
  if 'acestream' in i1iIIIi1i :
   if 'http' in i1iIIIi1i :
    OooOOOo0 += 1
    OOOooOO0 = '[COLOR aqua]Link :: ' + str ( OooOOOo0 ) + '[/COLOR]'
    I1I ( OOOooOO0 , i1iIIIi1i , 75 , O0OOO0OOoO0O , Oo , '' )
 if OooOOOo0 == 0 :
  I1I ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , O0OOO0OOoO0O , Oo , '' )
  if 54 - 54: OOooO - iI1 - oOo0 . iIii1I11I1II1
def o0OIIiI1I1 ( url ) :
 if 15 - 15: OOooO * ooo0Oo0 % o000o0o00o0Oo * iIii1I11I1II1 - i11iIiiIii
 Ii11iII1 = Oo0O0O0ooO0O ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( Ii11iII1 ) [ 0 ]
 oOooO0 ( OO00Oo , url , O0OOO0OOoO0O )
 if 60 - 60: iiI1iIiI * oOo0 % i1 + OOo0o0
def o0oo ( url , getphp ) :
 iiiIi = urllib2 . Request ( url )
 iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 iiiIi . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 10 )
 Ii11iII1 = IiIIIiI1I1 . read ( )
 IiIIIiI1I1 . close ( )
 return Ii11iII1
 if 80 - 80: oOo0 * Oooo0000 * i11Ii11I1Ii1i - O0 . Oooo0000 % iiI1iIiI
 if 13 - 13: OOo0o0 . iiI1iIiI * OOo0o0 + iiI1iIiI
 if 59 - 59: iiI1iIiI + i11iIiiIii + i1IIi / iI1
def I11 ( ) :
 if 47 - 47: o000o0o00o0Oo / OOo0o0 / OOoO00o
 I1i1I1II = 'http://m4ufree.com/?sort=key_top&page=1&='
 Ii11iII1 = Oo0O0O0ooO0O ( I1i1I1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIIii = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( Ii11iII1 )
 for OoO0O00 in IIIIii :
  OOOooOO0 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( OoO0O00 ) [ 0 ]
  iI1iIIiiii = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00 ) [ 0 ] . replace ( './' , '' )
  I1i1I1II = 'http://m4ufree.com/' + iI1iIIiiii
  if not re . search ( '\d+' , OOOooOO0 ) :
   O00Oo000ooO0 ( "[COLOR aqua]" + OOOooOO0 + "[/COLOR]" , I1i1I1II , 42 , I1IiI , Oo )
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
def O0oO0 ( text ) :
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
 IIiiIIi1 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 ooO000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 oOIII111iiIi1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 29 - 29: OoooooooOO + OOooO % iIii1I11I1II1 - OOoOoo00oo . iiI1iIiI % ooo0Oo0
 I1IIi = 0
 for ( O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( IIiiIIi1 ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( O0OOOo , file )
   I1IIi += os . path . getsize ( iIO0O00OOo )
 i11iIIIIIi1 = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1IIi / ( 1024 * 1024.0 ) )
 I1I ( i11iIIIIIi1 , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 66 - 66: i11iIiiIii / i1IIi11111i - OoooooooOO / i1IIi . i11iIiiIii
 I1IIi = 0
 for ( O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( OoOo0OOOoOo ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( O0OOOo , file )
   I1IIi += os . path . getsize ( iIO0O00OOo )
 i11iIIIIIi1 = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1IIi / ( 1024 * 1024.0 ) )
 I1I ( i11iIIIIIi1 , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 16 - 16: ooo0Oo0 % o000o0o00o0Oo + iI1 - O0 . OOoO00o / oOo0
 I1IIi = 0
 for ( O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( ooO000O ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( O0OOOo , file )
   I1IIi += os . path . getsize ( iIO0O00OOo )
 i11iIIIIIi1 = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1IIi / ( 1024 * 1024.0 ) )
 I1I ( i11iIIIIIi1 , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 35 - 35: OOo0o0 / oOo0 / i11Ii11I1Ii1i - iIii1I11I1II1 + i11Ii11I1Ii1i . oOo0
 I1IIi = 0
 for ( O0OOOo , i11I1I1iiI , I1i1iii1Ii ) in os . walk ( oOIII111iiIi1 ) :
  for file in I1i1iii1Ii :
   iIO0O00OOo = os . path . join ( O0OOOo , file )
   I1IIi += os . path . getsize ( iIO0O00OOo )
 i11iIIIIIi1 = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1IIi / ( 1024 * 1024.0 ) )
 I1I ( i11iIIIIIi1 , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 81 - 81: OOoO00o * OOoOoo00oo - o000o0o00o0Oo * OOooO % Oooo0000 * Oooo0000
 I1I ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 I1I ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 59 - 59: iIii1I11I1II1
def oOooO0 ( name , url , iconimage ) :
 if 7 - 7: OOoOoo00oo * iiI1iIiI / i1IIi11111i * i11iIiiIii
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import urlresolver
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
 if 'acestream' in url :
  iI1iIIiiii = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  OOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  OOoO0 . setPath ( url )
  xbmc . Player ( ) . play ( iI1iIIiiii , OOoO0 , False )
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  OOoO0 = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OOoO0 . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , OOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 else :
  OOoOooOoOOOoo = url
  OOoO0 = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  OOoO0 . setPath ( OOoOooOoOOOoo )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo , OOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 84 - 84: OOoOoo00oo . OOoO00o
def II1i111 ( name , url , iconimage ) :
 if 50 - 50: I1iiiiI1iII % i1IIi
 IIi1I11I1II , iii11II1I = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 IIi1I11I1II += urllib . unquote_plus ( iii11II1I )
 url = regex . resolve ( IIi1I11I1II )
 if 5 - 5: Oooo0000 - I1iiiiI1iII * I1iiiiI1iII
 PLAYREGEX ( name , url , iconimage )
 if 50 - 50: i11Ii11I1Ii1i * o000o0o00o0Oo / OOooO . i1IIi11111i + ooo0Oo0 - OOoOoo00oo
def IIiIiI ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 18 - 18: Oooo0000 % i11iIiiIii % o000o0o00o0Oo / OOo0o0 / i1IIi11111i / i1IIi
def IIi1I1 ( heading , text ) :
 if 28 - 28: o000o0o00o0Oo . i1IIi
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 iIIi = xbmcgui . Window ( id )
 ooO00O00oOO = 50
 while ( ooO00O00oOO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   ooO00O00oOO -= 1
   iIIi . getControl ( 1 ) . setLabel ( heading )
   iIIi . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 40 - 40: OOoO00o . OOo0o0 + iiI1iIiI + o000o0o00o0Oo + oOo0
  if 26 - 26: iIii1I11I1II1
def Oo0O0O0ooO0O ( url ) :
 try :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11iII1 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  Ii11iII1 = Ii11iII1 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return Ii11iII1
 except : quit ( )
 if 87 - 87: o000o0o00o0Oo / OoooooooOO - ooo0Oo0 % Oooo0000 % I1iiiiI1iII % ooo0Oo0
def oooooo0O000o ( url ) :
 try :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11iII1 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  Ii11iII1 = Ii11iII1 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return Ii11iII1
 except : quit ( )
 if 29 - 29: OoooooooOO . iiI1iIiI % o000o0o00o0Oo - OOoO00o
def I1I ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OO0Oo = True
 OOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OOoO0 . setProperty ( "fanart_Image" , fanart )
 OOoO0 . setProperty ( "icon_Image" , iconimage )
 OOoO0 . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOoO0 . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 3 - 3: oOo0 - O0 % iIii1I11I1II1 / I1iiiiI1iII . i1IIi11111i
 o0OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiii , listitem = OOoO0 , isFolder = False )
 return o0OO0Oo
 if 3 - 3: O0 % OoooooooOO / OOoOoo00oo
def Oooo0O0oo00oO ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OO0Oo = True
 OOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 OOoO0 . setProperty ( "fanart_Image" , fanart )
 OOoO0 . setProperty ( "icon_Image" , iconimage )
 OOoO0 . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 89 - 89: i11Ii11I1Ii1i / OOo0o0
 OOoO0 . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 14 - 14: OOoOoo00oo . iiI1iIiI * i1Ii + i11Ii11I1Ii1i - i1Ii + OOoOoo00oo
 o0OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiii , listitem = OOoO0 , isFolder = False )
 return o0OO0Oo
 if 18 - 18: OOo0o0 - i1IIi11111i - iiI1iIiI - iiI1iIiI
def OOooo00 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 i1oO = [ ]
 iIIi1IIi = [ ]
 i111i11I1ii = [ ]
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 i1iIIIi1i = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( Ii11iII1 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1iIIIi1i ) [ 0 ]
 OoO0O00 = re . compile ( '<link>(.+?)</link>' ) . findall ( i1iIIIi1i )
 if len ( OoO0O00 ) < 1 :
  OoO0O00 = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( i1iIIIi1i )
 OooOoooOo = 1
 for OOooo in OoO0O00 :
  oo0 = OOooo
  if '(' in OOooo :
   OOooo = OOooo . split ( '(' ) [ 0 ]
   oOOII1i11i1iIi11 = str ( oo0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   i1oO . append ( OOooo )
   iIIi1IIi . append ( oOOII1i11i1iIi11 )
  else :
   i1oO . append ( OOooo )
   iIIi1IIi . append ( '[COLOR aqua]Link ' + str ( OooOoooOo ) + '[/COLOR]' )
  OooOoooOo = OooOoooOo + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oo0O0oO0O0O = Iii1ii1II11i . select ( name , iIIi1IIi )
 if oo0O0oO0O0O < 0 :
  quit ( )
 else :
  url = i1oO [ oo0O0oO0O0O ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : OOoOooOoOOOoo = liveresolver . resolve ( url )
  else : OOoOooOoOOOoo = url
  OOoO0 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  OOoO0 . setPath ( OOoOooOoOOOoo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoO0 )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( OOoOooOoOOOoo )
  if 69 - 69: OOo0o0 / i11iIiiIii
def OOo00 ( name , url , iconimage ) :
 if 22 - 22: OOo0o0
 ii1ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 i1oO = [ ]
 iIIi1IIi = [ ]
 i111i11I1ii = [ ]
 oOoooO00O = [ ]
 Ii11iII1 = Oo0O0O0ooO0O ( url )
 i1iIIIi1i = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( Ii11iII1 ) [ 0 ]
 OoO0O00 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i1iIIIi1i )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1iIIIi1i ) [ 0 ]
 OooOoooOo = 1
 if 6 - 6: OOooO % i1IIi . OOooO * OOooO
 for OOooo in OoO0O00 :
  oo0 = OOooo
  if '(' in OOooo :
   OOooo = OOooo . split ( '(' ) [ 0 ]
   oOOII1i11i1iIi11 = str ( oo0 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   i1oO . append ( OOooo )
   iIIi1IIi . append ( oOOII1i11i1iIi11 )
   oOoooO00O . append ( 'Stream ' + str ( OooOoooOo ) )
  else :
   i1oO . append ( OOooo )
   iIIi1IIi . append ( 'Link ' + str ( OooOoooOo ) )
   if 81 - 81: OOoOoo00oo / iIii1I11I1II1 + I1iiiiI1iII
  OooOoooOo = OooOoooOo + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oo0O0oO0O0O = Iii1ii1II11i . select ( name , iIIi1IIi )
 if oo0O0oO0O0O < 0 :
  quit ( )
 else :
  I1I1iIiII1 = iIIi1IIi [ oo0O0oO0O0O ]
  i11i1I1 = "/"
  if not I1I1iIiII1 . endswith ( i11i1I1 ) :
   ii1I = I1I1iIiII1 + "/"
  else :
   ii1I = I1I1iIiII1
  url = ii1ii + i1oO [ oo0O0oO0O0O ] + "%26referer=" + ii1I
  print url
  if 49 - 49: OOoOoo00oo / OoooooooOO / iiI1iIiI
  xbmc . Player ( ) . play ( url )
  if 74 - 74: oOo0 % o000o0o00o0Oo
def i1Iiii111iI1iIi1 ( string ) :
 iiIiI = ( c for c in string if 0 < ord ( c ) < 127 )
 if 38 - 38: I1iiiiI1iII . OOooO
 return '' . join ( iiIiI )
 if 24 - 24: i1IIi11111i - i1IIi11111i + o000o0o00o0Oo + iiI1iIiI - OOo0o0
def O00Oo000ooO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 12 - 12: OOoO00o . I1iiiiI1iII . Oooo0000 / O0
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o0OO0Oo = True
 OOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 OOoO0 . setProperty ( "fanart_Image" , fanart )
 OOoO0 . setProperty ( "icon_Image" , iconimage )
 OOoO0 . setInfo ( 'video' , { 'Plot' : description } )
 o0OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiii , listitem = OOoO0 , isFolder = True )
 return o0OO0Oo
 if 58 - 58: i1IIi11111i - i11Ii11I1Ii1i % OOo0o0 + oOo0 . Oooo0000 / I1iiiiI1iII
def II ( name , url , iconimage ) :
 o0OO0Oo = True
 OOoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; OOoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0OO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = OOoO0 )
 xbmc . Player ( ) . play ( url , OOoO0 , False )
 if 94 - 94: iI1 + i11Ii11I1Ii1i % i11iIiiIii
def i1i1IiIiIi1Ii ( ) :
 if 64 - 64: OOoOoo00oo + OoooooooOO * OoooooooOO
 OoOo0OOOoOo = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IIiiIIi1 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 ooO000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 41 - 41: i1Ii . ooo0Oo0 + iiI1iIiI
 OooOoooOo = [ ( OoOo0OOOoOo , 'Cache' ) , ( IIiiIIi1 , 'Thumbnails' ) , ( ooO000O , 'Packages' ) ]
 if 100 - 100: OOooO + i1
 Oo00o0OO = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if Oo00o0OO :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for IIi1I11I1II in OooOoooOo :
   if 73 - 73: i1IIi11111i - iiI1iIiI * i1IIi / i11iIiiIii * OOoOoo00oo % i11Ii11I1Ii1i
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % IIi1I11I1II [ 1 ] )
   time . sleep ( 1 )
   if 56 - 56: OoooooooOO * ooo0Oo0 . ooo0Oo0 . o000o0o00o0Oo
   for II1 , i11I1I1iiI , I1i1iii1Ii in os . walk ( IIi1I11I1II [ 0 ] ) :
    for O00 in I1i1iii1Ii :
     if ( O00 . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( II1 , O00 ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % IIi1I11I1II [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 74 - 74: OoooooooOO % OOoOoo00oo % oOo0 - iiI1iIiI - iI1
def o0 ( url , mode , name , iconimage , fanart ) :
 if 35 - 35: I1iiiiI1iII + i1IIi * OOo0o0 - OOooO . ooo0Oo0
 with open ( I11i , "a" ) as iIi :
  iIi . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 31 - 31: i1IIi11111i
def Ii1IIiiIiiIi ( ) :
 if 40 - 40: i1IIi11111i
 with open ( I11i , "a" ) as iIi :
  oOOo0oo0o0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  iIii1 = open ( oOOo0oo0o0o0 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIIii = re . compile ( '<item>(.+?)</item>' ) . findall ( iIii1 )
  I1I ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  I1I ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  if len ( IIIIii ) < 1 :
   I1I ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  for Ooo0oO0 in IIIIii :
   OOOooOO0 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1i1I1II = re . compile ( '<url>(.+?)</url>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1I ( '[COLOR skyblue]' + OOOooOO0 + '[/COLOR]' , I1i1I1II , 2 , I1IiI , I1ii11iIi11i )
   if 86 - 86: O0
 I1I ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , O0OOO0OOoO0O , Oo )
 if 95 - 95: OOoO00o * OOoOoo00oo . Oooo0000 . i1IIi . i1IIi - i1IIi11111i
def ii1iIIiii1 ( ) :
 if 62 - 62: OOoOoo00oo
 with open ( IiII , "a" ) as iIi :
  oOOo0oo0o0o0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  iIii1 = open ( oOOo0oo0o0o0 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIIii = re . compile ( '<item>(.+?)</item>' ) . findall ( iIii1 )
  I1I ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  I1I ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  if len ( IIIIii ) < 1 :
   I1I ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , O0OOO0OOoO0O , Oo )
  for Ooo0oO0 in IIIIii :
   OOOooOO0 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1i1I1II = re . compile ( '<link>(.+?)</link>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ooo0oO0 ) [ 0 ]
   I1I ( '[COLOR skyblue]' + OOOooOO0 + '[/COLOR]' , I1i1I1II , 2 , I1IiI , I1ii11iIi11i )
   if 1 - 1: I1iiiiI1iII / I1iiiiI1iII - i11iIiiIii
 I1I ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , O0OOO0OOoO0O , Oo )
 if 87 - 87: ooo0Oo0 / O0 * I1iiiiI1iII / i1IIi11111i
def I1iiIII ( ) :
 if 16 - 16: OOo0o0 + i1Ii / i1IIi11111i
 with open ( I11i , "w" ) as iIi :
  iIi . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 82 - 82: I1iiiiI1iII * i11iIiiIii % i11Ii11I1Ii1i - OoooooooOO
def OO0Ooo0 ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as iIi :
  iIi . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 91 - 91: i1IIi - iIii1I11I1II1
 if 55 - 55: iiI1iIiI * i1IIi11111i % i1Ii . iIii1I11I1II1 * oOo0
 if 92 - 92: oOo0 - iIii1I11I1II1
def iI ( ) :
 if 32 - 32: OOooO % i1 * i1 + I1iiiiI1iII * i11Ii11I1Ii1i * OOooO
 o00O00O0O0O = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iIiIii1I1II = re . compile ( '<pin>(.+?)</pin>' ) . findall ( o00O00O0O0O ) [ 0 ]
  if iIiIii1I1II == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]http://streamarmy.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok, This takes less than a minute and helps pay for servers!!\n[COLOR red]This is only required once every 4 hours[/COLOR]" )
   O0O0Oo00 = ''
   oOoO00o = xbmc . Keyboard ( O0O0Oo00 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   oOoO00o . doModal ( )
   if oOoO00o . isConfirmed ( ) :
    O0O0Oo00 = oOoO00o . getText ( )
    if len ( O0O0Oo00 ) > 1 :
     oO00O0 = O0O0Oo00 . title ( )
     with open ( iI1Ii11111iIi , "w" ) as O00 :
      O00 . write ( "<pin>" + oO00O0 + "</pin>" )
     iI ( )
    else : quit ( )
   else : quit ( )
  if not 'EXPIRED' in iIiIii1I1II :
   O0Oooo = re . compile ( '<pin>(.+?)</pin>' ) . findall ( o00O00O0O0O ) [ 0 ]
   oO000 = ( 'http://www.streamarmy.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % O0Oooo )
   Ii11iII1 = Oo0O0O0ooO0O ( oO000 )
   if 'Pin Verified' in Ii11iII1 :
    pass
   else :
    with open ( iI1Ii11111iIi , "w" ) as O00 :
     O00 . write ( '<pin>EXPIRED</pin>' )
     iI ( )
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as O00 :
   O00 . write ( "<pin>EXPIRED</pin>\n" )
  iI ( )
  if 7 - 7: I1iiiiI1iII * iiI1iIiI + i1IIi + i11iIiiIii + ooo0Oo0 % iiI1iIiI
  if 62 - 62: i1IIi11111i - OOooO * Oooo0000 - i11iIiiIii % i1Ii
  if 52 - 52: o000o0o00o0Oo % OOo0o0 - i11iIiiIii
  if 30 - 30: OOoO00o / i1 + OOo0o0
def I1Io00oOOoO0oO ( url , iconimage , fanart ) :
 if 26 - 26: OOooO * iIii1I11I1II1 % i1 . i1IIi11111i + ooo0Oo0
 try :
  O0O0Oo00 = ''
  oOoO00o = xbmc . Keyboard ( O0O0Oo00 , 'Enter Name To Save File As' )
  oOoO00o . doModal ( )
  if oOoO00o . isConfirmed ( ) :
   O0O0Oo00 = oOoO00o . getText ( )
   if len ( O0O0Oo00 ) > 1 :
    oO00O0 = O0O0Oo00 . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   OOoOooOoOOOoo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = OOoOooOoOOOoo
  OOO00OOo0o0Oo = url . split ( '/' ) [ - 1 ]
  iiii = urllib2 . urlopen ( url )
  ooooOoO0O = os . path . join ( o0OOO , oO00O0 )
  O00 = open ( ooooOoO0O , 'wb' )
  if 1 - 1: o000o0o00o0Oo / i1 + OOo0o0 . i1IIi11111i / o000o0o00o0Oo - OOoO00o
  ii111i1iI = iiii . info ( )
  I1I1iII1i = int ( ii111i1iI . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( oO00O0 , I1I1iII1i ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 30 - 30: O0 + o000o0o00o0Oo + i11Ii11I1Ii1i
  III1I = 0
  I1I111iIi = 8192
  while True :
   buffer = iiii . read ( I1I111iIi )
   if not buffer :
    break
    if 53 - 53: iIii1I11I1II1 + i1IIi11111i - Oooo0000 - OOo0o0 / i1Ii % i11iIiiIii
   III1I += len ( buffer )
   O00 . write ( buffer )
   I11oOOooo = "[%3.2f%%]" % ( III1I * 100. / I1I1iII1i )
   I11oOOooo = I11oOOooo + chr ( 8 ) * ( len ( I11oOOooo ) + 1 )
   iIiiiI . update ( III1I , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( I11oOOooo , oO00O0 ) )
   if 80 - 80: iiI1iIiI - i11iIiiIii
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as iIi :
   iIi . write ( '<item>\n<title>' + oO00O0 + '</title>\n<link>' + ooooOoO0O + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 69 - 69: OOo0o0 % OoooooooOO . iiI1iIiI
  O00 . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 34 - 34: OOooO * Oooo0000 - I1iiiiI1iII - iiI1iIiI - OOooO
  if 42 - 42: i11Ii11I1Ii1i * iiI1iIiI % i1IIi - OOooO % I1iiiiI1iII
  if 36 - 36: i11iIiiIii / OOo0o0 * o000o0o00o0Oo * o000o0o00o0Oo + OOooO * iI1
  if 32 - 32: i1
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
  for OooOoooOo in range ( len ( iII1 ) ) :
   O000O = { }
   O000O = iII1 [ OooOoooOo ] . split ( '=' )
   if ( len ( O000O ) ) == 2 :
    oOo0O0o0000o0O0 [ O000O [ 0 ] ] = O000O [ 1 ]
 return oOo0O0o0000o0O0
 if 98 - 98: iIii1I11I1II1 + oOo0 % Oooo0000 + iI1 % Oooo0000
iIiiiIiIii1ii = i1iii11 ( ) ; I1i1I1II = None ; OO00Oo = None ; iI1I1I11IiII = None ; iIii11iI1II = None ; O0OOO0OOoO0O = None ; I1II1I1I = None
try : iIii11iI1II = urllib . unquote_plus ( iIiiiIiIii1ii [ "site" ] )
except : pass
try : I1i1I1II = urllib . unquote_plus ( iIiiiIiIii1ii [ "url" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( iIiiiIiIii1ii [ "name" ] )
except : pass
try : iI1I1I11IiII = int ( iIiiiIiIii1ii [ "mode" ] )
except : pass
try : O0OOO0OOoO0O = urllib . unquote_plus ( iIiiiIiIii1ii [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( iIiiiIiIii1ii [ "fanart" ] )
except : pass
try : I1II1I1I = urllib . unquote_plus ( iIiiiIiIii1ii [ "description" ] )
except : pass
if 79 - 79: OOoOoo00oo / oOo0 . Oooo0000 - o000o0o00o0Oo
if iI1I1I11IiII == None or I1i1I1II == None or len ( I1i1I1II ) < 1 : i1iiI11I ( )
if 47 - 47: OoooooooOO % O0 * OOoO00o . OOooO
if 38 - 38: O0 - I1iiiiI1iII % oOo0
if 64 - 64: iIii1I11I1II1
if 15 - 15: o000o0o00o0Oo + OOoOoo00oo / o000o0o00o0Oo / oOo0
if 31 - 31: i1Ii + O0 + i1Ii . iIii1I11I1II1 + ooo0Oo0 / i1IIi11111i
elif iI1I1I11IiII == 1 : I1111I1iII11 ( OO00Oo , I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 2 : oOooO0 ( OO00Oo , I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 3 : OOooo00 ( OO00Oo , I1i1I1II , O0OOO0OOoO0O )
if 6 - 6: ooo0Oo0 % I1iiiiI1iII * iI1 / iiI1iIiI + ooo0Oo0
if 39 - 39: Oooo0000 - ooo0Oo0 / OOoO00o * OoooooooOO
if 100 - 100: O0 . iI1 . i1 + O0 * OOo0o0
elif iI1I1I11IiII == 4 : o0o ( I1i1I1II )
elif iI1I1I11IiII == 5 : I1111IIi ( I1i1I1II )
elif iI1I1I11IiII == 6 : oOOoo00O00o ( )
elif iI1I1I11IiII == 7 : O0O0ooOOO ( I1i1I1II )
elif iI1I1I11IiII == 8 : iIi1ii ( I1i1I1II )
elif iI1I1I11IiII == 9 : i1OOoO ( I1i1I1II )
elif iI1I1I11IiII == 10 : IIiIiI ( I1i1I1II )
elif iI1I1I11IiII == 11 : o0o0O0O00oOOo ( )
elif iI1I1I11IiII == 12 : o0O0o0 ( I1i1I1II )
elif iI1I1I11IiII == 13 : ooooo0O0000oo ( I1i1I1II )
elif iI1I1I11IiII == 14 : oo0oO ( I1i1I1II )
elif iI1I1I11IiII == 15 : ooO0O00Oo0o ( )
elif iI1I1I11IiII == 16 : OOo00 ( OO00Oo , I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 17 : O0o ( I1i1I1II )
elif iI1I1I11IiII == 18 : oOooOo0 ( I1i1I1II )
elif iI1I1I11IiII == 19 : iIiIIi1 ( I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 20 : I1i1Iiiii ( )
elif iI1I1I11IiII == 21 : iI1i11iII111 ( I1i1I1II )
elif iI1I1I11IiII == 22 : II1i111Ii1i ( I1i1I1II )
elif iI1I1I11IiII == 23 : I1ii1iIiii1I ( )
elif iI1I1I11IiII == 24 : OoO ( I1i1I1II )
elif iI1I1I11IiII == 25 : o0OoOo00o0o ( I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 26 : o0O ( I1i1I1II )
elif iI1I1I11IiII == 27 : ooOoOo0 ( I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 28 : Oo0oooO0oO ( )
elif iI1I1I11IiII == 29 : iiIi1i ( I1i1I1II )
elif iI1I1I11IiII == 30 : ooo0OOO ( I1i1I1II )
elif iI1I1I11IiII == 31 : iII1iiiiIII ( I1i1I1II )
elif iI1I1I11IiII == 32 : O0OI11iiiii1II ( I1i1I1II )
elif iI1I1I11IiII == 33 : o0oo0 ( I1i1I1II )
elif iI1I1I11IiII == 34 : OooOOOO ( I1i1I1II )
elif iI1I1I11IiII == 35 : Ii1II ( )
elif iI1I1I11IiII == 36 : ii1iiIi1 ( I1i1I1II )
elif iI1I1I11IiII == 37 : I1iOOOO ( I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 38 : III ( )
elif iI1I1I11IiII == 39 : IIiIiI1I ( I1i1I1II )
elif iI1I1I11IiII == 40 : I1i1Iiiii ( )
elif iI1I1I11IiII == 41 : iI1i11iII111 ( I1i1I1II )
elif iI1I1I11IiII == 42 : O000o0 ( I1i1I1II )
elif iI1I1I11IiII == 43 : Ii1i1i1111 ( I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 44 : I11 ( )
if 42 - 42: OOo0o0 % OoooooooOO + i1IIi11111i
elif iI1I1I11IiII == 45 : II11iI111i1 ( )
elif iI1I1I11IiII == 46 : OoO00 ( I1i1I1II )
elif iI1I1I11IiII == 47 : Ooooooo ( OO00Oo , I1i1I1II , O0OOO0OOoO0O )
elif iI1I1I11IiII == 48 : ooo0O ( )
elif iI1I1I11IiII == 49 : oO0oO0 ( I1i1I1II )
elif iI1I1I11IiII == 50 : IIi1ii1Ii ( I1i1I1II )
elif iI1I1I11IiII == 51 : O00OO0oO ( )
elif iI1I1I11IiII == 52 : oOOo ( I1i1I1II )
elif iI1I1I11IiII == 53 : oo00OooO ( I1i1I1II )
elif iI1I1I11IiII == 54 : o00oO00 ( I1i1I1II , O0OOO0OOoO0O )
if 56 - 56: OoooooooOO + o000o0o00o0Oo - OOoO00o
if 24 - 24: i1IIi11111i + i1Ii + iI1 - iIii1I11I1II1
if 49 - 49: iI1 . i1Ii * Oooo0000 % I1iiiiI1iII . O0
elif iI1I1I11IiII == 59 : o0o0O00oo0 ( )
elif iI1I1I11IiII == 60 : ooOOo00O00Oo ( I1i1I1II )
elif iI1I1I11IiII == 61 : OoOoOo00o0 ( OO00Oo , I1i1I1II , O0OOO0OOoO0O )
if 48 - 48: O0 * OOooO - O0 / OOooO + Oooo0000
elif iI1I1I11IiII == 66 : iI1iIIIi1i ( )
elif iI1I1I11IiII == 67 : iIiii ( I1i1I1II )
elif iI1I1I11IiII == 68 : O00oO ( I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 69 : OoOIii11iI11i1I ( I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 70 : ii1IIIIiI11 ( I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 71 : o00 ( )
elif iI1I1I11IiII == 72 : I1iii ( )
elif iI1I1I11IiII == 73 : O0II11i11II ( )
elif iI1I1I11IiII == 74 : OOoO000O00oO ( I1i1I1II )
elif iI1I1I11IiII == 75 : o0OIIiI1I1 ( I1i1I1II )
if 52 - 52: i1 % OOooO * i11Ii11I1Ii1i
if 4 - 4: iI1 % O0 - OoooooooOO + i1Ii . OOo0o0 % i11Ii11I1Ii1i
elif iI1I1I11IiII == 884 : oooo0OOo ( )
elif iI1I1I11IiII == 885 : OO0Ooo0 ( )
elif iI1I1I11IiII == 886 : ii1iIIiii1 ( )
elif iI1I1I11IiII == 887 : I1Io00oOOoO0oO ( I1i1I1II , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 888 : IiiiiI1i1Iii ( )
elif iI1I1I11IiII == 889 : o0 ( I1i1I1II , iI1I1I11IiII , OO00Oo , O0OOO0OOoO0O , I1ii11iIi11i )
elif iI1I1I11IiII == 890 : Ii1IIiiIiiIi ( )
elif iI1I1I11IiII == 891 : I1iiIII ( )
elif iI1I1I11IiII == 892 : i1i1IiIiIi1Ii ( )
if 9 - 9: i11Ii11I1Ii1i * i11Ii11I1Ii1i . i11iIiiIii * iIii1I11I1II1
if iI1I1I11IiII == None or I1i1I1II == None or len ( I1i1I1II ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
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
