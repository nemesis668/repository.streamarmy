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
 OO00o0OOO0 ( )
 OOO00 ( )
 iiiiiIIii = i1iII1IiiIiI1
 O000OO0 = iiiiiIIii
 I11iii1Ii = int ( datetime . now ( ) . strftime ( '%H%M' ) )
 if ( I11iii1Ii >= 0000 ) and ( I11iii1Ii <= 1159 ) : I1IIiiIiii = "Morning"
 elif ( I11iii1Ii >= 1200 ) and ( I11iii1Ii <= 1759 ) : I1IIiiIiii = "Afternoon"
 else : I1IIiiIiii = "Evening"
 O000oo0O ( '[COLOR yellow]Good[COLOR aqua] ' + str ( I1IIiiIiii ) + '[COLOR yellow] From Nemesis Team[/COLOR]' , 'url' , '12' , I1IiI , Oo )
 O000oo0O ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 999 , I1IiI , Oo )
 try :
  OOOO = i11i1 ( i1iII1IiiIiI1 )
  IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( OOOO )
  for i1I1iI in IIIii1II1II :
   try :
    if '<m3u>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 11 , o0O , I1ii11iIi11i )
    elif '<mamahdsports>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<mamahdsports>(.+?)</mamahdsports>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 14 , o0O , I1ii11iIi11i )
    elif '<atc>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<atc>(.+?)</atc>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 6 , o0O , I1ii11iIi11i )
    elif '<scanner>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<scanner>(.+?)</scanner>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 11 , o0O , I1ii11iIi11i )
    elif '<cartoons>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 29 , o0O , I1ii11iIi11i )
    elif '<Adult>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<Adult>(.+?)</Adult>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 38 , o0O , I1ii11iIi11i )
    elif '<Anime>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<Anime>(.+?)</Anime>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 51 , o0O , I1ii11iIi11i )
    elif '<audiobooks>' in i1I1iI :
     oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiiiiIIii = re . compile ( '<audiobooks>(.+?)</audiobooks>' ) . findall ( i1I1iI ) [ 0 ]
     O00oO ( oo0OooOOo0 , iiiiiIIii , 59 , o0O , I1ii11iIi11i )
    elif '<folder>' in i1I1iI :
     I11i1I1I = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i1I1iI )
     for oo0OooOOo0 , iiiiiIIii , o0O , I1ii11iIi11i in I11i1I1I :
      O00oO ( oo0OooOOo0 , iiiiiIIii , 1 , o0O , I1ii11iIi11i )
    else :
     oO0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( i1I1iI )
     if len ( oO0Oo ) == 1 :
      I11i1I1I = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i1I1iI )
      oOOoo0Oo = len ( IIIii1II1II )
      for oo0OooOOo0 , iiiiiIIii , o0O , I1ii11iIi11i in I11i1I1I :
       if 'youtube.com/playlist' in iiiiiIIii :
        O00oO ( oo0OooOOo0 , iiiiiIIii , 2 , o0O , I1ii11iIi11i )
       else :
        O000oo0O ( oo0OooOOo0 , iiiiiIIii , 2 , o0O , I1ii11iIi11i )
     elif len ( oO0Oo ) > 1 :
      oo0OooOOo0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
      o0O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
      I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
      O000oo0O ( oo0OooOOo0 , O000OO0 , 3 , o0O , I1ii11iIi11i )
   except : pass
   if 78 - 78: O00OoOoo00
  O000oo0O ( "[COLOR yellow]---------------------------------------[/COLOR]" , 'url2' , 884 , I1IiI , Oo )
  try :
   file = xbmc . translatePath ( "special://home/userdata/addon_data/script.module.urlresolver/settings.xml" )
   I1IIiiIiii = open ( file ) . read ( )
   OO00Oo = re . compile ( '<setting id="RealDebridResolver_token"(.+?)/' ) . findall ( I1IIiiIiii ) [ 0 ]
   OO00Oo = OO00Oo . strip ( )
   iiiiiIIii = 'plugin://script.module.urlresolver/?mode=auth_rd'
   if 'value=""' in OO00Oo :
    O0OOO0OOoO0O = ( '[COLOR yellow]Real Debrid Not Active Click To Pair **[/COLOR]' )
    O000oo0O ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( O0OOO0OOoO0O ) + '[/COLOR]' , iiiiiIIii , 2 , I1IiI , Oo )
   else :
    O0OOO0OOoO0O = ( '[COLOR yellow]Real Debrid Active **[/COLOR]' )
    O000oo0O ( '[COLOR yellow]** [COLOR aqua]DEBRID STATUS : ' + str ( O0OOO0OOoO0O ) + '[/COLOR]' , 'url' , 999 , I1IiI , Oo )
  except : pass
  O00Oo000ooO0 = 'https://i.imgur.com/4Pzgdwu.png'
  O00oO ( "[COLOR yellow]** [COLOR aqua]NEMESIS FAVOURITES[COLOR yellow] **[/COLOR]" , 'url2' , 890 , O00Oo000ooO0 , Oo )
  OoO0O00 = 'https://i.imgur.com/Om0Lq7V.png'
  O00oO ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS[COLOR yellow] **[/COLOR]" , 'test' , 886 , OoO0O00 , Oo )
  IIiII = 'https://i.imgur.com/klnhdFx.png'
  O00oO ( "[COLOR yellow]** [COLOR aqua]MAINTENANCE[COLOR yellow] **[/COLOR]" , 'url2' , 884 , IIiII , Oo )
 except :
  o0 = Iii1ii1II11i . select ( '[COLOR aqua]No Internet Connection Detected, Would you Like Offline Mode?[/COLOR]' , [ '[COLOR aqua]Yes[/COLOR]' , '[COLOR aqua]No[/COLOR]' ] )
  if o0 == 0 :
   O000oo0O ( "[COLOR yellow]** OFFLINE MODE [COLOR yellow]**[/COLOR]" , 'test' , 999 , I1IiI , Oo )
   O00oO ( "[COLOR yellow]** [COLOR aqua]NEMESIS DOWNLOADS [COLOR yellow]**[/COLOR]" , 'test' , 886 , I1IiI , Oo )
  if o0 == 1 :
   quit ( )
   if 62 - 62: iIii1I11I1II1 * Oooo0000
 iI1 ( )
 if 26 - 26: oooOOOOO . i1iIIi1
