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
 II ( "[COLOR yellow]M[COLOR aqua]ovies[/COLOR]" , 'https://putlockermovies.to/movies/page/1' , 14 , Oo , O0O , 'Movies' )
 II ( "[COLOR yellow]T[COLOR aqua]v Shows[/COLOR]" , 'https://putlockermovies.to/series/page/1' , 14 , Oo , O0O , 'Tv Shows' )
 II ( "[COLOR yellow]L[COLOR aqua]atest Episodes[/COLOR]" , 'https://putlockermovies.to/episode/page/1' , 14 , Oo , O0O , 'Latest Episodes' )
 II ( "[COLOR yellow]G[COLOR aqua]enres[/COLOR]" , 'noop' , 10 , Oo , O0O , 'Movies and Tv Shows Sorted By Genre' )
 II ( "[COLOR yellow]F[COLOR aqua]eatured Movies[/COLOR]" , 'https://putlockermovies.to/genre/featured/page/1' , 14 , Oo , O0O , 'Featured Movies' )
 II ( "[COLOR yellow]T[COLOR aqua]op IMDB Movies[/COLOR]" , 'https://putlockermovies.to/top-imdb/page/1' , 14 , Oo , O0O , 'Movies Sorted By IMDB Rating' )
 if 63 - 63: oO0o % i1IIi
def o0oOo0Ooo0O ( ) :
 if 81 - 81: o0oO0 * i1IIi11111i * II1iI - O0Oooo00 - OOO0o0o
 OooO0OO = iiiIi ( Ooo0OO0oOO )
 IiIIIiI1I1 = re . compile ( '''<ul class='sub-menu'>(.*?)</div>''' ) . findall ( OooO0OO ) [ 0 ]
 OoO000 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( IiIIIiI1I1 )
 for IIiiIiI1 , iiIiIIi in OoO000 :
  if not 'https' in IIiiIiI1 :
   IIiiIiI1 = 'https://putlockermovies.to' + IIiiIiI1
  II ( "[COLOR yellow]" + iiIiIIi + "[/COLOR]" , IIiiIiI1 , 11 , Oo , O0O , iiIiIIi + ' Genre' )
  if 65 - 65: oO0o
