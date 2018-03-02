#########################################
############CODE BY @NEMZZY668###########
#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , base64
from resources . libs . common_addon import Addon
import requests
import resolveurl
from metahandler import metahandlers
from HTMLParser import HTMLParser
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = 'plugin.video.bashthebishop'
oo = Addon ( o0OO00 , sys . argv )
i1iII1IiiIiI1 = xbmcaddon . Addon ( id = o0OO00 )
iIiiiI1IiI1I1 = '[COLOR pink][B]Bash The Bishop[/B][/COLOR]'
o0OoOoOO00 = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.bashthebishop' )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'fanart.jpg' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'icon.png' ) )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'nextpage.png' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + o0OO00 , 'favs.xml' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'settings.xml' ) )
iIiiiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.bashthebishop/downloads/' ) )
Iii1ii1II11i = xbmcgui . DialogProgress ( )
iI111iI = xbmcgui . Dialog ( )
IiII = 'https://pastebin.com/raw/E0gVutHf'
if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 if 86 - 86: oO0o
 if not os . path . exists ( os . path . dirname ( iIiiiI ) ) :
  try :
   os . makedirs ( os . path . dirname ( iIiiiI ) )
   with open ( o0OOO , "w" ) as IIII :
    IIII . write ( "<date>000</date>" )
  except OSError as Oo0oO0oo0oO00 :
   if Oo0oO0oo0oO00 . errno != errno . EEXIST :
    raise
 i111I ( )
def II1Ii1iI1i ( ) :
 if 12 - 12: o0oOoO00o
 i1 ( "[COLOR white][B]M[COLOR pink]ovies[/B][/COLOR]" , 'null' , 1 , Oo , I11i , '[COLOR pink]XXX Movies[/COLOR]' )
 i1 ( "[COLOR white][B]Y[COLOR pink]ears[/B][/COLOR]" , 'null' , 2 , Oo , I11i , '[COLOR pink]XXX Sorted By Year[/COLOR]' )
 i1 ( "[COLOR white][B]G[COLOR pink]enres[/B][/COLOR]" , 'null' , 4 , Oo , I11i , '[COLOR pink]XXX Sorted By Genre[/COLOR]' )
 i1 ( "[COLOR white][B]H[COLOR pink]ighest Rated[/B][/COLOR]" , 'null' , 5 , Oo , I11i , '[COLOR pink]Highest Rated XXX[/COLOR]' )
 i1 ( "[COLOR white][B]M[COLOR pink]ost Viewed[/B][/COLOR]" , 'null' , 6 , Oo , I11i , '[COLOR pink]Most Viewed XXX[/COLOR]' )
 i1 ( "[COLOR white][B]H[COLOR pink]D[/B][/COLOR]" , 'null' , 7 , Oo , I11i , '[COLOR pink]HD XXX[/COLOR]' )
 i1I1ii1II1iII ( )
 oOOoo00O0O ( )
 if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( url ) :
 if 88 - 88: o0ooo / OOO0O / I1ii * oOOOo0o0O + OoOoo0 % oOOoo
 I1IiIiiIII = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies/page/1'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  iI111I11I1I1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  OOooO0OOoo = re . compile ( '<a href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ] . strip ( )
  iIii1 = re . compile ( '<p>(.*?)</p>' ) . findall ( ii11iIi1I ) [ 0 ]
  iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
  iIii1 = oOOoO0 ( iIii1 )
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 98 , Oo , I11i , iIii1 )
 try :
  O0OoO000O0OO = url . split ( '/' ) [ - 1 ]
  O0OoO000O0OO = int ( O0OoO000O0OO )
  iiI1IiI = O0OoO000O0OO + 1
  II = 'https://pandamoviehd.me/list-movies/page/' + str ( iiI1IiI )
  if iiI1IiI < I1IiIiiIII :
   i1 ( "[COLOR yellow]Next Page ---->[/COLOR]" , II , 1 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 oOOoo00O0O ( )
def ooOoOoo0O ( url ) :
 if 76 - 76: i1II1I11 / i1I / OO0o / ooO0o0Oo % oOOoo
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( '''<ul class='sub-menu'>(.*?)</ul>''' ) . findall ( iI11 ) [ 0 ]
 O00 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( i1iIIi1 )
 for OOooO0OOoo , iI111I11I1I1 in O00 :
  OOooO0OOoo = OOooO0OOoo + '/page/1'
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 3 , Oo , I11i , 'Movies From ' + iI111I11I1I1 )
 oOOoo00O0O ( )
 if 35 - 35: o0ooo + i1II1I11 + i1II1I11
