#########################################
############CODE BY @NEMZZY668###########
#########################################
if 64 - 64: i11iIiiIii
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , uuid , os , re , sys , base64 , json , time , shutil , urlresolver , random , liveresolver , hashlib , datetime
from resources . libs . modules import cfscrape
from resources . libs . common_addon import Addon
from metahandler import metahandlers
from HTMLParser import HTMLParser
from datetime import datetime
from resources . libs . modules import devilcheck
from resources . libs . modules import dom_parser2
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'plugin.video.sportsworld'
o0OOO = Addon ( I1IiI , sys . argv )
iIiiiI = xbmcaddon . Addon ( id = I1IiI )
Iii1ii1II11i = '[COLOR orange][B]Sports World[/B][/COLOR]'
iI111iI = os . path . join ( os . path . join ( xbmc . translatePath ( 'special://home' ) , 'addons' ) , 'plugin.video.sportsworld' )
IiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'icon.png' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'base.xml' ) )
I1i1iiI1 = xbmcgui . DialogProgress ( )
iiIIIII1i1iI = xbmcgui . Dialog ( )
o0oO0 = base64 . b64decode ( b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3NHSDBkWjBC' )
oo00 = xbmc . translatePath ( 'special://home/addons/plugin.video.sportsworld/intro' )
if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
def i1I1Iiii1111 ( url ) :
 try :
  i11 = urllib2 . Request ( url )
  i11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  I11 = urllib2 . urlopen ( i11 , timeout = 5 )
  Oo0o0000o0o0 = I11 . read ( )
  I11 . close ( )
  Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  return Oo0o0000o0o0
 except : quit ( )
 if 86 - 86: iiiii11iII1 % O0o
def oO0 ( url ) :
 i11 = urllib2 . Request ( url )
 i11 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 I11 = urllib2 . urlopen ( i11 )
 Oo0o0000o0o0 = I11 . read ( )
 I11 . close ( )
 if 32 - 32: I1i1I - OoOoo0 % iIiiI1 % II1iI
 return Oo0o0000o0o0
 if 91 - 91: o0oOOo0O0Ooo / II111iiii . I1ii11iIi11i + II1iI
def iI11 ( string ) :
 iII111ii = ( c for c in string if 0 < ord ( c ) < 127 )
 if 3 - 3: O0o + O0
 return '' . join ( iII111ii )
 if 42 - 42: II1iI / i1IIi + i11iIiiIii - iiiii11iII1
def oo0Ooo0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 46 - 46: iIiiI1 % iIiiI1 - O0Oo0oO0o * o0oOOo0O0Ooo % O0o
 if not "http" in iconimage :
  iconimage = i1i1II
 if not "http" in fanart :
  fanart = IiII
 OOooO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIii1 = True
 oOOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOOoO0 . setProperty ( "fanart_Image" , fanart )
 oOOoO0 . setProperty ( "icon_Image" , iconimage )
 iIii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOooO0OOoo , listitem = oOOoO0 , isFolder = True )
 return iIii1
 if 59 - 59: iiiii11iII1 * i11iIiiIii + iiiii11iII1 + iIiiI1 * OoO0O00
def OooOoO0Oo ( name , url , mode , iconimage , fanart , description = '' ) :
 if not "http" in iconimage :
  iconimage = i1i1II
 if not "http" in fanart :
  fanart = IiII
 OOooO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIii1 = True
 oOOoO0 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 oOOoO0 . setProperty ( "fanart_Image" , fanart )
 oOOoO0 . setProperty ( "icon_Image" , iconimage )
 iIii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOooO0OOoo , listitem = oOOoO0 , isFolder = False )
 return iIii1
 if 47 - 47: O0Oo0oO0o
def iiIiIiIi ( name , url , mode , iconimage , fanart , description = '' ) :
 OOooO0OOoo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIii1 = True
 oOOoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOOoO0 . setProperty ( 'fanart_image' , fanart )
 iIii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOooO0OOoo , listitem = oOOoO0 , isFolder = False )
 return iIii1
 if 33 - 33: iiiii11iII1 + II111iiii % i11iIiiIii . iIiiI1 - I1IiiI
def O00oooo0O ( txt ) :
 if 22 - 22: OoooooooOO % i1iIii1Ii1II - O0o . iIii1I11I1II1 * i11iIiiIii
 txt = txt . replace ( "&quot;" , "\"" )
 txt = txt . replace ( "&amp;" , "&" )
 txt = txt . replace ( u"\u2018" , "'" ) . replace ( u"\u2019" , "'" )
 txt = txt . strip ( )
 return txt
 if 32 - 32: Oo0Ooo * O0 % O0Oo0oO0o % iiiii11iII1 . I1i1I