def oOOOOo0 ( name , url , iconimage , fanart ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 O000OO0 = url
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  try :
   if '<image>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 9 , iconimage , fanart )
   elif '<playlist>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<playlist>(.+?)</playlist>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 22 , iconimage , fanart )
   elif '<fullhigh>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<fullhigh>(.+?)</fullhigh>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 18 , iconimage , fanart )
   elif '<motorsports>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<motorsports>(.+?)</motorsports>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 23 , iconimage , fanart )
   elif '<American>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<American>(.+?)</American>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<Rugby>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<WWE>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<UFC>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<Tennis>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<Boxing>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<Golf>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<Cricket>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 17 , iconimage , fanart )
   elif '<topmov>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<topmov>(.+?)</topmov>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 888 , iconimage , fanart )
   elif '<cinema>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<cinema>(.+?)</cinema>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 26 , iconimage , fanart )
   elif '<genti>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<genti>(.+?)</genti>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 28 , iconimage , fanart )
   elif '<cartoons>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 29 , iconimage , fanart )
   elif '<searchmovie>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<searchmovie>(.+?)</searchmovie>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 33 , iconimage , fanart )
   elif '<cctv>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<cctv>(.+?)</cctv>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 45 , iconimage , fanart )
   elif '<shadow>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<shadow>(.+?)</shadow>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 48 , iconimage , fanart )
   elif '<tvguide>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<tvguide>(.+?)</tvguide>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 66 , iconimage , fanart )
   elif '<tvsearch>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<tvsearch>(.+?)</tvsearch>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 71 , iconimage , fanart )
   elif '<trendingtv>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<trendingtv>(.+?)</trendingtv>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 72 , iconimage , fanart )
   elif '<musicchans>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<musicchans>(.+?)</musicchans>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 49 , iconimage , fanart )
   elif '<shighlights>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 20 , iconimage , fanart )
   elif '<putlockermovies>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<putlockermovies>(.+?)</putlockermovies>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 42 , iconimage , fanart )
   elif '<moviegenre>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<moviegenre>(.+?)</moviegenre>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 44 , iconimage , fanart )
   elif '<acestreamfootie>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<acestreamfootie>(.+?)</acestreamfootie>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 73 , iconimage , fanart )
   elif '<lordjd>' in i1I1iI :
    oO0Oo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( i1I1iI )
    if len ( oO0Oo ) == 1 :
     I11i1I1I = re . compile ( '<title>(.+?)</title>.+?lordjd>(.+?)</lordjd>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i1I1iI )
     oOOoo0Oo = len ( IIIii1II1II )
     for name , url , iconimage , fanart in I11i1I1I :
      if 'youtube.com/playlist' in url :
       O00oO ( name , url , 2 , iconimage , fanart )
      else :
       iiII1i1 ( name , url , 2 , iconimage , fanart )
    elif len ( oO0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     iiII1i1 ( name , O000OO0 , 3 , iconimage , fanart )
   elif '<reddit>' in i1I1iI :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
    url = re . compile ( '<reddit>(.+?)</reddit>' ) . findall ( i1I1iI ) [ 0 ]
    O00oO ( name , url , 4 , iconimage , fanart )
   elif '<sportsdevil>' in i1I1iI :
    oO0Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i1I1iI )
    if len ( oO0Oo ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i1I1iI ) [ 0 ]
     o00oOO0o = re . compile ( '<referer>(.+?)</referer>' ) . findall ( i1I1iI ) [ 0 ]
     OOO00O = o00oOO0o
     OOoOO0oo0ooO = "/"
     if not OOO00O . endswith ( OOoOO0oo0ooO ) :
      O0o0O00Oo0o0 = OOO00O + "/"
     else :
      O0o0O00Oo0o0 = OOO00O
     OOOO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = OOOO + '%26referer=' + O0o0O00Oo0o0
     O000oo0O ( name , url , 10 , iconimage , fanart )
    elif len ( oO0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     O000oo0O ( name , O000OO0 , 16 , iconimage , fanart )
     if 87 - 87: IiIi1Iii1I1 * ooo0Oo0 % i11iIiiIii % Oooo0000 - i1iIIII
   elif '<folder>' in i1I1iI :
    I11i1I1I = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i1I1iI )
    for name , url , iconimage , fanart in I11i1I1I :
     O00oO ( name , url , 1 , iconimage , fanart )
     if 68 - 68: i1iIIi1 % i1IIi . IiiIII111ii . o000o0o00o0Oo
   else :
    oO0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( i1I1iI )
    if len ( oO0Oo ) == 1 :
     I11i1I1I = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i1I1iI )
     oOOoo0Oo = len ( IIIii1II1II )
     for name , url , iconimage , fanart in I11i1I1I :
      if 'youtube.com/playlist' in url :
       O00oO ( name , url , 2 , iconimage , fanart )
      else :
       O000oo0O ( name , url , 2 , iconimage , fanart )
    elif len ( oO0Oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i1I1iI ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i1I1iI ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i1I1iI ) [ 0 ]
     O000oo0O ( name , O000OO0 , 3 , iconimage , fanart )
  except : pass
  if 92 - 92: oooOOOOO . i1iIIi1
 iI1 ( )
 if 31 - 31: i1iIIi1 . Oooo0000 / O0
 if 89 - 89: Oooo0000
 if 68 - 68: i1 * OoooooooOO % O0 + i1 + IiIi1Iii1I1
 if 4 - 4: IiIi1Iii1I1 + O0 * i1iIIII
 if 55 - 55: ooo0Oo0 + iIii1I11I1II1 / Oooo0000 * i1iII1I1i1i1 - i11iIiiIii - iiiI11
 if 25 - 25: o000o0o00o0Oo
 if 7 - 7: i1IIi / iiI1iIiI * i1iIIi1 . IiiIII111ii . iIii1I11I1II1
 if 13 - 13: i1iIIII / i11iIiiIii
def Iiii ( url ) :
 if 75 - 75: Oooo0000 % i1IIi11111i % i1IIi11111i . i1iIIi1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( 'data-event-action="title"(.+?)<span class="domain">' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  try :
   III1iII1I1ii = re . compile ( 'rel=.+?>(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
   url = re . compile ( 'href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   url = 'https://www.reddit.com' + url
   I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
   O00oO ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 5 , I1IiI , I1ii11iIi11i )
  except : pass
  if 61 - 61: i11Ii11I1Ii1i
def O0OOO ( url ) :
 if 10 - 10: i1iIIII * O00OoOoo00 % Oooo0000 / iiI1iIiI / Oooo0000
 iIIi1i1 = [ "reddit" , "redd.it" , "facebook" , "imgur" , "twitter" , "discord" , "soccerstreams" ]
 i1IIIiiII1 = [ "yalla" , "mlbstreams" , "livetvleak" ]
 I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
 O000oo0O ( "[COLOR yellow]Yellow Links Are Recommend[/COLOR]" , 'url1' , 999 , I1IiI , I1ii11iIi11i )
 OOOO = i11i1 ( url )
 oO0Oo = 0
 OOOOoOoo0O0O0 = re . compile ( 'href="([^"]+)' ) . findall ( OOOO )
 for url in OOOOoOoo0O0O0 :
  if 'http' in url :
   if not any ( x in url . lower ( ) for x in iIIi1i1 ) :
    oO0Oo += 1
    III1iII1I1ii = "Link " + str ( oO0Oo ) + " :: "
    I1IiI = 'http://png-4.findicons.com/files/icons/1788/large_icons_social/512/reddit.png'
    OOOo00oo0oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     O000oo0O ( "[COLOR skyblue]" + III1iII1I1ii + url + "[/COLOR]" , url , 2 , I1IiI , I1ii11iIi11i )
    elif any ( x in url . lower ( ) for x in i1IIIiiII1 ) :
     O000oo0O ( "[COLOR yellow]" + III1iII1I1ii + url + "[/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
    else :
     O000oo0O ( "[COLOR skyblue]" + III1iII1I1ii + url + "[/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
     if 1 - 1: i1 - i1iII1I1i1i1 . O00OoOoo00 . i1 / ooo0Oo0 + O00OoOoo00
     if 78 - 78: O0 . i1iII1I1i1i1 . i11Ii11I1Ii1i % i1iIIII
     if 49 - 49: iiiI11 / i1 . i11Ii11I1Ii1i
def ooOOoooooo ( url ) :
 if 1 - 1: ooo0Oo0 / i1IIi11111i % oooOOOOO * IiiIII111ii . i11iIiiIii
 if url == 'Football' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  III1Iiii1I11 = i11i1 ( 'http://wizhdsports.is/sport/Cricket' )
 IIII = dom_parser2 . parse_dom ( III1Iiii1I11 , 'div' , { 'class' : 'card' } )
 IIII = [ ( dom_parser2 . parse_dom ( iiIiI , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( iiIiI , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( iiIiI , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( iiIiI , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for iiIiI in IIII ]
 if len ( IIII ) < 1 :
  O000oo0O ( "[COLOR aqua][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , o0O , Oo , '' )
 IIII = [ ( iiIiI [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , iiIiI [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , iiIiI [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , iiIiI [ 2 ] [ 0 ] . content ) if iiIiI [ 2 ] else 'Upcoming' , iiIiI [ 3 ] [ 0 ] . content ) for iiIiI in IIII ]
 if 91 - 91: oooOOOOO % i1IIi % iIii1I11I1II1
 if 20 - 20: i1iIIII % iiiI11 / iiiI11 + iiiI11
 if 45 - 45: i1iII1I1i1i1 - IiiIII111ii - OoooooooOO - i1 . i11Ii11I1Ii1i / O0
 if 51 - 51: O0 + oooOOOOO
 IIII = [ ( iiIiI [ 0 ] , iiIiI [ 1 ] , iiIiI [ 2 ] , iiIiI [ 3 ] , iiIiI [ 4 ] ) for iiIiI in IIII ]
 IIIII11I1IiI = 0
 i1I = 0
 iIiiiI . create ( "[COLOR aqua]WizHD[/COLOR]" , '[COLOR aqua]' + "Searching For Matches" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 for iiIiI in IIII :
  OoOO = iiIiI [ 0 ]
  iIiiiI . update ( 100 , '[COLOR aqua]Searching For Matches :: Found [COLOR yellow]%s[COLOR aqua] Matches So Far[/COLOR]' % str ( IIIII11I1IiI ) )
  IIIII11I1IiI += 1
  time . sleep ( 0.10 )
  OoOO = ooOOO0 ( OoOO )
  o0o = iiIiI [ 1 ]
  O0OOoO00OO0o = iiIiI [ 3 ]
  if 'Match Over' in O0OOoO00OO0o :
   i1I += 1
  I1111IIIIIi = dom_parser2 . parse_dom ( iiIiI [ 4 ] , 'a' )
  for III1Iiii1I11 in I1111IIIIIi :
   Iiii1i1 = re . sub ( '<.+?>' , '' , III1Iiii1I11 . content )
   OOOO = III1Iiii1I11 . attrs [ 'href' ]
   OOOO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + OOOO
   if not 'Match Over' in O0OOoO00OO0o :
    O000oo0O ( '[COLOR aqua]' + OoOO + '[COLOR yellow]' + ' ' + O0OOoO00OO0o + '[/COLOR]' , OOOO , 2 , o0O , I1ii11iIi11i )
 iIiiiI . update ( 100 , '[COLOR aqua]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR aqua]Matches In Total' % str ( IIIII11I1IiI ) , '[COLOR yellow]%s[COLOR aqua] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( i1I ) )
 time . sleep ( 3 )
 iIiiiI . close ( )
 if 84 - 84: iiI1iIiI . iIii1I11I1II1 % OoooooooOO + iiiI11 % OoooooooOO % i1
def IIi1 ( url ) :
 if 45 - 45: oooOOOOO / oooOOOOO + i1iIIi1 + IiIi1Iii1I1
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="cover">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  if 47 - 47: i1IIi11111i + IiIi1Iii1I1
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 19 , I1IiI , Oo , '' )
  if 82 - 82: i11Ii11I1Ii1i . IiiIII111ii - iIii1I11I1II1 - IiiIII111ii * i11Ii11I1Ii1i
 try :
  ooO0oOOooOo0 = re . compile ( 'rel="next" href="(.+?)">' ) . findall ( OOOO ) [ 0 ]
  I1IiI = o0O
  O00oO ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , ooO0oOOooOo0 , 18 , o0O , Oo , '' )
 except : pass
 if 38 - 38: i1iIIi1
def Ooo00o0Oooo ( url , iconimage , fanart ) :
 if 84 - 84: i1IIi11111i % i11Ii11I1Ii1i . i11iIiiIii / i1
 O000oo0O ( "[COLOR yellow]" + "Please Pair Openload or Use Real Debrid" + "[/COLOR]" , 'url' , 999 , I1IiI , fanart , '' )
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<p style="text-align:center"><iframe(.+?)</p>' ) . findall ( OOOO )
 if 80 - 80: i1iIIi1 . i11iIiiIii - i1IIi11111i
 for oO0Oo in IIIii1II1II :
  url = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = str . lower ( url )
  if '1e' in OOOo00oo0oO :
   III1iII1I1ii = '1st Half'
  else :
   III1iII1I1ii = '2nd Half'
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 2 , I1IiI , fanart , '' )
  if 25 - 25: i1
def oOo0oO ( ) :
 if 51 - 51: ooo0Oo0 - i1iII1I1i1i1 + i11Ii11I1Ii1i * iiiI11 . O00OoOoo00 + i1iII1I1i1i1
 iiiiiIIii = 'http://www.goalsarena.org/en/'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II )
 for oO0o0Ooooo , OOo0oO00ooO00 in OoO0o :
  O00oO ( "[COLOR skyblue]" + OOo0oO00ooO00 + "[/COLOR]" , oO0o0Ooooo , 21 , I1IiI , Oo , '' )
  if 90 - 90: Oooo0000 * i1iIIi1 + i1IIi11111i
def OO ( url ) :
 if 83 - 83: O0 / iiI1iIiI - i1 - i1iIIII
 if 36 - 36: IiiIII111ii
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 o0 = Iii1ii1II11i . select ( '[COLOR skyblue]Choose Normal Or Extended Highlights[/COLOR]' , [ '[COLOR skyblue]Normal[/COLOR]' , '[COLOR skyblue]Extended[/COLOR]' ] )
 if o0 == 0 :
  try :
   IIIii1II1II = re . compile ( '<iframe src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Any Highlights Available[/COLOR]' , I1IiI , 9000 )
   quit ( )
  if 'ok.ru' in IIIii1II1II :
   I11iI ( oo0OooOOo0 , IIIii1II1II , o0O )
  I1iI1ii1II = i11i1 ( IIIii1II1II )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
  url = 'https:' + url
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  quit ( 0 )
 if o0 == 1 :
  try :
   IIIii1II1II = re . compile ( '<iframe src="(.+?)"' ) . findall ( OOOO ) [ 1 ]
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This Game Doesn\'t Have Extended Highlight Available[/COLOR]' , I1IiI , 9000 )
   time . sleep ( 2 )
   OO ( url )
  I1iI1ii1II = i11i1 ( IIIii1II1II )
  url = re . compile ( '<source src="(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
  url = 'https:' + url
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  quit ( 0 )
  if 74 - 74: o000o0o00o0Oo + i11Ii11I1Ii1i / i1
def oOo0O0Oo00oO ( ) :
 if 7 - 7: IiiIII111ii * i1iIIi1 % iiiI11 - i1IIi11111i
 iiiiiIIii = 'http://m.liveatc.net/feeds/'
 OOOO = i1i ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li>(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://m.liveatc.net' + iiiiiIIii
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 7 , I1IiI , Oo , '' )
  if 56 - 56: o000o0o00o0Oo % O0 - iiI1iIiI
def O00o0OO0 ( url ) :
 if 35 - 35: i1iII1I1i1i1 % IiIi1Iii1I1 / i1iIIi1 + iIii1I11I1II1 . OoooooooOO . iiI1iIiI
 if 71 - 71: IiiIII111ii * i11Ii11I1Ii1i * i1iII1I1i1i1
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li>(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?>(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 8 , I1IiI , Oo , '' )
  if 56 - 56: iiI1iIiI
def O0oO ( url ) :
 url = url . replace ( ' ' , '%20' )
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li>(.+?)</a>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '(.+?)</li>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://m.liveatc.net' + url
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 9 , I1IiI , Oo , '' )
  if 73 - 73: o000o0o00o0Oo * i11iIiiIii % i1iII1I1i1i1 . o000o0o00o0Oo
def OOOOo0 ( url ) :
 if 49 - 49: i11Ii11I1Ii1i % O0 . Oooo0000 + i1iII1I1i1i1 / iiI1iIiI
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li>(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  try :
   III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 10 , I1IiI , Oo , '' )
  except :
   O000oo0O ( "[COLOR yellow]Sorry Stream Down At The Moment, Try Others[/COLOR]" , 'url' , 999 , I1IiI , Oo , '' )
   if 72 - 72: IiIi1Iii1I1 * ooo0Oo0 . iiI1iIiI - i11Ii11I1Ii1i + i1IIi
def iIi1ii ( ) :
 if 58 - 58: Oooo0000 % i1IIi11111i
 O00oO ( "[COLOR yellow]TOP 25 FEEDS[/COLOR]" , 'url' , 15 , I1IiI , Oo , '' )
 iiiiiIIii = 'http://m.broadcastify.com/?a=la&coid=1'
 OOOO = i1i ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://m.broadcastify.com' + iiiiiIIii
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 12 , I1IiI , Oo , '' )
  if 50 - 50: i1iIIi1 . i1IIi11111i
def ooO0OO ( url ) :
 if 54 - 54: IiiIII111ii + iiiI11 % i1 + OoooooooOO - O0 - i1IIi11111i
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 13 , I1IiI , Oo , '' )
  if 77 - 77: i1iIIII * iIii1I11I1II1
def oO00oOOoooO ( url ) :
 if 46 - 46: iiI1iIiI - OoooooooOO - O00OoOoo00 * i11Ii11I1Ii1i
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://m.broadcastify.com' + url
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 14 , I1IiI , Oo , '' )
  if 34 - 34: O00OoOoo00 - oooOOOOO / i1iIIII + o000o0o00o0Oo * iiiI11
def OOOO0OoOO0o0o ( url ) :
 if 95 - 95: i11iIiiIii
 OOOO = i1i ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 try :
  IIIii1II1II = re . compile ( '<audio width=.+?src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR aqua]Sorry Link Down At The Moment[/COLOR]' , I1IiI , 5000 )
 iI1111iiii ( IIIii1II1II )
 if 67 - 67: OoooooooOO / iiI1iIiI * iiiI11 + O00OoOoo00
def OooOo0ooo ( ) :
 if 71 - 71: i1iIIi1 + iiiI11
 iiiiiIIii = 'http://m.broadcastify.com/?a=top25'
 OOOO = i1i ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<li class="arrow">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  iI1111ii1I = III1iII1I1ii . split ( ')' ) [ 0 ] . replace ( '(' , '' )
  III1iII1I1ii = III1iII1I1ii . split ( ')' ) [ - 1 ] . strip ( )
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://m.broadcastify.com' + iiiiiIIii
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[COLOR yellow] :: " + iI1111ii1I + " Listening" + "[/COLOR]" , iiiiiIIii , 14 , I1IiI , Oo , '' )
  if 45 - 45: i1IIi + i1IIi11111i
def OOO ( url ) :
 if 25 - 25: i1iII1I1i1i1 - i1 . iIii1I11I1II1 % i11iIiiIii % o000o0o00o0Oo
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in III1iII1I1ii :
    OOOo00oo0oO = 'https://www.youtube.com' + url
    O000oo0O ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
    if 92 - 92: OoooooooOO * i1iIIi1
def o0000oO ( ) :
 if 11 - 11: IiIi1Iii1I1 / Oooo0000 - IiiIII111ii * OoooooooOO + OoooooooOO . Oooo0000
 iiiiiIIii = 'http://burningwhee1s.blogspot.co.uk/'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( IIIii1II1II )
 for OOOO , III1iII1I1ii in OoO0o :
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OOOO , 24 , I1IiI , Oo , '' )
  if 26 - 26: iiiI11 % o000o0o00o0Oo
def o00Oo0oooooo ( url ) :
 if 76 - 76: O00OoOoo00 / i1iIIII . O0 % iiI1iIiI . i1IIi11111i + IiiIII111ii
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 71 - 71: i1iIIi1 . i11Ii11I1Ii1i
def oo0 ( url , iconimage ) :
 if 61 - 61: Oooo0000 - i1iIIII - i1IIi
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( IIIii1II1II )
 try :
  for oO0Oo in OoO0o :
   III1iII1I1ii = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    IiI1iIiIIIii = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     IiI1iIiIIIii = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     IiI1iIiIIIii = ''
   III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
   IiI1iIiIIIii = o0Oo0oO0oOO00 ( IiI1iIiIIIii )
   oOoO = re . compile ( '<option value="(.+?)"' ) . findall ( oO0Oo ) [ 1 ]
   O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "  " + IiI1iIiIIIii + "[/COLOR]" , oOoO , 2 , I1IiI , Oo , '' )
 except :
  O000oo0O ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 81 - 81: Oooo0000 - Oooo0000 . oooOOOOO
def o0OoOo00o0o ( ) :
 if 41 - 41: IiIi1Iii1I1 % i1 - ooo0Oo0 * i1iIIi1 * ooo0Oo0
 if 69 - 69: i1iIIII - OoooooooOO + i1IIi11111i - O00OoOoo00
 iiiiiIIii = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 OOOO = i11i1 ( iiiiiIIii )
 I11i1I1I = json . loads ( OOOO )
 ii = I11i1I1I [ 'results' ]
 for O0oOo00o in ii :
  o0ooooO0o0O = 'https://image.tmdb.org/t/p/w640'
  III1iII1I1ii = O0oOo00o [ 'title' ]
  I1IiI = O0oOo00o [ 'poster_path' ]
  iiIi11iI1iii = O0oOo00o [ 'id' ]
  I1IiI = o0ooooO0o0O + I1IiI
  I1ii11iIi11i = O0oOo00o [ 'backdrop_path' ]
  I1ii11iIi11i = o0ooooO0o0O + I1ii11iIi11i
  oo000 = O0oOo00o [ 'overview' ]
  iiIi11iI1iii = str ( iiIi11iI1iii )
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , III1iII1I1ii , 33 , I1IiI , I1ii11iIi11i , oo000 )
  if 63 - 63: IiIi1Iii1I1 + i1iIIII * iiiI11
def iI1I111I ( url ) :
 if 97 - 97: i1IIi . i1iII1I1i1i1 / oooOOOOO * O0
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div id="movie-featured"(.+?)</span>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1ii11iIi11i = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = re . compile ( '<i>(.+?)</i>' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = III1iII1I1ii . strip ( )
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 27 , I1IiI , I1ii11iIi11i , '' )
 try :
  o0O0o = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( OOOO ) [ 0 ]
  OO0o0o00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  O00oO ( '[COLOR yellow]Next Page >>[/COLOR]' , o0O0o , 26 , OO0o0o00 , I1ii11iIi11i )
 except : pass
 if 12 - 12: i1IIi + i1IIi - o000o0o00o0Oo * ooo0Oo0 % ooo0Oo0 - i11Ii11I1Ii1i
def o0OOOOooo ( url , iconimage ) :
 if 94 - 94: OoooooooOO + ooo0Oo0 / Oooo0000 * i1iIIII
 OOOO = i11i1 ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( OOOO ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 IIIii1II1II = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( OOOO )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 iiIiI = 1
 o0OOo0o0O0O = [ ]
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  o0OOo0o0O0O . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( iiIiI ) )
  time . sleep ( 0.02 )
  iiIiI += 1
  III1iII1I1ii = re . compile ( '(.+?)</p>' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'Server' , '' )
  III1iII1I1ii = III1iII1I1ii . strip ( )
 o0OO0o0oOOO0O = 1
 I1IIiiIiii = 0
 iI = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 2 - 2: IiIi1Iii1I1 / oooOOOOO . oooOOOOO % i1iIIi1
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if I1IIiiIiii > len ( o0OOo0o0O0O ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 11 - 11: iIii1I11I1II1
  if iI == 0 :
   I1IIiiIiii += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( I1IIiiIiii ) + "[/COLOR]" , '' )
   try :
    OOOO = i11i1 ( o0OOo0o0O0O [ I1IIiiIiii ] )
    OoO0o = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( OOOO ) [ 0 ]
    IiIIII1i11I = base64 . b64decode ( OoO0o )
    url = re . compile ( 'src="(.+?)"' ) . findall ( IiIIII1i11I ) [ 0 ]
    OOOiII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    OOo = open ( OOOiII1 ) . read ( )
    IIii11Ii1i1I = re . compile ( '<url>(.+?)</url>' ) . findall ( OOo )
    for Oooo0O in IIii11Ii1i1I :
     oo00O0oO0O0 = re . compile ( '<bad>(.+?)<bad>' ) . findall ( Oooo0O ) [ 0 ]
     if url == oo00O0oO0O0 :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( I1IIiiIiii ) )
      time . sleep ( 0.5 )
      iI = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     ooo0OO0O0Oo = liveresolver . resolve ( url )
    else : ooo0OO0O0Oo = url
    O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( I1IIiiIiii ) )
    time . sleep ( 0.5 )
    iI = 5
    pass
  if iI == 5 :
   iI = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   iI += 1
   if 62 - 62: O0 % O00OoOoo00 . O00OoOoo00 - iIii1I11I1II1 / i11iIiiIii
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 OOOiII1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 OOO00O = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if OOO00O :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( OOOiII1 , "a" ) as iiiII :
   iiiII . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 41 - 41: ooo0Oo0
def IIiIi ( url ) :
 if 91 - 91: o000o0o00o0Oo * ooo0Oo0 / iiI1iIiI . O0 + i1 + Oooo0000
 if 8 - 8: i1iII1I1i1i1 / o000o0o00o0Oo
 if url == 'search' :
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Search Term' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1 . lower ( )
    if 55 - 55: IiIi1Iii1I1 - O00OoOoo00 + i11Ii11I1Ii1i + oooOOOOO % iiiI11
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o0O , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o0O , 5000 )
   quit ( )
  ooO0OoOO = ooO0OoOO . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + ooO0OoOO + '.html'
  iiI11i1II ( url , I1IiI )
  if 51 - 51: i1IIi11111i % ooo0Oo0 % i1IIi11111i * O0 - i1iIIII % ooo0Oo0
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  iiI11i1II ( url , I1IiI )
  if 65 - 65: IiIi1Iii1I1
def iiI11i1II ( url , icon ) :
 if 68 - 68: IiIi1Iii1I1 % i11iIiiIii + i11Ii11I1Ii1i
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = re . compile ( '<i>(.+?)</i>' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 52 - 52: o000o0o00o0Oo - ooo0Oo0 + o000o0o00o0Oo % i1IIi11111i
def iI1IiI ( ) :
 if 21 - 21: i1 + iiI1iIiI % iiI1iIiI
 iiiiiIIii = 'http://www.genti.stream/'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  oO0o0oooO0oO = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ] . strip ( )
  IiIiII1 = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0Oo ) [ 1 ] . strip ( )
  iiiiiIIii = re . compile ( 'href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.genti.stream/' + iiiiiIIii
  O000oo0O ( "[COLOR aqua]" + oO0o0oooO0oO + "[COLOR yellow] vs [COLOR aqua]" + IiIiII1 + "[/COLOR]" , iiiiiIIii , 39 , I1IiI , I1ii11iIi11i )
  if 21 - 21: O0 % IiiIII111ii . iiI1iIiI / i11Ii11I1Ii1i + IiiIII111ii
def OOOO0O00o ( url ) :
 if 62 - 62: iIii1I11I1II1
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1II = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 if not 'http' in i1II :
  i1II = 'http://www.genti.stream' + i1II
 oO0o0Ooooo = i11i1 ( i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI1I = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( oO0o0Ooooo ) [ 0 ]
 I1iI1ii1II = i11i1 ( iI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
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
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , o0O , 5000 )
  quit ( )
 I11iI ( oo0OooOOo0 , url , o0O )
 if 14 - 14: i1IIi11111i * i1iIIII + oooOOOOO + O0 + i11iIiiIii
 if 77 - 77: i1IIi11111i / OoooooooOO
def IIii11I1i1I ( url ) :
 if 99 - 99: oooOOOOO
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 O000OO0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( O000OO0 ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II )
 for url , III1iII1I1ii in OoO0o :
  url = 'http://kimcartoon.me/CartoonList' + url
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 17 - 17: i1IIi
def iiIi1i ( url ) :
 if 27 - 27: i1iIIII * IiIi1Iii1I1 . i1iIIi1 % IiiIII111ii * IiiIII111ii . i1IIi
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 O000OO0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( O000OO0 )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   O0OOoOOO0oO = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( oO0Oo ) [ 0 ]
   O0OOoOOO0oO = o0Oo0oO0oOO00 ( O0OOoOOO0oO )
  except IndexError :
   O0OOoOOO0oO = ''
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , O0OOoOOO0oO )
  if 28 - 28: IiIi1Iii1I1 + i11iIiiIii / O00OoOoo00 % Oooo0000 % ooo0Oo0 - O0
 try :
  ooo0OOO = re . compile ( '<li>(.+?)Next' ) . findall ( O000OO0 )
  for oO0Oo in ooo0OOO :
   o0O0o = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ - 1 ]
   iii1Ii1Ii1 = 'http://kimcartoon.me' + o0O0o
   IIi = 'https://i.imgur.com/mjCRjXT.png'
   O00oO ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , iii1Ii1Ii1 , 30 , IIi , I1ii11iIi11i )
 except : pass
 if 94 - 94: i11Ii11I1Ii1i - ooo0Oo0
