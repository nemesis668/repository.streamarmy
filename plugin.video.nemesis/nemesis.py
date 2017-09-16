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
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.nemesis'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = base64 . b64decode ( b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3LzBFVlFkS3l4' )
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
 iI = i1iII1IiiIiI1
 I1i1I1II = iI
 try :
  iiiIi = urllib2 . Request ( 'http://streamarmy.co.uk/dapi.php' )
  iiiIi . add_header ( 'User-Agent' , 'StreamArmy' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 3 )
  OoO000 = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  i1IiIiiI ( '[COLOR yellow]' + OoO000 + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
 except : pass
 I1I = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 oOO00oOO = int ( datetime . now ( ) . strftime ( '%d' ) )
 o00O00O0O0O = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OooO0OO = re . compile ( '<date>(.+?)</date>' ) . findall ( o00O00O0O0O ) [ 0 ]
 if str ( OooO0OO ) != str ( oOO00oOO ) :
  iI111iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.nemesis/intro.mp4' ) )
  with open ( iI1Ii11111iIi , "w" ) as iIi :
   iIi . write ( '<date>' + str ( oOO00oOO ) + '</date>\n' )
   xbmc . Player ( ) . play ( iI111iI , xbmcgui . ListItem ( 'Welcome to Nemesis' ) )
 if ( I1I >= 0000 ) and ( I1I <= 1159 ) : OoOo = "Morning"
 elif ( I1I >= 1200 ) and ( I1I <= 1759 ) : OoOo = "Afternoon"
 else : OoOo = "Evening"
 i1IiIiiI ( '[COLOR yellow]Good[COLOR aqua] ' + str ( OoOo ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 i1IiIiiI ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  if 18 - 18: i11iIiiIii
  Ii11I = OOO0OOO00oo ( i1iII1IiiIiI1 )
  Iii111II = re . compile ( '<item>(.+?)</item>' ) . findall ( Ii11I )
  for iiii11I in Iii111II :
   try :
    if '<m3u>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 11 , ii11i1 , I1ii11iIi11i )
    elif '<mamahdsports>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 14 , ii11i1 , I1ii11iIi11i )
    elif '<atc>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<atc>(.+?)</atc>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 6 , ii11i1 , I1ii11iIi11i )
    elif '<scanner>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 11 , ii11i1 , I1ii11iIi11i )
    elif '<cartoons>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 29 , ii11i1 , I1ii11iIi11i )
    elif '<Adult>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 38 , ii11i1 , I1ii11iIi11i )
    elif '<Anime>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 51 , ii11i1 , I1ii11iIi11i )
    elif '<audiobooks>' in iiii11I :
     Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     iI = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( iiii11I ) [ 0 ]
     IIIii1II1II ( Ooo0OO0oOO , iI , 59 , ii11i1 , I1ii11iIi11i )
    elif '<folder>' in iiii11I :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iiii11I )
     for Ooo0OO0oOO , iI , ii11i1 , I1ii11iIi11i in OoO000 :
      IIIii1II1II ( Ooo0OO0oOO , iI , 1 , ii11i1 , I1ii11iIi11i )
    else :
     i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( iiii11I )
     if len ( i1I1iI ) == 1 :
      OoO000 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iiii11I )
      oo0OooOOo0 = len ( Iii111II )
      for Ooo0OO0oOO , iI , ii11i1 , I1ii11iIi11i in OoO000 :
       if 'youtube.com/playlist' in iI :
        IIIii1II1II ( Ooo0OO0oOO , iI , 2 , ii11i1 , I1ii11iIi11i )
       else :
        i1IiIiiI ( Ooo0OO0oOO , iI , 2 , ii11i1 , I1ii11iIi11i )
     elif len ( i1I1iI ) > 1 :
      Ooo0OO0oOO = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
      ii11i1 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
      i1IiIiiI ( Ooo0OO0oOO , I1i1I1II , 3 , ii11i1 , I1ii11iIi11i )
   except : pass
   if 92 - 92: OOoO00o . iI1 + i1IIi11111i
  i1IiIiiI ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.urlresolver/settings.xml" )
   OoOo = open ( file ) . read ( )
   IiII1I11i1I1I = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( OoOo ) [ 0 ]
   IiII1I11i1I1I = IiII1I11i1I1I . strip ( )
   iI = 'plugin://script.module.urlresolver/?mode=auth_rd'
   if 'value=""' in IiII1I11i1I1I :
    oO0Oo = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    i1IiIiiI ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( oO0Oo ) + '[/COLOR]' , iI , 2 , I1IiI , Oo )
   else :
    oO0Oo = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    i1IiIiiI ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( oO0Oo ) + '[/COLOR]' , 'url' , 999 , icondeb , Oo )
  except : pass
  oOOoo0Oo = 'https://i.imgur.com/4Pzgdwu.png'
  IIIii1II1II ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , oOOoo0Oo , Oo )
  o00OO00OoO = 'https://i.imgur.com/Om0Lq7V.png'
  IIIii1II1II ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , o00OO00OoO , Oo )
  OOOO0OOoO0O0 = 'https://i.imgur.com/klnhdFx.png'
  IIIii1II1II ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , OOOO0OOoO0O0 , Oo )
 except :
  O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if O0Oo000ooO00 == 0 :
   i1IiIiiI ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   IIIii1II1II ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if O0Oo000ooO00 == 1 :
   quit ( )
   if 75 - 75: OOo0o0 . i1 * OOoOoo00oo
 iI11i1I1 ( )
 if 91 - 91: OOooO