def o0OOOOO00o0O0 ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 o0o0OOO0o0 = xbmcgui . Window ( id )
 ooOOOo0oo0O0 = 50
 while ( ooOOOo0oo0O0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   ooOOOo0oo0O0 -= 1
   o0o0OOO0o0 . getControl ( 1 ) . setLabel ( heading )
   o0o0OOO0o0 . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 71 - 71: OoOoo0 . O0
def o0OO0oo0oOO ( name , url , iconimage ) :
 if 54 - 54: I1IiiI % II111iiii % II111iiii
 iI1 = [ ]
 i11Iiii = [ ]
 iI = [ ]
 Oo0o0000o0o0 = i1I1Iiii1111 ( url )
 I1i1I1II = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( Oo0o0000o0o0 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( I1i1I1II ) [ 0 ]
 i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( I1i1I1II )
 IiIiiI = 1
 for I1I in i1 :
  oOO00oOO = I1I
  if '(' in I1I :
   I1I = I1I . split ( '(' ) [ 0 ]
   OoOo = str ( oOO00oOO . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iI1 . append ( I1I )
   i11Iiii . append ( OoOo )
  else :
   iI1 . append ( I1I )
   i11Iiii . append ( 'Link ' + str ( IiIiiI ) )
  IiIiiI = IiIiiI + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 iiIIIII1i1iI = xbmcgui . Dialog ( )
 iIo00O = iiIIIII1i1iI . select ( name , i11Iiii )
 if iIo00O < 0 :
  quit ( )
 else :
  url = iI1 [ iIo00O ]
  if 69 - 69: O0Oo0oO0o % OoOoo0 - o0oOOo0O0Ooo + OoOoo0 - O0 % OoooooooOO
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : Iii111II = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : Iii111II = liveresolver . resolve ( url )
  else : Iii111II = url
  oOOoO0 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  oOOoO0 . setPath ( Iii111II )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOoO0 )
  iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , i1i1II , 5000 )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
  if 9 - 9: OoO0O00
def i11O0oo0OO0oOOOo ( name , url , iconimage ) :
 if 35 - 35: I1i1I % I1IiiI
 iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , i1i1II , 5000 )
 if 70 - 70: O0o * I1ii11iIi11i
 import urlresolver
 if '.m3u8' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
  xbmc . Player ( ) . play ( url )
  quit ( )
  if 46 - 46: iIiiI1 / OoO0O00
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  Iii111II = urlresolver . HostedMediaFile ( url ) . resolve ( )
  iiIIIII1i1iI . ok ( "Debug" , str ( Iii111II ) )
  oOOoO0 = xbmcgui . ListItem ( name , iconImage = i1i1II , thumbnailImage = i1i1II )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 else :
  Iii111II = url
  oOOoO0 = xbmcgui . ListItem ( name , iconImage = i1i1II , thumbnailImage = i1i1II )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Link Dead, Please try another[/COLOR]' , i1i1II , 5000 )
  if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + iiiii11iII1 + iiiii11iII1 - o0oOOo0O0Ooo / OoOoo0
def I1IiIi11Ii1 ( name , url , iconimage ) :
 iIii1 = True
 oOOoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; oOOoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oOOoO0 )
 xbmc . Player ( ) . play ( url , oOOoO0 , False )
 if 50 - 50: II111iiii - iIiiI1 * I1ii11iIi11i / OoOoo0 + o0oOOo0O0Ooo
def O0O0O ( ) :
 if 83 - 83: I1ii11iIi11i / iIiiI1
 iIIIIii1 = xbmc . getInfoLabel ( "System.BuildVersion" )
 oo000OO00Oo = float ( iIIIIii1 [ : 4 ] )
 if oo000OO00Oo >= 11.0 and oo000OO00Oo <= 11.9 :
  O0OOO0OOoO0O = 'Eden'
 elif oo000OO00Oo >= 12.0 and oo000OO00Oo <= 12.9 :
  O0OOO0OOoO0O = 'Frodo'
 elif oo000OO00Oo >= 13.0 and oo000OO00Oo <= 13.9 :
  O0OOO0OOoO0O = 'Gotham'
 elif oo000OO00Oo >= 14.0 and oo000OO00Oo <= 14.9 :
  O0OOO0OOoO0O = 'Helix'
 elif oo000OO00Oo >= 15.0 and oo000OO00Oo <= 15.9 :
  O0OOO0OOoO0O = 'Isengard'
 elif oo000OO00Oo >= 16.0 and oo000OO00Oo <= 16.9 :
  O0OOO0OOoO0O = 'Jarvis'
 elif oo000OO00Oo >= 17.0 and oo000OO00Oo <= 17.9 :
  O0OOO0OOoO0O = 'Krypton'
 else : O0OOO0OOoO0O = "Decline"
 if 70 - 70: I1i1I * Oo0Ooo * i1iIii1Ii1II / iiiii11iII1
 if O0OOO0OOoO0O == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif O0OOO0OOoO0O == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 88 - 88: O0
 if 64 - 64: i1iIii1Ii1II * O0 + I1i1I - II1iI + i11iIiiIii * iiiii11iII1
def I1IiIi11Ii1 ( name , url , iconimage ) :
 iIii1 = True
 oOOoO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; oOOoO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIii1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oOOoO0 )
 xbmc . Player ( ) . play ( url , oOOoO0 , False )
 if 30 - 30: o0oOOo0O0Ooo . iiiii11iII1 - OoooooooOO
def Ii1iIiii1 ( url ) :
 if 91 - 91: OoO0O00 . I1ii11iIi11i + OoO0O00 - O0o / OoooooooOO
 iII1 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iII1 )
 sys . exit ( 1 )
 if 30 - 30: II111iiii - II1iI - i11iIiiIii % OoOoOO00 - II111iiii * iiiii11iII1
def oO00O0O0O ( text ) :
 if 31 - 31: i1iIii1Ii1II - II111iiii . i1iIii1Ii1II
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
 if 18 - 18: o0oOOo0O0Ooo
 return text
 if 98 - 98: O0o * O0o / O0o + i1iIii1Ii1II