def oo0oO0 ( url ) :
 if 1 - 1: i1IIi . i11iIiiIii % i1iIIII
 oOO0O00o0OO0O = cfscrape . create_scraper ( )
 O000OO0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<td>(.+?)</td>' ) . findall ( O000OO0 )
 for oO0Oo in IIIii1II1II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   O000oo0O ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 82 - 82: iIii1I11I1II1 + ooo0Oo0 . iIii1I11I1II1 % IiiIII111ii / iiiI11 . iiiI11
def IIioOoO00oo0O ( url ) :
 if 39 - 39: iIii1I11I1II1 / O0 / i1iII1I1i1i1 - iiiI11 - oooOOOOO % i1iIIII
 o0 = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if o0 == 0 :
  url = url + '&s=rapidvideo'
  oOO0O00o0OO0O = cfscrape . create_scraper ( )
  O000OO0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   OoO0o = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( O000OO0 )
   for OOOO in OoO0o :
    url = re . compile ( 'src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
    if 'rapidvideo' in url :
     I11iI ( oo0OooOOo0 , url , o0O )
    else :
     Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
 if o0 == 1 :
  url = url + '&s=openload'
  oOO0O00o0OO0O = cfscrape . create_scraper ( )
  O000OO0 = oOO0O00o0OO0O . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   OoO0o = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( O000OO0 )
   for OOOO in OoO0o :
    url = re . compile ( 'src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
    I11iI ( oo0OooOOo0 , url , o0O )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 31 - 31: O00OoOoo00 - O0 / IiIi1Iii1I1 * Oooo0000
   if 12 - 12: i1IIi11111i - IiIi1Iii1I1 * i1iIIi1
def II1111ii ( ) :
 if 27 - 27: O0
 iiiiiIIii = "http://www.loyalbooks.com/genre-menu"
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  if "paid" not in i1I1iI :
   oO0o0Ooooo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
   I1iI1ii1II = "http://www.loyalbooks.com" + oO0o0Ooooo
   oo0OooOOo0 = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
   O00oO ( "[COLOR aqua]" + oo0OooOOo0 + "[/COLOR]" , I1iI1ii1II , 60 , I1IiI , Oo , '' )
   if 79 - 79: i1IIi11111i - O00OoOoo00 + i1IIi11111i . i1iII1I1i1i1
def ii1III11 ( url ) :
 if 7 - 7: oooOOOOO % O0 . Oooo0000 + iiI1iIiI - O00OoOoo00
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 o0o0O00oo0 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( IIIii1II1II )
 for i1I1iI in o0o0O00oo0 :
  OOOo00oo0oO = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  I1iI1ii1II = "http://www.loyalbooks.com" + OOOo00oo0oO
  I1IiI = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  o0O = "http://www.loyalbooks.com" + I1IiI
  oo0OooOOo0 = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  O00oO ( "[COLOR aqua]" + oo0OooOOo0 + "[/COLOR]" , I1iI1ii1II , 61 , o0O , Oo , '' )
 try :
  OOOO = i11i1 ( url )
  ooO0oOOooOo0 = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
  I1IiI = 'https://i.imgur.com/mjCRjXT.png'
  O00oO ( "[COLOR yellow]Next Page -->[/COLOR]" , ooO0oOOooOo0 , 60 , I1IiI , Oo , '' )
 except : pass
 if 27 - 27: i11iIiiIii % i11Ii11I1Ii1i % O00OoOoo00 . O0 - ooo0Oo0 + Oooo0000
 if 57 - 57: iIii1I11I1II1 / O00OoOoo00 - i1IIi
def ooOOo00O00Oo ( name , url , iconimage ) :
 if 42 - 42: O0 / i1IIi11111i + OoooooooOO * IiIi1Iii1I1 % IiIi1Iii1I1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  III1iII1I1ii = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  OOOo00oo0oO = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OOOo00oo0oO , 10 , iconimage , Oo , '' )
  if 7 - 7: oooOOOOO / o000o0o00o0Oo / i11iIiiIii
def IIIIIo0ooOoO000oO ( ) :
 if 85 - 85: i1IIi11111i . Oooo0000 / IiIi1Iii1I1 . O0 % i1iIIi1
 iiiiiIIii = 'http://www.shadownet.me/'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II )
 for iiiiiIIii , III1iII1I1ii in OoO0o :
  III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
  if 'P2P' not in III1iII1I1ii :
   O00oO ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 49 , I1IiI , Oo , '' )
   if 90 - 90: ooo0Oo0 % O0 * iIii1I11I1II1 . oooOOOOO
   if 8 - 8: IiIi1Iii1I1 + i11Ii11I1Ii1i / oooOOOOO / O00OoOoo00
