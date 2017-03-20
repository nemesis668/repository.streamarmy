import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , time , shutil , urlresolver , random , liveresolver , hashlib
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
I1i1iiI1 = base64 . b64decode ( b'aHR0cDovL3N0cmVhbWFybXkub2Zmc2hvcmVwYXN0ZWJpbi5jb20vTWFpbi9NZW51LnhtbA==' )
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
oOo0oooo00o = 'http://streamarmy.offshorepastebin.com/Main/Exceptions/Exceptions.xml'
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
 OO00Oo = "https://offshoregit.com/Nemzzy668/repository.streamarmy/addons.xml"
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
   elif '<cmovies>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 62 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<mflixcats>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 75 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<mflixpop>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 78 , O0O0OoOO0 , Iii1ii1II11i )
    if 49 - 49: I1IiiI % O0OOooO . O0OOooO . OoOooOOOO * O0OOooO
   elif '<cam>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 70 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<multisearch>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 91 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<porncom>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 65 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<shighlights>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 68 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<pornscrape>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 16 , O0O0OoOO0 , Iii1ii1II11i )
   elif '<sockshare>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 60 , O0O0OoOO0 , Iii1ii1II11i )
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
   elif '<vodly>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 60 , O0O0OoOO0 , Iii1ii1II11i )
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
   elif '<watch>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 30 , O0O0OoOO0 , Iii1ii1II11i )
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
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     OO00Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OO00Oo
     OO00Oo = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( oO0o0OOOO , OO00Oo , 4 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( O0oOO0 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( oO0o0OOOO , oO0OOoo0OO , 8 , O0O0OoOO0 , Iii1ii1II11i )
     if 65 - 65: OoOO . iIii1I11I1II1 / O0 - OoOO
   elif '<folder>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    oO0OOoo0OO = re . compile ( '<folder>(.+?)</folder>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    if 21 - 21: I1IiiI * iIii1I11I1II1
    if oO0OOoo0OO in iiIIiIiIi :
     iiiI1I11i1 ( oO0o0OOOO , oO0OOoo0OO , 1 , O0O0OoOO0 , Iii1ii1II11i )
    else :
     iiiI1I11i1 ( oO0o0OOOO , oO0OOoo0OO , 20 , O0O0OoOO0 , Iii1ii1II11i )
   else :
    if 91 - 91: iIii1
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i in iiIii :
      if 'youtube.com/playlist' in OO00Oo :
       iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
      else :
       oOoO0o00OO0 ( oO0o0OOOO , OO00Oo , 2 , O0O0OoOO0 , Iii1ii1II11i )
    elif len ( O0oOO0 ) > 1 :
     oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( oO0o0OOOO , oO0OOoo0OO , 3 , O0O0OoOO0 , Iii1ii1II11i )
     if 7 - 7: iI1 + oO + O0
     if 9 - 9: II111iiii . o0oOOo0O0Ooo - O0OOooO / o0oOOo0O0Ooo
  except : pass
  if 46 - 46: OoOooOOOO . iI1 * OoOooOOOO % i1IIi
  iIIiII ( )
  if 38 - 38: oO
def Ii1 ( url ) :
 if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / iI1 + OoOO
 OOOOoOoo0O0O0 = OOOo00oo0oO ( url )
 IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , OOOOoOoo0O0O0 )
 if 35 - 35: OoOO % O0 - O0
def i1OOO ( ) :
 OOOOoOoo0O0O0 = OOOo00oo0oO ( i1111 )
 if len ( OOOOoOoo0O0O0 ) > 1 :
  IiIIIi1iIi = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  ooOOoooooo = os . path . join ( os . path . join ( IiIIIi1iIi , '' ) , 'compare.txt' )
  II1I = open ( ooOOoooooo )
  O0i1II1Iiii1I11 = II1I . read ( )
  if O0i1II1Iiii1I11 == OOOOoOoo0O0O0 : pass
  else :
   IIiIi1iI ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , OOOOoOoo0O0O0 )
   IIII = open ( ooOOoooooo , "w" )
   IIII . write ( OOOOoOoo0O0O0 )
   IIII . close ( )
   if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