def ii1I ( url ) :
 if 76 - 76: O0 / OOO0o0o . I1Ii111 * i1iIii1Ii1II - O0Oo0oO0o
 OooO0OO = iiiIi ( url )
 IiIIIiI1I1 = re . compile ( '''class="ml-item">(.*?)</a>''' ) . findall ( OooO0OO )
 for OoO000 in IiIIIiI1I1 :
  Oooo = re . compile ( 'oldtitle="(.*?)"' ) . findall ( OoO000 ) [ 0 ]
  Oooo = O00o ( Oooo )
  url = re . compile ( '<a href="(.*?)"' ) . findall ( OoO000 ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( OoO000 ) [ 0 ] . strip ( )
  if '/series/' in url :
   II ( "[COLOR yellow]" + Oooo + "[/COLOR]" , url , 12 , Oo , O0O , Oooo )
  else :
   II ( "[COLOR yellow]" + Oooo + "[/COLOR]" , url , 4 , Oo , O0O , Oooo )
   if 61 - 61: O0Oooo00 . iIii1I11I1II1 * I1Ii111 . ooIiII1I1i1i1ii % OOo
def oOo00Oo00O ( url , iconimage ) :
 if 43 - 43: I1Ii111 - O0Oooo00 * iIii1I11I1II1
 OooO0OO = iiiIi ( url )
 IiIIIiI1I1 = re . compile ( '<div class="les-title">(.*?)</ul>' ) . findall ( OooO0OO )
 O0O00o0OOO0 = 0
 for OoO000 in IiIIIiI1I1 :
  O0O00o0OOO0 += 1
  Ii1iIIIi1ii = re . compile ( '''<strong>(.*?)</strong>''' ) . findall ( OoO000 ) [ 0 ]
  o0oo0o0O00OO = 'season-' + str ( O0O00o0OOO0 ) + '-'
  II ( "[COLOR yellow]" + Ii1iIIIi1ii + "[/COLOR]" , url + ':::' + o0oo0o0O00OO , 13 , iconimage , O0O , Ii1iIIIi1ii )
  if 80 - 80: i1IIi
def oOOO0o0o ( url , iconimage ) :
 if 26 - 26: OoooooooOO
 if 12 - 12: OoooooooOO % oO0o / ooIiII1I1i1i1ii % OOO0o0o
 iiii = url . split ( ':::' ) [ 1 ]
 url = url . split ( ':::' ) [ 0 ]
 OooO0OO = iiiIi ( url )
 IiIIIiI1I1 = re . compile ( '<div class="les-title">(.*?)</ul>' ) . findall ( OooO0OO )
 oO0o0O0OOOoo0 = [ ]
 IiIiiI = [ ]
 I1I = [ ]
 for OoO000 in IiIIIiI1I1 :
  Oooo = re . compile ( '''<a href=".*?">(.*?)</a>''' ) . findall ( OoO000 )
  for iiIiIIi in Oooo :
   IiIiiI . append ( iiIiIIi )
  url = re . compile ( '''<a href="(.*?)"''' ) . findall ( OoO000 )
  for oOO00oOO in url :
   oO0o0O0OOOoo0 . append ( oOO00oOO )
  I1I = list ( zip ( IiIiiI , oO0o0O0OOOoo0 ) )
 for OoOo , OooO0OO in I1I :
  if iiii in OooO0OO :
   iI ( "[COLOR yellow]" + OoOo + "[/COLOR]" , OooO0OO , 4 , iconimage , O0O , OoOo )
   if 60 - 60: II1iI / II1iI
def I1II1III11iii ( url ) :
 if 75 - 75: iIii1I11I1II1 / O0Oo0oO0o % OOO0o0o * oO0o
 OooO0OO = iiiIi ( url )
 IiIIIiI1I1 = re . compile ( '''class="ml-item">(.*?)</a>''' ) . findall ( OooO0OO )
 for OoO000 in IiIIIiI1I1 :
  Oooo = re . compile ( 'oldtitle="(.*?)"' ) . findall ( OoO000 ) [ 0 ]
  Oooo = O00o ( Oooo )
  iiii11I = re . compile ( '<a href="(.*?)"' ) . findall ( OoO000 ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( OoO000 ) [ 0 ] . strip ( )
  if '/series/' in url :
   II ( "[COLOR yellow]" + Oooo + "[/COLOR]" , iiii11I , 12 , Oo , O0O , Oooo )
  else :
   iI ( "[COLOR yellow]" + Oooo + "[/COLOR]" , iiii11I , 4 , Oo , O0O , Oooo )
 try :
  Ooo0OO0oOOii11i1 = url . split ( 'page/' ) [ 1 ]
  IIIii1II1II = url . split ( 'page/' ) [ 0 ]
  i1I1iI = int ( Ooo0OO0oOOii11i1 ) + 1
  oo0OooOOo0 = IIIii1II1II + 'page/' + str ( i1I1iI )
  II ( "[COLOR aqua]Next Page --->[/COLOR]" , oo0OooOOo0 , 14 , o0O , O0O , Oooo )
 except : pass
 if 72 - 72: O0Oooo00 / i1IIi * OOo - I11i1i11i1I
 if 51 - 51: I1iII1iiII * I1II1 % OOO0o0o * I1iII1iiII % o0oO0 / ooIiII1I1i1i1ii
def iIIIIii1 ( url ) :
 if 58 - 58: i11iIiiIii % II1iI
 OooO0OO = iiiIi ( url )
 OO00Oo = re . compile ( '<iframe src="(.*?)"' ) . findall ( OooO0OO ) [ 0 ]
 O0OOO0OOoO0O ( iiIiIIi , OO00Oo , o0O )
 if 70 - 70: i1IIi11111i * OOo * II1iI / i1iIii1Ii1II
def iiiIi ( url ) :
 try :
  oO = urllib2 . Request ( url )
  oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OOoO0O00o0 = urllib2 . urlopen ( oO , timeout = 5 )
  OooO0OO = OOoO0O00o0 . read ( )
  OOoO0O00o0 . close ( )
  OooO0OO = OooO0OO . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return OooO0OO
 except : quit ( )
 if 30 - 30: OOO0o0o . i1iIii1Ii1II - OoooooooOO
def II ( name , url , mode , iconimage , fanart , description = '' ) :
 if 8 - 8: i1IIi - iIii1I11I1II1 * I1iII1iiII + i11iIiiIii / I11i1i11i1I % O0Oo0oO0o
 if not iconimage :
  iconimage = Oo
 if not fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 iIIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiII1i1 = True
 o00oOO0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 o00oOO0o . setProperty ( "fanart_Image" , fanart )
 o00oOO0o . setProperty ( "icon_Image" , iconimage )
 o00oOO0o . setInfo ( 'video' , { 'Plot' : description } )
 iiII1i1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIi1 , listitem = o00oOO0o , isFolder = True )
 OOO00O = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return iiII1i1
 if 84 - 84: i111I * I1II1 / II1iI - O0
def iI ( name , url , mode , iconimage , fanart , description = '' ) :
 if 30 - 30: iIii1I11I1II1 / ooIiII1I1i1i1ii - I11i1i11i1I - I1iII1iiII % O0Oooo00
 if not iconimage :
  iconimage = Oo
 if not fanart :
  fanart = I11i
 iIIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iiII1i1 = True
 o00oOO0o = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 o00oOO0o . setProperty ( "fanart_Image" , fanart )
 o00oOO0o . setProperty ( "icon_Image" , iconimage )
 o00oOO0o . setInfo ( 'video' , { 'Plot' : description } )
 IIi1i11111 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 o00oOO0o . addContextMenuItems ( [ ( '[COLOR pink]Add To Bishop Favourites[/COLOR]' , 'xbmc.RunPlugin(' + IIi1i11111 + ')' ) ] )
 OOO00O = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 iiII1i1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIIi1 , listitem = o00oOO0o , isFolder = False )
 return iiII1i1
 if 81 - 81: i11iIiiIii % oO0o - O0Oo0oO0o
