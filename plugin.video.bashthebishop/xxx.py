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
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
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
 if 16 - 16: Oo0oO0ooo % IiIiI11iIi - O0OOo . O0Oooo00 . oo00 * I11
def Oo0o0000o0o0 ( url , mode , name , iconimage , fanart ) :
 if 86 - 86: iiiii11iII1 % O0o
 with open ( I1IiI , "a" ) as oO0 :
  oO0 . write ( '<item>\n<title>' + name + '</title>\n<url>' + url + '</url>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart>\n</item>\n\n' )
  iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR pink]' + name + ' added to favourites[/COLOR]' , Oo , 5000 )
  if 32 - 32: I1i1I - OoOoo0 % iIiiI1 % OoOooOOOO
def i11iiII ( ) :
 if 34 - 34: I11 % OoooooooOO / i1IIi . I1i1I + O0
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I1Ii ( '[COLOR pink]' + "REMOVE ALL FAVOURITES" + '[/COLOR]' , 'url' , 893 , o0oOo0Ooo0O , I11i )
 with open ( I1IiI , "a" ) as oO0 :
  OO00O0O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/' + o0OO00 , 'favs.xml' ) )
  IIIiiiiiIii = open ( OO00O0O0O00Oo ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  OO = re . compile ( '<item>(.+?)</item>' ) . findall ( IIIiiiiiIii )
  I1Ii ( '[COLOR pink]' + "Your Favourites" + '[/COLOR]' , 'url' , '2' , o0oOo0Ooo0O , I11i )
  I1Ii ( '[COLOR white]' + "----------------------------------------------------" + '[/COLOR]' , 'url' , '2' , o0oOo0Ooo0O , I11i )
  if len ( OO ) < 1 :
   I1Ii ( '[COLOR pink]' + "NO FAVS ADDED YET" + '[/COLOR]' , 'url' , '2' , o0oOo0Ooo0O , I11i )
  for oO0O in OO :
   OOoO000O0OO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0O ) [ 0 ]
   iiI1IiI = re . compile ( '<url>(.+?)</url>' ) . findall ( oO0O ) [ 0 ]
   Oo = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0O ) [ 0 ]
   O0O = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0O ) [ 0 ]
   I1Ii ( '[COLOR pink]' + OOoO000O0OO + '[/COLOR]' , iiI1IiI , 99 , Oo , O0O )
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 if 13 - 13: oO0o . i11iIiiIii - iIii1I11I1II1 - IiIiI11iIi
def ii1I ( ) :
 if 76 - 76: O0 / O0OOo . iiI1i1 * O0o - I11
 with open ( I1IiI , "w" ) as oO0 :
  oO0 . write ( '' )
  iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR pink]Favourites has been wiped[/COLOR]' , Oo , 5000 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . O0Oooo00 % I11 / OoooooooOO % oo00
def o0ooo00O0o0 ( ) :
 if 63 - 63: O0o
 O00 ( "[COLOR white][B]M[COLOR pink]ovies[/B][/COLOR]" , 'null' , 1 , Oo , I11i , '[COLOR pink]XXX Movies[/COLOR]' )
 O00 ( "[COLOR white][B]Y[COLOR pink]ears[/B][/COLOR]" , 'null' , 2 , Oo , I11i , '[COLOR pink]XXX Sorted By Year[/COLOR]' )
 O00 ( "[COLOR white][B]G[COLOR pink]enres[/B][/COLOR]" , 'null' , 4 , Oo , I11i , '[COLOR pink]XXX Sorted By Genre[/COLOR]' )
 O00 ( "[COLOR white][B]H[COLOR pink]ighest Rated[/B][/COLOR]" , 'null' , 5 , Oo , I11i , '[COLOR pink]Highest Rated XXX[/COLOR]' )
 O00 ( "[COLOR white][B]M[COLOR pink]ost Viewed[/B][/COLOR]" , 'null' , 6 , Oo , I11i , '[COLOR pink]Most Viewed XXX[/COLOR]' )
 O00 ( "[COLOR white][B]H[COLOR pink]D[/B][/COLOR]" , 'null' , 7 , Oo , I11i , '[COLOR pink]HD XXX[/COLOR]' )
 O00 ( "[COLOR white][B]Y[COLOR pink]our Favourites[/B][/COLOR]" , 'null' , 890 , Oo , I11i , '[COLOR pink]Save Your Bishops Favourite Videos[/COLOR]' )
 i1I1ii1II1iII ( )
 iII11i ( )
 if 97 - 97: iiiii11iII1 % iiiii11iII1 + Ii11111i * I1i1I