def ooo0O ( url ) :
 if 16 - 16: Oooo0000
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( IIIii1II1II )
 for oO0Oo in OoO0o :
  III1iII1I1ii = re . compile ( 'alt="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  O000oo0O ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o0O0o = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  O00oO ( "[COLOR orange]Next Page --->[/COLOR]" , o0O0o , 49 , I1IiI , Oo , '' )
 except : pass
 if 41 - 41: i1IIi * i11Ii11I1Ii1i / OoooooooOO . i1iIIII
def O0iII1 ( url ) :
 if 27 - 27: i1 . O00OoOoo00 + Oooo0000 / iIii1I11I1II1 % oooOOOOO . IiIi1Iii1I1
 def IIIIi1 ( url ) :
  iIi11iiIiI1I = urllib2 . Request ( url )
  iIi11iiIiI1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iIi11iiIiI1I . add_header ( 'Referer' , url )
  IiiioooOOoooo = urllib2 . urlopen ( iIi11iiIiI1I , timeout = 5 )
  OOOO = IiiioooOOoooo . read ( )
  IiiioooOOoooo . close ( )
  return OOOO
  if 89 - 89: oooOOOOO - IiIi1Iii1I1 % ooo0Oo0 % i1IIi11111i
 OOOO = IIIIi1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  IIIii1II1II = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( OOOO ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in IIIii1II1II :
  url = IIIii1II1II
  I11iI ( oo0OooOOo0 , url , o0O )
 I1iI1ii1II = IIIIi1 ( IIIii1II1II )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 49 - 49: ooo0Oo0 - iiI1iIiI / IiiIII111ii / O0 % i1IIi11111i * iiiI11
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo , O0O0OOOOoo , False )
 else :
  if '.m3u8' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + oo0OooOOo0 + '&amp;url=' + url + '&amp;iconImage=' + o0O
  elif '.ts' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + oo0OooOOo0 + '&amp;url=' + url + '&amp;iconImage=' + o0O
  else :
   OOOo00oo0oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 100 - 100: i1iIIII . oooOOOOO / O0 * i1IIi * iiiI11 * ooo0Oo0
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( url )
  if 84 - 84: o000o0o00o0Oo / i1iIIII % i11iIiiIii * i1iIIi1 % o000o0o00o0Oo - OoooooooOO
  xbmc . Player ( ) . play ( OOOo00oo0oO , O0O0OOOOoo , False )
  if 99 - 99: iiI1iIiI + O0 + i1IIi / i11iIiiIii - i1IIi * iIii1I11I1II1
  if 72 - 72: iiI1iIiI * o000o0o00o0Oo . iiiI11 * IiiIII111ii * ooo0Oo0 * i1iIIi1
def iii11 ( ) :
 if 97 - 97: IiIi1Iii1I1 / i1iIIi1 % i1IIi % o000o0o00o0Oo
 iiiiiIIii = 'https://m.skylinewebcams.com/en/webcam'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoO0o = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 ii111I11iI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoO0o )
 for iiiiiIIii , III1iII1I1ii in ii111I11iI :
  if 'http|https' not in iiiiiIIii :
   iiiiiIIii = 'https://m.skylinewebcams.com' + iiiiiIIii
   O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 46 , I1IiI , Oo , '' )
   if 93 - 93: o000o0o00o0Oo / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * O00OoOoo00
def Ooooooo ( url ) :
 if 39 - 39: IiiIII111ii * ooo0Oo0 + iIii1I11I1II1 - IiiIII111ii + i1iIIII
 OOOO = i11i1 ( url )
 OoO0o = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( OOOO )
 for url , I1IiI , III1iII1I1ii in OoO0o :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 69 - 69: O0
  if 85 - 85: IiIi1Iii1I1 / O0
def iI1iIIIi1i ( name , url , iconimage ) :
 if 89 - 89: iIii1I11I1II1
 OOOO = i11i1 ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  IIIii1II1II = re . compile ( '<amp-video src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
  url = 'https:' + IIIii1II1II
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  if 21 - 21: O00OoOoo00 % O00OoOoo00
 except : pass
 quit ( 0 )
 if 27 - 27: i11iIiiIii / o000o0o00o0Oo
def oOoOOo ( ) :
 if 3 - 3: O0 / oooOOOOO
 iiiiiIIii = 'http://www.watchepisodeseries.com/home/schedule'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( IIIii1II1II )
 for iiiiiIIii , iIiIi1I , iiii11i in OoO0o :
  O00oO ( "[COLOR aqua]" + iIiIi1I + "  " + iiii11i + "[/COLOR]" , iiiiiIIii , 67 , I1IiI , I1ii11iIi11i )
  if 35 - 35: o000o0o00o0Oo * oooOOOOO - i1 % i1IIi11111i
  if 87 - 87: Oooo0000 * i1iIIi1 . O00OoOoo00
def O0Oo0o000oO ( url ) :
 if 99 - 99: i1iII1I1i1i1 * i11Ii11I1Ii1i * i1iIIi1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 1 ]
  III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  o0O = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 68 , o0O , I1ii11iIi11i )
  if 92 - 92: ooo0Oo0
  if 40 - 40: Oooo0000 / IiiIII111ii
