#########################################
############CODE BY @NEMZZY668###########
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , base64 , time
from resources . libs . common_addon import Addon
import requests
import resolveurl
from metahandler import metahandlers
from HTMLParser import HTMLParser
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.entertainmenttime'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = o0OO00 )
iIiiiI1IiI1I1 = '[COLOR yellow][B]E[COLOR aqua]ntertainment Time[/B][/COLOR]'
o0OoOoOO00 = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.entertainmenttime' )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.entertainmenttime/downloads/' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'settings.xml' ) )
iIiiiI = xbmcgui . DialogProgress ( )
Iii1ii1II11i = xbmcgui . Dialog ( )
if 10 - 10: I1iII1iiII + I1Ii111 / OOo
if 41 - 41: I1II1
Ooo0OO0oOO = 'https://putlockermovies.to/putlocker/'
if 86 - 86: oO0o
if 12 - 12: OOO0o0o / o0oO0 + i111I * O0Oo0oO0o . II1iI . i1iIii1Ii1II
if 1 - 1: O0Oooo00
if 87 - 87: i1IIi11111i / I11i1i11i1I % ooIiII1I1i1i1ii / II1iI + i111I / OOO0o0o
def I1i1I ( ) :
 if 72 - 72: OOo % O0Oo0oO0o . I1Ii111 / II1iI * I1Ii111
 if not os . path . exists ( os . path . dirname ( I1IiI ) ) :
  try :
   os . makedirs ( os . path . dirname ( I1IiI ) )
   with open ( o0OOO , "w" ) as iiiI11 :
    iiiI11 . write ( "<date>000</date>" )
  except OSError as OOooO :
   if OOooO . errno != errno . EEXIST :
    raise
    if 58 - 58: I1II1 + oO0o / i1iIii1Ii1II * OoooooooOO
def II111iiii ( ) :
 if 48 - 48: I1II1 . OoooooooOO - oO0o % O0Oo0oO0o / i1iIii1Ii1II . i1iIii1Ii1II
 i1Ii ( "[COLOR lime]Search[/COLOR]" , 'null' , 15 , Oo , O0O , 'Search For Content' )
 i1Ii ( "[COLOR yellow]M[COLOR aqua]ovies[/COLOR]" , 'https://putlockermovies.to/movies/page/1' , 14 , Oo , O0O , 'Movies' )
 i1Ii ( "[COLOR yellow]T[COLOR aqua]v Shows[/COLOR]" , 'https://putlockermovies.to/series/page/1' , 14 , Oo , O0O , 'Tv Shows' )
 i1Ii ( "[COLOR yellow]L[COLOR aqua]atest Episodes[/COLOR]" , 'https://putlockermovies.to/episode/page/1' , 14 , Oo , O0O , 'Latest Episodes' )
 i1Ii ( "[COLOR yellow]G[COLOR aqua]enres[/COLOR]" , 'noop' , 10 , Oo , O0O , 'Movies and Tv Shows Sorted By Genre' )
 i1Ii ( "[COLOR yellow]F[COLOR aqua]eatured Movies[/COLOR]" , 'https://putlockermovies.to/genre/featured/page/1' , 14 , Oo , O0O , 'Featured Movies' )
 i1Ii ( "[COLOR yellow]T[COLOR aqua]op IMDB Movies[/COLOR]" , 'https://putlockermovies.to/top-imdb/page/1' , 14 , Oo , O0O , 'Movies Sorted By IMDB Rating' )
 if 25 - 25: O0Oooo00 + ooIiII1I1i1i1ii % ooIiII1I1i1i1ii - i111I * OOO0o0o % O0Oooo00
def OOooO0OOoo ( ) :
 if 29 - 29: OOO0o0o / iIii1I11I1II1
 IiIIIiI1I1 = ''
 OoO000 = xbmc . Keyboard ( IiIIIiI1I1 , 'Enter Search Term' )
 OoO000 . doModal ( )
 if OoO000 . isConfirmed ( ) :
  IiIIIiI1I1 = OoO000 . getText ( )
  if len ( IiIIIiI1I1 ) > 1 :
   IIiiIiI1 = IiIIIiI1I1 . lower ( )
  else :
   Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , iiIiIIi , 5000 )
   quit ( )
 else :
  Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , "[COLOR aqua]Sorry, No Search Term Was Entered![/COLOR]" , iiIiIIi , 5000 )
  quit ( )
 IIiiIiI1 = IIiiIiI1 . replace ( ' ' , '+' )
 ooOoo0O = 'https://putlockermovies.to/?s=' + IIiiIiI1
 OooO0 ( ooOoo0O )
 if 35 - 35: O0Oo0oO0o % I11i1i11i1I % i11iIiiIii / OoooooooOO