def I11I11i1I ( url ) :
 if 49 - 49: Ii11111i % i1II1I11 * O0
 if '1980' in url : I1IiIiiIII = 1
 elif '1981' in url : I1IiIiiIII = 1
 elif '1982' in url : I1IiIiiIII = 1
 elif '1983' in url : I1IiIiiIII = 1
 elif '1984' in url : I1IiIiiIII = 1
 elif '1985' in url : I1IiIiiIII = 1
 elif '1986' in url : I1IiIiiIII = 1
 elif '1987' in url : I1IiIiiIII = 1
 elif '1988' in url : I1IiIiiIII = 1
 elif '1989' in url : I1IiIiiIII = 1
 elif '1990' in url : I1IiIiiIII = 2
 elif '1991' in url : I1IiIiiIII = 1
 elif '1992' in url : I1IiIiiIII = 1
 elif '1993' in url : I1IiIiiIII = 1
 elif '1994' in url : I1IiIiiIII = 1
 elif '1995' in url : I1IiIiiIII = 3
 elif '1996' in url : I1IiIiiIII = 1
 elif '1997' in url : I1IiIiiIII = 3
 elif '1999' in url : I1IiIiiIII = 5
 elif '2000' in url : I1IiIiiIII = 11
 elif '2001' in url : I1IiIiiIII = 9
 elif '2002' in url : I1IiIiiIII = 12
 else : I1IiIiiIII = 50
 if 89 - 89: I1ii + oO0o
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  iI111I11I1I1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  OOooO0OOoo = re . compile ( '<a href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ] . strip ( )
  try :
   iIii1 = re . compile ( '<p>(.*?)</p>' ) . findall ( ii11iIi1I ) [ 0 ]
  except :
   iIii1 = '[COLOR pink]No Film Description Found[/COLOR]'
  iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
  iIii1 = oOOoO0 ( iIii1 )
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 98 , Oo , I11i , iIii1 )
 try :
  O0OoO000O0OO = url . split ( 'page/' ) [ 0 ]
  iiI1IiI = url . split ( 'page/' ) [ - 1 ]
  iiI1IiI = int ( iiI1IiI )
  II = iiI1IiI + 1
  Ii1I = O0OoO000O0OO + 'page/' + str ( II )
  if II < I1IiIiiIII :
   i1 ( "[COLOR yellow]Next Page ---->[/COLOR]" , Ii1I , 3 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 oOOoo00O0O ( )
def Oo0o0 ( url ) :
 if 49 - 49: I1ii % oOOoo + i1IIi . iiI1i1 % OOO0O
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( '''<ul class='sub-menu'>(.*?)</ul>''' ) . findall ( iI11 ) [ 1 ]
 O00 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( i1iIIi1 )
 for OOooO0OOoo , iI111I11I1I1 in O00 :
  OOooO0OOoo = OOooO0OOoo + '/page/1'
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 3 , Oo , I11i , 'Movie Genre ' + iI111I11I1I1 )
 oOOoo00O0O ( )
