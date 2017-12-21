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
   if 10 - 10: i1iII1I1i1i1 + i1IIi
   if 87 - 87: iiI1iIiI
   if 58 - 58: Oooo0000 % i1IIi11111i
   if 50 - 50: i1iIIi1 . i1IIi11111i
   if 97 - 97: O0 + Oooo0000
   if 89 - 89: i1IIi11111i + i1 * O00OoOoo00 * iiiI11
   if 37 - 37: OoooooooOO - O0 - i1IIi11111i
   if 77 - 77: i1iIIII * iIii1I11I1II1
   if 98 - 98: iiI1iIiI % iiiI11 * OoooooooOO
   if 51 - 51: iIii1I11I1II1 . Oooo0000 / i1iII1I1i1i1 + i1IIi11111i
   if 33 - 33: IiIi1Iii1I1 . i11Ii11I1Ii1i % oooOOOOO + i1IIi11111i
   if 71 - 71: ooo0Oo0 % i1iIIII
   if 98 - 98: O00OoOoo00 % i11iIiiIii % IiIi1Iii1I1 + iiiI11
   if 78 - 78: o000o0o00o0Oo % i1iII1I1i1i1 / oooOOOOO - iIii1I11I1II1
   if 69 - 69: i1iIIi1
   if 11 - 11: iiI1iIiI
   if 16 - 16: iiiI11 + IiiIII111ii * O0 % i1IIi . iiI1iIiI
   if 67 - 67: OoooooooOO / iiI1iIiI * iiiI11 + O00OoOoo00
   if 65 - 65: OoooooooOO - o000o0o00o0Oo / IiIi1Iii1I1 / i11Ii11I1Ii1i / i1IIi
   if 71 - 71: i1iIIi1 + iiiI11
   if 28 - 28: i1iIIII
   if 38 - 38: IiIi1Iii1I1 % i11Ii11I1Ii1i % O00OoOoo00 / i1 + Oooo0000 / i1IIi
   if 54 - 54: iIii1I11I1II1 % o000o0o00o0Oo - i1iIIII / i1iII1I1i1i1 - i1 . O00OoOoo00
   if 11 - 11: o000o0o00o0Oo . i1 * IiiIII111ii * OoooooooOO + IiIi1Iii1I1
   if 33 - 33: O0 * i1IIi11111i - i1iIIi1 % i1iIIi1
   if 18 - 18: i1iIIi1 / ooo0Oo0 * i1iIIi1 + i1iIIi1 * i11iIiiIii * o000o0o00o0Oo
   if 11 - 11: IiIi1Iii1I1 / Oooo0000 - IiiIII111ii * OoooooooOO + OoooooooOO . Oooo0000
   if 26 - 26: iiiI11 % o000o0o00o0Oo
   if 76 - 76: IiiIII111ii * oooOOOOO
   if 52 - 52: i1iIIII
   if 19 - 19: iiI1iIiI
   if 25 - 25: iiiI11 / IiIi1Iii1I1
   if 31 - 31: i1iIIII . O0 % iiI1iIiI . i1IIi11111i + IiiIII111ii
   if 71 - 71: i1iIIi1 . i11Ii11I1Ii1i
   if 62 - 62: OoooooooOO . O00OoOoo00
   if 61 - 61: Oooo0000 - i1iIIII - i1IIi
   if 25 - 25: O0 * O00OoOoo00 + o000o0o00o0Oo . i1IIi11111i . i1IIi11111i
   if 58 - 58: iiI1iIiI
   if 53 - 53: i1IIi
   if 59 - 59: i1IIi11111i
   if 81 - 81: Oooo0000 - Oooo0000 . oooOOOOO
   if 73 - 73: O00OoOoo00 % i11iIiiIii - iiI1iIiI
   if 7 - 7: O0 * i11iIiiIii * iiiI11 + IiIi1Iii1I1 % i1 - IiIi1Iii1I1
   if 39 - 39: ooo0Oo0 * i1iIIII % i1iIIII - OoooooooOO + i1IIi11111i - O00OoOoo00
   if 23 - 23: i11iIiiIii
   if 30 - 30: i1IIi11111i - i1IIi % i11Ii11I1Ii1i + O00OoOoo00 * iIii1I11I1II1
   if 81 - 81: IiiIII111ii % i1IIi . iIii1I11I1II1
   if 4 - 4: i11iIiiIii % i1 % i1IIi / IiiIII111ii
   if 6 - 6: oooOOOOO / iiI1iIiI % i1iIIII - iiI1iIiI
   if 31 - 31: i1iIIII
   if 23 - 23: i1iIIi1 . IiiIII111ii
   if 92 - 92: Oooo0000 + i1iIIi1 * iiiI11 % iiI1iIiI
   if 42 - 42: ooo0Oo0
   if 76 - 76: iiI1iIiI * oooOOOOO % i1iIIi1
def OoooO00o ( url ) :
 if 73 - 73: i1iIIII / i1iII1I1i1i1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'video-title="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
  I1IiI = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  I1ii11iIi11i = re . compile ( 'url="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ] . replace ( '&amp;' , '&' )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  if not 'http' in url :
   if not 'Deleted video' in III1iII1I1ii :
    OOOo00oo0oO = 'https://www.youtube.com' + url
    O000oo0O ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , OOOo00oo0oO , 2 , I1IiI , I1ii11iIi11i )
    if 100 - 100: i1iII1I1i1i1 / i1iIIi1 / o000o0o00o0Oo
def oOoOOo0O ( ) :
 if 84 - 84: i1 + i1IIi - i11Ii11I1Ii1i . o000o0o00o0Oo * OoooooooOO + iiI1iIiI
 iiiiiIIii = 'http://burningwhee1s.blogspot.co.uk/'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class=\'clearfix\' id=\'content\'>(.+?)<div id=\'main-wrapper\'>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a dir=\'ltr\' href=\'(.+?)\'>(.+?)</a>' ) . findall ( IIIii1II1II )
 for OOOO , III1iII1I1ii in OoO0o :
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OOOO , 24 , I1IiI , Oo , '' )
  if 38 - 38: i1iIIII + i11Ii11I1Ii1i % IiIi1Iii1I1 % Oooo0000 - iiiI11 / OoooooooOO
def oOOoo0000O0o0 ( url ) :
 if 1 - 1: i1iII1I1i1i1 + i1iII1I1i1i1 % Oooo0000 + i11iIiiIii
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<h3 class=\'post-title entry-title\'>(.+?)<div class=\'jump-link\'>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=\'.+?\'>(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( '<img border=".+?" src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href=\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 25 , I1IiI , Oo , '' )
  if 56 - 56: i1IIi11111i
def I1 ( url , iconimage ) :
 if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . i1IIi11111i / i11Ii11I1Ii1i % ooo0Oo0
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class=\'post-header\'>(.+?)<div class=\'post-footer\'>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<div class=".+?" style=".+?">(.+?)</select>' ) . findall ( IIIii1II1II )
 try :
  for oO0Oo in OoO0o :
   III1iII1I1ii = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 0 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   try :
    i1i11I11 = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 3 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
   except IndexError :
    try :
     i1i11I11 = re . compile ( '<b>(.+?)</b>' ) . findall ( oO0Oo ) [ 2 ] . replace ( '<span style="font-size: large;">' , '' ) . replace ( '</span>' , '' )
    except IndexError :
     i1i11I11 = ''
   III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
   i1i11I11 = o0OO0o0o00o ( i1i11I11 )
   iiiiII1I = re . compile ( '<option value="(.+?)"' ) . findall ( oO0Oo ) [ 1 ]
   O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "  " + i1i11I11 + "[/COLOR]" , iiiiII1I , 2 , I1IiI , Oo , '' )
 except :
  O000oo0O ( "[COLOR yellow]Sorry No Links Available[/COLOR]" , 'video' , 999 , I1IiI , Oo , '' )
  if 86 - 86: i1IIi11111i
def i1Iii11Ii1i1 ( ) :
 if 59 - 59: ooo0Oo0 % OoooooooOO . oooOOOOO / IiiIII111ii + iiI1iIiI
 if 76 - 76: IiIi1Iii1I1
 iiiiiIIii = 'https://api.themoviedb.org/3/movie/popular?api_key=' + I1i1iiI1 + '&language=en-US&page=1'
 OOOO = i11i1 ( iiiiiIIii )
 I11i1I1I = json . loads ( OOOO )
 OoO0O00O0oo0O = I11i1I1I [ 'results' ]
 for I1IiI11 in OoO0O00O0oo0O :
  iI1iiiiIii = 'https://image.tmdb.org/t/p/w640'
  III1iII1I1ii = I1IiI11 [ 'title' ]
  I1IiI = I1IiI11 [ 'poster_path' ]
  iIiIiIiI = I1IiI11 [ 'id' ]
  I1IiI = iI1iiiiIii + I1IiI
  I1ii11iIi11i = I1IiI11 [ 'backdrop_path' ]
  I1ii11iIi11i = iI1iiiiIii + I1ii11iIi11i
  i11 = I1IiI11 [ 'overview' ]
  iIiIiIiI = str ( iIiIiIiI )
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , III1iII1I1ii , 33 , I1IiI , I1ii11iIi11i , i11 )
  if 98 - 98: ooo0Oo0 / iiI1iIiI . O0 + i1
def ii ( url ) :
 if 25 - 25: OoooooooOO - iiI1iIiI . iiI1iIiI * i1iII1I1i1i1
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
  o000oo = re . compile ( '<a class=\"pagecurrent\".+?pagelink\"\s.+?href=([^ ]+)' ) . findall ( OOOO ) [ 0 ]
  o00o0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
  O00oO ( '[COLOR yellow]Next Page >>[/COLOR]' , o000oo , 26 , o00o0 , I1ii11iIi11i )
 except : pass
 if 50 - 50: ooo0Oo0 / ooo0Oo0 % o000o0o00o0Oo . o000o0o00o0Oo