def o00oooO0Oo ( name , url , iconimage , fanart ) :
 oO0OOoo0OO = url
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
   elif '<sportsmamachans>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamachans>(.+?)</sportsmamachans>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<sportsmamagames>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamagames>(.+?)</sportsmamagames>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 44 , iconimage , fanart )
   elif '<porncom>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 65 , iconimage , fanart )
   elif '<multisearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 91 , iconimage , fanart )
   elif '<mflixcats>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 75 , iconimage , fanart )
   elif '<mflixpop>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 78 , iconimage , fanart )
    if 55 - 55: iI1 . I1IiiI
   elif '<cam>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 70 , iconimage , fanart )
   elif '<cmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 62 , iconimage , fanart )
   elif '<vodly>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<shighlights>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 68 , iconimage , fanart )
   elif '<sockshare>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
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
   elif '<watch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 30 , iconimage , fanart )
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
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , oO0OOoo0OO , 8 , iconimage , fanart )
     if 61 - 61: Oo0Ooo % iIii1 . Oo0Ooo
   elif '<folder>' in oO0Oo :
    iiIii = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in iiIii :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
      if 100 - 100: oO * O0
   else :
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for name , url , iconimage , fanart in iiIii :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       oOoO0o00OO0 ( name , url , 2 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( name , oO0OOoo0OO , 3 , iconimage , fanart )
  except : pass
 iIIiII ( )
 if 64 - 64: iI1 % iIii1I11I1II1 * o00oo
def o0 ( name , url , iconimage , fanart ) :
 if 37 - 37: o00oo - oO % Oo0Ooo
 if 77 - 77: Oo0Ooo - i1IIi - OoOooOOOO . OoOoOO00
 oO0OOoo0OO = url
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
   elif '<sportsmamachans>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamachans>(.+?)</sportsmamachans>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 12 , iconimage , fanart )
   elif '<sportsmamagames>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sportsmamagames>(.+?)</sportsmamagames>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 44 , iconimage , fanart )
   elif '<hdmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<hdmovies>(.+?)</hdmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 49 , iconimage , fanart )
   elif '<multisearch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<multisearch>(.+?)</multisearch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 91 , iconimage , fanart )
   elif '<cmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 62 , iconimage , fanart )
   elif '<mflixcats>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixcats>(.+?)</mflixcats>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 75 , iconimage , fanart )
   elif '<mflixpop>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<mflixpop>(.+?)</mflixpop>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 78 , iconimage , fanart )
    if 77 - 77: iI1 * iIii1I11I1II1
   elif '<shighlights>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<shighlights>(.+?)</shighlights>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 68 , iconimage , fanart )
   elif '<porncom>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<porncom>(.+?)</porncom>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 65 , iconimage , fanart )
   elif '<cam>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cam>(.+?)</cam>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 70 , iconimage , fanart )
   elif '<sockshare>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<sockshare>(.+?)</sockshare>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<pornhd>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<pornhd>(.+?)</pornhd>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 41 , iconimage , fanart , '' )
   elif '<vodly>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<vodly>(.+?)</vodly>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 60 , iconimage , fanart )
   elif '<soccerstreams>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 55 , iconimage , fanart )
   elif '<watch>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<watch>(.+?)</watch>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 30 , iconimage , fanart )
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
    O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oO0Oo ) [ 0 ]
     O0ooo0O0oo0 = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oO0Oo ) [ 0 ]
     oo0oOo = O0ooo0O0oo0
     o000O0o = "/"
     if not oo0oOo . endswith ( o000O0o ) :
      iI1iII1 = oo0oOo + "/"
     else :
      iI1iII1 = oo0oOo
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + iI1iII1
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     Ii1iIiII1ii1 ( name , oO0OOoo0OO , 8 , iconimage , fanart )
     if 98 - 98: I1IiiI % OoOO * OoooooooOO
   elif '<folder>' in oO0Oo :
    iiIii = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
    for name , url , iconimage , fanart in iiIii :
     if url in iiIIiIiIi :
      iiiI1I11i1 ( name , url , 1 , iconimage , fanart )
     else :
      iiiI1I11i1 ( name , url , 20 , iconimage , fanart )
   else :
    O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( oO0Oo )
    if len ( O0oOO0 ) == 1 :
     iiIii = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oO0Oo )
     ooo0O = len ( I11i1I1I )
     for name , url , iconimage , fanart in iiIii :
      if 'youtube.com/playlist' in url :
       iiiI1I11i1 ( name , url , 2 , iconimage , fanart )
      else :
       oOoO0o00OO0 ( name , url , 2 , iconimage , fanart )
    elif len ( O0oOO0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
     oOoO0o00OO0 ( name , oO0OOoo0OO , 3 , iconimage , fanart )
  except : pass
 iIIiII ( )
 if 51 - 51: iIii1I11I1II1 . OoOoOO00 / o00oo + o0oOOo0O0Ooo
def I11iI1i1I11I11 ( name , url , iconimage ) :
 if 69 - 69: OoOoOO00
 II1I , OO0OoOO0o0o = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 II1I += urllib . unquote_plus ( OO0OoOO0o0o )
 url = regex . resolve ( II1I )
 if 95 - 95: i11iIiiIii
 iI1111iiii ( name , url , iconimage )
 if 67 - 67: OoooooooOO / I1IiiI * OoOO + OoOooOOOO
def OooOo0ooo ( name , url , iconimage ) :
 if 71 - 71: oO + OoOO
 iI1111ii1I = urllib2 . Request ( url )
 iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 OO00OooO0OO = o0O0O00
 OO00OooO0OO = OO00OooO0OO . replace ( '#AAASTREAM:' , '#A:' )
 OO00OooO0OO = OO00OooO0OO . replace ( '#EXTINF:' , '#A:' )
 iiI11iI = re . compile ( '^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( OO00OooO0OO )
 oOOoO0o0oO = [ ]
 for o0Oo0oO0oOO00 , oo00OO0000oO , url in iiI11iI :
  I1II1 = { "params" : o0Oo0oO0oOO00 , "display_name" : oo00OO0000oO , "url" : url }
  oOOoO0o0oO . append ( I1II1 )
 list = [ ]
 for oooO in oOOoO0o0oO :
  I1II1 = { "display_name" : oooO [ "display_name" ] , "url" : oooO [ "url" ] }
  iiI11iI = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( oooO [ "params" ] )
  for i1I1i111Ii , ooo in iiI11iI :
   I1II1 [ i1I1i111Ii . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = ooo . strip ( )
  list . append ( I1II1 )
 for oooO in list :
  name = i1i1iI1iiiI ( oooO [ "display_name" ] )
  url = i1i1iI1iiiI ( oooO [ "url" ] )
  url = url . replace ( '\\r' , '' ) . replace ( '\\t' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( ' ' , '' ) . replace ( 'm3u8' , 'm3u8' )
  oOoO0o00OO0 ( name , url , 2 , IiII , Iii1ii1II11i , '' )
  if 51 - 51: I1IiiI % oO . o00oo / iIii1I11I1II1 / OoOooOOOO . o00oo
def IIIii11 ( name , url , iconimage ) :
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 o0O0O00 = Oo0oOOo ( url )
 II = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II ) [ 0 ]
 O0oOO0 = re . compile ( '<link>(.+?)</link>' ) . findall ( II )
 IIi11i1i1iI1 = 1
 for OOO0O00O0OOOO in O0oOO0 :
  I1iiii1I = OOO0O00O0OOOO
  if '(' in OOO0O00O0OOOO :
   OOO0O00O0OOOO = OOO0O00O0OOOO . split ( '(' ) [ 0 ]
   OOo0 = str ( I1iiii1I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( OOo0 )
  else :
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  if 75 - 75: i1IIi / O0 * o0oOOo0O0Ooo
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : IiI1iiiIii = liveresolver . resolve ( url )
  else : IiI1iiiIii = url
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
  if 38 - 38: I1iiiiI1iII + OoOooOOOO / oO % O0OOooO - I1ii11iIi11i
def iI11 ( name , url , iconimage ) :
 if 10 - 10: II111iiii / o00oo % OoooooooOO * OoOooOOOO % I1ii11iIi11i
 if 48 - 48: O0OOooO / oO . iIii1I11I1II1 * OoOoOO00 * o00oo / i1IIi
 OOOOoOOo0O0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 oOooo0 = [ ]
 o0O0O00 = o000o ( url )
 II = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 O0oOO0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( II )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( II ) [ 0 ]
 IIi11i1i1iI1 = 1
 if 58 - 58: I1IiiI . I1iiiiI1iII + OoOoOO00
 for OOO0O00O0OOOO in O0oOO0 :
  I1iiii1I = OOO0O00O0OOOO
  if '(' in OOO0O00O0OOOO :
   OOO0O00O0OOOO = OOO0O00O0OOOO . split ( '(' ) [ 0 ]
   OOo0 = str ( I1iiii1I . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( OOo0 )
   oOooo0 . append ( 'Stream ' + str ( IIi11i1i1iI1 ) )
  else :
   iiIiIIIiiI . append ( OOO0O00O0OOOO )
   iiI1IIIi . append ( 'Link ' + str ( IIi11i1i1iI1 ) )
   if 66 - 66: I1iiiiI1iII / o00oo * OoooooooOO + OoooooooOO % OoOooOOOO
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 I11 = xbmcgui . Dialog ( )
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  oo0oOo = iiI1IIIi [ oO00ooooO0o ]
  o000O0o = "/"
  if not oo0oOo . endswith ( o000O0o ) :
   iI1iII1 = oo0oOo + "/"
  else :
   iI1iII1 = oo0oOo
  url = OOOOoOOo0O0 + iiIiIIIiiI [ oO00ooooO0o ] + "%26referer=" + iI1iII1
  print url
  if 49 - 49: o00oo - i11iIiiIii . oO * OoOO % I1iiiiI1iII + i1IIi
  xbmc . Player ( ) . play ( url )
  if 71 - 71: o0oOOo0O0Ooo
  if 38 - 38: o00oo % OoOoOO00 + I1ii11iIi11i . i11iIiiIii
  if 53 - 53: i11iIiiIii * I1iiiiI1iII
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . o0oOOo0O0Ooo / II111iiii % Oo0Ooo
  if 38 - 38: O0OOooO - iI1 / I1iiiiI1iII
  if 66 - 66: O0 % I1ii11iIi11i + i11iIiiIii . OoOoOO00 / OoOO + I1ii11iIi11i
  if 86 - 86: o0oOOo0O0Ooo
def i1Iii11Ii1i1 ( ) :
 if 59 - 59: Oo0Ooo % OoooooooOO . I1iiiiI1iII / iIii1 + I1IiiI
 OO00Oo = 'http://www.animetoon.org/dubbed-anime'
 if 76 - 76: O0OOooO
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 36 - 36: iI1 + O0 - OoOO - O0 % OoOooOOOO . o00oo
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   oooiiI = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oooiiI + "[/COLOR]" , OO00Oo , 33 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
def ii111I ( url ) :
 if 17 - 17: I1IiiI . O0 + OoO0O00
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 43 - 43: II111iiii . o00oo / I1ii11iIi11i
 for i1iI1 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 34 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 33 - 33: iIii1 % iIii1I11I1II1 * I1IiiI
def o00o0 ( name , url , iconimage ) :
 if 50 - 50: Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
 o0O0O00 = o000o ( url )
 O0O0Oo00 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOoO00o ( name , O0O0Oo00 , iconimage )
 if 100 - 100: o0oOOo0O0Ooo + iI1 * o0oOOo0O0Ooo
 if 80 - 80: o0oOOo0O0Ooo * O0 - OoOO
 if 66 - 66: i11iIiiIii - iI1 * Oo0Ooo
 if 76 - 76: i11iIiiIii + o0oOOo0O0Ooo / I1ii11iIi11i - OoO0O00 - OoOO + I1ii11iIi11i
 if 51 - 51: iIii1I11I1II1 . O0OOooO + iIii1I11I1II1
 if 95 - 95: I1IiiI
 if 46 - 46: OoOoOO00 + OoO0O00
def o0o0O ( ) :
 if 68 - 68: O0OOooO
 OO00Oo = 'http://www.toonget.net/cartoon'
 if 25 - 25: I1ii11iIi11i . O0OOooO
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 24 - 24: o00oo / i11iIiiIii + o00oo
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   oooiiI = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oooiiI + "[/COLOR]" , OO00Oo , 36 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 20 - 20: OoOooOOOO + OoOO / O0 % iIii1I11I1II1
def oOo0O ( url ) :
 if 64 - 64: I1ii11iIi11i - I1iiiiI1iII + I1iiiiI1iII - OoOooOOOO
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 30 - 30: iIii1I11I1II1 . I1IiiI . iI1 / o0oOOo0O0Ooo
 for i1iI1 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( i1iI1 ) [ 0 ]
   oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 37 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 42 - 42: Oo0Ooo
 try :
  II1IIiiIiI = re . compile ( '<li><a href=\"([^"]*)\">Next' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , II1IIiiIiI , 36 , IiII , iI111iI , '' )
 except : pass
 if 1 - 1: I1iiiiI1iII
def O0O0Ooo ( name , url , iconimage ) :
 if 77 - 77: o0oOOo0O0Ooo / OoooooooOO
 o0O0O00 = o000o ( url )
 O0O0Oo00 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOoO00o ( name , O0O0Oo00 , iconimage )
 if 46 - 46: o0oOOo0O0Ooo % iIii1I11I1II1 . I1iiiiI1iII % I1iiiiI1iII + i11iIiiIii
 if 72 - 72: iIii1I11I1II1 * OoOO % O0OOooO / OoO0O00
 if 35 - 35: O0OOooO + i1IIi % I1ii11iIi11i % OoOooOOOO + o00oo
 if 17 - 17: i1IIi
 if 21 - 21: Oo0Ooo
 if 29 - 29: OoOooOOOO / II111iiii / O0OOooO * iI1
 if 10 - 10: oO % iIii1 * iIii1 . OoOooOOOO / OoOO % iI1
def IIII1 ( ) :
 if 10 - 10: oO / O0OOooO + i11iIiiIii / OoOO
 OO00Oo = 'http://www.readcomics.tv/comic-list'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 74 - 74: iI1 + O0 + i1IIi - i1IIi + II111iiii
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 39 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 83 - 83: I1ii11iIi11i - I1IiiI + iI1
def iIi1Ii1i1iI ( url ) :
 if 16 - 16: iI1 / Oo0Ooo / OoooooooOO * I1IiiI + i1IIi % iI1
 o0O0O00 = o000o ( url )
 ooo0o00 = re . compile ( '<div class="manga-image"><img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oO0o0OOOO = re . compile ( '<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ] . replace ( 'Read ' , '' ) . replace ( 'Online' , '' )
 ooO = re . compile ( '<a class="stread" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = ooO . split ( '/' ) [ - 1 ]
 O00oO = o0O . replace ( 'chapter-' , ' ' )
 O00oO = int ( O00oO )
 iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , ooO , 40 , ooo0o00 , iI111iI , '' )
 I11i1I1I = re . compile ( '<ul class="ml-list">(.+?)</ul>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0oOO0 in sorted ( OoO0O00O0oo0O ) :
  O00oO = O00oO + 1
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , url , 40 , ooo0o00 , iI111iI , '' )
  if 74 - 74: I1IiiI
def o0o0oOoOO0O ( url ) :
 if 16 - 16: iIii1 % iIii1I11I1II1 . OoOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' )
 oooooOOO000Oo = re . compile ( '<div class="label">of (.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 52 - 52: II111iiii % iIii1 . OoOoOO00 * iIii1I11I1II1
 oooooOOO000Oo = int ( oooooOOO000Oo )
 I111i1II = re . compile ( '<img id="main_img" src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = I111i1II . replace ( '.jpg' , '' ) . replace ( 'http://' , '' )
 O00oO = o0O . split ( '/' )
 O0ooooo0OOOO0 = len ( O00oO )
 IiiIi1III = O0ooooo0OOOO0 - 1
 O0Oo = 1
 ii11i11i1 = ""
 for Ooo0o00o0o in O00oO :
  if O0Oo <= IiiIi1III :
   ii11i11i1 = ii11i11i1 + "/" + Ooo0o00o0o
   O0Oo = O0Oo + 1
   if 7 - 7: O0 - Oo0Ooo + I1ii11iIi11i + II111iiii + iIii1I11I1II1
 OOo0ii11I1 = 1
 ii11i11i1 = "http://" + ii11i11i1 + "/"
 if 75 - 75: OoO0O00 / II111iiii % O0
 while OOo0ii11I1 <= oooooOOO000Oo :
  url = ii11i11i1 + str ( OOo0ii11I1 ) + ".jpg"
  oO0 ( "[COLOR lime]Page " + str ( OOo0ii11I1 ) + "[/COLOR]" , url , 9 , url , url , '' )
  OOo0ii11I1 = OOo0ii11I1 + 1
  if 38 - 38: OoooooooOO * O0OOooO % O0 * OoOoOO00
  if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - OoOO
  if 20 - 20: i1IIi % OoO0O00 . I1IiiI / iIii1 * i11iIiiIii * iI1
  if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / O0OOooO . O0 % oO
  if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . I1iiiiI1iII
  if 8 - 8: O0OOooO + II111iiii / I1iiiiI1iII / OoOooOOOO
  if 74 - 74: O0 / i1IIi
def OoO ( url ) :
 if 41 - 41: i1IIi * II111iiii / OoooooooOO . iI1
 if 83 - 83: I1iiiiI1iII . O0 / Oo0Ooo / iI1 - II111iiii
 o0O0O00 = o000o ( url ) . replace ( '&amp;' , 'and' )
 if 100 - 100: OoO0O00
 if 46 - 46: OoOoOO00 / iIii1I11I1II1 % I1iiiiI1iII . iIii1I11I1II1 * I1iiiiI1iII
 I11i1I1I = re . compile ( '<li.+?href="(.+?)".+?>(.+?)</a.+?li>' ) . findall ( o0O0O00 )
 for oO0OOoo0OO , IIi1ii1Ii in I11i1I1I :
  if oO0OOoo0OO . find ( 'categ' ) != - 1 :
   OoOoO = url + oO0OOoo0OO
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , OoOoO , 25 , IiII , iI111iI , '' )
   if 83 - 83: iI1 . i1IIi / OoooooooOO
def IIiIiiii ( url ) :
 if 89 - 89: I1iiiiI1iII - O0OOooO % Oo0Ooo % o0oOOo0O0Ooo
 IIiii11i = o000o ( url ) . replace ( '&#8217;' , "'" )
 O00oOo00o0o = re . compile ( '<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"' , re . DOTALL ) . findall ( IIiii11i )
 for url , O00oO0 , oO0o0OOOO in O00oOo00o0o :
  O0Oo00OoOo = o000o ( url )
  ii1ii111 = re . compile ( '<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"' ) . findall ( O0Oo00OoOo )
  for i11111I1I in ii1ii111 :
   try :
    ii1 = i11111I1I . split ( "/embed/" ) [ 1 ]
    Oo0000oOo = "plugin://plugin.video.youtube/play/?video_id=" + ii1
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , Oo0000oOo , 7 , O00oO0 , iI111iI , '' )
   except : pass
   if 31 - 31: OoOooOOOO . oO * O0OOooO + i11iIiiIii * o00oo
 try :
  II1IIiiIiI = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( IIiii11i ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , II1IIiiIiI , 25 , IiII , iI111iI , '' )
 except : pass
 if 93 - 93: I1ii11iIi11i / iIii1I11I1II1 * i1IIi % OoooooooOO * O0 * OoOooOOOO
 if 64 - 64: II111iiii + O0 / iIii1I11I1II1 / Oo0Ooo . O0OOooO % iIii1
 if 50 - 50: iIii1I11I1II1 - iIii1 + iI1
 if 69 - 69: O0
 if 85 - 85: O0OOooO / O0
 if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
 if 62 - 62: oO . iIii1 . OoooooooOO
def i111 ( ) :
 if 27 - 27: i11iIiiIii / I1ii11iIi11i
 OO00Oo = 'http://www.filmon.com/tv/bbc-news'
 if 84 - 84: Oo0Ooo
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"group_id"(.+?)channels_count' ) . findall ( o0O0O00 )
 for iIiiiii1i in I11i1I1I :
  oO0o0OOOO = re . compile ( 'title":"(.+?)"' ) . findall ( iIiiiii1i ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , iIiiiii1i , 27 , IiII , iI111iI , '' )
  if 40 - 40: O0 - OoooooooOO - iIii1
def iIiii ( url ) :
 if 76 - 76: I1IiiI . O0OOooO - I1ii11iIi11i - I1iiiiI1iII * OoO0O00
 I11i1I1I = re . compile ( '{"id"(.+?)}' ) . findall ( url )
 for O0Oo00O in I11i1I1I :
  oO0o0OOOO = re . compile ( ':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"' ) . findall ( O0Oo00O ) [ 0 ]
  O0O0OoOO0 = re . compile ( ':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"' ) . findall ( O0Oo00O ) [ 0 ]
  url = re . compile ( ':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"' ) . findall ( O0Oo00O ) [ 0 ]
  O0O0OoOO0 = O0O0OoOO0 . replace ( '\\' , '' )
  oO0OOoo0OO = 'https://www.filmon.com/tv/' + url
  oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , oO0OOoo0OO , 2 , O0O0OoOO0 , iI111iI , '' )
  if 91 - 91: o00oo % OoOO . O0OOooO / I1iiiiI1iII * iIii1I11I1II1
  if 43 - 43: O0OOooO + I1iiiiI1iII - oO / O0 * Oo0Ooo + I1IiiI
  if 28 - 28: OoOO * o0oOOo0O0Ooo - OoO0O00
  if 42 - 42: I1ii11iIi11i
  if 76 - 76: I1ii11iIi11i * II111iiii . I1IiiI - Oo0Ooo + o00oo + i11iIiiIii
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
  for O0oOO0 in I11i1I1I :
   IIi1ii1Ii = re . compile ( '<a title="(.+?)" href=".+?">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   o0O0O00 = re . compile ( '<a title=".+?" href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   O00oO0 = re . compile ( 'src="(.+?)"/>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OOOooo = re . compile ( '<div class="video_quality">(.+?)</div>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   IIiii11i = 'http://hdvidmusic.com' + o0O0O00
   Oo00oo0000OO = 'http://hdvidmusic.com' + O00oO0
   oO0 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 29 , Oo00oo0000OO , iI111iI , '' )
  IIIii = IIIii + 1
  if 69 - 69: O0OOooO - OoO0O00 / i11iIiiIii + I1ii11iIi11i % OoooooooOO
def o000O000 ( url ) :
 if 19 - 19: iIii1I11I1II1
 IIiii11i = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe id\=.+?www(.+?)aut' ) . findall ( IIiii11i ) [ 0 ]
 id = Ii1IiI1i1ii . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 30 - 30: iIii1 + oO - iIii1 . iIii1 - II111iiii + O0
def oOO0 ( ) :
 OO00Oo = 'http://www.bigtop40.com/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&amp;' , 'and' ) . replace ( '&#39;' , "'" ) . replace ( '&quot;' , '"' )
 I11i1I1I = re . compile ( '<li data-chart-position=".+?"(.+?)</em>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  try :
   i1IIiIii1i = re . compile ( '<a name="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ] . replace ( 'number' , 'Number' ) . replace ( '_' , ' ' )
   ooo0o00 = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   ooOOO0OooOo = re . compile ( 'alt="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in OO00Oo :
    oO0OOoo0OO = 'http://www.bigtop40.com' + OO00Oo
    oO0 ( "[COLOR red]" + i1IIiIii1i + "[/COLOR]" + ' -- ' + "[COLOR lime]" + ooOOO0OooOo + "[/COLOR]" , oO0OOoo0OO , 47 , ooo0o00 , iI111iI , '' )
  except : pass
  if 33 - 33: iI1 / i1IIi - I1IiiI % Oo0Ooo . I1ii11iIi11i
def Ii1II ( url ) :
 IIiii11i = o000o ( url ) . replace ( '?' , '' )
 Ii1IiI1i1ii = re . compile ( '<iframe width=".+?" height="348" src="(.+?)"' ) . findall ( IIiii11i ) [ 0 ]
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
  II1IIiiIiI = re . compile ( '<div class="nav-previous alignleft"><a href="(.+?)" ></a>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , II1IIiiIiI , 50 , IiII , iI111iI , '' )
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
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , I1III1111iIi , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 58 - 58: iI1 * o0oOOo0O0Ooo + O0 % iI1
def iI1I1iIi11 ( ) :
 iiiI1I11i1 ( "[COLOR red] Search [/COLOR]" , 'null' , 90 , IiII , iI111iI , '' )
 OO00Oo = "http://www.afdah.bz/"
 o0O0O00 = o000o ( OO00Oo )
 OoO0O00O0oo0O = re . compile ( '<li class="cat-item.+?<a href="(.+?)" >(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for OO00Oo , oO0o0OOOO in sorted ( OoO0O00O0oo0O ) :
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 53 , IiII , iI111iI , '' )
  if 87 - 87: OoOoOO00
def Ii ( url ) :
 if 65 - 65: OoOoOO00 / OoO0O00 % iIii1
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 37 - 37: i1IIi
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 98 - 98: II111iiii % O0OOooO * iIii1I11I1II1 + OoOooOOOO + II111iiii % OoOooOOOO
 OOoOoO00O0O0o = url
 if 12 - 12: I1ii11iIi11i + OoO0O00 % OoOooOOOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="movie-preview-content">(.+?)Views</small>' , re . DOTALL ) . findall ( o0O0O00 )
 if 85 - 85: I1iiiiI1iII * o0oOOo0O0Ooo
 for oO0Oo in sorted ( I11i1I1I , reverse = True ) :
  oO0OOoo0OO = re . compile ( '<a href="(.+?)" title=".+?">.+?</a>' , re . DOTALL ) . findall ( oO0Oo ) [ - 1 ]
  oO0o0OOOO = re . compile ( '<a href=".+?" title=".+?">(.+?)</a>' , re . DOTALL ) . findall ( oO0Oo ) [ - 1 ]
  oO0o0OOOO = oO0o0OOOO . replace ( "Afdah" , "" )
  oO0o0OOOO = iii11 ( oO0o0OOOO )
  try :
   OOOooo = re . compile ( 'Quality">(.+?)<' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  except : OOOooo = "Unknown"
  oO0o0OOOO = "[COLOR lime]" + oO0o0OOOO + ' - Quality = ' "[/COLOR]" "[COLOR yellow]" + OOOooo + "[/COLOR]"
  ooo0o00 = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  III1i1iI1 . append ( oO0o0OOOO )
  o0ooo00o . append ( oO0OOoo0OO )
  oOO00oO00O0OO . append ( ooo0o00 )
  o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  if 3 - 3: iI1
  if 20 - 20: II111iiii . I1iiiiI1iII / II111iiii % i11iIiiIii % I1iiiiI1iII
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   oO0 ( IIi1ii1Ii , IIiii11i , 54 , IiII , iI111iI , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     oO0 ( IIi1ii1Ii , IIiii11i , 54 , IiII , iI111iI , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     oO0 ( IIi1ii1Ii , IIiii11i , 54 , IiII , iI111iI , '' )
     if 55 - 55: O0OOooO % OoooooooOO / OoooooooOO % OoooooooOO
 try :
  if not '?s=' in url :
   II1IIiiIiI = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , II1IIiiIiI , 53 , IiII , iI111iI , '' )
 except : pass
 if 52 - 52: I1ii11iIi11i + I1ii11iIi11i . II111iiii
def Iii ( url ) :
 if 6 - 6: iI1 - I1ii11iIi11i + OoOO + i1IIi / O0 / o0oOOo0O0Ooo
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 try :
  import urlresolver
  if urlresolver . HostedMediaFile ( I11i1I1I ) . valid_url ( ) :
   I11i1I1I = urlresolver . HostedMediaFile ( I11i1I1I ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( I11i1I1I )
   xbmc . Player ( ) . play ( I11i1I1I , I1III1111iIi , False )
  else :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 except :
  I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  if 42 - 42: i1IIi . I1IiiI / i1IIi + OoOO
def O0o0O0OO00o ( ) :
 if 92 - 92: o0oOOo0O0Ooo + oO / Oo0Ooo % OoO0O00 % iIii1 . OoooooooOO
 ii11i11i1 = ''
 O0OoI1IiI111I11 = xbmc . Keyboard ( ii11i11i1 , 'Enter Search Term' )
 O0OoI1IiI111I11 . doModal ( )
 if O0OoI1IiI111I11 . isConfirmed ( ) :
  ii11i11i1 = O0OoI1IiI111I11 . getText ( )
  if len ( ii11i11i1 ) > 1 :
   OOo00 = ii11i11i1 . lower ( )
   OOo00 = OOo00 . replace ( " " , "+" )
  else : quit ( )
  if 16 - 16: O0 / OoOO . I1ii11iIi11i
 OO00Oo = "http://www.afdah.bz/?s=" + OOo00
 if 58 - 58: Oo0Ooo / o00oo
 Ii ( OO00Oo )
 if 44 - 44: iI1
def O0O0o0o0o ( ) :
 if 9 - 9: Oo0Ooo + OoOoOO00 - iIii1I11I1II1 - OoOO + o0oOOo0O0Ooo
 ii11i11i1 = ''
 O0OoI1IiI111I11 = xbmc . Keyboard ( ii11i11i1 , 'Search For A Movie' )
 O0OoI1IiI111I11 . doModal ( )
 if O0OoI1IiI111I11 . isConfirmed ( ) :
  o000O0OOoo = O0OoI1IiI111I11 . getText ( )
  OOo00 = o000O0OOoo
  ii11i11i1 = o000O0OOoo . replace ( ' ' , '+' )
  if not len ( ii11i11i1 ) > 1 :
   I11 . ok ( "STREAM ARMY" , "No search term was entered." )
   quit ( )
   if 60 - 60: I1IiiI * oO % OoO0O00 + o00oo
  ii11i11i1 = ii11i11i1 . replace ( ' ' , '+' )
  OO00Oo = "http://housemovie.to/search?q=" + ii11i11i1
  o0O0O00 = o000o ( OO00Oo )
  I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
  if 52 - 52: i1IIi
  for i1iI1 in I11i1I1I :
   try :
    oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( i1iI1 ) [ 0 ]
    OO00Oo = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( i1iI1 ) [ 0 ]
    O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    try :
     o000 = re . compile ( '<span class="imdb">(.+?)</span>' ) . findall ( i1iI1 ) [ 0 ]
    except : o000 = "IMDB Rating Unknown"
    if not "http" in OO00Oo :
     OO00Oo = "http://housemovie.to" + OO00Oo
     oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR] - [COLOR yellow][I]" + o000 + "[/I][/COLOR]" , OO00Oo , 21 , O0O0OoOO0 , iI111iI , '' )
   except : pass
   if 94 - 94: o0oOOo0O0Ooo + O0 / OoOooOOOO . I1IiiI + iI1 . iIii1I11I1II1
def OOOoO ( url ) :
 if 57 - 57: OoO0O00 / i1IIi . i1IIi
 o0O0O00 = o000o ( url )
 if 74 - 74: iIii1I11I1II1 * iIii1 % OoOoOO00
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 36 - 36: OoooooooOO - o00oo
 for O0oOO0 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( O0oOO0 ) [ 0 ]
   oO0OOoo0OO = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0oOO0 ) [ 0 ]
   if "genres" in oO0OOoo0OO :
    oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
    iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , oO0OOoo0OO , 19 , IiII , iI111iI , '' )
  except : pass
  if 85 - 85: o0oOOo0O0Ooo . iIii1 / O0 . o0oOOo0O0Ooo . I1ii11iIi11i . OoO0O00
def OO0O0Oo0 ( url ) :
 if 74 - 74: o0oOOo0O0Ooo + Oo0Ooo
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 51 - 51: I1iiiiI1iII * OoooooooOO - OoO0O00 - OoooooooOO
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 95 - 95: OoOooOOOO * Oo0Ooo + OoOoOO00 / O0
 OOoOoO00O0O0o = url
 if 37 - 37: i1IIi
 o0O0O00 = o000o ( url )
 if 91 - 91: OoOoOO00 + O0OOooO . I1IiiI
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 71 - 71: I1iiiiI1iII % o0oOOo0O0Ooo / iI1 / Oo0Ooo
 for O0oOO0 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   o000 = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   if "(SOON)" in oO0o0OOOO :
    OO0OO0OO = oO0o0OOOO . split ( "(SOON)" ) [ 0 ]
    oO0o0OOOO = OO0OO0OO . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
   else : oO0o0OOOO = oO0o0OOOO . title ( )
   if 'search?' in url :
    oO0OOoo0OO = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( O0oOO0 ) [ 0 ]
   else :
    oO0OOoo0OO = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0oOO0 ) [ 0 ]
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if "watch" in oO0OOoo0OO :
    oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
    III1i1iI1 . append ( oO0o0OOOO )
    o0ooo00o . append ( oO0OOoo0OO )
    oOO00oO00O0OO . append ( O0O0OoOO0 )
    o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  except : pass
  if 61 - 61: OoooooooOO . o00oo . OoooooooOO / Oo0Ooo
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + o000 + "[/I][/COLOR]" , oO0OOoo0OO , 21 , O0O0OoOO0 , iI111iI , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + o000 + "[/I][/COLOR]" , oO0OOoo0OO , 21 , O0O0OoOO0 , iI111iI , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + o000 + "[/I][/COLOR]" , oO0OOoo0OO , 21 , O0O0OoOO0 , iI111iI , '' )
     if 72 - 72: i1IIi
     if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
     if 63 - 63: I1ii11iIi11i
def i1II ( name , url , iconimage ) :
 if 2 - 2: II111iiii - OoO0O00 . iIii1 * I1iiiiI1iII / o00oo
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 OOo0iiIii1IIi = [ ]
 ii1IiIiI1 = [ ]
 if 90 - 90: o0oOOo0O0Ooo - i11iIiiIii + i1IIi - OoOO % Oo0Ooo
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 59 - 59: iI1 % iIii1I11I1II1 . i1IIi + II111iiii * iIii1
 I11i1I1I = re . compile ( '<div class="fig_holder">(.+?)</div>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  name = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
  oO0OOoo0OO = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  iconimage = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  try :
   o000 = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
  except : o000 = "0.0"
  if "imdb" in o000 . lower ( ) :
   o000 = o000 . replace ( "IMDB: " , "" ) . replace ( " " , "" )
  if not "." in o000 :
   o000 = o000 + ".0"
   if 41 - 41: OoOO % I1ii11iIi11i
  if "(SOON)" in name :
   OO0OO0OO = name . split ( "(SOON)" ) [ 0 ]
   name = OO0OO0OO . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
  else : name = name . title ( )
  oO0OOoo0OO = "http://housemovie.to" + oO0OOoo0OO
  if 12 - 12: iI1
  III1i1iI1 . append ( name )
  o0ooo00o . append ( oO0OOoo0OO )
  oOO00oO00O0OO . append ( iconimage )
  OOo0iiIii1IIi . append ( o000 )
  ii1IiIiI1 = list ( zip ( OOo0iiIii1IIi , III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  if 69 - 69: OoooooooOO + iI1
 IIi11I1 = sorted ( ii1IiIiI1 , reverse = True )
 if 49 - 49: II111iiii - I1IiiI / OoOooOOOO
 for o000 , name , oO0OOoo0OO , iconimage in IIi11I1 :
  if o000 == "0.0" :
   o000 = "IMDB Rating Unknown"
  else : o000 = "IMDB: " + o000
  oO0 ( "[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + o000 + "[/I][/COLOR]" , oO0OOoo0OO , 21 , iconimage , iI111iI , '' )
  if 74 - 74: OoOooOOOO - iI1 + i1IIi . I1IiiI + iI1 - OoOooOOOO
 try :
  IiIiiiiI1 = re . compile ( '<a href="([^"]*)" class="page_next">Next</a>' ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , IiIiiiiI1 , 19 , IiII , iI111iI , '' )
 except : pass
 if 62 - 62: I1ii11iIi11i % I1iiiiI1iII * OoO0O00 - i1IIi
def OoOOo ( name , url , iconimage ) :
 if 17 - 17: i1IIi
 iiI1IIIi = [ ]
 iiIiIIIiiI = [ ]
 II11IiIi11 = [ ]
 if 1 - 1: O0OOooO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 78 - 78: I1ii11iIi11i + OoOooOOOO - O0
 O0oOO0 = re . compile ( '<div class="md_full_cell">(.+?)</div>' ) . findall ( o0O0O00 )
 if 10 - 10: oO % I1IiiI
 for II in O0oOO0 :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( II ) [ 0 ]
   IIi1ii1Ii = re . compile ( 'rel="nofollow">(.+?)</a>' ) . findall ( II ) [ 0 ]
   url = "http://housemovie.to" + url
   for IiIiiI11111I1 in oo0o0O00 :
    if IiIiiI11111I1 . lower ( ) in IIi1ii1Ii . lower ( ) :
     if 97 - 97: OoooooooOO - oO
     iiI1IIIi . append ( IIi1ii1Ii )
     iiIiIIIiiI . append ( url )
     II11IiIi11 . append ( iconimage )
  except : pass
  if 58 - 58: iIii1I11I1II1 + O0
  if 30 - 30: O0OOooO % I1iiiiI1iII * iI1 - I1ii11iIi11i * OoOO % O0OOooO
 name = '[COLOR lime]' + name + '[/COLOR]'
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  url = str ( url )
  IiII = II11IiIi11 [ oO00ooooO0o ]
  IiII = str ( IiII )
  if 46 - 46: i11iIiiIii - O0 . o00oo
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 100 - 100: I1IiiI / o0oOOo0O0Ooo * I1iiiiI1iII . O0 / iI1
  url = re . compile ( '<a href="([^"]*)" target="_blank" class="button_type_1">' ) . findall ( o0O0O00 ) [ 0 ]
  if 83 - 83: oO
  try :
   import urlresolver
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
    I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
    I1III1111iIi . setPath ( IiI1iiiIii )
    xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
   else : I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  except :
   I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
   if 48 - 48: II111iiii * iI1 * oO
def i1iiiIii11 ( url ) :
 if 67 - 67: o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - O0OOooO
 url = 'http://cmovieshd.com/library/'
 o0O0O00 = o000o ( url )
 if 90 - 90: O0OOooO + II111iiii * I1ii11iIi11i / OoOO . o0oOOo0O0Ooo + o0oOOo0O0Ooo
 I11i1I1I = re . compile ( '<div class="movies-letter">(.+?)<div class="clearfix">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 I11I = re . compile ( '<a(.+?)</a>' , re . DOTALL ) . findall ( I11i1I1I )
 for O0oOO0 in I11I :
  oO0OOoo0OO = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  oOoO = re . compile ( 'href=".+?">(.+?)' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ] . replace ( '0' , '0-9' )
  iiiI1I11i1 ( "[COLOR lime]" + oOoO + "[/COLOR]" , oO0OOoo0OO , 63 , IiII , iI111iI , '' )
  if 26 - 26: OoOoOO00 / Oo0Ooo - i1IIi + OoOooOOOO
def IiiIi ( url ) :
 if 10 - 10: OoO0O00 / Oo0Ooo
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 15 - 15: I1iiiiI1iII . OoOoOO00 / I1iiiiI1iII * OoOooOOOO - I1IiiI % I1ii11iIi11i
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 57 - 57: O0 % OoOoOO00 % o00oo
 OOoOoO00O0O0o = url
 if 45 - 45: I1ii11iIi11i + II111iiii * i11iIiiIii
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I11i1I1I = re . compile ( '<div class="movies-list">(.+?)<div class="clearfix">' ) . findall ( o0O0O00 ) [ 0 ]
  Ooo0o00o0o = re . compile ( '<a href="(.+?)" rel=".+?" class=".+?" title="(.+?)">.+?<img data-original="(.+?)"' ) . findall ( I11i1I1I )
  for O0oOO0 , IIi1ii1Ii , IiII in Ooo0o00o0o :
   IIiii11i = O0oOO0 + 'watch/openload-0.html'
   if 13 - 13: OoooooooOO * o00oo - OoOO / iI1 + OoOooOOOO + iIii1
  III1i1iI1 . append ( IIi1ii1Ii )
  o0ooo00o . append ( IIiii11i )
  oOO00oO00O0OO . append ( IiII )
  o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  if 39 - 39: iIii1I11I1II1 - OoooooooOO
  for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
   if iIiIIii == 0 :
    iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 64 , IiII , iI111iI , '' )
   else :
    if ' ' in OOo00 :
     I11Ii11iI1 = 0
     IiIiiI11111I1 = OOo00 . split ( " " )
     for oo0oOo in IiIiiI11111I1 :
      if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
       I11Ii11iI1 = 1
     if I11Ii11iI1 == 0 :
      iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 74 , IiII , iI111iI , '' )
    else :
     if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
      iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 74 , IiII , iI111iI , '' )
 except : pass
def oO0oooooo ( url ) :
 if 65 - 65: iIii1 + Oo0Ooo
 if 59 - 59: OoooooooOO + OoOooOOOO . oO - O0 % iIii1I11I1II1 / O0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( 'var movie =(.+?)data-toggle="tooltip"]' ) . findall ( o0O0O00 ) [ 0 ]
 OOooO0o = re . compile ( 'embed_src.+?"(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
 if 25 - 25: iIii1I11I1II1 - I1iiiiI1iII
 import urlresolver
 if urlresolver . HostedMediaFile ( OOooO0o ) . valid_url ( ) :
  OOooO0o = urlresolver . HostedMediaFile ( OOooO0o ) . resolve ( )
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( OOooO0o )
  xbmc . Player ( ) . play ( OOooO0o , I1III1111iIi , False )
 else : I11 . ok ( oO0o0o0ooO0oO , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
 if 3 - 3: I1IiiI * O0OOooO + II111iiii - OoO0O00
def OOOO ( url ) :
 if 57 - 57: I1IiiI - o0oOOo0O0Ooo + OoO0O00 % Oo0Ooo
 if 26 - 26: I1iiiiI1iII . I1iiiiI1iII
 if 35 - 35: oO . OoOoOO00 * i11iIiiIii
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '\r' , '' )
 if 44 - 44: i11iIiiIii / Oo0Ooo
 I11i1I1I = re . compile ( '<td class="mlnh-thumb">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  Ii1IIi = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  IIi1ii1Ii = re . compile ( 'title="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 53 , IiII , iI111iI , '' )
 try :
  IiIiiiiI1 = re . compile ( 'class="next"><a href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  I11 . ok ( "22" , str ( IiIiiiiI1 ) )
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , IiIiiiiI1 , 63 , IiII , iI111iI , '' )
 except : pass
 if 43 - 43: oO % I1iiiiI1iII
def o0O0ooOOoO ( ) :
 if 19 - 19: i11iIiiIii
 OO00Oo = 'http://movieflixter.to/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<ul class="menu vertical">(.+?)</ul>' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<a href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 for OO00Oo , IIi1ii1Ii in Ooo0o00o0o :
  if not 'http' in OO00Oo :
   oO0OOoo0OO = 'http://movieflixter.to' + OO00Oo
   IiII = 'http://static.movieflixter.to/img/logo.png'
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , oO0OOoo0OO , 76 , IiII , Iii1ii1II11i , '' )
   if 54 - 54: II111iiii . OoOooOOOO
def oOO ( url ) :
 if 32 - 32: OoOoOO00 * I1IiiI % O0OOooO * OoOO . O0
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 48 - 48: I1iiiiI1iII * I1iiiiI1iII
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 13 - 13: OoOO / OoOooOOOO + OoOoOO00 . o0oOOo0O0Ooo % O0OOooO
 OOoOoO00O0O0o = url
 if 48 - 48: I1IiiI / i11iIiiIii - o0oOOo0O0Ooo * o00oo / OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="year">(.+?)</a>' ) . findall ( o0O0O00 )
 if 89 - 89: iIii1I11I1II1 / I1IiiI - II111iiii / OoOO . i11iIiiIii . OoOO
 for O0oOO0 in I11i1I1I :
  Ii1IIi = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in Ii1IIi :
   IIiii11i = 'http://movieflixter.to' + Ii1IIi
   IIi1ii1Ii = re . compile ( 'title="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = iii11 ( IIi1ii1Ii )
   try :
    IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if not 'http' in IiII :
     IiiiI1 = 'http:' + IiII
     III1i1iI1 . append ( IIi1ii1Ii )
     o0ooo00o . append ( IIiii11i )
     oOO00oO00O0OO . append ( IiiiI1 )
     o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
   except : pass
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 77 , IiII , iI111iI , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 77 , IiII , iI111iI , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 77 , IiII , iI111iI , '' )
     if 100 - 100: o00oo . OoOO % i1IIi . O0OOooO
 try :
  IiIiiiiI1 = re . compile ( "<li class='pagination-next'><a href='(.+?)'></a>" ) . findall ( o0O0O00 ) [ 0 ]
  if not 'http' in IiIiiiiI1 :
   OOo0Oo0OOo0 = 'http://movieflixter.to' + IiIiiiiI1
   if not 'search?' in url :
    iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , OOo0Oo0OOo0 , 76 , IiII , iI111iI , '' )
 except : pass
 if 19 - 19: OoOooOOOO + II111iiii
def OooooOoO ( url ) :
 if 38 - 38: iIii1 . OoOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 if 24 - 24: o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + I1IiiI - o00oo
 if 12 - 12: I1iiiiI1iII . iIii1 . OoOoOO00 / O0
 I11i1I1I = re . compile ( '<td nowrap>(.+?)&nbsp;' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  try :
   OO0oOOo0o = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in OO0oOOo0o :
    I1III11iiii11i1 = 'http://movieflixter.to' + OO0oOOo0o
    IIi1ii1Ii = re . compile ( '<b>(.+?)</b>' ) . findall ( O0oOO0 ) [ 0 ]
    oOoO0o00OO0 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , I1III11iiii11i1 , 666 , IiII , iI111iI , '' )
  except : pass
  if 54 - 54: i1IIi - o00oo
def IiIIII ( ) :
 if 89 - 89: OoO0O00 / I1IiiI
 OO00Oo = 'http://movieflixter.to/movies/best-rated-popular'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="year">(.+?)</a>' ) . findall ( o0O0O00 )
 if 16 - 16: Oo0Ooo + O0OOooO / Oo0Ooo / OoO0O00 % o00oo % I1ii11iIi11i
 for O0oOO0 in I11i1I1I :
  Ii1IIi = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in Ii1IIi :
   IIiii11i = 'http://movieflixter.to' + Ii1IIi
   IIi1ii1Ii = re . compile ( 'title="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = iii11 ( IIi1ii1Ii )
   try :
    IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if not 'http' in IiII :
     IiiiI1 = 'http:' + IiII
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 77 , IiiiI1 , Iii1ii1II11i , '' )
   except : pass
   if 22 - 22: II111iiii * OoO0O00 * OoOooOOOO + I1ii11iIi11i * o0oOOo0O0Ooo
def oo0o0 ( url ) :
 if 69 - 69: I1ii11iIi11i - oO
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 16 - 16: Oo0Ooo
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 14 - 14: i1IIi - O0 % Oo0Ooo
 OOoOoO00O0O0o = url
 if 92 - 92: OoOO % I1iiiiI1iII / I1ii11iIi11i % I1ii11iIi11i * I1IiiI
 try :
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I11i1I1I = re . compile ( 'class="posts posts-3 grid ">(.+?)class="navigation">' ) . findall ( o0O0O00 ) [ 0 ]
  OoO0O00O0oo0O = re . compile ( 'class="cover">(.+?)class="postcontent">' ) . findall ( I11i1I1I )
  for O0oOO0 in OoO0O00O0oo0O :
   IIiii11i = re . compile ( '<ahref="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = re . compile ( 'title="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = iii11 ( IIi1ii1Ii )
   IiII = re . compile ( 'imgsrc="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   Iii1ii1II11i = re . compile ( 'imgsrc="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   III1i1iI1 . append ( IIi1ii1Ii )
   o0ooo00o . append ( IIiii11i )
   oOO00oO00O0OO . append ( IiII )
   o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
 except : pass
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 80 , IiII , Iii1ii1II11i , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 80 , IiII , Iii1ii1II11i , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 80 , IiII , Iii1ii1II11i , '' )
     if 74 - 74: O0 . I1IiiI % OoO0O00 % iIii1
def oOo0OooOo ( url ) :
 try :
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I11i1I1I = re . compile ( '>Watch.+?</h1>(.+?)<htmlxmlns' ) . findall ( o0O0O00 ) [ 0 ]
  Ooo0o00o0o = re . compile ( '<ahref="(.+?)".+?<strong>(.+?)</strong>' ) . findall ( I11i1I1I )
  if 51 - 51: OoOooOOOO . Oo0Ooo
  for Ii1IIi , oO0o0OOOO in Ooo0o00o0o :
   oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , Ii1IIi , 666 , IiII , Iii1ii1II11i , '' )
 except : pass
def IiiIiiIi ( url ) :
 if 40 - 40: o0oOOo0O0Ooo
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 78 - 78: iIii1I11I1II1
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 56 - 56: OoooooooOO - OoOooOOOO - i1IIi
 OOoOoO00O0O0o = url
 if 8 - 8: oO / iI1 . I1IiiI + I1ii11iIi11i / i11iIiiIii
 try :
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  I11i1I1I = re . compile ( '<header class="post-header">(.+?)</figure' ) . findall ( o0O0O00 )
  if 31 - 31: O0OOooO - iIii1I11I1II1 + I1iiiiI1iII . Oo0Ooo / iIii1 % iIii1I11I1II1
  for O0oOO0 in I11i1I1I :
   Ii1IIi = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = re . compile ( 'title=".+?">(.+?)</a>' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = iii11 ( IIi1ii1Ii )
   IiII = re . compile ( 'data-src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   III1i1iI1 . append ( IIi1ii1Ii )
   o0ooo00o . append ( Ii1IIi )
   oOO00oO00O0OO . append ( IiII )
   o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
 except : pass
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 82 , IiII , Iii1ii1II11i , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 82 , IiII , Iii1ii1II11i , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 82 , IiII , Iii1ii1II11i , '' )
     if 6 - 6: iIii1 * i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + o0oOOo0O0Ooo / i1IIi
def o0o0oOO ( url ) :
 if 5 - 5: OoOO / o00oo
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<iframe id="trailer"(.+?)scrolling="no"' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  OOooO0o = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  oO0o0OOOO = 'Play Movie'
  oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OOooO0o , 666 , IiII , Iii1ii1II11i , '' )
  if 6 - 6: Oo0Ooo . iIii1 / iIii1 - i11iIiiIii
def OO0o ( url ) :
 if 32 - 32: OoooooooOO - OoOoOO00 - i11iIiiIii * o0oOOo0O0Ooo / Oo0Ooo + OoooooooOO
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 35 - 35: i1IIi - o0oOOo0O0Ooo * I1iiiiI1iII
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 63 - 63: I1iiiiI1iII * I1ii11iIi11i . OoooooooOO / iI1 * Oo0Ooo . O0OOooO
 OOoOoO00O0O0o = url
 if 62 - 62: i1IIi / O0OOooO . I1IiiI * o0oOOo0O0Ooo
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( 'class="visual-thumbnail">(.+?)</article>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  Ii1IIi = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  IiII = re . compile ( 'img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  IIi1ii1Ii = re . compile ( 'alt="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  III1i1iI1 . append ( IIi1ii1Ii )
  o0ooo00o . append ( Ii1IIi )
  oOO00oO00O0OO . append ( IiII )
  o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  if 21 - 21: o0oOOo0O0Ooo
 for IIi1ii1Ii , Ii1IIi , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 84 , IiII , Iii1ii1II11i , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 84 , IiII , Iii1ii1II11i , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , Ii1IIi , 84 , IiII , Iii1ii1II11i , '' )
     if 81 - 81: OoOooOOOO / iIii1I11I1II1 - O0OOooO * oO . I1IiiI * I1ii11iIi11i
def o0000 ( url ) :
 if 42 - 42: oO + oO * II111iiii
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<tbody>(.+?)</tbody>' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<tr>(.+?)</tr>' ) . findall ( I11i1I1I )
 for O0oOO0 in Ooo0o00o0o :
  IIi1ii1Ii = re . compile ( '<td style="text-align:center">(.+?)</td>' ) . findall ( O0oOO0 ) [ 0 ]
  OOOooo = re . compile ( '<td style="text-align:center">(.+?)</td>' ) . findall ( O0oOO0 ) [ 1 ]
  OOooO0o = re . compile ( 'href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  oOoO0o00OO0 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" + " - " + "[COLOR yellow]" + OOOooo + "[/COLOR]" , OOooO0o , 666 , IiII , Iii1ii1II11i , '' )
  if 78 - 78: OoooooooOO
def OOoo0 ( url ) :
 if 36 - 36: o0oOOo0O0Ooo + OoOooOOOO - iIii1 + iIii1I11I1II1 + OoooooooOO
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 4 - 4: II111iiii . OoOooOOOO + OoOO * oO . O0OOooO
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 87 - 87: OoOoOO00 / OoO0O00 / i11iIiiIii
 OOoOoO00O0O0o = url
 if 74 - 74: o00oo / I1ii11iIi11i % o0oOOo0O0Ooo
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<header class="entry-header"(.+?)<!-- .entry-header -->' ) . findall ( o0O0O00 )
 if 88 - 88: OoOoOO00 - i11iIiiIii % o0oOOo0O0Ooo * OoOooOOOO + I1ii11iIi11i
 for O0oOO0 in I11i1I1I :
  try :
   IiII = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   Ii1IIi = re . compile ( 'data-url="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   oO0o0OOOO = re . compile ( 'rel="bookmark">(.+?)</a>' ) . findall ( O0oOO0 ) [ 0 ] . replace ( 'Watch Online' , '' ) . replace ( 'watch online' , '' )
   if 52 - 52: II111iiii . I1IiiI + OoOoOO00 % OoO0O00
   III1i1iI1 . append ( oO0o0OOOO )
   o0ooo00o . append ( Ii1IIi )
   oOO00oO00O0OO . append ( IiII )
   o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  except : pass
  if 62 - 62: o0oOOo0O0Ooo
 for oO0o0OOOO , Ii1IIi , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , Ii1IIi , 86 , IiII , iI111iI , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in oO0o0OOOO . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , Ii1IIi , 86 , IiII , Iii1ii1II11i , '' )
   else :
    if OOo00 . lower ( ) in oO0o0OOOO . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , Ii1IIi , 86 , IiII , Iii1ii1II11i , '' )
     if 15 - 15: OoOooOOOO + OoOO . iI1 * OoO0O00 . OoOoOO00
     if 18 - 18: i1IIi % II111iiii + oO % OoOO
def oOOoO0OO00OOo0 ( url ) :
 if 18 - 18: I1IiiI + OoO0O00 % iIii1I11I1II1 - i1IIi . o00oo
 I11I = [ ]
 IIi11i1i1iI1 = 0
 if 26 - 26: o0oOOo0O0Ooo * iIii1 . i1IIi
 if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
 if 62 - 62: i11iIiiIii % iI1 . iIii1 . iI1
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div id="primary"(.+?)<div class="gk-social-buttons">' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  Iii1ii1II11i = re . compile ( 'data-url="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if 84 - 84: i11iIiiIii * OoO0O00
 Ooo0o00o0o = re . compile ( '<div class="tabcontent">(.+?)</div>' ) . findall ( o0O0O00 )
 for IIiii11i in Ooo0o00o0o :
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  oO0o0OOOO = 'Link: ' + str ( IIi11i1i1iI1 )
  I1I1iII1i = re . compile ( 'src="(.+?)"' ) . findall ( IIiii11i ) [ 0 ]
  iiIIii = I1I1iII1i + '!split!' + oO0o0OOOO
  I11I . append ( iiIIii )
 try :
  OoO0O00O0oo0O = re . compile ( '<strong>-Version 2-</strong>(.+?)</div>' ) . findall ( o0O0O00 ) [ 0 ]
  oO0Oo0O0 = re . compile ( '<a href="(.+?)"' ) . findall ( OoO0O00O0oo0O )
  for I1iIiI1IiIIII in oO0Oo0O0 :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   oO0o0OOOO = 'Link: ' + str ( IIi11i1i1iI1 )
   iiIIii = I1iIiI1IiIIII + '!split!' + oO0o0OOOO
   I11I . append ( iiIIii )
 except : pass
 if 18 - 18: O0OOooO % i11iIiiIii . iIii1I11I1II1 - I1iiiiI1iII
 for O0Oo00OoOo in I11I :
  url , oO0o0OOOO = O0Oo00OoOo . split ( '!split!' )
  if 80 - 80: I1IiiI + o00oo - i1IIi . OoOO / o0oOOo0O0Ooo / I1IiiI
  oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 2 , IiII , Iii1ii1II11i , '' )
  if 1 - 1: OoOooOOOO + i11iIiiIii - I1IiiI / iI1 + oO
  if 80 - 80: o00oo + o0oOOo0O0Ooo * OoOO + OoO0O00
  if 75 - 75: OoOooOOOO / o0oOOo0O0Ooo / iI1 / iIii1 % O0OOooO + II111iiii
  if 4 - 4: I1iiiiI1iII - Oo0Ooo - iIii1 - OoOooOOOO % i11iIiiIii / OoO0O00
  if 50 - 50: O0OOooO + i1IIi
  if 31 - 31: OoOO
  if 78 - 78: i11iIiiIii + o0oOOo0O0Ooo + oO / o0oOOo0O0Ooo % iIii1I11I1II1 % iIii1
  if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % oO . I1ii11iIi11i % O0
  if 47 - 47: o0oOOo0O0Ooo
def oo0ooooO ( url ) :
 if 12 - 12: II111iiii
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<a class="site_tag(.+?)/a>' ) . findall ( o0O0O00 )
 if 2 - 2: i1IIi - I1IiiI + OoOooOOOO . II111iiii
 for o0O0O00 in I11i1I1I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
  oO0o0OOOO = re . compile ( '/i>(.+?)<' ) . findall ( o0O0O00 ) [ 0 ]
  oO0OOoo0OO = "http://xoxfuck.com" + url
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , oO0OOoo0OO , 17 , IiII , Iii1ii1II11i , '' )
  if 25 - 25: o00oo
def iI1iiII11I ( ) :
 if 32 - 32: iI1 % O0OOooO - OoOoOO00 % I1iiiiI1iII . oO
 OO00Oo = 'http://www.pornhd.com/category'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '&amp;' , 'and' )
 I11i1I1I = re . compile ( '<ul class="tag-150-list">(.+?)<div class="footer-zone">' , re . DOTALL ) . findall ( o0O0O00 )
 OoO0O00O0oo0O = re . compile ( '<li class="category">(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 47 - 47: OoOooOOOO % i1IIi + i1IIi
 for O0oOO0 in OoO0O00O0oo0O :
  ooo0o00 = re . compile ( 'data-original="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  oO0o0OOOO = re . compile ( 'alt="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  oOoO = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  if not 'http' in oOoO :
   IIiii11i = 'http://www.pornhd.com' + oOoO
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , IIiii11i , 42 , ooo0o00 , Iii1ii1II11i , '' )
   if 87 - 87: Oo0Ooo * iI1 % iIii1 % OoOoOO00
def iIi1Ii ( url ) :
 if 11 - 11: I1IiiI % OoOO - OoO0O00 - o00oo + o0oOOo0O0Ooo
 o0O0O0 = url
 i1i1II = 0
 try :
  o0O , url = url . split ( '|' )
  if 55 - 55: O0 - oO
 except : i1i1II = 1
 iI1i11Iiii = o000o ( url )
 if 58 - 58: OoOoOO00 - I1iiiiI1iII - OoooooooOO
 I11i1I1I = re . compile ( '<section id="pageContent"(.+?)<div class="pager paging">' , re . DOTALL ) . findall ( iI1i11Iiii )
 OoO0O00O0oo0O = re . compile ( '<a class="thumb"(.+?)<span class="add-to">' , re . DOTALL ) . findall ( iI1i11Iiii )
 if 96 - 96: iIii1I11I1II1
 if 82 - 82: OoOoOO00 + O0 - iIii1 % o00oo * i11iIiiIii
 if 15 - 15: o0oOOo0O0Ooo
 if 39 - 39: iI1 / I1ii11iIi11i / I1IiiI * oO
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   IIi1ii1Ii = re . compile ( '<img alt="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if 44 - 44: O0 + O0OOooO . iIii1I11I1II1 + Oo0Ooo / O0 - OoOooOOOO
   if 83 - 83: iIii1 * OoOooOOOO / Oo0Ooo
   iIIIiI = re . compile ( '<time>(.+?)</time>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if 93 - 93: O0OOooO . iIii1I11I1II1 % i11iIiiIii . OoOoOO00 % O0OOooO + O0
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   if 65 - 65: OoOO + OoO0O00 - OoooooooOO
   if not "http" in O0O0OoOO0 :
    O0O0OoOO0 = re . compile ( 'data-original="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
    if 51 - 51: Oo0Ooo + o00oo / I1iiiiI1iII - i1IIi
    if 51 - 51: Oo0Ooo - I1ii11iIi11i * OoOooOOOO
   o0O0O00 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in o0O0O00 :
    IIiii11i = 'http://www.pornhd.com' + o0O0O00
    iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" "[COLOR red]" " :: Video Length :: " + iIIIiI + "[/COLOR]" , IIiii11i , 43 , O0O0OoOO0 , Iii1ii1II11i , '' )
  except : pass
  if 12 - 12: iIii1I11I1II1 % O0OOooO % O0OOooO
  if 78 - 78: iIii1 . OoOoOO00 . OoOooOOOO
 if i1i1II == 1 :
  try :
   o0ooO0OOO = ""
   if not "=" in o0O0O0 :
    o0O0O0 = o0O0O0 + "?page=1"
    o0O , O00oO = o0O0O0 . split ( "=" )
    O0ooooo0OOOO0 = int ( O00oO ) + 1
    o0ooO0OOO = o0O + "=" + str ( O0ooooo0OOOO0 )
    if 74 - 74: OoOO * i11iIiiIii / oO
    iiiI1I11i1 ( '[COLOR red]Next Page >>[/COLOR]' , o0ooO0OOO , 42 , IiII , Iii1ii1II11i )
    if 75 - 75: O0 - OoooooooOO + O0OOooO . o00oo % II111iiii
  except : pass
  if 9 - 9: II111iiii * II111iiii . i11iIiiIii * iIii1I11I1II1
def II1 ( url , icon , fanart ) :
 if 27 - 27: OoOO + I1IiiI * iIii1I11I1II1 . OoooooooOO * OoOoOO00
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( 'sources.+?{(.+?)}' , re . DOTALL ) . findall ( o0O0O00 )
 o0O = str ( I11i1I1I )
 I11i1I1I = o0O . replace ( '\\' , '' )
 OOOo = re . compile ( "720.+?'.+?'(.+?)'," ) . findall ( I11i1I1I ) [ 0 ]
 I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
 if 74 - 74: OoOO - OoooooooOO . Oo0Ooo
 xbmc . Player ( ) . play ( OOOo , I1III1111iIi , False )
 if 31 - 31: o0oOOo0O0Ooo % OoOooOOOO + iIii1I11I1II1 + i11iIiiIii * oO
 quit ( 0 )
 if 45 - 45: iI1 * oO . O0OOooO - oO + iIii1
def iII ( name , url , iconimage ) :
 if 78 - 78: I1ii11iIi11i % I1IiiI / OoooooooOO % iI1 - I1iiiiI1iII
 iIi = name . split ( '(' ) [ 1 ]
 iIi = iIi . replace ( ')' , '' ) . replace ( "[/COLOR]" , '' )
 iIi = int ( iIi )
 ii = url
 if 94 - 94: O0OOooO * OoOooOOOO - iIii1 . iIii1I11I1II1
 O000oO0O = 0
 o00ooo0 = 1
 IIi11i1i1iI1 = 0
 i1i1IiIi1 = 6
 if 22 - 22: OoOooOOOO * O0 . II111iiii - OoO0O00
 Oo0o0000o0o0 . create ( "STREAM ARMY" , "[COLOR lime]Getting video 1 of " + str ( iIi ) + "![/COLOR]" )
 Oo0o0000o0o0 . update ( 0 )
 while o00ooo0 < 2000 :
  if 90 - 90: o00oo
  if IIi11i1i1iI1 == 0 :
   o0O0O00 = o000o ( ii )
   if 94 - 94: OoOooOOOO / I1ii11iIi11i * oO - OoOoOO00
   I11i1I1I = re . compile ( '<div class="inner_block video_box">(.+?)</a>' ) . findall ( o0O0O00 )
   for i1iI1 in I11i1I1I :
    oO0OOoo0OO = re . compile ( 'href="(.+?)">' ) . findall ( i1iI1 ) [ 0 ]
    name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( i1iI1 ) [ 0 ]
    iconimage = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    O000oO0O = O000oO0O + 1
    I1Ii11II1I1 = 100 * int ( O000oO0O ) / int ( iIi )
    Oo0o0000o0o0 . update ( I1Ii11II1I1 , "[COLOR lime]Getting video " + str ( O000oO0O ) + " of " + str ( iIi ) + "![/COLOR]" )
    oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , oO0OOoo0OO , 18 , iconimage , Iii1ii1II11i , '' )
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  else :
   url = ii + '?load_more=10&loaded=' + str ( i1i1IiIi1 )
   o0O0O00 = o000o ( url )
   o0O0O00 = o0O0O00 . replace ( '\\' , '' )
   if 41 - 41: O0 * O0OOooO - OoOoOO00 . OoOO
   if "no_more_videos" in o0O0O00 :
    o00ooo0 = 2001
    if 65 - 65: Oo0Ooo . OoooooooOO
   I11i1I1I = re . compile ( '<div class="(.+?)</a>' ) . findall ( o0O0O00 )
   for i1iI1 in I11i1I1I :
    if o00ooo0 < 2000 :
     oO0OOoo0OO = re . compile ( 'href="(.+?)">' ) . findall ( i1iI1 ) [ 0 ]
     name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( i1iI1 ) [ 0 ]
     iconimage = re . compile ( 'src="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
     O000oO0O = O000oO0O + 1
     I1Ii11II1I1 = 100 * int ( O000oO0O ) / int ( iIi )
     Oo0o0000o0o0 . update ( I1Ii11II1I1 , "[COLOR lime]Getting video " + str ( O000oO0O ) + " of " + str ( iIi ) + "![/COLOR]" )
     oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , oO0OOoo0OO , 18 , iconimage , Iii1ii1II11i , '' )
   i1i1IiIi1 = i1i1IiIi1 + 10
  o00ooo0 = o00ooo0 + 1
 Oo0o0000o0o0 . close
 if 70 - 70: Oo0Ooo - o00oo . iIii1I11I1II1 % OoOooOOOO / OoOoOO00 - O0
def o0O0oo0o ( ) :
 if 12 - 12: OoOoOO00 % iIii1 % I1ii11iIi11i . i11iIiiIii * iIii1I11I1II1
 OO00Oo = 'https://www.porn.com/categories'
 if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="wrap grid categories">(.+?)<div class="listFilters listFiltersWide"' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<a class="thumbs" href="(.+?)" title="(.+?)"><img src="(.+?)"' ) . findall ( I11i1I1I )
 for Ii1IIi , IIi1ii1Ii , iIiI1iI1i1I in Ooo0o00o0o :
  if not 'http' in Ii1IIi :
   IIiii11i = 'https://www.porn.com' + Ii1IIi
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 66 , iIiI1iI1i1I , Iii1ii1II11i , '' )
   if 82 - 82: I1IiiI % I1ii11iIi11i * I1iiiiI1iII . OoOO % I1IiiI - iIii1I11I1II1
def iII1ii1I1i ( url ) :
 if 49 - 49: OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<ul class="listThumbs">(.+?)<div class="pager">' ) . findall ( o0O0O00 ) [ 0 ]
 OoO0O00O0oo0O = re . compile ( '<img(.+?)<span class="added"' ) . findall ( I11i1I1I )
 for O0oOO0 in OoO0O00O0oo0O :
  try :
   II111iIII1Ii = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   iIiI1iI1i1I = re . compile ( 'src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   IIi1ii1Ii = re . compile ( 'class="title">(.+?)<' ) . findall ( O0oOO0 ) [ 0 ]
   if not 'http' in II111iIII1Ii :
    iI1IiiiIiI1Ii = 'https://www.porn.com' + II111iIII1Ii
    iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , iI1IiiiIiI1Ii , 67 , iIiI1iI1i1I , Iii1ii1II11i , '' )
  except : pass
  if 78 - 78: OoooooooOO / iI1 % OoOoOO00 * OoooooooOO
 try :
  IiIiiiiI1 = re . compile ( '<link rel="next" href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  if not 'http' in IiIiiiiI1 :
   ooOO00o00 = 'https://www.porn.com' + IiIiiiiI1
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , ooOO00o00 , 66 , IiII , Iii1ii1II11i , '' )
 except : pass
 if 18 - 18: iIii1I11I1II1 + OoOooOOOO * I1IiiI - iI1 / I1IiiI
def o00iI1i1II ( url ) :
 if 14 - 14: O0OOooO - iIii1I11I1II1 / O0 % iIii1 . OoOoOO00
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="dlRow">(.+?)<div class="bn">' ) . findall ( o0O0O00 ) [ 0 ]
 iI1IIi11i1I1 = re . compile ( '<a href="(.+?)".+?</i>(.+?)<' ) . findall ( I11i1I1I )
 for O00oo , OOOooo in iI1IIi11i1I1 :
  if not 'http' in O00oo :
   oO0OOoo0OO = 'https://www.porn.com' + O00oo
   if 'mp4' in oO0OOoo0OO :
    oO0 ( OOOooo , oO0OOoo0OO , 4 , O0O0OoOO0 , Iii1ii1II11i , '' )
    if 58 - 58: iIii1I11I1II1 - i11iIiiIii - i11iIiiIii * OoOO + o0oOOo0O0Ooo . OoOoOO00
def OoOo00o ( name , url , iconimage ) :
 if 30 - 30: OoOoOO00 . OoOooOOOO / OoOooOOOO * i11iIiiIii
 IIiii11i = o000o ( url )
 O0oOO0 = re . compile ( '<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">' ) . findall ( IIiii11i ) [ 0 ]
 IIi1ii1Ii = re . compile ( '<title>(.+?)</title>' ) . findall ( IIiii11i ) [ 0 ]
 IIi1ii1Ii = IIi1ii1Ii . split ( ' | ' ) [ 0 ]
 IIi1ii1Ii = IIi1ii1Ii . strip ( ' ' )
 I1III1111iIi = xbmcgui . ListItem ( IIi1ii1Ii , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( O0oOO0 , I1III1111iIi , False )
 if 46 - 46: OoO0O00 * Oo0Ooo % o00oo + O0 * iIii1
 if 34 - 34: OoO0O00
 if 27 - 27: OoOO - O0 % OoOooOOOO * oO . iIii1 % iIii1I11I1II1
 if 37 - 37: OoooooooOO + O0 - i1IIi % O0OOooO
 if 24 - 24: OoOoOO00
 if 94 - 94: i1IIi * i1IIi % II111iiii + iI1
 if 28 - 28: I1IiiI
def I11o0000o0Oo ( ) :
 OO00Oo = 'http://watchseries.cr/letters/A'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<a href="(.+?)".+?wpb_btn-small">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 O0O0OoOO0 = 'http://watchseries.cr/assets/wp-content/themes/Snaptube/images/new-logo.png'
 for o0O0O00 , IIi1ii1Ii in I11i1I1I :
  if 'http' in o0O0O00 :
   iiiI1I11i1 ( IIi1ii1Ii , o0O0O00 , 31 , O0O0OoOO0 , Iii1ii1II11i , '' )
   if 90 - 90: iIii1I11I1II1 * II111iiii
def oOOo0OoOOOoo ( url ) :
 if 88 - 88: o00oo * OoO0O00
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<td><a style="font-size: 15px;" href="(.+?)">(.+?)</a></td>' , re . DOTALL ) . findall ( o0O0O00 )
 for o0O0O00 , oO0o0OOOO in I11i1I1I :
  iiiI1I11i1 ( oO0o0OOOO , o0O0O00 , 57 , O0O0OoOO0 , Iii1ii1II11i , '' )
  if 35 - 35: I1ii11iIi11i / I1iiiiI1iII % I1IiiI + iIii1I11I1II1
def oO00o ( url ) :
 if 36 - 36: oO . II111iiii % O0OOooO
 o0O0O00 = o000o ( url )
 ooo0o00 = re . compile ( '<img src="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 5 ]
 I11i1I1I = re . compile ( '<h2 class="video-module-title">(.+?)<a href="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
 for OoooooooO , o0O0O00 in I11i1I1I :
  iiiI1I11i1 ( OoooooooO , o0O0O00 , 58 , ooo0o00 , Iii1ii1II11i , '' )
  if 4 - 4: Oo0Ooo + o0oOOo0O0Ooo
def iIIiIii11i1Ii ( url ) :
 if 95 - 95: iIii1I11I1II1 - oO - iI1 + oO % I1ii11iIi11i . I1IiiI
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="vid_info">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  IIi1ii1Ii = re . compile ( '</b>(.+?)</a>' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  iiiI1I11i1 ( IIi1ii1Ii , url , 59 , O0O0OoOO0 , iI111iI , '' )
  if 41 - 41: O0 + o00oo . i1IIi - II111iiii * o0oOOo0O0Ooo . OoO0O00
def oooO00Oo ( url ) :
 if 86 - 86: II111iiii + O0OOooO + iIii1
 o0O0O00 = o000o ( url )
 if 9 - 9: O0OOooO + II111iiii % O0OOooO % iIii1 + iIii1I11I1II1
 I11i1I1I = re . compile ( '<td class="view_link">(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  OOooO0o = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
  if 'watchseries' in OOooO0o :
   IIiii11i = o000o ( OOooO0o )
   OoO0O00O0oo0O = re . compile ( '<h1>(.+?)</a>' , re . DOTALL ) . findall ( IIiii11i )
   if 59 - 59: i1IIi
   for O0oOO0 in OoO0O00O0oo0O :
    OO0oOOo0o = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0oOO0 ) [ 0 ]
    if 'daclips.in' in OO0oOOo0o :
     oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO0oOOo0o , 2 , O0O0OoOO0 , iI111iI , '' )
    elif 'vidzi.tv' in OO0oOOo0o :
     oOoO0o00OO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO0oOOo0o , 2 , O0O0OoOO0 , iI111iI , '' )
     if 48 - 48: O0 * OoOO * OoO0O00 . OoO0O00 * OoOooOOOO - OoOO
def iIi11i ( ) :
 if 56 - 56: i11iIiiIii . O0OOooO / I1iiiiI1iII
 OO00Oo = 'http://sockshare.net/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div id="mainmenu2">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOoO = re . compile ( '<a href="(.+?)"><img src="(.+?)">' , re . DOTALL ) . findall ( I11i1I1I )
 for Ii1IIi , iIiI1iI1i1I in oOoO :
  III1iii1i1II = 0
  if not 'http' in oOoO :
   oo0oOo = [ 'genres' , 'countries' , 'years' , 'tv-series' , 'new-movies' , 'anime-series' ]
   for O0oOO0o in oo0oOo :
    if O0oOO0o in Ii1IIi :
     III1iii1i1II = 1
   if III1iii1i1II == 0 :
    IIiii11i = 'http://sockshare.net' + Ii1IIi
    iiiiI1IiI1I1 = 'http://sockshare.net' + iIiI1iI1i1I
    if not IIiii11i . endswith ( '/' ) :
     IIi1ii1Ii = IIiii11i . replace ( 'http://sockshare.net/' , '' ) . replace ( 'search-movies/2016' , 'New Releases' ) . replace ( 'new-movies' , 'Recently Added' ) . replace ( '.html' , '' ) . replace ( '-' , ' ' )
     IIi1ii1Ii = IIi1ii1Ii . title ( )
     III1iii1i1II = 1
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 61 , iiiiI1IiI1I1 , iI111iI , '' )
     if 19 - 19: OoOO
def O0o00oO0oOO ( url ) :
 if 49 - 49: iIii1I11I1II1 * i1IIi . OoooooooOO
 iIiIIii = 0
 try :
  url , OOo00 = url . split ( "|SPLIT|" )
  iIiIIii = 1
 except : pass
 if 90 - 90: o0oOOo0O0Ooo % I1ii11iIi11i - iIii1I11I1II1 % OoOoOO00
 III1i1iI1 = [ ]
 o0ooo00o = [ ]
 oOO00oO00O0OO = [ ]
 oOo00OO = [ ]
 o0oOO0OO = [ ]
 if 8 - 8: OoOoOO00 * Oo0Ooo / iIii1 % OoOO - I1IiiI
 OOoOoO00O0O0o = url
 if 71 - 71: I1iiiiI1iII
 oo0oOo = any ( i . isdigit ( ) for i in OOoOoO00O0O0o )
 if 23 - 23: i1IIi . iIii1I11I1II1 . iI1 . O0 % OoOO % i11iIiiIii
 if 'http://sockshare.net/search-movies/2016.html' in url :
  Iiiii111 = url . replace ( '.html' , '' )
  o0ooO0OOO = Iiiii111 + '/page-2.html'
  if 93 - 93: OoooooooOO * Oo0Ooo
 elif oo0oOo == False :
  url = url . replace ( ".html" , "" )
  url = url + "/page-1.html"
  OOoOoO00O0O0o = url
  I1IiI1iIiIiii = int ( filter ( str . isdigit , OOoOoO00O0O0o ) )
  IiIiiiiI1 = int ( I1IiI1iIiIiii ) + 1
  if len ( str ( I1IiI1iIiIiii ) ) == 1 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 6 ]
  elif len ( str ( I1IiI1iIiIiii ) ) == 2 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 7 ]
  elif len ( str ( I1IiI1iIiIiii ) ) == 3 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 8 ]
  o0ooO0OOO = OOoOoO00O0O0o + str ( IiIiiiiI1 ) + ".html"
 else :
  I1IiI1iIiIiii = int ( filter ( str . isdigit , OOoOoO00O0O0o ) )
  IiIiiiiI1 = int ( I1IiI1iIiIiii ) + 1
  if len ( str ( I1IiI1iIiIiii ) ) == 1 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 6 ]
  elif len ( str ( I1IiI1iIiIiii ) ) == 2 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 7 ]
  elif len ( str ( I1IiI1iIiIiii ) ) == 3 :
   OOoOoO00O0O0o = OOoOoO00O0O0o [ : - 8 ]
  o0ooO0OOO = OOoOoO00O0O0o + str ( IiIiiiiI1 ) + ".html"
  if 29 - 29: O0OOooO - i1IIi . OoOooOOOO - I1ii11iIi11i + O0OOooO + OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<li class="item">(.+?)/div>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  IIi1ii1Ii = re . compile ( '<b>(.+?)</b>' ) . findall ( O0oOO0 ) [ 0 ]
  IIiii11i = re . compile ( 'href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  III1i1iI1 . append ( IIi1ii1Ii )
  o0ooo00o . append ( IIiii11i )
  oOO00oO00O0OO . append ( IiII )
  o0oOO0OO = list ( zip ( III1i1iI1 , o0ooo00o , oOO00oO00O0OO ) )
  if 36 - 36: i1IIi / O0OOooO . iIii1I11I1II1
 for IIi1ii1Ii , IIiii11i , IiII in o0oOO0OO :
  if iIiIIii == 0 :
   iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 64 , IiII , iI111iI , '' )
  else :
   if ' ' in OOo00 :
    I11Ii11iI1 = 0
    IiIiiI11111I1 = OOo00 . split ( " " )
    for oo0oOo in IiIiiI11111I1 :
     if not oo0oOo . lower ( ) in IIi1ii1Ii . lower ( ) :
      I11Ii11iI1 = 1
    if I11Ii11iI1 == 0 :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 64 , IiII , iI111iI , '' )
   else :
    if OOo00 . lower ( ) in IIi1ii1Ii . lower ( ) :
     iiiI1I11i1 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , IIiii11i , 64 , IiII , iI111iI , '' )
     if 12 - 12: OoOO
 try :
  if not 'search-movies' in url :
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , o0ooO0OOO , 61 , IiII , iI111iI , '' )
 except : pass
 if 71 - 71: I1IiiI . II111iiii . I1IiiI - O0OOooO
