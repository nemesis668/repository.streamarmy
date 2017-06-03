import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , json , os , re , sys , datetime , time , shutil , random , hashlib
from resources . libs . common_addon import Addon
import base64
import HTMLParser
from metahandler import metahandlers
import os
if 64 - 64: i11iIiiIii
OO0o = 'plugin.audio.beatz'
Oo0Ooo = Addon ( OO0o , sys . argv )
O0O0OO0O0O0 = xbmcaddon . Addon ( id = OO0o )
iiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'fanart.jpg' ) )
ooo0OO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'fanart.jpg' ) )
II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'icon.png' ) )
O00ooooo00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'search.jpg' ) )
I1IiiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o , 'next.png' ) )
IIi1IiiiI1Ii = base64 . b64decode ( b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2JURWJtR3Rx' )
I11i11Ii = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
oO00oOo = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
OOOo0 = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
Oooo000o = '&part=snippet&playlistId='
IiIi11iIIi1Ii = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
Oo0O = O0O0OO0O0O0 . getSetting ( 'enable_meta' )
IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + OO0o ) )
ooOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + OO0o ) )
Oo = xbmc . translatePath ( os . path . join ( ooOo , 'favourites.xml' ) )
o0O = 'http://pastebin.com/raw/4B2BhvJz'
IiiIII111iI = base64 . b64decode ( b'aHR0cDovL3N0cmVhbWFybXkub2Zmc2hvcmVwYXN0ZWJpbi5jb20vTWFpbi95b3V0dWJlLnBocA==' )
IiII = xbmcgui . Dialog ( )
iI1Ii11111iIi = xbmcgui . DialogProgress ( )
i1i1II = "[COLOR red][B]Beatz By Stream Army[/B][/COLOR]"
O0oo0OO0 = base64 . b64decode ( b'ZDBmYWY4MzNlMzVmYzZmYzU2MzVjODUxNTllMTYyMTA=' )
if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
if 12 - 12: o0oOoO00o
if 43 - 43: O0OOo . II1Iiii1111i
if 25 - 25: OOo000
def O0 ( text ) :
 if 34 - 34: O0o00 % o0ooo / OOO0O / I1ii * oOOOo0o0O + OOoOoo00oo
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
 text = text . replace ( '&apos;' , "'" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 if 41 - 41: i11IiIiiIIIII / IiiIII111ii / i1iIIi1
 return text
 if 50 - 50: IiIi1Iii1I1 - O00O0O0O0
def ooO0O ( url ) :
 if 63 - 63: o0oOoO00o . o0oOoO00o
 Ii1 = oOOoO0 ( url )
 O0OoO000O0OO ( '[B][COLOR aqua]B[COLOR white]eatZ[/B] [B][COLOR aqua]B[COLOR white]y [COLOR aqua]S[COLOR white]tream [COLOR aqua]A[COLOR white]rmy[/COLOR][/B]' , Ii1 )
 if 23 - 23: i11iIiiIii + O0OOo
 if 68 - 68: O0o00 . I1ii . i11iIiiIii
def II ( ) :
 if 14 - 14: II1Iiii1111i . O0OOo / i11IiIiiIIIII
 if 38 - 38: o0oOoO00o % i11iIiiIii . O00O0O0O0 - oOOOo0o0O + i11IiIiiIIIII
 if 66 - 66: i111I * i111I . oOOOo0o0O . II1Ii1iI1i - oOOOo0o0O
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 o0o00ooo0 = IIi1IiiiI1Ii
 oo0Oo00Oo0 = oOOO00o ( IIi1IiiiI1Ii )
 O0O00o0OOO0 = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0Oo00Oo0 )
 if 27 - 27: oooO0oo0oOOOO % II1Ii1iI1i * I1ii + i11iIiiIii + i111I * II1Ii1iI1i
 for o0oo0o0O00OO in O0O00o0OOO0 :
  try :
   if '<folder>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    I1i1iii = re . compile ( '<folder>(.+?)</folder>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , I1i1iii , 1 , i1iiI11I , iiiii )
   elif '<top40>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<top40>(.+?)</top40>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , o0o00ooo0 , 3 , i1iiI11I , iiiii )
   elif '<lastfm>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<lastfm>(.+?)</lastfm>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , o0o00ooo0 , 12 , i1iiI11I , iiiii )
   elif '<disney>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<disney>(.+?)</disney>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , o0o00ooo0 , 22 , i1iiI11I , iiiii )
   elif '<search>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<search>(.+?)</search>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , 'None' , 20 , i1iiI11I , iiiii )
   elif '<changelog>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<changelog>(.+?)</changelog>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    oO0o0O0OOOoo0 ( o0oO , o0o00ooo0 , 19 , i1iiI11I , iiiii )
   elif '<radio>' in o0oo0o0O00OO :
    o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    o0o00ooo0 = re . compile ( '<radio>(.+?)</radio>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( o0oO , o0o00ooo0 , 5 , i1iiI11I , iiiii )
   else :
    IiIiiI = re . compile ( '<link>(.+?)</link>' ) . findall ( o0oo0o0O00OO )
    if len ( IiIiiI ) == 1 :
     I1I = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO )
     oOO00oOO = len ( O0O00o0OOO0 )
     for o0oO , o0o00ooo0 , i1iiI11I , iiiii in I1I :
      if 'youtube.com/playlist' in o0o00ooo0 :
       iiii ( o0oO , o0o00ooo0 , 2 , i1iiI11I , iiiii )
      else :
       OoOo ( o0oO , o0o00ooo0 , 2 , i1iiI11I , iiiii )
    elif len ( IiIiiI ) > 1 :
     o0oO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     i1iiI11I = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     iiiii = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     OoOo ( o0oO , I1i1iii , 3 , i1iiI11I , iiiii )
     if 18 - 18: i11iIiiIii
     if 46 - 46: II1Ii1iI1i / OOoOoo00oo % oOOOo0o0O + IiIi1Iii1I1
  except : pass
  if 79 - 79: IiIi1Iii1I1 - o0ooo + IiIi1Iii1I1 - IiiIII111ii
  if 8 - 8: O0OOo
 Oo000 ( )
 if 51 - 51: i11iIiiIii . O0OOo + o0oOoO00o
 if 10 - 10: OOO0O * O00O0O0O0 * o0oOoO00o % i11IiIiiIIIII . oOOOo0o0O + IiIi1Iii1I1