def O0O0Oo00 ( url , iconimage ) :
 if 80 - 80: i1iII1I1i1i1 + i1iIIII / O00OoOoo00
 OOOO = i11i1 ( url )
 I1IiI = re . compile ( '<div class="thumb mvic-thumb".+?url(.+?);">' ) . findall ( OOOO ) [ 0 ] . replace ( '(' , '' ) . replace ( ')' , '' )
 IIIii1II1II = re . compile ( '<p class="server_servername">(.+?)</a>' ) . findall ( OOOO )
 iIiiiI . create ( o0OoOoOO00 , '[COLOR aqua]' + "Searching Links" + "[/COLOR]" )
 iIiiiI . update ( 0 )
 iiIiI = 1
 oOOO00O0O0OOo = [ ]
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  oOOO00O0O0OOo . append ( url )
  iIiiiI . update ( 100 , '[COLOR aqua]Generating links  [COLOR aqua][COLOR yellow]Found - %s Links' "[/COLOR]" % str ( iiIiI ) )
  time . sleep ( 0.02 )
  iiIiI += 1
  III1iII1I1ii = re . compile ( '(.+?)</p>' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'Server' , '' )
  III1iII1I1ii = III1iII1I1ii . strip ( )
 OOo00O = 1
 I1IIiiIiii = 0
 OooOOOO = 0
 while not xbmc . Player ( ) . isPlaying ( ) :
  if 45 - 45: o000o0o00o0Oo % iiI1iIiI - i11iIiiIii
  if iIiiiI . iscanceled ( ) :
   iIiiiI . close ( )
   quit ( )
  if I1IIiiIiii > len ( oOOO00O0O0OOo ) :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]None of the links played![/COLOR]" , I1IiI , 50 )
   quit ( )
   if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * iiI1iIiI
  if OooOOOO == 0 :
   I1IIiiIiii += 1
   iIiiiI . update ( 100 , "[COLOR aqua]Attempting to play link :: [COLOR yellow]" + str ( I1IIiiIiii ) + "[/COLOR]" , '' )
   try :
    OOOO = i11i1 ( oOOO00O0O0OOo [ I1IIiiIiii ] )
    OoO0o = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( OOOO ) [ 0 ]
    iII1ii1 = base64 . b64decode ( OoO0o )
    url = re . compile ( 'src="(.+?)"' ) . findall ( iII1ii1 ) [ 0 ]
    I1i1iiiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
    iIIi = open ( I1i1iiiI1 ) . read ( )
    oO0o00oo0 = re . compile ( '<url>(.+?)</url>' ) . findall ( iIIi )
    for ii1IIII in oO0o00oo0 :
     oO00oOooooo0 = re . compile ( '<bad>(.+?)<bad>' ) . findall ( ii1IIII ) [ 0 ]
     if url == oO00oOooooo0 :
      url = 'bad'
      iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] is blacklisted![/COLOR]" % str ( I1IIiiIiii ) )
      time . sleep ( 0.5 )
      OooOOOO = 5
      pass
    import urlresolver
    if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
     oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
    elif liveresolver . isValid ( url ) == True :
     oOo = liveresolver . resolve ( url )
    else : oOo = url
    O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
    xbmc . Player ( ) . play ( oOo , O0O0OOOOoo , False )
   except :
    iIiiiI . update ( 100 , '' , "[COLOR aqua]Link [COLOR yellow] %s [COLOR aqua] failed![/COLOR]" % str ( I1IIiiIiii ) )
    time . sleep ( 0.5 )
    OooOOOO = 5
    pass
  if OooOOOO == 5 :
   OooOOOO = 0
   xbmc . Player ( ) . stop ( )
  else :
   time . sleep ( 1 )
   OooOOOO += 1
   if 64 - 64: IiIi1Iii1I1 - Oooo0000 - iiI1iIiI . O0 + ooo0Oo0
 try : iIiiiI . close ( )
 except : pass
 time . sleep ( 15 )
 I1i1iiiI1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'blacklist.txt' ) )
 OOO00O = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Is The Movie Playing For You?[/COLOR]' , '' , yeslabel = 'Yes' , nolabel = 'No' )
 if OOO00O :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Enjoy Your Content![/COLOR]" , I1IiI , 500 )
  quit ( )
 else :
  with open ( I1i1iiiI1 , "a" ) as i1II1I1Iii1 :
   i1II1I1Iii1 . write ( '<url><bad>' + url + '<bad></url>\n' )
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]Ok we blacklisted the link Please try the movie again![/COLOR]" , I1IiI , 5000 )
   time . sleep ( 2 )
   xbmc . Player ( ) . stop ( )
   quit ( )
   if 30 - 30: OoooooooOO - Oooo0000
def Ooo00O0o ( url ) :
 if 72 - 72: iIii1I11I1II1 * iiiI11 % IiIi1Iii1I1 / i1
 if 35 - 35: IiIi1Iii1I1 + i1IIi % o000o0o00o0Oo % O00OoOoo00 + i1iII1I1i1i1
 if url == 'search' :
  iiiI = ''
  I1ii1 = xbmc . Keyboard ( iiiI , 'Enter Search Term' )
  I1ii1 . doModal ( )
  if I1ii1 . isConfirmed ( ) :
   iiiI = I1ii1 . getText ( )
   if len ( iiiI ) > 1 :
    O00 = iiiI . lower ( )
    if 92 - 92: iIii1I11I1II1 * i1IIi * oooOOOOO % i1iIIII % o000o0o00o0Oo + i11Ii11I1Ii1i
   else :
    Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o0O , 5000 )
    quit ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , o0O , 5000 )
   quit ( )
  O00 = O00 . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + O00 + '.html'
  i1iIi1I1i ( url , I1IiI )
  if 1 - 1: O00OoOoo00 % i1iIIII + O0 + i1IIi - i1
 else :
  url = url . replace ( ' ' , '+' )
  url = 'http://123movies.net/search-movies/' + url + '.html'
  i1iIi1I1i ( url , I1IiI )
  if 22 - 22: iiI1iIiI % o000o0o00o0Oo
def i1iIi1I1i ( url , icon ) :
 if 57 - 57: i1iIIII + O0 . iiiI11
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="ml-item">(.+?)</span>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = re . compile ( '<i>(.+?)</i>' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
  icon = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 27 , icon , I1ii11iIi11i )
  if 46 - 46: IiiIII111ii
def ii1iIi1iIiI1i ( ) :
 if 40 - 40: i1IIi % i1iIIII
 iiiiiIIii = 'http://www.genti.stream/'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="date">(.+?)<!-- Table.+?finish-->' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  ooo0o00 = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ] . strip ( )
  ooO = re . compile ( '<div class="team-name">(.+?)</div>' ) . findall ( oO0Oo ) [ 1 ] . strip ( )
  iiiiiIIii = re . compile ( 'href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.genti.stream/' + iiiiiIIii
  O000oo0O ( "[COLOR aqua]" + ooo0o00 + "[COLOR yellow] vs [COLOR aqua]" + ooO + "[/COLOR]" , iiiiiIIii , 39 , I1IiI , I1ii11iIi11i )
  if 74 - 74: iiI1iIiI
def o0o0oOoOO0O ( url ) :
 if 16 - 16: IiiIII111ii % iIii1I11I1II1 . iiiI11
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oooooOOO000Oo = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 if not 'http' in oooooOOO000Oo :
  oooooOOO000Oo = 'http://www.genti.stream' + oooooOOO000Oo
 oO0o0Ooooo = i11i1 ( oooooOOO000Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Ooo00OoOOO = re . compile ( '<iframe.+?src="(.+?)"' ) . findall ( oO0o0Ooooo ) [ 0 ]
 I1iI1ii1II = i11i1 ( Ooo00OoOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
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
 if 98 - 98: iIii1I11I1II1 * o000o0o00o0Oo * i1iIIII + IiIi1Iii1I1 % i11iIiiIii % O0
 if 'http' not in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR aqua]Sorry, No Link Avilable At The Moment![/COLOR]" , o0O , 5000 )
  quit ( )
 I11iI ( oo0OooOOo0 , url , o0O )
 if 27 - 27: O0
 if 79 - 79: i1IIi11111i - O00OoOoo00 + i1IIi11111i . i1iII1I1i1i1
def ii1III11 ( url ) :
 if 7 - 7: oooOOOOO % O0 . Oooo0000 + iiI1iIiI - O00OoOoo00
 o0o0O00oo0 = cfscrape . create_scraper ( )
 O000OO0 = o0o0O00oo0 . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="alphabet">(.+?)</div>' ) . findall ( O000OO0 ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II )
 for url , III1iII1I1ii in OoO0o :
  url = 'http://kimcartoon.me/CartoonList' + url
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 30 , I1IiI , I1ii11iIi11i , '' )
  if 27 - 27: i11iIiiIii % i11Ii11I1Ii1i % O00OoOoo00 . O0 - ooo0Oo0 + Oooo0000
def ooO0o ( url ) :
 if 51 - 51: IiiIII111ii
 o0o0O00oo0 = cfscrape . create_scraper ( )
 O000OO0 = o0o0O00oo0 . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<div class="item.+?"(.+?)</a>' ) . findall ( O000OO0 )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<span class="title">(.+?)</span>' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'http://kimcartoon.me' + url
  try :
   ii11I1 = re . compile ( 'description&quot;>(.+?)</p>' ) . findall ( oO0Oo ) [ 0 ]
   ii11I1 = o0OO0o0o00o ( ii11I1 )
  except IndexError :
   ii11I1 = ''
  O00oO ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 31 , I1IiI , I1ii11iIi11i , ii11I1 )
  if 75 - 75: i1 / i11Ii11I1Ii1i % O0
 try :
  Ii111iIi1iIi = re . compile ( '<li>(.+?)Next' ) . findall ( O000OO0 )
  for oO0Oo in Ii111iIi1iIi :
   o000oo = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ - 1 ]
   IIIIIo0ooOoO000oO = 'http://kimcartoon.me' + o000oo
   OOo = 'https://i.imgur.com/mjCRjXT.png'
   O00oO ( "[COLOR yellow][B]Next Page ===>[/B][/COLOR]" , IIIIIo0ooOoO000oO , 30 , OOo , I1ii11iIi11i )
 except : pass
 if 50 - 50: IiIi1Iii1I1
def o0O0O0ooo0oOO ( url ) :
 if 97 - 97: iiI1iIiI / oooOOOOO
 o0o0O00oo0 = cfscrape . create_scraper ( )
 O000OO0 = o0o0O00oo0 . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIii1II1II = re . compile ( '<td>(.+?)</td>' ) . findall ( O000OO0 )
 for oO0Oo in IIIii1II1II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
   url = 'http://kimcartoon.me' + url
   O000oo0O ( "[COLOR aqua][B]" + III1iII1I1ii + "[/B][/COLOR]" , url , 32 , I1IiI , I1ii11iIi11i )
  except : pass
  if 71 - 71: i11Ii11I1Ii1i / i1IIi . o000o0o00o0Oo % OoooooooOO . Oooo0000
def Iiiiii111i1ii ( url ) :
 if 25 - 25: i1iIIII - IiIi1Iii1I1 / i11iIiiIii
 o0 = Iii1ii1II11i . select ( '[COLOR aqua]Choose A Source[/COLOR]' , [ '[COLOR yellow]Rapid Video[/COLOR]' , '[COLOR yellow]Openload [COLOR aqua](Requires Pairing)[/COLOR]' ] )
 if o0 == 0 :
  url = url + '&s=rapidvideo'
  o0o0O00oo0 = cfscrape . create_scraper ( )
  O000OO0 = o0o0O00oo0 . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
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
  o0o0O00oo0 = cfscrape . create_scraper ( )
  O000OO0 = o0o0O00oo0 . get ( url ) . content . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  try :
   OoO0o = re . compile ( '<div id="divContentVideo"(.+?)</iframe>' ) . findall ( O000OO0 )
   for OOOO in OoO0o :
    url = re . compile ( 'src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
    I11iI ( oo0OooOOo0 , url , o0O )
  except IndexError :
   Iii1ii1II11i . notification ( o0OoOoOO00 , "[COLOR yellow]No Links For This Source, Try Another[/COLOR]" , I1IiI , 5000 )
   if 41 - 41: i1IIi % oooOOOOO + iIii1I11I1II1
   if 2 - 2: iIii1I11I1II1 * ooo0Oo0 % i1iII1I1i1i1 - i11Ii11I1Ii1i - oooOOOOO
def iIi11iiIiI1I ( ) :
 if 3 - 3: i1IIi / i11Ii11I1Ii1i / i11iIiiIii * i1IIi - i11Ii11I1Ii1i
 iiiiiIIii = "http://www.loyalbooks.com/genre-menu"
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<td class="link menu">(.+?)</a>' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  if "paid" not in i1I1iI :
   oO0o0Ooooo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
   I1iI1ii1II = "http://www.loyalbooks.com" + oO0o0Ooooo
   oo0OooOOo0 = re . compile ( 'id="(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
   O00oO ( "[COLOR aqua]" + oo0OooOOo0 + "[/COLOR]" , I1iI1ii1II , 60 , I1IiI , Oo , '' )
   if 42 - 42: i11Ii11I1Ii1i . OoooooooOO . i1IIi11111i * i1iII1I1i1i1
def O0OOO0OOooo00 ( url ) :
 if 6 - 6: iiiI11 - IiIi1Iii1I1 * i1iIIII . oooOOOOO / O0 * IiIi1Iii1I1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '</table><br>(.+?)data-ad-format="horizontal' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 II11iI111i1 = re . compile ( '<td(.+?)</td>' , re . DOTALL ) . findall ( IIIii1II1II )
 for i1I1iI in II11iI111i1 :
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
 if 95 - 95: OoooooooOO - IiiIII111ii * iiI1iIiI + Oooo0000
 if 10 - 10: i1IIi11111i / i11iIiiIii
def o00 ( name , url , iconimage ) :
 if 85 - 85: o000o0o00o0Oo . i1iIIi1
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '{name:(.+?)}' , re . DOTALL ) . findall ( OOOO )
 for i1I1iI in IIIii1II1II :
  III1iII1I1ii = re . compile ( '"(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  OOOo00oo0oO = re . compile ( 'mp3:"(.+?)"' , re . DOTALL ) . findall ( i1I1iI ) [ 0 ]
  O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , OOOo00oo0oO , 10 , iconimage , Oo , '' )
  if 78 - 78: IiIi1Iii1I1 * i1iIIi1 + iIii1I11I1II1 + iIii1I11I1II1 / i1iIIi1 . iiiI11
def O000 ( ) :
 if 79 - 79: OoooooooOO - iiI1iIiI
 iiiiiIIii = 'http://www.shadownet.me/'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( "<div class=\"SideCategoryListClassic\">(.+?)</div>" ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II )
 for iiiiiIIii , III1iII1I1ii in OoO0o :
  III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
  if 'P2P' not in III1iII1I1ii :
   O00oO ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 49 , I1IiI , Oo , '' )
   if 69 - 69: O00OoOoo00
   if 95 - 95: IiIi1Iii1I1 + i11iIiiIii * i1iIIi1 - i1IIi * i1iIIi1 - iIii1I11I1II1