def ii111111I1iII ( ) :
 if 68 - 68: O0o - iIii1I11I1II1 * i11iIiiIii / I1ii11iIi11i * OoOoo0
 i1iIi1iIi1i = o0oO0
 Oo0o0000o0o0 = i1I1Iiii1111 ( i1iIi1iIi1i )
 I1I1iIiII1 = re . compile ( '<item>(.+?)</item>' ) . findall ( Oo0o0000o0o0 )
 for i11i1I1 in I1I1iIiII1 :
  if '<folder>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<folder>(.+?)</folder>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 1 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<football>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = 'Football'
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 3 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<sportschans>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<sportschans>(.+?)</sportschans>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 5 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<nba>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<nba>(.+?)</nba>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 18 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<baseball>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<baseball>(.+?)</baseball>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 19 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<American>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<American>(.+?)</American>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<Rugby>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<Rugby>(.+?)</Rugby>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<WWE>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<WWE>(.+?)</WWE>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<UFC>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<UFC>(.+?)</UFC>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<Tennis>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<Tennis>(.+?)</Tennis>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<Boxing>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<Boxing>(.+?)</Boxing>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<Golf>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<Golf>(.+?)</Golf>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<Cricket>' in i11i1I1 :
   ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
   Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
   iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
   i1iIi1iIi1i = re . compile ( '<Cricket>(.+?)</Cricket>' ) . findall ( i11i1I1 ) [ 0 ]
   oo0Ooo0 ( ii1I , i1iIi1iIi1i , 20 , Oo0ooOo0o , iI1Ii11111iIi )
  elif '<sportsdevil>' in i11i1I1 :
   i1 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i11i1I1 )
   if len ( i1 ) == 1 :
    ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
    Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
    i1iIi1iIi1i = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i11i1I1 ) [ 0 ]
    Ii1i1 = 'None'
    iiIii = Ii1i1
    ooo0O = "/"
    if not iiIii . endswith ( ooo0O ) :
     oOoO0o00OO0 = iiIii + "/"
    else :
     oOoO0o00OO0 = iiIii
    Oo0o0000o0o0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + i1iIi1iIi1i
    i1iIi1iIi1i = Oo0o0000o0o0 + '%26referer=' + oOoO0o00OO0
    OooOoO0Oo ( ii1I , i1iIi1iIi1i , 4 , Oo0ooOo0o , IiII )
  else :
   i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( i11i1I1 )
   if len ( i1 ) == 1 :
    i1I1ii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i11i1I1 )
    oOOo0 = len ( I1I1iIiII1 )
    for ii1I , i1iIi1iIi1i , Oo0ooOo0o , iI1Ii11111iIi in i1I1ii :
     if 'youtube.com/playlist' in i1iIi1iIi1i :
      oo0Ooo0 ( ii1I , i1iIi1iIi1i , 2 , Oo0ooOo0o , iI1Ii11111iIi )
     else :
      OooOoO0Oo ( ii1I , i1iIi1iIi1i , 2 , Oo0ooOo0o , iI1Ii11111iIi )
   elif len ( i1 ) > 1 :
    ii1I = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
    Oo0ooOo0o = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
    iI1Ii11111iIi = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
    OooOoO0Oo ( ii1I , url2 , 3 , Oo0ooOo0o , iI1Ii11111iIi )
 if not os . path . exists ( oo00 ) :
  oo00O00oO = 'http://streamarmy.co.uk/sw.mp4'
  xbmc . Player ( ) . play ( oo00O00oO , xbmcgui . ListItem ( 'Welcome to Sports World' ) )
  os . makedirs ( oo00 )
  if 23 - 23: OoO0O00 + OoO0O00 . II1iI
 O0O0O ( )
 if 38 - 38: OoOoo0