def IIiIi11i1 ( name , url , iconimage , fanart ) :
 I1i1iii = url
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<item>(.+?)</item>' ) . findall ( oo0Oo00Oo0 )
 for o0oo0o0O00OO in O0O00o0OOO0 :
  try :
   if '<folder>' in o0oo0o0O00OO :
    I1I = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO )
    for name , url , iconimage , fanart in I1I :
     iiii ( name , url , 1 , iconimage , fanart )
   elif '<pumpyouup>' in o0oo0o0O00OO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    url = re . compile ( '<pumpyouup>(.+?)</pumpyouup>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( name , url , 9 , iconimage , fanart )
   elif '<summer2016>' in o0oo0o0O00OO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    url = re . compile ( '<summer2016>(.+?)</summer2016>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( name , url , 10 , iconimage , fanart )
   elif '<70S80S90S>' in o0oo0o0O00OO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    url = re . compile ( '<70S80S90S>(.+?)</70S80S90S>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( name , url , 11 , iconimage , fanart )
   elif '<random>' in o0oo0o0O00OO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    url = re . compile ( '<random>(.+?)</random>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( name , url , 15 , iconimage , fanart )
   elif '<album1>' in o0oo0o0O00OO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    url = re . compile ( '<album1>(.+?)</album1>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
    iiii ( name , url , 17 , iconimage , fanart )
   else :
    IiIiiI = re . compile ( '<link>(.+?)</link>' ) . findall ( o0oo0o0O00OO )
    if len ( IiIiiI ) == 1 :
     I1I = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO )
     oOO00oOO = len ( O0O00o0OOO0 )
     for name , url , iconimage , fanart in I1I :
      if 'youtube.com/playlist' in url :
       iiii ( name , url , 2 , iconimage , fanart )
      else :
       OoOo ( name , url , 2 , iconimage , fanart )
    elif len ( IiIiiI ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( o0oo0o0O00OO ) [ 0 ]
     OoOo ( name , I1i1iii , 3 , iconimage , fanart )
  except : pass
 Oo000 ( )
 if 29 - 29: OOO0O % O0OOo + O00O0O0O0 / o0ooo + oOOOo0o0O * o0ooo
 if 42 - 42: i11IiIiiIIIII + I1ii
 if 76 - 76: IiIi1Iii1I1 - OOo000
 if 70 - 70: O00O0O0O0
 if 61 - 61: OOO0O . OOO0O
def IIi1I1Ii11iI ( url = 'None' ) :
 if 39 - 39: i1iIIi1 - o0oOoO00o * OOo000 % o0ooo * o0oOoO00o % o0oOoO00o
 if url == 'None' :
  OoOOOOO = ''
  iIi1i111II = xbmc . Keyboard ( OoOOOOO , 'Enter Search Term' )
  iIi1i111II . doModal ( )
  if iIi1i111II . isConfirmed ( ) :
   OoOOOOO = iIi1i111II . getText ( )
   if len ( OoOOOOO ) > 1 :
    OoOO00O = OoOOOOO . lower ( )
    OoOO00O = OoOO00O . replace ( ' ' , '-' )
    if 53 - 53: OOo000 % i111I - O0o00
   else : quit ( )
 else : OoOO00O = urllib . unquote_plus ( url ) . lower ( ) ; OoOOOOO = urllib . unquote_plus ( url )
 if 97 - 97: I1ii % i1iIIi1 * i1iIIi1
 if 39 - 39: i11IiIiiIIIII % i1iIIi1
 url = "http://megamp3.com.br/search/" + OoOO00O
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<div class="row search-results">(.+?)</span>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  i111IiI1I = re . compile ( '<h2 class="song-title pull-left">(.+?)</h2>' ) . findall ( IiIiiI ) [ 0 ]
  II1 = re . compile ( 'src="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  II1 = II1 . strip ( )
  oo0Oo00Oo0 = re . compile ( 'link="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  O0iII ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , oo0Oo00Oo0 , 7 , II1 , ooo0OO )
 Oo000 ( )
def o0 ( url ) :
 if 62 - 62: ooO0oo0oO0 * O0o00
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<div class="player-wrap">(.+?)</div>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  i1 = re . compile ( 'poster="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  OOO = re . compile ( '<source src="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  O0iII ( '[COLOR aqua]' + "Play" + '[/COLOR]' , OOO , 7 , i1 , ooo0OO )
  if 59 - 59: o0oOoO00o + i111I * O0o00 + II1Ii1iI1i
  if 58 - 58: o0oOoO00o * oOOOo0o0O * OOO0O / oOOOo0o0O
def oO0o0OOOO ( ) :
 if 68 - 68: IiiIII111ii - IiIi1Iii1I1 - O0OOo - OOO0O + OOoOoo00oo
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL3d3dy5iaWd0b3A0MC5jb20v' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O00o0OOO0 = re . compile ( '<div class="chart_holder">(.+?)<p class="full_chart">' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   iiiI1I11i1 = re . compile ( 'class="chart_label">(.+?)<span class="chart_date">(.+?)</span>' ) . findall ( IiIiiI )
   for IIi1i11111 , ooOO00O00oo in iiiI1I11i1 :
    oO0o0O0OOOoo0 ( "[B][COLOR red]" + IIi1i11111 + ooOO00O00oo + "[/COLOR][/B]" , 'url' , 999 , II1 , ooo0OO )
    oO0o0O0OOOoo0 ( "[B][COLOR red]" + '--------------------------------------------------' + "[/COLOR][/B]" , 'url' , 999 , II1 , ooo0OO )
   I1ii11iI = re . compile ( '<img class="track_image".+?src="(.+?)" alt="(.+?)">.+?<a href="(.+?)"' ) . findall ( IiIiiI )
   for IIi1i , i111IiI1I , oo0Oo00Oo0 in I1ii11iI :
    if 46 - 46: IiIi1Iii1I1 % OOoOoo00oo + OOo000 . O0o00 . OOo000
    if 'http' not in oo0Oo00Oo0 :
     o0o00ooo0 = 'http://www.bigtop40.com' + oo0Oo00Oo0
     i111IiI1I = O0 ( i111IiI1I )
     iiii ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , o0o00ooo0 , 4 , IIi1i , ooo0OO )
  except : pass
 Oo000 ( )
def oO00o0 ( url ) :
 OOoo0O = oOOO00o ( url ) . replace ( '?' , '' )
 Oo0ooOo0o = re . compile ( '<iframe width=".+?" height="348" src="(.+?)"' ) . findall ( OOoo0O ) [ 0 ]
 id = Oo0ooOo0o . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 quit ( )
 if 22 - 22: ooO0oo0oO0 / i11iIiiIii * ooO0oo0oO0 * o0oOoO00o . oOOOo0o0O / i11iIiiIii
def Iiii ( ) :
 if 75 - 75: O0o00 % o0ooo % o0ooo . IiIi1Iii1I1
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<table width="550" id="thetable">(.+?)<table width="180" cellpadding="3" class="cell">' , re . DOTALL ) . findall ( oo0Oo00Oo0 ) [ 0 ]
 I1ii11iI = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( O0O00o0OOO0 )
 for III1iII1I1ii , oOOo0 in I1ii11iI :
  if 'http' not in III1iII1I1ii :
   o0o00ooo0 = 'http://www.listenlive.eu/' + III1iII1I1ii
   iiii ( '[COLOR aqua]' + oOOo0 + '[/COLOR]' , o0o00ooo0 , 6 , II1 , ooo0OO )
 Oo000 ( )
def oo00O00oO ( url ) :
 if 23 - 23: OOo000 + OOo000 . oOOOo0o0O
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<tr>(.+?)</tr>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   i111IiI1I = re . compile ( '<td>.+?<b>(.+?)</b>' ) . findall ( IiIiiI ) [ 0 ]
   i111IiI1I = O0 ( i111IiI1I )
   if 38 - 38: IiIi1Iii1I1
   url = re . compile ( '<a href="(.+?)"' ) . findall ( IiIiiI ) [ 1 ]
   if '.m3u' in url :
    if not 'Radio station' in i111IiI1I :
     O0iII ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , url , 8 , II1 , ooo0OO )
  except : pass
 Oo000 ( )
def Ii1OOooOO000 ( url ) :
 if 97 - 97: OOO0O + oOOOo0o0O / ooO0oo0oO0 / IiiIII111ii
 oo0Oo00Oo0 = oOOO00o ( url ) . replace ( '[playlist]NumberOfEntries=1File1=' , '' )
 I1111IIi = 'http://i.imgur.com/eBxpxQn.png'
 Oo0oO = xbmcgui . ListItem ( o0oO , iconImage = i1iiI11I , thumbnailImage = i1iiI11I )
 xbmc . Player ( ) . play ( oo0Oo00Oo0 , Oo0oO , False )
 if 1 - 1: OOo000 - I1ii . OOoOoo00oo . OOo000 / II1Iiii1111i + OOoOoo00oo
def Ooo ( ) :
 if 62 - 62: oOOOo0o0O / OOo000 + i11IiIiiIIIII / OOo000 . o0oOoO00o
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL3d3dy5wdW1weW91dXAuY29tLyM=' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<ul class="graphic">(.+?)</div>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  I1ii11iI = re . compile ( '<a href=".+?" rel="(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( IiIiiI )
  for oo0Oo00Oo0 , i111IiI1I in I1ii11iI :
   if 'http' not in oo0Oo00Oo0 :
    o0o00ooo0 = 'http://www.pumpyouup.com/' + oo0Oo00Oo0
    O0iII ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , o0o00ooo0 , 7 , II1 , ooo0OO )
 Oo000 ( )
def ooOOoooooo ( ) :
 if 1 - 1: II1Iiii1111i / o0ooo % IiiIII111ii * i1iIIi1 . i11iIiiIii
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL3NydjIudGV1cGxvYWQuY29tL011c2ljL0FsYnVtL0hvdCUyMDEwMCUyMC0lMjAxMSUyMEp1bmUlMjAyMDE2L0hvdCUyMDEwMCUyMC0lMjAxMSUyMEp1bmUlMjAyMDE2JTIwMzIwLw==' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oo0Oo00Oo0 )
 for oo0Oo00Oo0 , i111IiI1I in O0O00o0OOO0 :
  if not 'http' in oo0Oo00Oo0 :
   i111IiI1I = i111IiI1I . replace ( '.mp3' , '' )
   i111IiI1I = O0 ( i111IiI1I )
   if '.mp3' in oo0Oo00Oo0 :
    o0o00ooo0 = 'http://srv2.teupload.com/Music/Album/Hot%20100%20-%2011%20June%202016/Hot%20100%20-%2011%20June%202016%20320/' + oo0Oo00Oo0
    O0iII ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , o0o00ooo0 , 7 , II1 , ooo0OO )
 Oo000 ( )
def III1Iiii1I11 ( ) :
 if 9 - 9: OOO0O / II1Iiii1111i - O0OOo / i111I / ooO0oo0oO0 - o0ooo
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL2RvcmEtcm9iby5jb20vbXV6eWthLzcwJTI3cy04MCUyN3MtOTAlMjdzJTIwLw==' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( oo0Oo00Oo0 )
 for oo0Oo00Oo0 , i111IiI1I in O0O00o0OOO0 :
  if 'http' not in oo0Oo00Oo0 :
   o0o00ooo0 = 'http://dora-robo.com/muzyka/70%27s-80%27s-90%27s%20/' + oo0Oo00Oo0
   if '.mp3' in i111IiI1I :
    i111IiI1I = i111IiI1I . replace ( '.mp3' , '' )
    i111IiI1I = O0 ( i111IiI1I )
    O0iII ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , o0o00ooo0 , 7 , II1 , ooo0OO )
 Oo000 ( )
def o00oooO0Oo ( ) :
 if 78 - 78: i11IiIiiIIIII % IiIi1Iii1I1 + OOO0O
 i1iiI11I = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Warning_-_Wikis_on_toilet.svg/500px-Warning_-_Wikis_on_toilet.svg.png'
 oO0o0O0OOOoo0 ( '[COLOR red]' + 'Some Albums will be Empty, This is because no info is in the API' + '[/COLOR]' , 'url' , 999 , i1iiI11I , ooo0OO )
 o0o00ooo0 = 'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=' + O0oo0OO0
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<artist>(.+?)</artist>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   o0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( IiIiiI ) [ 0 ]
   II1 = re . compile ( '<image size="mega">(.+?)</image>' ) . findall ( IiIiiI ) [ 0 ]
   OOooOoooOoOo = re . compile ( '<mbid>(.+?)</mbid>' ) . findall ( IiIiiI ) [ 0 ]
   o0o00ooo0 = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&mbid=' + OOooOoooOoOo + '&api_key=' + O0oo0OO0
   iiii ( '[COLOR aqua]' + o0oO + '[/COLOR]' , o0o00ooo0 , 13 , II1 , ooo0OO )
   if 84 - 84: i1iIIi1
  except : pass
 Oo000 ( )
 if 86 - 86: O0o00 - i11IiIiiIIIII - OOo000 * IiiIII111ii
def oooo0O0 ( url ) :
 if 51 - 51: OOo000 / OOo000
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<album>(.+?)</album>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   o0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( IiIiiI ) [ 0 ]
   o0oO = O0 ( o0oO )
   ooOOO0 = re . compile ( '<name>(.+?)</name>' ) . findall ( IiIiiI ) [ 1 ]
   II1 = re . compile ( '<image size="extralarge">(.+?)</image>' ) . findall ( IiIiiI ) [ 0 ]
   OOooOoooOoOo = re . compile ( '<mbid>(.+?)</mbid>' ) . findall ( IiIiiI ) [ 0 ]
   url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=' + O0oo0OO0 + '&artist=' + ooOOO0 + '&album=' + o0oO
   iiii ( '[COLOR aqua]' + o0oO + '[/COLOR]' , url , 14 , II1 , ooo0OO )
  except : pass
 Oo000 ( )
def o0o ( url ) :
 if 73 - 73: i1iIIi1 * OOO0O + O0OOo . O00O0O0O0
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<track rank=".+?">(.+?)</track>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   o0oO = re . compile ( '<name>(.+?)</name>' ) . findall ( IiIiiI ) [ 0 ]
   o0oO = O0 ( o0oO )
   OOooOoooOoOo = re . compile ( '<mbid>(.+?)</mbid>' ) . findall ( IiIiiI ) [ 0 ]
   if 70 - 70: IiIi1Iii1I1 - II1Iiii1111i / i11IiIiiIIIII
   url = o0oO
   iiii ( '[COLOR aqua]' + o0oO + '[/COLOR]' , url , 20 , II1 , ooo0OO )
  except : pass
 Oo000 ( )
 if 82 - 82: OOoOoo00oo % o0ooo % OOo000 - II1Iiii1111i + i111I
def Iiii1i1 ( ) :
 if 84 - 84: O0OOo . ooO0oo0oO0 % i111I + i11IiIiiIIIII % i111I % OOo000
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL3BvcnRhbGExLmNvbS9tcDNfZmlsZXMvbXAzL21wLw==' )
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<li>(.+?)</li>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  i111IiI1I = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IiIiiI ) [ 0 ]
  IIi1 = re . compile ( '<a href="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  if 'http' not in IIi1 :
   o0o00ooo0 = 'http://portala1.com/mp3_files/mp3/mp/' + IIi1
  if '.mp3' in i111IiI1I :
   iiii ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , o0o00ooo0 , 16 , II1 , ooo0OO )
 Oo000 ( )
 if 45 - 45: IiiIII111ii / IiiIII111ii + IiIi1Iii1I1 + O00O0O0O0
def iI111i ( ) :
 if 26 - 26: OOO0O * IiiIII111ii . o0oOoO00o * i11IiIiiIIIII
 o0o00ooo0 = base64 . b64decode ( b'aHR0cDovL2hjbWFzbG92LmQtcmVhbC5zY2ktbm5vdi5ydS9wdWJsaWMvbXAzLw==' )
 if 28 - 28: OOo000 . II1Ii1iI1i * O0OOo + oooO0oo0oOOOO . II1Ii1iI1i - O00O0O0O0
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 )
 O0O00o0OOO0 = re . compile ( '<tr>(.+?)</tr>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   o0o00ooo0 = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( IiIiiI ) [ 0 ]
   if 38 - 38: IiIi1Iii1I1
   i111IiI1I = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IiIiiI ) [ 0 ] . replace ( '/' , '' )
   i111IiI1I = Ooo00o0Oooo ( i111IiI1I )
   if '%' not in o0o00ooo0 :
    if 'Name' not in i111IiI1I :
     if 'Parent Directory' not in i111IiI1I :
      if 'http' not in o0o00ooo0 :
       OOooooO0Oo = 'http://hcmaslov.d-real.sci-nnov.ru/public/mp3/' + o0o00ooo0
       iiii ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , OOooooO0Oo , 18 , II1 , ooo0OO )
  except : pass
 Oo000 ( )