def OOOoO000 ( url , iconimage , fanart ) :
 if 57 - 57: i11Ii11I1Ii1i
 OOOO = i11i1 ( url )
 oOOOoo = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in oOOOoo :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
 IIIii1II1II = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( OOOO )
 iiIiI = datetime . now ( )
 for oO0Oo in IIIii1II1II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
   Ii1ii111i1 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   i1i1i1I = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   iIiIi1I = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in iIiIi1I :
    iIiIi1I = iIiIi1I . strip ( )
    iIiIi1I = time . strptime ( iIiIi1I , "%d/%m/%Y" )
    oOoo000 = ( "%s/%s/%s" % ( iiIiI . day , iiIiI . month , iiIiI . year ) )
    oOoo000 = time . strptime ( oOoo000 , "%d/%m/%Y" )
    if ( oOoo000 < iIiIi1I ) :
     III1iII1I1ii = '[COLOR yellow]' + ( III1iII1I1ii ) + ' - Not Aired Yet' + '[/COLOR]'
     i1i1i1I = '[COLOR yellow]' + ( i1i1i1I ) + '[/COLOR]'
     Ii1ii111i1 = '[COLOR yellow]' + ( Ii1ii111i1 ) + '[/COLOR]'
     if 87 - 87: OoooooooOO - i1IIi11111i / IiiIII111ii . i11iIiiIii * OoooooooOO
    if not 'Season 0' in Ii1ii111i1 :
     O00oO ( "[COLOR aqua]" + Ii1ii111i1 + " " + i1i1i1I + " " + III1iII1I1ii + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 84 - 84: Oooo0000 / O00OoOoo00 * oooOOOOO / i1iII1I1i1i1 - i11iIiiIii . ooo0Oo0
  if 60 - 60: o000o0o00o0Oo * iiI1iIiI
def I1iIiI11I1 ( url , iconimage , fanart ) :
 if 27 - 27: iiiI11 . i11iIiiIii % i1iIIi1
 if 65 - 65: i11Ii11I1Ii1i . iiI1iIiI % i1iII1I1i1i1 * i1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="domain">(.+?)<div class="watch"' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  try :
   III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = III1iII1I1ii . title ( )
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
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
              O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 70 , iconimage , fanart )
  except : pass
  if 38 - 38: Oooo0000 / oooOOOOO % ooo0Oo0
  if 11 - 11: oooOOOOO - i1iII1I1i1i1 + i11Ii11I1Ii1i - iIii1I11I1II1
def I1i11ii11 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( 'href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    ooo0OO0O0Oo = liveresolver . resolve ( url )
   else : ooo0OO0O0Oo = url
   O0O0OOOOoo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
   xbmc . Player ( ) . play ( ooo0OO0O0Oo )
   if 81 - 81: i1iIIII - O00OoOoo00 % IiIi1Iii1I1 - i1 / ooo0Oo0
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 4 - 4: OoooooooOO - i1IIi % iiiI11 - i1iIIII * i1IIi11111i
def Ooooo00o0OoO ( ) :
 if 75 - 75: iiI1iIiI % i11Ii11I1Ii1i
 i1iI1 = ''
 i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Search Term' )
 i11ii1ii11i . doModal ( )
 if i11ii1ii11i . isConfirmed ( ) :
  i1iI1 = i11ii1ii11i . getText ( )
  if len ( i1iI1 ) > 1 :
   ooO0OoOO = i1iI1 . lower ( )
   ooO0OoOO = ooO0OoOO . replace ( ' ' , '%20' )
   if 30 - 30: IiiIII111ii + i1iIIi1 - IiiIII111ii . IiiIII111ii - i11Ii11I1Ii1i + O0
  else : quit ( )
 else : ooO0OoOO = urllib . unquote_plus ( iiiiiIIii ) . lower ( ) ; i1iI1 = urllib . unquote_plus ( iiiiiIIii )
 iiiiiIIii = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + ooO0OoOO
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '"series"(.+?)"series_id"' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'original_name":"(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '"seo_name":"(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.watchepisodeseries.com/' + OOOo00oo0oO
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + OOOo00oo0oO + '.jpg'
  O00oO ( III1iII1I1ii , iiiiiIIii , 68 , I1IiI , I1ii11iIi11i , '' )
  if 86 - 86: i1IIi
def IIi11IIiIii1 ( ) :
 if 17 - 17: iiiI11 + i1iII1I1i1i1 . i1 - ooo0Oo0 * i11iIiiIii
 iiiiiIIii = 'http://www.watchepisodeseries.com/home/popular-series'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<div title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0Oo0oO0oOO00 ( III1iII1I1ii )
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  O00oO ( '[COLOR aqua]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 68 , I1IiI , I1ii11iIi11i )
  if 20 - 20: iiI1iIiI . OoooooooOO % i1iIIII
  if 63 - 63: iiI1iIiI % iIii1I11I1II1
def I1ii ( ) :
 if 73 - 73: IiiIII111ii + iiI1iIiI * ooo0Oo0 * OoooooooOO
 try :
  Oo0o0O = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1
   else : quit ( )
  if ooO0OoOO == Oo0o0O :
   ii1iIi1II ( )
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
   if 2 - 2: ooo0Oo0 + Oooo0000 - i1iIIII . iiI1iIiI - i1iIIII
   if 67 - 67: iIii1I11I1II1 - oooOOOOO
   if 11 - 11: iIii1I11I1II1 . OoooooooOO . i11Ii11I1Ii1i / i1IIi - O00OoOoo00
def ii1iIi1II ( ) :
 if 30 - 30: Oooo0000
 Ii111 = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 oO0 = '[COLOR aqua]Asian Special Porn[/COLOR]'
 O00oO ( oO0 , Ii111 , 1 , I1IiI , Oo , '' )
 iiiiiIIii = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<li class="">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oO0Oo ) [ 0 ]
  i1iI = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'https://www.eporner.com' + OOOo00oo0oO
  if not 'All' in III1iII1I1ii :
   if not 'Homemade' in III1iII1I1ii :
    O00oO ( "[COLOR aqua]" + III1iII1I1ii + "  " + "[COLOR yellow]" + i1iI + "[/COLOR]" , iiiiiIIii , 36 , I1IiI , Oo , '' )
    if 10 - 10: i11Ii11I1Ii1i . oooOOOOO
def I1i ( url ) :
 if 86 - 86: ooo0Oo0 / i1iII1I1i1i1 + O0 * oooOOOOO
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'https://www.eporner.com' + OOOo00oo0oO
  O00oO ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 19 - 19: i11Ii11I1Ii1i * IiiIII111ii + iiiI11
 try :
  o0O0o = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( OOOO ) [ 0 ]
  ooO0oOOooOo0 = 'https://www.eporner.com' + o0O0o
  OO0o0o00 = 'http://imgur.com/3eNoY0p'
  O00oO ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , ooO0oOOooOo0 , 36 , OO0o0o00 , Oo , '' )
 except : pass
 if 65 - 65: i1iIIII . i1iIIi1 . i1 . oooOOOOO - i1iIIII
def ii111i ( url , iconimage ) :
 if 93 - 93: i1
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i111I = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( i111I )
 for OOO0oOoO0O , OOOO in OoO0o :
  OOO0oOoO0O = OOO0oOoO0O . replace ( ':' , '' )
  url = 'https://www.eporner.com' + OOOO
  O000oo0O ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + OOO0oOoO0O + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 84 - 84: O0 * OoooooooOO - IiiIII111ii * IiiIII111ii
def i1ii ( url ) :
 if 65 - 65: Oooo0000 / i1 % IiiIII111ii
 O000oo0O ( "[COLOR yellow]Anime Catergories[/COLOR]" , url , 999 , I1IiI , Oo , '' )
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<ul class="nav nav-pills nav-stacked"><li>(.+?)</ul>' ) . findall ( OOOO ) [ 1 ]
 OoO0o = re . compile ( '<a href="(.+?)" title="(.+?)">.+?</a>' ) . findall ( IIIii1II1II )
 for url , III1iII1I1ii in OoO0o :
  III1iII1I1ii = III1iII1I1ii . strip ( )
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 52 , I1IiI , Oo , '' )
  if 45 - 45: Oooo0000
def oOooOO ( url ) :
 if 31 - 31: i1iIIII / ooo0Oo0 * i1IIi . Oooo0000
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<th class="st-sort-descent">(.+?)</table>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)".+?>(.+?)</a>' ) . findall ( IIIii1II1II )
 for url , III1iII1I1ii in OoO0o :
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 53 , I1IiI , Oo , '' )
  if 57 - 57: i1iIIII + iIii1I11I1II1 % i1IIi % iiI1iIiI
def OO0oo ( url ) :
 if 15 - 15: iIii1I11I1II1 % OoooooooOO - ooo0Oo0 * iiiI11 + O00OoOoo00
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1IiI = re . compile ( '''<div class=\"col-md-3\">.+?url\('(.+?)'\)''' ) . findall ( OOOO ) [ 0 ]
 except :
  I1IiI = o0O
 IIIii1II1II = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '''<a class="black" href='(.+?)'>(.+?)</a>''' ) . findall ( IIIii1II1II )
 O000oo0O ( "[COLOR yellow]Links Can Take Up To 45 Secs To Play, Be Patient![/COLOR]" , url , 54 , I1IiI , Oo , '' )
 for url , III1iII1I1ii in OoO0o :
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 54 , I1IiI , Oo , '' )
  if 11 - 11: oooOOOOO * iiiI11 - Oooo0000
def OOOIII1iI1iII1I ( url , iconimage ) :
 if 39 - 39: iiiI11 * IiIi1Iii1I1 / Oooo0000 * i1 . O00OoOoo00 % i11Ii11I1Ii1i
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 oOoO = re . compile ( '<source src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 I11iI ( oo0OooOOo0 , oOoO , iconimage )
 if 71 - 71: i1iIIi1 % i1IIi - i11Ii11I1Ii1i - i1iIIII + i1iIIII * IiIi1Iii1I1
 if 51 - 51: iIii1I11I1II1 / Oooo0000 + i1iIIII - O00OoOoo00 + oooOOOOO
 if 29 - 29: i1IIi11111i % iIii1I11I1II1 . OoooooooOO % OoooooooOO % i11Ii11I1Ii1i / oooOOOOO
 if 70 - 70: i11iIiiIii % oooOOOOO
 if 11 - 11: IiiIII111ii % o000o0o00o0Oo % iiiI11 / i11Ii11I1Ii1i % i1iIIi1 - ooo0Oo0
 if 96 - 96: o000o0o00o0Oo / i11Ii11I1Ii1i . iiiI11 - oooOOOOO * O00OoOoo00 * i1iII1I1i1i1
 if 76 - 76: iiiI11 - i11Ii11I1Ii1i * i1iIIII / OoooooooOO
 if 18 - 18: i1 + iIii1I11I1II1 - i11Ii11I1Ii1i - iiI1iIiI
def oooOOOO0oooo ( url ) :
 if 51 - 51: O0 - i1IIi / iiI1iIiI
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( './' , '/' )
  if 37 - 37: i1IIi11111i % IiIi1Iii1I1
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOO0oOoO0O = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[COLOR yellow] " + OOO0oOoO0O + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 83 - 83: i1iIIII . i1iIIi1 + i1iII1I1i1i1 - i1iIIII * i1iIIi1 / i1iIIi1
 try :
  ooO0oOOooOo0 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( OOOO ) [ 0 ]
  o0O0o = re . compile ( '<a.+?href="(.+?)"' ) . findall ( ooO0oOOooOo0 ) [ 5 ]
  I11I1 = 'http://m4ufree.com' + o0O0o
  if 'genre' in I11I1 :
   I11I1 = I11I1 . replace ( '.com' , '.com/' )
  iiI1i1Iii111 = 'https://i.imgur.com/mjCRjXT.png'
  O00oO ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I11I1 , 42 , iiI1i1Iii111 , Oo , '' )
 except : pass
 if 43 - 43: i1IIi11111i