def I1ii1 ( url ) :
 if 48 - 48: O0OOooO / iIii1I11I1II1 + iI1 + iIii1I11I1II1 . OoO0O00
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<p class="server_play">(.+?)</p>' ) . findall ( o0O0O00 )
 for O0oOO0 in I11i1I1I :
  OOooO0o = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if 'openload' in OOooO0o :
   oO0OOoo0OO = o000o ( OOooO0o )
  elif 'vidto' in OOooO0o :
   oO0OOoo0OO = o000o ( OOooO0o )
  elif 'veoh' in OOooO0o :
   oO0OOoo0OO = o000o ( OOooO0o )
  elif 'moviepod' in OOooO0o :
   oO0OOoo0OO = o000o ( OOooO0o )
  try :
   o0o0OO0o00o0O = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( oO0OOoo0OO ) [ 0 ]
   IIIIIIi1i = base64 . decodestring ( o0o0OO0o00o0O )
   OO0oOOo0o = re . compile ( 'src="(.+?)"' ) . findall ( IIIIIIi1i ) [ 0 ]
   IIi1ii1Ii = OO0oOOo0o . replace ( 'https://' , '' ) . replace ( 'http://' , '' ) . replace ( '/' , '' ) . split ( '.' ) [ 0 ]
   IIi1ii1Ii = IIi1ii1Ii . title ( )
   if 'http' in OO0oOOo0o :
    oOoO0o00OO0 ( "[COLOR lime]" + IIi1ii1Ii + "[/COLOR]" , OO0oOOo0o , 2 , O0O0OoOO0 , iI111iI , '' )
    if 26 - 26: iIii1I11I1II1 - O0 . O0
  except : pass
  if 68 - 68: iI1 + o00oo . O0 . OoOO % i1IIi % iI1