def o0o00o0 ( url ) :
 if 25 - 25: oO0o - OoOoo0 . OoooooooOO
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11ii1 = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies/page/1'
 I11II1i = IIIII ( url )
 OO = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  OOoO000O0OO = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( '<a href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ] . strip ( )
  I1IIIii = re . compile ( '<p>(.*?)</p>' ) . findall ( ooooooO0oo ) [ 0 ]
  OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
  I1IIIii = oOoOooOo0o0 ( I1IIIii )
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 98 , Oo , I11i , I1IIIii )
 try :
  OOOO = url . split ( '/' ) [ - 1 ]
  OOOO = int ( OOOO )
  OOO00 = OOOO + 1
  iiiiiIIii = 'https://pandamoviehd.me/list-movies/page/' + str ( OOO00 )
  if OOO00 < I11ii1 :
   O00 ( "[COLOR yellow]Next Page ---->[/COLOR]" , iiiiiIIii , 1 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def O000OO0 ( url ) :
 if 43 - 43: iIiiI1 - O0 % iiI1i1 . iiiii11iII1
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies'
 I11II1i = IIIII ( url )
 OO = re . compile ( '''<ul class='sub-menu'>(.*?)</ul>''' ) . findall ( I11II1i ) [ 0 ]
 o00 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( OO )
 for IIiiiiiiIi1I1 , OOoO000O0OO in o00 :
  IIiiiiiiIi1I1 = IIiiiiiiIi1I1 + '/page/1'
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 3 , Oo , I11i , 'Movies From ' + OOoO000O0OO )
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
 if 95 - 95: O0 + Oo0oO0ooo . Ii11111i / O0