def O0OOO0OOoO0O ( name , url , iconimage ) :
 if 68 - 68: I11i1i11i1I % i1IIi . i1IIi11111i . o0oO0
 Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Lets Grab That Link[/COLOR]' , Oo , 4000 )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  o0 = resolveurl . HostedMediaFile ( url ) . resolve ( )
  o00oOO0o = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  o00oOO0o . setPath ( o0 )
  xbmc . Player ( ) . play ( o0 , o00oOO0o , False )
  if 91 - 91: iIii1I11I1II1 + I11i1i11i1I
 else :
  o0 = url
  o00oOO0o = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  o00oOO0o . setPath ( o0 )
  xbmc . Player ( ) . play ( o0 , o00oOO0o , False )
  if 31 - 31: i1IIi11111i . oO0o . O0Oo0oO0o
 time . sleep ( 6 )
 if xbmc . Player ( ) . isPlaying ( ) :
  Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Enjoy Your Content[/COLOR]' , Oo , 4000 )
  quit ( )
 else :
  xbmc . executebuiltin ( "Dialog.Close(all)" )
  Iii1ii1II11i . notification ( iIiiiI1IiI1I1 , '[COLOR yellow]Damn Seems That Link Down At The Moment[/COLOR]' , Oo , 4000 )
  quit ( )
  if 75 - 75: II1iI + I1II1 . oO0o . ooIiII1I1i1i1ii + OOo . I1II1
def O0Oooo0OO ( ) :
 if 65 - 65: i1iIii1Ii1II . iIii1I11I1II1 / O0 - i1iIii1Ii1II
 if 21 - 21: I1Ii111 * iIii1I11I1II1
 oooooOoo0ooo = open ( o0OOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I1I1IiI1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oooooOoo0ooo ) [ 0 ]
  if I1I1IiI1 == 'EXPIRED' :
   Iii1ii1II11i . ok ( iIiiiI1IiI1I1 , "[COLOR aqua]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR aqua] to generate a Pin to access Entertainment Time then enter it after clicking ok[/COLOR]" )
   III1iII1I1ii = ''
   oOOo0 = xbmc . Keyboard ( III1iII1I1ii , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   oOOo0 . doModal ( )
   if oOOo0 . isConfirmed ( ) :
    III1iII1I1ii = oOOo0 . getText ( )
    if len ( III1iII1I1ii ) > 1 :
     oo00O00oO = III1iII1I1ii . title ( )
     with open ( o0OOO , "w" ) as iiiI11 :
      iiiI11 . write ( "<pin>" + oo00O00oO + "</pin>" )
     O0Oooo0OO ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in I1I1IiI1 :
   iIiIIIi = re . compile ( '<pin>(.+?)</pin>' ) . findall ( oooooOoo0ooo ) [ 0 ]
   ooo00OOOooO = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % iIiIIIi )
   OooO0OO = iiiIi ( ooo00OOOooO )
   if len ( OooO0OO ) < 1 or 'Pin Expired' in OooO0OO :
    with open ( o0OOO , "w" ) as iiiI11 :
     iiiI11 . write ( '<pin>EXPIRED</pin>' )
    O0Oooo0OO ( )
   else :
    global baseurl
    baseurl = OooO0OO
 except IndexError :
  with open ( o0OOO , "w" ) as iiiI11 :
   iiiI11 . write ( "<pin>EXPIRED</pin>\n" )
  O0Oooo0OO ( )
  if 67 - 67: II1iI * i111I * o0oO0 + O0Oo0oO0o / i1IIi
def I1I111 ( string ) :
 if 82 - 82: i11iIiiIii - O0Oooo00 * OoooooooOO / II1iI
 i1 = ( c for c in string if 0 < ord ( c ) < 127 )
 return '' . join ( i1 )
 if 57 - 57: i111I . II1iI . i1IIi