def I1i1iii ( url ) :
 if 20 - 20: o0ooo
 I1IiIiiIII = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/most-rating/page/1'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  iI111I11I1I1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  OOooO0OOoo = re . compile ( '<a href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ] . strip ( )
  iIii1 = re . compile ( '<p>(.*?)</p>' ) . findall ( ii11iIi1I ) [ 0 ]
  iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
  iIii1 = oOOoO0 ( iIii1 )
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 98 , Oo , I11i , iIii1 )
 try :
  O0OoO000O0OO = url . split ( '/' ) [ - 1 ]
  O0OoO000O0OO = int ( O0OoO000O0OO )
  iiI1IiI = O0OoO000O0OO + 1
  II = 'https://pandamoviehd.me/most-rating/page/' + str ( iiI1IiI )
  if iiI1IiI < I1IiIiiIII :
   i1 ( "[COLOR yellow]Next Page ---->[/COLOR]" , II , 5 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 oOOoo00O0O ( )
def oO00 ( url ) :
 if 53 - 53: OoooooooOO . i1IIi
 I1IiIiiIII = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/most-viewed/page/1'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  iI111I11I1I1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  OOooO0OOoo = re . compile ( '<a href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ] . strip ( )
  iIii1 = re . compile ( '<p>(.*?)</p>' ) . findall ( ii11iIi1I ) [ 0 ]
  iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
  iIii1 = oOOoO0 ( iIii1 )
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 98 , Oo , I11i , iIii1 )
 try :
  O0OoO000O0OO = url . split ( '/' ) [ - 1 ]
  O0OoO000O0OO = int ( O0OoO000O0OO )
  iiI1IiI = O0OoO000O0OO + 1
  II = 'https://pandamoviehd.me/most-viewed/page/' + str ( iiI1IiI )
  if iiI1IiI < I1IiIiiIII :
   i1 ( "[COLOR yellow]Next Page ---->[/COLOR]" , II , 6 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 oOOoo00O0O ( )
def ii1I1i1I ( url ) :
 if 88 - 88: o0oOoO00o + O0 / I11iii11IIi * i1II1I11
 I1IiIiiIII = 313
 if 'null' in url :
  url = 'https://pandamoviehd.me/watch-hd-movies-online-free/page/1'
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  iI111I11I1I1 = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  OOooO0OOoo = re . compile ( '<a href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ] . strip ( )
  iIii1 = re . compile ( '<p>(.*?)</p>' ) . findall ( ii11iIi1I ) [ 0 ]
  iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
  iIii1 = oOOoO0 ( iIii1 )
  i1 ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 98 , Oo , I11i , iIii1 )
 try :
  O0OoO000O0OO = url . split ( '/' ) [ - 1 ]
  O0OoO000O0OO = int ( O0OoO000O0OO )
  iiI1IiI = O0OoO000O0OO + 1
  II = 'https://pandamoviehd.me/watch-hd-movies-online-free/page/' + str ( iiI1IiI )
  if iiI1IiI < I1IiIiiIII :
   i1 ( "[COLOR yellow]Next Page ---->[/COLOR]" , II , 7 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 oOOoo00O0O ( )
def iiiIi1i1I ( title ) :
 if 80 - 80: I11iii11IIi - o0oOoO00o
 title = title . lower ( )
 if 'openload' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'thevideo' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'vidup' in title :
  title = title . title ( )
  title = title + '[COLOR yellow] (Requires Pairing)[/COLOR]'
  return title
 if 'upvid' in title :
  title = 'not supported'
  return title
 else :
  title = title . title ( )
  return title
  if 87 - 87: I1ii / OoOoo0 - i1IIi * oOOOo0o0O / OoooooooOO . O0
def iii11I111 ( url , iconimage , description ) :
 if 63 - 63: o0oOoO00o * I1ii - i1II1I11 * O0
 iI11 = iII111ii ( url )
 i1iIIi1 = re . compile ( '<li class="hosts-buttons-wpx">(.*?)</li>' ) . findall ( iI11 )
 for ii11iIi1I in i1iIIi1 :
  try :
   iI111I11I1I1 = re . compile ( 'class="selected">(.*?)</a>' ) . findall ( ii11iIi1I ) [ 0 ]
   iI111I11I1I1 = oOOoO0 ( iI111I11I1I1 )
   iI111I11I1I1 = iiiIi1i1I ( iI111I11I1I1 )
   OOooO0OOoo = re . compile ( 'href="(.*?)"' ) . findall ( ii11iIi1I ) [ 0 ]
   if not 'not supported' in iI111I11I1I1 :
    iIii111IIi ( "[COLOR pink]" + iI111I11I1I1 + "[/COLOR]" , OOooO0OOoo , 99 , iconimage , I11i , description )
  except : pass
 oOOoo00O0O ( )
def iII111ii ( url ) :
 try :
  iii11 = urllib2 . Request ( url )
  iii11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  O0oo0OO0oOOOo = urllib2 . urlopen ( iii11 , timeout = 5 )
  iI11 = O0oo0OO0oOOOo . read ( )
  O0oo0OO0oOOOo . close ( )
  iI11 = iI11 . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return iI11
 except : quit ( )
 if 35 - 35: i1I % iiI1i1
 if 70 - 70: i1II1I11 * OOO0O
def i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 46 - 46: ooO0o0Oo / o0oOoO00o
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 OOOoO0O0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 O0o0Ooo = True
 O00iI1Ii11iII1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 O00iI1Ii11iII1 . setProperty ( "fanart_Image" , fanart )
 O00iI1Ii11iII1 . setProperty ( "icon_Image" , iconimage )
 O00iI1Ii11iII1 . setInfo ( 'video' , { 'Plot' : description } )
 O0o0Ooo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOoO0O0o , listitem = O00iI1Ii11iII1 , isFolder = True )
 Oo0O0O0ooO0O = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return O0o0Ooo
 if 15 - 15: OOO0O + I11iii11IIi - OoooooooOO / oOOOo0o0O
 if 58 - 58: i11iIiiIii % OoOoo0
def iIii111IIi ( name , url , mode , iconimage , fanart , description = '' ) :
 if 71 - 71: oOOOo0o0O + ooO0o0Oo % i11iIiiIii + OOO0O - i1I
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 OOOoO0O0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 O0o0Ooo = True
 O00iI1Ii11iII1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 O00iI1Ii11iII1 . setProperty ( "fanart_Image" , fanart )
 O00iI1Ii11iII1 . setProperty ( "icon_Image" , iconimage )
 O00iI1Ii11iII1 . setInfo ( 'video' , { 'Plot' : description } )
 if 88 - 88: I11iii11IIi - o0oOoO00o % oOOOo0o0O
 if 16 - 16: iiI1i1 * I1ii % i1I
 Oo0O0O0ooO0O = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 O0o0Ooo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOOoO0O0o , listitem = O00iI1Ii11iII1 , isFolder = False )
 return O0o0Ooo
 if 86 - 86: iiI1i1 + oOOoo % i11iIiiIii * I1ii . ooO0o0Oo * OoOoo0
 if 44 - 44: I1ii