def OO ( url ) :
 if 25 - 25: OOo000
 oo0Oo00Oo0 = oOOO00o ( url )
 O0O00o0OOO0 = re . compile ( '<tr>(.+?)</tr>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   i111IiI1I = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IiIiiI ) [ 0 ]
   oo0Oo00Oo0 = re . compile ( '<a href="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
   if 'http' not in oo0Oo00Oo0 :
    if not 'Name' in i111IiI1I :
     if not 'Parent Directory' in i111IiI1I :
      OOooooO0Oo = url + oo0Oo00Oo0
      iiii ( '[COLOR aqua]' + i111IiI1I + '[/COLOR]' , OOooooO0Oo , 16 , II1 , ooo0OO )
  except : pass
 Oo000 ( )
 if 62 - 62: oOOOo0o0O + oooO0oo0oOOOO
def oO0OOOO0 ( ) :
 if 26 - 26: i11IiIiiIIIII
 o0o00ooo0 = 'http://76.92.66.82/MUSIC/TYLER/The%20Ultimate%20Disney%20Collection/Assorted/Music%20From%20Disney/'
 oo0Oo00Oo0 = oOOO00o ( o0o00ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O00o0OOO0 = re . compile ( '<td valign="top">(.+?)</tr>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  try :
   o0o00ooo0 = re . compile ( '<a href="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
   i111IiI1I = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IiIiiI ) [ 0 ]
   if 'Parent Directory' not in i111IiI1I :
    if 'http' not in o0o00ooo0 :
     OOooooO0Oo = 'http://76.92.66.82/MUSIC/TYLER/The%20Ultimate%20Disney%20Collection/Assorted/Music%20From%20Disney/' + o0o00ooo0
     II1 = 'http://ianusher.com/wp-content/uploads/2015/06/500_sq_WaltDisney.jpg'
     iiii ( "[COLOR aqua]" + i111IiI1I + "[/COLOR]" , OOooooO0Oo , 23 , II1 , ooo0OO , '' )
  except : pass
 Oo000 ( )
 if 35 - 35: i11IiIiiIIIII - O0OOo % o0ooo . i111I % i11IiIiiIIIII
def I1i1Iiiii ( url ) :
 if 94 - 94: o0ooo * i11IiIiiIIIII / II1Iiii1111i / i11IiIiiIIIII
 oo0Oo00Oo0 = oOOO00o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0O00o0OOO0 = re . compile ( '<td valign="top">(.+?)</tr>' ) . findall ( oo0Oo00Oo0 )
 for IiIiiI in O0O00o0OOO0 :
  OOooooO0Oo = re . compile ( '<a href="(.+?)"' ) . findall ( IiIiiI ) [ 0 ]
  i111IiI1I = re . compile ( '<td><a href=".+?">(.+?)</a>' ) . findall ( IiIiiI ) [ 0 ]
  I1i1iii = url + OOooooO0Oo
  if '.mp3' in I1i1iii :
   O0iII ( "[COLOR aqua]" + i111IiI1I + "[/COLOR]" , I1i1iii , 7 , II1 , ooo0OO , '' )
 Oo000 ( )
 if 87 - 87: II1Iiii1111i . i1iIIi1
 if 75 - 75: O00O0O0O0 + O0o00 + o0ooo * OOoOoo00oo % I1ii . IiiIII111ii
 if 55 - 55: oOOOo0o0O . O0OOo
 if 61 - 61: II1Iiii1111i % i1iIIi1 . II1Iiii1111i
 if 100 - 100: IiIi1Iii1I1 * oooO0oo0oOOOO
 if 64 - 64: oOOOo0o0O % ooO0oo0oO0 * I1ii
def iiii ( name , url , mode , iconimage , fanart , description = '' ) :
 if 79 - 79: oooO0oo0oOOOO
 oOO00O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 Oo0oO . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : oOO00O = url
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO00O , listitem = Oo0oO , isFolder = True )
 return OOOoo0OO
 if 57 - 57: OOo000 / O00O0O0O0
def OoOo ( name , url , mode , iconimage , fanart , description = '' ) :
 if 29 - 29: ooO0oo0oO0 + O0o00 * OOo000 * oOOOo0o0O . O0OOo * O0OOo
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
  if 7 - 7: i1iIIi1 * IiIi1Iii1I1 % i11IiIiiIIIII - o0ooo
 oOO00O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  Oo0oO . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : oOO00O = url
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO00O , listitem = Oo0oO , isFolder = False )
 return OOOoo0OO
 if 13 - 13: i11IiIiiIIIII . i11iIiiIii
def O0iII ( name , url , mode , iconimage , fanart , description = '' ) :
 oOO00O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setProperty ( 'fanart_image' , fanart )
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO00O , listitem = Oo0oO , isFolder = False )
 return OOOoo0OO
 if 56 - 56: OOO0O % oooO0oo0oOOOO - O0OOo
def Ooo00o0Oooo ( string ) :
 O00o0OO0 = ( c for c in string if 0 < ord ( c ) < 127 )
 if 35 - 35: I1ii % O00O0O0O0 / IiIi1Iii1I1 + ooO0oo0oO0 . i111I . O0OOo
 return '' . join ( O00o0OO0 )
 if 71 - 71: i1iIIi1 * o0oOoO00o * I1ii
def oO0o0O0OOOoo0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 56 - 56: O0OOo
 oOO00O = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Oo0oO . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  Oo0oO . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : oOO00O = url
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO00O , listitem = Oo0oO , isFolder = False )
 return OOOoo0OO
 if 54 - 54: IiIi1Iii1I1 / oOOOo0o0O . I1ii % IiiIII111ii