def i11Iii ( ) :
 if 16 - 16: I1iII1iiII % oO0o - I1iII1iiII + i1iIii1Ii1II
 i1I1i = xbmc . getInfoLabel ( "System.BuildVersion" )
 Ii = float ( i1I1i [ : 4 ] )
 if Ii >= 11.0 and Ii <= 11.9 :
  iii1i = 'Eden'
 elif Ii >= 12.0 and Ii <= 12.9 :
  iii1i = 'Frodo'
 elif Ii >= 13.0 and Ii <= 13.9 :
  iii1i = 'Gotham'
 elif Ii >= 14.0 and Ii <= 14.9 :
  iii1i = 'Helix'
 elif Ii >= 15.0 and Ii <= 15.9 :
  iii1i = 'Isengard'
 elif Ii >= 16.0 and Ii <= 16.9 :
  iii1i = 'Jarvis'
 elif Ii >= 17.0 and Ii <= 17.9 :
  iii1i = 'Krypton'
 else : iii1i = "Decline"
 if iii1i == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 elif iii1i == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 39 - 39: O0Oooo00 - O0 % i11iIiiIii * I11i1i11i1I . i1IIi11111i
def O00o ( text ) :
 if 58 - 58: I1II1 % i11iIiiIii . O0Oooo00 / i111I
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
 text = I1I111 ( text )
 return text
 if 84 - 84: O0Oooo00 . o0oO0 / OOo - I1Ii111 / OoooooooOO / OOO0o0o
 if 12 - 12: I1Ii111 * O0Oooo00 % i1IIi % iIii1I11I1II1
 if 20 - 20: O0Oo0oO0o % i1iIii1Ii1II / i1iIii1Ii1II + i1iIii1Ii1II
 if 45 - 45: i111I - i1IIi11111i - OoooooooOO - I1II1 . I1iII1iiII / O0
def oo0o00O ( ) :
 if 51 - 51: i1iIii1Ii1II - I1II1 * O0Oooo00
 oooo0O0 = [ ]
 oOOO = sys . argv [ 2 ]
 if len ( oOOO ) >= 2 :
  iIII1 = sys . argv [ 2 ]
  o0o = iIII1 . replace ( '?' , '' )
  if ( iIII1 [ len ( iIII1 ) - 1 ] == '/' ) :
   iIII1 = iIII1 [ 0 : len ( iIII1 ) - 2 ]
  O0OOoO00OO0o = o0o . split ( '&' )
  oooo0O0 = { }
  for O0O00o0OOO0 in range ( len ( O0OOoO00OO0o ) ) :
   I1111IIIIIi = { }
   I1111IIIIIi = O0OOoO00OO0o [ O0O00o0OOO0 ] . split ( '=' )
   if ( len ( I1111IIIIIi ) ) == 2 :
    oooo0O0 [ I1111IIIIIi [ 0 ] ] = I1111IIIIIi [ 1 ]
 return oooo0O0
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * O0Oooo00 % i11iIiiIii * I1Ii111
iIII1 = oo0o00O ( ) ; IIiiIiI1 = None ; iiIiIIi = None ; oo000o = None ; iiIi1IIi1I = None ; o0O = None ; o0OoOO000ooO0 = None
try : iiIi1IIi1I = urllib . unquote_plus ( iIII1 [ "site" ] )
except : pass
try : IIiiIiI1 = urllib . unquote_plus ( iIII1 [ "url" ] )
except : pass
try : iiIiIIi = urllib . unquote_plus ( iIII1 [ "name" ] )
except : pass
try : oo000o = int ( iIII1 [ "mode" ] )
except : pass
try : o0O = urllib . unquote_plus ( iIII1 [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( iIII1 [ "fanart" ] )
except : pass
try : o0OoOO000ooO0 = urllib . unquote_plus ( iIII1 [ "description" ] )
except : pass
I1i1I ( )
O0Oooo0OO ( )
if oo000o == None or IIiiIiI1 == None or len ( IIiiIiI1 ) < 1 : II111iiii ( )
if 56 - 56: O0Oooo00
elif oo000o == 2 : GetContent ( IIiiIiI1 )
elif oo000o == 4 : iIIIIii1 ( IIiiIiI1 )
if 86 - 86: I1iII1iiII % I11i1i11i1I
elif oo000o == 10 : o0oOo0Ooo0O ( )
elif oo000o == 11 : ii1I ( IIiiIiI1 )
elif oo000o == 12 : oOo00Oo00O ( IIiiIiI1 , o0O )
elif oo000o == 13 : oOOO0o0o ( IIiiIiI1 , o0O )
elif oo000o == 14 : I1II1III11iii ( IIiiIiI1 )
if 15 - 15: i1IIi * I1Ii111 + i11iIiiIii
elif oo000o == 99 : O0OOO0OOoO0O ( iiIiIIi , IIiiIiI1 , o0O )
if 6 - 6: ooIiII1I1i1i1ii / i11iIiiIii + O0Oooo00 * i111I
if oo000o == None or IIiiIiI1 == None or len ( IIiiIiI1 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