def i1I1iI ( url ) :
 if 92 - 92: Oo0Ooo / i11iIiiIii + I1ii11iIi11i
 try :
  if not "http" in url :
   if "https://" in url :
    url = url . replace ( "https://" , "http://" )
   o0O0O00 = o000o ( url )
   oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0O0O00 ) [ 0 ] . split ( ' (' ) [ 0 ]
   oOo0Oo0O0O = re . compile ( '<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">' ) . findall ( o0O0O00 )
   O0O0OoOO0 = re . compile ( '<meta property="og:image" content="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   if 48 - 48: Oo0Ooo - O0OOooO + Oo0Ooo - I1IiiI * i11iIiiIii . I1iiiiI1iII
   for url , IIi1ii1Ii in oOo0Oo0O0O :
    oO0 ( IIi1ii1Ii , url , 14 , O0O0OoOO0 , iI111iI , '' )
  else :
   o0O0O00 = o000o ( url )
   if 35 - 35: iIii1 . O0 + Oo0Ooo + iI1 + i1IIi
   I11i1I1I = re . compile ( '<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>' ) . findall ( o0O0O00 ) [ 0 ]
   ii11i11i1 = str ( I11i1I1I )
   OoO0O00O0oo0O = re . compile ( '<td width="100%" class="entry">(.+?)</td>' ) . findall ( ii11i11i1 )
   OooOooO0O0o0 = re . compile ( '<meta property="og:image" content="(.+?)"/>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   for i1iI1 in OoO0O00O0oo0O :
    oO0o0OOOO = re . compile ( 'title="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    url = re . compile ( '<a href="(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
    IIi1ii1Ii = oO0o0OOOO . split ( ' - ' ) [ 1 ]
    if not 'http' in url : url = 'http:' + url
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , url , 14 , OooOooO0O0o0 , iI111iI , '' )
 except :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
  if 59 - 59: Oo0Ooo + I1iiiiI1iII - iI1 . o0oOOo0O0Ooo + I1IiiI % o00oo
  if 37 - 37: I1iiiiI1iII + I1iiiiI1iII % o0oOOo0O0Ooo
  if 29 - 29: O0OOooO
  if 41 - 41: O0 % I1iiiiI1iII
  if 10 - 10: I1iiiiI1iII . i1IIi + OoOO
  if 66 - 66: OoO0O00 % o0oOOo0O0Ooo
  if 21 - 21: OoOoOO00 - OoooooooOO % i11iIiiIii
def Oo00O0OO ( ) :
 if 77 - 77: o00oo - Oo0Ooo - iIii1I11I1II1
 OO00Oo = 'https://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
 if 16 - 16: OoO0O00 / I1iiiiI1iII / i1IIi . I1iiiiI1iII + o00oo
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"start(.+?)}' ) . findall ( o0O0O00 )
 for i1iI1 in I11i1I1I :
  if not 'event_status":""' in str ( i1iI1 ) :
   Iiii1I = 1
  else : Iiii1I = 0
  ooooo0Oo0 = re . compile ( 'date":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  o0I1IIIi11ii11 = re . compile ( 'competition_name":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  O0o0oo0oOO0oO = re . compile ( 'competition_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  iIiIII1iI1111 = re . compile ( 'home_team":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  Ii1I1I111iI = re . compile ( 'home_team_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  I1i11I = re . compile ( 'home_team_slug":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  try :
   ooo0oo00O00Oo = re . compile ( 'event_status":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  except : ooo0oo00O00Oo = "null"
  OOO000000OOO0 = re . compile ( 'away_team":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  ooOoOOoooO000 = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  OoO0o000oOo = re . compile ( 'away_team_slug":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  Oo00OO00o0oO = re . compile ( 'event_id":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  try :
   iI1I1I1i1i = re . compile ( 'game_minute":"(.+?)"' ) . findall ( i1iI1 ) [ 0 ]
  except : iI1I1I1i1i = "null"
  OOo0O = Ii1I1I111iI . split ( "-" )
  oOOoooO0O0 = ooOoOOoooO000 . split ( "-" )
  iIiIII1iI1111 = ""
  IIi11i1i1iI1 = 0
  for o0O in OOo0O :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   iIIIiI = len ( OOo0O )
   if IIi11i1i1iI1 < iIIIiI :
    iIiIII1iI1111 = iIiIII1iI1111 + " " + o0O
  OOO000000OOO0 = ""
  IIi11i1i1iI1 = 0
  for o0O in oOOoooO0O0 :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   iIIIiI = len ( oOOoooO0O0 )
   if IIi11i1i1iI1 < iIIIiI :
    OOO000000OOO0 = OOO000000OOO0 + " " + o0O
    if 46 - 46: iIii1I11I1II1
  ooooo0Oo0 = ooooo0Oo0 + "!"
  ooooo0Oo0 , I111iiiii1 = ooooo0Oo0 . split ( ' ' )
  I111iiiii1 = I111iiiii1 . replace ( ":00!" , "" )
  o0O , O00oO , O0ooooo0OOOO0 = ooooo0Oo0 . split ( "-" )
  ooooo0Oo0 = O0ooooo0OOOO0 + "-" + O00oO + "-" + o0O
  I111iiiii1 = "[COLOR red][B]" + I111iiiii1 + "[/B][/COLOR]"
  ooooo0Oo0 = "[COLOR red][B]" + ooooo0Oo0 + "[/B][/COLOR]"
  OO00Oo = 'https://soccerstreams.net/streams/' + Oo00OO00o0oO + '/' + I1i11I + '_vs_' + OoO0o000oOo
  oO0o0OOOO = '[COLOR lime][B]' + iIiIII1iI1111 . title ( ) + ' vs ' + OOO000000OOO0 . title ( ) + '[/B][/COLOR]'
  OO00Oo = OO00Oo + "|SPLIT|" + oO0o0OOOO
  O0O0OoOO0 = 'https://soccerstreams.net/images/teams/' + Ii1I1I111iI
  if Iiii1I == 0 :
   oO0 ( I111iiiii1 + ' | ' + oO0o0OOOO + ' - ' + ooooo0Oo0 + ' | [COLOR yellow]' + o0I1IIIi11ii11 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
  else :
   iI1I1I1i1i = iI1I1I1i1i . replace ( '&#039;' , "'" )
   oO0 ( "[COLOR red][B]" + iI1I1I1i1i + " " + ooo0oo00O00Oo + '[/B][/COLOR] | ' + oO0o0OOOO + ' - ' + ooooo0Oo0 + ' | [COLOR yellow]' + o0I1IIIi11ii11 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
   if 100 - 100: I1ii11iIi11i * i11iIiiIii % o00oo / Oo0Ooo / O0OOooO + I1ii11iIi11i
   if 59 - 59: oO - iIii1
def iiiii111 ( name , url , iconimage ) :
 if 93 - 93: o00oo * OoOO
 I11 = xbmcgui . Dialog ( )
 if 27 - 27: I1IiiI * O0OOooO
 url , name = url . split ( "|SPLIT|" )
 oO0ooooo0O00 = name
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 if 5 - 5: OoOoOO00 % I1iiiiI1iII + iIii1
 IIi11i1i1iI1 = 1
 i1i1IiIi1 = 0
 IIiii11i = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0oOO0 = re . compile ( '<tr class="(.+?)</tr>' , re . DOTALL ) . findall ( IIiii11i )
 for iiiIi1II1III in O0oOO0 :
  url = re . compile ( 'data.+?="(.+?)"' ) . findall ( iiiIi1II1III ) [ 0 ]
  iiIiIIIiiI . append ( url )
  iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  if 8 - 8: iIii1 % iI1 . Oo0Ooo % O0OOooO - I1iiiiI1iII
 if IIi11i1i1iI1 == 1 :
  I11 . ok ( oO0o0o0ooO0oO , "Sorry no links found!" )
  quit ( )
  if 16 - 16: I1iiiiI1iII
 oO0ooooo0O00 = '[COLOR mediumpurple]' + oO0ooooo0O00 + '[/COLOR]'
 if 66 - 66: I1ii11iIi11i * O0OOooO . iI1
 oO00ooooO0o = I11 . select ( oO0ooooo0O00 , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  oo0oOo = iiI1IIIi [ oO00ooooO0o ]
  name = urllib . quote_plus ( iiI1IIIi [ oO00ooooO0o ] )
  import liveresolver
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  elif liveresolver . isValid ( url ) == True :
   url = liveresolver . resolve ( url )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  else :
   if '.m3u8' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   elif '.ts' in url :
    url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
   else :
    OOOOoOOo0O0 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=' + name + '%26url='
    o000O0o = "/"
    if not oo0oOo . endswith ( o000O0o ) :
     iI1iII1 = oo0oOo + "/"
    else :
     iI1iII1 = oo0oOo
    url = OOOOoOOo0O0 + iiIiIIIiiI [ oO00ooooO0o ] + "%26referer=" + iI1iII1
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
   I1III1111iIi . setPath ( url )
   xbmc . Player ( ) . play ( url , I1III1111iIi , False )
   if 96 - 96: OoOooOOOO % O0OOooO
def oOi1 ( ) :
 OO00Oo = 'http://mamahd.com/index.html'
 if 39 - 39: O0OOooO / O0 * iIii1
 if 17 - 17: OoOO / iIii1I11I1II1 - OoO0O00 + I1IiiI % iI1
 if 14 - 14: o0oOOo0O0Ooo % iIii1 + I1ii11iIi11i + OoO0O00
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="standard row channels">(.+?)<div class="standard row">' ) . findall ( o0O0O00 ) [ 0 ]
 OOOoOOo0o = re . compile ( '<a href="(.+?)".+?<img src="(.+?)">.+?<span>(.+?)</span>' ) . findall ( I11i1I1I )
 for o0O0O00 , iIiI1iI1i1I , oO0o0OOOO in OOOoOOo0o :
  OO00Oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O0O00 + '%26referer=no'
  oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 2 , iIiI1iI1i1I , iI111iI , '' )
  if 50 - 50: II111iiii - oO + iIii1I11I1II1 + iIii1I11I1II1
  if 91 - 91: II111iiii - O0 . iIii1I11I1II1 . O0 + I1ii11iIi11i - II111iiii
def iiIiiIi1 ( url ) :
 if 30 - 30: iI1 + II111iiii - iIii1 * OoooooooOO
 url = 'http://mamahd.com/index.html'
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="schedule">(.+?)<div id="pagination">' ) . findall ( o0O0O00 ) [ 0 ]
 I1iIiiiI1 = re . compile ( '<a(.+?)</a>' ) . findall ( I11i1I1I )
 for O0oOO0 in I1iIiiiI1 :
  time = re . compile ( '<span class="day">(.+?)</span.+?span class="hours">(.+?)</span.+?span class="minutes">(.+?)</span.+?span class="seconds">(.+?)</span>' ) . findall ( O0oOO0 )
  for OOO0O00Oo , ii1oOOO0ooOO , i11IiI1iiI11 , OOoOOOO00 in time :
   IIii1III = re . compile ( '<img src="(.+?)">' ) . findall ( O0oOO0 ) [ 0 ]
   ooooOoo0OO = re . compile ( '<img src=".+?"><span>(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   Oo0 = re . compile ( '<div class="away cell">.+?<span>(.+?)</span>' ) . findall ( O0oOO0 ) [ 0 ]
   O0000Oo00o = re . compile ( 'href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + O0000Oo00o + '%26referer=no'
   oO0 ( "[COLOR lime]" + OOO0O00Oo + "[/COLOR]" + "[COLOR lightseagreen]" + "-Days" + "[/COLOR]" + "  " + "[COLOR lime]" + ii1oOOO0ooOO + "[/COLOR]" + "[COLOR lightseagreen]" + "-Hours" + "[/COLOR]" + "  " + "[COLOR lime]" + i11IiI1iiI11 + "[/COLOR]" + "[COLOR lightseagreen]" + "-Minutes" + "[/COLOR]" + "   " + ":::" + "    " + "[COLOR yellow]" + ooooOoo0OO + "  " + "Vs" + "  " + Oo0 + "[/COLOR]" , url , 2 , IIii1III , iI111iI , '' )
   if 20 - 20: OoO0O00 . I1IiiI * i11iIiiIii / i11iIiiIii
def o00iIiiiII ( ) :
 if 5 - 5: OoooooooOO / o0oOOo0O0Ooo % OoOooOOOO % OoO0O00 * I1iiiiI1iII + iIii1I11I1II1
 OO00Oo = 'http://www.goalsarena.org/en/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 if 11 - 11: oO % i11iIiiIii % o00oo . iIii1
 for Ii1IIi , oOO0o in Ooo0o00o0o :
  iiiI1I11i1 ( "[COLOR lime]" + oOO0o + "[/COLOR]" , Ii1IIi , 69 , IiII , iI111iI , '' )
  if 65 - 65: I1iiiiI1iII . OoO0O00 + OoOO
def IIiI1I ( url ) :
 if 67 - 67: OoOO
 if 43 - 43: OoO0O00 % OoO0O00
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . I1iiiiI1iII . O0 * O0OOooO / OoooooooOO
 try :
  I11i1I1I = re . compile ( '<div id="videodetailsarea"(.+?)</div>' ) . findall ( o0O0O00 ) [ 0 ]
  OoO0O00O0oo0O = re . compile ( '<script data-config="(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
  if not 'http' in OoO0O00O0oo0O :
   II1iI1IIi = 'http:' + ( OoO0O00O0oo0O )
   Ii11iiI1 = o000o ( II1iI1IIi )
   oO0Oo0O0 = re . compile ( '"f4m":"(.+?)"' ) . findall ( Ii11iiI1 ) [ 0 ]
   oO0O = o000o ( oO0Oo0O0 )
   OO0oOOo0o = re . compile ( '<media url="(.+?)"' ) . findall ( oO0O ) [ 2 ]
   I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
   xbmc . Player ( ) . play ( OO0oOOo0o , I1III1111iIi , False )
   if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . OoOooOOOO % O0OOooO . II111iiii
   if 10 - 10: OoOO - i11iIiiIii . I1ii11iIi11i % i1IIi
 except : pass
 quit ( 0 )
 if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - iI1 . iIii1I11I1II1
 if 30 - 30: O0OOooO + O0OOooO % iIii1 - o0oOOo0O0Ooo - I1ii11iIi11i
 if 36 - 36: OoOooOOOO % iI1
 if 72 - 72: I1IiiI / I1iiiiI1iII - O0 + OoOooOOOO
 if 83 - 83: O0
 if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
 if 40 - 40: OoO0O00 + OoO0O00
def o0oo0o00ooO00 ( ) :
 if 37 - 37: OoO0O00 - I1ii11iIi11i . OoooooooOO . O0OOooO + OoOoOO00 / OoOO
 OO00Oo = 'http://www.opentopia.com/hiddencam.php'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<select name="country"(.+?)</select>' ) . findall ( o0O0O00 ) [ 0 ] . replace ( '&nbsp;-&nbsp;' , '' ) . replace ( '* ' , '' ) . replace ( 'Anywhere' , 'Random' )
 OoO0O00O0oo0O = re . compile ( '<option value=".+?">(.+?)</option>' ) . findall ( I11i1I1I )
 for O0oOO0 in OoO0O00O0oo0O :
  if not 'http' in O0oOO0 :
   oo0oOo = "<" + O0oOO0 + ">"
   try :
    I1oOoO0OOO00O = re . compile ( "<(.+?) \(.+?\)>" ) . findall ( oo0oOo ) [ 0 ]
   except : I1oOoO0OOO00O = O0oOO0
   ii11i11i1 = I1oOoO0OOO00O . replace ( " " , "+" )
   OO00Oo = "http://www.opentopia.com/hiddencam.php?country=" + ii11i11i1
   IiII = 'http://www.greenplanetfireandsecurity.co.uk/images/page-tops/cctv.jpg'
   iiiI1I11i1 ( "[COLOR lime]" + O0oOO0 + "[/COLOR]" , OO00Oo , 71 , IiII , iI111iI , '' )
   if 73 - 73: o0oOOo0O0Ooo % OoO0O00 + iIii1 + I1IiiI
def OoOO00 ( url ) :
 if 74 - 74: OoOooOOOO * OoOO - I1ii11iIi11i % iIii1I11I1II1
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<h3 class="navigation">(.+?)<div class="page">' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<li>(.+?)</li>' ) . findall ( I11i1I1I )
 for O0oOO0 in Ooo0o00o0o :
  Ii1IIi = re . compile ( '<a href="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
  if 56 - 56: I1ii11iIi11i - O0
  if not 'http' in Ii1IIi :
   IIiii11i = 'http://www.opentopia.com' + Ii1IIi + '?viewmode=livevideo'
   iIiI1iI1i1I = re . compile ( '<img src="(.+?)"' ) . findall ( O0oOO0 ) [ 0 ]
   oO0o0OOOO = re . compile ( '<div class="viewcamsname">(.+?)</div>' ) . findall ( O0oOO0 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , IIiii11i , 72 , iIiI1iI1i1I , iI111iI , '' )
   if 58 - 58: iIii1 + iIii1I11I1II1
 try :
  II1IIiiIiI = re . compile ( '<link rel="next" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , II1IIiiIiI , 71 , IiII , iI111iI , '' )
 except : pass
 if 94 - 94: OoOO . i1IIi
def O0OOo0o ( url ) :
 if 44 - 44: I1IiiI * iIii1I11I1II1 / O0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 try :
  I11i1I1I = re . compile ( '<div class="big">(.+?)<div id="camdetailbottom">' ) . findall ( o0O0O00 ) [ 0 ]
  iiiIi = re . compile ( '<img src="(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( iiiIi , I1III1111iIi , False )
  if 62 - 62: O0 . Oo0Ooo
 except : pass
 quit ( 0 )
 if 33 - 33: Oo0Ooo / iIii1I11I1II1 % i1IIi
 if 76 - 76: OoOO + iIii1I11I1II1 + OoOoOO00 . OoO0O00
 if 49 - 49: iIii1 / O0OOooO / iI1
 if 25 - 25: I1IiiI % O0 + i1IIi - O0OOooO
 if 38 - 38: o0oOOo0O0Ooo % oO + i11iIiiIii + I1iiiiI1iII + O0OOooO / i11iIiiIii
 if 94 - 94: I1iiiiI1iII - Oo0Ooo + o00oo
 if 59 - 59: OoOooOOOO . I1IiiI - iIii1I11I1II1 + iIii1I11I1II1
 if 56 - 56: o00oo + O0OOooO
 if 32 - 32: II111iiii + OoOoOO00 % O0OOooO / OoOoOO00 + I1ii11iIi11i
 if 2 - 2: i11iIiiIii - oO + OoO0O00 % OoOooOOOO * OoOO
 if 54 - 54: O0 - I1iiiiI1iII . iI1 % I1iiiiI1iII + I1iiiiI1iII
 if 36 - 36: iI1 % i11iIiiIii
 if 47 - 47: i1IIi + II111iiii . Oo0Ooo * o00oo . OoOooOOOO / i1IIi
 if 50 - 50: oO / i1IIi % OoooooooOO
 if 83 - 83: I1ii11iIi11i * I1ii11iIi11i + iI1
 if 57 - 57: O0 - O0 . I1ii11iIi11i / o0oOOo0O0Ooo / OoOO
def I1IiII1I1i1I1 ( ) :
 if 28 - 28: Oo0Ooo + iIii1 % II111iiii / OoO0O00 + i11iIiiIii
 ii11i11i1 = ''
 O0OoI1IiI111I11 = xbmc . Keyboard ( ii11i11i1 , 'Enter Search Term' )
 O0OoI1IiI111I11 . doModal ( )
 if O0OoI1IiI111I11 . isConfirmed ( ) :
  ii11i11i1 = O0OoI1IiI111I11 . getText ( )
  if len ( ii11i11i1 ) > 1 :
   OOo00 = ii11i11i1 . lower ( )
   if 20 - 20: I1ii11iIi11i
  else : quit ( )
  if 3 - 3: OoO0O00 * i1IIi . I1IiiI . O0 - OoOoOO00
 ooO = 0
 OOoooOoO0 = 9
 if 95 - 95: OoOO - I1ii11iIi11i - O0 . I1IiiI . I1iiiiI1iII
 Oo0o0000o0o0 . create ( oO0o0o0ooO0oO , '[COLOR yellow]Searching for ' + ii11i11i1 . title ( ) )
 Oo0o0000o0o0 . update ( 0 )
 if 7 - 7: oO
 oOoO0o00OO0 ( "[COLOR gold]STREAM ARMY HAVE JUST SCRAPPED MULTIPLE SITES FOR YOU[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 oOoO0o00OO0 ( "[COLOR gold]IF A LINK DOESN'T WORK JUST TRY ANOTHER ONE, WE DON'T HOST THE FILES[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 if 45 - 45: O0 - iI1
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching 300mb Movies...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 56 - 56: O0 + OoOO
 IiI11II11 = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://300mbmovies4u.co/?s=" + IiI11II11
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From 300Movies[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 oo0o0 ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 46 - 46: iIii1I11I1II1 / I1ii11iIi11i
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching SeeHD Movies...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 7 - 7: I1ii11iIi11i / II111iiii - OoOooOOOO + i1IIi + OoOO
 i11i11i = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://www.seehd.se/?s=" + i11i11i
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From SeeHD[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 OOoo0 ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 31 - 31: i11iIiiIii + iI1 - O0
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching UWatch...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 51 - 51: OoO0O00 * i1IIi / OoOO * iI1 + O0OOooO % I1ii11iIi11i
 IIIiI1iiiiiIi = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://www.uwatchfree.co/?s=" + IIIiI1iiiiiIi + '&submit=Search'
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Uwatch[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , Iii1ii1II11i , '' )
 OO0o ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 74 - 74: OoOooOOOO / OoooooooOO / Oo0Ooo * i11iIiiIii . II111iiii . OoooooooOO
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching Movie 2k...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 59 - 59: i11iIiiIii . OoooooooOO / OoOooOOOO * I1ii11iIi11i + OoooooooOO
 Ii1I1i1ii1I1 = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://movie2k.io/?s=" + Ii1I1i1ii1I1
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Movie2K[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 IiiIiiIi ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 98 - 98: iIii1 * iIii1I11I1II1 . OoOO * Oo0Ooo / I1ii11iIi11i + O0OOooO
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching House Movies...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 25 - 25: o00oo
 Iii11111iiI = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://housemovie.to/search?q=" + Iii11111iiI
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From House Movies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 OO0O0Oo0 ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 67 - 67: o0oOOo0O0Ooo
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching Afdah Movies...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 76 - 76: OoOoOO00 - I1IiiI + iI1 + OoOooOOOO
 i1Iiii = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://www.afdah.bz/?s=" + i1Iiii
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Afdah Movies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 Ii ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 87 - 87: iIii1 / oO - Oo0Ooo
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching CMovies...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 56 - 56: O0
 iIIIII1iI = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://cmovieshd.com/search/?q=" + iIIIII1iI
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From CMovies[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 IiiIi ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 18 - 18: Oo0Ooo - O0
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching Sockshare...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 85 - 85: OoOO - O0 * i11iIiiIii . i1IIi
 i11i1 = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://sockshare.net/search-movies/" + i11i1 + '.html'
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From Sockshare[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 O0o00oO0oOO ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 100 - 100: OoOooOOOO % i11iIiiIii * I1iiiiI1iII / OoO0O00 % I1ii11iIi11i + iI1
 ooO = ooO + 1
 I1Ii11II1I1 = 100 * int ( ooO ) / int ( OOoooOoO0 )
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellowgreen]Currently searching MovieFlix...' , '[COLOR lime]Site number ' + str ( ooO ) + ' of ' + str ( OOoooOoO0 ) + '[/COLOR]' )
 if 48 - 48: iIii1I11I1II1 % i1IIi + OoOoOO00 % o0oOOo0O0Ooo
 OO0oo00oOO = OOo00 . replace ( ' ' , '+' )
 OO00Oo = "http://movieflixter.to/search?q=" + OO0oo00oOO
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR lavender]Search Results From MovieFlix[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOoO0o00OO0 ( "[COLOR yellow]---------------------------------------------------[/COLOR]" , 'null' , 999 , 'img' , iI111iI , '' )
 oOO ( OO00Oo + "|SPLIT|" + ii11i11i1 )
 if 38 - 38: oO . I1iiiiI1iII . I1IiiI * OoO0O00
 Oo0o0000o0o0 . update ( I1Ii11II1I1 , '' , '[COLOR yellow]Filtering results...' , '[COLOR lime]Please wait...[/COLOR]' )
 time . sleep ( 2 )
 if 69 - 69: o0oOOo0O0Ooo % i11iIiiIii / OoOO
 Oo0o0000o0o0 . close ( )
 if 93 - 93: O0OOooO
def II11iIIii ( name , url , iconimage ) :
 if 57 - 57: O0 * I1ii11iIi11i . i11iIiiIii
 iconimage = "null"
 if 69 - 69: O0 / II111iiii * i1IIi
 IIi11i1i1iI1 = 0
 iiIiIIIiiI = [ ]
 iiI1IIIi = [ ]
 II11IiIi11 = [ ]
 if 66 - 66: O0
 oOooOOo00ooO = 1
 o0OO0oooo = 0
 if "http" in url :
  if 40 - 40: oO - OoOoOO00 * OoOooOOOO - iIii1 / OoOoOO00
  Oo0o0000o0o0 . create ( "Stream Army" , "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]" )
  Oo0o0000o0o0 . update ( 0 )
  if 71 - 71: o00oo / OoooooooOO % iIii1 / OoOoOO00 % oO
  while oOooOOo00ooO < 11 :
   I1Ii11II1I1 = 100 * int ( oOooOOo00ooO ) / int ( 10 )
   Oo0o0000o0o0 . update ( I1Ii11II1I1 , "" , "[COLOR lime]Connection attempt " + str ( oOooOOo00ooO ) + " of 10[/COLOR]" )
   o0O0O00 = o000o ( url )
   if 19 - 19: oO + iIii1 / o00oo / II111iiii
   if o0OO0oooo == 0 :
    oOooOOo00ooO = oOooOOo00ooO + 1
    IIi1ii1Ii = re . compile ( 'title="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
    IIi1ii1Ii = IIi1ii1Ii . split ( " - " ) [ 0 ]
    if 92 - 92: i1IIi % O0OOooO + O0OOooO - iIii1I11I1II1 . OoOO
    iIIi1 = re . compile ( '<td class="entry">(.+?)target' ) . findall ( o0O0O00 )
    for II in iIIi1 :
     o0Ooo0o0Oo = 1
     oo00ooooOOo00 = len ( II )
     ii1i = 100 * int ( o0Ooo0o0Oo ) / int ( oo00ooooOOo00 )
     Oo0o0000o0o0 . update ( ii1i , "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]" , "[COLOR lime]Filtering links " + str ( o0Ooo0o0Oo ) + " of " + str ( oo00ooooOOo00 ) + " possible matches[/COLOR]" )
     if 70 - 70: o00oo % iIii1 % I1IiiI + i11iIiiIii . OoOO % oO
     if not "putlocker.bypassed.info" in II :
      iI1ii111iiIii = re . compile ( '<a rel=".+?" href="(.+?)"' ) . findall ( II ) [ 0 ]
      IIi11i1i1iI1 = IIi11i1i1iI1 + 1
      iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
      iiIiIIIiiI . append ( iI1ii111iiIii )
      II11IiIi11 . append ( iconimage )
     o0OO0oooo = 1
     oOooOOo00ooO = 12
     o0Ooo0o0Oo = o0Ooo0o0Oo + 1
     if 57 - 57: o0oOOo0O0Ooo / oO
   if Oo0o0000o0o0 . iscanceled ( ) :
    sys . exit ( )
   import time
   time . sleep ( 1 )
   oOooOOo00ooO = oOooOOo00ooO + 1
   if 13 - 13: OoooooooOO + OoO0O00
 else :
  if 32 - 32: O0 + o00oo % Oo0Ooo
  IIiii11i = o000o ( url )
  O0oOO0 = re . compile ( '<td class="entry">(.+?)</tr>' ) . findall ( IIiii11i )
  if 7 - 7: I1ii11iIi11i / O0OOooO
  for II in O0oOO0 :
   url = re . compile ( 'href="(.+?)"' ) . findall ( II ) [ 0 ]
   if not "putlocker.unblocked.ink" in url :
    IIi11i1i1iI1 = IIi11i1i1iI1 + 1
    iiI1IIIi . append ( "Link " + str ( IIi11i1i1iI1 ) )
    iiIiIIIiiI . append ( url )
    II11IiIi11 . append ( iconimage )
    if 11 - 11: iIii1 * O0OOooO / O0OOooO - iI1
    if 68 - 68: I1IiiI % iIii1 - iIii1 / I1IiiI + I1ii11iIi11i - Oo0Ooo
    if 65 - 65: O0OOooO - i1IIi
 if IIi11i1i1iI1 == 0 :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
 name = '[COLOR lime]' + name + '[/COLOR]'
 oO00ooooO0o = I11 . select ( name , iiI1IIIi )
 if oO00ooooO0o < 0 :
  quit ( )
 else :
  url = iiIiIIIiiI [ oO00ooooO0o ]
  url = str ( url )
  IiII = II11IiIi11 [ oO00ooooO0o ]
  IiII = str ( IiII )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
   I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
   I1III1111iIi . setPath ( IiI1iiiIii )
   xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
   if 62 - 62: OoOooOOOO / o00oo % Oo0Ooo . OoooooooOO / i11iIiiIii / oO
def OooO0O0Ooo ( name , url , iconimage ) :
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = I1III1111iIi )
 xbmc . Player ( ) . play ( url , I1III1111iIi , False )
 if 15 - 15: I1ii11iIi11i . I1iiiiI1iII
def iI1111iiii ( name , url , iconimage ) :
 if 94 - 94: OoOooOOOO . I1IiiI
 name = name . replace ( '  ' , '' )
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
 else : url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
 if 73 - 73: i1IIi / II111iiii
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  quit ( )
 else :
  IiI1iiiIii = url
  I1III1111iIi = xbmcgui . ListItem ( name , iconImage = IiII , thumbnailImage = IiII )
  I1III1111iIi . setPath ( IiI1iiiIii )
  xbmc . Player ( ) . play ( IiI1iiiIii , I1III1111iIi , False )
  quit ( )
  if 45 - 45: OoOO / O0OOooO . OoooooooOO + OoO0O00
def oOoO00o ( name , url , iconimage ) :
 if 51 - 51: I1iiiiI1iII % i11iIiiIii % iIii1 + oO % I1ii11iIi11i
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  IIIII = url . split ( 'list=' ) [ 1 ]
  iiiiI1I = iiIIIII1i1iI + IIIII + o0oO0
  iI1111ii1I = urllib2 . Request ( iiiiI1I )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   II1IIiiIiI = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   iiiiI1I = oo00 + II1IIiiIiI + o00 + IIIII + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , iiiiI1I , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 93 - 93: Oo0Ooo * o00oo + OoO0O00 - oO . I1ii11iIi11i + OoooooooOO
  if 44 - 44: OoOooOOOO * o0oOOo0O0Ooo
  if 49 - 49: iI1 % OoOooOOOO * i11iIiiIii / o00oo % iI1
  if 70 - 70: OoOoOO00 / II111iiii % O0OOooO - I1iiiiI1iII
  for name , I1II1IiI1 in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + I1II1IiI1
   iconimage = 'https://i.ytimg.com/vi/' + I1II1IiI1 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOoO0o00OO0 ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 26 - 26: iI1 * Oo0Ooo
 if 'https://www.googleapis.com/youtube/v3' in url :
  IIIII = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   II1IIiiIiI = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   iiiiI1I = oo00 + II1IIiiIiI + o00 + IIIII + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , iiiiI1I , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 31 - 31: OoOooOOOO * o00oo . OoOO
  if 35 - 35: OoOooOOOO
  if 94 - 94: O0OOooO / i11iIiiIii % O0
  for name , I1II1IiI1 in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + I1II1IiI1
   iconimage = 'https://i.ytimg.com/vi/' + I1II1IiI1 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOoO0o00OO0 ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 70 - 70: OoOooOOOO - Oo0Ooo / OoooooooOO % OoooooooOO
     if 95 - 95: OoooooooOO % OoooooooOO . OoOO
     if 26 - 26: o00oo + iIii1 - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 68 - 68: O0
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  IiI1iiiIii = liveresolver . resolve ( url )
 else : IiI1iiiIii = url
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 I1III1111iIi . setPath ( IiI1iiiIii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
 if 76 - 76: I1ii11iIi11i
def ooO000OO ( url ) :
 if 43 - 43: O0OOooO * oO % iI1
 try :
  oO0o0OOOO , url , O0O0OoOO0 = url . split ( "!SASPLIT!" )
  I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( url , I1III1111iIi , False )
 except :
  xbmc . Player ( ) . play ( url )
  if 38 - 38: Oo0Ooo
def o000o ( url ) :
 try :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I , timeout = 5 )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 34 - 34: OoOoOO00
  return o0O0O00
 except : quit ( )
 if 70 - 70: iIii1I11I1II1 * iIii1 - iI1 / Oo0Ooo % o00oo
def Oo0oOOo ( url ) :
 if 66 - 66: OoooooooOO + O0OOooO * I1iiiiI1iII
 if 2 - 2: I1iiiiI1iII . OoO0O00 / o00oo
 try :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'obsession' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  o0O0O00 = OO00OooO0OO . read ( )
  if 41 - 41: OoO0O00 . oO * iIii1 * oO
  ooOO = o00O ( o0O0O00 )
  print "--------- decoded --------" , ooOO
  OO00OooO0OO . close ( )
  ooOO = ooOO . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 86 - 86: OoOO . iI1 / iIii1 - OoooooooOO
  return ooOO
 except : quit ( )
 if 45 - 45: iI1
def OOOo00oo0oO ( url ) :
 iI1111ii1I = urllib2 . Request ( url )
 iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 if 25 - 25: iI1 % O0
 return o0O0O00
 if 44 - 44: oO . OoOO * II111iiii / iIii1 + iIii1I11I1II1
def Ii1111III1 ( ) :
 oO00oooo0 = [ ]
 OO0 = sys . argv [ 2 ]
 if len ( OO0 ) >= 2 :
  o0Oo0oO0oOO00 = sys . argv [ 2 ]
  Oo = o0Oo0oO0oOO00 . replace ( '?' , '' )
  if ( o0Oo0oO0oOO00 [ len ( o0Oo0oO0oOO00 ) - 1 ] == '/' ) :
   o0Oo0oO0oOO00 = o0Oo0oO0oOO00 [ 0 : len ( o0Oo0oO0oOO00 ) - 2 ]
  OoO00OOoOOOo0 = Oo . split ( '&' )
  oO00oooo0 = { }
  for IIi11i1i1iI1 in range ( len ( OoO00OOoOOOo0 ) ) :
   oOoO00O = { }
   oOoO00O = OoO00OOoOOOo0 [ IIi11i1i1iI1 ] . split ( '=' )
   if ( len ( oOoO00O ) ) == 2 :
    oO00oooo0 [ oOoO00O [ 0 ] ] = oOoO00O [ 1 ]
 return oO00oooo0
 if 31 - 31: O0OOooO . OoOoOO00 % OoOoOO00 % Oo0Ooo % I1IiiI * I1iiiiI1iII
def I1i1iII1I11 ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 o00OOo0o0O = name . partition ( '(' )
 I111Iii1 = ""
 i11i = ""
 if len ( o00OOo0o0O ) > 0 :
  I111Iii1 = o00OOo0o0O [ 0 ]
  i11i = o00OOo0o0O [ 2 ] . partition ( ')' )
 if len ( i11i ) > 0 :
  i11i = i11i [ 0 ]
 O0o0O00o0o = metahandlers . MetaData ( )
 OoO0o = O0o0O00o0o . get_meta ( 'movie' , name = I111Iii1 , year = i11i )
 II1IIiiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = OoO0o [ 'cover_url' ] , thumbnailImage = OoO0o [ 'cover_url' ] )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = OoO0o )
 O00O00 = [ ]
 O00O00 . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 I1III1111iIi . addContextMenuItems ( O00O00 , replaceItems = False )
 if not OoO0o [ 'backdrop_url' ] == '' : I1III1111iIi . setProperty ( 'fanart_image' , OoO0o [ 'backdrop_url' ] )
 else : I1III1111iIi . setProperty ( 'fanart_image' , Iii1ii1II11i )
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1IIiiI1 , listitem = I1III1111iIi , isFolder = isFolder , totalItems = itemcount )
 return oO0OIIIiIi1iiI
 if 66 - 66: Oo0Ooo - iIii1I11I1II1
def iiiI1I11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 II1IIiiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : II1IIiiI1 = url
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1IIiiI1 , listitem = I1III1111iIi , isFolder = True )
 return oO0OIIIiIi1iiI
 if 9 - 9: o0oOOo0O0Ooo % I1ii11iIi11i . I1ii11iIi11i
def oO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 II1IIiiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1IIiiI1 , listitem = I1III1111iIi , isFolder = False )
 return oO0OIIIiIi1iiI
 if 28 - 28: OoooooooOO % o00oo + I1ii11iIi11i + O0 . oO
def oOoO0o00OO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 80 - 80: i11iIiiIii % I1ii11iIi11i
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 II1IIiiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  I1III1111iIi . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : II1IIiiI1 = url
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1IIiiI1 , listitem = I1III1111iIi , isFolder = False )
 return oO0OIIIiIi1iiI
 if 54 - 54: o0oOOo0O0Ooo + OoOooOOOO - iIii1I11I1II1 % O0OOooO % iIii1
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 19 - 19: I1ii11iIi11i / iIii1I11I1II1 % i1IIi . OoooooooOO
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 II1IIiiI1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 oO0OIIIiIi1iiI = True
 I1III1111iIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1III1111iIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I1III1111iIi . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  I1III1111iIi . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : II1IIiiI1 = url
 oO0OIIIiIi1iiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = II1IIiiI1 , listitem = I1III1111iIi , isFolder = False )
 return oO0OIIIiIi1iiI
 if 57 - 57: O0OOooO . Oo0Ooo - OoO0O00 - i11iIiiIii * oO / o0oOOo0O0Ooo
def OO0O0OO ( url ) :
 import urlresolver
 if 21 - 21: I1iiiiI1iII
 if 'movieflixter.to' in url :
  iI1111ii1I = urllib2 . Request ( url )
  iI1111ii1I . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iI1111ii1I )
  url = OO00OooO0OO . geturl ( )
  if 24 - 24: I1iiiiI1iII / O0OOooO
  if 61 - 61: iIii1I11I1II1 + o00oo
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  IiI1iiiIii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  IiI1iiiIii = liveresolver . resolve ( url )
 else : IiI1iiiIii = url
 I1III1111iIi = xbmcgui . ListItem ( oO0o0OOOO , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O0OoOO0 )
 I1III1111iIi . setPath ( IiI1iiiIii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1III1111iIi )
 if 8 - 8: oO + OoO0O00
 if 9 - 9: iI1 + o0oOOo0O0Ooo
def I1iII1IIi1IiI ( url ) :
 if 8 - 8: iIii1I11I1II1
 oOOo0ooO0 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( oOOo0ooO0 )
 sys . exit ( 1 )
 if 38 - 38: oO
def I1II1O0o0OO00O ( text , pattern ) :
 if 60 - 60: iIii1I11I1II1 + o0oOOo0O0Ooo . iIii1I11I1II1 . OoOooOOOO + OoOooOOOO . O0OOooO
 iI1i11Iiii = ""
 try :
  o0o00OoO0 = re . findall ( pattern , text , flags = re . DOTALL )
  iI1i11Iiii = o0o00OoO0 [ 0 ]
 except :
  iI1i11Iiii = ""
  if 89 - 89: iIii1 / OoO0O00 * O0 / OoOooOOOO . oO
 return iI1i11Iiii
 if 17 - 17: OoOooOOOO
def i1i1iI1iiiI ( str ) :
 if 56 - 56: O0OOooO * o0oOOo0O0Ooo + OoOooOOOO
 try :
  import chardet
  str = str . decode ( chardet . detect ( str ) [ "encoding" ] ) . encode ( "utf-8" )
 except :
  try :
   str = str . encode ( "utf-8" )
  except :
   pass
 return str
 if 48 - 48: iIii1 * OoO0O00 % oO - OoOooOOOO
def IIiIi1iI ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 Oo0000OOO0 = xbmcgui . Window ( id )
 Ooo0O0OO = 50
 while ( Ooo0O0OO > 0 ) :
  try :
   xbmc . sleep ( 10 )
   Ooo0O0OO -= 1
   Oo0000OOO0 . getControl ( 1 ) . setLabel ( heading )
   Oo0000OOO0 . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 38 - 38: oO
def Iiiii1Iii1I ( link ) :
 try :
  I11i1I1I = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 83 - 83: OoOoOO00
def iIIiII ( ) :
 if 62 - 62: o00oo + Oo0Ooo / i11iIiiIii
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 90 - 90: iIii1I11I1II1 + OoOoOO00
 if II11iiii1Ii >= 1.0 and II11iiii1Ii <= 16.9 :
  IiI = 'Jarvis'
 elif II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  IiI = 'Krypton'
  if 16 - 16: Oo0Ooo / OoO0O00 / I1iiiiI1iII / iIii1I11I1II1
 if IiI == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif IiI == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 44 - 44: Oo0Ooo . Oo0Ooo + OoooooooOO * i11iIiiIii / OoOooOOOO + oO
o0Oo0oO0oOO00 = Ii1111III1 ( ) ; OO00Oo = None ; oO0o0OOOO = None ; iIiII11 = None ; II11IiiiiI1i = None ; O0O0OoOO0 = None
try : II11IiiiiI1i = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "site" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "url" ] )
except : pass
try : oO0o0OOOO = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "name" ] )
except : pass
try : iIiII11 = int ( o0Oo0oO0oOO00 [ "mode" ] )
except : pass
try : O0O0OoOO0 = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "iconimage" ] )
except : pass
try : Iii1ii1II11i = urllib . unquote_plus ( o0Oo0oO0oOO00 [ "fanart" ] )
except : pass
if 68 - 68: OoOooOOOO * II111iiii + OoOoOO00
if iIiII11 == None or OO00Oo == None or len ( OO00Oo ) < 1 : II1III ( )
elif iIiII11 == 1 : o00oooO0Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif iIiII11 == 2 : oOoO00o ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 3 : IIIii11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 4 : OooO0O0Ooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 5 : SEARCH ( )
elif iIiII11 == 6 : YOUTUBE_CHANNEL ( OO00Oo )
elif iIiII11 == 7 : ooO000OO ( OO00Oo )
elif iIiII11 == 8 : iI11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 9 : I1iII1IIi1IiI ( OO00Oo )
elif iIiII11 == 10 : I11iI1i1I11I11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 11 : OooOo0ooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 12 : oOi1 ( )
elif iIiII11 == 13 : i1I1iI ( OO00Oo )
elif iIiII11 == 14 : II11iIIii ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 15 : OOOoO ( OO00Oo )
elif iIiII11 == 16 : oo0ooooO ( OO00Oo )
elif iIiII11 == 17 : iII ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 18 : OoOo00o ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 19 : i1II ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 20 : o0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif iIiII11 == 21 : OoOOo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 22 : OO0O0Oo0 ( OO00Oo )
elif iIiII11 == 23 : O0O0o0o0o ( )
elif iIiII11 == 24 : OoO ( OO00Oo )
elif iIiII11 == 25 : IIiIiiii ( OO00Oo )
elif iIiII11 == 26 : i111 ( )
elif iIiII11 == 27 : iIiii ( OO00Oo )
elif iIiII11 == 28 : i11i1iiI1i ( OO00Oo )
elif iIiII11 == 29 : o000O000 ( OO00Oo )
elif iIiII11 == 30 : I11o0000o0Oo ( )
elif iIiII11 == 31 : oOOo0OoOOOoo ( OO00Oo )
elif iIiII11 == 32 : i1Iii11Ii1i1 ( )
elif iIiII11 == 33 : ii111I ( OO00Oo )
elif iIiII11 == 34 : o00o0 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 35 : o0o0O ( )
elif iIiII11 == 36 : oOo0O ( OO00Oo )
elif iIiII11 == 37 : O0O0Ooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 38 : IIII1 ( )
elif iIiII11 == 39 : iIi1Ii1i1iI ( OO00Oo )
elif iIiII11 == 40 : o0o0oOoOO0O ( OO00Oo )
elif iIiII11 == 41 : iI1iiII11I ( )
elif iIiII11 == 42 : iIi1Ii ( OO00Oo )
elif iIiII11 == 43 : II1 ( OO00Oo , IiII , Iii1ii1II11i )
elif iIiII11 == 44 : iiIiiIi1 ( OO00Oo )
elif iIiII11 == 45 : Ii1 ( OO00Oo )
elif iIiII11 == 46 : oOO0 ( )
elif iIiII11 == 47 : Ii1II ( OO00Oo )
elif iIiII11 == 48 : SCRAPE_SPORTSMAMA_PLAY ( OO00Oo )
elif iIiII11 == 49 : Ii111 ( )
elif iIiII11 == 50 : I1i1i ( OO00Oo )
elif iIiII11 == 51 : IIi ( OO00Oo )
elif iIiII11 == 52 : iI1I1iIi11 ( )
elif iIiII11 == 53 : Ii ( OO00Oo )
elif iIiII11 == 54 : Iii ( OO00Oo )
elif iIiII11 == 55 : Oo00O0OO ( )
elif iIiII11 == 56 : iiiii111 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif iIiII11 == 57 : oO00o ( OO00Oo )
elif iIiII11 == 58 : iIIiIii11i1Ii ( OO00Oo )
elif iIiII11 == 59 : oooO00Oo ( OO00Oo )
elif iIiII11 == 60 : iIi11i ( )
elif iIiII11 == 61 : O0o00oO0oOO ( OO00Oo )
elif iIiII11 == 62 : i1iiiIii11 ( OO00Oo )
elif iIiII11 == 63 : OOOO ( OO00Oo )
elif iIiII11 == 64 : I1ii1 ( OO00Oo )
elif iIiII11 == 65 : o0O0oo0o ( )
elif iIiII11 == 66 : iII1ii1I1i ( OO00Oo )
elif iIiII11 == 67 : o00iI1i1II ( OO00Oo )
elif iIiII11 == 68 : o00iIiiiII ( )
elif iIiII11 == 69 : IIiI1I ( OO00Oo )
elif iIiII11 == 70 : o0oo0o00ooO00 ( )
elif iIiII11 == 71 : OoOO00 ( OO00Oo )
elif iIiII11 == 72 : O0OOo0o ( OO00Oo )
elif iIiII11 == 73 : IiiIi ( OO00Oo )
elif iIiII11 == 74 : oO0oooooo ( OO00Oo )
elif iIiII11 == 75 : o0O0ooOOoO ( )
elif iIiII11 == 76 : oOO ( OO00Oo )
elif iIiII11 == 77 : OooooOoO ( OO00Oo )
elif iIiII11 == 78 : IiIIII ( )
elif iIiII11 == 79 : oo0o0 ( OO00Oo )
elif iIiII11 == 80 : oOo0OooOo ( OO00Oo )
elif iIiII11 == 81 : IiiIiiIi ( OO00Oo )
elif iIiII11 == 82 : o0o0oOO ( OO00Oo )
elif iIiII11 == 83 : OO0o ( OO00Oo )
elif iIiII11 == 84 : o0000 ( OO00Oo )
elif iIiII11 == 85 : OOoo0 ( OO00Oo )
elif iIiII11 == 86 : oOOoO0OO00OOo0 ( OO00Oo )
if 77 - 77: o0oOOo0O0Ooo . i1IIi
if 77 - 77: i1IIi * OoooooooOO % I1iiiiI1iII % o0oOOo0O0Ooo % O0OOooO / I1ii11iIi11i
if 64 - 64: i11iIiiIii . O0OOooO
if 93 - 93: O0 - OoO0O00 . I1IiiI
if 64 - 64: OoOoOO00 + o0oOOo0O0Ooo
if 65 - 65: II111iiii / Oo0Ooo
if 42 - 42: i11iIiiIii . O0
if 75 - 75: oO + iIii1I11I1II1
if 19 - 19: I1IiiI + i11iIiiIii . iIii1 - OoOooOOOO / OoOO + o0oOOo0O0Ooo
if 38 - 38: Oo0Ooo / iIii1I11I1II1 * iIii1I11I1II1 % I1ii11iIi11i
elif iIiII11 == 90 : O0o0O0OO00o ( )
elif iIiII11 == 91 : I1IiII1I1i1I1 ( )
if 92 - 92: OoOooOOOO / O0 * I1IiiI - OoOooOOOO
elif iIiII11 == 666 : OO0O0OO ( OO00Oo )
if 99 - 99: i11iIiiIii % OoooooooOO
if 56 - 56: iIii1 * oO
if 98 - 98: OoOooOOOO + O0 * oO + i11iIiiIii - iI1 - iIii1I11I1II1
if 5 - 5: iI1 % Oo0Ooo % iIii1 % O0OOooO
if 17 - 17: OoOO + II111iiii + OoooooooOO / iI1 / iIii1
if 80 - 80: o0oOOo0O0Ooo % i1IIi / OoOooOOOO
if 56 - 56: i1IIi . i11iIiiIii
if 15 - 15: II111iiii * o00oo % I1iiiiI1iII / i11iIiiIii - o00oo + Oo0Ooo
if 9 - 9: OoOooOOOO - o00oo + O0 / I1iiiiI1iII % i1IIi
if 97 - 97: o0oOOo0O0Ooo * O0OOooO
if 78 - 78: OoOooOOOO . iI1 + o00oo * I1iiiiI1iII - i1IIi
if 27 - 27: OoOO % i1IIi . Oo0Ooo % oO
if 10 - 10: iIii1 / OoooooooOO
if iIiII11 == None or OO00Oo == None or len ( OO00Oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