def OoO0OOOOo0O ( url ) :
 if 81 - 81: oooO0oo0oOOOO / OOo000 . II1Ii1iI1i + O0OOo - OOoOoo00oo
 oo0Oo00Oo0 = oOOO00o ( url )
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( o0oO , iconImage = "DefaultFolder.png" , thumbnailImage = i1iiI11I ) ; Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : o0oO } )
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = Oo0oO )
 xbmc . Player ( ) . play ( url , Oo0oO , False )
 quit ( )
 if 74 - 74: ooO0oo0oO0 * OOO0O + O0o00 / II1Ii1iI1i / o0oOoO00o . II1Iiii1111i
 if 62 - 62: i111I * O0OOo
def oOOOoo0O0oO ( ) :
 iIII1I111III = [ ]
 IIo0o0O0O00oOOo = sys . argv [ 2 ]
 if len ( IIo0o0O0O00oOOo ) >= 2 :
  iIIIiIi = sys . argv [ 2 ]
  OO0O0 = iIIIiIi . replace ( '?' , '' )
  if ( iIIIiIi [ len ( iIIIiIi ) - 1 ] == '/' ) :
   iIIIiIi = iIIIiIi [ 0 : len ( iIIIiIi ) - 2 ]
  I11I11 = OO0O0 . split ( '&' )
  iIII1I111III = { }
  for o000O0O in range ( len ( I11I11 ) ) :
   I1i1i1iii = { }
   I1i1i1iii = I11I11 [ o000O0O ] . split ( '=' )
   if ( len ( I1i1i1iii ) ) == 2 :
    iIII1I111III [ I1i1i1iii [ 0 ] ] = I1i1i1iii [ 1 ]
 return iIII1I111III
 if 16 - 16: i11IiIiiIIIII + i1iIIi1 * oooO0oo0oOOOO % II1Ii1iI1i . O0OOo
