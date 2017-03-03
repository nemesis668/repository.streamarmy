import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , shutil , urlresolver , random , liveresolver , hashlib
from resources . libs . common_addon import Addon
from resources . libs . modules import regex
import base64
from metahandler import metahandlers
import os
if 64 - 64: i11iIiiIii
#################################################################
#                     STREAM ARMY BASE CODE                     # 
#                                                               #
#                                                               #
#                                                               #
#################################################################
#                     MODDED BY @NEMZZY668                      # 
#                              &                                #
#                           @_Manc_                             #
#                                                               #
#################################################################
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
I1IiI = 'plugin.video.streamarmy'
o0OOO = Addon ( I1IiI , sys . argv )
iIiiiI = xbmcaddon . Addon ( id = I1IiI )
Iii1ii1II11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
iI111iI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'fanart.jpg' ) )
IiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'icon.png' ) )
iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'search.jpg' ) )
i1i1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + I1IiI , 'next.png' ) )
O0oo0OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' , 'plugin.video.sportsdevil' ) )
I1i1iiI1 = base64 . b64decode ( b'aHR0cDovL3d3dy5zdHJlYW1hcm15LnVrL01haW4vTWVudS54bWw=' )
iiIIIII1i1iI = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
o0oO0 = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
oo00 = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
o00 = '&part=snippet&playlistId='
Oo0oO0ooo = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
o0oOoO00o = iIiiiI . getSetting ( 'password' )
i1 = iIiiiI . getSetting ( 'Conspiracy Password' )
oOOoo00O0O = iIiiiI . getSetting ( 'enable_meta' )
i1111 = 'http://pastebin.com/raw/4B2BhvJz'
i11 = base64 . b64decode ( b'aHR0cDovL2dldGFmbGl4LnVzL2FkZG9uL3lvdXR1YmUucGhw' )
I11 = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmcgui . DialogProgress ( )
oOo0oooo00o = 'http://www.streamarmy.uk/Main/Exceptions/Exceptions.xml'
oO0o0o0ooO0oO = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"
oo0o0O00 = [ "aliez" , "alldebrid" , "allvid" , "anistream" , "anyfiles" , "apnasave" , "blazefile" , "castamp" , "clicknupload" , "cloudmailru" , "cloudy" , "daclips" , "dailymotion" , "divxstage" , "ecostream" , "estream" , "exashare" , "facebook" , "fastplay" , "filepup" , "fileweed" , "flashx" , "googlevideo" , "gorillavid" , "grifthost" , "hugefiles" , "indavideo" , "jetload" , "kingfiles" , "letwatch" , "letwatch" , "mailru" , "megadebrid" , "megamp" , "mersalaayitten" , "movdivx" , "movpod" , "movshare" , "mpengine" , "mpstream" , "mpupload" , "myvidstream" , "nosvideo" , "novamov" , "nowvideo" , "ok" , "ol_gmu" , "ol_openload" , "play_net" , "play_playedto" , "playhd" , "playwire" , "premiumize_me" , "purevid" , "putload" , "rapidvideo" , "rapidvideocom" , "realdebrid" , "rpnet" , "rutube" , "simplydebrid" , "speedplay" , "speedvideo" , "stagevu" , "streamcloud" , "streamenet" , "streaminto" , "streamplay" , "teramixer" , "thevid" , "thevideo" , "thevideos" , "trollvid" , "tudou" , "tunepk" , "tusfiles" , "twitch" , "uploadaf" , "uploadx" , "uploadz" , "uptobox" , "userscloud" , "usersfiles" , "veeHD" , "veeHD" , "oveoh" , "vidabc" , "vidcrazynet" , "videa" , "videobee" , "videocloud" , "videoget" , "videohut" , "videoraj" , "videorev" , "videoweed" , "videowood" , "videozoo" , "vidlox" , "vidmad" , "vidme" , "vidto" , "vidtodo" , "vidup_me" , "vidup_vidup_org" , "vidup_vidzi" , "vimeo" , "vivosx" , "vk" , "vshare" , "vshareeu" , "watchers" , "watchonline" , "watchpass" , "watchvideo" , "weshare" , "xvidstage" , "yourupload" , "youtube" , "youwatch" , "zevera" , "zstream" ]
if 68 - 68: o00oo . iI1 + OoOooOOOO
if 45 - 45: OoOO + I1iiiiI1iII
def IiIi11i ( link , splitting = '\n' ) :
 iIii1I111I11I = urllib2 . Request ( link )
 try :
  OO00OooO0OO = urllib2 . urlopen ( iIii1I111I11I )
 except IOError :
  return [ ]
  if 28 - 28: iIii1
 else :
  oOOoO0 = OO00OooO0OO . read ( )
  return oOOoO0 . split ( splitting )
  if 59 - 59: oO * O0OOooO % I1IiiI . OoO0O00 % OoooooooOO
iiIIiIiIi = IiIi11i ( oOo0oooo00o )
if 38 - 38: OoOO / Oo0Ooo
try :
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 70 - 70: o00oo / iIii1I11I1II1 % O0OOooO % i11iIiiIii . I1IiiI
 if II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  if 68 - 68: OoOooOOOO + iI1 . iIii1I11I1II1 - iIii1 % iIii1I11I1II1 - O0OOooO
  oOOO00o = [ "special://cache" ,
 "special://temp/" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/Other" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/LocalAndRental" ]
  if 97 - 97: OoOooOOOO % OoOooOOOO + II111iiii * I1iiiiI1iII
  for o0o00o0 in oOOO00o :
   if "special" in o0o00o0 :
    o0o00o0 = xbmc . translatePath ( o0o00o0 )
   if os . path . exists ( o0o00o0 ) :
    iIi1ii1I1 = os . path . join ( o0o00o0 , "archive_cache" )
    if not os . path . exists ( iIi1ii1I1 ) :
     os . makedirs ( iIi1ii1I1 )
except : pass
if 71 - 71: oO . O0
def o0OO0oo0oOO ( input_data , key ) :
 if 54 - 54: I1IiiI % II111iiii % II111iiii
 iI1i11Iiii = ""
 for iI in input_data :
  iI1i11Iiii += chr ( ord ( iI ) ^ key )
  if 28 - 28: iI1 - iIii1 . iIii1 + OoOoOO00 - OoooooooOO + O0
 return iI1i11Iiii
 if 95 - 95: OoO0O00 % o00oo . O0
def I1i1I ( input_data , password ) :
 if 80 - 80: OoOoOO00 - OoO0O00
 OOO00 = 0
 for iI in password :
  OOO00 ^= ( ( 2 * ord ( iI ) + 3 ) & 0xff )
  if 21 - 21: OoooooooOO - OoooooooOO
 return o0OO0oo0oOO ( input_data , OOO00 )
 if 8 - 8: OoOoOO00
def o00O ( input_data , password = base64 . b64decode ( b"bGl2ZXJwb29s" ) ) :
 if 69 - 69: o00oo % oO - o0oOOo0O0Ooo + oO - O0 % OoooooooOO
 return I1i1I ( input_data , password )
 if 31 - 31: II111iiii - iI1 . oO % OoOoOO00 - O0
def iii11 ( text ) :
 if 58 - 58: iI1 * i11iIiiIii / OoOoOO00 % oO - I1ii11iIi11i / o00oo
 text = str ( text )
 text = text . replace ( '\\r' , '' )
 text = text . replace ( '\\n' , '' )
 text = text . replace ( '\\t' , '' )
 text = text . replace ( '\\' , '' )
 text = text . replace ( '<br />' , '\n' )
 text = text . replace ( '<hr />' , '' )
 text = text . replace ( '&#039;' , "'" )
 text = text . replace ( '&quot;' , '"' )
 text = text . replace ( '&rsquo;' , "'" )
 text = text . replace ( '&amp;' , "&" )
 text = text . replace ( '&#8211;' , "&" )
 text = text . replace ( '&#8217;' , "'" )
 text = text . replace ( '&#038;' , "&" )
 text = text . lstrip ( ' ' )
 text = text . lstrip ( '	' )
 if 50 - 50: I1IiiI
 return text
 if 34 - 34: I1IiiI * II111iiii % I1iiiiI1iII * OoOoOO00 - I1IiiI