def OO00oOooo0O ( url , iconimage ) :
 if 58 - 58: ooo0Oo0 / i1iII1I1i1i1
 import requests
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iIII1I1i1i = re . compile ( 'data="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 o0OIIiI1I1 = 'http://m4ufree.com/ajax_new.php'
 I11I1IIiiII1 = requests . post ( o0OIIiI1I1 , data = { 'm4u' : iIII1I1i1i } )
 json = ( I11I1IIiiII1 . text )
 IIIIIii1ii11 = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 OOOooo0OooOoO = re . compile ( '{(.+?)}' ) . findall ( IIIIIii1ii11 )
 oOoOOOo = 0
 for iiIiI in OOOooo0OooOoO :
  try :
   oOoOOOo += 1
   III1iII1I1ii = 'Link ' + str ( oOoOOOo )
   OOO0oOoO0O = re . compile ( '''"label":"(.+?)"''' ) . findall ( iiIiI ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( iiIiI ) [ 0 ]
   O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + " | [COLOR yellow] " + OOO0oOoO0O + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( iiIiI ) [ 0 ]
   OOO0oOoO0O = re . compile ( """label:.+?'(.+?)'""" ) . findall ( iiIiI ) [ 0 ]
   O000oo0O ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + OOO0oOoO0O + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 43 - 43: i1IIi
def I1i11II ( ) :
 if 31 - 31: i1iII1I1i1i1 / IiiIII111ii * i1IIi11111i . i11Ii11I1Ii1i
 iiiiiIIii = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<td>(.+?)</td>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOo0oO00ooO00 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.livefootballol.me' + iiiiiIIii
  O00oO ( "[COLOR aqua]" + OOo0oO00ooO00 + "[/COLOR]" , iiiiiIIii , 74 , o0O , Oo , '' )
  if 89 - 89: O0
def II ( url ) :
 if 41 - 41: o000o0o00o0Oo * IiIi1Iii1I1 - iiiI11 + ooo0Oo0
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<a href="(.+?)"' ) . findall ( OOOO )
 IiIIIII11I = 0
 for OOOOoOoo0O0O0 in IIIii1II1II :
  if 'acestream' in OOOOoOoo0O0O0 :
   if 'http' in OOOOoOoo0O0O0 :
    IiIIIII11I += 1
    III1iII1I1ii = '[COLOR aqua]Link :: ' + str ( IiIIIII11I ) + '[/COLOR]'
    O000oo0O ( III1iII1I1ii , OOOOoOoo0O0O0 , 75 , o0O , Oo , '' )
 if IiIIIII11I == 0 :
  O000oo0O ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , o0O , Oo , '' )
  if 17 - 17: OoooooooOO + i1iIIII * O00OoOoo00 * Oooo0000
def iiIii1I ( url ) :
 if 47 - 47: IiIi1Iii1I1 . O00OoOoo00 / i1IIi11111i
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 I11iI ( oo0OooOOo0 , url , o0O )
 if 83 - 83: i1IIi11111i / i1iIIII / i1iIIII + i1IIi11111i * i1iIIi1 + i1IIi11111i
def IIIIiii ( url , getphp ) :
 iIi11iiIiI1I = urllib2 . Request ( url )
 iIi11iiIiI1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 iIi11iiIiI1I . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 IiiioooOOoooo = urllib2 . urlopen ( iIi11iiIiI1I , timeout = 10 )
 OOOO = IiiioooOOoooo . read ( )
 IiiioooOOoooo . close ( )
 return OOOO
 if 65 - 65: ooo0Oo0 / O00OoOoo00
 if 12 - 12: O00OoOoo00 % Oooo0000
 if 48 - 48: oooOOOOO . i11iIiiIii
def IIioo0OO ( ) :
 if 2 - 2: i11Ii11I1Ii1i - i1 . IiiIII111ii * oooOOOOO / i1iII1I1i1i1
 iiiiiIIii = 'http://m4ufree.com/?sort=key_top&page=1&='
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( './' , '' )
  iiiiiIIii = 'http://m4ufree.com/' + OOOo00oo0oO
  if not re . search ( '\d+' , III1iII1I1ii ) :
   O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 42 , I1IiI , Oo )
   if 80 - 80: i1iIIII / O00OoOoo00 / Oooo0000 + i1IIi - ooo0Oo0
   if 11 - 11: i1IIi11111i * i1
   if 15 - 15: Oooo0000
   if 62 - 62: iiiI11
   if 51 - 51: Oooo0000
   if 14 - 14: IiiIII111ii % i1iII1I1i1i1 % ooo0Oo0 - i11iIiiIii
   if 53 - 53: iiiI11 % ooo0Oo0
   if 59 - 59: i1iIIII % iIii1I11I1II1 . i1IIi + i11Ii11I1Ii1i * IiiIII111ii
   if 41 - 41: iiiI11 % o000o0o00o0Oo
   if 12 - 12: i1iIIII
def o0Oo0oO0oOO00 ( text ) :
 if 69 - 69: OoooooooOO + i1iIIII
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
 if 26 - 26: ooo0Oo0 + i1iIIII / i1 % Oooo0000 % o000o0o00o0Oo + i11Ii11I1Ii1i
 return text
 if 31 - 31: O00OoOoo00 % i1iIIII * O00OoOoo00
def IiI ( ) :
 if 34 - 34: O00OoOoo00 % IiIi1Iii1I1 . O0 . iIii1I11I1II1
 ooi1II1I = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 OOoO0ooOO = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 iii1IIII1iii11I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 oo0OoOooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 95 - 95: IiiIII111ii * o000o0o00o0Oo % IiIi1Iii1I1 % iiiI11 - iiiI11
 oOoooO0 = 0
 for ( o0Oo0 , i1i1II1i11 , o00o ) in os . walk ( OOoO0ooOO ) :
  for file in o00o :
   iii11II1I = os . path . join ( o0Oo0 , file )
   oOoooO0 += os . path . getsize ( iii11II1I )
 O0OOO0OOoO0O = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoooO0 / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 5 - 5: Oooo0000 - IiiIII111ii * IiiIII111ii
 oOoooO0 = 0
 for ( o0Oo0 , i1i1II1i11 , o00o ) in os . walk ( ooi1II1I ) :
  for file in o00o :
   iii11II1I = os . path . join ( o0Oo0 , file )
   oOoooO0 += os . path . getsize ( iii11II1I )
 O0OOO0OOoO0O = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoooO0 / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 50 - 50: i11Ii11I1Ii1i * o000o0o00o0Oo / iiiI11 . i1IIi11111i + ooo0Oo0 - i1iIIII
 oOoooO0 = 0
 for ( o0Oo0 , i1i1II1i11 , o00o ) in os . walk ( iii1IIII1iii11I ) :
  for file in o00o :
   iii11II1I = os . path . join ( o0Oo0 , file )
   oOoooO0 += os . path . getsize ( iii11II1I )
 O0OOO0OOoO0O = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoooO0 / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 18 - 18: Oooo0000 % i11iIiiIii % o000o0o00o0Oo / i1iII1I1i1i1 / i1IIi11111i / i1IIi
 oOoooO0 = 0
 for ( o0Oo0 , i1i1II1i11 , o00o ) in os . walk ( oo0OoOooo ) :
  for file in o00o :
   iii11II1I = os . path . join ( o0Oo0 , file )
   oOoooO0 += os . path . getsize ( iii11II1I )
 O0OOO0OOoO0O = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( oOoooO0 / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 48 - 48: Oooo0000 + O00OoOoo00 / IiiIII111ii + i11Ii11I1Ii1i
 O000oo0O ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 O000oo0O ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 18 - 18: o000o0o00o0Oo
def I11iI ( name , url , iconimage ) :
 if 23 - 23: i11Ii11I1Ii1i
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 import urlresolver
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
 if 'acestream' in url :
  OOOo00oo0oO = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  O0O0OOOOoo . setPath ( url )
  xbmc . Player ( ) . play ( OOOo00oo0oO , O0O0OOOOoo , False )
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
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
  if 24 - 24: iIii1I11I1II1 + iIii1I11I1II1 * oooOOOOO
def i1I11iIII1i1I ( name , url , iconimage ) :
 if 63 - 63: ooo0Oo0 + i1iIIi1 - i11Ii11I1Ii1i
 IIII , i1iIIi1I1I11 = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 IIII += urllib . unquote_plus ( i1iIIi1I1I11 )
 url = regex . resolve ( IIII )
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 PLAYREGEX ( name , url , iconimage )
 if 81 - 81: o000o0o00o0Oo - O0 * OoooooooOO
def iI1111iiii ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 23 - 23: i11Ii11I1Ii1i / i1iII1I1i1i1
def iII1Iii1I11i ( heading , text ) :
 if 17 - 17: O0
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 OOooO0o = xbmcgui . Window ( id )
 ii1iI1iI1 = 50
 while ( ii1iI1iI1 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   ii1iI1iI1 -= 1
   OOooO0o . getControl ( 1 ) . setLabel ( heading )
   OOooO0o . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 55 - 55: IiIi1Iii1I1 + i1iIIII
  if 18 - 18: i1iII1I1i1i1 - i1IIi11111i - iiI1iIiI - iiI1iIiI
def i11i1 ( url ) :
 try :
  iIi11iiIiI1I = urllib2 . Request ( url )
  iIi11iiIiI1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  IiiioooOOoooo = urllib2 . urlopen ( iIi11iiIiI1I , timeout = 5 )
  OOOO = IiiioooOOoooo . read ( )
  IiiioooOOoooo . close ( )
  OOOO = OOOO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OOOO
 except : quit ( )
 if 54 - 54: ooo0Oo0 + iiI1iIiI / oooOOOOO . iiI1iIiI * Oooo0000
def i1i ( url ) :
 try :
  iIi11iiIiI1I = urllib2 . Request ( url )
  iIi11iiIiI1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  IiiioooOOoooo = urllib2 . urlopen ( iIi11iiIiI1I , timeout = 5 )
  OOOO = IiiioooOOoooo . read ( )
  IiiioooOOoooo . close ( )
  OOOO = OOOO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OOOO
 except : quit ( )
 if 1 - 1: Oooo0000 * i1 . i1IIi / ooo0Oo0 . o000o0o00o0Oo + ooo0Oo0
def O000oo0O ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IIiIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 Oo00O0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 28 - 28: i11iIiiIii / i1IIi11111i . iIii1I11I1II1 / i11Ii11I1Ii1i
 Oo00O0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIi1 , listitem = O0O0OOOOoo , isFolder = False )
 return Oo00O0ooOO
 if 72 - 72: OoooooooOO / iiI1iIiI + iiiI11 / Oooo0000 * iiiI11
def iiII1i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IIiIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 Oo00O0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 34 - 34: O0 * O0 % OoooooooOO + oooOOOOO * iIii1I11I1II1 % iiiI11
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 25 - 25: O00OoOoo00 + Oooo0000 . i1IIi11111i % Oooo0000 * i1iIIII
 Oo00O0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIi1 , listitem = O0O0OOOOoo , isFolder = False )
 return Oo00O0ooOO
 if 32 - 32: i11iIiiIii - i1iIIi1