def Ii11iI1i ( ) :
 if 82 - 82: i11iIiiIii . O0Oo0oO0o / OOo * O0 % i111I % iIii1I11I1II1
 Oo00OOOOO = O0OO00o0OO ( Ooo0OO0oOO )
 I11i1 = re . compile ( '''<ul class='sub-menu'>(.*?)</div>''' ) . findall ( Oo00OOOOO ) [ 0 ]
 iIi1ii1I1 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( I11i1 )
 for ooOoo0O , o0 in iIi1ii1I1 :
  if not 'https' in ooOoo0O :
   ooOoo0O = 'https://putlockermovies.to' + ooOoo0O
  i1Ii ( "[COLOR yellow]" + o0 + "[/COLOR]" , ooOoo0O , 11 , Oo , O0O , o0 + ' Genre' )
  if 9 - 9: i1iIii1Ii1II + i111I % i1iIii1Ii1II + i1IIi . O0Oo0oO0o
def OooO0 ( url ) :
 if 31 - 31: OOO0o0o + II1iI + II1iI / I1iII1iiII
 Oo00OOOOO = O0OO00o0OO ( url )
 I11i1 = re . compile ( '''class="ml-item">(.*?)</a>''' ) . findall ( Oo00OOOOO )
 for iIi1ii1I1 in I11i1 :
  iiI1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ]
  iiI1 = i11Iiii ( iiI1 )
  url = re . compile ( '<a href="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ] . strip ( )
  if '/series/' in url :
   i1Ii ( "[COLOR yellow]" + iiI1 + "[/COLOR]" , url , 12 , Oo , O0O , iiI1 )
  else :
   i1Ii ( "[COLOR yellow]" + iiI1 + "[/COLOR]" , url , 4 , Oo , O0O , iiI1 )
   if 23 - 23: OOO0o0o . I1iII1iiII
def Oo0O0OOOoo ( url , iconimage ) :
 if 95 - 95: I1II1 % i111I . O0
 Oo00OOOOO = O0OO00o0OO ( url )
 I11i1 = re . compile ( '<div class="les-title">(.*?)</ul>' ) . findall ( Oo00OOOOO )
 I1i1IoOO00oOO = 0
 for iIi1ii1I1 in I11i1 :
  I1i1IoOO00oOO += 1
  OoOo = re . compile ( '''<strong>(.*?)</strong>''' ) . findall ( iIi1ii1I1 ) [ 0 ]
  iI = 'season-' + str ( I1i1IoOO00oOO ) + '-'
  i1Ii ( "[COLOR yellow]" + OoOo + "[/COLOR]" , url + ':::' + iI , 13 , iconimage , O0O , OoOo )
  if 60 - 60: II1iI / II1iI
def I1II1III11iii ( url , iconimage ) :
 if 75 - 75: iIii1I11I1II1 / O0Oo0oO0o % OOO0o0o * oO0o
 if 9 - 9: I1II1
 i11 = url . split ( ':::' ) [ 1 ]
 url = url . split ( ':::' ) [ 0 ]
 Oo00OOOOO = O0OO00o0OO ( url )
 I11i1 = re . compile ( '<div class="les-title">(.*?)</ul>' ) . findall ( Oo00OOOOO )
 O0oo0OO0oOOOo = [ ]
 i1i1i11IIi = [ ]
 II1III = [ ]
 for iIi1ii1I1 in I11i1 :
  iiI1 = re . compile ( '''<a href=".*?">(.*?)</a>''' ) . findall ( iIi1ii1I1 )
  for o0 in iiI1 :
   i1i1i11IIi . append ( o0 )
  url = re . compile ( '''<a href="(.*?)"''' ) . findall ( iIi1ii1I1 )
  for iI1iI1I1i1I in url :
   O0oo0OO0oOOOo . append ( iI1iI1I1i1I )
  II1III = list ( zip ( i1i1i11IIi , O0oo0OO0oOOOo ) )
 for iIi11Ii1 , Oo00OOOOO in II1III :
  if i11 in Oo00OOOOO :
   Ii11iII1 ( "[COLOR yellow]" + iIi11Ii1 + "[/COLOR]" , Oo00OOOOO , 4 , iconimage , O0O , iIi11Ii1 )
   if 51 - 51: I1iII1iiII * I1II1 % OOO0o0o * I1iII1iiII % o0oO0 / ooIiII1I1i1i1ii
def iIIIIii1 ( url ) :
 if 58 - 58: i11iIiiIii % II1iI
 Oo00OOOOO = O0OO00o0OO ( url )
 I11i1 = re . compile ( '''class="ml-item">(.*?)</a>''' ) . findall ( Oo00OOOOO )
 for iIi1ii1I1 in I11i1 :
  iiI1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ]
  iiI1 = i11Iiii ( iiI1 )
  OO00Oo = re . compile ( '<a href="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( iIi1ii1I1 ) [ 0 ] . strip ( )
  if '/series/' in url :
   i1Ii ( "[COLOR yellow]" + iiI1 + "[/COLOR]" , OO00Oo , 12 , Oo , O0O , iiI1 )
  else :
   Ii11iII1 ( "[COLOR yellow]" + iiI1 + "[/COLOR]" , OO00Oo , 4 , Oo , O0O , iiI1 )
 try :
  O0OOO0OOoO0O = url . split ( 'page/' ) [ 1 ]
  O00Oo000ooO0 = url . split ( 'page/' ) [ 0 ]
  OoO0O00 = int ( O0OOO0OOoO0O ) + 1
  IIiII = O00Oo000ooO0 + 'page/' + str ( OoO0O00 )
  i1Ii ( "[COLOR aqua]Next Page --->[/COLOR]" , IIiII , 14 , iiIiIIi , O0O , iiI1 )
 except : pass
 if 80 - 80: i1IIi11111i . i111I
 if 25 - 25: oO0o . I1iII1iiII / O0Oooo00 . O0Oo0oO0o * I1II1 . I1Ii111
def Oo0oOOo ( url ) :
 if 58 - 58: I1iII1iiII * O0Oo0oO0o * o0oO0 / O0Oo0oO0o
 Oo00OOOOO = O0OO00o0OO ( url )
 oO0o0OOOO = re . compile ( '<iframe src="(.*?)"' ) . findall ( Oo00OOOOO ) [ 0 ]
 O0O0OoOO0 ( o0 , oO0o0OOOO , iiIiIIi )
 if 10 - 10: OoooooooOO % iIii1I11I1II1
def O0OO00o0OO ( url ) :
 try :
  O00o0O00 = urllib2 . Request ( url )
  O00o0O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  ii111111I1iII = urllib2 . urlopen ( O00o0O00 , timeout = 5 )
  Oo00OOOOO = ii111111I1iII . read ( )
  ii111111I1iII . close ( )
  Oo00OOOOO = Oo00OOOOO . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return Oo00OOOOO
 except : quit ( )
 if 68 - 68: O0Oooo00 - iIii1I11I1II1 * i11iIiiIii / o0oO0 * I11i1i11i1I
def i1Ii ( name , url , mode , iconimage , fanart , description = '' ) :
 if 23 - 23: O0Oooo00
 if not iconimage :
  iconimage = Oo
 if not fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 oo0oOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 o000O0o = True
 iI1iII1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 iI1iII1 . setProperty ( "fanart_Image" , fanart )
 iI1iII1 . setProperty ( "icon_Image" , iconimage )
 iI1iII1 . setInfo ( 'video' , { 'Plot' : description } )
 o000O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0oOo , listitem = iI1iII1 , isFolder = True )
 oO0OOoo0OO = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return o000O0o
 if 65 - 65: i1iIii1Ii1II . iIii1I11I1II1 / O0 - i1iIii1Ii1II