def oo0o0O0Oooooo ( url ) :
 if 1 - 1: IiIi1Iii1I1 % Oooo0000 * ooo0Oo0
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( "<div class=\"CategoryDescription\">(.+?)<br class=\"Clear\" />" ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<div class="ProductImage">(.+?)</a>' ) . findall ( IIIii1II1II )
 for oO0Oo in OoO0o :
  III1iII1I1ii = re . compile ( 'alt="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  O000oo0O ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 50 , I1IiI , Oo , '' )
 try :
  o000oo = re . compile ( '<a href=\"([^"]*)\">Next &raquo;</a>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
  I1IiI = 'http://i.imgur.com/CIZ8oYV.png'
  O00oO ( "[COLOR orange]Next Page --->[/COLOR]" , o000oo , 49 , I1IiI , Oo , '' )
 except : pass
 if 55 - 55: Oooo0000
def Ooo0oo0ooO ( url ) :
 if 74 - 74: O0 * i1iII1I1i1i1 - i11iIiiIii + i1iIIi1
 def Iii ( url ) :
  I1iiiiI1iI = urllib2 . Request ( url )
  I1iiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  I1iiiiI1iI . add_header ( 'Referer' , url )
  iIiiiii1i = urllib2 . urlopen ( I1iiiiI1iI , timeout = 5 )
  OOOO = iIiiiii1i . read ( )
  iIiiiii1i . close ( )
  return OOOO
  if 40 - 40: O0 - OoooooooOO - IiiIII111ii
 OOOO = Iii ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  IIIii1II1II = re . compile ( '<iframe src=\'(.+?)\'' ) . findall ( OOOO ) [ 0 ]
 except IndexError :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 if 'youtube' in IIIii1II1II :
  url = IIIii1II1II
  I11iI ( oo0OooOOo0 , url , o0O )
 I1iI1ii1II = Iii ( IIIii1II1II )
 url = re . compile ( 'source: "(.+?)"' ) . findall ( I1iI1ii1II ) [ 0 ]
 if 'http://thepk.co' in url :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry Channel Offline At The Moment[/COLOR]' , I1IiI , 5000 )
  quit ( )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 if 37 - 37: Oooo0000 / i11Ii11I1Ii1i / O0
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( oOo )
  xbmc . Player ( ) . play ( oOo , O0O0OOOOoo , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( oOo )
  xbmc . Player ( ) . play ( oOo , O0O0OOOOoo , False )
 else :
  if '.m3u8' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + oo0OooOOo0 + '&amp;url=' + url + '&amp;iconImage=' + o0O
  elif '.ts' in url :
   OOOo00oo0oO = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + oo0OooOOo0 + '&amp;url=' + url + '&amp;iconImage=' + o0O
  else :
   OOOo00oo0oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 76 - 76: iiI1iIiI . IiIi1Iii1I1 - o000o0o00o0Oo - oooOOOOO * i1
  O0O0OOOOoo = xbmcgui . ListItem ( oo0OooOOo0 , iconImage = o0O , thumbnailImage = o0O )
  O0O0OOOOoo . setPath ( url )
  if 54 - 54: IiiIII111ii + O0 + O00OoOoo00 * i1iIIi1 - i1iIIII % i1iII1I1i1i1
  xbmc . Player ( ) . play ( OOOo00oo0oO , O0O0OOOOoo , False )
  if 13 - 13: IiIi1Iii1I1 / oooOOOOO * i1 . i1 * IiIi1Iii1I1
  if 63 - 63: i1iIIi1 / O0 * ooo0Oo0 + i11Ii11I1Ii1i / IiiIII111ii + iiiI11
def OOoO000 ( ) :
 if 57 - 57: i11Ii11I1Ii1i
 iiiiiIIii = 'https://m.skylinewebcams.com/en/webcam'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 OoO0o = re . compile ( '<div id="list-menu">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 oOOOoo = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( OoO0o )
 for iiiiiIIii , III1iII1I1ii in oOOOoo :
  if 'http|https' not in iiiiiIIii :
   iiiiiIIii = 'https://m.skylinewebcams.com' + iiiiiIIii
   O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 46 , I1IiI , Oo , '' )
   if 15 - 15: i11iIiiIii % iiI1iIiI * O00OoOoo00 / i1iIIi1
def oooO0o0o0O0 ( url ) :
 if 27 - 27: OoooooooOO - oooOOOOO / O00OoOoo00
 OOOO = i11i1 ( url )
 OoO0o = re . compile ( '<div class="cam"><a href="(.+?)"><amp-img src="(.+?)" alt="(.+?)"' ) . findall ( OOOO )
 for url , I1IiI , III1iII1I1ii in OoO0o :
  if 'https:' not in I1IiI :
   I1IiI = 'https:' + I1IiI
  if 'https' not in url :
   url = 'https://m.skylinewebcams.com' + url
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 47 , I1IiI , Oo , '' )
  if 76 - 76: i1IIi11111i % iiI1iIiI . iIii1I11I1II1 - IiiIII111ii * OoooooooOO . oooOOOOO
  if 84 - 84: i1iIIi1 + O00OoOoo00
def IIiiIIi1 ( name , url , iconimage ) :
 if 59 - 59: IiiIII111ii . i1iIIII % i11Ii11I1Ii1i
 OOOO = i11i1 ( url )
 try :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  IIIii1II1II = re . compile ( '<amp-video src="(.+?)"' ) . findall ( OOOO ) [ 0 ]
  url = 'https:' + IIIii1II1II
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
  if 39 - 39: o000o0o00o0Oo
 except : pass
 quit ( 0 )
 if 97 - 97: i1iIIII - i1 / iiiI11 . i11iIiiIii % i1iII1I1i1i1 * i1iII1I1i1i1
def ii1IIIIiI11 ( ) :
 if 40 - 40: i1IIi11111i
 iiiiiIIii = 'https://watchepisodeseries.immunicity.st/home/schedule'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class="schedule-calendar">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<a href="(.+?)" class="passive"><span>(.+?)</span><br>(.+?)</a>' ) . findall ( IIIii1II1II )
 for iiiiiIIii , OOOooo , Oo00oo0000OO in OoO0o :
  O00oO ( "[COLOR aqua]" + OOOooo + "  " + Oo00oo0000OO + "[/COLOR]" , iiiiiIIii , 67 , I1IiI , I1ii11iIi11i )
  if 69 - 69: IiIi1Iii1I1 - i1 / i11iIiiIii + o000o0o00o0Oo % OoooooooOO
  if 73 - 73: iiiI11 - i1iIIi1
def O00oooo00o0O ( url ) :
 if 9 - 9: iiI1iIiI % iiI1iIiI % i11Ii11I1Ii1i
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="sl-box">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 1 ]
  III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  o0O = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  I1ii11iIi11i = re . compile ( 'style="background-image:.+?\'(.+?)\'' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , url , 68 , o0O , I1ii11iIi11i )
  if 30 - 30: IiiIII111ii + i1iIIi1 - IiiIII111ii . IiiIII111ii - i11Ii11I1Ii1i + O0
  if 86 - 86: i1IIi
def IIi11IIiIii1 ( url , iconimage , fanart ) :
 if 17 - 17: iiiI11 + i1iII1I1i1i1 . i1 - ooo0Oo0 * i11iIiiIii
 OOOO = i11i1 ( url )
 iioOo0OoOOo0 = re . compile ( '<ul class="sd-gallery">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in iioOo0OoOOo0 :
  fanart = re . compile ( 'data-src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
 IIIii1II1II = re . compile ( '<div class="watched">(.+?)<div class="el-item">' ) . findall ( OOOO )
 iiIiI = datetime . now ( )
 for oO0Oo in IIIii1II1II :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = re . compile ( '<div class="name">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
   iII11I1Ii1 = re . compile ( '<div class="season">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   o0o0 = re . compile ( '<div class="episode">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
   OOOooo = re . compile ( '<div class="date">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ] . replace ( '-' , '/' )
   if 'Air Date' not in OOOooo :
    OOOooo = OOOooo . strip ( )
    OOOooo = time . strptime ( OOOooo , "%d/%m/%Y" )
    oOo0oOIIi1IIIIi = ( "%s/%s/%s" % ( iiIiI . day , iiIiI . month , iiIiI . year ) )
    oOo0oOIIi1IIIIi = time . strptime ( oOo0oOIIi1IIIIi , "%d/%m/%Y" )
    if ( oOo0oOIIi1IIIIi < OOOooo ) :
     III1iII1I1ii = '[COLOR yellow]' + ( III1iII1I1ii ) + ' - Not Aired Yet' + '[/COLOR]'
     o0o0 = '[COLOR yellow]' + ( o0o0 ) + '[/COLOR]'
     iII11I1Ii1 = '[COLOR yellow]' + ( iII11I1Ii1 ) + '[/COLOR]'
     if 70 - 70: i1iIIII / i11Ii11I1Ii1i - iIii1I11I1II1 - oooOOOOO
    if not 'Season 0' in iII11I1Ii1 :
     O00oO ( "[COLOR aqua]" + iII11I1Ii1 + " " + o0o0 + " " + III1iII1I1ii + "[/COLOR]" , url , 69 , iconimage , fanart )
  except : pass
  if 11 - 11: iIii1I11I1II1 . OoooooooOO . i11Ii11I1Ii1i / i1IIi - O00OoOoo00
  if 30 - 30: Oooo0000
def Ii111 ( url , iconimage , fanart ) :
 if 67 - 67: O0
 if 52 - 52: i11Ii11I1Ii1i . IiIi1Iii1I1 / Oooo0000 / OoooooooOO . i11iIiiIii
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
  if 30 - 30: O00OoOoo00 / iiiI11 . IiiIII111ii . OoooooooOO - ooo0Oo0
  if 44 - 44: O0 * OoooooooOO % IiIi1Iii1I1 + i11Ii11I1Ii1i
def II1i1i1iII1 ( url , iconimage , fanart ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="wb-main">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  url = re . compile ( 'href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  import urlresolver
  try :
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   elif liveresolver . isValid ( url ) == True :
    oOo = liveresolver . resolve ( url )
   else : oOo = url
   O0O0OOOOoo = xbmcgui . ListItem ( iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
   O0O0OOOOoo . setPath ( oOo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
   xbmc . Player ( ) . play ( oOo )
   if 68 - 68: ooo0Oo0 + i11iIiiIii
  except :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Sorry Link Is Dead, Try Another[/COLOR]' , I1IiI , 5000 )
   if 69 - 69: iIii1I11I1II1 * iIii1I11I1II1 * i11iIiiIii + iiI1iIiI / i1iIIII % iiiI11
def O0OO0oOoO0O0O ( ) :
 if 99 - 99: i1iII1I1i1i1
 iiiI = ''
 I1ii1 = xbmc . Keyboard ( iiiI , 'Enter Search Term' )
 I1ii1 . doModal ( )
 if I1ii1 . isConfirmed ( ) :
  iiiI = I1ii1 . getText ( )
  if len ( iiiI ) > 1 :
   O00 = iiiI . lower ( )
   O00 = O00 . replace ( ' ' , '%20' )
   if 16 - 16: IiiIII111ii * Oooo0000 . IiIi1Iii1I1 / i1IIi . i1 - i1IIi
  else : quit ( )
 else : O00 = urllib . unquote_plus ( iiiiiIIii ) . lower ( ) ; iiiI = urllib . unquote_plus ( iiiiiIIii )
 iiiiiIIii = base64 . b64decode ( b'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzZXJpZXMuY29tL2hvbWUvc2VhcmNoP3E9' ) + O00
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '"series"(.+?)"series_id"' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'original_name":"(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '"seo_name":"(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.watchepisodeseries.com/' + OOOo00oo0oO
  I1IiI = 'http://www.watchepisodeseries.com/series_images/' + OOOo00oo0oO + '.jpg'
  O00oO ( III1iII1I1ii , iiiiiIIii , 68 , I1IiI , I1ii11iIi11i , '' )
  if 46 - 46: IiiIII111ii + iIii1I11I1II1 + i1iIIII + i1 . o000o0o00o0Oo
def iIiIi11Ii ( ) :
 if 23 - 23: i1iII1I1i1i1 - i1iIIII + O00OoOoo00
 iiiiiIIii = 'https://watchepisodeseries.immunicity.st/home/popular-series'
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<div class="cover-box">(.+?)<div class="cb-star">' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<div title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  III1iII1I1ii = o0OO0o0o00o ( III1iII1I1ii )
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  I1ii11iIi11i = re . compile ( 'style="background-image: (.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( 'url(\'' , '' ) . replace ( '\')' , '' )
  O00oO ( '[COLOR aqua]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 68 , I1IiI , I1ii11iIi11i )
  if 12 - 12: iiI1iIiI / IiIi1Iii1I1 % i1IIi11111i / i11iIiiIii % OoooooooOO
  if 15 - 15: iIii1I11I1II1 % OoooooooOO - ooo0Oo0 * iiiI11 + O00OoOoo00
def i1I1II1iIIi11 ( ) :
 if 49 - 49: OoooooooOO * O00OoOoo00 - ooo0Oo0 . i1iII1I1i1i1
 try :
  O000o0 = open ( i1i1II ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  iiiI = ''
  I1ii1 = xbmc . Keyboard ( iiiI , '[COLOR aqua]Enter The Password You Set[/COLOR]' )
  I1ii1 . doModal ( )
  if I1ii1 . isConfirmed ( ) :
   iiiI = I1ii1 . getText ( )
   if len ( iiiI ) > 1 :
    O00 = iiiI
   else : quit ( )
  if O00 == O000o0 :
   oO0 ( )
  else :
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Wrong Password, I\'m Telling Mum![/COLOR]' , I1IiI , 5000 )
   quit ( )
 except :
  Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Enter A Password To Prevent Unauthorised Access[/COLOR]" )
  iiiI = ''
  I1ii1 = xbmc . Keyboard ( iiiI , 'Enter The Password You Set' )
  I1ii1 . doModal ( )
  if I1ii1 . isConfirmed ( ) :
   iiiI = I1ii1 . getText ( )
   if len ( iiiI ) > 1 :
    O00 = iiiI
   else : quit ( )
  with open ( i1i1II , "w" ) as i1II1I1Iii1 :
   i1II1I1Iii1 . write ( O00 )
   Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Password Saved, Now Re Enter[/COLOR]' , I1IiI , 5000 )
   quit ( )
   if 75 - 75: IiiIII111ii % O00OoOoo00
   if 94 - 94: i1iII1I1i1i1 / iiI1iIiI / IiIi1Iii1I1 % i1iIIII
   if 96 - 96: iiI1iIiI % ooo0Oo0 . o000o0o00o0Oo + i1iIIII
def oO0 ( ) :
 if 42 - 42: i11Ii11I1Ii1i * oooOOOOO * i11iIiiIii - i1iIIII . OoooooooOO
 oo00o = 'http://streamarmy.co.uk/Main/LordJD/JAV.xml'
 oo0000Oo00o = '[COLOR aqua]Asian Special Porn[/COLOR]'
 O00oO ( oo0000Oo00o , oo00o , 1 , I1IiI , Oo , '' )
 iiiiiIIii = base64 . b64decode ( b'aHR0cHM6Ly93d3cuZXBvcm5lci5jb20v' )
 OOOO = i11i1 ( iiiiiIIii )
 IIIii1II1II = re . compile ( '<li class="">(.+?)</li>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<strong>(.+?)</strong>' ) . findall ( oO0Oo ) [ 0 ]
  O00oOo = re . compile ( '<div class="cllnumber">(.+?)</div>' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'https://www.eporner.com' + OOOo00oo0oO
  if not 'All' in III1iII1I1ii :
   if not 'Homemade' in III1iII1I1ii :
    O00oO ( "[COLOR aqua]" + III1iII1I1ii + "  " + "[COLOR yellow]" + O00oOo + "[/COLOR]" , iiiiiIIii , 36 , I1IiI , Oo , '' )
    if 26 - 26: IiiIII111ii % i1iIIi1 % i1iII1I1i1i1 % iiiI11
def O0oo0ooOOOO ( url ) :
 if 14 - 14: iiI1iIiI / OoooooooOO % iiI1iIiI . O0
 OOOO = i11i1 ( url )
 IIIii1II1II = re . compile ( '<div class="mbtit"(.+?)onmouseover=' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  I1IiI = re . compile ( 'src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = 'https://www.eporner.com' + OOOo00oo0oO
  O00oO ( "[COLOR skyblue]" + III1iII1I1ii + "[/COLOR]" , url , 37 , I1IiI , Oo , '' )
  if 94 - 94: Oooo0000 - ooo0Oo0 - iiI1iIiI % i1IIi
 try :
  o000oo = re . compile ( '<a href=\"([^"]*)\" title="Next page">' ) . findall ( OOOO ) [ 0 ]
  ooO0oOOooOo0 = 'https://www.eporner.com' + o000oo
  o00o0 = 'http://imgur.com/3eNoY0p'
  O00oO ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , ooO0oOOooOo0 , 36 , o00o0 , Oo , '' )
 except : pass
 if 19 - 19: i1IIi11111i
def Iiii1I1 ( url , iconimage ) :
 if 83 - 83: i1iIIII . i1iIIi1 + i1iII1I1i1i1 - i1iIIII * i1iIIi1 / i1iIIi1
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11I1 = re . compile ( '<div id="hd-porn-dload">(.+?)</div>' ) . findall ( OOOO ) [ 0 ]
 OoO0o = re . compile ( '<strong>(.+?)</strong>.+?<a href="(.+?)"' ) . findall ( I11I1 )
 for iiI1i1Iii111 , OOOO in OoO0o :
  iiI1i1Iii111 = iiI1i1Iii111 . replace ( ':' , '' )
  url = 'https://www.eporner.com' + OOOO
  O000oo0O ( "[COLOR red]" + "Link Quality :: " + "[COLOR silver]" + iiI1i1Iii111 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  if 43 - 43: i1IIi11111i
  if 71 - 71: i1iII1I1i1i1 % O00OoOoo00 * Oooo0000 . O0 / iiiI11 . o000o0o00o0Oo
  if 58 - 58: ooo0Oo0 / i1iII1I1i1i1
  if 44 - 44: i1iIIII
  if 54 - 54: iiiI11 - O00OoOoo00 - i1iIIi1 . iIii1I11I1II1
  if 79 - 79: iiiI11 . i1
  if 40 - 40: i1IIi11111i + ooo0Oo0 . i1IIi11111i % IiIi1Iii1I1
  if 15 - 15: iiiI11 * ooo0Oo0 % o000o0o00o0Oo * iIii1I11I1II1 - i11iIiiIii
  if 60 - 60: iiI1iIiI * i1iIIi1 % i1 + i1iII1I1i1i1
  if 52 - 52: i1IIi
  if 84 - 84: iiiI11 / IiiIII111ii
  if 86 - 86: Oooo0000 * i11Ii11I1Ii1i - O0 . Oooo0000 % iIii1I11I1II1 / i1iIIII
  if 11 - 11: iiI1iIiI * i1iII1I1i1i1 + o000o0o00o0Oo / o000o0o00o0Oo
  if 37 - 37: i11iIiiIii + i1IIi
  if 23 - 23: oooOOOOO + O00OoOoo00 . Oooo0000 * iiI1iIiI + o000o0o00o0Oo
  if 18 - 18: IiiIII111ii * i1IIi11111i . IiiIII111ii / O0
  if 8 - 8: i1IIi11111i
  if 4 - 4: o000o0o00o0Oo + o000o0o00o0Oo * IiIi1Iii1I1 - Oooo0000
  if 78 - 78: iiiI11 / i11Ii11I1Ii1i % Oooo0000
  if 52 - 52: i1iIIII - oooOOOOO * i1iII1I1i1i1
  if 17 - 17: OoooooooOO + i1iIIII * O00OoOoo00 * Oooo0000
  if 36 - 36: O0 + ooo0Oo0
  if 5 - 5: ooo0Oo0 * Oooo0000
  if 46 - 46: IiIi1Iii1I1
  if 33 - 33: oooOOOOO - i11Ii11I1Ii1i * OoooooooOO - ooo0Oo0 - i1iIIII
  if 84 - 84: i1iIIi1 + ooo0Oo0 - Oooo0000 * Oooo0000
  if 61 - 61: OoooooooOO . i1iII1I1i1i1 . OoooooooOO / ooo0Oo0
  if 72 - 72: i1IIi
  if 82 - 82: Oooo0000 + OoooooooOO / i11iIiiIii * o000o0o00o0Oo . OoooooooOO
  if 63 - 63: o000o0o00o0Oo
  if 6 - 6: IiIi1Iii1I1 / o000o0o00o0Oo
  if 57 - 57: O00OoOoo00
  if 67 - 67: i1 . IiIi1Iii1I1
  if 87 - 87: i1iII1I1i1i1 % iiiI11
  if 83 - 83: i11Ii11I1Ii1i - O00OoOoo00
  if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
  if 86 - 86: iIii1I11I1II1 + Oooo0000 . i11iIiiIii - iiiI11
  if 51 - 51: Oooo0000
  if 14 - 14: IiiIII111ii % i1iII1I1i1i1 % ooo0Oo0 - i11iIiiIii
  if 53 - 53: iiiI11 % ooo0Oo0
  if 59 - 59: i1iIIII % iIii1I11I1II1 . i1IIi + i11Ii11I1Ii1i * IiiIII111ii
  if 41 - 41: iiiI11 % o000o0o00o0Oo
  if 12 - 12: i1iIIII
  if 69 - 69: OoooooooOO + i1iIIII
  if 26 - 26: ooo0Oo0 + i1iIIII / i1 % Oooo0000 % o000o0o00o0Oo + i11Ii11I1Ii1i
  if 31 - 31: O00OoOoo00 % i1iIIII * O00OoOoo00
  if 45 - 45: i1IIi . iiI1iIiI + i1iIIII - OoooooooOO % IiIi1Iii1I1
  if 1 - 1: iIii1I11I1II1
  if 93 - 93: i1IIi . i11iIiiIii . ooo0Oo0
  if 99 - 99: O00OoOoo00 - i1iIIi1 - i1iII1I1i1i1 % i1
  if 21 - 21: i11Ii11I1Ii1i % o000o0o00o0Oo . i1IIi - OoooooooOO
def iiOOOO0o ( url ) :
 if 10 - 10: i1iIIi1 % iiI1iIiI
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="item">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( 'title="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( './' , '/' )
  if 97 - 97: OoooooooOO - i1iIIi1
  I1IiI = re . compile ( '<img src="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  iiI1i1Iii111 = re . compile ( '<span class="quality" >(.+?)</span>' ) . findall ( oO0Oo ) [ 0 ]
  O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[COLOR yellow] " + iiI1i1Iii111 + "[/COLOR]" , url , 43 , I1IiI , Oo , '' )
  if 58 - 58: iIii1I11I1II1 + O0
 try :
  ooO0oOOooOo0 = re . compile ( '<div class="pagination">(.+?)</div><div class="footer">' ) . findall ( OOOO ) [ 0 ]
  o000oo = re . compile ( '<a.+?href="(.+?)"' ) . findall ( ooO0oOOooOo0 ) [ 5 ]
  I111I11I111 = 'http://m4ufree.com' + o000oo
  if 'genre' in I111I11I111 :
   I111I11I111 = I111I11I111 . replace ( '.com' , '.com/' )
  iiiiI11ii = 'https://i.imgur.com/mjCRjXT.png'
  O00oO ( "[COLOR yellow]" + "Next Page" + "[/COLOR]" , I111I11I111 , 42 , iiiiI11ii , Oo , '' )
 except : pass
 if 96 - 96: oooOOOOO . O0 / oooOOOOO % O0
def o0o000 ( url , iconimage ) :
 if 50 - 50: IiiIII111ii % i1IIi
 import requests
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iii11II1I = re . compile ( 'data="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 iI111I11i = 'http://m4ufree.com/ajax_new.php'
 I1II1i11I1 = requests . post ( iI111I11i , data = { 'm4u' : iii11II1I } )
 json = ( I1II1i11I1 . text )
 iiIiIiII = re . compile ( 'sources:(.+?)]' ) . findall ( json ) [ 0 ]
 i1I1 = re . compile ( '{(.+?)}' ) . findall ( iiIiIiII )
 iIi = 0
 for iiIiI in i1I1 :
  try :
   iIi += 1
   III1iII1I1ii = 'Link ' + str ( iIi )
   iiI1i1Iii111 = re . compile ( '''"label":"(.+?)"''' ) . findall ( iiIiI ) [ 0 ]
   url = re . compile ( '''"file":"(.+?)"''' ) . findall ( iiIiI ) [ 0 ]
   O000oo0O ( "[COLOR aqua]" + III1iII1I1ii + " | [COLOR yellow] " + iiI1i1Iii111 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
  except IndexError :
   url = re . compile ( """file:.+?"(.+?)\"""" ) . findall ( iiIiI ) [ 0 ]
   iiI1i1Iii111 = re . compile ( """label:.+?'(.+?)'""" ) . findall ( iiIiI ) [ 0 ]
   O000oo0O ( "[COLOR aqua]" + "Link VIP | " + "[COLOR yellow] " + iiI1i1Iii111 + "[/COLOR]" , url , 2 , iconimage , Oo , '' )
   if 10 - 10: i1 / ooo0Oo0
def I1i ( ) :
 if 50 - 50: i1IIi11111i * iiiI11 % o000o0o00o0Oo / ooo0Oo0 - O0 % oooOOOOO
 iiiiiIIii = 'http://www.livefootballol.me/streaming/english-premier-league-2017/'
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<td>(.+?)</td>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  iiiiiIIii = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ]
  OOo0oO00ooO00 = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  iiiiiIIii = 'http://www.livefootballol.me' + iiiiiIIii
  O00oO ( "[COLOR aqua]" + OOo0oO00ooO00 + "[/COLOR]" , iiiiiIIii , 74 , o0O , Oo , '' )
  if 48 - 48: iiI1iIiI + o000o0o00o0Oo + i11Ii11I1Ii1i * i11iIiiIii
def IiIIi1I1I11Ii ( url ) :
 if 64 - 64: OoooooooOO
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<a href="(.+?)"' ) . findall ( OOOO )
 oO0oooooo = 0
 for OOOOoOoo0O0O0 in IIIii1II1II :
  if 'acestream' in OOOOoOoo0O0O0 :
   if 'http' in OOOOoOoo0O0O0 :
    oO0oooooo += 1
    III1iII1I1ii = '[COLOR aqua]Link :: ' + str ( oO0oooooo ) + '[/COLOR]'
    O000oo0O ( III1iII1I1ii , OOOOoOoo0O0O0 , 75 , o0O , Oo , '' )
 if oO0oooooo == 0 :
  O000oo0O ( "[COLOR yellow]No Links Yet, Try Closer To Kick Off[/COLOR]" , 'urls' , 999 , o0O , Oo , '' )
  if 65 - 65: IiiIII111ii + ooo0Oo0
def Ooo0O0 ( url ) :
 if 71 - 71: OoooooooOO
 OOOO = i11i1 ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 url = re . compile ( '<div class="uk-text-center"><a href="(.+?)"' ) . findall ( OOOO ) [ 0 ]
 I11iI ( oo0OooOOo0 , url , o0O )
 if 11 - 11: IiiIII111ii
def o0oooO ( url , getphp ) :
 I1iiiiI1iI = urllib2 . Request ( url )
 I1iiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 I1iiiiI1iI . add_header ( 'Cookie' , 'PHPSESSID=' + getphp )
 iIiiiii1i = urllib2 . urlopen ( I1iiiiI1iI , timeout = 10 )
 OOOO = iIiiiii1i . read ( )
 iIiiiii1i . close ( )
 return OOOO
 if 89 - 89: i11Ii11I1Ii1i / i1iII1I1i1i1
 if 14 - 14: i1iIIII . iiI1iIiI * IiIi1Iii1I1 + i11Ii11I1Ii1i - IiIi1Iii1I1 + i1iIIII
 if 18 - 18: i1iII1I1i1i1 - i1IIi11111i - iiI1iIiI - iiI1iIiI
def OOooo00 ( ) :
 if 35 - 35: i1iIIi1 . Oooo0000 * i11iIiiIii
 iiiiiIIii = 'http://m4ufree.com/?sort=key_top&page=1&='
 OOOO = i11i1 ( iiiiiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIii1II1II = re . compile ( '<div class="genre_item">(.+?)</div>' ) . findall ( OOOO )
 for oO0Oo in IIIii1II1II :
  III1iII1I1ii = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( oO0Oo ) [ 0 ]
  OOOo00oo0oO = re . compile ( '<a href="(.+?)"' ) . findall ( oO0Oo ) [ 0 ] . replace ( './' , '' )
  iiiiiIIii = 'http://m4ufree.com/' + OOOo00oo0oO
  if not re . search ( '\d+' , III1iII1I1ii ) :
   O00oO ( "[COLOR aqua]" + III1iII1I1ii + "[/COLOR]" , iiiiiIIii , 42 , I1IiI , Oo )
   if 44 - 44: i11iIiiIii / ooo0Oo0
   if 42 - 42: OoooooooOO + ooo0Oo0 % i11Ii11I1Ii1i + i1
   if 24 - 24: oooOOOOO * i11Ii11I1Ii1i % oooOOOOO % IiiIII111ii + OoooooooOO
   if 29 - 29: i11Ii11I1Ii1i - OoooooooOO - i11iIiiIii . i1IIi11111i
   if 19 - 19: i11Ii11I1Ii1i
   if 72 - 72: OoooooooOO / iiI1iIiI + iiiI11 / Oooo0000 * iiiI11
   if 34 - 34: O0 * O0 % OoooooooOO + oooOOOOO * iIii1I11I1II1 % iiiI11
   if 25 - 25: O00OoOoo00 + Oooo0000 . i1IIi11111i % Oooo0000 * i1iIIII
   if 32 - 32: i11iIiiIii - i1iIIi1
   if 53 - 53: OoooooooOO - IiiIII111ii
def o0OO0o0o00o ( text ) :
 if 87 - 87: i1iII1I1i1i1 . iiI1iIiI
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
 if 17 - 17: iiiI11 . i11iIiiIii
 return text
 if 5 - 5: o000o0o00o0Oo + O0 + O0 . i1iIIi1 - IiIi1Iii1I1
def o00oo0000 ( ) :
 if 44 - 44: ooo0Oo0 % iIii1I11I1II1
 oo0ooO0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IIiiiiIiIIii = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 O0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 IIIiIiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.nemesis/downloads' ) )
 if 7 - 7: IiiIII111ii . Oooo0000 / o000o0o00o0Oo . i1iIIII * O00OoOoo00 - i11Ii11I1Ii1i
 I1ii1iI1II11ii = 0
 for ( i1i1IiIiIi1Ii , oO0ooOO , IIi1iI1 ) in os . walk ( IIiiiiIiIIii ) :
  for file in IIi1iI1 :
   IIi11i1II = os . path . join ( i1i1IiIiIi1Ii , file )
   I1ii1iI1II11ii += os . path . getsize ( IIi11i1II )
 O0OOO0OOoO0O = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1ii1iI1II11ii / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 73 - 73: i1IIi11111i - iiI1iIiI * i1IIi / i11iIiiIii * i1iIIII % i11Ii11I1Ii1i
 I1ii1iI1II11ii = 0
 for ( i1i1IiIiIi1Ii , oO0ooOO , IIi1iI1 ) in os . walk ( oo0ooO0 ) :
  for file in IIi1iI1 :
   IIi11i1II = os . path . join ( i1i1IiIiIi1Ii , file )
   I1ii1iI1II11ii += os . path . getsize ( IIi11i1II )
 O0OOO0OOoO0O = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1ii1iI1II11ii / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 56 - 56: OoooooooOO * ooo0Oo0 . ooo0Oo0 . o000o0o00o0Oo
 I1ii1iI1II11ii = 0
 for ( i1i1IiIiIi1Ii , oO0ooOO , IIi1iI1 ) in os . walk ( O0OO ) :
  for file in IIi1iI1 :
   IIi11i1II = os . path . join ( i1i1IiIiIi1Ii , file )
   I1ii1iI1II11ii += os . path . getsize ( IIi11i1II )
 O0OOO0OOoO0O = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1ii1iI1II11ii / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 24 - 24: ooo0Oo0 . O00OoOoo00 * iiiI11 % oooOOOOO / i1iIIII
 I1ii1iI1II11ii = 0
 for ( i1i1IiIiIi1Ii , oO0ooOO , IIi1iI1 ) in os . walk ( IIIiIiI ) :
  for file in IIi1iI1 :
   IIi11i1II = os . path . join ( i1i1IiIiIi1Ii , file )
   I1ii1iI1II11ii += os . path . getsize ( IIi11i1II )
 O0OOO0OOoO0O = "[COLOR aqua]Download Folder Size =[COLOR yellow] %0.1f MB[/COLOR]" % ( I1ii1iI1II11ii / ( 1024 * 1024.0 ) )
 O000oo0O ( O0OOO0OOoO0O , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 if 58 - 58: iiI1iIiI - o000o0o00o0Oo % O0 . iiI1iIiI % i1 % IiiIII111ii
 O000oo0O ( "[COLOR white]--------------------------[/COLOR]" , 'url2' , 999 , I1IiI , I1ii11iIi11i )
 O000oo0O ( "[COLOR yellow]Cleanup [COLOR aqua](Will Not Clear Downloads)[/COLOR]" , 'url2' , 892 , I1IiI , I1ii11iIi11i )
 if 87 - 87: i1iII1I1i1i1 - i11iIiiIii
def I11iI ( name , url , iconimage ) :
 if 78 - 78: i11iIiiIii / iIii1I11I1II1 - i1IIi11111i
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
  oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O0OOOOoo . setPath ( oOo )
  xbmc . Player ( ) . play ( oOo , O0O0OOOOoo , False )
  time . sleep ( 2 )
  quit ( )
 else :
  oOo = url
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = I1IiI , thumbnailImage = I1IiI )
  O0O0OOOOoo . setPath ( oOo )
  xbmc . Player ( ) . play ( oOo , O0O0OOOOoo , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Link Dead, Please try another[/COLOR]' , I1IiI , 5000 )
  if 23 - 23: O00OoOoo00
def iIiiIiiIi ( name , url , iconimage ) :
 if 40 - 40: i1IIi11111i
 IIII , oOO = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 IIII += urllib . unquote_plus ( oOO )
 url = regex . resolve ( IIII )
 if 66 - 66: O00OoOoo00 - i1IIi
 PLAYREGEX ( name , url , iconimage )
 if 8 - 8: i1iIIi1 / i1iIIII . iiI1iIiI + o000o0o00o0Oo / i11iIiiIii
def I1Iii1iI1 ( url ) :
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR yellow]Tuning to Frequency Now[/COLOR]' , I1IiI , 10000 )
 time . sleep ( 2 )
 xbmc . Player ( ) . play ( url )
 if 86 - 86: O0
def O0o0oOooOoOo ( heading , text ) :
 if 49 - 49: i1iIIII . o000o0o00o0Oo . i11iIiiIii - i11Ii11I1Ii1i / iiiI11
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 ooOo0O0o0 = xbmcgui . Window ( id )
 o0oo0O = 50
 while ( o0oo0O > 0 ) :
  try :
   xbmc . sleep ( 10 )
   o0oo0O -= 1
   ooOo0O0o0 . getControl ( 1 ) . setLabel ( heading )
   ooOo0O0o0 . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 19 - 19: i1iIIi1 + i1IIi . iiI1iIiI - ooo0Oo0
  if 16 - 16: i1iII1I1i1i1 + IiIi1Iii1I1 / i1IIi11111i
def i11i1 ( url ) :
 try :
  I1iiiiI1iI = urllib2 . Request ( url )
  I1iiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  iIiiiii1i = urllib2 . urlopen ( I1iiiiI1iI , timeout = 5 )
  OOOO = iIiiiii1i . read ( )
  iIiiiii1i . close ( )
  OOOO = OOOO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OOOO
 except : quit ( )
 if 82 - 82: IiiIII111ii * i11iIiiIii % i11Ii11I1Ii1i - OoooooooOO
def i1i ( url ) :
 try :
  I1iiiiI1iI = urllib2 . Request ( url )
  I1iiiiI1iI . add_header ( 'User-Agent' , 'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30' )
  iIiiiii1i = urllib2 . urlopen ( I1iiiiI1iI , timeout = 5 )
  OOOO = iIiiiii1i . read ( )
  iIiiiii1i . close ( )
  OOOO = OOOO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return OOOO
 except : quit ( )
 if 90 - 90: ooo0Oo0 . i1iII1I1i1i1 * i1IIi - i1IIi
def O000oo0O ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IiIiiI11i1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O00Iii1111III111 = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o0OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '887' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) , ( '[COLOR aqua]Download[/COLOR]' , 'xbmc.RunPlugin(' + o0OOO + ')' ) ] )
 if 28 - 28: OoooooooOO . i1iII1I1i1i1 % o000o0o00o0Oo / i1IIi / i1iIIII
 O00Iii1111III111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIiiI11i1Ii , listitem = O0O0OOOOoo , isFolder = False )
 return O00Iii1111III111
 if 36 - 36: i1IIi11111i + O00OoOoo00 - IiiIII111ii + iIii1I11I1II1 + OoooooooOO
def iiII1i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 IiIiiI11i1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O00Iii1111III111 = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 I11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 if 4 - 4: i11Ii11I1Ii1i . O00OoOoo00 + iiiI11 * i1iIIi1 . IiIi1Iii1I1
 O0O0OOOOoo . addContextMenuItems ( [ ( '[COLOR aqua]Add To Nemesis Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I11i + ')' ) ] )
 if 87 - 87: Oooo0000 / i1 / i11iIiiIii
 O00Iii1111III111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIiiI11i1Ii , listitem = O0O0OOOOoo , isFolder = False )
 return O00Iii1111III111
 if 74 - 74: i1iII1I1i1i1 / o000o0o00o0Oo % i1IIi11111i
def OO0o0OO0 ( name , url , iconimage ) :
 Iii1ii1II11i = xbmcgui . Dialog ( )
 OooOo0OOO = [ ]
 I1Io00oOOoO0oO = [ ]
 I11iiIIII1I1 = [ ]
 OOOO = i11i1 ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 oO0Oo = re . compile ( '<link>(.+?)</link>' ) . findall ( OOOOoOoo0O0O0 )
 if len ( oO0Oo ) < 1 :
  oO0Oo = re . compile ( '<lordjd>(.+?)</lordjd>' ) . findall ( OOOOoOoo0O0O0 )
 iiIiI = 1
 for i1IIi1i1Ii1 in oO0Oo :
  Iiio0Oo0oO = i1IIi1i1Ii1
  if '(' in i1IIi1i1Ii1 :
   i1IIi1i1Ii1 = i1IIi1i1Ii1 . split ( '(' ) [ 0 ]
   iI = str ( Iiio0Oo0oO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OooOo0OOO . append ( i1IIi1i1Ii1 )
   I1Io00oOOoO0oO . append ( iI )
  else :
   OooOo0OOO . append ( i1IIi1i1Ii1 )
   I1Io00oOOoO0oO . append ( '[COLOR aqua]Link ' + str ( iiIiI ) + '[/COLOR]' )
  iiIiI = iiIiI + 1
 name = '[COLOR aqua]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 II1iiIi11 = Iii1ii1II11i . select ( name , I1Io00oOOoO0oO )
 if II1iiIi11 < 0 :
  quit ( )
 else :
  url = OooOo0OOO [ II1iiIi11 ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : oOo = liveresolver . resolve ( url )
  else : oOo = url
  O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  O0O0OOOOoo . setPath ( oOo )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O0OOOOoo )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , I1IiI , 5000 )
  time . sleep ( 1 )
  xbmc . Player ( ) . play ( oOo )
  if 84 - 84: i11iIiiIii * i1
def I1I1iII1i ( name , url , iconimage ) :
 if 30 - 30: O0 + o000o0o00o0Oo + i11Ii11I1Ii1i
 III1I = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 OooOo0OOO = [ ]
 I1Io00oOOoO0oO = [ ]
 I11iiIIII1I1 = [ ]
 I1I111iIi = [ ]
 OOOO = i11i1 ( url )
 OOOOoOoo0O0O0 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( OOOO ) [ 0 ]
 oO0Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( OOOOoOoo0O0O0 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( OOOOoOoo0O0O0 ) [ 0 ]
 iiIiI = 1
 if 53 - 53: iIii1I11I1II1 + i1IIi11111i - Oooo0000 - i1iII1I1i1i1 / IiIi1Iii1I1 % i11iIiiIii
 for i1IIi1i1Ii1 in oO0Oo :
  Iiio0Oo0oO = i1IIi1i1Ii1
  if '(' in i1IIi1i1Ii1 :
   i1IIi1i1Ii1 = i1IIi1i1Ii1 . split ( '(' ) [ 0 ]
   iI = str ( Iiio0Oo0oO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   OooOo0OOO . append ( i1IIi1i1Ii1 )
   I1Io00oOOoO0oO . append ( iI )
   I1I111iIi . append ( 'Stream ' + str ( iiIiI ) )
  else :
   OooOo0OOO . append ( i1IIi1i1Ii1 )
   I1Io00oOOoO0oO . append ( 'Link ' + str ( iiIiI ) )
   if 3 - 3: oooOOOOO . IiIi1Iii1I1 % iiI1iIiI + o000o0o00o0Oo
  iiIiI = iiIiI + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 Iii1ii1II11i = xbmcgui . Dialog ( )
 II1iiIi11 = Iii1ii1II11i . select ( name , I1Io00oOOoO0oO )
 if II1iiIi11 < 0 :
  quit ( )
 else :
  OOO00O = I1Io00oOOoO0oO [ II1iiIi11 ]
  OOoOO0oo0ooO = "/"
  if not OOO00O . endswith ( OOoOO0oo0ooO ) :
   O0o0O00Oo0o0 = OOO00O + "/"
  else :
   O0o0O00Oo0o0 = OOO00O
  url = III1I + OooOo0OOO [ II1iiIi11 ] + "%26referer=" + O0o0O00Oo0o0
  print url
  if 64 - 64: i1IIi
  xbmc . Player ( ) . play ( url )
  if 29 - 29: i1IIi11111i / i11iIiiIii / iiI1iIiI % i1iII1I1i1i1 % i11iIiiIii
def ooOOO0 ( string ) :
 i111II = ( c for c in string if 0 < ord ( c ) < 127 )
 if 63 - 63: iiI1iIiI - i1 % oooOOOOO % O00OoOoo00 / i1IIi11111i / i1IIi
 return '' . join ( i111II )
 if 69 - 69: ooo0Oo0 * i11Ii11I1Ii1i * IiIi1Iii1I1 . oooOOOOO - o000o0o00o0Oo
def O00oO ( name , url , mode , iconimage , fanart , description = '' ) :
 if 39 - 39: iiiI11 * iiI1iIiI % i1 . Oooo0000
 if not "http" in iconimage :
  iconimage = I1IiI
 if not "http" in fanart :
  fanart = Oo
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 IiIiiI11i1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O00Iii1111III111 = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 O0O0OOOOoo . setProperty ( "fanart_Image" , fanart )
 O0O0OOOOoo . setProperty ( "icon_Image" , iconimage )
 O0O0OOOOoo . setInfo ( 'video' , { 'Plot' : description } )
 O00Iii1111III111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IiIiiI11i1Ii , listitem = O0O0OOOOoo , isFolder = True )
 return O00Iii1111III111
 if 24 - 24: i1IIi * iIii1I11I1II1 / iiiI11
def OoOOo00 ( name , url , iconimage ) :
 O00Iii1111III111 = True
 O0O0OOOOoo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; O0O0OOOOoo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O00Iii1111III111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = O0O0OOOOoo )
 xbmc . Player ( ) . play ( url , O0O0OOOOoo , False )
 if 53 - 53: IiiIII111ii . i1iIIi1 % iIii1I11I1II1 % Oooo0000 % O00OoOoo00
def o0OoOoOOoOo0o ( ) :
 if 20 - 20: i1 / iIii1I11I1II1
 oo0ooO0 = xbmc . translatePath ( os . path . join ( 'special://home/cache' ) )
 IIiiiiIiIIii = xbmc . translatePath ( os . path . join ( 'special://profile/Thumbnails' ) )
 O0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' ) )
 if 15 - 15: i1iII1I1i1i1 . i1IIi11111i
 iiIiI = [ ( oo0ooO0 , 'Cache' ) , ( IIiiiiIiIIii , 'Thumbnails' ) , ( O0OO , 'Packages' ) ]
 if 21 - 21: iIii1I11I1II1 / i11Ii11I1Ii1i % i1IIi
 IIiI1i = xbmcgui . Dialog ( ) . yesno ( o0OoOoOO00 , '[COLOR aqua]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]' , '' , yeslabel = 'Lets Clean' , nolabel = 'No Thankyou' )
 if IIiI1i :
  iIiiiI . create ( o0OoOoOO00 , '' , '' , '' )
  iIiiiI . update ( 0 )
  for IIII in iiIiI :
   if 6 - 6: o000o0o00o0Oo / oooOOOOO - i1iIIII
   iIiiiI . update ( 50 , "[COLOR aqua]Clearing %s[/COLOR]" % IIII [ 1 ] )
   time . sleep ( 1 )
   if 62 - 62: O00OoOoo00 % i1iIIII
   for OOo00OO00Oo , oO0ooOO , IIi1iI1 in os . walk ( IIII [ 0 ] ) :
    for I11II1i in IIi1iI1 :
     if ( I11II1i . endswith ( '.log' ) ) : continue
     try : os . unlink ( os . path . join ( OOo00OO00Oo , I11II1i ) )
     except : pass
   iIiiiI . update ( 100 , "[COLOR aqua]The %s have been cleared![/COLOR]" % IIII [ 1 ] )
   time . sleep ( 3 )
  iIiiiI . close ( )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Maintenance Completed[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
 else : quit ( )
 if 23 - 23: i1iIIi1 - i1iIIII + iiiI11 - Oooo0000 * Oooo0000 . ooo0Oo0
def iIii11iI1II ( url , mode , name , iconimage , fanart ) :
 if 42 - 42: IiIi1Iii1I1 - iiI1iIiI + o000o0o00o0Oo % iiiI11
 with open ( I11i , "a" ) as i1II1I1Iii1 :
  i1II1I1Iii1 . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]' + name + ' added to favourites[/COLOR]' , I1IiI , 5000 )
  if 44 - 44: i1IIi - O0 - o000o0o00o0Oo * o000o0o00o0Oo + Oooo0000
def O0oo ( ) :
 if 82 - 82: Oooo0000 + O0 - IiiIII111ii % i1iII1I1i1i1 * i11iIiiIii
 with open ( I11i , "a" ) as i1II1I1Iii1 :
  iIIi1iI1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  I1Iii1I = open ( iIIi1iI1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( I1Iii1I )
  O000oo0O ( '[COLOR aqua]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  O000oo0O ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  if len ( IIIii1II1II ) < 1 :
   O000oo0O ( '[COLOR skyblue]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  for iIi11I in IIIii1II1II :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( iIi11I ) [ 0 ]
   iiiiiIIii = re . compile ( '<url>(.+?)</url>' ) . findall ( iIi11I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIi11I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIi11I ) [ 0 ]
   O000oo0O ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 2 , I1IiI , I1ii11iIi11i )
   if 87 - 87: O00OoOoo00 / iiI1iIiI + ooo0Oo0 + i1iIIII - OoooooooOO + ooo0Oo0
 O000oo0O ( '[COLOR aqua]' + "Delete Favourites" + '[/COLOR]' , 'url' , 891 , o0O , Oo )
 if 93 - 93: IiIi1Iii1I1 . iIii1I11I1II1 % i11iIiiIii . Oooo0000 % IiIi1Iii1I1 + O0
def o0OOoOO ( ) :
 if 46 - 46: i1iII1I1i1i1 / oooOOOOO - i1IIi
 with open ( IiII , "a" ) as i1II1I1Iii1 :
  iIIi1iI1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'download.xml' ) )
  I1Iii1I = open ( iIIi1iI1 ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIii1II1II = re . compile ( '<item>(.+?)</item>' ) . findall ( I1Iii1I )
  O000oo0O ( '[COLOR aqua]' + "Your Downloads" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  O000oo0O ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  if len ( IIIii1II1II ) < 1 :
   O000oo0O ( '[COLOR skyblue]' + "NO DOWNLOADS YET" + '[/COLOR]' , 'url' , '2' , o0O , Oo )
  for iIi11I in IIIii1II1II :
   III1iII1I1ii = re . compile ( '<title>(.+?)</title>' ) . findall ( iIi11I ) [ 0 ]
   iiiiiIIii = re . compile ( '<link>(.+?)</link>' ) . findall ( iIi11I ) [ 0 ]
   I1IiI = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( iIi11I ) [ 0 ]
   I1ii11iIi11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( iIi11I ) [ 0 ]
   O000oo0O ( '[COLOR skyblue]' + III1iII1I1ii + '[/COLOR]' , iiiiiIIii , 2 , I1IiI , I1ii11iIi11i )
   if 51 - 51: ooo0Oo0 - o000o0o00o0Oo * O00OoOoo00
 O000oo0O ( '[COLOR aqua]' + "Clear Downloads Folder" + '[/COLOR]' , 'url' , 885 , o0O , Oo )
 if 12 - 12: iIii1I11I1II1 % IiIi1Iii1I1 % IiIi1Iii1I1
def o0i1iI1iiI1I ( ) :
 if 52 - 52: i1 % iiiI11 * i11Ii11I1Ii1i
 with open ( I11i , "w" ) as i1II1I1Iii1 :
  i1II1I1Iii1 . write ( '' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Favourites has been wiped[/COLOR]' , I1IiI , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 4 - 4: O00OoOoo00 % O0 - OoooooooOO + IiIi1Iii1I1 . i1iII1I1i1i1 % i11Ii11I1Ii1i
def Iiii1iiiIiI1 ( ) :
 shutil . rmtree ( o0OOO )
 os . mkdir ( o0OOO )
 with open ( IiII , "w" ) as i1II1I1Iii1 :
  i1II1I1Iii1 . write ( '' )
 Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Downloads Folder Cleared[/COLOR]' , I1IiI , 5000 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 27 - 27: iiiI11 + iiI1iIiI * iIii1I11I1II1 . OoooooooOO * Oooo0000
 if 100 - 100: i1 / i1IIi - iiI1iIiI % iiiI11 - iIii1I11I1II1
 if 17 - 17: O00OoOoo00 / i1IIi11111i % ooo0Oo0
def OOO00 ( ) :
 if 71 - 71: IiiIII111ii . i1iIIi1 . i1
 Oo0O0O00Oo = open ( iI1Ii11111iIi ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I111Ii = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Oo0O0O00Oo ) [ 0 ]
  if I111Ii == 'EXPIRED' :
   Iii1ii1II11i . ok ( o0OoOoOO00 , "[COLOR aqua]Please visit [COLOR yellow]http://streamarmy.co.uk[COLOR aqua] to generate a Pin to access Nemesis Addon then enter it after clicking ok, This takes less than a minute and helps pay for servers!!\n[COLOR red]This is only required once every 4 hours[/COLOR]" )
   iiiI = ''
   I1ii1 = xbmc . Keyboard ( iiiI , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   I1ii1 . doModal ( )
   if I1ii1 . isConfirmed ( ) :
    iiiI = I1ii1 . getText ( )
    if len ( iiiI ) > 1 :
     O00 = iiiI . title ( )
     with open ( iI1Ii11111iIi , "w" ) as I11II1i :
      I11II1i . write ( "<pin>" + O00 + "</pin>" )
     OOO00 ( )
    else : quit ( )
   else : quit ( )
  if not 'EXPIRED' in I111Ii :
   II11 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Oo0O0O00Oo ) [ 0 ]
   iIiii = ( 'http://www.streamarmy.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % II11 )
   OOOO = i11i1 ( iIiii )
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
  if 94 - 94: IiIi1Iii1I1 * O00OoOoo00 - IiiIII111ii . iIii1I11I1II1
  if 66 - 66: IiIi1Iii1I1 - i1iIIII * Oooo0000 / i1iII1I1i1i1 * i11Ii11I1Ii1i * i1
  if 91 - 91: OoooooooOO / iiiI11 . iiI1iIiI + IiIi1Iii1I1 . i11Ii11I1Ii1i
  if 45 - 45: i1iII1I1i1i1 * Oooo0000 / iIii1I11I1II1
def o00ooOoO0 ( url , iconimage , fanart ) :
 if 15 - 15: i1iIIII * O00OoOoo00 / o000o0o00o0Oo * i1IIi11111i
 try :
  iiiI = ''
  I1ii1 = xbmc . Keyboard ( iiiI , 'Enter Name To Save File As' )
  I1ii1 . doModal ( )
  if I1ii1 . isConfirmed ( ) :
   iiiI = I1ii1 . getText ( )
   if len ( iiiI ) > 1 :
    O00 = iiiI . title ( )
   else : quit ( )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   oOo = urlresolver . HostedMediaFile ( url ) . resolve ( )
   url = oOo
  o000Oo0 = url . split ( '/' ) [ - 1 ]
  IiIiiI11i1Ii = urllib2 . urlopen ( url )
  o0O0OO0o = os . path . join ( o0OOO , O00 )
  I11II1i = open ( o0O0OO0o , 'wb' )
  if 54 - 54: Oooo0000 . i1iII1I1i1i1 % i11iIiiIii / OoooooooOO + IiiIII111ii % i1iII1I1i1i1
  i1ii1IIiI = IiIiiI11i1Ii . info ( )
  II1ii1ii11I1 = int ( i1ii1IIiI . getheaders ( "Content-Length" ) [ 0 ] )
  iIiiiI . create ( o0OoOoOO00 , "Starting Download: %s File Size: %s" % ( O00 , II1ii1ii11I1 ) )
  iIiiiI . update ( 0 )
  time . sleep ( 2 )
  if 88 - 88: o000o0o00o0Oo
  oOOooooo0OoO0 = 0
  ii1I111i1Ii = 8192
  while True :
   buffer = IiIiiI11i1Ii . read ( ii1I111i1Ii )
   if not buffer :
    break
    if 84 - 84: o000o0o00o0Oo % iIii1I11I1II1 + i1 . o000o0o00o0Oo % i1
   oOOooooo0OoO0 += len ( buffer )
   I11II1i . write ( buffer )
   o0OooooO0O = "[%3.2f%%]" % ( oOOooooo0OoO0 * 100. / II1ii1ii11I1 )
   o0OooooO0O = o0OooooO0O + chr ( 8 ) * ( len ( o0OooooO0O ) + 1 )
   iIiiiI . update ( oOOooooo0OoO0 , "[COLOR aqua]Downloaded [COLOR yellow]%s[/COLOR][COLOR aqua] Of %s[/COLOR]" % ( o0OooooO0O , O00 ) )
   if 81 - 81: i1IIi % i1IIi11111i - i1iIIi1 + i11iIiiIii - OoooooooOO
   if iIiiiI . iscanceled ( ) :
    iIiiiI . close ( )
    quit ( )
  with open ( IiII , "a" ) as i1II1I1Iii1 :
   i1II1I1Iii1 . write ( '<item>\n<title>' + O00 + '</title>\n<link>' + o0O0OO0o + '</link>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Download Complete[/COLOR]' , I1IiI , 5000 )
  if 50 - 50: iiiI11 - i11iIiiIii + iIii1I11I1II1 / O0 - iiiI11 + i1IIi11111i
  I11II1i . close ( )
 except :
  Iii1ii1II11i . notification ( o0OoOoOO00 , '[COLOR skyblue]Sorry This File Couldn\'t Be Downloaded[/COLOR]' , I1IiI , 5000 )
  if 22 - 22: i11Ii11I1Ii1i - iiiI11 / IiIi1Iii1I1 % OoooooooOO + i1iIIII
  if 5 - 5: i1 / oooOOOOO + i11iIiiIii % O00OoOoo00
  if 93 - 93: Oooo0000 % iIii1I11I1II1
  if 90 - 90: iiI1iIiI - i1iIIII / iiiI11 / O0 / O00OoOoo00
def oOO0 ( ) :
 IIi1I1i = [ ]
 Ii = sys . argv [ 2 ]
 if len ( Ii ) >= 2 :
  oO0O = sys . argv [ 2 ]
  Oo00o0O0O = oO0O . replace ( '?' , '' )
  if ( oO0O [ len ( oO0O ) - 1 ] == '/' ) :
   oO0O = oO0O [ 0 : len ( oO0O ) - 2 ]
  o0ooO0OoOo = Oo00o0O0O . split ( '&' )
  IIi1I1i = { }
  for iiIiI in range ( len ( o0ooO0OoOo ) ) :
   o0oOO00 = { }
   o0oOO00 = o0ooO0OoOo [ iiIiI ] . split ( '=' )
   if ( len ( o0oOO00 ) ) == 2 :
    IIi1I1i [ o0oOO00 [ 0 ] ] = o0oOO00 [ 1 ]
 return IIi1I1i
 if 46 - 46: i11iIiiIii - O00OoOoo00
oO0O = oOO0 ( ) ; iiiiiIIii = None ; oo0OooOOo0 = None ; oOoOo = None ; OoO00O0OOO = None ; o0O = None ; oooOo0O00o00 = None
try : OoO00O0OOO = urllib . unquote_plus ( oO0O [ "site" ] )
except : pass
try : iiiiiIIii = urllib . unquote_plus ( oO0O [ "url" ] )
except : pass
try : oo0OooOOo0 = urllib . unquote_plus ( oO0O [ "name" ] )
except : pass
try : oOoOo = int ( oO0O [ "mode" ] )
except : pass
try : o0O = urllib . unquote_plus ( oO0O [ "iconimage" ] )
except : pass
try : I1ii11iIi11i = urllib . unquote_plus ( oO0O [ "fanart" ] )
except : pass
try : oooOo0O00o00 = urllib . unquote_plus ( oO0O [ "description" ] )
except : pass
if 6 - 6: IiiIII111ii % ooo0Oo0 . ooo0Oo0 - o000o0o00o0Oo / O00OoOoo00 . i1IIi
if oOoOo == None or iiiiiIIii == None or len ( iiiiiIIii ) < 1 : I1I ( )
if 99 - 99: Oooo0000 . i1iIIi1
if 59 - 59: O00OoOoo00 / ooo0Oo0 / i1iIIII / O0 / Oooo0000 + i1IIi11111i
if 13 - 13: i1IIi11111i % i1iII1I1i1i1 / i1iIIi1 % i1iIIi1 % O0
if 90 - 90: IiiIII111ii . IiIi1Iii1I1 / iIii1I11I1II1
if 28 - 28: IiiIII111ii + i1iII1I1i1i1 - IiIi1Iii1I1 / iIii1I11I1II1 - iiI1iIiI
elif oOoOo == 1 : oOOOOo0 ( oo0OooOOo0 , iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 2 : I11iI ( oo0OooOOo0 , iiiiiIIii , o0O )
elif oOoOo == 3 : OO0o0OO0 ( oo0OooOOo0 , iiiiiIIii , o0O )
if 45 - 45: O0 / i1IIi * i1iII1I1i1i1 * i1
if 35 - 35: o000o0o00o0Oo / oooOOOOO % iiI1iIiI + iIii1I11I1II1
if 79 - 79: Oooo0000 / IiIi1Iii1I1
elif oOoOo == 4 : Iiii ( iiiiiIIii )
elif oOoOo == 5 : O0OOO ( iiiiiIIii )
elif oOoOo == 6 : oOo0O0Oo00oO ( )
elif oOoOo == 7 : O00o0OO0 ( iiiiiIIii )
elif oOoOo == 8 : O0oO ( iiiiiIIii )
elif oOoOo == 9 : OOOOo0 ( iiiiiIIii )
elif oOoOo == 10 : I1Iii1iI1 ( iiiiiIIii )
elif oOoOo == 11 : SCANNER ( )
elif oOoOo == 12 : SCANNER_STATE ( iiiiiIIii )
elif oOoOo == 13 : SCANNER_CITY ( iiiiiIIii )
elif oOoOo == 14 : SCANNER_PLAY ( iiiiiIIii )
elif oOoOo == 15 : SCANNER_TOP25 ( )
elif oOoOo == 16 : I1I1iII1i ( oo0OooOOo0 , iiiiiIIii , o0O )
elif oOoOo == 17 : ooOOoooooo ( iiiiiIIii )
elif oOoOo == 18 : IIi1 ( iiiiiIIii )
elif oOoOo == 19 : Ooo00o0Oooo ( iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 20 : oOo0oO ( )
elif oOoOo == 21 : OO ( iiiiiIIii )
elif oOoOo == 22 : OoooO00o ( iiiiiIIii )
elif oOoOo == 23 : oOoOOo0O ( )
elif oOoOo == 24 : oOOoo0000O0o0 ( iiiiiIIii )
elif oOoOo == 25 : I1 ( iiiiiIIii , o0O )
elif oOoOo == 26 : ii ( iiiiiIIii )
elif oOoOo == 27 : O0O0Oo00 ( iiiiiIIii , o0O )
elif oOoOo == 28 : ii1iIi1iIiI1i ( )
elif oOoOo == 29 : ii1III11 ( iiiiiIIii )
elif oOoOo == 30 : ooO0o ( iiiiiIIii )
elif oOoOo == 31 : o0O0O0ooo0oOO ( iiiiiIIii )
elif oOoOo == 32 : Iiiiii111i1ii ( iiiiiIIii )
elif oOoOo == 33 : Ooo00O0o ( iiiiiIIii )
elif oOoOo == 34 : i1iIi1I1i ( iiiiiIIii )
elif oOoOo == 35 : oO0 ( )
elif oOoOo == 36 : O0oo0ooOOOO ( iiiiiIIii )
elif oOoOo == 37 : Iiii1I1 ( iiiiiIIii , o0O )
elif oOoOo == 38 : i1I1II1iIIi11 ( )
elif oOoOo == 39 : o0o0oOoOO0O ( iiiiiIIii )
elif oOoOo == 40 : oOo0oO ( )
elif oOoOo == 41 : OO ( iiiiiIIii )
elif oOoOo == 42 : iiOOOO0o ( iiiiiIIii )
elif oOoOo == 43 : o0o000 ( iiiiiIIii , o0O )
elif oOoOo == 44 : OOooo00 ( )
if 77 - 77: ooo0Oo0
elif oOoOo == 45 : OOoO000 ( )
elif oOoOo == 46 : oooO0o0o0O0 ( iiiiiIIii )
elif oOoOo == 47 : IIiiIIi1 ( oo0OooOOo0 , iiiiiIIii , o0O )
elif oOoOo == 48 : O000 ( )
elif oOoOo == 49 : oo0o0O0Oooooo ( iiiiiIIii )
elif oOoOo == 50 : Ooo0oo0ooO ( iiiiiIIii )
elif oOoOo == 51 : ANIME_CATS ( )
elif oOoOo == 52 : ANIME_SHOWS ( iiiiiIIii )
elif oOoOo == 53 : ANIME_EPI ( iiiiiIIii )
elif oOoOo == 54 : ANIME_PLAY ( iiiiiIIii , o0O )
if 46 - 46: i1iIIi1
if 72 - 72: oooOOOOO * i1iIIII
if 67 - 67: i1IIi
elif oOoOo == 59 : iIi11iiIiI1I ( )
elif oOoOo == 60 : O0OOO0OOooo00 ( iiiiiIIii )
elif oOoOo == 61 : o00 ( oo0OooOOo0 , iiiiiIIii , o0O )
if 5 - 5: i11Ii11I1Ii1i . OoooooooOO
elif oOoOo == 66 : ii1IIIIiI11 ( )
elif oOoOo == 67 : O00oooo00o0O ( iiiiiIIii )
elif oOoOo == 68 : IIi11IIiIii1 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 69 : Ii111 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 70 : II1i1i1iII1 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 71 : O0OO0oOoO0O0O ( )
elif oOoOo == 72 : iIiIi11Ii ( )
elif oOoOo == 73 : I1i ( )
elif oOoOo == 74 : IiIIi1I1I11Ii ( iiiiiIIii )
elif oOoOo == 75 : Ooo0O0 ( iiiiiIIii )
if 57 - 57: iiI1iIiI
if 35 - 35: OoooooooOO - i1iIIi1 / i1
elif oOoOo == 884 : o00oo0000 ( )
elif oOoOo == 885 : Iiii1iiiIiI1 ( )
elif oOoOo == 886 : o0OOoOO ( )
elif oOoOo == 887 : o00ooOoO0 ( iiiiiIIii , o0O , I1ii11iIi11i )
elif oOoOo == 888 : i1Iii11Ii1i1 ( )
elif oOoOo == 889 : iIii11iI1II ( iiiiiIIii , oOoOo , oo0OooOOo0 , o0O , I1ii11iIi11i )
elif oOoOo == 890 : O0oo ( )
elif oOoOo == 891 : o0i1iI1iiI1I ( )
elif oOoOo == 892 : o0OoOoOOoOo0o ( )
if 50 - 50: Oooo0000
if oOoOo == None or iiiiiIIii == None or len ( iiiiiIIii ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 33 - 33: O00OoOoo00
if 98 - 98: Oooo0000 % i11Ii11I1Ii1i
if 95 - 95: iIii1I11I1II1 - i1iIIi1 - i1iIIII + i1iIIi1 % o000o0o00o0Oo . iiI1iIiI
if 41 - 41: O0 + i1iII1I1i1i1 . i1IIi - i11Ii11I1Ii1i * i1IIi11111i . i1
if 68 - 68: i1IIi11111i
if 20 - 20: i1iIIi1 - i1iIIi1
if 37 - 37: IiiIII111ii
if 37 - 37: ooo0Oo0 / IiiIII111ii * O0
if 73 - 73: oooOOOOO * oooOOOOO / IiIi1Iii1I1
if 43 - 43: o000o0o00o0Oo . i1IIi . IiiIII111ii + O0 * iiiI11 * O0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