def o0o0oOoOO0 ( txt ) :
 if 17 - 17: i1I
 txt = txt . replace ( "&quot;" , "\"" )
 txt = txt . replace ( "&amp;" , "&" )
 txt = txt . replace ( u"\u2018" , "'" ) . replace ( u"\u2019" , "'" )
 txt = txt . strip ( )
 return txt
 if 62 - 62: iIii1I11I1II1 * I11iii11IIi
def i1OOO ( string ) :
 Oo0oOOo = ( c for c in string if 0 < ord ( c ) < 127 )
 if 58 - 58: Ii11111i * oOOOo0o0O * OOO0O / oOOOo0o0O
 return '' . join ( Oo0oOOo )
 if 75 - 75: I1ii
def I1III ( heading , text ) :
 if 63 - 63: oOOOo0o0O % I1ii * I1ii * o0oOoO00o / OOO0O
 text = text + "\n\nNews Updates Every 5 Seconds"
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 o0ooO = xbmcgui . Window ( id )
 O0o0O00Oo0o0 = 50
 while ( O0o0O00Oo0o0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   O0o0O00Oo0o0 -= 1
   o0ooO . getControl ( 1 ) . setLabel ( heading )
   o0ooO . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 87 - 87: ooO0o0Oo * oO0o % i11iIiiIii % I11iii11IIi - oOOOo0o0O
def O0ooo0O0oo0 ( name , url , iconimage ) :
 if 91 - 91: iIii1I11I1II1 + OO0o
 iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR pink]Attempting To Resolve Link Now[/COLOR]' , Oo , 5000 )
 if 31 - 31: i1I . I11iii11IIi . oOOOo0o0O
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  O0oOoOO = resolveurl . HostedMediaFile ( url ) . resolve ( )
  O00iI1Ii11iII1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  O00iI1Ii11iII1 . setPath ( O0oOoOO )
  xbmc . Player ( ) . play ( O0oOoOO , O00iI1Ii11iII1 , False )
  quit ( )
 else :
  O0oOoOO = url
  O00iI1Ii11iII1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  O00iI1Ii11iII1 . setPath ( O0oOoOO )
  xbmc . Player ( ) . play ( O0oOoOO , O00iI1Ii11iII1 , False )
  quit ( )
  if 96 - 96: oO0o