def Ii11iII1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 21 - 21: I1Ii111 * iIii1I11I1II1
 if not iconimage :
  iconimage = Oo
 if not fanart :
  fanart = I11i
 oo0oOo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o000O0o = True
 iI1iII1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iI1iII1 . setProperty ( "fanart_Image" , fanart )
 iI1iII1 . setProperty ( "icon_Image" , iconimage )
 iI1iII1 . setInfo ( 'video' , { 'Plot' : description } )
 oooooOoo0ooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1iII1 . addContextMenuItems ( [ ( '[COLOR pink]Add To Bishop Favourites[/COLOR]' , 'xbmc.RunPlugin(' + oooooOoo0ooo + ')' ) ] )
 oO0OOoo0OO = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 o000O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0oOo , listitem = iI1iII1 , isFolder = False )
 return o000O0o
 if 6 - 6: II1iI - i1iIii1Ii1II + iIii1I11I1II1 - I11i1i11i1I - i11iIiiIii
def O0O0OoOO0 ( name , url , iconimage ) :
 if 79 - 79: oO0o - O0 * I1II1 + oO0o % O0 * O0
 Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Lets Grab That Link[/COLOR]' , Oo , 4000 )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  oOOo0 = resolveurl . HostedMediaFile ( url ) . resolve ( )
  iI1iII1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  iI1iII1 . setPath ( oOOo0 )
  xbmc . Player ( ) . play ( oOOo0 , iI1iII1 , False )
  if 54 - 54: O0 - i1IIi11111i % O0Oo0oO0o
 else :
  oOOo0 = url
  iI1iII1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  iI1iII1 . setPath ( oOOo0 )
  xbmc . Player ( ) . play ( oOOo0 , iI1iII1 , False )
  if 77 - 77: oO0o / I1Ii111 / I1II1 + I1II1 . O0Oo0oO0o
 time . sleep ( 6 )
 if xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Enjoy Your Content[/COLOR]' , Oo , 4000 )
  quit ( )
 else :
  xbmc . executebuiltin ( "Dialog.Close(all)" )
  Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Damn Seems That Link Down At The Moment[/COLOR]' , Oo , 4000 )
  quit ( )
  if 38 - 38: I11i1i11i1I