def oo00ooOoo ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 iii1IIIiiiI = [ ]
 OoO00oo00 = [ ]
 Oo0Oo0O = [ ]
 OOOO = i11i1 ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 oO0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( OOOOoOoo0O0O0 )
 if len ( oO0Oo ) < 1 :
  oO0Oo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OOOOoOoo0O0O0 )
 iiIiI = 1
 for iiiI1i11Ii in oO0Oo :
  iIiII = iiiI1i11Ii
  if '(' in iiiI1i11Ii :
   iiiI1i11Ii = iiiI1i11Ii . split ( '(' ) [ 0 ]
   i1i1IIIIIIIi = str ( iIiII . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iii1IIIiiiI . append ( iiiI1i11Ii )
   OoO00oo00 . append ( i1i1IIIIIIIi )
  else :
   iii1IIIiiiI . append ( iiiI1i11Ii )
   OoO00oo00 . append ( '[COLOR aqua]Link ' + str ( iiIiI ) + '[/COLOR]' )
  iiIiI = iiIiI + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oo0o0oOo = Iii1ii1II11i . select ( name , OoO00oo00 )
 if oo0o0oOo < 0 :
  quit ( )
 else :
  url = iii1IIIiiiI [ oo0o0oOo ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : ooo0OO0O0Oo = liveresolver . resolve ( url )
  else : ooo0OO0O0Oo = url
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  O0O0OOOOoo . setPath ( ooo0OO0O0Oo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( ooo0OO0O0Oo )
  if 58 - 58: i1IIi11111i - i11Ii11I1Ii1i % i1iII1I1i1i1 + i1iIIi1 . Oooo0000 / IiiIII111ii
def IIo00ooo ( name , url , iconimage ) :
 if 31 - 31: O0 * i1IIi11111i % i1IIi11111i / i1iII1I1i1i1 / O00OoOoo00 / i1
 III1ii = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iii1IIIiiiI = [ ]
 OoO00oo00 = [ ]
 Oo0Oo0O = [ ]
 i1IiiI1I1IIi11i1 = [ ]
 OOOO = i11i1 ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 oO0Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OOOOoOoo0O0O0 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 iiIiI = 1
 if 45 - 45: IiIi1Iii1I1 % i1IIi11111i - IiIi1Iii1I1
 for iiiI1i11Ii in oO0Oo :
  iIiII = iiiI1i11Ii
  if '(' in iiiI1i11Ii :
   iiiI1i11Ii = iiiI1i11Ii . split ( '(' ) [ 0 ]
   i1i1IIIIIIIi = str ( iIiII . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iii1IIIiiiI . append ( iiiI1i11Ii )
   OoO00oo00 . append ( i1i1IIIIIIIi )
   i1IiiI1I1IIi11i1 . append ( 'Stream ' + str ( iiIiI ) )
  else :
   iii1IIIiiiI . append ( iiiI1i11Ii )
   OoO00oo00 . append ( 'Link ' + str ( iiIiI ) )
   if 31 - 31: IiiIII111ii / i11iIiiIii
  iiIiI = iiIiI + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 oo0o0oOo = Iii1ii1II11i . select ( name , OoO00oo00 )
 if oo0o0oOo < 0 :
  quit ( )
 else :
  OOO00O = OoO00oo00 [ oo0o0oOo ]
  OOoOO0oo0ooO = "/"
  if not OOO00O . endswith ( OOoOO0oo0ooO ) :
   O0o0O00Oo0o0 = OOO00O + "/"
  else :
   O0o0O00Oo0o0 = OOO00O
  url = III1ii + iii1IIIiiiI [ oo0o0oOo ] + "%26referer=" + O0o0O00Oo0o0
  print url
  if 83 - 83: o000o0o00o0Oo / i1iIIi1 - i11iIiiIii . iIii1I11I1II1 + ooo0Oo0
  xbmc . Player ( ) . play ( url )
  if 59 - 59: O0 % ooo0Oo0
def ooOOO0 ( string ) :
 O0o00O0Oo0 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 58 - 58: O0
 return '' . join ( O0o00O0Oo0 )
 if 78 - 78: i1 % IiiIII111ii * i1IIi
def O00oO ( name , url , mode , iconimage , fanart , description = '' ) :
 if 66 - 66: iiiI11 . iiI1iIiI + i1IIi11111i . iIii1I11I1II1
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 IIiIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Oo00O0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 Oo00O0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIi1 , listitem = O0O0OOOOoo , isFolder = True )
 return Oo00O0ooOO
 if 51 - 51: O00OoOoo00 . ooo0Oo0
def IiiIiiIi ( name , url , iconimage ) :
 Oo00O0ooOO = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; O0O0OOOOoo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Oo00O0ooOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = O0O0OOOOoo )
 xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
 if 40 - 40: i1IIi11111i
def oOO ( ) :
 if 66 - 66: O00OoOoo00 - i1IIi
 ooi1II1I = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 OOoO0ooOO = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 iii1IIII1iii11I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 8 - 8: i1iIIi1 / i1iIIII . iiI1iIiI + o000o0o00o0Oo / i11iIiiIii
 iiIiI = [ ( ooi1II1I , 'Cache' ) , ( OOoO0ooOO , 'Thumbnails' ) , ( iii1IIII1iii11I , 'Packages' ) ]
 if 31 - 31: IiIi1Iii1I1 - iIii1I11I1II1 + oooOOOOO . ooo0Oo0 / IiiIII111ii % iIii1I11I1II1
 I11i1iIiiIiIi = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if I11i1iIiiIiIi :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for IIII in iiIiI :
   if 49 - 49: i1iIIII . o000o0o00o0Oo . i11iIiiIii - i11Ii11I1Ii1i / iiiI11
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % IIII [ 1 ] )
   time . sleep ( 1 )
   if 62 - 62: i1iIIII
   for i1I1i , i1i1II1i11 , o00o in os . walk ( IIII [ 0 ] ) :
    for I11II1i in o00o :
     if ( I11II1i . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( i1I1i , I11II1i ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % IIII [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 87 - 87: ooo0Oo0 / O0 * IiiIII111ii / i1IIi11111i
def I1iiIII ( url , mode , name , iconimage , fanart ) :
 if 16 - 16: i1iII1I1i1i1 + IiIi1Iii1I1 / i1IIi11111i
 with open ( I11i , "a" ) as iiiII :
  iiiII . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 82 - 82: IiiIII111ii * i11iIiiIii % i11Ii11I1Ii1i - OoooooooOO
def OO0 ( ) :
 if 62 - 62: i1IIi / IiIi1Iii1I1 . iiI1iIiI * i1IIi11111i
 with open ( I11i , "a" ) as iiiII :
  i11i1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  o0oO0oo0000OO = open ( i11i1Ii1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oO0oo0000OO )
  O000oo0O ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  O000oo0O ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  if len ( IIIii1II1II ) < 1 :
   O000oo0O ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  for I1i1ii1IiIii in IIIii1II1II :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   iiiiiIIii = re . compile ( '<url>(.+?)</url>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   O000oo0O ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 2 , I1IiI , I1ii11iIi11i )
   if 69 - 69: Oooo0000 % i1iII1I1i1i1 - O00OoOoo00
 O000oo0O ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , o0O , Oo )
 if 38 - 38: iIii1I11I1II1 + i11iIiiIii / i11iIiiIii % i1 / IiIi1Iii1I1 % iiiI11
def I1IiIiIi1IiI1 ( ) :
 if 60 - 60: iiiI11 * Oooo0000 - i11iIiiIii % IiIi1Iii1I1
 with open ( IiII , "a" ) as iiiII :
  i11i1Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  o0oO0oo0000OO = open ( i11i1Ii1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oO0oo0000OO )
  O000oo0O ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  O000oo0O ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  if len ( IIIii1II1II ) < 1 :
   O000oo0O ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  for I1i1ii1IiIii in IIIii1II1II :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   iiiiiIIii = re . compile ( '<link>(.+?)</link>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( I1i1ii1IiIii ) [ 0 ]
   O000oo0O ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 2 , I1IiI , I1ii11iIi11i )
   if 52 - 52: o000o0o00o0Oo % i1iII1I1i1i1 - i11iIiiIii
 O000oo0O ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , o0O , Oo )
 if 30 - 30: oooOOOOO / i1 + i1iII1I1i1i1
def I1Io00oOOoO0oO ( ) :
 if 26 - 26: iiiI11 * iIii1I11I1II1 % i1 . i1IIi11111i + ooo0Oo0
 with open ( I11i , "w" ) as iiiII :
  iiiII . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 80 - 80: ooo0Oo0 * iiiI11 + o000o0o00o0Oo * i1iIIII
def I1Ii ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as iiiII :
  iiiII . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 77 - 77: iIii1I11I1II1 - i1IIi . i1iII1I1i1i1
 if 26 - 26: i1IIi11111i * IiiIII111ii . i1IIi
 if 59 - 59: O0 + i1IIi - i1IIi11111i
def OOO00 ( ) :
 if 62 - 62: i11iIiiIii % i1iIIII . IiiIII111ii . i1iIIII
 if 84 - 84: i11iIiiIii * i1
 I1I1iII1i = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  iiIIii = re . compile ( '<pin>(.+?)</pin>' ) . findall ( I1I1iII1i ) [ 0 ]
  if iiIIii == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok[/COLOR]" )
   i1iI1 = ''
   i11ii1ii11i = xbmc . Keyboard ( i1iI1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   i11ii1ii11i . doModal ( )
   if i11ii1ii11i . isConfirmed ( ) :
    i1iI1 = i11ii1ii11i . getText ( )
    if len ( i1iI1 ) > 1 :
     ooO0OoOO = i1iI1 . title ( )
     with open ( iI1Ii11111iIi , "w" ) as I11II1i :
      I11II1i . write ( "<pin>" + ooO0OoOO + "</pin>" )
     OOO00 ( )
    else : quit ( )
   else : quit ( )
  if not 'EXPIRED' in iiIIii :
   oO0Oo0O0 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( I1I1iII1i ) [ 0 ]
   I1iIiI1IiIIII = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % oO0Oo0O0 )
   OOOO = i11i1 ( I1iIiI1IiIIII )
   if 'Pin Verified' in OOOO :
    pass
   else :
    with open ( iI1Ii11111iIi , "w" ) as I11II1i :
     I11II1i . write ( '<pin>EXPIRED</pin>' )
     OOO00 ( )
 except IndexError :
  with open ( iI1Ii11111iIi , "w" ) as I11II1i :
   I11II1i . write ( "<pin>EXPIRED</pin>\n" )
  OOO00 ( )
  if 18 - 18: IiIi1Iii1I1 % i11iIiiIii . iIii1I11I1II1 - oooOOOOO
  if 80 - 80: iiI1iIiI + i1iII1I1i1i1 - i1IIi . iiiI11 / i1IIi11111i / iiI1iIiI
  if 1 - 1: O00OoOoo00 + i11iIiiIii - iiI1iIiI / i1iIIII + i1iIIi1
  if 80 - 80: i1iII1I1i1i1 + i1IIi11111i * iiiI11 + i1
def O0oOo ( url , iconimage , fanart ) :
 if 69 - 69: ooo0Oo0 * i11Ii11I1Ii1i * IiIi1Iii1I1 . oooOOOOO - o000o0o00o0Oo
 try :
  i1iI1 = ''
  i11ii1ii11i = xbmc . Keyboard ( i1iI1 , 'Enter Name To Save File As' )
  i11ii1ii11i . doModal ( )
  if i11ii1ii11i . isConfirmed ( ) :
   i1iI1 = i11ii1ii11i . getText ( )
   if len ( i1iI1 ) > 1 :
    ooO0OoOO = i1iI1 . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   ooo0OO0O0Oo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = ooo0OO0O0Oo
  I11iiIIiI1ii = url . split ( '/' ) [ - 1 ]
  IIiIi1 = urllib2 . urlopen ( url )
  I1IiIIi11I1 = os . path . join ( o0OOO , ooO0OoOO )
  I11II1i = open ( I1IiIIi11I1 , 'wb' )
  if 15 - 15: i1iIIi1 % iIii1I11I1II1 % Oooo0000 % i1IIi11111i % i1iIIi1 . i1iIIII
  ooOOoOo = IIiIi1 . info ( )
  oooO = int ( ooOOoOo . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( ooO0OoOO , oooO ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 12 - 12: i11Ii11I1Ii1i
  IiIii1ii = 0
  IIiI1i = 8192
  while True :
   buffer = IIiIi1 . read ( IIiI1i )
   if not buffer :
    break
    if 6 - 6: o000o0o00o0Oo / oooOOOOO - i1iIIII
   IiIii1ii += len ( buffer )
   I11II1i . write ( buffer )
   o00O00Oo00O = "[%3.2f%%]" % ( IiIii1ii * 100. / oooO )
   o00O00Oo00O = o00O00Oo00O + chr ( 8 ) * ( len ( o00O00Oo00O ) + 1 )
   iIiiiI . update ( IiIii1ii , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( o00O00Oo00O , ooO0OoOO ) )
   if 46 - 46: Oooo0000 % i1IIi / i1iII1I1i1i1 * ooo0Oo0 * i1iIIII
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as iiiII :
   iiiII . write ( '<item>\n<title>' + ooO0OoOO + '</title>\n<link>' + I1IiIIi11I1 + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 67 - 67: Oooo0000 * Oooo0000 . Oooo0000 + iiiI11 / i1iII1I1i1i1
  I11II1i . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 13 - 13: oooOOOOO
  if 80 - 80: iiiI11 - i1IIi11111i
  if 41 - 41: i1IIi11111i - ooo0Oo0 * iiI1iIiI
  if 82 - 82: i1 % i1IIi11111i % i1iIIII / O0
def OOOO0o0 ( ) :
 i1IIIi111Ii = [ ]
 iIIi1iI1 = sys . argv [ 2 ]
 if len ( iIIi1iI1 ) >= 2 :
  I1Iii1I = sys . argv [ 2 ]
  iIi11I = I1Iii1I . replace ( '?' , '' )
  if ( I1Iii1I [ len ( I1Iii1I ) - 1 ] == '/' ) :
   I1Iii1I = I1Iii1I [ 0 : len ( I1Iii1I ) - 2 ]
  O0Oo = iIi11I . split ( '&' )
  i1IIIi111Ii = { }
  for iiIiI in range ( len ( O0Oo ) ) :
   iIIiI11i = { }
   iIIiI11i = O0Oo [ iiIiI ] . split ( '=' )
   if ( len ( iIIiI11i ) ) == 2 :
    i1IIIi111Ii [ iIIiI11i [ 0 ] ] = iIIiI11i [ 1 ]
 return i1IIIi111Ii
 if 100 - 100: O0 . O00OoOoo00 . i1 + O0 * i1iII1I1i1i1
I1Iii1I = OOOO0o0 ( ) ; iiiiiIIii = None ; oo0OooOOo0 = None ; iIIiIIIIiII = None ; oOOO0O0o = None ; o0O = None ; I11 = None
try : oOOO0O0o = urllib . unquote_plus ( I1Iii1I [ "site" ] )
except : pass
try : iiiiiIIii = urllib . unquote_plus ( I1Iii1I [ "url" ] )
except : pass
try : oo0OooOOo0 = urllib . unquote_plus ( I1Iii1I [ "name" ] )
except : pass
try : iIIiIIIIiII = int ( I1Iii1I [ "mode" ] )
except : pass
try : o0O = urllib . unquote_plus ( I1Iii1I [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( I1Iii1I [ "fanart" ] )
except : pass
try : I11 = urllib . unquote_plus ( I1Iii1I [ "description" ] )
except : pass
if 99 - 99: O0 + O0 * O00OoOoo00 + O0 * i1iII1I1i1i1
if iIIiIIIIiII == None or iiiiiIIii == None or len ( iiiiiIIii ) < 1 : I1I ( )
if 80 - 80: iiI1iIiI . iiiI11
if 47 - 47: O00OoOoo00 + IiIi1Iii1I1 + i11Ii11I1Ii1i % i11iIiiIii
if 93 - 93: o000o0o00o0Oo % Oooo0000 . O0 / oooOOOOO * i1iII1I1i1i1
if 29 - 29: i1IIi11111i
if 86 - 86: i11Ii11I1Ii1i . IiiIII111ii
elif iIIiIIIIiII == 1 : oOOOOo0 ( oo0OooOOo0 , iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 2 : I11iI ( oo0OooOOo0 , iiiiiIIii , o0O )
elif iIIiIIIIiII == 3 : oo00ooOoo ( oo0OooOOo0 , iiiiiIIii , o0O )
if 2 - 2: OoooooooOO
if 60 - 60: i1
if 81 - 81: Oooo0000 % iiiI11
elif iIIiIIIIiII == 4 : Iiii ( iiiiiIIii )
elif iIIiIIIIiII == 5 : O0OOO ( iiiiiIIii )
elif iIIiIIIIiII == 6 : oOo0O0Oo00oO ( )
elif iIIiIIIIiII == 7 : O00o0OO0 ( iiiiiIIii )
elif iIIiIIIIiII == 8 : O0oO ( iiiiiIIii )
elif iIIiIIIIiII == 9 : OOOOo0 ( iiiiiIIii )
elif iIIiIIIIiII == 10 : iI1111iiii ( iiiiiIIii )
elif iIIiIIIIiII == 11 : iIi1ii ( )
elif iIIiIIIIiII == 12 : ooO0OO ( iiiiiIIii )
elif iIIiIIIIiII == 13 : oO00oOOoooO ( iiiiiIIii )
elif iIIiIIIIiII == 14 : OOOO0OoOO0o0o ( iiiiiIIii )
elif iIIiIIIIiII == 15 : OooOo0ooo ( )
elif iIIiIIIIiII == 16 : IIo00ooo ( oo0OooOOo0 , iiiiiIIii , o0O )
elif iIIiIIIIiII == 17 : ooOOoooooo ( iiiiiIIii )
elif iIIiIIIIiII == 18 : IIi1 ( iiiiiIIii )
elif iIIiIIIIiII == 19 : Ooo00o0Oooo ( iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 20 : oOo0oO ( )
elif iIIiIIIIiII == 21 : OO ( iiiiiIIii )
elif iIIiIIIIiII == 22 : OOO ( iiiiiIIii )
elif iIIiIIIIiII == 23 : o0000oO ( )
elif iIIiIIIIiII == 24 : o00Oo0oooooo ( iiiiiIIii )
elif iIIiIIIIiII == 25 : oo0 ( iiiiiIIii , o0O )
elif iIIiIIIIiII == 26 : iI1I111I ( iiiiiIIii )
elif iIIiIIIIiII == 27 : o0OOOOooo ( iiiiiIIii , o0O )
elif iIIiIIIIiII == 28 : iI1IiI ( )
elif iIIiIIIIiII == 29 : IIii11I1i1I ( iiiiiIIii )
elif iIIiIIIIiII == 30 : iiIi1i ( iiiiiIIii )
elif iIIiIIIIiII == 31 : oo0oO0 ( iiiiiIIii )
elif iIIiIIIIiII == 32 : IIioOoO00oo0O ( iiiiiIIii )
elif iIIiIIIIiII == 33 : IIiIi ( iiiiiIIii )
elif iIIiIIIIiII == 34 : iiI11i1II ( iiiiiIIii )
elif iIIiIIIIiII == 35 : ii1iIi1II ( )
elif iIIiIIIIiII == 36 : I1i ( iiiiiIIii )
elif iIIiIIIIiII == 37 : ii111i ( iiiiiIIii , o0O )
elif iIIiIIIIiII == 38 : I1ii ( )
elif iIIiIIIIiII == 39 : OOOO0O00o ( iiiiiIIii )
elif iIIiIIIIiII == 40 : oOo0oO ( )
elif iIIiIIIIiII == 41 : OO ( iiiiiIIii )
elif iIIiIIIIiII == 42 : oooOOOO0oooo ( iiiiiIIii )
elif iIIiIIIIiII == 43 : OO00oOooo0O ( iiiiiIIii , o0O )
elif iIIiIIIIiII == 44 : IIioo0OO ( )
if 87 - 87: iIii1I11I1II1 . OoooooooOO * Oooo0000
elif iIIiIIIIiII == 45 : iii11 ( )
elif iIIiIIIIiII == 46 : Ooooooo ( iiiiiIIii )
elif iIIiIIIIiII == 47 : iI1iIIIi1i ( oo0OooOOo0 , iiiiiIIii , o0O )
elif iIIiIIIIiII == 48 : IIIIIo0ooOoO000oO ( )
elif iIIiIIIIiII == 49 : ooo0O ( iiiiiIIii )
elif iIIiIIIIiII == 50 : O0iII1 ( iiiiiIIii )
elif iIIiIIIIiII == 51 : i1ii ( iiiiiIIii )
elif iIIiIIIIiII == 52 : oOooOO ( iiiiiIIii )
elif iIIiIIIIiII == 53 : OO0oo ( iiiiiIIii )
elif iIIiIIIIiII == 54 : OOOIII1iI1iII1I ( iiiiiIIii , o0O )
if 100 - 100: i1 / i1IIi - iiI1iIiI % iiiI11 - iIii1I11I1II1
if 17 - 17: O00OoOoo00 / i1IIi11111i % ooo0Oo0
if 71 - 71: IiiIII111ii . i1iIIi1 . i1
elif iIIiIIIIiII == 59 : II1111ii ( )
elif iIIiIIIIiII == 60 : ii1III11 ( iiiiiIIii )
elif iIIiIIIIiII == 61 : ooOOo00O00Oo ( oo0OooOOo0 , iiiiiIIii , o0O )
if 68 - 68: i11iIiiIii % i1iII1I1i1i1 * i1 * IiiIII111ii * i11Ii11I1Ii1i + O0
elif iIIiIIIIiII == 66 : oOoOOo ( )
elif iIIiIIIIiII == 67 : O0Oo0o000oO ( iiiiiIIii )
elif iIIiIIIIiII == 68 : OOOoO000 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 69 : I1iIiI11I1 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 70 : I1i11ii11 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 71 : Ooooo00o0OoO ( )
elif iIIiIIIIiII == 72 : IIi11IIiIii1 ( )
elif iIIiIIIIiII == 73 : I1i11II ( )
elif iIIiIIIIiII == 74 : II ( iiiiiIIii )
elif iIIiIIIIiII == 75 : iiIii1I ( iiiiiIIii )
if 66 - 66: O00OoOoo00 % o000o0o00o0Oo % OoooooooOO
if 34 - 34: i1IIi11111i / oooOOOOO % O0 . i1 . i1IIi
elif iIIiIIIIiII == 884 : IiI ( )
elif iIIiIIIIiII == 885 : I1Ii ( )
elif iIIiIIIIiII == 886 : I1IiIiIi1IiI1 ( )
elif iIIiIIIIiII == 887 : O0oOo ( iiiiiIIii , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 888 : o0OoOo00o0o ( )
elif iIIiIIIIiII == 889 : I1iiIII ( iiiiiIIii , iIIiIIIIiII , oo0OooOOo0 , o0O , I1ii11iIi11i )
elif iIIiIIIIiII == 890 : OO0 ( )
elif iIIiIIIIiII == 891 : I1Io00oOOoO0oO ( )
elif iIIiIIIIiII == 892 : oOO ( )
if 29 - 29: O0 . i1iIIi1
if iIIiIIIIiII == None or iiiiiIIii == None or len ( iiiiiIIii ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 66 - 66: i1iII1I1i1i1 * iIii1I11I1II1 % iIii1I11I1II1 * IiiIII111ii - IiIi1Iii1I1 - IiiIII111ii
if 70 - 70: i1iIIi1 + i1iII1I1i1i1
if 93 - 93: i1iIIi1 + iiiI11
if 33 - 33: O0
if 78 - 78: O0 / i11Ii11I1Ii1i * i1
if 50 - 50: OoooooooOO - iIii1I11I1II1 + i1IIi % i1iIIi1 - iIii1I11I1II1 % O0
if 58 - 58: IiiIII111ii + iIii1I11I1II1
if 65 - 65: i11Ii11I1Ii1i - i1iIIi1 % i1IIi11111i - Oooo0000 * oooOOOOO + iiiI11
if 79 - 79: IiIi1Iii1I1 . Oooo0000 % i1iIIi1 - ooo0Oo0
if 69 - 69: IiIi1Iii1I1 - i1IIi11111i . IiIi1Iii1I1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