def oOOO00o ( url ) :
 try :
  Oo0OO = urllib2 . Request ( url )
  Oo0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  O0OooOo0o = urllib2 . urlopen ( Oo0OO , timeout = 5 )
  oo0Oo00Oo0 = O0OooOo0o . read ( )
  O0OooOo0o . close ( )
  oo0Oo00Oo0 = oo0Oo00Oo0 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 29 - 29: O0OOo % O0OOo
  return oo0Oo00Oo0
 except : quit ( )
 if 94 - 94: ooO0oo0oO0 / II1Iiii1111i % IiiIII111ii * IiiIII111ii * o0oOoO00o
def oOOoO0 ( url ) :
 Oo0OO = urllib2 . Request ( url )
 Oo0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 O0OooOo0o = urllib2 . urlopen ( Oo0OO )
 oo0Oo00Oo0 = O0OooOo0o . read ( )
 O0OooOo0o . close ( )
 if 29 - 29: OOo000 + O0o00 / o0ooo / oOOOo0o0O * ooO0oo0oO0
 return oo0Oo00Oo0
 if 62 - 62: oOOOo0o0O / I1ii - OOo000 . OOoOoo00oo
def Oo000 ( ) :
 if 11 - 11: OOO0O . OOo000 * i1iIIi1 * i111I + O00O0O0O0
 IiII111i1i11 = xbmc . getInfoLabel ( "System.BuildVersion" )
 i111iIi1i1II1 = float ( IiII111i1i11 [ : 4 ] )
 if 86 - 86: ooO0oo0oO0 / O0o00 . o0oOoO00o
 if i111iIi1i1II1 >= 1.0 and i111iIi1i1II1 <= 16.9 :
  II1i111Ii1i = 'Jarvis'
 elif i111iIi1i1II1 >= 17.0 and i111iIi1i1II1 <= 17.9 :
  II1i111Ii1i = 'Krypton'
  if 15 - 15: o0oOoO00o / II1Ii1iI1i
 if II1i111Ii1i == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif II1i111Ii1i == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 76 - 76: OOoOoo00oo / oOOOo0o0O . oooO0oo0oOOOO % O0OOo . o0ooo + i1iIIi1
 if 71 - 71: IiIi1Iii1I1 . o0oOoO00o