def Ii1 ( ) :
 if 82 - 82: o0oO0 - iIii1I11I1II1 / O0Oo0oO0o + i1iIii1Ii1II
 if 87 - 87: i111I * o0oO0 + O0Oo0oO0o / iIii1I11I1II1 / O0Oooo00
 I1111IIi = open ( o0OOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  Oo0oO = re . compile ( '<pin>(.+?)</pin>' ) . findall ( I1111IIi ) [ 0 ]
  if Oo0oO == 'EXPIRED' :
   Iii1ii1II11i . ok ( iIiiiI1IiI1I1 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Entertainment Time then enter it after clicking ok[/COLOR]" )
   IiIIIiI1I1 = ''
   OoO000 = xbmc . Keyboard ( IiIIIiI1I1 , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   OoO000 . doModal ( )
   if OoO000 . isConfirmed ( ) :
    IiIIIiI1I1 = OoO000 . getText ( )
    if len ( IiIIIiI1I1 ) > 1 :
     IIiiIiI1 = IiIIIiI1I1 . title ( )
     with open ( o0OOO , "w" ) as iiiI11 :
      iiiI11 . write ( "<pin>" + IIiiIiI1 + "</pin>" )
     Ii1 ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in Oo0oO :
   IIiIi1iI = re . compile ( '<pin>(.+?)</pin>' ) . findall ( I1111IIi ) [ 0 ]
   i1IiiiI1iI = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % IIiIi1iI )
   Oo00OOOOO = O0OO00o0OO ( i1IiiiI1iI )
   if len ( Oo00OOOOO ) < 1 or 'Pin Expired' in Oo00OOOOO :
    with open ( o0OOO , "w" ) as iiiI11 :
     iiiI11 . write ( '<pin>EXPIRED</pin>' )
    Ii1 ( )
   else :
    global baseurl
    baseurl = Oo00OOOOO
 except IndexError :
  with open ( o0OOO , "w" ) as iiiI11 :
   iiiI11 . write ( "<pin>EXPIRED</pin>\n" )
  Ii1 ( )
  if 49 - 49: i1iIii1Ii1II / I1II1 . I1iII1iiII
def ooOOoooooo ( string ) :
 if 1 - 1: OOo / OOO0o0o % O0Oooo00 * i1IIi11111i . i11iIiiIii
 III1Iiii1I11 = ( c for c in string if 0 < ord ( c ) < 127 )
 return '' . join ( III1Iiii1I11 )
 if 9 - 9: o0oO0 / OOo - I1Ii111 / OoooooooOO / iIii1I11I1II1 - OOO0o0o
def o00oooO0Oo ( ) :
 if 78 - 78: i1iIii1Ii1II % I11i1i11i1I + o0oO0
 OOooOoooOoOo = xbmc . getInfoLabel ( "System.BuildVersion" )
 o0OOOO00O0Oo = float ( OOooOoooOoOo [ : 4 ] )
 if o0OOOO00O0Oo >= 11.0 and o0OOOO00O0Oo <= 11.9 :
  ii = 'Eden'
 elif o0OOOO00O0Oo >= 12.0 and o0OOOO00O0Oo <= 12.9 :
  ii = 'Frodo'
 elif o0OOOO00O0Oo >= 13.0 and o0OOOO00O0Oo <= 13.9 :
  ii = 'Gotham'
 elif o0OOOO00O0Oo >= 14.0 and o0OOOO00O0Oo <= 14.9 :
  ii = 'Helix'
 elif o0OOOO00O0Oo >= 15.0 and o0OOOO00O0Oo <= 15.9 :
  ii = 'Isengard'
 elif o0OOOO00O0Oo >= 16.0 and o0OOOO00O0Oo <= 16.9 :
  ii = 'Jarvis'
 elif o0OOOO00O0Oo >= 17.0 and o0OOOO00O0Oo <= 17.9 :
  ii = 'Krypton'
 else : ii = "Decline"
 if ii == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif ii == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 90 - 90: OOO0o0o % i1IIi / I1II1
def i11Iiii ( text ) :
 if 44 - 44: OOo . I1II1 / o0oO0 + i1iIii1Ii1II
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
 text = text . replace ( '&#8216;' , "'" )
 text = text . replace ( '&#8230;' , "..." )
 text = text . replace ( '&#8220;' , "'" )
 text = text . replace ( '&#8221;' , "'" )
 text = text . replace ( '&#8212;' , "_" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 text = ooOOoooooo ( text )
 return text
 if 65 - 65: O0
 if 68 - 68: O0Oo0oO0o % I11i1i11i1I
 if 88 - 88: iIii1I11I1II1 - ooIiII1I1i1i1ii + O0Oo0oO0o
 if 40 - 40: I1Ii111 * i1iIii1Ii1II + O0Oo0oO0o % O0Oooo00
def OOOOOoo0 ( ) :
 if 49 - 49: O0 . O0Oooo00
 I1iI1iIi111i = [ ]
 iiIi1IIi1I = sys . argv [ 2 ]
 if len ( iiIi1IIi1I ) >= 2 :
  o0OoOO000ooO0 = sys . argv [ 2 ]
  o0o0o0oO0oOO = o0OoOO000ooO0 . replace ( '?' , '' )
  if ( o0OoOO000ooO0 [ len ( o0OoOO000ooO0 ) - 1 ] == '/' ) :
   o0OoOO000ooO0 = o0OoOO000ooO0 [ 0 : len ( o0OoOO000ooO0 ) - 2 ]
  ii1Ii11I = o0o0o0oO0oOO . split ( '&' )
  I1iI1iIi111i = { }
  for I1i1IoOO00oOO in range ( len ( ii1Ii11I ) ) :
   o00o0 = { }
   o00o0 = ii1Ii11I [ I1i1IoOO00oOO ] . split ( '=' )
   if ( len ( o00o0 ) ) == 2 :
    I1iI1iIi111i [ o00o0 [ 0 ] ] = o00o0 [ 1 ]
 return I1iI1iIi111i
 if 45 - 45: O0
o0OoOO000ooO0 = OOOOOoo0 ( ) ; ooOoo0O = None ; o0 = None ; I1IiiiiI = None ; o0O = None ; iiIiIIi = None ; IiII = None
try : o0O = urllib . unquote_plus ( o0OoOO000ooO0 [ "site" ] )
except : pass
try : ooOoo0O = urllib . unquote_plus ( o0OoOO000ooO0 [ "url" ] )
except : pass
try : o0 = urllib . unquote_plus ( o0OoOO000ooO0 [ "name" ] )
except : pass
try : I1IiiiiI = int ( o0OoOO000ooO0 [ "mode" ] )
except : pass
try : iiIiIIi = urllib . unquote_plus ( o0OoOO000ooO0 [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( o0OoOO000ooO0 [ "fanart" ] )
except : pass
try : IiII = urllib . unquote_plus ( o0OoOO000ooO0 [ "description" ] )
except : pass
I1i1I ( )
Ii1 ( )
if I1IiiiiI == None or ooOoo0O == None or len ( ooOoo0O ) < 1 : II111iiii ( )
if 25 - 25: O0 - O0 * OOO0o0o
elif I1IiiiiI == 2 : GetContent ( ooOoo0O )
elif I1IiiiiI == 4 : Oo0oOOo ( ooOoo0O )
if 51 - 51: OOo - i111I + I1iII1iiII * i1iIii1Ii1II . II1iI + i111I
elif I1IiiiiI == 10 : Ii11iI1i ( )
elif I1IiiiiI == 11 : OooO0 ( ooOoo0O )
elif I1IiiiiI == 12 : Oo0O0OOOoo ( ooOoo0O , iiIiIIi )
elif I1IiiiiI == 13 : I1II1III11iii ( ooOoo0O , iiIiIIi )
elif I1IiiiiI == 14 : iIIIIii1 ( ooOoo0O )
elif I1IiiiiI == 15 : OOooO0OOoo ( )
if 78 - 78: i11iIiiIii / O0Oooo00 - i1iIii1Ii1II / O0Oo0oO0o + i111I
elif I1IiiiiI == 99 : O0O0OoOO0 ( o0 , ooOoo0O , iiIiIIi )
if 82 - 82: i1iIii1Ii1II
if I1IiiiiI == None or ooOoo0O == None or len ( ooOoo0O ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