def O000oo0O ( url ) :
 if 66 - 66: O0Oooo00 / IiIiI11iIi - iiI1i1 . I11 / iiI1i1 * I11
 if '1980' in url : I11ii1 = 1
 elif '1981' in url : I11ii1 = 1
 elif '1982' in url : I11ii1 = 1
 elif '1983' in url : I11ii1 = 1
 elif '1984' in url : I11ii1 = 1
 elif '1985' in url : I11ii1 = 1
 elif '1986' in url : I11ii1 = 1
 elif '1987' in url : I11ii1 = 1
 elif '1988' in url : I11ii1 = 1
 elif '1989' in url : I11ii1 = 1
 elif '1990' in url : I11ii1 = 2
 elif '1991' in url : I11ii1 = 1
 elif '1992' in url : I11ii1 = 1
 elif '1993' in url : I11ii1 = 1
 elif '1994' in url : I11ii1 = 1
 elif '1995' in url : I11ii1 = 3
 elif '1996' in url : I11ii1 = 1
 elif '1997' in url : I11ii1 = 3
 elif '1999' in url : I11ii1 = 5
 elif '2000' in url : I11ii1 = 11
 elif '2001' in url : I11ii1 = 9
 elif '2002' in url : I11ii1 = 12
 else : I11ii1 = 50
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11II1i = IIIII ( url )
 OO = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  OOoO000O0OO = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( '<a href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ] . strip ( )
  try :
   I1IIIii = re . compile ( '<p>(.*?)</p>' ) . findall ( ooooooO0oo ) [ 0 ]
  except :
   I1IIIii = '[COLOR pink]No Film Description Found[/COLOR]'
  OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
  I1IIIii = oOoOooOo0o0 ( I1IIIii )
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 98 , Oo , I11i , I1IIIii )
 try :
  OOOO = url . split ( 'page/' ) [ 0 ]
  OOO00 = url . split ( 'page/' ) [ - 1 ]
  OOO00 = int ( OOO00 )
  iiiiiIIii = OOO00 + 1
  IIIii1II1II = OOOO + 'page/' + str ( iiiiiIIii )
  if iiiiiIIii < I11ii1 :
   O00 ( "[COLOR yellow]Next Page ---->[/COLOR]" , IIIii1II1II , 3 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def i1I1iI ( url ) :
 if 93 - 93: iIii1I11I1II1 % oo00 * i1IIi
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 if 'null' in url :
  url = 'https://pandamoviehd.me/list-movies'
 I11II1i = IIIII ( url )
 OO = re . compile ( '''<ul class='sub-menu'>(.*?)</ul>''' ) . findall ( I11II1i ) [ 1 ]
 o00 = re . compile ( '<a href="(.*?)">(.*?)</a>' ) . findall ( OO )
 for IIiiiiiiIi1I1 , OOoO000O0OO in o00 :
  IIiiiiiiIi1I1 = IIiiiiiiIi1I1 + '/page/1'
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 3 , Oo , I11i , 'Movie Genre ' + OOoO000O0OO )
 iII11i ( )
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
def Ii11Ii1I ( url ) :
 if 72 - 72: I1i1I / i1IIi * oO0o - iIiiI1
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11ii1 = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/most-rating/page/1'
 I11II1i = IIIII ( url )
 OO = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  OOoO000O0OO = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( '<a href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ] . strip ( )
  I1IIIii = re . compile ( '<p>(.*?)</p>' ) . findall ( ooooooO0oo ) [ 0 ]
  OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
  I1IIIii = oOoOooOo0o0 ( I1IIIii )
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 98 , Oo , I11i , I1IIIii )
 try :
  OOOO = url . split ( '/' ) [ - 1 ]
  OOOO = int ( OOOO )
  OOO00 = OOOO + 1
  iiiiiIIii = 'https://pandamoviehd.me/most-rating/page/' + str ( OOO00 )
  if OOO00 < I11ii1 :
   O00 ( "[COLOR yellow]Next Page ---->[/COLOR]" , iiiiiIIii , 5 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def Oo0O0O0ooO0O ( url ) :
 if 15 - 15: O0Oooo00 + IiIiI11iIi - OoooooooOO / I11
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11ii1 = 972
 if 'null' in url :
  url = 'https://pandamoviehd.me/most-viewed/page/1'
 I11II1i = IIIII ( url )
 OO = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  OOoO000O0OO = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( '<a href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ] . strip ( )
  I1IIIii = re . compile ( '<p>(.*?)</p>' ) . findall ( ooooooO0oo ) [ 0 ]
  OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
  I1IIIii = oOoOooOo0o0 ( I1IIIii )
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 98 , Oo , I11i , I1IIIii )
 try :
  OOOO = url . split ( '/' ) [ - 1 ]
  OOOO = int ( OOOO )
  OOO00 = OOOO + 1
  iiiiiIIii = 'https://pandamoviehd.me/most-viewed/page/' + str ( OOO00 )
  if OOO00 < I11ii1 :
   O00 ( "[COLOR yellow]Next Page ---->[/COLOR]" , iiiiiIIii , 6 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def oo000OO00Oo ( url ) :
 if 51 - 51: OoOoo0 * O0OOo + iiiii11iII1 + Oo0oO0ooo
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11ii1 = 313
 if 'null' in url :
  url = 'https://pandamoviehd.me/watch-hd-movies-online-free/page/1'
 I11II1i = IIIII ( url )
 OO = re . compile ( 'class="ml-item">(.*?)<div class="block">' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  OOoO000O0OO = re . compile ( 'oldtitle="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  IIiiiiiiIi1I1 = re . compile ( '<a href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
  Oo = re . compile ( '<img data-original="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ] . strip ( )
  try :
   I1IIIii = re . compile ( '<p>(.*?)</p>' ) . findall ( ooooooO0oo ) [ 0 ]
  except :
   I1IIIii = '[COLOR pink]No Description Available For This Movie[/COLOR]'
  OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
  I1IIIii = oOoOooOo0o0 ( I1IIIii )
  O00 ( "[COLOR pink]" + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 98 , Oo , I11i , I1IIIii )
 try :
  OOOO = url . split ( '/' ) [ - 1 ]
  OOOO = int ( OOOO )
  OOO00 = OOOO + 1
  iiiiiIIii = 'https://pandamoviehd.me/watch-hd-movies-online-free/page/' + str ( OOO00 )
  if OOO00 < I11ii1 :
   O00 ( "[COLOR yellow]Next Page ---->[/COLOR]" , iiiiiIIii , 7 , I1ii11iIi11i , I11i , 'Next Page' )
 except :
  pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , o0oOo0Ooo0O , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def o0O0O00 ( title ) :
 if 86 - 86: iiiii11iII1 / OoOoo0 % i11iIiiIii
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
  if 7 - 7: OoOooOOOO * Oo0oO0ooo % oo00 . OoOoo0
def Ii1iIiII1ii1 ( name , url , iconimage , description ) :
 if 62 - 62: iIii1I11I1II1 * IiIiI11iIi
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , iconimage , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 I11II1i = IIIII ( url )
 OO = re . compile ( '<li class="hosts-buttons-wpx">(.*?)</li>' ) . findall ( I11II1i )
 for ooooooO0oo in OO :
  try :
   OOoO000O0OO = re . compile ( 'class="selected">(.*?)</a>' ) . findall ( ooooooO0oo ) [ 0 ]
   OOoO000O0OO = oOoOooOo0o0 ( OOoO000O0OO )
   OOoO000O0OO = o0O0O00 ( OOoO000O0OO )
   IIiiiiiiIi1I1 = re . compile ( 'href="(.*?)"' ) . findall ( ooooooO0oo ) [ 0 ]
   if not 'not supported' in OOoO000O0OO :
    I1Ii ( "[COLOR pink]" + name + " :: " + OOoO000O0OO + "[/COLOR]" , IIiiiiiiIi1I1 , 99 , iconimage , I11i , description )
  except : pass
 I1Ii ( "[COLOR red]" + "EMERGENCY EXIT" + "[/COLOR]" , 'url1' , 911 , iconimage , I11i , '[COLOR pink]BAIL THE WIFE IS COMING[/COLOR]' )
 iII11i ( )
def IIIII ( url ) :
 try :
  i1 = urllib2 . Request ( url )
  i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OOO = urllib2 . urlopen ( i1 , timeout = 5 )
  I11II1i = OOO . read ( )
  OOO . close ( )
  I11II1i = I11II1i . replace ( '\n' , '' ) . replace ( '\r' , '' )
  return I11II1i
 except : quit ( )
 if 59 - 59: Ii11111i + OoooooooOO * IiIiI11iIi + i1IIi
 if 58 - 58: Ii11111i * I11 * O0Oooo00 / I11
def O00 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 75 - 75: oo00
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 description = description . encode ( encoding = 'UTF-8' , errors = 'strict' )
 I1III = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OO0O0OoOO0 = True
 iiiI1I11i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage , )
 iiiI1I11i1 . setProperty ( "fanart_Image" , fanart )
 iiiI1I11i1 . setProperty ( "icon_Image" , iconimage )
 iiiI1I11i1 . setInfo ( 'video' , { 'Plot' : description } )
 OO0O0OoOO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1III , listitem = iiiI1I11i1 , isFolder = True )
 IIi1i11111 = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 return OO0O0OoOO0
 if 81 - 81: i11iIiiIii % IiIiI11iIi - I11
 if 68 - 68: iIiiI1 % i1IIi . OoOoo0 . O0Oooo00
def I1Ii ( name , url , mode , iconimage , fanart , description = '' ) :
 if 92 - 92: I1i1I . iIiiI1
 if not "http" in iconimage :
  iconimage = Oo
 if not "http" in fanart :
  fanart = I11i
 I1III = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 OO0O0OoOO0 = True
 iiiI1I11i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iiiI1I11i1 . setProperty ( "fanart_Image" , fanart )
 iiiI1I11i1 . setProperty ( "icon_Image" , iconimage )
 iiiI1I11i1 . setInfo ( 'video' , { 'Plot' : description } )
 I1IiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( '889' ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart )
 iiiI1I11i1 . addContextMenuItems ( [ ( '[COLOR pink]Add To Bishop Favourites[/COLOR]' , 'xbmc.RunPlugin(' + I1IiI + ')' ) ] )
 if 31 - 31: iIiiI1 . IiIiI11iIi / O0
 IIi1i11111 = xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
 OO0O0OoOO0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1III , listitem = iiiI1I11i1 , isFolder = False )
 return OO0O0OoOO0
 if 89 - 89: IiIiI11iIi
 if 68 - 68: Oo0oO0ooo * OoooooooOO % O0 + Oo0oO0ooo + OoOooOOOO
def i11i1I1 ( txt ) :
 if 36 - 36: iIii1I11I1II1 / IiIiI11iIi * I11
 txt = txt . replace ( "&quot;" , "\"" )
 txt = txt . replace ( "&amp;" , "&" )
 txt = txt . replace ( u"\u2018" , "'" ) . replace ( u"\u2019" , "'" )
 txt = txt . strip ( )
 return txt
 if 65 - 65: O0o . iIii1I11I1II1 / O0 - O0o
def iii1i1iiiiIi ( string ) :
 Iiii = ( c for c in string if 0 < ord ( c ) < 127 )
 if 75 - 75: IiIiI11iIi % O0OOo % O0OOo . iIiiI1
 return '' . join ( Iiii )
 if 5 - 5: O0OOo * OoOooOOOO + IiIiI11iIi . I11 + IiIiI11iIi
def oO ( heading , text ) :
 if 7 - 7: O0OOo - iiI1i1
 text = text + "\n\nNews Updates Every 5 Seconds"
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 OOo00O0 = xbmcgui . Window ( id )
 ooOOOoO = 50
 while ( ooOOOoO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   ooOOOoO -= 1
   OOo00O0 . getControl ( 1 ) . setLabel ( heading )
   OOo00O0 . getControl ( 5 ) . setText ( text )
   quit ( )
   return
  except : pass
  if 67 - 67: iIiiI1 . I1i1I . O0
def IIIIiiII111 ( name , url , iconimage ) :
 if 97 - 97: O0Oooo00 + I11 / iIii1I11I1II1 / I1i1I
 iI111iI . notification ( iIiiiI1IiI1I1 , '[COLOR pink]Attempting To Resolve Link Now[/COLOR]' , Oo , 5000 )
 if resolveurl . HostedMediaFile ( url ) . valid_url ( ) :
  I1111IIi = resolveurl . HostedMediaFile ( url ) . resolve ( )
  iiiI1I11i1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  iiiI1I11i1 . setPath ( I1111IIi )
  xbmc . Player ( ) . play ( I1111IIi , iiiI1I11i1 , False )
  quit ( )
 else :
  I1111IIi = url
  iiiI1I11i1 = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  iiiI1I11i1 . setPath ( I1111IIi )
  xbmc . Player ( ) . play ( I1111IIi , iiiI1I11i1 , False )
  quit ( )
  if 93 - 93: OoooooooOO / iiI1i1 % i11iIiiIii + O0Oooo00 * Oo0oO0ooo
def i111I ( ) :
 if 15 - 15: iiiii11iII1 . Oo0oO0ooo / oO0o + iiiii11iII1
 Ooo = open ( o0OOO ) . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  OOOOo = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Ooo ) [ 0 ]
  if OOOOo == 'EXPIRED' :
   iI111iI . ok ( iIiiiI1IiI1I1 , "[COLOR pink]Please visit [COLOR yellow]https://pinsystem.co.uk[COLOR pink] to generate a Pin to access Bash The Bishop then enter it after clicking ok[/COLOR]" )
   oo0O0oO = ''
   ooooo = xbmc . Keyboard ( oo0O0oO , '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]' )
   ooooo . doModal ( )
   if ooooo . isConfirmed ( ) :
    oo0O0oO = ooooo . getText ( )
    if len ( oo0O0oO ) > 1 :
     II1I = oo0O0oO . title ( )
     with open ( o0OOO , "w" ) as IIII :
      IIII . write ( "<pin>" + II1I + "</pin>" )
     i111I ( )
    else : quit ( )
   else :
    quit ( )
  if not 'EXPIRED' in OOOOo :
   O0i1II1Iiii1I11 = re . compile ( '<pin>(.+?)</pin>' ) . findall ( Ooo ) [ 0 ]
   IIIIiiIiI = ( 'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % O0i1II1Iiii1I11 )
   I11II1i = IIIII ( IIIIiiIiI )
   if 'Pin Verified' in I11II1i :
    pass
   else :
    with open ( o0OOO , "w" ) as IIII :
     IIII . write ( '<pin>EXPIRED</pin>' )
     i111I ( )
 except IndexError :
  with open ( o0OOO , "w" ) as IIII :
   IIII . write ( "<pin>EXPIRED</pin>\n" )
  i111I ( )
  if 91 - 91: I1i1I % i1IIi % iIii1I11I1II1
def IIi1I11I1II ( ) :
 if 63 - 63: OoooooooOO - Oo0oO0ooo . Ii11111i / O0OOo . IiIiI11iIi / O0
 xbmc . executebuiltin ( "XBMC.Container.Update(path,replace)" )
 xbmc . executebuiltin ( "XBMC.ActivateWindow(Home)" )
 if 84 - 84: OoOoo0
def iII11i ( ) :
 if 86 - 86: IiIiI11iIi - O0o - Oo0oO0ooo * I1i1I
 oooo0O0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 oOOO = float ( oooo0O0 [ : 4 ] )
 if oOOO >= 11.0 and oOOO <= 11.9 :
  iIII1 = 'Eden'
 elif oOOO >= 12.0 and oOOO <= 12.9 :
  iIII1 = 'Frodo'
 elif oOOO >= 13.0 and oOOO <= 13.9 :
  iIII1 = 'Gotham'
 elif oOOO >= 14.0 and oOOO <= 14.9 :
  iIII1 = 'Helix'
 elif oOOO >= 15.0 and oOOO <= 15.9 :
  iIII1 = 'Isengard'
 elif oOOO >= 16.0 and oOOO <= 16.9 :
  iIII1 = 'Jarvis'
 elif oOOO >= 17.0 and oOOO <= 17.9 :
  iIII1 = 'Krypton'
 else : iIII1 = "Decline"
 if 65 - 65: O0
 if iIII1 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif iIII1 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 if 68 - 68: I11 % iIiiI1
def oOoOooOo0o0 ( text ) :
 if 88 - 88: iIii1I11I1II1 - OoOooOOOO + I11
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
 text = iii1i1iiiiIi ( text )
 return text
 if 40 - 40: iiI1i1 * O0o + I11 % I1i1I
def OOOOOoo0 ( ) :
 if 49 - 49: O0 . I1i1I
 i1iII1IiiIiI1 . openSettings ( )
 if 11 - 11: OoOoo0 * iiI1i1 . iIii1I11I1II1 % OoooooooOO + I1i1I
def OOOoo0OOo0 ( ) :
 if 47 - 47: iIiiI1 + IiIiI11iIi * oO0o / OoOooOOOO - I1i1I % iIii1I11I1II1
 IIi11i1i1iI1 = [ ]
 iiiIi1 = sys . argv [ 2 ]
 if len ( iiiIi1 ) >= 2 :
  i1I1ii11i1Iii = sys . argv [ 2 ]
  I1IiiiiI = i1I1ii11i1Iii . replace ( '?' , '' )
  if ( i1I1ii11i1Iii [ len ( i1I1ii11i1Iii ) - 1 ] == '/' ) :
   i1I1ii11i1Iii = i1I1ii11i1Iii [ 0 : len ( i1I1ii11i1Iii ) - 2 ]
  o0O = I1IiiiiI . split ( '&' )
  IIi11i1i1iI1 = { }
  for IiIIii1iII1II in range ( len ( o0O ) ) :
   Iii1I1I11iiI1 = { }
   Iii1I1I11iiI1 = o0O [ IiIIii1iII1II ] . split ( '=' )
   if ( len ( Iii1I1I11iiI1 ) ) == 2 :
    IIi11i1i1iI1 [ Iii1I1I11iiI1 [ 0 ] ] = Iii1I1I11iiI1 [ 1 ]
 return IIi11i1i1iI1
 if 18 - 18: I11 + I1i1I - O0o . Ii11111i + i11iIiiIii
i1I1ii11i1Iii = OOOoo0OOo0 ( ) ; iiI1IiI = None ; iI1Ii1iI11iiI = None ; OO0OO0O00oO0 = None ; oOI1Ii1I1 = None ; o0oOo0Ooo0O = None ; IiII111iI1ii1 = None
try : oOI1Ii1I1 = urllib . unquote_plus ( i1I1ii11i1Iii [ "site" ] )
except : pass
try : iiI1IiI = urllib . unquote_plus ( i1I1ii11i1Iii [ "url" ] )
except : pass
try : iI1Ii1iI11iiI = urllib . unquote_plus ( i1I1ii11i1Iii [ "name" ] )
except : pass
try : OO0OO0O00oO0 = int ( i1I1ii11i1Iii [ "mode" ] )
except : pass
try : o0oOo0Ooo0O = urllib . unquote_plus ( i1I1ii11i1Iii [ "iconimage" ] )
except : pass
try : O0O = urllib . unquote_plus ( i1I1ii11i1Iii [ "fanart" ] )
except : pass
try : IiII111iI1ii1 = urllib . unquote_plus ( i1I1ii11i1Iii [ "description" ] )
except : pass
if 37 - 37: oo00 - iIiiI1 % oO0o
if OO0OO0O00oO0 == None or iiI1IiI == None or len ( iiI1IiI ) < 1 : o0ooo00O0o0 ( )
if 77 - 77: oO0o - i1IIi - iiiii11iII1 . IiIiI11iIi
elif OO0OO0O00oO0 == 1 : o0o00o0 ( iiI1IiI )
elif OO0OO0O00oO0 == 2 : O000OO0 ( iiI1IiI )
elif OO0OO0O00oO0 == 3 : O000oo0O ( iiI1IiI )
elif OO0OO0O00oO0 == 4 : i1I1iI ( iiI1IiI )
elif OO0OO0O00oO0 == 5 : Ii11Ii1I ( iiI1IiI )
elif OO0OO0O00oO0 == 6 : Oo0O0O0ooO0O ( iiI1IiI )
elif OO0OO0O00oO0 == 7 : oo000OO00Oo ( iiI1IiI )
if 39 - 39: Ii11111i / OoOooOOOO + iIiiI1 / IiIiI11iIi
if 13 - 13: OoOoo0 + O0 + I1i1I % iiI1i1 / O0OOo . OoOoo0
if 86 - 86: oo00 * O0OOo % i1IIi . O0o . i11iIiiIii
if 56 - 56: O0Oooo00 % O0 - iiI1i1
elif OO0OO0O00oO0 == 98 : Ii1iIiII1ii1 ( iI1Ii1iI11iiI , iiI1IiI , o0oOo0Ooo0O , IiII111iI1ii1 )
elif OO0OO0O00oO0 == 99 : IIIIiiII111 ( iI1Ii1iI11iiI , iiI1IiI , o0oOo0Ooo0O )
elif OO0OO0O00oO0 == 889 : Oo0o0000o0o0 ( iiI1IiI , OO0OO0O00oO0 , iI1Ii1iI11iiI , o0oOo0Ooo0O , O0O )
elif OO0OO0O00oO0 == 890 : i11iiII ( )
elif OO0OO0O00oO0 == 891 : REMFAVS ( iI1Ii1iI11iiI , iiI1IiI , o0oOo0Ooo0O )
elif OO0OO0O00oO0 == 892 : OOOOOoo0 ( )
elif OO0OO0O00oO0 == 893 : ii1I ( )
elif OO0OO0O00oO0 == 911 : IIi1I11I1II ( )
if 100 - 100: O0o - O0 % oo00 * I11 + iiI1i1
if 88 - 88: OoooooooOO - Oo0oO0ooo * O0 * OoooooooOO . OoooooooOO
if OO0OO0O00oO0 == None or iiI1IiI == None or len ( iiI1IiI ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True )
if 33 - 33: iIiiI1 + I1i1I * oo00 / iIii1I11I1II1 - iiI1i1
if 54 - 54: iIiiI1 / I11 . oo00 % I1i1I
if 57 - 57: i11iIiiIii . O0Oooo00 - O0o - oo00 + IiIiI11iIi
if 63 - 63: IiIiI11iIi * I1i1I
if 69 - 69: O0 . Oo0oO0ooo
if 49 - 49: iiI1i1 - iiiii11iII1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