def II1III ( ) :
 if 19 - 19: o00oo % i1IIi % o0oOOo0O0Ooo
 oo0OooOOo0 = xbmc . translatePath ( 'special://home/addons/' + I1IiI + '/addon.xml' )
 o0O = open ( oo0OooOOo0 ) . read ( )
 O00oO = o0O . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 I11i1I1I = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( O00oO ) )
 for oO0Oo in I11i1I1I :
  oOOoo0Oo = oO0Oo
  if 78 - 78: OoOooOOOO
 OO00Oo = "https://raw.githubusercontent.com/nemesis668/repository.streamarmy/master/addons.xml"
 if 51 - 51: iIii1 * o0oOOo0O0Ooo + OoOooOOOO + OoO0O00
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<addon id="' + I1IiI + '" name=".+?" version="(.+?)" provider-name=".+?">' ) . findall ( o0O0O00 ) [ 0 ]
 if 7 - 7: O0OOooO * OoO0O00 % o00oo . iIii1
 Ii1iIiII1ii1 ( '[B][COLOR lime]Your Current Version: ' + str ( oOOoo0Oo ) + '[/COLOR] | [COLOR yellow]Our Latest Version: ' + I11i1I1I + '[/COLOR][/B]' , 'url' , 999 , IiII , iI111iI )
 if 62 - 62: iIii1I11I1II1 * OoOoOO00
 i1OOO ( )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 OO00Oo = I1i1iiI1
 o0O0O00 = Oo0oOOo ( I1i1iiI1 )
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 58 - 58: II111iiii * iI1 * I1ii11iIi11i / iI1
 for oO0Oo in I11i1I1I :
  try :
   if '<m3u>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 11 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<changelog>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<changelog>(.+?)</changelog>' ) . findall ( oO0Oo ) [ 0 ]
    Ii1iIiII1ii1 ( oO0o0OOOO , OO00Oo , 45 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<pornscrape>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 16 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<soccerstreams>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 55 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<afdah>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 52 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<top40>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 46 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<pornhd>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 41 , O0O0OoOO0 , Iii1ii1II11i , '' )
   elif '<docs>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 24 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<anime>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 32 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<cartoons>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 35 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<comics>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 38 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<filmon>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 26 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<music>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 28 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<hdmovies>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 49 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<channel>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 6 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<tvput>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<tvputsput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 13 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<moviescrape>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 15 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<moviescrapenorm>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 22 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<sportsdevil>' in oO0Oo :
    IIi1i11111 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     OO00Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     ooOO00O00oo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iI = ooOO00O00oo
     IIi1i = "/"
     if not I1ii11iI . endswith ( IIi1i ) :
      I1I1iIiII1 = I1ii11iI + "/"
     else :
      I1I1iIiII1 = I1ii11iI
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OO00Oo
     OO00Oo = o0O0O00 + '%26referer=' + I1I1iIiII1
     Ii1iIiII1ii1 ( oO0o0OOOO , OO00Oo , 4 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( IIi1i11111 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( oO0o0OOOO , i11i1I1 , 8 , O0O0OoOO0 , Iii1ii1II11i )
     if 36 - 36: iIii1I11I1II1 / OoOoOO00 * iI1
   elif '<folder>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    i11i1I1 = re . compile ( '<folder>(.+?)</folder>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    if 65 - 65: OoOO . iIii1I11I1II1 / O0 - OoOO
    if i11i1I1 in iiIIiIiIi :
     iiiI1I11i1 ( oO0o0OOOO , i11i1I1 , 1 , O0O0OoOO0 , Iii1ii1II11i )
    else :
     iiiI1I11i1 ( oO0o0OOOO , i11i1I1 , 20 , O0O0OoOO0 , Iii1ii1II11i )
   else :
    if 21 - 21: I1IiiI * iIii1I11I1II1
    IIi1i11111 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     oooooOoo0ooo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     I1I1IiI1 = len ( I11i1I1I )
     for oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i in oooooOoo0ooo :
      if 'youtube.com/playlist' in OO00Oo :
       iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
      else :
       III1iII1I1ii ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( IIi1i11111 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     III1iII1I1ii ( oO0o0OOOO , i11i1I1 , 3 , O0O0OoOO0 , Iii1ii1II11i )
     if 61 - 61: II111iiii
     if 64 - 64: O0OOooO / OoOoOO00 - O0 - OoOooOOOO
  except : pass
  if 86 - 86: OoOooOOOO % OoOoOO00 / I1IiiI / OoOoOO00
  iIIi1i1 ( )
  if 10 - 10: OoOooOOOO
def OOooOO000 ( url ) :
 if 97 - 97: I1ii11iIi11i + iI1 / iIii1I11I1II1 / I1iiiiI1iII
 I1111IIi = Oo0oO ( url )
 IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , I1111IIi )
 if 35 - 35: OoOO % O0 - O0
def i1OOO ( ) :
 I1111IIi = Oo0oO ( i1111 )
 if len ( I1111IIi ) > 1 :
  IiIIIi1iIi = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  ooOOoooooo = os . path . join ( os . path . join ( IiIIIi1iIi , '' ) , 'compare.txt' )
  II1I = open ( ooOOoooooo )
  O0i1II1Iiii1I11 = II1I . read ( )
  if O0i1II1Iiii1I11 == I1111IIi : pass
  else :
   IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , I1111IIi )
   IIII = open ( ooOOoooooo , "w" )
   IIII . write ( I1111IIi )
   IIII . close ( )
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
def o00oooO0Oo ( name , url , iconimage , fanart ) :
 i11i1I1 = url
 o0O0O00 = o000o ( url )
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
    iIiiiI . setSetting ( 'password' , I1 )
   else : quit ( )
   if 86 - 86: OoOoOO00 - OoOO - OoO0O00 * I1iiiiI1iII
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
   if I1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 66 - 66: OoooooooOO + O0
 if 'con>yes</con' in o0O0O00 :
  if i1 == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , I1IiiIIIi )
   else : quit ( )
   if 41 - 41: OoOO - O0 - O0
 if 'con>yes</con' in o0O0O00 :
  if i1 <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
   if I1IiiIIIi <> i1 :
    quit ( )
  else : quit ( )
  if 68 - 68: iI1 % oO
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 88 - 88: iIii1I11I1II1 - O0OOooO + iI1
 if 40 - 40: I1IiiI * OoOO + iI1 % I1iiiiI1iII
 if 74 - 74: o00oo - Oo0Ooo + OoooooooOO + oO / OoOoOO00
 for oO0Oo in I11i1I1I :
  try :
   if 23 - 23: O0
   if '<regex>' in oO0Oo :
    o00oO0oOo00 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0Oo )
    o00oO0oOo00 = '' . join ( o00oO0oOo00 )
    oO0oOo0 = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( o00oO0oOo00 )
    o00oO0oOo00 = urllib . quote_plus ( o00oO0oOo00 )
    if 45 - 45: I1iiiiI1iII / I1iiiiI1iII + oO + O0OOooO
    iI111i = hashlib . md5 ( )
    for IIi11i1i1iI1 in o00oO0oOo00 : iI111i . update ( str ( IIi11i1i1iI1 ) )
    iI111i = str ( iI111i . hexdigest ( ) )
    if 23 - 23: i11iIiiIii + o0oOOo0O0Ooo . i1IIi
    oO0Oo = oO0Oo . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    oO0Oo = re . sub ( '<regex>.+?</regex>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<link></link>' , '' , oO0Oo )
    if 100 - 100: oO . o00oo * OoOO
    name = re . sub ( '<meta>.+?</meta>' , '' , oO0Oo )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 14 - 14: iI1 % iIii1I11I1II1
    try : oo = re . findall ( '<date>(.+?)</date>' , oO0Oo ) [ 0 ]
    except : oo = ''
    if re . search ( r'\d+' , oo ) : name += ' [COLOR red] Updated %s[/COLOR]' % oo
    if 26 - 26: OoOooOOOO - iIii1I11I1II1 - I1IiiI / OoO0O00 . OoOoOO00 % iIii1I11I1II1
    try : OO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , oO0Oo ) [ 0 ]
    except : OO = IiII
    if 25 - 25: OoO0O00
    try : oOo0oO = re . findall ( '<fanart>(.+?)</fanart>' , oO0Oo ) [ 0 ]
    except : oOo0oO = iI111iI
    if 51 - 51: Oo0Ooo - o00oo + II111iiii * OoOO . OoOooOOOO + o00oo
    try : OoO0o = re . findall ( '<meta>(.+?)</meta>' , oO0Oo ) [ 0 ]
    except : OoO0o = '0'
    if 78 - 78: o00oo % O0 % OoOO
    try : url = re . findall ( '<link>(.+?)</link>' , oO0Oo ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % OoO0o )
    url = '<preset>search</preset>%s' % OoO0o if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % OoO0o )
    url = '<preset>searchsd</preset>%s' % OoO0o if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 46 - 46: OoooooooOO . i11iIiiIii
    if not o00oO0oOo00 == '' :
     hash . append ( { 'regex' : iI111i , 'response' : o00oO0oOo00 } )
     url += '|regex=%s' % o00oO0oOo00
     if 94 - 94: o0oOOo0O0Ooo * OoOO / Oo0Ooo / OoOO
    oO0 ( name , url , 10 , OO , oOo0oO , "" )
    if 75 - 75: O0OOooO + OoOoOO00 + o0oOOo0O0Ooo * OoOooOOOO % o00oo . I1iiiiI1iII
   elif '<sportsmama>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmama>(.+?)</sportsmama>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<hdmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 49 , iconimage , fanart )
   elif '<afdah>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 52 , iconimage , fanart )
   elif '<soccerstreams>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
   elif '<top40>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 46 , iconimage , fanart )
   elif '<pornhd>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 41 , iconimage , fanart , '' )
   elif '<m3u>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 11 , iconimage , fanart )
   elif '<anime>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 35 , iconimage , fanart )
   elif '<docs>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 24 , iconimage , fanart )
   elif '<filmon>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 26 , iconimage , fanart )
   elif '<music>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 28 , iconimage , fanart )
   elif '<pornscrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 16 , iconimage , fanart )
   elif '<tvput>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 13 , iconimage , fanart )
   elif '<moviescrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 22 , iconimage , fanart )
   elif '<channel>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in oO0Oo :
    IIi1i11111 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     ooOO00O00oo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iI = ooOO00O00oo
     IIi1i = "/"
     if not I1ii11iI . endswith ( IIi1i ) :
      I1I1iIiII1 = I1ii11iI + "/"
     else :
      I1I1iIiII1 = I1ii11iI
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + I1I1iIiII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( IIi1i11111 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , i11i1I1 , 8 , iconimage , fanart )
     if 55 - 55: iI1 . I1IiiI
   elif '<folder>' in oO0Oo :
    oooooOoo0ooo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in oooooOoo0ooo :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
      if 61 - 61: Oo0Ooo % iIii1 . Oo0Ooo
   else :
    IIi1i11111 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     oooooOoo0ooo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     I1I1IiI1 = len ( I11i1I1I )
     for name , url , iconimage , fanart in oooooOoo0ooo :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       III1iII1I1ii ( name , url , 2 , iconimage , fanart )
    elif len ( IIi1i11111 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     III1iII1I1ii ( name , i11i1I1 , 3 , iconimage , fanart )
  except : pass
 iIIi1i1 ( )
 if 100 - 100: oO * O0
def o00oO0oo0OO ( name , url , iconimage , fanart ) :
 if 57 - 57: oO % OoOO + o0oOOo0O0Ooo - Oo0Ooo
 if 65 - 65: OoOooOOOO . OoOoOO00
 i11i1I1 = url
 o0O0O00 = Oo0oOOo ( url )
 if 39 - 39: II111iiii / O0OOooO + oO / OoOoOO00
 if 13 - 13: iIii1 + O0 + I1iiiiI1iII % I1IiiI / o0oOOo0O0Ooo . iIii1
 if 86 - 86: o00oo * o0oOOo0O0Ooo % i1IIi . OoOO . i11iIiiIii
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   else : quit ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
    iIiiiI . setSetting ( 'password' , I1 )
   else : quit ( )
   if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 if 'XXX>yes</XXX' in o0O0O00 :
  if o0oOoO00o <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   else : quit ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1 = iiIiI . getText ( )
   if I1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 100 - 100: OoOO - O0 % o00oo * iI1 + I1IiiI
 if 'con>yes</con' in o0O0O00 :
  if i1 == '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Set Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , I1IiiIIIi )
   else : quit ( )
   if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if 'con>yes</con' in o0O0O00 :
  if i1 <> '' :
   I11 = xbmcgui . Dialog ( )
   o0O0OOO0Ooo = I11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if o0O0OOO0Ooo == 1 :
    iiIiI = xbmc . Keyboard ( '' , 'Enter Password' )
    iiIiI . doModal ( )
   if ( iiIiI . isConfirmed ( ) ) :
    I1IiiIIIi = iiIiI . getText ( )
   if I1IiiIIIi <> i1 :
    quit ( )
  else : quit ( )
  if 33 - 33: oO + I1iiiiI1iII * o00oo / iIii1I11I1II1 - I1IiiI
 I11i1I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 for oO0Oo in I11i1I1I :
  try :
   if 54 - 54: oO / iI1 . o00oo % I1iiiiI1iII
   if '<regex>' in oO0Oo :
    o00oO0oOo00 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0Oo )
    o00oO0oOo00 = '' . join ( o00oO0oOo00 )
    oO0oOo0 = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( o00oO0oOo00 )
    o00oO0oOo00 = urllib . quote_plus ( o00oO0oOo00 )
    if 57 - 57: i11iIiiIii . I1ii11iIi11i - OoOO - o00oo + OoOoOO00
    iI111i = hashlib . md5 ( )
    for IIi11i1i1iI1 in o00oO0oOo00 : iI111i . update ( str ( IIi11i1i1iI1 ) )
    iI111i = str ( iI111i . hexdigest ( ) )
    if 63 - 63: OoOoOO00 * I1iiiiI1iII
    oO0Oo = oO0Oo . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    oO0Oo = re . sub ( '<regex>.+?</regex>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , oO0Oo )
    oO0Oo = re . sub ( '<link></link>' , '' , oO0Oo )
    if 69 - 69: O0 . OoO0O00
    name = re . sub ( '<meta>.+?</meta>' , '' , oO0Oo )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 49 - 49: I1IiiI - OoOooOOOO
    try : oo = re . findall ( '<date>(.+?)</date>' , oO0Oo ) [ 0 ]
    except : oo = ''
    if re . search ( r'\d+' , oo ) : name += ' [COLOR red] Updated %s[/COLOR]' % oo
    if 74 - 74: iIii1I11I1II1 * I1ii11iIi11i + OoOoOO00 / i1IIi / II111iiii . Oo0Ooo
    try : OO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , oO0Oo ) [ 0 ]
    except : OO = IiII
    if 62 - 62: OoooooooOO * I1IiiI
    try : oOo0oO = re . findall ( '<fanart>(.+?)</fanart>' , oO0Oo ) [ 0 ]
    except : oOo0oO = iI111iI
    if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
    try : OoO0o = re . findall ( '<meta>(.+?)</meta>' , oO0Oo ) [ 0 ]
    except : OoO0o = '0'
    if 50 - 50: oO . o0oOOo0O0Ooo
    try : url = re . findall ( '<link>(.+?)</link>' , oO0Oo ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % OoO0o )
    url = '<preset>search</preset>%s' % OoO0o if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % OoO0o )
    url = '<preset>searchsd</preset>%s' % OoO0o if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 97 - 97: O0 + OoOoOO00
    if not o00oO0oOo00 == '' :
     hash . append ( { 'regex' : iI111i , 'response' : o00oO0oOo00 } )
     url += '|regex=%s' % o00oO0oOo00
     if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * OoOooOOOO * OoOO
    oO0 ( name , url , 10 , OO , oOo0oO , "" )
    if 37 - 37: OoooooooOO - O0 - o0oOOo0O0Ooo
   elif '<sportsmama>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmama>(.+?)</sportsmama>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<hdmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 49 , iconimage , fanart )
   elif '<pornhd>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 41 , iconimage , fanart , '' )
   elif '<soccerstreams>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 55 , iconimage , fanart )
   elif '<afdah>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<afdah>(.+?)</afdah>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 52 , iconimage , fanart )
   elif '<top40>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<top40>(.+?)</top40>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 46 , iconimage , fanart )
   elif '<m3u>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 11 , iconimage , fanart )
   elif '<docs>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 24 , iconimage , fanart )
   elif '<anime>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 35 , iconimage , fanart )
   elif '<music>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 28 , iconimage , fanart )
   elif '<filmon>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 26 , iconimage , fanart )
   elif '<tvput>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 13 , iconimage , fanart )
   elif '<pornscrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 16 , iconimage , fanart )
   elif '<moviescrape>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 22 , iconimage , fanart )
   elif '<moviessearch>yes</moviessearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , 'url' , 23 , iconimage , fanart )
   elif '<channel>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in oO0Oo :
    IIi1i11111 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     ooOO00O00oo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     I1ii11iI = ooOO00O00oo
     IIi1i = "/"
     if not I1ii11iI . endswith ( IIi1i ) :
      I1I1iIiII1 = I1ii11iI + "/"
     else :
      I1I1iIiII1 = I1ii11iI
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + I1I1iIiII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( IIi1i11111 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , i11i1I1 , 8 , iconimage , fanart )
     if 77 - 77: iI1 * iIii1I11I1II1
   elif '<folder>' in oO0Oo :
    oooooOoo0ooo = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in oooooOoo0ooo :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
   else :
    IIi1i11111 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( IIi1i11111 ) == 1 :
     oooooOoo0ooo = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     I1I1IiI1 = len ( I11i1I1I )
     for name , url , iconimage , fanart in oooooOoo0ooo :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       III1iII1I1ii ( name , url , 2 , iconimage , fanart )
    elif len ( IIi1i11111 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     III1iII1I1ii ( name , i11i1I1 , 3 , iconimage , fanart )
  except : pass
 iIIi1i1 ( )
 if 98 - 98: I1IiiI % OoOO * OoooooooOO
def Oo ( name , url , iconimage ) :
 if 34 - 34: o00oo + I1IiiI - o00oo
 II1I , IiI1I1i1I1 = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 II1I += urllib . unquote_plus ( IiI1I1i1I1 )
 url = regex . resolve ( II1I )
 if 98 - 98: OoOooOOOO % i11iIiiIii % O0OOooO + OoOO
 OOoOO0o0o0 ( name , url , iconimage )
 if 11 - 11: I1IiiI
def I1111i ( name , url , iconimage ) :
 if 14 - 14: iI1 / o0oOOo0O0Ooo
 iII11I1IiiIi = urllib2 . Request ( url )
 iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 OO00OooO0OO = o0O0O00
 OO00OooO0OO = OO00OooO0OO . replace ( '#AAASTREAM:' , '#A:' )
 OO00OooO0OO = OO00OooO0OO . replace ( '#EXTINF:' , '#A:' )
 oo0oO = re . compile ( '^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( OO00OooO0OO )
 Oo0O0 = [ ]
 for Ooo0OOoOoO0 , oOo0OOoO0 , url in oo0oO :
  II = { "params" : Ooo0OOoOoO0 , "display_name" : oOo0OOoO0 , "url" : url }
  Oo0O0 . append ( II )
 list = [ ]
 for o0Oo0oO0oOO00 in Oo0O0 :
  II = { "display_name" : o0Oo0oO0oOO00 [ "display_name" ] , "url" : o0Oo0oO0oOO00 [ "url" ] }
  oo0oO = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( o0Oo0oO0oOO00 [ "params" ] )
  for oo00OO0000oO , I1II1 in oo0oO :
   II [ oo00OO0000oO . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = I1II1 . strip ( )
  list . append ( II )
 for o0Oo0oO0oOO00 in list :
  name = oooO ( o0Oo0oO0oOO00 [ "display_name" ] )
  url = oooO ( o0Oo0oO0oOO00 [ "url" ] )
  url = url . replace ( '\\r' , '' ) . replace ( '\\t' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( ' ' , '' ) . replace ( 'm3u8' , 'm3u8' )
  oO0 ( name , url , 2 , IiII , Iii1ii1II11i , '' )
  if 26 - 26: OoOO % I1ii11iIi11i
def o00Oo0oooooo ( name , url , iconimage ) :
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 o0O0O00 = Oo0oOOo ( url )
 o00o = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o00o ) [ 0 ]
 IIi1i11111 = re . compile ( '<link>(.+?)</link>' ) . findall ( o00o )
 IIi11i1i1iI1 = 1
 for IIIIiiIiiI in IIi1i11111 :
  IIIIiI11I11 = IIIIiiIiiI
  if '(' in IIIIiiIiiI :
   IIIIiiIiiI = IIIIiiIiiI . split ( '(' ) [ 0 ]
   oo00o0 = str ( IIIIiI11I11 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   O0oO0 . append ( IIIIiiIiiI )
   iII11 . append ( oo00o0 )
  else :
   O0oO0 . append ( IIIIiiIiiI )
   iII11 . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 i11II1I11I1 = I11 . select ( name , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  url = O0oO0 [ i11II1I11I1 ]
  if 67 - 67: I1IiiI - o0oOOo0O0Ooo / OoOooOOOO - i1IIi
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : i1II1 = liveresolver . resolve ( url )
  else : i1II1 = url
  i11i1 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  i11i1 . setPath ( i1II1 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11i1 )
  if 42 - 42: i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . i11iIiiIii % OoOooOOOO
def i1iI ( name , url , iconimage ) :
 if 29 - 29: I1IiiI % iI1 - I1IiiI / iI1 . i1IIi
 if 31 - 31: oO
 OOO0000oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 iI1i111I1Ii = [ ]
 o0O0O00 = o000o ( url )
 o00o = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 IIi1i11111 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( o00o )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( o00o ) [ 0 ]
 IIi11i1i1iI1 = 1
 if 25 - 25: oO - I1iiiiI1iII
 for IIIIiiIiiI in IIi1i11111 :
  IIIIiI11I11 = IIIIiiIiiI
  if '(' in IIIIiiIiiI :
   IIIIiiIiiI = IIIIiiIiiI . split ( '(' ) [ 0 ]
   oo00o0 = str ( IIIIiI11I11 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   O0oO0 . append ( IIIIiiIiiI )
   iII11 . append ( oo00o0 )
   iI1i111I1Ii . append ( 'Stream ' + str ( IIi11i1i1iI1 ) )
  else :
   O0oO0 . append ( IIIIiiIiiI )
   iII11 . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
   if 10 - 10: II111iiii / o00oo % OoooooooOO * OoOooOOOO % I1ii11iIi11i
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 i11II1I11I1 = I11 . select ( name , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  I1ii11iI = iII11 [ i11II1I11I1 ]
  IIi1i = "/"
  if not I1ii11iI . endswith ( IIi1i ) :
   I1I1iIiII1 = I1ii11iI + "/"
  else :
   I1I1iIiII1 = I1ii11iI
  url = OOO0000oO + O0oO0 [ i11II1I11I1 ] + "%26referer=" + I1I1iIiII1
  print url
  if 48 - 48: O0OOooO / oO . iIii1I11I1II1 * OoOoOO00 * o00oo / i1IIi
  xbmc . Player ( ) . play ( url )
  if 92 - 92: Oo0Ooo % Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
  if 10 - 10: I1iiiiI1iII + Oo0Ooo * I1ii11iIi11i + iIii1I11I1II1 / oO / I1ii11iIi11i
  if 42 - 42: I1IiiI
  if 38 - 38: iI1 + II111iiii % O0OOooO % OoOoOO00 - OoOO / OoooooooOO
  if 73 - 73: o0oOOo0O0Ooo * O0 - i11iIiiIii
  if 85 - 85: OoOO % I1iiiiI1iII + OoOooOOOO / o0oOOo0O0Ooo . o00oo + iI1
  if 62 - 62: i11iIiiIii + i11iIiiIii - o0oOOo0O0Ooo
def I1OooooO0oOOOO ( ) :
 if 100 - 100: I1iiiiI1iII % iI1
 OO00Oo = 'http://www.animetoon.org/dubbed-anime'
 if 86 - 86: Oo0Ooo . O0 - OoooooooOO . OoO0O00 + OoOO
 o0O0O00 = o000o ( OO00Oo )
 OOo = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 22 - 22: OoOoOO00 * O0 . iIii1 * i11iIiiIii - I1IiiI * O0OOooO
 for IIi1i11111 in OOo :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OOooo0O0o0 = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + OOooo0O0o0 + "[/COLOR]" , OO00Oo , 33 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 14 - 14: o0oOOo0O0Ooo % O0 * I1iiiiI1iII + OoOO + Oo0Ooo * OoOO
def iII1I1IiI11ii ( url ) :
 if 72 - 72: I1IiiI % i11iIiiIii . Oo0Ooo / II111iiii
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 14 - 14: I1ii11iIi11i + OoO0O00
 for iIi in OOo :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 34 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 39 - 39: O0 + oO
def OoOooOoO ( name , url , iconimage ) :
 if 43 - 43: II111iiii . o00oo / I1ii11iIi11i
 o0O0O00 = o000o ( url )
 i1iI1 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 i11ii1ii11i ( name , i1iI1 , iconimage )
 if 70 - 70: i1IIi - I1iiiiI1iII + Oo0Ooo
 if 12 - 12: o0oOOo0O0Ooo - I1ii11iIi11i % OoOoOO00 * OoOooOOOO
 if 44 - 44: I1iiiiI1iII % OoOO
 if 41 - 41: i1IIi - OoOooOOOO - OoOO
 if 8 - 8: OoO0O00 + oO - o0oOOo0O0Ooo % Oo0Ooo % o0oOOo0O0Ooo * o00oo
 if 9 - 9: Oo0Ooo - i11iIiiIii - iI1 * OoOO + O0OOooO
 if 44 - 44: II111iiii
def OOOO0OOO ( ) :
 if 3 - 3: OoO0O00
 OO00Oo = 'http://www.toonget.net/cartoon'
 if 97 - 97: oO
 o0O0O00 = o000o ( OO00Oo )
 OOo = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 15 - 15: i1IIi + OoOoOO00
 for IIi1i11111 in OOo :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OOooo0O0o0 = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + OOooo0O0o0 + "[/COLOR]" , OO00Oo , 36 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 48 - 48: I1IiiI % I1iiiiI1iII / iIii1I11I1II1
def Oo0oooO0oO ( url ) :
 if 19 - 19: i11iIiiIii + OoooooooOO - Oo0Ooo - OoOooOOOO
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 21 - 21: O0 % iIii1 . I1IiiI / II111iiii + iIii1
 for iIi in OOo :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 37 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 53 - 53: o00oo - I1IiiI - o00oo * I1iiiiI1iII
def oooooo0OO ( name , url , iconimage ) :
 if 14 - 14: o00oo / o00oo % O0OOooO
 o0O0O00 = o000o ( url )
 i1iI1 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 i11ii1ii11i ( name , i1iI1 , iconimage )
 if 56 - 56: I1IiiI . O0 + Oo0Ooo
 if 1 - 1: I1iiiiI1iII
 if 97 - 97: iI1 + I1iiiiI1iII + O0 + i11iIiiIii
 if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . I1iiiiI1iII % I1iiiiI1iII + i11iIiiIii
 if 72 - 72: iIii1I11I1II1 * OoOO % O0OOooO / OoO0O00
 if 35 - 35: O0OOooO + i1IIi % I1ii11iIi11i % OoOooOOOO + o00oo
def iiiI ( ) :
 if 29 - 29: OoOooOOOO / II111iiii / O0OOooO * iI1
 OO00Oo = 'http://www.readcomics.tv/comic-list'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 10 - 10: oO % iIii1 * iIii1 . OoOooOOOO / OoOO % iI1
 for IIi1i11111 in OOo :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 39 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 49 - 49: OoO0O00 / o00oo + O0 * o0oOOo0O0Ooo
def I1ii11 ( url ) :
 if 74 - 74: Oo0Ooo - o0oOOo0O0Ooo . i1IIi
 o0O0O00 = o000o ( url )
 i1III = re . compile ( '<div class="manga-image"><img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oO0o0OOOO = re . compile ( '<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ] . replace ( 'Read ' , '' ) . replace ( 'Online' , '' )
 iii1Ii1Ii1 = re . compile ( '<a class="stread" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = iii1Ii1Ii1 . split ( '/' ) [ - 1 ]
 O00oO = o0O . replace ( 'chapter-' , ' ' )
 O00oO = int ( O00oO )
 iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , iii1Ii1Ii1 , 40 , i1III , iI111iI , '' )
 I11i1I1I = re . compile ( '<ul class="ml-list">(.+?)</ul>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 for IIi1i11111 in sorted ( OOo ) :
  O00oO = O00oO + 1
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , url , 40 , i1III , iI111iI , '' )
  if 21 - 21: o00oo . oO . iI1 / Oo0Ooo / oO
def i1iI1ii1 ( url ) :
 if 1 - 1: O0OOooO % iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % I1IiiI
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' )
 o0o0oOoOO0O = re . compile ( '<div class="label">of (.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 16 - 16: iIii1 % iIii1I11I1II1 . OoOO
 o0o0oOoOO0O = int ( o0o0oOoOO0O )
 oooooOOO000Oo = re . compile ( '<img id="main_img" src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = oooooOOO000Oo . replace ( '.jpg' , '' ) . replace ( 'http://' , '' )
 O00oO = o0O . split ( '/' )
 Ooo00OoOOO = len ( O00oO )
 Oo0OO0000oooo = Ooo00OoOOO - 1
 IIII1iII = 1
 ii1III11 = ""
 for I1iiIIIi11 in O00oO :
  if IIII1iII <= Oo0OO0000oooo :
   ii1III11 = ii1III11 + "/" + I1iiIIIi11
   IIII1iII = IIII1iII + 1
   if 12 - 12: OoooooooOO % o0oOOo0O0Ooo * OoOooOOOO % iIii1I11I1II1 / OoOO
 Ii1ii1IiIII = 1
 ii1III11 = "http://" + ii1III11 + "/"
 if 57 - 57: iIii1I11I1II1 / OoOooOOOO - i1IIi
 while Ii1ii1IiIII <= o0o0oOoOO0O :
  url = ii1III11 + str ( Ii1ii1IiIII ) + ".jpg"
  oO0 ( "[COLOR lime]Page " + str ( Ii1ii1IiIII ) + "[/COLOR]" , url , 9 , url , url , '' )
  Ii1ii1IiIII = Ii1ii1IiIII + 1
  if 51 - 51: iIii1
  if 25 - 25: OoooooooOO + iIii1 * I1ii11iIi11i
  if 92 - 92: I1IiiI + OoOooOOOO + O0 / o0oOOo0O0Ooo + oO
  if 18 - 18: O0OOooO * OoOoOO00 . I1iiiiI1iII / I1ii11iIi11i / i11iIiiIii
  if 21 - 21: o00oo / I1ii11iIi11i + OoOO + OoooooooOO
  if 91 - 91: i11iIiiIii / i1IIi + I1iiiiI1iII + O0OOooO * i11iIiiIii
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + OoOooOOOO * oO . iIii1
def O0ooo0 ( url ) :
 if 8 - 8: O0OOooO + II111iiii / I1iiiiI1iII / OoOooOOOO
 if 74 - 74: O0 / i1IIi
 o0O0O00 = o000o ( url ) . replace ( '&amp;' , 'and' )
 if 78 - 78: OoooooooOO . OoO0O00 + O0OOooO - i1IIi
 if 31 - 31: OoooooooOO . iI1
 I11i1I1I = re . compile ( '<li.+?href="(.+?)".+?>(.+?)</a.+?li>' ) . findall ( o0O0O00 )
 for i11i1I1 , O0iII1 in I11i1I1I :
  if i11i1I1 . find ( 'categ' ) != - 1 :
   IIII1i = url + i11i1I1
   iiiI1I11i1 ( "[COLOR lime]" + O0iII1 + "[/COLOR]" , IIII1i , 25 , IiII , iI111iI , '' )
   if 2 - 2: iIii1I11I1II1 * Oo0Ooo % o00oo - II111iiii - I1iiiiI1iII
def iIi11iiIiI1I ( url ) :
 if 3 - 3: i1IIi / II111iiii / i11iIiiIii * i1IIi - II111iiii
 Ii = o000o ( url ) . replace ( '&#8217;' , "'" )
 iII1111III1I = re . compile ( '<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"' , re . DOTALL ) . findall ( Ii )
 for url , ii11i , oO0o0OOOO in iII1111III1I :
  O00oOo00o0o = o000o ( url )
  O00oO0 = re . compile ( '<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"' ) . findall ( O00oOo00o0o )
  for O0Oo00OoOo in O00oO0 :
   try :
    ii1ii111 = O0Oo00OoOo . split ( "/embed/" ) [ 1 ]
    i11111I1I = "plugin://plugin.video.youtube/play/?video_id=" + ii1ii111
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11111I1I , 7 , ii11i , iI111iI , '' )
   except : pass
   if 11 - 11: OoooooooOO . oO
 try :
  Oo0000oOo = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( Ii ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , Oo0000oOo , 25 , IiII , iI111iI , '' )
 except : pass
 if 31 - 31: OoOooOOOO . oO * O0OOooO + i11iIiiIii * o00oo
 if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * OoOooOOOO
 if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . O0OOooO % iIii1
 if 50 - 50: iIii1I11I1II1 - iIii1 + iI1
 if 69 - 69: O0
 if 85 - 85: O0OOooO / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
def o0 ( ) :
 if 17 - 17: iIii1I11I1II1 . OoooooooOO / OoOooOOOO % II111iiii % i1IIi / i11iIiiIii
 OO00Oo = 'http://www.filmon.com/tv/bbc-news'
 if 58 - 58: Oo0Ooo . II111iiii + o00oo - i11iIiiIii / II111iiii / O0
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"group_id"(.+?)channels_count' ) . findall ( o0O0O00 )
 for oOOoOo in I11i1I1I :
  oO0o0OOOO = re . compile ( 'title":"(.+?)"' ) . findall ( oOOoOo ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , oOOoOo , 27 , IiII , iI111iI , '' )
  if 89 - 89: II111iiii + i1IIi + II111iiii
def IiII1II11I ( url ) :
 if 54 - 54: iIii1 + O0 + OoOooOOOO * oO - iI1 % o00oo
 I11i1I1I = re . compile ( '{"id"(.+?)}' ) . findall ( url )
 for I111 in I11i1I1I :
  oO0o0OOOO = re . compile ( ':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"' ) . findall ( I111 ) [ 0 ]
  O0O0OoOO0 = re . compile ( ':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"' ) . findall ( I111 ) [ 0 ]
  url = re . compile ( ':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"' ) . findall ( I111 ) [ 0 ]
  O0O0OoOO0 = O0O0OoOO0 . replace ( '\\' , '' )
  i11i1I1 = 'https://www.filmon.com/tv/' + url
  III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , i11i1I1 , 2 , O0O0OoOO0 , iI111iI , '' )
  if 13 - 13: OoO0O00 * o00oo * I1iiiiI1iII
  if 26 - 26: O0 * Oo0Ooo + II111iiii / iIii1 + o00oo % o0oOOo0O0Ooo
  if 42 - 42: I1ii11iIi11i . oO % oO
  if 57 - 57: II111iiii
  if 54 - 54: Oo0Ooo + o00oo + i11iIiiIii
  if 28 - 28: o00oo
  if 70 - 70: iIii1
def i11i1iiI1i ( url ) :
 if 87 - 87: O0OOooO
 IIIii = 1
 url = 'http://hdvidmusic.com'
 O00OooOo00o = o000o ( url )
 IiI11i1IIiiI = re . compile ( '<a href="([^"]*)">>></a></div>' , re . DOTALL ) . findall ( O00OooOo00o ) [ 0 ]
 IiI11i1IIiiI = IiI11i1IIiiI . replace ( '?page=' , '' )
 oOOo000oOoO0 = int ( IiI11i1IIiiI )
 if 86 - 86: II111iiii % i11iIiiIii + OoOO % i11iIiiIii
 url = 'http://hdvidmusic.com/?page=' + str ( IIIii )
 while IIIii <= oOOo000oOoO0 :
  if 92 - 92: i11iIiiIii - I1iiiiI1iII / O0OOooO / o00oo
  url = 'http://hdvidmusic.com/?page=' + str ( IIIii )
  if 43 - 43: II111iiii + iI1 + I1iiiiI1iII
  o0O0O00 = o000o ( url )
  I11i1I1I = re . compile ( '<div class="cell_container">(.+?)<!--div class="video_rating">' , re . DOTALL ) . findall ( o0O0O00 )
  if 40 - 40: o0oOOo0O0Ooo
  for IIi1i11111 in I11i1I1I :
   O0iII1 = re . compile ( '<a title="(.+?)" href=".+?">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   o0O0O00 = re . compile ( '<a title=".+?" href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   ii11i = re . compile ( 'src="(.+?)"/>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OOOooo = re . compile ( '<div class="video_quality">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   Ii = 'http://hdvidmusic.com' + o0O0O00
   Oo00oo0000OO = 'http://hdvidmusic.com' + ii11i
   oO0 ( "[COLOR lime]" + O0iII1 + "[/COLOR]" , Ii , 29 , Oo00oo0000OO , iI111iI , '' )
  IIIii = IIIii + 1
  if 69 - 69: O0OOooO - OoO0O00 / i11iIiiIii + I1ii11iIi11i % OoooooooOO
def o000O000 ( url ) :
 if 19 - 19: iIii1I11I1II1
 Ii = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe id\=.+?www(.+?)aut' ) . findall ( Ii ) [ 0 ]
 id = Ii1IiI1i1ii . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 30 - 30: iIii1 + oO - iIii1 . iIii1 - II111iiii + O0
def oOO0 ( ) :
 OO00Oo = 'http://www.bigtop40.com/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&amp;' , 'and' ) . replace ( '&#39;' , "'" ) . replace ( '&quot;' , '"' )
 I11i1I1I = re . compile ( '<li data-chart-position=".+?"(.+?)</em>' , re . DOTALL ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  try :
   i1IIiIii1i = re . compile ( '<a name="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ] . replace ( 'number' , 'Number' ) . replace ( '_' , ' ' )
   i1III = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   ooOOO0OooOo = re . compile ( 'alt="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if not 'http' in OO00Oo :
    i11i1I1 = 'http://www.bigtop40.com' + OO00Oo
    oO0 ( "[COLOR red]" + i1IIiIii1i + "[/COLOR]" + ' -- ' + "[COLOR lime]" + ooOOO0OooOo + "[/COLOR]" , i11i1I1 , 47 , i1III , iI111iI , '' )
  except : pass
  if 33 - 33: iI1 / i1IIi - I1IiiI % Oo0Ooo . I1ii11iIi11i
def Ii1II ( url ) :
 Ii = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe width=".+?" height="348" src="(.+?)"' ) . findall ( Ii ) [ 0 ]
 id = Ii1IiI1i1ii . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 89 - 89: oO + OoooooooOO + oO * i1IIi + iIii1I11I1II1 % OoOooOOOO
 if 59 - 59: iI1 + i11iIiiIii
 if 88 - 88: i11iIiiIii - O0OOooO
 if 67 - 67: iI1 . Oo0Ooo + OoOoOO00 - OoooooooOO
 if 70 - 70: iI1 / II111iiii - iIii1I11I1II1 - I1iiiiI1iII
 if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - OoOooOOOO
 if 30 - 30: OoOoOO00
def Ii111 ( ) :
 OO00Oo = 'http://www.hdmovieswatch.org/'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<li class="cat-item(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 67 - 67: O0
 for oO0Oo in I11i1I1I :
  OO00Oo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  oO0o0OOOO = re . compile ( 'title.+?">(.+?)</a>' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  IiII = 'https://www.dropbox.com/s/2b0j135ip39g89p/Movies.png?dl=1'
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 50 , IiII , iI111iI , '' )
  if 52 - 52: II111iiii . O0OOooO / OoOoOO00 / OoooooooOO . i11iIiiIii
def I1i1i ( url ) :
 if 86 - 86: Oo0Ooo / o00oo + O0 * I1iiiiI1iII
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="item">(.+?)<span class="player">' , re . DOTALL ) . findall ( o0O0O00 )
 if 19 - 19: II111iiii * iIii1 + OoOO
 for oO0Oo in I11i1I1I :
  try :
   url = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . split ( "Full" ) [ 0 ]
   oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 51 , IiII , iI111iI , '' )
  except : pass
  if 65 - 65: iI1 . oO . OoO0O00 . I1iiiiI1iII - iI1
 try :
  Oo0000oOo = re . compile ( '<div class="nav-previous alignleft"><a href="(.+?)" ></a>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , Oo0000oOo , 50 , IiII , iI111iI , '' )
 except : pass
 if 19 - 19: i11iIiiIii + I1iiiiI1iII % O0OOooO
def IIi ( url ) :
 if 27 - 27: iI1 % OoOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 try :
  import urlresolver
  if urlresolver . HostedMediaFile ( I11i1I1I ) . valid_url ( ) :
   I11i1I1I = urlresolver . HostedMediaFile ( I11i1I1I ) . resolve ( )
   i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   i11i1 . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , i11i1 , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 58 - 58: iI1 * o0oOOo0O0Ooo + O0 % iI1
def iI1I1iIi11 ( ) :
 if 87 - 87: OoOoOO00
 OO00Oo = "http://www.afdah.bz/"
 o0O0O00 = o000o ( OO00Oo )
 OOo = re . compile ( '<li class="cat-item.+?<a href="(.+?)" >(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for OO00Oo , oO0o0OOOO in sorted ( OOo ) :
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 53 , IiII , iI111iI , '' )
  if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
def III ( url ) :
 if 1 - 1: o00oo
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="movie-preview-content">(.+?)Views</small>' , re . DOTALL ) . findall ( o0O0O00 )
 if 62 - 62: i1IIi - iI1
 for oO0Oo in sorted ( I11i1I1I , reverse = True ) :
  if not "<i class" in oO0Oo :
   i11i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . replace ( "Afdah" , "" )
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   i1III = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  try :
   OOOooo = re . compile ( 'title=.+?Quality">(.+?)<' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  except : OOOooo = "Unknown"
  oO0 ( "[COLOR lime]" + oO0o0OOOO + 'Quality = ' "[/COLOR]" "[COLOR yellow]" + OOOooo + "[/COLOR]" , i11i1I1 , 54 , i1III , iI111iI , '' )
  if 96 - 96: i1IIi . I1ii11iIi11i + o00oo
 try :
  Oo0000oOo = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , Oo0000oOo , 53 , IiII , iI111iI , '' )
 except : pass
 if 48 - 48: iIii1I11I1II1 % i1IIi % I1iiiiI1iII + O0OOooO
def Iiii11iIi1 ( url ) :
 if 40 - 40: OoOooOOOO % OoO0O00 . oO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 try :
  import urlresolver
  if urlresolver . HostedMediaFile ( I11i1I1I ) . valid_url ( ) :
   I11i1I1I = urlresolver . HostedMediaFile ( I11i1I1I ) . resolve ( )
   i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   i11i1 . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , i11i1 , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 84 - 84: OoOoOO00 % O0OOooO - OoOoOO00 . o0oOOo0O0Ooo
def III1iI1iII1I ( ) :
 if 39 - 39: OoOO * O0OOooO / OoOoOO00 * OoO0O00 . OoOooOOOO % II111iiii
 ii1III11 = ''
 O0OoOoO00O = xbmc . Keyboard ( ii1III11 , 'Search For A Movie' )
 O0OoOoO00O . doModal ( )
 if O0OoOoO00O . isConfirmed ( ) :
  OooOOO0O00 = O0OoOoO00O . getText ( )
  IIii1i1iii1 = OooOOO0O00
  ii1III11 = OooOOO0O00 . replace ( ' ' , '+' )
  if not len ( ii1III11 ) > 1 :
   I11 . ok ( "STREAM ARMY" , "No search term was entered." )
   quit ( )
   if 70 - 70: i11iIiiIii % I1iiiiI1iII
  ii1III11 = ii1III11 . replace ( ' ' , '+' )
  OO00Oo = "http://housemovie.to/search?q=" + ii1III11
  o0O0O00 = o000o ( OO00Oo )
  I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
  if 11 - 11: iIii1 % I1ii11iIi11i % OoOO / II111iiii % oO - Oo0Ooo
  for iIi in I11i1I1I :
   try :
    oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( iIi ) [ 0 ]
    OO00Oo = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( iIi ) [ 0 ]
    O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
    try :
     OOooO = re . compile ( '<span class="imdb">(.+?)</span>' ) . findall ( iIi ) [ 0 ]
    except : OOooO = "IMDB Rating Unknown"
    if not "http" in OO00Oo :
     OO00Oo = "http://housemovie.to" + OO00Oo
     oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR] - [COLOR yellow][I]" + OOooO + "[/I][/COLOR]" , OO00Oo , 21 , O0O0OoOO0 , iI111iI , '' )
   except : pass
   if 79 - 79: oO % o00oo % o0oOOo0O0Ooo % OoOO - II111iiii * OoooooooOO
def oOOO ( url ) :
 if 56 - 56: I1ii11iIi11i
 o0O0O00 = o000o ( url )
 if 26 - 26: OoooooooOO % OoooooooOO
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 33 - 33: oO
 for IIi1i11111 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   i11i1I1 = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   if "genres" in i11i1I1 :
    i11i1I1 = "http://housemovie.to" + i11i1I1
    iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11i1I1 , 19 , IiII , iI111iI , '' )
  except : pass
  if 62 - 62: I1ii11iIi11i + OoOO + i1IIi / OoooooooOO
def IIiiii ( url ) :
 if 37 - 37: o0oOOo0O0Ooo % O0OOooO
 o0O0O00 = o000o ( url )
 if 83 - 83: iI1 . oO + o00oo - iI1 * oO / oO
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 39 - 39: oO / Oo0Ooo % OoO0O00 % i11iIiiIii
 for IIi1i11111 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   OOooO = re . compile ( 'imdb">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   if "(SOON)" in oO0o0OOOO :
    o0o0Ooo0 = oO0o0OOOO . split ( "(SOON)" ) [ 0 ]
    oO0o0OOOO = o0o0Ooo0 . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
   else : oO0o0OOOO = oO0o0OOOO . title ( )
   i11i1I1 = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   if "watch" in i11i1I1 :
    i11i1I1 = "http://housemovie.to" + i11i1I1
    oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + OOooO + "[/I][/COLOR]" , i11i1I1 , 21 , O0O0OoOO0 , iI111iI , '' )
    if 78 - 78: iIii1I11I1II1 + OoOooOOOO - OoOO * oO - OoooooooOO % OoOoOO00
  except : pass
  if 34 - 34: O0
def OooOOOo0 ( name , url , iconimage ) :
 if 54 - 54: OoOO - OoOooOOOO - oO . iIii1I11I1II1
 o0OIIiI1I1 = [ ]
 I11I1IIiiII1 = [ ]
 IIIIIii1ii11 = [ ]
 OOOooo0OooOoO = [ ]
 oOoOOOo = [ ]
 if 43 - 43: i1IIi
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 23 - 23: I1iiiiI1iII + OoOooOOOO . OoOoOO00 * I1IiiI + I1ii11iIi11i
 I11i1I1I = re . compile ( '<div class="fig_holder">(.+?)</div>' ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  name = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
  i11i1I1 = re . compile ( '<a href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  iconimage = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  try :
   OOooO = re . compile ( 'imdb">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
  except : OOooO = "0.0"
  if "imdb" in OOooO . lower ( ) :
   OOooO = OOooO . replace ( "IMDB: " , "" ) . replace ( " " , "" )
  if not "." in OOooO :
   OOooO = OOooO + ".0"
   if 18 - 18: iIii1 * o0oOOo0O0Ooo . iIii1 / O0
  if "(SOON)" in name :
   o0o0Ooo0 = name . split ( "(SOON)" ) [ 0 ]
   name = o0o0Ooo0 . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
  else : name = name . title ( )
  i11i1I1 = "http://housemovie.to" + i11i1I1
  if 8 - 8: o0oOOo0O0Ooo
  o0OIIiI1I1 . append ( name )
  I11I1IIiiII1 . append ( i11i1I1 )
  IIIIIii1ii11 . append ( iconimage )
  OOOooo0OooOoO . append ( OOooO )
  oOoOOOo = list ( zip ( OOOooo0OooOoO , o0OIIiI1I1 , I11I1IIiiII1 , IIIIIii1ii11 ) )
  if 4 - 4: I1ii11iIi11i + I1ii11iIi11i * O0OOooO - OoOoOO00
 o00oIII11I = sorted ( oOoOOOo , reverse = True )
 if 17 - 17: OoooooooOO + iI1 * OoOooOOOO * OoOoOO00
 for OOooO , name , i11i1I1 , iconimage in o00oIII11I :
  if OOooO == "0.0" :
   OOooO = "IMDB Rating Unknown"
  else : OOooO = "IMDB: " + OOooO
  oO0 ( "[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + OOooO + "[/I][/COLOR]" , i11i1I1 , 21 , iconimage , iI111iI , '' )
  if 36 - 36: O0 + Oo0Ooo
 try :
  iIIIi1i1I11i = re . compile ( '<a href="([^"]*)" class="page_next">Next</a>' ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iIIIi1i1I11i , 19 , IiII , iI111iI , '' )
 except : pass
 if 55 - 55: Oo0Ooo - iI1
def O0OO0O ( name , url , iconimage ) :
 if 49 - 49: iIii1I11I1II1 - O0 . i1IIi - OoooooooOO
 iII11 = [ ]
 O0oO0 = [ ]
 iiIiii1IIIII = [ ]
 if 37 - 37: i1IIi . OoOooOOOO % OoOoOO00 + OoooooooOO / I1iiiiI1iII
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 3 - 3: I1ii11iIi11i
 IIi1i11111 = re . compile ( '<div class="md_full_cell">(.+?)</div>' ) . findall ( o0O0O00 )
 if 17 - 17: I1ii11iIi11i . II111iiii . O0OOooO / I1ii11iIi11i
 for o00o in IIi1i11111 :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( o00o ) [ 0 ]
   O0iII1 = re . compile ( 'rel="nofollow">(.+?)</a>' ) . findall ( o00o ) [ 0 ]
   url = "http://housemovie.to" + url
   for oOooO00o0O in oo0o0O00 :
    if oOooO00o0O . lower ( ) in O0iII1 . lower ( ) :
     if 80 - 80: iI1 / OoOooOOOO / OoOoOO00 + i1IIi - Oo0Ooo
     iII11 . append ( O0iII1 )
     O0oO0 . append ( url )
     iiIiii1IIIII . append ( iconimage )
  except : pass
  if 11 - 11: o0oOOo0O0Ooo * OoO0O00
  if 15 - 15: OoOoOO00
 name = '[COLOR lime]' + name + '[/COLOR]'
 i11II1I11I1 = I11 . select ( name , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  url = O0oO0 [ i11II1I11I1 ]
  url = str ( url )
  IiII = iiIiii1IIIII [ i11II1I11I1 ]
  IiII = str ( IiII )
  if 62 - 62: OoOO
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 51 - 51: OoOoOO00
  url = re . compile ( '<a href="([^"]*)" target="_blank" class="button_type_1">' ) . findall ( o0O0O00 ) [ 0 ]
  if 14 - 14: iIii1 % o00oo % Oo0Ooo - i11iIiiIii
  try :
   import urlresolver
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
    i11i1 = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
    i11i1 . setPath ( i1II1 )
    xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
   else : I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  except :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
   if 53 - 53: OoOO % Oo0Ooo
   if 59 - 59: iI1 % iIii1I11I1II1 . i1IIi + II111iiii * iIii1
   if 41 - 41: OoOO % I1ii11iIi11i
   if 12 - 12: iI1
   if 69 - 69: OoooooooOO + iI1
   if 26 - 26: Oo0Ooo + iI1 / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
   if 31 - 31: OoOooOOOO % iI1 * OoOooOOOO
def IiI ( url ) :
 if 34 - 34: OoOooOOOO % O0OOooO . O0 . iIii1I11I1II1
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<a class="site_tag(.+?)/a>' ) . findall ( o0O0O00 )
 if 93 - 93: i1IIi . i11iIiiIii . Oo0Ooo
 for o0O0O00 in I11i1I1I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
  oO0o0OOOO = re . compile ( '/i>(.+?)<' ) . findall ( o0O0O00 ) [ 0 ]
  i11i1I1 = "http://xoxfuck.com" + url
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11i1I1 , 17 , IiII , iI111iI , '' )
  if 99 - 99: OoOooOOOO - oO - o00oo % OoO0O00
def IiiIIiiiiii ( ) :
 if 100 - 100: Oo0Ooo + o0oOOo0O0Ooo - O0 % II111iiii . I1iiiiI1iII
 OO00Oo = 'http://www.pornhd.com/category'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '&amp;' , 'and' )
 I11i1I1I = re . compile ( '<ul class="tag-150-list">(.+?)<div class="footer-zone">' , re . DOTALL ) . findall ( o0O0O00 )
 OOo = re . compile ( '<li class="category">(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 92 - 92: II111iiii * OoooooooOO - oO
 for IIi1i11111 in OOo :
  i1III = re . compile ( 'data-original="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  oO0o0OOOO = re . compile ( 'alt="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  oooo00 = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  if not 'http' in oooo00 :
   Ii = 'http://www.pornhd.com' + oooo00
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , Ii , 42 , i1III , iI111iI , '' )
   if 96 - 96: I1ii11iIi11i % O0OOooO % OoOO - O0OOooO % OoOoOO00 + I1ii11iIi11i
def iIOo0O ( url ) :
 if 1 - 1: O0 / I1iiiiI1iII % oO . Oo0Ooo + iIii1
 I1Ii11iiiI = url
 i1i1II = 0
 try :
  o0O , url = url . split ( '|' )
  if 16 - 16: oO
 except : i1i1II = 1
 iI1i11Iiii = o000o ( url )
 if 68 - 68: OoOO - i11iIiiIii - o00oo + OoOoOO00
 I11i1I1I = re . compile ( '<section id="pageContent"(.+?)<div class="pager paging">' , re . DOTALL ) . findall ( iI1i11Iiii )
 OOo = re . compile ( '<a class="thumb"(.+?)<span class="add-to">' , re . DOTALL ) . findall ( iI1i11Iiii )
 if 99 - 99: OoOoOO00 * oO * i1IIi / O0 - OoOoOO00 % o0oOOo0O0Ooo
 if 51 - 51: OoooooooOO % iI1 * OoOoOO00
 if 69 - 69: i1IIi
 if 59 - 59: II111iiii - o0oOOo0O0Ooo
 for IIi1i11111 in OOo :
  try :
   O0iII1 = re . compile ( '<img alt="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if 24 - 24: Oo0Ooo - i1IIi + OoOooOOOO
   if 38 - 38: OoooooooOO / I1ii11iIi11i . O0 / i1IIi / Oo0Ooo + iIii1I11I1II1
   ooO00O00oOO = re . compile ( '<time>(.+?)</time>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if 40 - 40: I1iiiiI1iII . o00oo + I1IiiI + I1ii11iIi11i + oO
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   if 26 - 26: iIii1I11I1II1
   if not "http" in O0O0OoOO0 :
    O0O0OoOO0 = re . compile ( 'data-original="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
    if 87 - 87: I1ii11iIi11i / OoooooooOO - Oo0Ooo % OoOoOO00 % iIii1 % Oo0Ooo
    if 29 - 29: OoooooooOO . I1IiiI % I1ii11iIi11i - I1iiiiI1iII
   o0O0O00 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if not 'http' in o0O0O00 :
    Ii = 'http://www.pornhd.com' + o0O0O00
    iiiI1I11i1 ( "[COLOR lime]" + O0iII1 + "[/COLOR]" "[COLOR red]" " :: Video Length :: " + ooO00O00oOO + "[/COLOR]" , Ii , 43 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 8 - 8: i1IIi
  if 32 - 32: o00oo / II111iiii
 if i1i1II == 1 :
  try :
   II1Iii = ""
   if not "=" in I1Ii11iiiI :
    I1Ii11iiiI = I1Ii11iiiI + "?page=1"
    o0O , O00oO = I1Ii11iiiI . split ( "=" )
    Ooo00OoOOO = int ( O00oO ) + 1
    II1Iii = o0O + "=" + str ( Ooo00OoOOO )
    if 73 - 73: OoOooOOOO * OoooooooOO . O0 . iIii1
    iiiI1I11i1 ( '[COLOR red]Next Page >>[/COLOR]' , II1Iii , 42 , IiII , Iii1ii1II11i )
    if 55 - 55: Oo0Ooo
  except : pass
  if 77 - 77: II111iiii
def IiiiIi1iI1iI ( url , icon , fanart ) :
 if 98 - 98: OoO0O00 / iI1 * I1ii11iIi11i / o00oo
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( 'sources.+?{(.+?)}' , re . DOTALL ) . findall ( o0O0O00 )
 o0O = str ( I11i1I1I )
 I11i1I1I = o0O . replace ( '\\' , '' )
 OOoOO0OO = re . compile ( "720.+?'.+?'(.+?)'," ) . findall ( I11i1I1I ) [ 0 ]
 i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
 if 26 - 26: I1iiiiI1iII . I1iiiiI1iII
 xbmc . Player ( ) . play ( OOoOO0OO , i11i1 , False )
 if 35 - 35: oO . OoOoOO00 * i11iIiiIii
 quit ( 0 )
 if 44 - 44: i11iIiiIii / Oo0Ooo
def Ii1IIi ( name , url , iconimage ) :
 if 43 - 43: oO % I1iiiiI1iII
 o0O0ooOOoO = name . split ( '(' ) [ 1 ]
 o0O0ooOOoO = o0O0ooOOoO . replace ( ')' , '' ) . replace ( "[/COLOR]" , '' )
 o0O0ooOOoO = int ( o0O0ooOOoO )
 iIi11ii = url
 if 50 - 50: OoOO / OoOoOO00 * OoOO
 Ii1iIi111i1i1 = 0
 IIOO0ooOo0OoOo0 = 1
 IIi11i1i1iI1 = 0
 oOo = 6
 if 17 - 17: OoOO . i11iIiiIii
 Oo0o0000o0o0 . create ( "STREAM ARMY" , "[COLOR lime]Getting video 1 of " + str ( o0O0ooOOoO ) + "![/COLOR]" )
 Oo0o0000o0o0 . update ( 0 )
 while IIOO0ooOo0OoOo0 < 2000 :
  if 5 - 5: I1ii11iIi11i + O0 + O0 . oO - O0OOooO
  if IIi11i1i1iI1 == 0 :
   o0O0O00 = o000o ( iIi11ii )
   if 63 - 63: o00oo
   I11i1I1I = re . compile ( '<div class="inner_block video_box">(.+?)</a>' ) . findall ( o0O0O00 )
   for iIi in I11i1I1I :
    i11i1I1 = re . compile ( 'href="(.+?)">' ) . findall ( iIi ) [ 0 ]
    name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( iIi ) [ 0 ]
    iconimage = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
    Ii1iIi111i1i1 = Ii1iIi111i1i1 + 1
    Oo0 = 100 * int ( Ii1iIi111i1i1 ) / int ( o0O0ooOOoO )
    Oo0o0000o0o0 . update ( Oo0 , "[COLOR lime]Getting video " + str ( Ii1iIi111i1i1 ) + " of " + str ( o0O0ooOOoO ) + "![/COLOR]" )
    oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , i11i1I1 , 18 , iconimage , iI111iI , '' )
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  else :
   url = iIi11ii + '?load_more=10&loaded=' + str ( oOo )
   o0O0O00 = o000o ( url )
   o0O0O00 = o0O0O00 . replace ( '\\' , '' )
   if 79 - 79: OoO0O00 % iI1 / iIii1I11I1II1 + OoOoOO00 * OoO0O00
   if "no_more_videos" in o0O0O00 :
    IIOO0ooOo0OoOo0 = 2001
    if 30 - 30: OoooooooOO / OoOooOOOO + I1iiiiI1iII / I1ii11iIi11i * O0
   I11i1I1I = re . compile ( '<div class="(.+?)</a>' ) . findall ( o0O0O00 )
   for iIi in I11i1I1I :
    if IIOO0ooOo0OoOo0 < 2000 :
     i11i1I1 = re . compile ( 'href="(.+?)">' ) . findall ( iIi ) [ 0 ]
     name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( iIi ) [ 0 ]
     iconimage = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
     Ii1iIi111i1i1 = Ii1iIi111i1i1 + 1
     Oo0 = 100 * int ( Ii1iIi111i1i1 ) / int ( o0O0ooOOoO )
     Oo0o0000o0o0 . update ( Oo0 , "[COLOR lime]Getting video " + str ( Ii1iIi111i1i1 ) + " of " + str ( o0O0ooOOoO ) + "![/COLOR]" )
     oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , i11i1I1 , 18 , iconimage , iI111iI , '' )
   oOo = oOo + 10
  IIOO0ooOo0OoOo0 = IIOO0ooOo0OoOo0 + 1
 Oo0o0000o0o0 . close
 if 16 - 16: Oo0Ooo / i11iIiiIii
def oo00IIIIIIIiI ( name , url , iconimage ) :
 if 12 - 12: I1iiiiI1iII . iIii1 . OoOoOO00 / O0
 Ii = o000o ( url )
 IIi1i11111 = re . compile ( '<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">' ) . findall ( Ii ) [ 0 ]
 O0iII1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii ) [ 0 ]
 O0iII1 = O0iII1 . split ( ' | ' ) [ 0 ]
 O0iII1 = O0iII1 . strip ( ' ' )
 i11i1 = xbmcgui . ListItem ( O0iII1 , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( IIi1i11111 , i11i1 , False )
 if 58 - 58: o0oOOo0O0Ooo - II111iiii % o00oo + oO . OoOoOO00 / iIii1
 if 8 - 8: I1ii11iIi11i . OoO0O00 * OoOooOOOO + II111iiii % i11iIiiIii
 if 8 - 8: O0OOooO * O0
 if 73 - 73: o0oOOo0O0Ooo / o00oo / OoOooOOOO / OoO0O00
 if 11 - 11: OoOoOO00 + iIii1 - OoooooooOO / OoO0O00
 if 34 - 34: O0OOooO
 if 45 - 45: O0OOooO / Oo0Ooo / OoOO
def IIi11i1II ( url ) :
 if 73 - 73: o0oOOo0O0Ooo - I1IiiI * i1IIi / i11iIiiIii * iI1 % II111iiii
 try :
  if not "http" in url :
   if "https://" in url :
    url = url . replace ( "https://" , "http://" )
   o0O0O00 = o000o ( url )
   oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0O0O00 ) [ 0 ] . split ( ' (' ) [ 0 ]
   OooOoOOo0oO00 = re . compile ( '<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">' ) . findall ( o0O0O00 )
   O0O0OoOO0 = re . compile ( '<meta property="og:image" content="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   if 73 - 73: I1iiiiI1iII / I1ii11iIi11i % I1ii11iIi11i * OoOooOOOO / I1ii11iIi11i
   for url , O0iII1 in OooOoOOo0oO00 :
    oO0 ( O0iII1 , url , 14 , O0O0OoOO0 , iI111iI , '' )
  else :
   o0O0O00 = o000o ( url )
   if 8 - 8: OoOO
   I11i1I1I = re . compile ( '<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>' ) . findall ( o0O0O00 ) [ 0 ]
   ii1III11 = str ( I11i1I1I )
   OOo = re . compile ( '<td width="100%" class="entry">(.+?)</td>' ) . findall ( ii1III11 )
   I11iII = re . compile ( '<meta property="og:image" content="(.+?)"/>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   for iIi in OOo :
    oO0o0OOOO = re . compile ( 'title="(.+?)"' ) . findall ( iIi ) [ 0 ]
    url = re . compile ( '<a href="(.+?)"' ) . findall ( iIi ) [ 0 ]
    O0iII1 = oO0o0OOOO . split ( ' - ' ) [ 1 ]
    if not 'http' in url : url = 'http:' + url
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , url , 14 , I11iII , iI111iI , '' )
 except :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
  if 2 - 2: I1IiiI + o0oOOo0O0Ooo . o0oOOo0O0Ooo . O0 / OoOooOOOO
  if 40 - 40: o0oOOo0O0Ooo - II111iiii / Oo0Ooo
  if 14 - 14: I1ii11iIi11i
  if 5 - 5: o0oOOo0O0Ooo . iIii1I11I1II1 % iIii1I11I1II1
  if 56 - 56: OoooooooOO - OoOooOOOO - i1IIi
  if 8 - 8: oO / iI1 . I1IiiI + I1ii11iIi11i / i11iIiiIii
  if 31 - 31: O0OOooO - iIii1I11I1II1 + I1iiiiI1iII . Oo0Ooo / iIii1 % iIii1I11I1II1
def I11i1iIiiIiIi ( ) :
 if 49 - 49: iI1 . I1ii11iIi11i . i11iIiiIii - II111iiii / OoOO
 OO00Oo = 'https://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
 if 62 - 62: iI1
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"start(.+?)}' ) . findall ( o0O0O00 )
 for iIi in I11i1I1I :
  if not 'event_status":""' in str ( iIi ) :
   i1I1i = 1
  else : i1I1i = 0
  OO0o = re . compile ( 'date":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  IiII1iiI = re . compile ( 'competition_name":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  iII = re . compile ( 'competition_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  oO0O000oOoo0O = re . compile ( 'home_team":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  iIIiii11iIiiI = re . compile ( 'home_team_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  O0Oo0 = re . compile ( 'home_team_slug":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  try :
   o0oO0oo0000OO = re . compile ( 'event_status":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  except : o0oO0oo0000OO = "null"
  I1i1ii1IiIii = re . compile ( 'away_team":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  oOOO0O0Ooo = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  IiI1i111IiIiIi1 = re . compile ( 'away_team_slug":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  i1II11II1 = re . compile ( 'event_id":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  try :
   II1IIIii = re . compile ( 'game_minute":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  except : II1IIIii = "null"
  iIIIiIi1I1i = iIIiii11iIiiI . split ( "-" )
  OoOOoO0oOo = oOOO0O0Ooo . split ( "-" )
  oO0O000oOoo0O = ""
  IIi11i1i1iI1 = 0
  for o0O in iIIIiIi1I1i :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   ooO00O00oOO = len ( iIIIiIi1I1i )
   if IIi11i1i1iI1 < ooO00O00oOO :
    oO0O000oOoo0O = oO0O000oOoo0O + " " + o0O
  I1i1ii1IiIii = ""
  IIi11i1i1iI1 = 0
  for o0O in OoOOoO0oOo :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   ooO00O00oOO = len ( OoOOoO0oOo )
   if IIi11i1i1iI1 < ooO00O00oOO :
    I1i1ii1IiIii = I1i1ii1IiIii + " " + o0O
    if 70 - 70: OoOooOOOO % iIii1I11I1II1 . Oo0Ooo + Oo0Ooo - o0oOOo0O0Ooo % oO
  OO0o = OO0o + "!"
  OO0o , i1IIi1i1Ii1 = OO0o . split ( ' ' )
  i1IIi1i1Ii1 = i1IIi1i1Ii1 . replace ( ":00!" , "" )
  o0O , O00oO , Ooo00OoOOO = OO0o . split ( "-" )
  OO0o = Ooo00OoOOO + "-" + O00oO + "-" + o0O
  i1IIi1i1Ii1 = "[COLOR red][B]" + i1IIi1i1Ii1 + "[/B][/COLOR]"
  OO0o = "[COLOR red][B]" + OO0o + "[/B][/COLOR]"
  OO00Oo = 'https://soccerstreams.net/streams/' + i1II11II1 + '/' + O0Oo0 + '_vs_' + IiI1i111IiIiIi1
  oO0o0OOOO = '[COLOR lime][B]' + oO0O000oOoo0O . title ( ) + ' vs ' + I1i1ii1IiIii . title ( ) + '[/B][/COLOR]'
  OO00Oo = OO00Oo + "|SPLIT|" + oO0o0OOOO
  O0O0OoOO0 = 'https://soccerstreams.net/images/teams/' + iIIiii11iIiiI
  if i1I1i == 0 :
   oO0 ( i1IIi1i1Ii1 + ' | ' + oO0o0OOOO + ' - ' + OO0o + ' | [COLOR yellow]' + IiII1iiI + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
  else :
   II1IIIii = II1IIIii . replace ( '&#039;' , "'" )
   oO0 ( "[COLOR red][B]" + II1IIIii + " " + o0oO0oo0000OO + '[/B][/COLOR] | ' + oO0o0OOOO + ' - ' + OO0o + ' | [COLOR yellow]' + IiII1iiI + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
   if 45 - 45: iIii1I11I1II1 . o00oo / OoOoOO00 / iIii1
   if 55 - 55: iIii1
def IIiIiII ( name , url , iconimage ) :
 if 56 - 56: iIii1I11I1II1 . i11iIiiIii - iI1 * II111iiii * oO
 I11 = xbmcgui . Dialog ( )
 if 5 - 5: iI1 / iI1 - I1ii11iIi11i
 url , name = url . split ( "|SPLIT|" )
 oO0ooOO = name
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 if 7 - 7: II111iiii - iI1 . II111iiii
 IIi11i1i1iI1 = 1
 oOo = 0
 Ii = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1i11111 = re . compile ( '<tr class="(.+?)</tr>' , re . DOTALL ) . findall ( Ii )
 for OOo0O0O000 in IIi1i11111 :
  url = re . compile ( 'data.+?="(.+?)"' ) . findall ( OOo0O0O000 ) [ 0 ]
  O0oO0 . append ( url )
  iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  if 29 - 29: o0oOOo0O0Ooo / Oo0Ooo * I1ii11iIi11i . o0oOOo0O0Ooo
 if IIi11i1i1iI1 == 1 :
  I11 . ok ( oO0o0o0ooO0oO , "Sorry no links found!" )
  quit ( )
  if 64 - 64: o00oo / O0OOooO % i11iIiiIii
 oO0ooOO = '[COLOR mediumpurple]' + oO0ooOO + '[/COLOR]'
 if 3 - 3: I1iiiiI1iII . O0OOooO % I1IiiI + I1ii11iIi11i
 i11II1I11I1 = I11 . select ( oO0ooOO , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  url = O0oO0 [ i11II1I11I1 ]
  I1ii11iI = iII11 [ i11II1I11I1 ]
  name = urllib . quote_plus ( iII11 [ i11II1I11I1 ] )
  import liveresolver
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
   i11i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   i11i1 . setPath ( i1II1 )
   xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
  elif liveresolver . isValid ( url ) == True :
   url = liveresolver . resolve ( url )
   i11i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   i11i1 . setPath ( i1II1 )
   xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
  else :
   if '.m3u8' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   elif '.ts' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   else :
    OOO0000oO = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=' + name + '%26url='
    IIi1i = "/"
    if not I1ii11iI . endswith ( IIi1i ) :
     I1I1iIiII1 = I1ii11iI + "/"
    else :
     I1I1iIiII1 = I1ii11iI
    url = OOO0000oO + O0oO0 [ i11II1I11I1 ] + "%26referer=" + I1I1iIiII1
   i11i1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   i11i1 . setPath ( url )
   xbmc . Player ( ) . play ( url , i11i1 , False )
   if 64 - 64: i1IIi
def IIii1 ( ) :
 OO00Oo = 'https://mamahd.tv/'
 if 35 - 35: i11iIiiIii - I1IiiI / iI1 + OoOO * o00oo
 try :
  o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '<ul class="mainnav sports">(.+?)</div> <!-- /container -->' ) . findall ( o0O0O00 )
  OOo = re . compile ( '<ul class="mainnav sports">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 )
  oooo00 = re . compile ( 'title="(.+?)" href="(.+?)"></a> </li>' , re . DOTALL ) . findall ( o0O0O00 )
  O0O0OoOO0 = 'http://mamahd.com/images/logo.png'
  for O0iII1 , o0O0O00 in oooo00 :
   if 49 - 49: o0oOOo0O0Ooo * OoOO + OoOooOOOO + I1iiiiI1iII
   iiiI1I11i1 ( "[COLOR lime]" + O0iII1 + "[/COLOR]" , o0O0O00 , 44 , O0O0OoOO0 , iI111iI , '' )
   if 30 - 30: o0oOOo0O0Ooo / iI1 / iIii1 % O0OOooO + II111iiii
 except :
  I11 . ok ( "Stream Army" , "Damn, No Links available at the moment, come back closer to the event!" )
  quit ( )
  if 4 - 4: I1iiiiI1iII - Oo0Ooo - iIii1 - OoOooOOOO % i11iIiiIii / OoO0O00
def i1iii11 ( url ) :
 if 92 - 92: OoOoOO00 . OoooooooOO - oO
 IIi11i1i1iI1 = 0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '  ' , '' )
 if 74 - 74: iIii1I11I1II1 % I1iiiiI1iII * iI1 * iIii1I11I1II1
 OOo = re . compile ( '<td class="home-time">(.+?)<td class="home-status">' , re . DOTALL ) . findall ( o0O0O00 )
 if 73 - 73: o0oOOo0O0Ooo % oO . iI1
 for iIi in OOo :
  try :
   oo = re . compile ( '<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   ooOOoOo = re . compile ( '<span class="date">.+?</span>(.+?)-' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   if 90 - 90: II111iiii / I1IiiI
   if 45 - 45: iIii1I11I1II1
   i1III = re . compile ( '<img src="(.+?)">' , re . DOTALL ) . findall ( iIi ) [ 2 ]
   iIiIii1ii = re . compile ( '<img data-toggle="tooltip" data-placement="left" title="Country" src=".+?">(.+?)</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   if 8 - 8: OoO0O00 + OoOoOO00 . iIii1I11I1II1 % O0
   o0O0O00 = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( iIi ) [ 1 ]
   iI11Ii111 = re . compile ( '<td class="home-away">.+?<a href=".+?">(.+?)<img' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   ooOOoOo = ooOOoOo . lstrip ( ' ' )
   iI11Ii111 = iI11Ii111 . lstrip ( ' ' )
   if 54 - 54: OoOoOO00 % I1iiiiI1iII . OoOoOO00 * iI1 + OoOoOO00 % i1IIi
   if 23 - 23: oO - iI1 + OoOO - OoOoOO00 * OoOoOO00 . Oo0Ooo
   IIi11i1i1iI1 = 1
   iiiI1I11i1 ( "[COLOR lime]" + oo + ' ::: ' + ooOOoOo + "[/COLOR]" ' ' "[COLOR yellow]" + iIiIii1ii + 'Vs ' + iI11Ii111 + "[/COLOR]" , o0O0O00 , 48 , i1III , iI111iI , '' )
  except :
   pass
   if 47 - 47: o00oo % iIii1I11I1II1
 if IIi11i1i1iI1 == 0 :
  I11 . ok ( "Stream Army" , "Damn, No Links available at the moment, come back closer to the event!" )
  quit ( )
  if 11 - 11: I1IiiI % OoOO - OoO0O00 - o00oo + o0oOOo0O0Ooo
def o0O0O0 ( url ) :
 if 55 - 55: O0 - oO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<td class="event-software">(.+?)<td class="event-rate">' , re . DOTALL ) . findall ( o0O0O00 )
 if 58 - 58: OoOoOO00 - I1iiiiI1iII - OoooooooOO
 for IIi1i11111 in I11i1I1I :
  o00ii111Iiii = re . compile ( '<td class="event-site">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  if not 'VIP' in IIi1i11111 :
   oo0oO0o0 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OOOooo = re . compile ( '<td class="event-bitrate">(.+?)</td>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   Iii1Ii = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + oo0oO0o0 + '%26referer=no'
   III1iII1I1ii ( "[COLOR red]" + o00ii111Iiii + "[/COLOR]" + ' ::----:: [COLOR lime]  QUALITY = ' + OOOooo + "[/COLOR]" , url , 2 , Iii1Ii , iI111iI , '' )
   if 30 - 30: O0 - I1iiiiI1iII % Oo0Ooo
   if 87 - 87: OoOooOOOO / I1IiiI + Oo0Ooo + iI1 - OoooooooOO + Oo0Ooo
   if 93 - 93: O0OOooO . iIii1I11I1II1 % i11iIiiIii . OoOoOO00 % O0OOooO + O0
   if 65 - 65: OoOO + OoO0O00 - OoooooooOO
   if 51 - 51: Oo0Ooo + o00oo / I1iiiiI1iII - i1IIi
   if 51 - 51: Oo0Ooo - I1ii11iIi11i * OoOooOOOO
   if 12 - 12: iIii1I11I1II1 % O0OOooO % O0OOooO
def o0i1iI1iiI1I ( name , url , iconimage ) :
 if 52 - 52: OoO0O00 % OoOO * II111iiii
 iconimage = "null"
 if 4 - 4: OoOooOOOO % O0 - OoooooooOO + O0OOooO . o00oo % II111iiii
 IIi11i1i1iI1 = 0
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
 II1 = 1
 I11Iii1 = 0
 if "http" in url :
  if 16 - 16: OoOO * OoO0O00 / o00oo
  Oo0o0000o0o0 . create ( "Stream Army" , "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]" )
  Oo0o0000o0o0 . update ( 0 )
  if 22 - 22: o00oo + iIii1I11I1II1 % Oo0Ooo / OoOooOOOO / OoOO
  while II1 < 11 :
   Oo0 = 100 * int ( II1 ) / int ( 10 )
   Oo0o0000o0o0 . update ( Oo0 , "" , "[COLOR lime]Connection attempt " + str ( II1 ) + " of 10[/COLOR]" )
   o0O0O00 = o000o ( url )
   if 54 - 54: OoOoOO00 % iIii1 . i11iIiiIii
   if I11Iii1 == 0 :
    II1 = II1 + 1
    O0iII1 = re . compile ( 'title="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
    O0iII1 = O0iII1 . split ( " - " ) [ 0 ]
    if 93 - 93: O0OOooO % i11iIiiIii % oO
    O00OooO = re . compile ( '<td class="entry">(.+?)target' ) . findall ( o0O0O00 )
    for o00o in O00OooO :
     I1IiI1iI11 = 1
     iIiii = len ( o00o )
     O0O0o0oO0O00 = 100 * int ( I1IiI1iI11 ) / int ( iIiii )
     Oo0o0000o0o0 . update ( O0O0o0oO0O00 , "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]" , "[COLOR lime]Filtering links " + str ( I1IiI1iI11 ) + " of " + str ( iIiii ) + " possible matches[/COLOR]" )
     if 70 - 70: oO + o00oo
     if not "putlocker.bypassed.info" in o00o :
      o00ooo0 = re . compile ( '<a rel=".+?" href="(.+?)"' ) . findall ( o00o ) [ 0 ]
      IIi11i1i1iI1 = IIi11i1i1iI1 + 1
      iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
      O0oO0 . append ( o00ooo0 )
      iiIiii1IIIII . append ( iconimage )
     I11Iii1 = 1
     II1 = 12
     I1IiI1iI11 = I1IiI1iI11 + 1
     if 39 - 39: O0OOooO . II111iiii
   if Oo0o0000o0o0 . iscanceled ( ) :
    sys . exit ( )
   import time
   time . sleep ( 1 )
   II1 = II1 + 1
   if 45 - 45: o00oo * OoOoOO00 / iIii1I11I1II1
 else :
  if 77 - 77: oO - OoOooOOOO
  Ii = o000o ( url )
  IIi1i11111 = re . compile ( '<td class="entry">(.+?)</tr>' ) . findall ( Ii )
  if 11 - 11: I1ii11iIi11i
  for o00o in IIi1i11111 :
   url = re . compile ( 'href="(.+?)"' ) . findall ( o00o ) [ 0 ]
   if not "putlocker.unblocked.ink" in url :
    IIi11i1i1iI1 = IIi11i1i1iI1 + 1
    iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
    O0oO0 . append ( url )
    iiIiii1IIIII . append ( iconimage )
    if 26 - 26: iIii1I11I1II1 * oO - iI1
    if 27 - 27: I1ii11iIi11i * oO - OoO0O00 + OoOO * OoOO
    if 55 - 55: O0OOooO
 if IIi11i1i1iI1 == 0 :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
 name = '[COLOR lime]' + name + '[/COLOR]'
 i11II1I11I1 = I11 . select ( name , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  url = O0oO0 [ i11II1I11I1 ]
  url = str ( url )
  IiII = iiIiii1IIIII [ i11II1I11I1 ]
  IiII = str ( IiII )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
   i11i1 = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
   i11i1 . setPath ( i1II1 )
   xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
   if 82 - 82: oO - iI1 + OoO0O00
def OO0 ( name , url , iconimage ) :
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = i11i1 )
 xbmc . Player ( ) . play ( url , i11i1 , False )
 if 64 - 64: OoooooooOO . I1ii11iIi11i % O0 + I1IiiI - o0oOOo0O0Ooo
def OOoOO0o0o0 ( name , url , iconimage ) :
 if 84 - 84: i11iIiiIii * OoOO . i11iIiiIii
 name = name . replace ( '  ' , '' )
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
 else : url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
 if 12 - 12: OoOoOO00 % iIii1 % I1ii11iIi11i . i11iIiiIii * iIii1I11I1II1
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
  i11i1 = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  i11i1 . setPath ( i1II1 )
  xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
  quit ( )
 else :
  i1II1 = url
  i11i1 = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  i11i1 . setPath ( i1II1 )
  xbmc . Player ( ) . play ( i1II1 , i11i1 , False )
  quit ( )
  if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
def i11ii1ii11i ( name , url , iconimage ) :
 if 5 - 5: OoOoOO00 % OoooooooOO
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  OO0I111i1I = url . split ( 'list=' ) [ 1 ]
  I1IIiiI1II1 = iiIIIII1i1iI + OO0I111i1I + o0oO0
  iII11I1IiiIi = urllib2 . Request ( I1IIiiI1II1 )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   Oo0000oOo = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   I1IIiiI1II1 = oo00 + Oo0000oOo + o00 + OO0I111i1I + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , I1IIiiI1II1 , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 5 - 5: I1iiiiI1iII
  if 62 - 62: OoOoOO00 . OoooooooOO . iI1 . OoO0O00 * I1iiiiI1iII
  if 78 - 78: o00oo / OoO0O00 - o00oo * OoooooooOO . OoOoOO00
  if 96 - 96: I1IiiI % i1IIi . o0oOOo0O0Ooo . O0
  for name , Ii1Iii11 in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + Ii1Iii11
   iconimage = 'https://i.ytimg.com/vi/' + Ii1Iii11 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     III1iII1I1ii ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 97 - 97: iI1 / o00oo . II111iiii
 if 'https://www.googleapis.com/youtube/v3' in url :
  OO0I111i1I = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   Oo0000oOo = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   I1IIiiI1II1 = oo00 + Oo0000oOo + o00 + OO0I111i1I + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , I1IIiiI1II1 , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 44 - 44: OoOO % OoOooOOOO . oO
  if 18 - 18: iIii1I11I1II1 + OoOooOOOO * I1IiiI - iI1 / I1IiiI
  if 78 - 78: OoOooOOOO . iIii1
  for name , Ii1Iii11 in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + Ii1Iii11
   iconimage = 'https://i.ytimg.com/vi/' + Ii1Iii11 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     III1iII1I1ii ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 38 - 38: OoOoOO00 + iIii1
     if 15 - 15: Oo0Ooo + OoOooOOOO . O0OOooO - iIii1I11I1II1 / O0 % iIii1I11I1II1
     if 86 - 86: I1IiiI / o00oo * OoOO
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 64 - 64: O0OOooO / O0 * OoOoOO00 * O0OOooO
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  i1II1 = liveresolver . resolve ( url )
 else : i1II1 = url
 i11i1 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 i11i1 . setPath ( i1II1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11i1 )
 if 60 - 60: OoOooOOOO / i1IIi % I1ii11iIi11i / I1ii11iIi11i * I1ii11iIi11i . i11iIiiIii
def o0oOO00 ( url ) :
 if 46 - 46: i11iIiiIii - OoOooOOOO
 try :
  oO0o0OOOO , url , O0O0OoOO0 = url . split ( "!SASPLIT!" )
  i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( url , i11i1 , False )
 except :
  xbmc . Player ( ) . play ( url )
  if 95 - 95: II111iiii
def o000o ( url ) :
 try :
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 65 - 65: OoOoOO00
  return o0O0O00
 except : quit ( )
 if 31 - 31: OoOooOOOO * OoOoOO00 . iIii1 % OoOO + Oo0Ooo
def Oo0oOOo ( url ) :
 if 47 - 47: O0 * I1IiiI * OoO0O00 . II111iiii
 if 95 - 95: OoOO % iIii1 . O0 % oO
 try :
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'obsession' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  if 68 - 68: Oo0Ooo . Oo0Ooo - I1ii11iIi11i / OoOooOOOO . O0OOooO / i1IIi
  iI1i1iIi1iiII = o00O ( o0O0O00 )
  print "--------- decoded --------" , iI1i1iIi1iiII
  OO00OooO0OO . close ( )
  iI1i1iIi1iiII = iI1i1iIi1iiII . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 53 - 53: OoOooOOOO
  return iI1i1iIi1iiII
 except : quit ( )
 if 68 - 68: o00oo / oO % oO % O0
def Oo0oO ( url ) :
 iII11I1IiiIi = urllib2 . Request ( url )
 iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 if 90 - 90: iIii1 . O0OOooO / iIii1I11I1II1
 return o0O0O00
 if 28 - 28: iIii1 + o00oo - O0OOooO / iIii1I11I1II1 - I1IiiI
def Ii1i1 ( ) :
 oOoO00 = [ ]
 i1i = sys . argv [ 2 ]
 if len ( i1i ) >= 2 :
  Ooo0OOoOoO0 = sys . argv [ 2 ]
  i1iIIi11i111I = Ooo0OOoOoO0 . replace ( '?' , '' )
  if ( Ooo0OOoOoO0 [ len ( Ooo0OOoOoO0 ) - 1 ] == '/' ) :
   Ooo0OOoOoO0 = Ooo0OOoOoO0 [ 0 : len ( Ooo0OOoOoO0 ) - 2 ]
  ii = i1iIIi11i111I . split ( '&' )
  oOoO00 = { }
  for IIi11i1i1iI1 in range ( len ( ii ) ) :
   iIii = { }
   iIii = ii [ IIi11i1i1iI1 ] . split ( '=' )
   if ( len ( iIii ) ) == 2 :
    oOoO00 [ iIii [ 0 ] ] = iIii [ 1 ]
 return oOoO00
 if 35 - 35: OoooooooOO - oO / OoO0O00
def iii11i1 ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 i1IiI1I111iIi = name . partition ( '(' )
 IiiIIi1 = ""
 iI1iIiiI = ""
 if len ( i1IiI1I111iIi ) > 0 :
  IiiIIi1 = i1IiI1I111iIi [ 0 ]
  iI1iIiiI = i1IiI1I111iIi [ 2 ] . partition ( ')' )
 if len ( iI1iIiiI ) > 0 :
  iI1iIiiI = iI1iIiiI [ 0 ]
 Oo0OOo = metahandlers . MetaData ( )
 OoO0o = Oo0OOo . get_meta ( 'movie' , name = IiiIIi1 , year = iI1iIiiI )
 Ii1I11i11I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = OoO0o [ 'cover_url' ] , thumbnailImage = OoO0o [ 'cover_url' ] )
 i11i1 . setInfo ( type = "Video" , infoLabels = OoO0o )
 oO00 = [ ]
 oO00 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i11i1 . addContextMenuItems ( oO00 , replaceItems = False )
 if not OoO0o [ 'backdrop_url' ] == '' : i11i1 . setProperty ( 'fanart_image' , OoO0o [ 'backdrop_url' ] )
 else : i11i1 . setProperty ( 'fanart_image' , Iii1ii1II11i )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11i11I1i , listitem = i11i1 , isFolder = isFolder , totalItems = itemcount )
 return iIiiIi11IIi
 if 7 - 7: O0 % oO + I1ii11iIi11i + OoOO % OoooooooOO . Oo0Ooo
def iiiI1I11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 Ii1I11i11I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : Ii1I11i11I1i = url
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11i11I1i , listitem = i11i1 , isFolder = True )
 return iIiiIi11IIi
 if 56 - 56: I1iiiiI1iII
def oO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 Ii1I11i11I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11i11I1i , listitem = i11i1 , isFolder = False )
 return iIiiIi11IIi
 if 84 - 84: OoOoOO00 - i11iIiiIii
def III1iII1I1ii ( name , url , mode , iconimage , fanart , description = '' ) :
 if 1 - 1: I1iiiiI1iII * OoOoOO00
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 Ii1I11i11I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  i11i1 . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : Ii1I11i11I1i = url
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11i11I1i , listitem = i11i1 , isFolder = False )
 return iIiiIi11IIi
 if 66 - 66: OoOoOO00 + i1IIi % II111iiii . O0 * I1ii11iIi11i % I1ii11iIi11i
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 87 - 87: iI1 + o0oOOo0O0Ooo . I1iiiiI1iII - OoooooooOO
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 Ii1I11i11I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 iIiiIi11IIi = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i11i1 . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  i11i1 . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : Ii1I11i11I1i = url
 iIiiIi11IIi = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11i11I1i , listitem = i11i1 , isFolder = False )
 return iIiiIi11IIi
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
def iIiI1I1ii1I1 ( url ) :
 if 83 - 83: iI1 / O0 % I1iiiiI1iII - o0oOOo0O0Ooo . Oo0Ooo
 iiiii1I1III1 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iiiii1I1III1 )
 sys . exit ( 1 )
 if 12 - 12: I1iiiiI1iII . OoOoOO00 * I1IiiI
def II1I1i1i1iii ( text , pattern ) :
 if 14 - 14: iI1
 iI1i11Iiii = ""
 try :
  o0oo0Ooooo0 = re . findall ( pattern , text , flags = re . DOTALL )
  iI1i11Iiii = o0oo0Ooooo0 [ 0 ]
 except :
  iI1i11Iiii = ""
  if 76 - 76: i1IIi * OoooooooOO * O0 + oO * oO
 return iI1i11Iiii
 if 35 - 35: o0oOOo0O0Ooo
def oooO ( str ) :
 if 73 - 73: O0 - I1ii11iIi11i
 try :
  import chardet
  str = str . decode ( chardet . detect ( str ) [ "encoding" ] ) . encode ( "utf-8" )
 except :
  try :
   str = str . encode ( "utf-8" )
  except :
   pass
 return str
 if 2 - 2: II111iiii / oO
def IIiIi1iI ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 OoO = xbmcgui . Window ( id )
 oO0oOOooo = 50
 while ( oO0oOOooo > 0 ) :
  try :
   xbmc . sleep ( 10 )
   oO0oOOooo -= 1
   OoO . getControl ( 1 ) . setLabel ( heading )
   OoO . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 99 - 99: iIii1I11I1II1
def IIiiiiIi1I ( link ) :
 try :
  I11i1I1I = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 56 - 56: OoooooooOO * O0
def iIIi1i1 ( ) :
 if 85 - 85: OoooooooOO % OoOoOO00 * iIii1I11I1II1
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 44 - 44: iIii1I11I1II1 . I1ii11iIi11i + oO . O0OOooO
 if II11iiii1Ii >= 1.0 and II11iiii1Ii <= 16.9 :
  II1i11 = 'Jarvis'
 elif II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  II1i11 = 'Krypton'
  if 28 - 28: II111iiii - o00oo % OoOoOO00 + OoO0O00 - OoOoOO00
 if II1i11 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif II1i11 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 28 - 28: II111iiii . o00oo + O0 . O0 . iI1
Ooo0OOoOoO0 = Ii1i1 ( ) ; OO00Oo = None ; oO0o0OOOO = None ; ooOoo000oO = None ; i1I1iI = None ; O0O0OoOO0 = None
try : i1I1iI = urllib . unquote_plus ( Ooo0OOoOoO0 [ "site" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( Ooo0OOoOoO0 [ "url" ] )
except : pass
try : oO0o0OOOO = urllib . unquote_plus ( Ooo0OOoOoO0 [ "name" ] )
except : pass
try : ooOoo000oO = int ( Ooo0OOoOoO0 [ "mode" ] )
except : pass
try : O0O0OoOO0 = urllib . unquote_plus ( Ooo0OOoOoO0 [ "iconimage" ] )
except : pass
try : Iii1ii1II11i = urllib . unquote_plus ( Ooo0OOoOoO0 [ "fanart" ] )
except : pass
if 92 - 92: Oo0Ooo / i11iIiiIii + I1ii11iIi11i
if ooOoo000oO == None or OO00Oo == None or len ( OO00Oo ) < 1 : II1III ( )
elif ooOoo000oO == 1 : o00oooO0Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif ooOoo000oO == 2 : i11ii1ii11i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 3 : o00Oo0oooooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 4 : OO0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 5 : SEARCH ( )
elif ooOoo000oO == 6 : YOUTUBE_CHANNEL ( OO00Oo )
elif ooOoo000oO == 7 : o0oOO00 ( OO00Oo )
elif ooOoo000oO == 8 : i1iI ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 9 : iIiI1I1ii1I1 ( OO00Oo )
elif ooOoo000oO == 10 : Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 11 : I1111i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 12 : IIii1 ( )
elif ooOoo000oO == 13 : IIi11i1II ( OO00Oo )
elif ooOoo000oO == 14 : o0i1iI1iiI1I ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 15 : oOOO ( OO00Oo )
elif ooOoo000oO == 16 : IiI ( OO00Oo )
elif ooOoo000oO == 17 : Ii1IIi ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 18 : oo00IIIIIIIiI ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 19 : OooOOOo0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 20 : o00oO0oo0OO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif ooOoo000oO == 21 : O0OO0O ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 22 : IIiiii ( OO00Oo )
elif ooOoo000oO == 23 : III1iI1iII1I ( )
elif ooOoo000oO == 24 : O0ooo0 ( OO00Oo )
elif ooOoo000oO == 25 : iIi11iiIiI1I ( OO00Oo )
elif ooOoo000oO == 26 : o0 ( )
elif ooOoo000oO == 27 : IiII1II11I ( OO00Oo )
elif ooOoo000oO == 28 : i11i1iiI1i ( OO00Oo )
elif ooOoo000oO == 29 : o000O000 ( OO00Oo )
elif ooOoo000oO == 32 : I1OooooO0oOOOO ( )
elif ooOoo000oO == 33 : iII1I1IiI11ii ( OO00Oo )
elif ooOoo000oO == 34 : OoOooOoO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 35 : OOOO0OOO ( )
elif ooOoo000oO == 36 : Oo0oooO0oO ( OO00Oo )
elif ooOoo000oO == 37 : oooooo0OO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif ooOoo000oO == 38 : iiiI ( )
elif ooOoo000oO == 39 : I1ii11 ( OO00Oo )
elif ooOoo000oO == 40 : i1iI1ii1 ( OO00Oo )
elif ooOoo000oO == 41 : IiiIIiiiiii ( )
elif ooOoo000oO == 42 : iIOo0O ( OO00Oo )
elif ooOoo000oO == 43 : IiiiIi1iI1iI ( OO00Oo , IiII , Iii1ii1II11i )
elif ooOoo000oO == 44 : i1iii11 ( OO00Oo )
elif ooOoo000oO == 45 : OOooOO000 ( OO00Oo )
elif ooOoo000oO == 46 : oOO0 ( )
elif ooOoo000oO == 47 : Ii1II ( OO00Oo )
elif ooOoo000oO == 48 : o0O0O0 ( OO00Oo )
elif ooOoo000oO == 49 : Ii111 ( )
elif ooOoo000oO == 50 : I1i1i ( OO00Oo )
elif ooOoo000oO == 51 : IIi ( OO00Oo )
elif ooOoo000oO == 52 : iI1I1iIi11 ( )
elif ooOoo000oO == 53 : III ( OO00Oo )
elif ooOoo000oO == 54 : Iiii11iIi1 ( OO00Oo )
elif ooOoo000oO == 55 : I11i1iIiiIiIi ( )
elif ooOoo000oO == 56 : IIiIiII ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
if 87 - 87: OoOoOO00 % iIii1I11I1II1
if 72 - 72: iI1 . iI1 - I1ii11iIi11i
if 48 - 48: Oo0Ooo - O0OOooO + Oo0Ooo - I1IiiI * i11iIiiIii . I1iiiiI1iII
if 35 - 35: iIii1 . O0 + Oo0Ooo + iI1 + i1IIi
if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
if 58 - 58: iI1 . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
if 50 - 50: I1iiiiI1iII % II111iiii - O0OOooO . i1IIi + O0 % I1iiiiI1iII
if 10 - 10: I1iiiiI1iII . i1IIi + OoOO
if 66 - 66: OoO0O00 % o0oOOo0O0Ooo
if 21 - 21: OoOoOO00 - OoooooooOO % i11iIiiIii
if 71 - 71: i1IIi - OoOooOOOO * oO + o00oo - OoO0O00 % I1ii11iIi11i
if 63 - 63: iIii1I11I1II1 + iI1 . OoO0O00 / I1IiiI
if 84 - 84: i1IIi
if ooOoo000oO == None or OO00Oo == None or len ( OO00Oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