def Ii1 ( name , url , iconimage , fanart ) :
 iiIIIII1i1iI = xbmcgui . Dialog ( )
 OOooOO000 = url
 Oo0o0000o0o0 = i1I1Iiii1111 ( url )
 I1I1iIiII1 = re . compile ( '<item>(.+?)</item>' ) . findall ( Oo0o0000o0o0 )
 for i11i1I1 in I1I1iIiII1 :
  try :
   if '<image>' in i11i1I1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( i11i1I1 ) [ 0 ]
    oo0Ooo0 ( name , url , 9 , iconimage , fanart )
   elif '<sportsdevil>' in i11i1I1 :
    i1 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i11i1I1 )
    if len ( i1 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( i11i1I1 ) [ 0 ]
     Ii1i1 = 'None'
     iiIii = Ii1i1
     ooo0O = "/"
     if not iiIii . endswith ( ooo0O ) :
      oOoO0o00OO0 = iiIii + "/"
     else :
      oOoO0o00OO0 = iiIii
     Oo0o0000o0o0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = Oo0o0000o0o0 + '%26referer=' + oOoO0o00OO0
     OooOoO0Oo ( name , url , 9 , iconimage , fanart )
   elif '<folder>' in i11i1I1 :
    i1I1ii = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i11i1I1 )
    for name , url , iconimage , fanart in i1I1ii :
     oo0Ooo0 ( name , url , 1 , iconimage , fanart )
     if 97 - 97: I1ii11iIi11i + II1iI / iIii1I11I1II1 / O0o
   else :
    i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( i11i1I1 )
    if len ( i1 ) == 1 :
     i1I1ii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( i11i1I1 )
     oOOo0 = len ( I1I1iIiII1 )
     for name , url , iconimage , fanart in i1I1ii :
      if 'youtube.com/playlist' in url :
       oo0Ooo0 ( name , url , 2 , iconimage , fanart )
      else :
       OooOoO0Oo ( "[COLOR red][B]" + name + "[/B][/COLOR]" , url , 2 , iconimage , fanart )
    elif len ( i1 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( i11i1I1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11i1I1 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( i11i1I1 ) [ 0 ]
     OooOoO0Oo ( name , OOooOO000 , 10 , iconimage , fanart )
  except : pass
 O0O0O ( )
 if 37 - 37: O0o - iIiiI1 * O0Oo0oO0o % i11iIiiIii - OoOoo0
def o0oO ( ) :
 if 1 - 1: OoO0O00 - O0Oo0oO0o . i1iIii1Ii1II . OoO0O00 / Oo0Ooo + i1iIii1Ii1II
 file = xbmc . translatePath ( "special://home/kodi.log" )
 Ooo = open ( file ) . read ( )
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 o0o0OOO0o0 = xbmcgui . Window ( id )
 ooOOOo0oo0O0 = 50
 while ( ooOOOo0oo0O0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   ooOOOo0oo0O0 -= 1
   o0o0OOO0o0 . getControl ( 1 ) . setLabel ( Iii1ii1II11i )
   o0o0OOO0o0 . getControl ( 5 ) . setText ( Ooo )
   return
   quit ( )
  except : pass
  if 62 - 62: II1iI / OoO0O00 + iiiii11iII1 / OoO0O00 . II111iiii
def ooOOoooooo ( ) :
 if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % O0o * I1i1I . i11iIiiIii
 iiIIIII1i1iI = xbmcgui . Dialog ( )
 III1Iiii1I11 = iiIIIII1i1iI . select ( '[COLOR lime]Choose A Source[/COLOR]' , [ '[COLOR lime]SoccerStreams [COLOR yellow]( LIVE GAMES )[/COLOR]' , '[COLOR lime]WizHD [COLOR yellow]( LIVE GAMES )[/COLOR]' , '[COLOR white]---------------------[/COLOR]' , '[COLOR lime]Football Highlights[/COLOR]' ] )
 if III1Iiii1I11 == 0 :
  IIII ( )
 if III1Iiii1I11 == 1 :
  i1iIi1iIi1i = 'Football'
  iiIiI ( i1iIi1iIi1i )
 if III1Iiii1I11 == 3 :
  o00oooO0Oo ( i1iIi1iIi1i )
  if 78 - 78: iiiii11iII1 % OoOoo0 + I1ii11iIi11i
def o00oooO0Oo ( url ) :
 if 64 - 64: O0Oo0oO0o * O0 . I1IiiI + II111iiii
 if not 'page/' in url :
  url = 'http://www.sportp2p.com/highlights/'
 Oo0o0000o0o0 = i1I1Iiii1111 ( url )
 I1I1iIiII1 = re . compile ( '<td class="contact" width="60%">(.+?)</td>' ) . findall ( Oo0o0000o0o0 )
 IIi1i = 0
 for i1 in I1I1iIiII1 :
  I1i1iiI1 . create ( "[COLOR lime]Footie Highlights[/COLOR]" , '[COLOR lime]' + "Searching For Highlights" + "[/COLOR]" )
  I1i1iiI1 . update ( 0 )
  OOOO00O0O = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( i1 ) [ 0 ]
  I1i1iiI1 . update ( 100 , '[COLOR lime]Found Highlights For [COLOR yellow]%s[/COLOR]' % str ( OOOO00O0O ) , '[COLOR yellow]%s[COLOR lime] Games In Total Found[/COLOR]' % str ( IIi1i ) )
  IIi1i += 1
  time . sleep ( 0.20 )
  url = re . compile ( '<a href="(.+?)"' ) . findall ( i1 ) [ 0 ]
  url = 'http://www.sportp2p.com' + url
  OooOoO0Oo ( '[COLOR lime]' + OOOO00O0O + '[/COLOR]' , url , 12 , Oo0ooOo0o , iI1Ii11111iIi )
  if 33 - 33: O0 . I1i1I . I1IiiI
 try :
  OoOO = re . compile ( '<td align="left" width="45%"><b><a href="(.+?)">' ) . findall ( Oo0o0000o0o0 ) [ 0 ]
  ooOOO0 = 'http://www.sportp2p.com' + OoOO
  oo0Ooo0 ( '[COLOR red]' + 'Next Page ------>' + '[/COLOR]' , ooOOO0 , 13 , Oo0ooOo0o , iI1Ii11111iIi )
 except : pass
 if 65 - 65: O0
def oO00OOoO00 ( url ) :
 if 40 - 40: I1IiiI * iiiii11iII1 + II1iI % O0o
 Oo0o0000o0o0 = i1I1Iiii1111 ( url )
 try :
  url = re . compile ( '<iframe width=.+?src="(.+?)"' ) . findall ( Oo0o0000o0o0 ) [ 0 ]
  url = devilcheck . Devil_Checker ( url )
 except IndexError :
  url = re . compile ( '<script data-config="(.+?)"' ) . findall ( Oo0o0000o0o0 ) [ 0 ]
  url = 'http:' + url
  url = devilcheck . Devil_Checker ( url )
 iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Attempting To Resolve Link Now[/COLOR]' , i1i1II , 5000 )
 import urlresolver
 if '.m3u8' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + ii1I + '&amp;url=' + url + '&amp;iconImage=' + Oo0ooOo0o
  xbmc . Player ( ) . play ( url )
  quit ( )
  if 74 - 74: O0Oo0oO0o - Oo0Ooo + OoooooooOO + OoOoo0 / OoOoOO00
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  Iii111II = urlresolver . HostedMediaFile ( url ) . resolve ( )
  iiIIIII1i1iI . ok ( "Debug" , str ( Iii111II ) )
  oOOoO0 = xbmcgui . ListItem ( ii1I , iconImage = i1i1II , thumbnailImage = i1i1II )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 else :
  Iii111II = url
  oOOoO0 = xbmcgui . ListItem ( ii1I , iconImage = i1i1II , thumbnailImage = i1i1II )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
  time . sleep ( 2 )
  quit ( )
 if not xbmc . Player ( ) . isPlaying ( ) :
  iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Link Dead, Please try another[/COLOR]' , i1i1II , 5000 )
  if 23 - 23: O0
  if 85 - 85: iiiii11iII1
  if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + iiiii11iII1 % OoooooooOO % OoO0O00
def IIII ( ) :
 if 42 - 42: OoO0O00 / i1iIii1Ii1II / o0oOOo0O0Ooo + O0o / OoOoOO00
 i1iIi1iIi1i = 'https://soccerstreams.net/'
 Oo0o0000o0o0 = i1I1Iiii1111 ( i1iIi1iIi1i )
 I1I1iIiII1 = re . compile ( '<div class="col-md-5 text-right">(.+?)</a>' ) . findall ( Oo0o0000o0o0 )
 I1i1iiI1 . create ( "[COLOR lime]Soccer Streams[/COLOR]" , '[COLOR lime]' + "Searching For Matches" + "[/COLOR]" )
 I1i1iiI1 . update ( 0 )
 IiIiiI = 0
 IIi1i = 0
 o0OoOO000ooO0 = [ ]
 o0o0o0oO0oOO = [ ]
 ii1Ii11I = [ ]
 i1iIi1iIi1i = [ ]
 for i1 in I1I1iIiII1 :
  o00o0 = re . compile ( 'alt="(.+?)"' ) . findall ( i1 ) [ 0 ]
  ii = re . compile ( 'alt="(.+?)"' ) . findall ( i1 ) [ 1 ]
  OOooooO0Oo = re . compile ( '<a href="(.+?)"' ) . findall ( i1 ) [ 0 ]
  I1i1iiI1 . update ( 100 , '[COLOR lime]Searching For Matches :: Found [COLOR yellow]%s[COLOR lime] Matches So Far' % str ( IiIiiI ) , '[COLOR yellow]%s[COLOR lime] Of Them Have Links Available' "[/COLOR]" % str ( IIi1i ) )
  time . sleep ( 0.07 )
  IiIiiI += 1
  try :
   OO = re . compile ( '<span class="count">(.+?)</span>' ) . findall ( i1 ) [ 0 ]
   o0OoOO000ooO0 . append ( o00o0 )
   o0o0o0oO0oOO . append ( ii )
   ii1Ii11I . append ( OO )
   i1iIi1iIi1i . append ( OOooooO0Oo )
   IIi1i += 1
  except : IndexError
  iIiIIi1 = list ( zip ( o0OoOO000ooO0 , o0o0o0oO0oOO , ii1Ii11I , i1iIi1iIi1i ) )
 I1i1iiI1 . close ( )
 I1i1iiI1 . create ( Iii1ii1II11i , '' , '' , '' )
 I1i1iiI1 . update ( 0 )
 I1i1iiI1 . update ( 100 , '[COLOR yellow]Here Are Your Results' , 'We Found %s Matches In Total' % str ( IiIiiI ) , '[COLOR lime]%s Have Links Available[/COLOR]' % str ( IIi1i ) )
 time . sleep ( 2 )
 I1i1iiI1 . close ( )
 for o00o0 , ii , ii1Ii11I , i1iIi1iIi1i in iIiIIi1 :
  o00o0 = oO00O0O0O ( o00o0 )
  ii = oO00O0O0O ( ii )
  if ii1Ii11I :
   oo0Ooo0 ( "[COLOR lime][B]" + o00o0 + "[COLOR yellow] vs [COLOR lime]" + ii + "[COLOR red] " + ii1Ii11I + " Links Found" + "[/B][/COLOR]" , i1iIi1iIi1i , 16 , i1i1II , iI1Ii11111iIi , '' )
   if 7 - 7: iIiiI1 - Oo0Ooo - O0Oo0oO0o + iIiiI1
def iI1I11iiI1i ( url ) :
 if 78 - 78: O0Oo0oO0o % O0 % iiiii11iII1
 Oo0o0000o0o0 = i1I1Iiii1111 ( url )
 I1I1iIiII1 = re . compile ( '<div class="stream_comments parent_comment hidden" >(.+?)</span>' ) . findall ( Oo0o0000o0o0 )
 IiIiiI = 0
 IIi1i = 0
 iiI1Ii1iI1 = [ ]
 oO0O0OO0O = [ ]
 OOOoOoO = [ ]
 for i1 in I1I1iIiII1 :
  url = re . compile ( 'data-href="(.+?)"' ) . findall ( i1 ) [ 0 ]
  I1i1iiI1 . create ( Iii1ii1II11i , '[COLOR lime]Checking If The [COLOR yellow]%s[COLOR lime] Links Found Are Supported' % str ( IiIiiI ) , '[COLOR yellow]%s[COLOR lime] Links Are Supported![/COLOR]' % str ( IIi1i ) )
  I1i1iiI1 . update ( 0 )
  url = devilcheck . Devil_Checker ( url )
  time . sleep ( 0.07 )
  IiIiiI += 1
  Ii1I1i = re . compile ( 'data-quality="(.+?)"' ) . findall ( i1 ) [ 0 ]
  OOI1iI1ii1II = re . compile ( 'data-language="(.+?)"' ) . findall ( i1 ) [ 0 ]
  if url :
   IIi1i += 1
   OooOoO0Oo ( "[COLOR lime]Link " + str ( IiIiiI ) + "   " "[COLOR yellow]" + Ii1I1i + "[COLOR red]" + "   " + "[COLOR white]" + OOI1iI1ii1II + "[/COLOR]" , url , 17 , i1i1II , iI1Ii11111iIi , '' )
 if IIi1i == 0 :
  iiIIIII1i1iI . notification ( Iii1ii1II11i , '[COLOR red]Sorry The Links Found Are Not Supported[/COLOR]' , i1i1II , 5000 )
  quit ( )
  if 57 - 57: OoOoo0 % iiiii11iII1 + o0oOOo0O0Ooo - Oo0Ooo
def iiIiI ( url ) :
 if 65 - 65: i1iIii1Ii1II . OoOoOO00
 if url == 'Football' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Football' )
 elif url == 'American' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/NFL' )
 elif url == 'Rugby' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Rugby' )
 elif url == 'WWE' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/WWE' )
 elif url == 'UFC' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/UFC' )
 elif url == 'Tennis' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Tennis' )
 elif url == 'Boxing' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Boxing' )
 elif url == 'Golf' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Golf' )
 elif url == 'Cricket' :
  IiI1i = i1I1Iiii1111 ( 'http://wizhdsports.is/sport/Cricket' )
 o0O = dom_parser2 . parse_dom ( IiI1i , 'div' , { 'class' : 'card' } )
 o0O = [ ( dom_parser2 . parse_dom ( IiIiiI , 'div' , { 'class' : 'col-md-6' } ) ,
 dom_parser2 . parse_dom ( IiIiiI , 'div' , { 'class' : 'col-md-2' } ) ,
 dom_parser2 . parse_dom ( IiIiiI , 'font' , { 'color' : re . compile ( '.+?' ) } ) ,
 dom_parser2 . parse_dom ( IiIiiI , 'div' , { 'class' : re . compile ( 'card-block\sdrop_box' ) } ) ) for IiIiiI in o0O ]
 if len ( o0O ) < 1 :
  OooOoO0Oo ( "[COLOR lime][B]" + "No Events At The Moment, Please Try Later" + "[/B][/COLOR]" , url , 4 , Oo0ooOo0o , IiII , '' )
 o0O = [ ( IiIiiI [ 0 ] [ 0 ] . content , re . sub ( '<.+?>' , '' , IiIiiI [ 1 ] [ 0 ] . content ) , re . sub ( '<.+?>' , '' , IiIiiI [ 1 ] [ 1 ] . content ) , re . sub ( '<.+?>' , '' , IiIiiI [ 2 ] [ 0 ] . content ) if IiIiiI [ 2 ] else 'Upcoming' , IiIiiI [ 3 ] [ 0 ] . content ) for IiIiiI in o0O ]
 if 90 - 90: II1iI . I1IiiI * I1IiiI
 if 7 - 7: I1i1I * OoOoo0 % iiiii11iII1 - o0oOOo0O0Ooo
 if 13 - 13: iiiii11iII1 . i11iIiiIii
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 o0O = [ ( IiIiiI [ 0 ] , IiIiiI [ 1 ] , IiIiiI [ 2 ] , IiIiiI [ 3 ] , IiIiiI [ 4 ] ) for IiIiiI in o0O ]
 O00o0OO0 = 0
 IIi1I1iiiii = 0
 I1i1iiI1 . create ( "[COLOR lime]WizHD[/COLOR]" , '[COLOR lime]' + "Searching For Matches" + "[/COLOR]" )
 I1i1iiI1 . update ( 0 )
 for IiIiiI in o0O :
  o00oOOooOOo0o = IiIiiI [ 0 ]
  I1i1iiI1 . update ( 100 , '[COLOR lime]Searching For Matches :: Found [COLOR yellow]%s[COLOR lime] Matches So Far[/COLOR]' % str ( O00o0OO0 ) )
  O00o0OO0 += 1
  time . sleep ( 0.10 )
  o00oOOooOOo0o = iI11 ( o00oOOooOOo0o )
  O0O0ooOOO = IiIiiI [ 1 ]
  oOOo0O00o = IiIiiI [ 3 ]
  if 'Match Over' in oOOo0O00o :
   IIi1I1iiiii += 1
  iIiIi11 = dom_parser2 . parse_dom ( IiIiiI [ 4 ] , 'a' )
  for IiI1i in iIiIi11 :
   OOO = re . sub ( '<.+?>' , '' , IiI1i . content )
   Oo0o0000o0o0 = IiI1i . attrs [ 'href' ]
   Oo0o0000o0o0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + Oo0o0000o0o0
   if not 'Match Over' in oOOo0O00o :
    OooOoO0Oo ( '[COLOR lime]' + o00oOOooOOo0o + '[COLOR yellow]' + ' ' + oOOo0O00o + '[/COLOR]' , Oo0o0000o0o0 , 2 , Oo0ooOo0o , iI1Ii11111iIi )
 I1i1iiI1 . update ( 100 , '[COLOR lime]Here Are Your Results' , 'We Found [COLOR yellow] %s [COLOR lime]Matches In Total' % str ( O00o0OO0 ) , '[COLOR yellow]%s[COLOR lime] Have Ended So Have Been Removed From Listings[/COLOR]' % str ( IIi1I1iiiii ) )
 time . sleep ( 3 )
 I1i1iiI1 . close ( )
 if 32 - 32: i1IIi / II111iiii . Oo0Ooo
 if 62 - 62: OoooooooOO * I1IiiI
def oOOOoo0O0oO ( url ) :
 if 6 - 6: II1iI * o0oOOo0O0Ooo + O0o
 I1i1iiI1 . create ( Iii1ii1II11i , "[COLOR yellow]Generating link...[/COLOR]" , '[COLOR red]Please wait...[/COLOR]' , '' )
 I1i1iiI1 . update ( 0 )
 time . sleep ( 1 )
 import liveresolver
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  Iii111II = urlresolver . HostedMediaFile ( url ) . resolve ( )
  oOOoO0 = xbmcgui . ListItem ( ii1I , iconImage = Oo0ooOo0o , thumbnailImage = Oo0ooOo0o )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
 elif liveresolver . isValid ( url ) == True :
  url = liveresolver . resolve ( url )
  oOOoO0 = xbmcgui . ListItem ( ii1I , iconImage = Oo0ooOo0o , thumbnailImage = Oo0ooOo0o )
  oOOoO0 . setPath ( Iii111II )
  xbmc . Player ( ) . play ( Iii111II , oOOoO0 , False )
 else :
  if '.m3u8' in url :
   I1IIIiIiI1 = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + ii1I + '&amp;url=' + url + '&amp;iconImage=' + Oo0ooOo0o
  elif '.ts' in url :
   I1IIIiIiI1 = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + ii1I + '&amp;url=' + url + '&amp;iconImage=' + Oo0ooOo0o
  elif 'rtmp://' in url :
   xbmc . Player ( ) . play ( url )
   quit ( )
  else :
   I1IIIiIiI1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + url + '%26referer=https://soccerstreams.net'
   if 28 - 28: iIii1I11I1II1 % Oo0Ooo * I1IiiI % iiiii11iII1 * o0oOOo0O0Ooo / o0oOOo0O0Ooo
  oOOoO0 = xbmcgui . ListItem ( ii1I , iconImage = Oo0ooOo0o , thumbnailImage = Oo0ooOo0o )
  oOOoO0 . setPath ( url )
  if 5 - 5: I1IiiI
  xbmc . Player ( ) . play ( I1IIIiIiI1 , oOOoO0 , False )
  if 48 - 48: o0oOOo0O0Ooo - O0Oo0oO0o / OoooooooOO
def OO0O0 ( ) :
 if 30 - 30: II1iI + I1ii11iIi11i * i1iIii1Ii1II % i11iIiiIii % OoOoOO00
 i1iIi1iIi1i = 'http://www.liveonlinetv247.info/tvchannels.php'
 Oo0o0000o0o0 = i1I1Iiii1111 ( i1iIi1iIi1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I1I1iIiII1 = re . compile ( '<h2>Sports Channels</h2>(.+?)</table>' ) . findall ( Oo0o0000o0o0 ) [ 0 ]
 OO0OoOO0o0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I1I1iIiII1 )
 for i1iIi1iIi1i , OOOO00O0O in OO0OoOO0o0o :
  i1iIi1iIi1i = i1iIi1iIi1i . replace ( ' ' , '%20' )
  OOOO00O0O = OOOO00O0O . replace ( '<b>' , '' ) . replace ( '</b>' , '' )
  I1IIIiIiI1 = 'http://www.liveonlinetv247.info' + i1iIi1iIi1i
  oo = i1I1Iiii1111 ( I1IIIiIiI1 )
  I1111i = re . compile ( '</h4>(.+?)</a>' ) . findall ( oo ) [ 0 ]
  iIIii = re . compile ( '<a href="(.+?)"' ) . findall ( I1111i ) [ 0 ]
  I1i1iiI1 . create ( Iii1ii1II11i , '[COLOR lime]We Found[COLOR yellow] %s[/COLOR] adding it now to our list now[/COLOR]' % str ( OOOO00O0O ) )
  I1i1iiI1 . update ( 100 )
  i1iIi1iIi1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=%26url=' + iIIii
  time . sleep ( 0.07 )
  OooOoO0Oo ( '[COLOR lime]' + OOOO00O0O + '[/COLOR]' , i1iIi1iIi1i , 4 , Oo0ooOo0o , iI1Ii11111iIi )
  if 92 - 92: iiiii11iII1 + O0Oo0oO0o % II1iI
def oOo0 ( ) :
 if 30 - 30: i1iIii1Ii1II / I1IiiI
 i1iIi1iIi1i = 'http://nba-stream.com/next-games/'
 Oo0o0000o0o0 = i1I1Iiii1111 ( i1iIi1iIi1i )
 I1I1iIiII1 = re . compile ( '<div itemscope itemtype="http://data-vocabulary.org/Event"(.+?)</span>' ) . findall ( Oo0o0000o0o0 )
 if len ( I1I1iIiII1 ) < 1 :
  OooOoO0Oo ( "[COLOR lime][B]" + "No Games At The Moment, Please Try Later" + "[/B][/COLOR]" , i1iIi1iIi1i , 4 , Oo0ooOo0o , IiII , '' )
 for i1 in I1I1iIiII1 :
  OOOO00O0O = re . compile ( 'title="(.+?)"' ) . findall ( i1 ) [ 0 ] . replace ( 'Watch' , '' ) . replace ( 'Live Stream' , '' ) . strip ( )
  i1iIi1iIi1i = re . compile ( 'href="(.+?)"' ) . findall ( i1 ) [ 0 ]
  i1iIi1iIi1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + i1iIi1iIi1i + '%26referer=no'
  time = re . compile ( 'datetime="(.+?)"' ) . findall ( i1 ) [ 0 ] . replace ( 'T' , ' :: ' )
  i1i1II = 'https://www.irononsticker.net/images/NBA/STK-NBA-NBA-P1971-01.jpg'
  OooOoO0Oo ( "[COLOR lime][B]" + OOOO00O0O + " :: " + time + "[/B][/COLOR]" , i1iIi1iIi1i , 4 , i1i1II , iI1Ii11111iIi , '' )
  if 35 - 35: II111iiii % II1iI . iIiiI1 + iIiiI1 % II111iiii % II111iiii
def ooOoO00 ( ) :
 if 14 - 14: i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
 i1iIi1iIi1i = 'http://nba-stream.com/next-games/'
 Oo0o0000o0o0 = i1I1Iiii1111 ( i1iIi1iIi1i )
 I1I1iIiII1 = re . compile ( '<div class="match-info">(.+?)</div>' ) . findall ( Oo0o0000o0o0 )
 for i1 in I1I1iIiII1 :
  OOOO00O0O = re . compile ( '<b>(.+?)</b>' ) . findall ( i1 ) [ 0 ]
  i1iIi1iIi1i = re . compile ( 'href="(.+?)"' ) . findall ( i1 ) [ 0 ]
  time = re . compile ( '<i class="match-date">(.+?)</i>' ) . findall ( i1 ) [ 0 ]
  OOOO00O0O = oO00O0O0O ( OOOO00O0O )
  i1iIi1iIi1i = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + i1iIi1iIi1i + '%26referer=no'
  if not 'motorsports' in i1iIi1iIi1i :
   i1i1II = 'https://www.irononsticker.net/images/nhl/STK-MLB-MLB-P1970-01.jpg'
   OooOoO0Oo ( "[COLOR lime][B]" + OOOO00O0O + " :: " + time + "[/B][/COLOR]" , i1iIi1iIi1i , 4 , i1i1II , iI1Ii11111iIi , '' )
   if 72 - 72: iiiii11iII1
def II11Ii1iI1iII ( ) :
 Oo0o00OO0000 = [ ]
 I1i = sys . argv [ 2 ]
 if len ( I1i ) >= 2 :
  O00Oooo = sys . argv [ 2 ]
  i11I = O00Oooo . replace ( '?' , '' )
  if ( O00Oooo [ len ( O00Oooo ) - 1 ] == '/' ) :
   O00Oooo = O00Oooo [ 0 : len ( O00Oooo ) - 2 ]
  o00Oo0oooooo = i11I . split ( '&' )
  Oo0o00OO0000 = { }
  for IiIiiI in range ( len ( o00Oo0oooooo ) ) :
   O0oO0 = { }
   O0oO0 = o00Oo0oooooo [ IiIiiI ] . split ( '=' )
   if ( len ( O0oO0 ) ) == 2 :
    Oo0o00OO0000 [ O0oO0 [ 0 ] ] = O0oO0 [ 1 ]
 return Oo0o00OO0000
 if 7 - 7: I1IiiI
O00Oooo = II11Ii1iI1iII ( ) ; i1iIi1iIi1i = None ; ii1I = None ; I1ii1iIiii1I = None ; IIIii11 = None ; Oo0ooOo0o = None
try : IIIii11 = urllib . unquote_plus ( O00Oooo [ "site" ] )
except : pass
try : i1iIi1iIi1i = urllib . unquote_plus ( O00Oooo [ "url" ] )
except : pass
try : ii1I = urllib . unquote_plus ( O00Oooo [ "name" ] )
except : pass
try : I1ii1iIiii1I = int ( O00Oooo [ "mode" ] )
except : pass
try : Oo0ooOo0o = urllib . unquote_plus ( O00Oooo [ "iconimage" ] )
except : pass
try : iI1Ii11111iIi = urllib . unquote_plus ( O00Oooo [ "fanart" ] )
except : pass
if 9 - 9: O0 % O0 - o0oOOo0O0Ooo
if I1ii1iIiii1I == None or i1iIi1iIi1i == None or len ( i1iIi1iIi1i ) < 1 : ii111111I1iII ( )
if 51 - 51: I1IiiI . iIii1I11I1II1 - I1ii11iIi11i / O0
elif I1ii1iIiii1I == 1 : Ii1 ( ii1I , i1iIi1iIi1i , Oo0ooOo0o , iI1Ii11111iIi )
elif I1ii1iIiii1I == 2 : i11O0oo0OO0oOOOo ( ii1I , i1iIi1iIi1i , Oo0ooOo0o )
elif I1ii1iIiii1I == 3 : ooOOoooooo ( )
elif I1ii1iIiii1I == 4 : I1IiIi11Ii1 ( ii1I , i1iIi1iIi1i , Oo0ooOo0o )
elif I1ii1iIiii1I == 5 : OO0O0 ( )
elif I1ii1iIiii1I == 7 : PLAYVIDEO ( i1iIi1iIi1i )
elif I1ii1iIiii1I == 9 : I1IiIi11Ii1 ( ii1I , i1iIi1iIi1i , Oo0ooOo0o )
elif I1ii1iIiii1I == 10 : o0OO0oo0oOO ( ii1I , i1iIi1iIi1i , Oo0ooOo0o )
elif I1ii1iIiii1I == 11 : GET_M3U ( ii1I , i1iIi1iIi1i , Oo0ooOo0o )
elif I1ii1iIiii1I == 12 : oO00OOoO00 ( i1iIi1iIi1i )
elif I1ii1iIiii1I == 13 : o00oooO0Oo ( i1iIi1iIi1i )
if 52 - 52: o0oOOo0O0Ooo + O0 + O0o + Oo0Ooo % O0o
elif I1ii1iIiii1I == 15 : IIII ( )
elif I1ii1iIiii1I == 16 : iI1I11iiI1i ( i1iIi1iIi1i )
elif I1ii1iIiii1I == 17 : oOOOoo0O0oO ( i1iIi1iIi1i )
elif I1ii1iIiii1I == 18 : oOo0 ( )
elif I1ii1iIiii1I == 19 : ooOoO00 ( )
elif I1ii1iIiii1I == 20 : iiIiI ( i1iIi1iIi1i )
if 75 - 75: I1IiiI . iIiiI1 . O0 * OoOoo0
if 4 - 4: iiiii11iII1 % O0Oo0oO0o * OoO0O00
if 100 - 100: OoOoo0 * II1iI + II1iI
if I1ii1iIiii1I == None or i1iIi1iIi1i == None or len ( i1iIi1iIi1i ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 54 - 54: OoooooooOO + o0oOOo0O0Ooo - i1IIi % i11iIiiIii
if 3 - 3: o0oOOo0O0Ooo % o0oOOo0O0Ooo
if 83 - 83: II111iiii + OoOoo0
if 73 - 73: O0o
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