def i111I ( ) :
 if 45 - 45: O0 * o0ooo % oO0o * OoooooooOO + i1II1I11 . I11iii11IIi
 Oo0ooOo0o = open ( o0OOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  Ii1i1 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Oo0ooOo0o ) [ 0 ]
  if Ii1i1 == 'EXPIRED' :
   iI111iI . ok ( iIiiiI1IiI1I1 , "[COLOR pink]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR pink] to generate a Pin to access Bash The Bishop then enter it after clicking ok[/COLOR]" )
   iiIii = ''
   ooo0O = xbmc . Keyboard ( iiIii , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   ooo0O . doModal ( )
   if ooo0O . isConfirmed ( ) :
    iiIii = ooo0O . getText ( )
    if len ( iiIii ) > 1 :
     oOoO0o00OO0 = iiIii . title ( )
     with open ( o0OOO , "w" ) as IIII :
      IIII . write ( "<pin>" + oOoO0o00OO0 + "</pin>" )
     i111I ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in Ii1i1 :
   i1I1ii = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Oo0ooOo0o ) [ 0 ]
   oOOo0 = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % i1I1ii )
   iI11 = iII111ii ( oOOo0 )
   if 'Pin Verified' in iI11 :
    pass
   else :
    with open ( o0OOO , "w" ) as IIII :
     IIII . write ( '<pin>EXPIRED</pin>' )
     i111I ( )
 except IndexError :
  with open ( o0OOO , "w" ) as IIII :
   IIII . write ( "<pin>EXPIRED</pin>\n" )
  i111I ( )
  if 54 - 54: O0 - i1I % oOOOo0o0O
def oOOoo00O0O ( ) :
 if 77 - 77: I11iii11IIi / iiI1i1 / o0oOoO00o + o0oOoO00o . oOOOo0o0O
 ii1ii11IIIiiI = xbmc . getInfoLabel ( "System.BuildVersion" )
 O00OOOoOoo0O = float ( ii1ii11IIIiiI [ : 4 ] )
 if O00OOOoOoo0O >= 11.0 and O00OOOoOoo0O <= 11.9 :
  O000OOo00oo = 'Eden'
 elif O00OOOoOoo0O >= 12.0 and O00OOOoOoo0O <= 12.9 :
  O000OOo00oo = 'Frodo'
 elif O00OOOoOoo0O >= 13.0 and O00OOOoOoo0O <= 13.9 :
  O000OOo00oo = 'Gotham'
 elif O00OOOoOoo0O >= 14.0 and O00OOOoOoo0O <= 14.9 :
  O000OOo00oo = 'Helix'
 elif O00OOOoOoo0O >= 15.0 and O00OOOoOoo0O <= 15.9 :
  O000OOo00oo = 'Isengard'
 elif O00OOOoOoo0O >= 16.0 and O00OOOoOoo0O <= 16.9 :
  O000OOo00oo = 'Jarvis'
 elif O00OOOoOoo0O >= 17.0 and O00OOOoOoo0O <= 17.9 :
  O000OOo00oo = 'Krypton'
 else : O000OOo00oo = "Decline"
 if 71 - 71: i11iIiiIii + i1I
 if O000OOo00oo == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif O000OOo00oo == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 57 - 57: I1ii . OoOoo0 . i1IIi
def oOOoO0 ( text ) :
 if 42 - 42: OoOoo0 + OOO0O % O0
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
 text = i1OOO ( text )
 return text
 if 6 - 6: I1ii
def oOOo0oOo0 ( ) :
 if 49 - 49: oO0o . i11iIiiIii - i1IIi / Ii11111i . iiI1i1
 i1iII1IiiIiI1 . openSettings ( )
 if 1 - 1: oO0o / o0ooo % i1II1I11 * i1I . i11iIiiIii