def oo0 ( name , url , iconimage ) :
 if 61 - 61: O0o00 - oOOOo0o0O - II1Ii1iI1i
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  IiI1iIiIIIii = url . split ( 'list=' ) [ 1 ]
  oOoO = I11i11Ii + IiI1iIiIIIii + oO00oOo
  Oo0OO = urllib2 . Request ( oOoO )
  Oo0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  O0OooOo0o = urllib2 . urlopen ( Oo0OO )
  oo0Oo00Oo0 = O0OooOo0o . read ( )
  O0OooOo0o . close ( )
  oo0Oo00Oo0 = oo0Oo00Oo0 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  O0O00o0OOO0 = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( oo0Oo00Oo0 )
  try :
   oOoO00O0 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( oo0Oo00Oo0 ) [ 0 ]
   oOoO = OOOo0 + oOoO00O0 + Oooo000o + IiI1iIiIIIii + IiIi11iIIi1Ii
   iiii ( 'Next Page >>' , oOoO , 1 , I1IiiI , iiiii )
  except : pass
  if 75 - 75: O0OOo . O00O0O0O0 . oooO0oo0oOOOO * IiIi1Iii1I1
  if 4 - 4: i11IiIiiIIIII % I1ii * OOo000
  if 100 - 100: IiIi1Iii1I1 * oOOOo0o0O + oOOOo0o0O
  if 54 - 54: i111I + o0ooo - II1Ii1iI1i % i11iIiiIii
  for name , iII1iIi11i in O0O00o0OOO0 :
   url = 'https://www.youtube.com/watch?v=' + iII1iIi11i
   iconimage = 'https://i.ytimg.com/vi/' + iII1iIi11i + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     OoOo ( name , url , 2 , iconimage , iiiii )
     if 81 - 81: i1iIIi1 % II1Ii1iI1i . ooO0oo0oO0
 if 'https://www.googleapis.com/youtube/v3' in url :
  IiI1iIiIIIii = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  Oo0OO = urllib2 . Request ( url )
  Oo0OO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  O0OooOo0o = urllib2 . urlopen ( Oo0OO )
  oo0Oo00Oo0 = O0OooOo0o . read ( )
  O0OooOo0o . close ( )
  oo0Oo00Oo0 = oo0Oo00Oo0 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  O0O00o0OOO0 = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( oo0Oo00Oo0 )
  try :
   oOoO00O0 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( oo0Oo00Oo0 ) [ 0 ]
   oOoO = OOOo0 + oOoO00O0 + Oooo000o + IiI1iIiIIIii + IiIi11iIIi1Ii
   iiii ( 'Next Page >>' , oOoO , 2 , I1IiiI , iiiii )
  except : pass
  if 4 - 4: i11iIiiIii % OOo000 % II1Ii1iI1i / i1iIIi1
  if 6 - 6: IiiIII111ii / O0OOo % oOOOo0o0O - O0OOo
  if 31 - 31: oOOOo0o0O
  for name , iII1iIi11i in O0O00o0OOO0 :
   url = 'https://www.youtube.com/watch?v=' + iII1iIi11i
   iconimage = 'https://i.ytimg.com/vi/' + iII1iIi11i + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     OoOo ( name , url , 2 , iconimage , iiiii )
     if 23 - 23: IiIi1Iii1I1 . i1iIIi1