def iII ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 I1i1I1II = url
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<item>(.+?)</item>' ) . findall ( Ii11I )
 for iiii11I in Iii111II :
  try :
   if '<image>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 23 , iconimage , fanart )
   elif '<American>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 49 , iconimage , fanart )
   elif '<lordjd>' in iiii11I :
    i1I1iI = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( iiii11I )
    if len ( i1I1iI ) == 1 :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iiii11I )
     oo0OooOOo0 = len ( Iii111II )
     for name , url , iconimage , fanart in OoO000 :
      if 'youtube.com/playlist' in url :
       IIIii1II1II ( name , url , 2 , iconimage , fanart )
      else :
       o0 ( name , url , 2 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     o0 ( name , I1i1I1II , 3 , iconimage , fanart )
   elif '<reddit>' in iiii11I :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( iiii11I ) [ 0 ]
    IIIii1II1II ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in iiii11I :
    i1I1iI = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( iiii11I )
    if len ( i1I1iI ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( iiii11I ) [ 0 ]
     ooOooo000oOO = re . compile ( '<referer>(.+?)</referer>' ) . findall ( iiii11I ) [ 0 ]
     Oo0oOOo = ooOooo000oOO
     Oo0OoO00oOO0o = "/"
     if not Oo0oOOo . endswith ( Oo0OoO00oOO0o ) :
      OOO00O = Oo0oOOo + "/"
     else :
      OOO00O = Oo0oOOo
     Ii11I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = Ii11I + '%26referer=' + OOO00O
     i1IiIiiI ( name , url , 10 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     i1IiIiiI ( name , I1i1I1II , 16 , iconimage , fanart )
     if 84 - 84: OOo0o0 * i1 / iI1 - O0
   elif '<folder>' in iiii11I :
    OoO000 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iiii11I )
    for name , url , iconimage , fanart in OoO000 :
     IIIii1II1II ( name , url , 1 , iconimage , fanart )
     if 30 - 30: iIii1I11I1II1 / i1Ii - oOo0 - i11Ii11I1Ii1i % OOoO00o
   else :
    i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( iiii11I )
    if len ( i1I1iI ) == 1 :
     OoO000 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iiii11I )
     oo0OooOOo0 = len ( Iii111II )
     for name , url , iconimage , fanart in OoO000 :
      if 'youtube.com/playlist' in url :
       IIIii1II1II ( name , url , 2 , iconimage , fanart )
      else :
       i1IiIiiI ( name , url , 2 , iconimage , fanart )
    elif len ( i1I1iI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( iiii11I ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iiii11I ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iiii11I ) [ 0 ]
     i1IiIiiI ( name , I1i1I1II , 3 , iconimage , fanart )
  except : pass
  if 49 - 49: iiI1iIiI % i1Ii . i1Ii . iI1 * i1Ii
 iI11i1I1 ( )
 if 97 - 97: OOooO + i1IIi11111i . OOoOoo00oo + o000o0o00o0Oo % OOoO00o
 if 95 - 95: i1IIi
 if 3 - 3: oOo0 - O0 / oOo0 % i1 / oOo0 . iiI1iIiI
 if 50 - 50: I1iiiiI1iII
 if 14 - 14: iI1 % i1 * iI1
 if 16 - 16: Oooo0000 . i1Ii + i11iIiiIii
 if 38 - 38: I1iiiiI1iII * OOoOoo00oo . i1IIi11111i
 if 98 - 98: OoooooooOO + OOoO00o . Oooo0000
def Oo0ooOo0o ( url ) :
 if 22 - 22: iIii1I11I1II1 / i11iIiiIii * iIii1I11I1II1 * i11Ii11I1Ii1i . OOoOoo00oo / i11iIiiIii
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   Iiii = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   IIIii1II1II ( "[COLOR skyblue]" + Iiii + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 75 - 75: Oooo0000 % i1IIi11111i % i1IIi11111i . oOo0
def III1iII1I1ii ( url ) :
 if 61 - 61: i11Ii11I1Ii1i
 O0OOO = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 II11iIiIIIiI = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 i1IiIiiI ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 Ii11I = OOO0OOO00oo ( url )
 i1I1iI = 0
 o0o = re . compile ( 'href="([^"]+)' ) . findall ( Ii11I )
 for url in o0o :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in O0OOO ) :
    i1I1iI += 1
    Iiii = "Link " + str ( i1I1iI ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    o00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     i1IiIiiI ( "[COLOR skyblue]" + Iiii + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in II11iIiIIIiI ) :
     i1IiIiiI ( "[COLOR yellow]" + Iiii + url + "[/COLOR]" , o00 , 2 , I1IiI , I1ii11iIi11i )
    else :
     i1IiIiiI ( "[COLOR skyblue]" + Iiii + url + "[/COLOR]" , o00 , 2 , I1IiI , I1ii11iIi11i )
     if 56 - 56: iiI1iIiI - ooo0Oo0 . OOooO - I1iiiiI1iII
     if 73 - 73: ooo0Oo0 - i1IIi - i1IIi - OOoO00o . OOooO + o000o0o00o0Oo
     if 81 - 81: OOoO00o * OOo0o0 - oOo0 . i11Ii11I1Ii1i % iI1 / iiI1iIiI
def iIIiIi1iIII1 ( url ) :
 if 78 - 78: O0 . OOo0o0 . i11Ii11I1Ii1i % OOoOoo00oo
 if url == 'Football' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  i1iIi = OOO0OOO00oo ( 'http://wizhdsports.is/sport/Cricket' )
 ooOOoooooo = dom_parser2 . parse_dom ( i1iIi , 'div' , { 'class' : 'card' } )
 ooOOoooooo = [ ( dom_parser2 . parse_dom ( II1I , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( II1I , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( II1I , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( II1I , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for II1I in ooOOoooooo ]
 if len ( ooOOoooooo ) < 1 :
  i1IiIiiI ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , ii11i1 , Oo , '' )
 ooOOoooooo = [ ( II1I [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , II1I [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , II1I [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , II1I [ 2 ] [ 0 ] . content ) if II1I [ 2 ] else 'Upcoming' , II1I [ 3 ] [ 0 ] . content ) for II1I in ooOOoooooo ]
 if 84 - 84: I1iiiiI1iII . i11iIiiIii . I1iiiiI1iII * o000o0o00o0Oo - iI1
 if 42 - 42: i11iIiiIii
 if 33 - 33: OOoO00o - O0 * i1IIi * i1IIi11111i - ooo0Oo0
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - i1IIi11111i
 ooOOoooooo = [ ( II1I [ 0 ] , II1I [ 1 ] , II1I [ 2 ] , II1I [ 3 ] , II1I [ 4 ] ) for II1I in ooOOoooooo ]
 o00oooO0Oo = 0
 o0O0OOO0Ooo = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for II1I in ooOOoooooo :
  iiIiI = II1I [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( o00oooO0Oo ) )
  o00oooO0Oo += 1
  time . sleep ( 0.10 )
  iiIiI = I1 ( iiIiI )
  OOO00O0O = II1I [ 1 ]
  iii = II1I [ 3 ]
  if 'Match Over' in iii :
   o0O0OOO0Ooo += 1
  oOooOOOoOo = dom_parser2 . parse_dom ( II1I [ 4 ] , 'a' )
  for i1iIi in oOooOOOoOo :
   i1Iii1i1I = re . sub ( '<.+?>' , '' , i1iIi . content )
   Ii11I = i1iIi . attrs [ 'href' ]
   Ii11I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + Ii11I
   if not 'Match Over' in iii :
    i1IiIiiI ( '[COLOR aqua]' + iiIiI + '[COLOR yellow]' + ' ' + iii + '[/COLOR]' , Ii11I , 2 , ii11i1 , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( o00oooO0Oo ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( o0O0OOO0Ooo ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 91 - 91: o000o0o00o0Oo + iiI1iIiI . OOoOoo00oo * o000o0o00o0Oo + iiI1iIiI * ooo0Oo0
def O000OOOOOo ( url ) :
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * OOoO00o % i11iIiiIii * iiI1iIiI
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = re . compile ( 'title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  if 77 - 77: ooo0Oo0
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 17 - 17: OOoO00o % i1 . OOoOoo00oo + i1 / i11Ii11I1Ii1i
 try :
  oo0O0O00 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( Ii11I ) [ 0 ]
  I1IiI = ii11i1
  IIIii1II1II ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , oo0O0O00 , 18 , ii11i1 , Oo , '' )
 except : pass
 if 47 - 47: i1IIi11111i + i1Ii
def OoO ( url , iconimage , fanart ) :
 if 88 - 88: OOoO00o . i11Ii11I1Ii1i * i11Ii11I1Ii1i % oOo0
 i1IiIiiI ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( Ii11I )
 if 15 - 15: i1IIi * iiI1iIiI + i11iIiiIii
 for i1I1iI in Iii111II :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  o00 = str . lower ( url )
  if '1e' in o00 :
   Iiii = '1st Half'
  else :
   Iiii = '2nd Half'
  i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 6 - 6: i1Ii / i11iIiiIii + OOoO00o * OOo0o0
def o00o0 ( ) :
 if 45 - 45: O0
 iI = 'http://www.goalsarena.org/en/'
 Ii11I = OOO0OOO00oo ( iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( Iii111II )
 for o0O , IiIIii1iII1II in I1IiiiiI :
  IIIii1II1II ( "[COLOR skyblue]" + IiIIii1iII1II + "[/COLOR]" , o0O , 21 , I1IiI , Oo , '' )
  if 48 - 48: i11Ii11I1Ii1i * OOooO . iI1 + OOo0o0
def OoO0o ( url ) :
 if 78 - 78: OOo0o0 % O0 % OOooO
 if 46 - 46: OoooooooOO . i11iIiiIii
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if O0Oo000ooO00 == 0 :
  Iii111II = re . compile ( '<iframe src="(.+?)"' ) . findall ( Ii11I ) [ 0 ]
  OOo0oO00ooO00 = OOO0OOO00oo ( Iii111II )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOo0oO00ooO00 ) [ 0 ]
  url = 'https:' + url
  oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = ii11i1 , thumbnailImage = ii11i1 )
  xbmc . Player ( ) . play ( url , oOO0O00oO0Ooo , False )
  quit ( 0 )
 if O0Oo000ooO00 == 1 :
  try :
   Iii111II = re . compile ( '<iframe src="(.+?)"' ) . findall ( Ii11I ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   OoO0o ( url )
  OOo0oO00ooO00 = OOO0OOO00oo ( Iii111II )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( OOo0oO00ooO00 ) [ 0 ]
  url = 'https:' + url
  oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = ii11i1 , thumbnailImage = ii11i1 )
  xbmc . Player ( ) . play ( url , oOO0O00oO0Ooo , False )
  quit ( 0 )
  if 67 - 67: i1 - OOoOoo00oo
def iI1i11iII111 ( ) :
 if 15 - 15: i11iIiiIii % OOooO . ooo0Oo0 + o000o0o00o0Oo
 iI = 'http://m.liveatc.net/feeds/'
 Ii11I = OO0OOOOoo0OOO ( iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  iI = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'http://m.liveatc.net' + iI
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , iI , 7 , I1IiI , Oo , '' )
  if 27 - 27: i1Ii + i11Ii11I1Ii1i
def o0Oo00 ( url ) :
 if 32 - 32: i1IIi11111i . I1iiiiI1iII * iI1
 if 93 - 93: i1IIi11111i % i1IIi . OOooO . i11iIiiIii
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 56 - 56: o000o0o00o0Oo % O0 - iiI1iIiI
def O00o0OO0 ( url ) :
 url = url . replace ( ' ' , '%20' )
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li>(.+?)</a>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '(.+?)</li>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 35 - 35: OOo0o0 % i1Ii / oOo0 + iIii1I11I1II1 . OoooooooOO . iiI1iIiI
def o00oOOooOOo0o ( url ) :
 if 66 - 66: OOoO00o - OOoO00o - i11iIiiIii . o000o0o00o0Oo - OOoOoo00oo
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li>(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   i1IiIiiI ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 77 - 77: Oooo0000 - i11Ii11I1Ii1i - i1Ii
def IiiiIIiIi1 ( ) :
 if 74 - 74: iIii1I11I1II1 * o000o0o00o0Oo + Oooo0000 / i1IIi / i11Ii11I1Ii1i . ooo0Oo0
 IIIii1II1II ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 iI = 'http://m.broadcastify.com/?a=la&coid=1'
 Ii11I = OO0OOOOoo0OOO ( iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  iI = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'http://m.broadcastify.com' + iI
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , iI , 12 , I1IiI , Oo , '' )
  if 62 - 62: OoooooooOO * iiI1iIiI
def oOOOoo0O0oO ( url ) :
 if 6 - 6: OOoOoo00oo * i1IIi11111i + OOoO00o
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 44 - 44: OOooO % i1 + OoooooooOO - O0 - OOooO - i11Ii11I1Ii1i
def O0Oo0oOOoooOOOOo ( url ) :
 if 62 - 62: i1Ii
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 74 - 74: OOoO00o + i1IIi11111i
def oO00O000oO0 ( url ) :
 if 79 - 79: iI1 - OoooooooOO - OOo0o0 - iIii1I11I1II1 * OOoOoo00oo
 Ii11I = OO0OOOOoo0OOO ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  Iii111II = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( Ii11I ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 Iii ( Iii111II )
 if 16 - 16: OOooO + I1iiiiI1iII * O0 % i1IIi . iiI1iIiI
def Oo0OO ( ) :
 if 78 - 78: OOoOoo00oo - OoooooooOO - o000o0o00o0Oo / i1Ii / i11Ii11I1Ii1i
 iI = 'http://m.broadcastify.com/?a=top25'
 Ii11I = OO0OOOOoo0OOO ( iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  iiI11ii1I1 = Iiii . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  Iiii = Iiii . split ( ')' ) [ - 1 ] . strip ( )
  iI = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'http://m.broadcastify.com' + iI
  i1IiIiiI ( "[COLOR aqua]" + Iiii + "[COLOR yellow] :: " + iiI11ii1I1 + " Listening" + "[/COLOR]" , iI , 14 , I1IiI , Oo , '' )
  if 82 - 82: i11Ii11I1Ii1i % iI1 / i1 + Oooo0000 / i1IIi11111i / oOo0
def oOo0OOoO0 ( url ) :
 if 11 - 11: o000o0o00o0Oo . i1 * I1iiiiI1iII * OoooooooOO + i1Ii
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  Iiii = IiII111i1i11 ( Iiii )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in Iiii :
    o00 = 'https://www.youtube.com' + url
    i1IiIiiI ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , o00 , 2 , I1IiI , I1ii11iIi11i )
    if 40 - 40: i1Ii * I1iiiiI1iII * i11iIiiIii
def oo0OO00OoooOo ( ) :
 if 19 - 19: o000o0o00o0Oo % OoooooooOO % I1iiiiI1iII * i1IIi11111i % O0
 iI = 'http://burningwhee1s.blogspot.co.uk/'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( Iii111II )
 for Ii11I , Iiii in I1IiiiiI :
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , Ii11I , 24 , I1IiI , Oo , '' )
  if 67 - 67: iiI1iIiI . i1IIi
def i1i1iI1iiiI ( url ) :
 if 51 - 51: iiI1iIiI % oOo0 . OOo0o0 / iIii1I11I1II1 / iI1 . OOo0o0
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 42 - 42: i1IIi11111i + i1IIi - OOooO / I1iiiiI1iII
def iiIiIIIiiI ( url , iconimage ) :
 if 12 - 12: O0 - i1IIi11111i
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( Iii111II )
 try :
  for i1I1iI in I1IiiiiI :
   Iiii = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    oOoO00O0 = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     oOoO00O0 = re . compile ( '<b>(.+?)</b>' ) . findall ( i1I1iI ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     oOoO00O0 = ''
   Iiii = IiII111i1i11 ( Iiii )
   oOoO00O0 = IiII111i1i11 ( oOoO00O0 )
   OO = re . compile ( '<option value="(.+?)"' ) . findall ( i1I1iI ) [ 1 ]
   i1IiIiiI ( "[COLOR aqua]" + Iiii + "  " + oOoO00O0 + "[/COLOR]" , OO , 2 , I1IiI , Oo , '' )
 except :
  i1IiIiiI ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 7 - 7: O0 * i11iIiiIii * OOooO + i1Ii % i1 - i1Ii
def II1IIIIiII1i ( ) :
 if 1 - 1: i11Ii11I1Ii1i
 if 68 - 68: OOoO00o - iiI1iIiI / oOo0 / iI1
 iI = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 Ii11I = OOO0OOO00oo ( iI )
 OoO000 = json . loads ( Ii11I )
 I11iiii = OoO000 [ 'results' ]
 for O0i1iI in I11iiii :
  IiI1iiiIii = 'https://image.tmdb.org/t/p/w640'
  Iiii = O0i1iI [ 'title' ]
  I1IiI = O0i1iI [ 'poster_path' ]
  I1III1111iIi = O0i1iI [ 'id' ]
  I1IiI = IiI1iiiIii + I1IiI
  I1ii11iIi11i = O0i1iI [ 'backdrop_path' ]
  I1ii11iIi11i = IiI1iiiIii + I1ii11iIi11i
  I1i111I = O0i1iI [ 'overview' ]
  I1III1111iIi = str ( I1III1111iIi )
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , Iiii , 33 , I1IiI , I1ii11iIi11i , I1i111I )
  if 97 - 97: i1IIi . OOo0o0 / OOoO00o * O0
def o0O0o ( url ) :
 if 77 - 77: Oooo0000 - iiI1iIiI * i11iIiiIii * i1Ii * iIii1I11I1II1
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = re . compile ( '<i>(.+?)</i>' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = Iiii . strip ( )
  IIIii1II1II ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  oOo0OOOoOO = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( Ii11I ) [ 0 ]
  I11IIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  IIIii1II1II ( '[COLOR yellow]Next Page >>[/COLOR]' , oOo0OOOoOO , 26 , I11IIIi , I1ii11iIi11i )
 except : pass
 if 15 - 15: o000o0o00o0Oo * i1
def i1II1i ( url , iconimage ) :
 if 83 - 83: Oooo0000 - OOooO / iI1 / oOo0 + OOo0o0 - O0
 Ii11I = OOO0OOO00oo ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( Ii11I ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 Iii111II = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( Ii11I )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 II1I = 1
 I11I1i1iIII1I = [ ]
 for i1I1iI in Iii111II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I11I1i1iIII1I . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( II1I ) )
  time . sleep ( 0.02 )
  II1I += 1
  Iiii = re . compile ( '(.+?)</p>' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'Server' , '' )
  Iiii = Iiii . strip ( )
 iII1i11 = 1
 OoOo = 0
 Ooo = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 20 - 20: i11Ii11I1Ii1i % ooo0Oo0 + o000o0o00o0Oo + i1Ii
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if OoOo > len ( I11I1i1iIII1I ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 23 - 23: OOoOoo00oo * OOooO * ooo0Oo0 . O0 - i11iIiiIii
  if Ooo == 0 :
   OoOo += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( OoOo ) + "[/COLOR]" , '' )
   try :
    Ii11I = OOO0OOO00oo ( I11I1i1iIII1I [ OoOo ] )
    I1IiiiiI = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( Ii11I ) [ 0 ]
    i1I1iIi = base64 . b64decode ( I1IiiiiI )
    url = re . compile ( 'src="(.+?)"' ) . findall ( i1I1iIi ) [ 0 ]
    IIii11Ii1i1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    Oooo0O = open ( IIii11Ii1i1I ) . read ( )
    oo00O0oO0O0 = re . compile ( '<url>(.+?)</url>' ) . findall ( Oooo0O )
    for ooo0OO0O0Oo in oo00O0oO0O0 :
     Ooo0O0oooo = re . compile ( '<bad>(.+?)<bad>' ) . findall ( ooo0OO0O0Oo ) [ 0 ]
     if url == Ooo0O0oooo :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( OoOo ) )
      time . sleep ( 0.5 )
      Ooo = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     iiI = liveresolver . resolve ( url )
    else : iiI = url
    oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( iiI , oOO0O00oO0Ooo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( OoOo ) )
    time . sleep ( 0.5 )
    Ooo = 5
    pass
  if Ooo == 5 :
   Ooo = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   Ooo += 1
   if 56 - 56: ooo0Oo0 . o000o0o00o0Oo . iiI1iIiI
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 IIii11Ii1i1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 Oo0oOOo = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if Oo0oOOo :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( IIii11Ii1i1I , "a" ) as iIi :
   iIi . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 39 - 39: O0 + oOo0
def OoOooOoO ( url ) :
 if 43 - 43: i11Ii11I1Ii1i . OOo0o0 / o000o0o00o0Oo
 if 20 - 20: iiI1iIiI
 if url == 'search' :
  o0oO000oo = ''
  o00o0II1I = xbmc . Keyboard ( o0oO000oo , 'Enter Search Term' )
  o00o0II1I . doModal ( )
  if o00o0II1I . isConfirmed ( ) :
   o0oO000oo = o00o0II1I . getText ( )
   if len ( o0oO000oo ) > 1 :
    II1I1I1Ii = o0oO000oo . lower ( )
    if 70 - 70: i1 % OOo0o0 + OOoOoo00oo / OOooO % O0
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , ii11i1 , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , ii11i1 , 5000 )
   quit ( )
  II1I1I1Ii = II1I1I1Ii . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + II1I1I1Ii + '.html'
  oO00O0 ( url , I1IiI )
  if 36 - 36: OOo0o0 - OOooO . ooo0Oo0 - i11iIiiIii - OOoOoo00oo * ooo0Oo0
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  oO00O0 ( url , I1IiI )
  if 76 - 76: i11iIiiIii + i1IIi11111i / o000o0o00o0Oo - i1 - OOooO + o000o0o00o0Oo
def oO00O0 ( url , icon ) :
 if 51 - 51: iIii1I11I1II1 . i1Ii + iIii1I11I1II1
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = re . compile ( '<i>(.+?)</i>' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = IiII111i1i11 ( Iiii )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  IIIii1II1II ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 95 - 95: iiI1iIiI
def iII1ii1 ( ) :
 if 12 - 12: OOoOoo00oo - i1Ii . OoooooooOO / o000o0o00o0Oo . i1IIi * i1
 iI = 'http://www.genti.stream/'
 Ii11I = OOO0OOO00oo ( iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii111II = re . compile ( '<div class="date">(.+?)<div class="match-list-item"' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  IiIiII1 = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ] . strip ( )
  Iii1iiIi1II = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( i1I1iI ) [ 1 ] . strip ( )
  iI = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'http://www.genti.stream/' + iI
  i1IiIiiI ( "[COLOR aqua]" + IiIiII1 + "[COLOR yellow] vs [COLOR aqua]" + Iii1iiIi1II + "[/COLOR]" , iI , 39 , I1IiI , I1ii11iIi11i )
  if 60 - 60: iiI1iIiI - OOo0o0 * iI1 % i11Ii11I1Ii1i
def ooo ( url ) :
 if 19 - 19: i1 - ooo0Oo0 . OOo0o0 / OOo0o0 % i1Ii
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ooO = re . compile ( '<iframe src="(.+?)"' ) . findall ( Ii11I ) [ 0 ]
 o0O = OOO0OOO00oo ( ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  url = re . compile ( 'source: "(.+?)"' ) . findall ( o0O ) [ 0 ]
 except IndexError :
  url = re . compile ( "source: '(.+?)'" ) . findall ( o0O ) [ 0 ]
 ii ( Ooo0OO0oOO , url , ii11i1 )
 if 82 - 82: Oooo0000 - i1 % Oooo0000 * i11iIiiIii . i11Ii11I1Ii1i % i11Ii11I1Ii1i
 if 54 - 54: iI1 + OOooO
def o00I1 ( url ) :
 if 55 - 55: OOoO00o . i11Ii11I1Ii1i % i1 * OOoO00o + i1Ii + OOooO
 II1Iiiiii = cfscrape . create_scraper ( )
 I1i1I1II = II1Iiiiii . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( I1i1I1II ) [ 0 ]
 I1IiiiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Iii111II )
 for url , Iiii in I1IiiiiI :
  url = 'http://kimcartoon.me/CartoonList' + url
  IIIii1II1II ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 36 - 36: iiI1iIiI - iI1
def i11i11111i1i ( url ) :
 if 72 - 72: OOoOoo00oo % o000o0o00o0Oo + i1 / OOo0o0 + I1iiiiI1iII
 II1Iiiiii = cfscrape . create_scraper ( )
 I1i1I1II = II1Iiiiii . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( I1i1I1II )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   I1I1i = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( i1I1iI ) [ 0 ]
   I1I1i = IiII111i1i11 ( I1I1i )
  except IndexError :
   I1I1i = ''
  IIIii1II1II ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , I1I1i )
  if 1 - 1: iI1 % OOoOoo00oo + O0 + i1IIi - i1
 try :
  iIIIII1ii1I = re . compile ( '<li>(.+?)Next' ) . findall ( I1i1I1II )
  for i1I1iI in iIIIII1ii1I :
   oOo0OOOoOO = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ - 1 ]
   Ii1i1iI = 'http://kimcartoon.me' + oOo0OOOoOO
   IIiI1 = 'https://i.imgur.com/mjCRjXT.png'
   IIIii1II1II ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , Ii1i1iI , 30 , IIiI1 , I1ii11iIi11i )
 except : pass
 if 17 - 17: OOoOoo00oo / OOoOoo00oo / iI1
def ii1 ( url ) :
 if 1 - 1: i1Ii % iIii1I11I1II1 + ooo0Oo0 . iIii1I11I1II1 % iiI1iIiI
 II1Iiiiii = cfscrape . create_scraper ( )
 I1i1I1II = II1Iiiiii . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( '<td>(.+?)</td>' ) . findall ( I1i1I1II )
 for i1I1iI in Iii111II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   Iiii = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   i1IiIiiI ( "[COLOR aqua][B]" + Iiii + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 89 - 89: OOooO
def ooOoOO0OoO00o ( url ) :
 if 11 - 11: ooo0Oo0 - iiI1iIiI * i11Ii11I1Ii1i . o000o0o00o0Oo . OOo0o0
 O0Oo000ooO00 = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if O0Oo000ooO00 == 0 :
  url = url + '&s=rapidvideo'
  II1Iiiiii = cfscrape . create_scraper ( )
  I1i1I1II = II1Iiiiii . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1IiiiiI = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( I1i1I1II )
   for Ii11I in I1IiiiiI :
    url = re . compile ( 'src="(.+?)"' ) . findall ( Ii11I ) [ 0 ]
    if 'rapidvideo' in url :
     ii ( Ooo0OO0oOO , url , ii11i1 )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if O0Oo000ooO00 == 1 :
  url = url + '&s=openload'
  II1Iiiiii = cfscrape . create_scraper ( )
  I1i1I1II = II1Iiiiii . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   I1IiiiiI = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( I1i1I1II )
   for Ii11I in I1IiiiiI :
    url = re . compile ( 'src="(.+?)"' ) . findall ( Ii11I ) [ 0 ]
    ii ( Ooo0OO0oOO , url , ii11i1 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 61 - 61: OOoO00o % iiI1iIiI - i1IIi11111i - i11Ii11I1Ii1i % O0
   if 90 - 90: iIii1I11I1II1 + o000o0o00o0Oo + i1Ii - oOo0 * I1iiiiI1iII . o000o0o00o0Oo
def I11iiiii1II ( ) :
 if 51 - 51: O0 % OOo0o0 - i11Ii11I1Ii1i
 iI = "http://www.loyalbooks.com/genre-menu"
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( Ii11I )
 for iiii11I in Iii111II :
  if "paid" not in iiii11I :
   o0O = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
   OOo0oO00ooO00 = "http://www.loyalbooks.com" + o0O
   Ooo0OO0oOO = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
   IIIii1II1II ( "[COLOR aqua]" + Ooo0OO0oOO + "[/COLOR]" , OOo0oO00ooO00 , 60 , I1IiI , Oo , '' )
   if 31 - 31: OOoO00o / ooo0Oo0 - OOoO00o - OOoOoo00oo
def I1iiIIIi11 ( url ) :
 if 12 - 12: OoooooooOO % i1IIi11111i * iI1 % iIii1I11I1II1 / OOooO
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( Ii11I ) [ 0 ]
 Ii1ii1IiIII = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( Iii111II )
 for iiii11I in Ii1ii1IiIII :
  o00 = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
  OOo0oO00ooO00 = "http://www.loyalbooks.com" + o00
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
  ii11i1 = "http://www.loyalbooks.com" + I1IiI
  Ooo0OO0oOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
  IIIii1II1II ( "[COLOR aqua]" + Ooo0OO0oOO + "[/COLOR]" , OOo0oO00ooO00 , 61 , ii11i1 , Oo , '' )
 try :
  Ii11I = OOO0OOO00oo ( url )
  oo0O0O00 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( Ii11I ) [ 0 ]
  I1IiI = 'https://i.imgur.com/mjCRjXT.png'
  IIIii1II1II ( "[COLOR yellow]Next Page -->[/COLOR]" , oo0O0O00 , 60 , I1IiI , Oo , '' )
 except : pass
 if 57 - 57: iIii1I11I1II1 / iI1 - i1IIi
 if 51 - 51: I1iiiiI1iII
def ii11I1 ( name , url , iconimage ) :
 if 75 - 75: i1 / i11Ii11I1Ii1i % O0
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( Ii11I )
 for iiii11I in Iii111II :
  Iiii = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
  o00 = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( iiii11I ) [ 0 ]
  i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , o00 , 10 , iconimage , Oo , '' )
  if 38 - 38: OoooooooOO * i1Ii % O0 * Oooo0000
def IIiiI ( ) :
 if 31 - 31: o000o0o00o0Oo + OOooO + oOo0 / OOooO
 iI = 'http://www.shadownet.me/'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( Iii111II )
 for iI , Iiii in I1IiiiiI :
  Iiii = IiII111i1i11 ( Iiii )
  if 'P2P' not in Iiii :
   IIIii1II1II ( "[COLOR skyblue]" + Iiii + "[/COLOR]" , iI , 49 , I1IiI , Oo , '' )
   if 25 - 25: i1
   if 24 - 24: I1iiiiI1iII * i11iIiiIii * OOoOoo00oo
def OOo ( url ) :
 if 50 - 50: i1Ii
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( Iii111II )
 for i1I1iI in I1IiiiiI :
  Iiii = re . compile ( 'alt="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  i1IiIiiI ( "[COLOR skyblue]" + Iiii + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  oOo0OOOoOO = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( Ii11I ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  IIIii1II1II ( "[COLOR orange]Next Page --->[/COLOR]" , oOo0OOOoOO , 49 , I1IiI , Oo , '' )
 except : pass
 if 72 - 72: oOo0
def OO0ooo0oOO ( url ) :
 if 97 - 97: iiI1iIiI / OOoO00o
 def Oooo0 ( url ) :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iiiIi . add_header ( 'Referer' , url )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11I = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  return Ii11I
  if 59 - 59: OoooooooOO
 Ii11I = Oooo0 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  Iii111II = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( Ii11I ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in Iii111II :
  url = Iii111II
  ii ( Ooo0OO0oOO , url , ii11i1 )
 OOo0oO00ooO00 = Oooo0 ( Iii111II )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( OOo0oO00ooO00 ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 47 - 47: i1Ii - iiI1iIiI / i11Ii11I1Ii1i
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
  oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = ii11i1 , thumbnailImage = ii11i1 )
  oOO0O00oO0Ooo . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oOO0O00oO0Ooo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = ii11i1 , thumbnailImage = ii11i1 )
  oOO0O00oO0Ooo . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oOO0O00oO0Ooo , False )
 else :
  if '.m3u8' in url :
   o00 = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + Ooo0OO0oOO + '&amp;url=' + url + '&amp;iconImage=' + ii11i1
  elif '.ts' in url :
   o00 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + Ooo0OO0oOO + '&amp;url=' + url + '&amp;iconImage=' + ii11i1
  else :
   o00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 12 - 12: OOoOoo00oo
  oOO0O00oO0Ooo = xbmcgui . ListItem ( Ooo0OO0oOO , iconImage = ii11i1 , thumbnailImage = ii11i1 )
  oOO0O00oO0Ooo . setPath ( url )
  if 83 - 83: OOoO00o . O0 / ooo0Oo0 / OOoOoo00oo - i11Ii11I1Ii1i
  xbmc . Player ( ) . play ( o00 , oOO0O00oO0Ooo , False )
  if 100 - 100: i1
  if 46 - 46: Oooo0000 / iIii1I11I1II1 % OOoO00o . iIii1I11I1II1 * OOoO00o
def IIi1ii1Ii ( ) :
 if 91 - 91: i11iIiiIii / OoooooooOO + OOoO00o - i11iIiiIii + OOoOoo00oo
 iI = 'https://www.skylinewebcams.com/en/webcam.html'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<i class="icon-angle-down">(.+?)<i class="icon-angle-down">' ) . findall ( Ii11I ) [ 0 ] . replace ( '<strong>' , '' ) . replace ( '&nbsp;' , '' )
 I1IiiiiI = re . compile ( '<a href="(.+?)" class="menu-item">(.+?)<span class="ccnt">(.+?)</span>' ) . findall ( Iii111II )
 for Ii11I , Iiii , ii1i in I1IiiiiI :
  if 'http' not in Ii11I :
   iI = 'https://www.skylinewebcams.com' + Ii11I
   IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , iI , 46 , I1IiI , Oo , '' )
   if 62 - 62: i1 / o000o0o00o0Oo
def ii1O000OOO0OOo ( url ) :
 if 32 - 32: OOooO * O0
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<li class="webcam">(.+?)</span>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   O00oOo00o0o = re . compile ( 'data-original="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   if not 'http' in O00oOo00o0o :
    I1IiI = 'http:' + O00oOo00o0o
    Iiii = re . compile ( 'alt="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
    O00oO0 = re . compile ( '<a href="(.+?)">' ) . findall ( i1I1iI ) [ 0 ]
    if not 'http:' in O00oO0 :
     url = 'https://www.skylinewebcams.com' + O00oO0
     IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  except : pass
  if 70 - 70: iI1 . o000o0o00o0Oo * OoooooooOO - I1iiiiI1iII * iiI1iIiI + Oooo0000
def iIi1 ( name , url , iconimage ) :
 if 21 - 21: iI1
 Ii11I = OOO0OOO00oo ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  Iii111II = re . compile ( '<script type="text/javascript">(.+?)</script>' ) . findall ( Ii11I ) [ 1 ]
  url = re . compile ( "url:'(.+?)'}" ) . findall ( Iii111II ) [ 0 ]
  oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , oOO0O00oO0Ooo , False )
  if 92 - 92: i11iIiiIii / oOo0 - OOoO00o % i1Ii * oOo0 + ooo0Oo0
 except : pass
 quit ( 0 )
 if 11 - 11: OoooooooOO . oOo0
def Oo0000oOo ( ) :
 if 31 - 31: iI1 . oOo0 * i1Ii + i11iIiiIii * OOo0o0
 iI = 'http://www.watchepisodeseries.com/home/schedule'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( Iii111II )
 for iI , oOO00oOO , OO0o in I1IiiiiI :
  IIIii1II1II ( "[COLOR aqua]" + oOO00oOO + "  " + OO0o + "[/COLOR]" , iI , 67 , I1IiI , I1ii11iIi11i )
  if 75 - 75: OoooooooOO * I1iiiiI1iII
  if 9 - 9: I1iiiiI1iII - i11Ii11I1Ii1i + O0 / iIii1I11I1II1 / i11iIiiIii
def I1IIIiI1I1ii1 ( url ) :
 if 30 - 30: O0 * OoooooooOO
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 1 ]
  Iiii = IiII111i1i11 ( Iiii )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  ii11i1 = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( i1I1iI ) [ 0 ]
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 68 , ii11i1 , I1ii11iIi11i )
  if 38 - 38: I1iiiiI1iII - o000o0o00o0Oo . Oooo0000 - oOo0 . OoooooooOO
  if 89 - 89: iIii1I11I1II1
def i11iiiiI1i ( url , iconimage , fanart ) :
 if 37 - 37: OOoOoo00oo / OoooooooOO - i11iIiiIii
 Ii11I = OOO0OOO00oo ( url )
 i1iIiIi1I = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in i1iIiIi1I :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
 Iii111II = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( Ii11I )
 II1I = datetime . now ( )
 for i1I1iI in Iii111II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   Iiii = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   Iiii = IiII111i1i11 ( Iiii )
   iiii11i = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   III11II1I1Ii1 = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   oOO00oOO = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in oOO00oOO :
    oOO00oOO = oOO00oOO . strip ( )
    oOO00oOO = time . strptime ( oOO00oOO , "%d/%m/%Y" )
    O00Oo0o000oO = ( "%s/%s/%s" % ( II1I . day , II1I . month , II1I . year ) )
    O00Oo0o000oO = time . strptime ( O00Oo0o000oO , "%d/%m/%Y" )
    if ( O00Oo0o000oO < oOO00oOO ) :
     Iiii = '[COLOR yellow]' + ( Iiii ) + ' - Not Aired Yet' + '[/COLOR]'
     III11II1I1Ii1 = '[COLOR yellow]' + ( III11II1I1Ii1 ) + '[/COLOR]'
     iiii11i = '[COLOR yellow]' + ( iiii11i ) + '[/COLOR]'
     if 99 - 99: OOo0o0 * i11Ii11I1Ii1i * oOo0
    if not 'Season 0' in iiii11i :
     IIIii1II1II ( "[COLOR aqua]" + iiii11i + " " + III11II1I1Ii1 + " " + Iiii + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 92 - 92: ooo0Oo0
  if 40 - 40: Oooo0000 / I1iiiiI1iII
def OOOoO000 ( url , iconimage , fanart ) :
 if 57 - 57: i11Ii11I1Ii1i
 if 54 - 54: ooo0Oo0 + OOo0o0 + i11iIiiIii
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   Iiii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1I1iI ) [ 0 ]
   Iiii = Iiii . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
   if not 'Lolzor.Com' in Iiii :
    if not 'Videoplayer.Gq' in Iiii :
     if not 'Vidbaba.Com' in Iiii :
      if not 'Gagomatic.Com' in Iiii :
       if not 'Favour.Me' in Iiii :
        if not 'Funblr.Com' in Iiii :
         if not 'Vid.Ag' in Iiii :
          if not 'Mycollection.Net' in Iiii :
           if not 'Adhqmedia.Com' in Iiii :
            if not 'Filenuke.Com' in Iiii :
             if not 'Mrfile.Me' in Iiii :
              i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 28 - 28: OOo0o0
  if 70 - 70: I1iiiiI1iII
def i11i1iiI1i ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  url = re . compile ( 'href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    iiI = liveresolver . resolve ( url )
   else : iiI = url
   oOO0O00oO0Ooo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   oOO0O00oO0Ooo . setPath ( iiI )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO0O00oO0Ooo )
   xbmc . Player ( ) . play ( iiI )
   if 87 - 87: i1Ii
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 45 - 45: i1 / OoooooooOO - OOoO00o / OOooO % I1iiiiI1iII
def OoOIii11iI11i1I ( ) :
 if 64 - 64: i11iIiiIii
 o0oO000oo = ''
 o00o0II1I = xbmc . Keyboard ( o0oO000oo , 'Enter Search Term' )
 o00o0II1I . doModal ( )
 if o00o0II1I . isConfirmed ( ) :
  o0oO000oo = o00o0II1I . getText ( )
  if len ( o0oO000oo ) > 1 :
   II1I1I1Ii = o0oO000oo . lower ( )
   II1I1I1Ii = II1I1I1Ii . replace ( ' ' , '%20' )
   if 38 - 38: I1iiiiI1iII / iiI1iIiI - I1iiiiI1iII . iI1
  else : quit ( )
 else : II1I1I1Ii = urllib . unquote_plus ( iI ) . lower ( ) ; o0oO000oo = urllib . unquote_plus ( iI )
 iI = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + II1I1I1Ii
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '"series"(.+?)"series_id"' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( 'original_name":"(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  o00 = re . compile ( '"seo_name":"(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'http://www.watchepisodeseries.com/' + o00
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + o00 + '.jpg'
  IIIii1II1II ( Iiii , iI , 68 , I1IiI , I1ii11iIi11i , '' )
  if 69 - 69: OoooooooOO + o000o0o00o0Oo
def O0oOo00o0 ( ) :
 if 65 - 65: i11Ii11I1Ii1i . iiI1iIiI % OOo0o0 * i1
 iI = 'http://www.watchepisodeseries.com/home/popular-series'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<div title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  Iiii = IiII111i1i11 ( Iiii )
  iI = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( i1I1iI ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  IIIii1II1II ( '[COLOR aqua]' + Iiii + '[/COLOR]' , iI , 68 , I1IiI , I1ii11iIi11i )
  if 38 - 38: Oooo0000 / OOoO00o % ooo0Oo0
  if 11 - 11: OOoO00o - OOo0o0 + i11Ii11I1Ii1i - iIii1I11I1II1
def I1i11ii11 ( ) :
 if 81 - 81: OOoOoo00oo - iI1 % i1Ii - i1 / ooo0Oo0
 try :
  Ii1iI111 = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  o0oO000oo = ''
  o00o0II1I = xbmc . Keyboard ( o0oO000oo , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  o00o0II1I . doModal ( )
  if o00o0II1I . isConfirmed ( ) :
   o0oO000oo = o00o0II1I . getText ( )
   if len ( o0oO000oo ) > 1 :
    II1I1I1Ii = o0oO000oo
   else : quit ( )
  if II1I1I1Ii == Ii1iI111 :
   O0oooo00o0Oo ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  o0oO000oo = ''
  o00o0II1I = xbmc . Keyboard ( o0oO000oo , 'Enter The Password You Set' )
  o00o0II1I . doModal ( )
  if o00o0II1I . isConfirmed ( ) :
   o0oO000oo = o00o0II1I . getText ( )
   if len ( o0oO000oo ) > 1 :
    II1I1I1Ii = o0oO000oo
   else : quit ( )
  with open ( i1i1II , "w" ) as iIi :
   iIi . write ( II1I1I1Ii )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 36 - 36: OOooO / i11Ii11I1Ii1i / I1iiiiI1iII / I1iiiiI1iII + o000o0o00o0Oo
   if 95 - 95: I1iiiiI1iII
   if 51 - 51: i11Ii11I1Ii1i + I1iiiiI1iII . i1IIi . o000o0o00o0Oo + Oooo0000 * iiI1iIiI
def O0oooo00o0Oo ( ) :
 if 72 - 72: OOo0o0 + OOo0o0 / i11Ii11I1Ii1i . OoooooooOO % OOooO
 iI = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<li class="">(.+?)</li>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( i1I1iI ) [ 0 ]
  ii1i = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
  o00 = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  iI = 'https://www.eporner.com' + o00
  if not 'All' in Iiii :
   if not 'Homemade' in Iiii :
    IIIii1II1II ( "[COLOR aqua]" + Iiii + "  " + "[COLOR yellow]" + ii1i + "[/COLOR]" , iI , 36 , I1IiI , Oo , '' )
    if 49 - 49: OOo0o0 . i1 - ooo0Oo0 * OoooooooOO . ooo0Oo0
def ii1Ii1IiIIi ( url ) :
 if 83 - 83: iI1 / o000o0o00o0Oo
 Ii11I = OOO0OOO00oo ( url )
 Iii111II = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  Iiii = re . compile ( 'title="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  o00 = re . compile ( '<a href="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( i1I1iI ) [ 0 ]
  url = 'https://www.eporner.com' + o00
  IIIii1II1II ( "[COLOR skyblue]" + Iiii + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 34 - 34: iiI1iIiI * ooo0Oo0 * oOo0 / i1 * iI1 / iIii1I11I1II1
 try :
  oOo0OOOoOO = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( Ii11I ) [ 0 ]
  oo0O0O00 = 'https://www.eporner.com' + oOo0OOOoOO
  I11IIIi = 'http://imgur.com/3eNoY0p'
  IIIii1II1II ( "[COLOR orange]" + "Next Page" + "[/COLOR]" , oo0O0O00 , 36 , I11IIIi , Oo , '' )
 except : pass
 if 74 - 74: ooo0Oo0 / i11iIiiIii - i11Ii11I1Ii1i * i1IIi11111i
def IIi1IIIIi ( url , iconimage ) :
 if 70 - 70: OOoOoo00oo / i11Ii11I1Ii1i - iIii1I11I1II1 - OOoO00o
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IiiiIi1i = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( IiiiIi1i )
 for i1ii , Ii11I in I1IiiiiI :
  i1ii = i1ii . replace ( ':' , '' )
  url = 'https://www.eporner.com' + Ii11I
  i1IiIiiI ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + i1ii + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 68 - 68: OOoOoo00oo * O0 . iI1 - i11Ii11I1Ii1i . i1Ii / i11Ii11I1Ii1i
def iii1 ( ) :
 if 32 - 32: OOooO . I1iiiiI1iII . OoooooooOO - i1 + OOo0o0
 iI = 'http://animeheaven.eu/dubbed.php'
 Ii11I = OOO0OOO00oo ( iI )
 Iii111II = re . compile ( '<a class=\'gridvan\'(.+?)</a>' ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   Iiii = re . compile ( '<div class=\'gridpg\'>(.+?)</div>' ) . findall ( i1I1iI ) [ 0 ]
   iI = re . compile ( "href='(.+?)'>" ) . findall ( i1I1iI ) [ 0 ]
   iI = 'http://animeheaven.eu/' + iI
   IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , iI , 52 , I1IiI , Oo , '' )
  except : pass
  if 88 - 88: OOoO00o
def iiI11I1i1i1iI ( url ) :
 if 60 - 60: OoooooooOO % ooo0Oo0 + OOoOoo00oo . i1Ii * iIii1I11I1II1
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( "<div class='lisb'>(.+?)<div class='side'>" ) . findall ( Ii11I ) [ 0 ]
 I1IiiiiI = re . compile ( "href='(.+?)'><div class='lis'>(.+?)</div>" ) . findall ( Iii111II )
 for url , Iiii in I1IiiiiI :
  url = url . replace ( ' ' , '%20' )
  url = 'http://animeheaven.eu/' + url
  IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 93 - 93: i1
def i111I ( url ) :
 if 57 - 57: iiI1iIiI % iI1 - OOoOoo00oo . iiI1iIiI / ooo0Oo0 % OOoO00o
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( "<a(.+?)</a>" ) . findall ( Ii11I )
 for i1I1iI in Iii111II :
  try :
   Iiii = re . compile ( "<div class='infoept2'>(.+?)</div>" ) . findall ( i1I1iI ) [ 0 ]
   Iiii = 'Episode ' + Iiii
   url = re . compile ( "href='(.+?)'" ) . findall ( i1I1iI ) [ 0 ]
   url = url . replace ( ' ' , '%20' )
   url = 'http://animeheaven.eu/' + url
   I1IiI = re . compile ( "<img src='(.+?)'" ) . findall ( Ii11I ) [ 0 ]
   I1IiI = 'http://animeheaven.eu/' + I1IiI
   IIIii1II1II ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  except : pass
  if 56 - 56: OOo0o0 . OOoO00o . I1iiiiI1iII * Oooo0000 . i1Ii / O0
def IiI1I1 ( url , iconimage ) :
 if 45 - 45: Oooo0000
 Ii11I = OOO0OOO00oo ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 Iii111II = re . compile ( "document.write\(\"<a class='an'(.+?)</div>" ) . findall ( Ii11I )
 II1I = 0
 for i1I1iI in Iii111II :
  II1I += 1
  url = re . compile ( "href='(.+?)'" ) . findall ( i1I1iI ) [ 0 ]
  Iiii = 'Link ' + str ( II1I )
  i1IiIiiI ( "[COLOR aqua]" + Iiii + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 66 - 66: i1
  if 56 - 56: O0
  if 61 - 61: i1IIi11111i / OOoOoo00oo / ooo0Oo0 * O0
  if 23 - 23: OOo0o0 - OOoOoo00oo + iI1
  if 12 - 12: iiI1iIiI / i1Ii % i1IIi11111i / i11iIiiIii % OoooooooOO
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - ooo0Oo0 * OOooO + iI1
  if 11 - 11: OOoO00o * OOooO - Oooo0000
  if 66 - 66: Oooo0000 . i11iIiiIii - OOoO00o * i1IIi11111i + OoooooooOO * o000o0o00o0Oo
  if 74 - 74: ooo0Oo0
def IiII111i1i11 ( text ) :
 if 61 - 61: ooo0Oo0 - oOo0 * i11Ii11I1Ii1i % i1Ii * iIii1I11I1II1 + i1
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
 text = text . lstrip ( '   ' )
 if 71 - 71: iI1 / iI1 * OOo0o0 * OOo0o0 / i11Ii11I1Ii1i
 return text
 if 35 - 35: OOoOoo00oo * i1IIi11111i * iiI1iIiI % ooo0Oo0 . Oooo0000
def O00o00O ( ) :
 if 3 - 3: OOoOoo00oo
 IiiO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 O0Oo00oO0O00 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 O000O0OO00oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 69 - 69: i1IIi11111i / ooo0Oo0
 IIi = 0
 for ( IiiIIIII1iii , IIiiii , iI111i1I1II ) in os . walk ( O0Oo00oO0O00 ) :
  for file in iI111i1I1II :
   O00OO = os . path . join ( IiiIIIII1iii , file )
   IIi += os . path . getsize ( O00OO )
 oO0Oo = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( IIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 29 - 29: ooo0Oo0 % i1 % I1iiiiI1iII . i1IIi11111i / OoooooooOO * i1Ii
 IIi = 0
 for ( IiiIIIII1iii , IIiiii , iI111i1I1II ) in os . walk ( IiiO0o0o ) :
  for file in iI111i1I1II :
   O00OO = os . path . join ( IiiIIIII1iii , file )
   IIi += os . path . getsize ( O00OO )
 oO0Oo = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( IIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 54 - 54: O0
 IIi = 0
 for ( IiiIIIII1iii , IIiiii , iI111i1I1II ) in os . walk ( Ii ) :
  for file in iI111i1I1II :
   O00OO = os . path . join ( IiiIIIII1iii , file )
   IIi += os . path . getsize ( O00OO )
 oO0Oo = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( IIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 68 - 68: i1 * i1IIi11111i . i1Ii % OOo0o0 % oOo0
 IIi = 0
 for ( IiiIIIII1iii , IIiiii , iI111i1I1II ) in os . walk ( O000O0OO00oo ) :
  for file in iI111i1I1II :
   O00OO = os . path . join ( IiiIIIII1iii , file )
   IIi += os . path . getsize ( O00OO )
 oO0Oo = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( IIi / ( 1024 * 1024.0 ) )
 i1IiIiiI ( oO0Oo , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 75 - 75: Oooo0000
 i1IiIiiI ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 i1IiIiiI ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 34 - 34: O0
def ii ( name , url , iconimage ) :
 if 80 - 80: i1IIi - ooo0Oo0 / i1 - i11iIiiIii
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import urlresolver
 if '.m3u8' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
 if 'acestream' in url :
  o00 = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  oOO0O00oO0Ooo . setPath ( url )
  xbmc . Player ( ) . play ( o00 , oOO0O00oO0Ooo , False )
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
  oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  oOO0O00oO0Ooo . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oOO0O00oO0Ooo , False )
  time . sleep ( 2 )
  quit ( )
 else :
  iiI = url
  oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  oOO0O00oO0Ooo . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oOO0O00oO0Ooo , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 68 - 68: OOo0o0 - o000o0o00o0Oo % O0 % oOo0
def Iii ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 11 - 11: O0 / i1 % OOoOoo00oo + i1IIi11111i + iIii1I11I1II1
def I1i1111I ( heading , text ) :
 if 95 - 95: iIii1I11I1II1 - o000o0o00o0Oo . oOo0 - iiI1iIiI
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 OOOOoo = xbmcgui . Window ( id )
 o000 = 50
 while ( o000 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   o000 -= 1
   OOOOoo . getControl ( 1 ) . setLabel ( heading )
   OOOOoo . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 94 - 94: i1IIi11111i + O0 / iI1 . iiI1iIiI + OOoOoo00oo . iIii1I11I1II1
  if 62 - 62: Oooo0000 / iiI1iIiI - o000o0o00o0Oo - iiI1iIiI + i11iIiiIii + i1IIi
def OOO0OOO00oo ( url ) :
 try :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11I = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  Ii11I = Ii11I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return Ii11I
 except : quit ( )
 if 23 - 23: OOoO00o + iI1 . Oooo0000 * iiI1iIiI + o000o0o00o0Oo
def OO0OOOOoo0OOO ( url ) :
 try :
  iiiIi = urllib2 . Request ( url )
  iiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  IiIIIiI1I1 = urllib2 . urlopen ( iiiIi , timeout = 5 )
  Ii11I = IiIIIiI1I1 . read ( )
  IiIIIiI1I1 . close ( )
  Ii11I = Ii11I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return Ii11I
 except : quit ( )
 if 18 - 18: I1iiiiI1iII * i1IIi11111i . I1iiiiI1iII / O0
def i1IiIiiI ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 iiIII1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOo00oOOOOO = True
 oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOO0O00oO0Ooo . setProperty ( "fanart_Image" , fanart )
 oOO0O00oO0Ooo . setProperty ( "icon_Image" , iconimage )
 oOO0O00oO0Ooo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOO0O00oO0Ooo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 85 - 85: OoooooooOO - i1 - oOo0 / i1Ii - iI1
 oOo00oOOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiIII1II , listitem = oOO0O00oO0Ooo , isFolder = False )
 return oOo00oOOOOO
 if 49 - 49: Oooo0000 / ooo0Oo0 . i11iIiiIii
def o0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 iiIII1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOo00oOOOOO = True
 oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOO0O00oO0Ooo . setProperty ( "fanart_Image" , fanart )
 oOO0O00oO0Ooo . setProperty ( "icon_Image" , iconimage )
 oOO0O00oO0Ooo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 21 - 21: Oooo0000 + i11iIiiIii + iiI1iIiI * i1IIi11111i % OOoO00o % i11Ii11I1Ii1i
 oOO0O00oO0Ooo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 55 - 55: ooo0Oo0 - OOoOoo00oo
 oOo00oOOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiIII1II , listitem = oOO0O00oO0Ooo , isFolder = False )
 return oOo00oOOOOO
 if 84 - 84: oOo0 + ooo0Oo0 - Oooo0000 * Oooo0000
def OoooO0o ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 IIIii1iiIi = [ ]
 oooo0OOo = [ ]
 OoO00 = [ ]
 Ii11I = OOO0OOO00oo ( url )
 o0o = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( Ii11I ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0o ) [ 0 ]
 i1I1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( o0o )
 if len ( i1I1iI ) < 1 :
  i1I1iI = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( o0o )
 II1I = 1
 for I11iIi1II in i1I1iI :
  ooo0OO = I11iIi1II
  if '(' in I11iIi1II :
   I11iIi1II = I11iIi1II . split ( '(' ) [ 0 ]
   iIi1IiI = str ( ooo0OO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   IIIii1iiIi . append ( I11iIi1II )
   oooo0OOo . append ( iIi1IiI )
  else :
   IIIii1iiIi . append ( I11iIi1II )
   oooo0OOo . append ( '[COLOR aqua]Link ' + str ( II1I ) + '[/COLOR]' )
  II1I = II1I + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 I11IIIiIi11 = Iii1ii1II11i . select ( name , oooo0OOo )
 if I11IIIiIi11 < 0 :
  quit ( )
 else :
  url = IIIii1iiIi [ I11IIIiIi11 ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : iiI = liveresolver . resolve ( url )
  else : iiI = url
  oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  oOO0O00oO0Ooo . setPath ( iiI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO0O00oO0Ooo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( iiI )
  if 39 - 39: OOooO % O0 % Oooo0000 . i1IIi
def oOo00OooO0oO ( name , url , iconimage ) :
 if 16 - 16: I1iiiiI1iII / ooo0Oo0 + OOoOoo00oo / OOooO
 IIIiiI1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 IIIii1iiIi = [ ]
 oooo0OOo = [ ]
 OoO00 = [ ]
 O0O0ooOOO = [ ]
 Ii11I = OOO0OOO00oo ( url )
 o0o = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( Ii11I ) [ 0 ]
 i1I1iI = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( o0o )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0o ) [ 0 ]
 II1I = 1
 if 70 - 70: i1Ii . O0 . oOo0 . O0 + i1IIi
 for I11iIi1II in i1I1iI :
  ooo0OO = I11iIi1II
  if '(' in I11iIi1II :
   I11iIi1II = I11iIi1II . split ( '(' ) [ 0 ]
   iIi1IiI = str ( ooo0OO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   IIIii1iiIi . append ( I11iIi1II )
   oooo0OOo . append ( iIi1IiI )
   O0O0ooOOO . append ( 'Stream ' + str ( II1I ) )
  else :
   IIIii1iiIi . append ( I11iIi1II )
   oooo0OOo . append ( 'Link ' + str ( II1I ) )
   if 9 - 9: ooo0Oo0
  II1I = II1I + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 I11IIIiIi11 = Iii1ii1II11i . select ( name , oooo0OOo )
 if I11IIIiIi11 < 0 :
  quit ( )
 else :
  Oo0oOOo = oooo0OOo [ I11IIIiIi11 ]
  Oo0OoO00oOO0o = "/"
  if not Oo0oOOo . endswith ( Oo0OoO00oOO0o ) :
   OOO00O = Oo0oOOo + "/"
  else :
   OOO00O = Oo0oOOo
  url = IIIiiI1 + IIIii1iiIi [ I11IIIiIi11 ] + "%26referer=" + OOO00O
  print url
  if 99 - 99: iI1 - oOo0 - OOo0o0 % i1
  xbmc . Player ( ) . play ( url )
  if 21 - 21: i11Ii11I1Ii1i % o000o0o00o0Oo . i1IIi - OoooooooOO
def I1 ( string ) :
 iiOOOO0o = ( c for c in string if 0 < ord ( c ) < 127 )
 if 10 - 10: oOo0 % iiI1iIiI
 return '' . join ( iiOOOO0o )
 if 97 - 97: OoooooooOO - oOo0
def IIIii1II1II ( name , url , mode , iconimage , fanart , description = '' ) :
 if 58 - 58: iIii1I11I1II1 + O0
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 iiIII1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oOo00oOOOOO = True
 oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 oOO0O00oO0Ooo . setProperty ( "fanart_Image" , fanart )
 oOO0O00oO0Ooo . setProperty ( "icon_Image" , iconimage )
 oOO0O00oO0Ooo . setInfo ( 'video' , { 'Plot' : description } )
 oOo00oOOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiIII1II , listitem = oOO0O00oO0Ooo , isFolder = True )
 return oOo00oOOOOO
 if 30 - 30: i1Ii % OOoO00o * OOoOoo00oo - o000o0o00o0Oo * OOooO % i1Ii
def iiiiI11ii ( name , url , iconimage ) :
 oOo00oOOOOO = True
 oOO0O00oO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; oOO0O00oO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOo00oOOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oOO0O00oO0Ooo )
 xbmc . Player ( ) . play ( url , oOO0O00oO0Ooo , False )
 if 96 - 96: OOoO00o . O0 / OOoO00o % O0
def o0o000 ( ) :
 if 50 - 50: I1iiiiI1iII % i1IIi
 IiiO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 O0Oo00oO0O00 = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 21 - 21: OoooooooOO - iIii1I11I1II1
 II1I = [ ( IiiO0o0o , 'Cache' ) , ( O0Oo00oO0O00 , 'Thumbnails' ) , ( Ii , 'Packages' ) ]
 if 93 - 93: OOo0o0 - i1IIi11111i % Oooo0000 . Oooo0000 - i1Ii
 O00ooOo = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if O00ooOo :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for ooOOoooooo in II1I :
   if 80 - 80: i1IIi11111i - OOoOoo00oo + OoooooooOO
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % ooOOoooooo [ 1 ] )
   time . sleep ( 1 )
   if 98 - 98: OOoOoo00oo + i1IIi . iiI1iIiI - i11Ii11I1Ii1i - i1IIi11111i
   for iIIi1I1ii , IIiiii , iI111i1I1II in os . walk ( ooOOoooooo [ 0 ] ) :
    for O00 in iI111i1I1II :
     if ( O00 . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( iIIi1I1ii , O00 ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % ooOOoooooo [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 14 - 14: O0 / i1IIi / ooo0Oo0 + iIii1I11I1II1
def ooO00O00oOO ( url , mode , name , iconimage , fanart ) :
 if 40 - 40: OOoO00o . OOo0o0 + iiI1iIiI + o000o0o00o0Oo + oOo0
 with open ( I11i , "a" ) as iIi :
  iIi . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 26 - 26: iIii1I11I1II1
def OOOo ( ) :
 if 79 - 79: Oooo0000 % I1iiiiI1iII % ooo0Oo0
 with open ( I11i , "a" ) as iIi :
  Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  I1iiiiii = open ( Ii1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Iii111II = re . compile ( '<item>(.+?)</item>' ) . findall ( I1iiiiii )
  i1IiIiiI ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  if len ( Iii111II ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  for o0OO0Oo in Iii111II :
   Iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( o0OO0Oo ) [ 0 ]
   iI = re . compile ( '<url>(.+?)</url>' ) . findall ( o0OO0Oo ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0OO0Oo ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0OO0Oo ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + Iiii + '[/COLOR]' , iI , 2 , I1IiI , I1ii11iIi11i )
   if 3 - 3: oOo0 - O0 % iIii1I11I1II1 / I1iiiiI1iII . i1IIi11111i
 i1IiIiiI ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , ii11i1 , Oo )
 if 3 - 3: O0 % OoooooooOO / OOoOoo00oo
def ooOo ( ) :
 if 84 - 84: OOoOoo00oo
 with open ( IiII , "a" ) as iIi :
  Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  I1iiiiii = open ( Ii1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  Iii111II = re . compile ( '<item>(.+?)</item>' ) . findall ( I1iiiiii )
  i1IiIiiI ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  i1IiIiiI ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  if len ( Iii111II ) < 1 :
   i1IiIiiI ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , ii11i1 , Oo )
  for o0OO0Oo in Iii111II :
   Iiii = re . compile ( '<title>(.+?)</title>' ) . findall ( o0OO0Oo ) [ 0 ]
   iI = re . compile ( '<link>(.+?)</link>' ) . findall ( o0OO0Oo ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0OO0Oo ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0OO0Oo ) [ 0 ]
   i1IiIiiI ( '[COLOR skyblue]' + Iiii + '[/COLOR]' , iI , 2 , I1IiI , I1ii11iIi11i )
   if 87 - 87: i1Ii + i1IIi11111i
 i1IiIiiI ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , ii11i1 , Oo )
 if 28 - 28: OOoOoo00oo * o000o0o00o0Oo / OOo0o0
def OOoOO0OO ( ) :
 if 26 - 26: OOoO00o . OOoO00o
 with open ( I11i , "w" ) as iIi :
  iIi . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 35 - 35: oOo0 . Oooo0000 * i11iIiiIii
def iiII ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as iIi :
  iIi . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 57 - 57: iI1 . ooo0Oo0 + i11Ii11I1Ii1i
 if 43 - 43: oOo0 % OOoO00o
 if 69 - 69: OOoO00o % i1
def oOOoO ( url , iconimage , fanart ) :
 if 19 - 19: i11iIiiIii
 try :
  o0oO000oo = ''
  o00o0II1I = xbmc . Keyboard ( o0oO000oo , 'Enter Name To Save File As' )
  o00o0II1I . doModal ( )
  if o00o0II1I . isConfirmed ( ) :
   o0oO000oo = o00o0II1I . getText ( )
   if len ( o0oO000oo ) > 1 :
    II1I1I1Ii = o0oO000oo . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = iiI
  oo0 = url . split ( '/' ) [ - 1 ]
  iiIII1II = urllib2 . urlopen ( url )
  oOO = os . path . join ( o0OOO , II1I1I1Ii )
  O00 = open ( oOO , 'wb' )
  if 32 - 32: Oooo0000 * iiI1iIiI % i1Ii * OOooO . O0
  i11i1i1I1iI1 = iiIII1II . info ( )
  O0ooOo0 = int ( i11i1i1I1iI1 . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( II1I1I1Ii , O0ooOo0 ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 53 - 53: OoooooooOO - I1iiiiI1iII
  oOo = 0
  i1i = 8192
  while True :
   buffer = iiIII1II . read ( i1i )
   if not buffer :
    break
    if 5 - 5: o000o0o00o0Oo + O0 + O0 . oOo0 - i1Ii
   oOo += len ( buffer )
   O00 . write ( buffer )
   o00oo0000 = "[%3.2f%%]" % ( oOo * 100. / O0ooOo0 )
   o00oo0000 = o00oo0000 + chr ( 8 ) * ( len ( o00oo0000 ) + 1 )
   iIiiiI . update ( oOo , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( o00oo0000 , II1I1I1Ii ) )
   if 44 - 44: ooo0Oo0 % iIii1I11I1II1
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as iIi :
   iIi . write ( '<item>\n<title>' + II1I1I1Ii + '</title>\n<link>' + oOO + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 90 - 90: i11Ii11I1Ii1i + OoooooooOO % OoooooooOO
  O00 . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 35 - 35: OOoO00o / o000o0o00o0Oo * OoooooooOO . i11Ii11I1Ii1i / ooo0Oo0
  if 1 - 1: OoooooooOO + I1iiiiI1iII . i1IIi % iI1
  if 66 - 66: i1IIi11111i + o000o0o00o0Oo + iiI1iIiI - OOo0o0
  if 12 - 12: OOoO00o . I1iiiiI1iII . Oooo0000 / O0
def OO0oOOo0o ( ) :
 I1III11iiii11i1 = [ ]
 ooOo0OoO = sys . argv [ 2 ]
 if len ( ooOo0OoO ) >= 2 :
  i1iiIIi1I = sys . argv [ 2 ]
  iiI1I1IIi11i1 = i1iiIIi1I . replace ( '?' , '' )
  if ( i1iiIIi1I [ len ( i1iiIIi1I ) - 1 ] == '/' ) :
   i1iiIIi1I = i1iiIIi1I [ 0 : len ( i1iiIIi1I ) - 2 ]
  i1II1iii1i = iiI1I1IIi11i1 . split ( '&' )
  I1III11iiii11i1 = { }
  for II1I in range ( len ( i1II1iii1i ) ) :
   OOO0o = { }
   OOO0o = i1II1iii1i [ II1I ] . split ( '=' )
   if ( len ( OOO0o ) ) == 2 :
    I1III11iiii11i1 [ OOO0o [ 0 ] ] = OOO0o [ 1 ]
 return I1III11iiii11i1
 if 4 - 4: ooo0Oo0 . i1IIi - OOoO00o
i1iiIIi1I = OO0oOOo0o ( ) ; iI = None ; Ooo0OO0oOO = None ; i111i11I1Ii1I = None ; iI1I11iIIi1 = None ; ii11i1 = None ; iIIi1I = None
try : iI1I11iIIi1 = urllib . unquote_plus ( i1iiIIi1I [ "site" ] )
except : pass
try : iI = urllib . unquote_plus ( i1iiIIi1I [ "url" ] )
except : pass
try : Ooo0OO0oOO = urllib . unquote_plus ( i1iiIIi1I [ "name" ] )
except : pass
try : i111i11I1Ii1I = int ( i1iiIIi1I [ "mode" ] )
except : pass
try : ii11i1 = urllib . unquote_plus ( i1iiIIi1I [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( i1iiIIi1I [ "fanart" ] )
except : pass
try : iIIi1I = urllib . unquote_plus ( i1iiIIi1I [ "description" ] )
except : pass
if 45 - 45: i1IIi - ooo0Oo0 / O0 . o000o0o00o0Oo
if i111i11I1Ii1I == None or iI == None or len ( iI ) < 1 : i1iiI11I ( )
if 5 - 5: i1IIi11111i . iIii1I11I1II1 % iIii1I11I1II1
if 56 - 56: OoooooooOO - iI1 - i1IIi
if 8 - 8: oOo0 / OOoOoo00oo . iiI1iIiI + o000o0o00o0Oo / i11iIiiIii
if 31 - 31: i1Ii - iIii1I11I1II1 + OOoO00o . ooo0Oo0 / I1iiiiI1iII % iIii1I11I1II1
if 6 - 6: I1iiiiI1iII * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + i1IIi11111i / i1IIi
elif i111i11I1Ii1I == 1 : iII ( Ooo0OO0oOO , iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 2 : ii ( Ooo0OO0oOO , iI , ii11i1 )
elif i111i11I1Ii1I == 3 : OoooO0o ( Ooo0OO0oOO , iI , ii11i1 )
if 53 - 53: iI1 + iIii1I11I1II1
if 70 - 70: o000o0o00o0Oo
if 67 - 67: OoooooooOO
elif i111i11I1Ii1I == 4 : Oo0ooOo0o ( iI )
elif i111i11I1Ii1I == 5 : III1iII1I1ii ( iI )
elif i111i11I1Ii1I == 6 : iI1i11iII111 ( )
elif i111i11I1Ii1I == 7 : o0Oo00 ( iI )
elif i111i11I1Ii1I == 8 : O00o0OO0 ( iI )
elif i111i11I1Ii1I == 9 : o00oOOooOOo0o ( iI )
elif i111i11I1Ii1I == 10 : Iii ( iI )
elif i111i11I1Ii1I == 11 : IiiiIIiIi1 ( )
elif i111i11I1Ii1I == 12 : oOOOoo0O0oO ( iI )
elif i111i11I1Ii1I == 13 : O0Oo0oOOoooOOOOo ( iI )
elif i111i11I1Ii1I == 14 : oO00O000oO0 ( iI )
elif i111i11I1Ii1I == 15 : Oo0OO ( )
elif i111i11I1Ii1I == 16 : oOo00OooO0oO ( Ooo0OO0oOO , iI , ii11i1 )
elif i111i11I1Ii1I == 17 : iIIiIi1iIII1 ( iI )
elif i111i11I1Ii1I == 18 : O000OOOOOo ( iI )
elif i111i11I1Ii1I == 19 : OoO ( iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 20 : o00o0 ( )
elif i111i11I1Ii1I == 21 : OoO0o ( iI )
elif i111i11I1Ii1I == 22 : oOo0OOoO0 ( iI )
elif i111i11I1Ii1I == 23 : oo0OO00OoooOo ( )
elif i111i11I1Ii1I == 24 : i1i1iI1iiiI ( iI )
elif i111i11I1Ii1I == 25 : iiIiIIIiiI ( iI , ii11i1 )
elif i111i11I1Ii1I == 26 : o0O0o ( iI )
elif i111i11I1Ii1I == 27 : i1II1i ( iI , ii11i1 )
elif i111i11I1Ii1I == 28 : iII1ii1 ( )
elif i111i11I1Ii1I == 29 : o00I1 ( iI )
elif i111i11I1Ii1I == 30 : i11i11111i1i ( iI )
elif i111i11I1Ii1I == 31 : ii1 ( iI )
elif i111i11I1Ii1I == 32 : ooOoOO0OoO00o ( iI )
elif i111i11I1Ii1I == 33 : OoOooOoO ( iI )
elif i111i11I1Ii1I == 34 : oO00O0 ( iI )
elif i111i11I1Ii1I == 35 : O0oooo00o0Oo ( )
elif i111i11I1Ii1I == 36 : ii1Ii1IiIIi ( iI )
elif i111i11I1Ii1I == 37 : IIi1IIIIi ( iI , ii11i1 )
elif i111i11I1Ii1I == 38 : I1i11ii11 ( )
elif i111i11I1Ii1I == 39 : ooo ( iI )
if 29 - 29: O0 - i11iIiiIii - i11Ii11I1Ii1i + OOoOoo00oo * I1iiiiI1iII
elif i111i11I1Ii1I == 45 : IIi1ii1Ii ( )
elif i111i11I1Ii1I == 46 : ii1O000OOO0OOo ( iI )
elif i111i11I1Ii1I == 47 : iIi1 ( Ooo0OO0oOO , iI , ii11i1 )
elif i111i11I1Ii1I == 48 : IIiiI ( )
elif i111i11I1Ii1I == 49 : OOo ( iI )
elif i111i11I1Ii1I == 50 : OO0ooo0oOO ( iI )
elif i111i11I1Ii1I == 51 : iii1 ( )
elif i111i11I1Ii1I == 52 : iiI11I1i1i1iI ( iI )
elif i111i11I1Ii1I == 53 : i111I ( iI )
elif i111i11I1Ii1I == 54 : IiI1I1 ( iI , ii11i1 )
if 2 - 2: i1IIi - i1Ii + iiI1iIiI . i1IIi11111i * i1IIi11111i / Oooo0000
if 93 - 93: i1IIi
if 53 - 53: OoooooooOO + ooo0Oo0 + OOo0o0
elif i111i11I1Ii1I == 59 : I11iiiii1II ( )
elif i111i11I1Ii1I == 60 : I1iiIIIi11 ( iI )
elif i111i11I1Ii1I == 61 : ii11I1 ( Ooo0OO0oOO , iI , ii11i1 )
if 24 - 24: OOoO00o - I1iiiiI1iII - OOoO00o * o000o0o00o0Oo . OoooooooOO / I1iiiiI1iII
elif i111i11I1Ii1I == 66 : Oo0000oOo ( )
elif i111i11I1Ii1I == 67 : I1IIIiI1I1ii1 ( iI )
elif i111i11I1Ii1I == 68 : i11iiiiI1i ( iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 69 : OOOoO000 ( iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 70 : i11i1iiI1i ( iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 71 : OoOIii11iI11i1I ( )
elif i111i11I1Ii1I == 72 : O0oOo00o0 ( )
if 66 - 66: ooo0Oo0
if 97 - 97: i1IIi - OoooooooOO / oOo0 * iiI1iIiI
if 55 - 55: i1IIi11111i . OOoO00o
if 87 - 87: i1IIi11111i % iIii1I11I1II1
elif i111i11I1Ii1I == 884 : O00o00O ( )
elif i111i11I1Ii1I == 885 : iiII ( )
elif i111i11I1Ii1I == 886 : ooOo ( )
elif i111i11I1Ii1I == 887 : oOOoO ( iI , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 888 : II1IIIIiII1i ( )
elif i111i11I1Ii1I == 889 : ooO00O00oOO ( iI , i111i11I1Ii1I , Ooo0OO0oOO , ii11i1 , I1ii11iIi11i )
elif i111i11I1Ii1I == 890 : OOOo ( )
elif i111i11I1Ii1I == 891 : OOoOO0OO ( )
elif i111i11I1Ii1I == 892 : o0o000 ( )
if 100 - 100: oOo0 . iiI1iIiI * oOo0 - iiI1iIiI . iI1 * OOooO
if i111i11I1Ii1I == None or iI == None or len ( iI ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 89 - 89: i1 + I1iiiiI1iII * oOo0
if 28 - 28: OoooooooOO . OOo0o0 % o000o0o00o0Oo / i1IIi / OOoOoo00oo
if 36 - 36: i1IIi11111i + iI1 - I1iiiiI1iII + iIii1I11I1II1 + OoooooooOO
if 4 - 4: i11Ii11I1Ii1i . iI1 + OOooO * oOo0 . i1Ii
if 87 - 87: Oooo0000 / i1 / i11iIiiIii
if 74 - 74: OOo0o0 / o000o0o00o0Oo % i1IIi11111i
if 88 - 88: Oooo0000 - i11iIiiIii % i1IIi11111i * iI1 + o000o0o00o0Oo
if 52 - 52: i11Ii11I1Ii1i . iiI1iIiI + Oooo0000 % i1
if 62 - 62: i1IIi11111i
if 15 - 15: iI1 + OOooO . OOoOoo00oo * i1 . Oooo0000
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3