def III1Iiii1I11 ( ) :
 if 9 - 9: OOO0O / oO0o - iiI1i1 / OoooooooOO / iIii1I11I1II1 - o0ooo
 o00oooO0Oo = [ ]
 o0O0OOO0Ooo = sys . argv [ 2 ]
 if len ( o0O0OOO0Ooo ) >= 2 :
  iiIiI = sys . argv [ 2 ]
  I1 = iiIiI . replace ( '?' , '' )
  if ( iiIiI [ len ( iiIiI ) - 1 ] == '/' ) :
   iiIiI = iiIiI [ 0 : len ( iiIiI ) - 2 ]
  OOO00O0O = I1 . split ( '&' )
  o00oooO0Oo = { }
  for iii in range ( len ( OOO00O0O ) ) :
   oOooOOOoOo = { }
   oOooOOOoOo = OOO00O0O [ iii ] . split ( '=' )
   if ( len ( oOooOOOoOo ) ) == 2 :
    o00oooO0Oo [ oOooOOOoOo [ 0 ] ] = oOooOOOoOo [ 1 ]
 return o00oooO0Oo
 if 41 - 41: oOOoo - O0 - O0
iiIiI = III1Iiii1I11 ( ) ; oO00OOoO00 = None ; IiI111111IIII = None ; i1Ii = None ; ii111iI1iIi1 = None ; OOO = None ; oo0OOo0 = None
try : ii111iI1iIi1 = urllib . unquote_plus ( iiIiI [ "site" ] )
except : pass
try : oO00OOoO00 = urllib . unquote_plus ( iiIiI [ "url" ] )
except : pass
try : IiI111111IIII = urllib . unquote_plus ( iiIiI [ "name" ] )
except : pass
try : i1Ii = int ( iiIiI [ "mode" ] )
except : pass
try : OOO = urllib . unquote_plus ( iiIiI [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( iiIiI [ "fanart" ] )
except : pass
try : oo0OOo0 = urllib . unquote_plus ( iiIiI [ "description" ] )
except : pass
if 47 - 47: OO0o + I11iii11IIi * oO0o / ooO0o0Oo - i1II1I11 % iIii1I11I1II1
if i1Ii == None or oO00OOoO00 == None or len ( oO00OOoO00 ) < 1 : II1Ii1iI1i ( )
if 26 - 26: OOO0O * i1II1I11 . Ii11111i * oOOoo
elif i1Ii == 1 : O00o0o0000o0o ( oO00OOoO00 )
elif i1Ii == 2 : ooOoOoo0O ( oO00OOoO00 )
elif i1Ii == 3 : I11I11i1I ( oO00OOoO00 )
elif i1Ii == 4 : Oo0o0 ( oO00OOoO00 )
elif i1Ii == 5 : I1i1iii ( oO00OOoO00 )
elif i1Ii == 6 : oO00 ( oO00OOoO00 )
elif i1Ii == 7 : ii1I1i1I ( oO00OOoO00 )
if 28 - 28: o0oOoO00o . i1IIi * iiI1i1 + O0 . i1IIi - ooO0o0Oo
if 38 - 38: OO0o
if 84 - 84: iIii1I11I1II1 % i1II1I11 / iIii1I11I1II1 % OoOoo0
if 45 - 45: O0
elif i1Ii == 98 : iii11I111 ( oO00OOoO00 , OOO , oo0OOo0 )
elif i1Ii == 99 : O0ooo0O0oo0 ( IiI111111IIII , oO00OOoO00 , OOO )
if 26 - 26: OoOoo0 - iIii1I11I1II1 - iiI1i1 / o0oOoO00o . I11iii11IIi % iIii1I11I1II1
elif i1Ii == 892 : oOOo0oOo0 ( )
if 91 - 91: o0ooo . iIii1I11I1II1 / I1ii + i1IIi
if 42 - 42: ooO0o0Oo . o0ooo . ooO0o0Oo - OOO0O
if i1Ii == None or oO00OOoO00 == None or len ( oO00OOoO00 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 40 - 40: ooO0o0Oo - i11iIiiIii / oOOoo
if 35 - 35: oOOoo - iiI1i1 % o0ooo . OoooooooOO % oOOoo
if 47 - 47: i1II1I11 - oOOoo . Ii11111i + OoooooooOO . i11iIiiIii
if 94 - 94: o0ooo * oOOoo / oO0o / oOOoo
if 87 - 87: oO0o . i1I
if 75 - 75: ooO0o0Oo + I11iii11IIi + o0ooo * OoOoo0 % I1ii . i1II1I11
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