def OO0000o ( name , url , iconimage ) :
 OOOoo0OO = True
 Oo0oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; Oo0oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOOoo0OO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = Oo0oO )
 xbmc . Player ( ) . play ( url , Oo0oO , False )
 if 42 - 42: II1Iiii1111i
def O0OoO000O0OO ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 oo000O0OoooO = xbmcgui . Window ( id )
 O0o = 50
 while ( O0o > 0 ) :
  try :
   xbmc . sleep ( 10 )
   O0o -= 1
   oo000O0OoooO . getControl ( 1 ) . setLabel ( heading )
   oo000O0OoooO . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 27 - 27: i1iIIi1 - i11IiIiiIIIII / OOO0O % i1iIIi1 + O0OOo
   if 96 - 96: IiIi1Iii1I1
   if 97 - 97: O00O0O0O0
   if 48 - 48: II1Ii1iI1i - IiIi1Iii1I1
   if 56 - 56: o0ooo + o0oOoO00o + O0o00 - O00O0O0O0 . O0o00
iIIIiIi = oOOOoo0O0oO ( ) ; o0o00ooo0 = None ; o0oO = None ; OOOooo = None ; OooO0OO = None ; i1iiI11I = None ; iiiii = None
try : OooO0OO = urllib . unquote_plus ( iIIIiIi [ "site" ] )
except : pass
try : o0o00ooo0 = urllib . unquote_plus ( iIIIiIi [ "url" ] )
except : pass
try : o0oO = urllib . unquote_plus ( iIIIiIi [ "name" ] )
except : pass
try : OOOooo = int ( iIIIiIi [ "mode" ] )
except : pass
try : i1iiI11I = urllib . unquote_plus ( iIIIiIi [ "iconimage" ] )
except : pass
try : iiiii = urllib . unquote_plus ( iIIIiIi [ "fanart" ] )
except : pass
if OOOooo == None or o0o00ooo0 == None or len ( o0o00ooo0 ) < 1 : II ( )
if 69 - 69: O00O0O0O0 % I1ii
elif OOOooo == 1 : IIiIi11i1 ( o0oO , o0o00ooo0 , i1iiI11I , iiiii )
elif OOOooo == 2 : oo0 ( o0oO , o0o00ooo0 , i1iiI11I )
elif OOOooo == 3 : oO0o0OOOO ( )
elif OOOooo == 4 : oO00o0 ( o0o00ooo0 )
elif OOOooo == 5 : Iiii ( )
elif OOOooo == 6 : oo00O00oO ( o0o00ooo0 )
elif OOOooo == 7 : OO0000o ( o0oO , o0o00ooo0 , i1iiI11I )
elif OOOooo == 8 : Ii1OOooOO000 ( o0o00ooo0 )
elif OOOooo == 9 : Ooo ( )
elif OOOooo == 10 : ooOOoooooo ( )
elif OOOooo == 11 : III1Iiii1I11 ( )
elif OOOooo == 12 : o00oooO0Oo ( )
elif OOOooo == 13 : oooo0O0 ( o0o00ooo0 )
elif OOOooo == 14 : o0o ( o0o00ooo0 )
elif OOOooo == 15 : Iiii1i1 ( )
elif OOOooo == 16 : OoO0OOOOo0O ( o0o00ooo0 )
elif OOOooo == 17 : iI111i ( )
elif OOOooo == 18 : OO ( o0o00ooo0 )
elif OOOooo == 19 : ooO0O ( o0o00ooo0 )
elif OOOooo == 20 : IIi1I1Ii11iI ( o0o00ooo0 )
elif OOOooo == 21 : o0 ( o0o00ooo0 )
elif OOOooo == 22 : oO0OOOO0 ( )
elif OOOooo == 23 : I1i1Iiiii ( o0o00ooo0 )
if 50 - 50: i111I % OOoOoo00oo
if 49 - 49: I1ii - i11iIiiIii . IiIi1Iii1I1 * i11IiIiiIIIII % IiiIII111ii + II1Ii1iI1i
elif OOOooo == 100 : GET_FAVOURITES ( )
elif OOOooo == 101 : DECIDE_FAVOURITES ( o0oO , o0o00ooo0 , i1iiI11I )
if 71 - 71: o0ooo
if 38 - 38: I1ii % O0o00 + OOO0O . i11iIiiIii
if 53 - 53: i11iIiiIii * IiiIII111ii
if OOOooo == None or o0o00ooo0 == None or len ( o0o00ooo0 ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
