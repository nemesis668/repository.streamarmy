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
I1i1iiI1 = base64 . b64decode ( b'aHR0cDovL3d3dy5zdHJlYW1hcm15LmNvLnVrL01haW4vTWVudS54bWw=' )
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
oOo0oooo00o = 'http://www.streamarmy.co.uk/Main/Exceptions/Exceptions.xml'
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
   elif '<cmovies>' in oO0Oo :
    oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    O0O0OoOO0 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    OO00Oo = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( oO0o0OOOO , OO00Oo , 62 , O0O0OoOO0 , Iii1ii1II11i )
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
   elif '<cmovies>' in oO0Oo :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oO0Oo ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oO0Oo ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oO0Oo ) [ 0 ]
    url = re . compile ( '<cmovies>(.+?)</cmovies>' ) . findall ( oO0Oo ) [ 0 ]
    iiiI1I11i1 ( name , url , 62 , iconimage , fanart )
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
  III1iII1I1ii ( name , url , 2 , IiII , Iii1ii1II11i , '' )
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
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / I1ii11iIi11i
  if 96 - 96: OoooooooOO + o00oo
def iiII1i11i ( url ) :
 if 11 - 11: I1IiiI / II111iiii + o0oOOo0O0Ooo * I1ii11iIi11i - I1ii11iIi11i - I1IiiI
 o0O0O00 = o000o ( url )
 O0O0OoOO0 = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 I11i1I1I = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 85 - 85: OoOooOOOO % o00oo / iIii1I11I1II1 . iIii1I11I1II1
 for iIi in OOo :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( iIi ) [ 0 ]
   III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 37 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 31 - 31: o0oOOo0O0Ooo % OoO0O00
 try :
  iI1I = re . compile ( '<li><a href=\"([^"]*)\">Next' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iI1I , 36 , IiII , iI111iI , '' )
 except : pass
 if 100 - 100: iIii1I11I1II1 + OoOoOO00 / Oo0Ooo . i11iIiiIii
def III1I1Iii1iiI ( name , url , iconimage ) :
 if 17 - 17: OoOO % iIii1I11I1II1 - iIii1I11I1II1
 o0O0O00 = o000o ( url )
 i1iI1 = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 i11ii1ii11i ( name , i1iI1 , iconimage )
 if 78 - 78: I1iiiiI1iII + OoOooOOOO . O0OOooO - I1iiiiI1iII . OoOO
 if 30 - 30: I1IiiI + OoO0O00 % OoOO * I1iiiiI1iII / Oo0Ooo - OoOooOOOO
 if 64 - 64: iIii1I11I1II1
 if 21 - 21: Oo0Ooo . II111iiii
 if 54 - 54: II111iiii % II111iiii
 if 86 - 86: O0 % OoOO * O0OOooO * iIii1I11I1II1 * i1IIi * OoOooOOOO
 if 83 - 83: OoOoOO00 % II111iiii - OoOoOO00 + iIii1 - O0
def oO0oo000OOOoO ( ) :
 if 22 - 22: II111iiii / I1IiiI % I1ii11iIi11i
 OO00Oo = 'http://www.readcomics.tv/comic-list'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 if 57 - 57: iI1 + O0 . OoOO
 for IIi1i11111 in OOo :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 39 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 46 - 46: iIii1
def ii1iIi1iIiI1i ( url ) :
 if 40 - 40: i1IIi % iI1
 o0O0O00 = o000o ( url )
 ooo0o00 = re . compile ( '<div class="manga-image"><img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oO0o0OOOO = re . compile ( '<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ] . replace ( 'Read ' , '' ) . replace ( 'Online' , '' )
 ooO = re . compile ( '<a class="stread" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0O = ooO . split ( '/' ) [ - 1 ]
 O00oO = o0O . replace ( 'chapter-' , ' ' )
 O00oO = int ( O00oO )
 iiiI1I11i1 ( "[COLOR lime]Issue " + str ( O00oO ) + "[/COLOR]" , ooO , 40 , ooo0o00 , iI111iI , '' )
 I11i1I1I = re . compile ( '<ul class="ml-list">(.+?)</ul>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( I11i1I1I )
 for IIi1i11111 in sorted ( OOo ) :
  O00oO = O00oO + 1
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
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
 OOo0 = 1
 ii11i11i1 = "http://" + ii11i11i1 + "/"
 if 25 - 25: OoooooooOO + iIii1 * I1ii11iIi11i
 while OOo0 <= oooooOOO000Oo :
  url = ii11i11i1 + str ( OOo0 ) + ".jpg"
  oO0 ( "[COLOR lime]Page " + str ( OOo0 ) + "[/COLOR]" , url , 9 , url , url , '' )
  OOo0 = OOo0 + 1
  if 92 - 92: I1IiiI + OoOooOOOO + O0 / o0oOOo0O0Ooo + oO
  if 18 - 18: O0OOooO * OoOoOO00 . I1iiiiI1iII / I1ii11iIi11i / i11iIiiIii
  if 21 - 21: o00oo / I1ii11iIi11i + OoOO + OoooooooOO
  if 91 - 91: i11iIiiIii / i1IIi + I1iiiiI1iII + O0OOooO * i11iIiiIii
  if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + OoOooOOOO * oO . iIii1
  if 52 - 52: O0OOooO + O0 . I1iiiiI1iII . I1ii11iIi11i . OoO0O00
  if 97 - 97: I1IiiI / I1iiiiI1iII
def Oooo0 ( url ) :
 if 59 - 59: OoooooooOO
 if 47 - 47: O0OOooO - I1IiiI / II111iiii
 o0O0O00 = o000o ( url ) . replace ( '&amp;' , 'and' )
 if 12 - 12: iI1
 if 83 - 83: I1iiiiI1iII . O0 / Oo0Ooo / iI1 - II111iiii
 I11i1I1I = re . compile ( '<li.+?href="(.+?)".+?>(.+?)</a.+?li>' ) . findall ( o0O0O00 )
 for i11i1I1 , oO0oO0 in I11i1I1I :
  if i11i1I1 . find ( 'categ' ) != - 1 :
   i1i1IIIIi1i = url + i11i1I1
   iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , i1i1IIIIi1i , 25 , IiII , iI111iI , '' )
   if 7 - 7: iIii1I11I1II1 + I1iiiiI1iII * i11iIiiIii / OoooooooOO + I1iiiiI1iII - Oo0Ooo
def Iiii ( url ) :
 if 89 - 89: o00oo
 iIiiii = o000o ( url ) . replace ( '&#8217;' , "'" )
 O0000OOO0 = re . compile ( '<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"' , re . DOTALL ) . findall ( iIiiii )
 for url , ooo0 , oO0o0OOOO in O0000OOO0 :
  oO000oOo00o0o = o000o ( url )
  O00oO0 = re . compile ( '<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"' ) . findall ( oO000oOo00o0o )
  for O0Oo00OoOo in O00oO0 :
   try :
    ii1ii111 = O0Oo00OoOo . split ( "/embed/" ) [ 1 ]
    i11111I1I = "plugin://plugin.video.youtube/play/?video_id=" + ii1ii111
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11111I1I , 7 , ooo0 , iI111iI , '' )
   except : pass
   if 11 - 11: OoooooooOO . oO
 try :
  iI1I = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( iIiiii ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iI1I , 25 , IiII , iI111iI , '' )
 except : pass
 if 80 - 80: OoooooooOO - iI1 * OoOO * I1ii11iIi11i / I1IiiI / iI1
 if 13 - 13: oO * O0OOooO + i11iIiiIii * oO - O0OOooO
 if 23 - 23: iIii1I11I1II1 * i1IIi % OoooooooOO * iIii1
 if 9 - 9: iIii1 - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
 if 39 - 39: iIii1 * Oo0Ooo + iIii1I11I1II1 - iIii1 + iI1
 if 69 - 69: O0
 if 85 - 85: O0OOooO / O0
def iI1iIIIi1i ( ) :
 if 89 - 89: iIii1I11I1II1
 OO00Oo = 'http://www.filmon.com/tv/bbc-news'
 if 21 - 21: OoOooOOOO % OoOooOOOO
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"group_id"(.+?)channels_count' ) . findall ( o0O0O00 )
 for iiI1 in I11i1I1I :
  oO0o0OOOO = re . compile ( 'title":"(.+?)"' ) . findall ( iiI1 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , iiI1 , 27 , IiII , iI111iI , '' )
  if 16 - 16: II111iiii + o00oo - OoooooooOO
def ii1iI ( url ) :
 if 49 - 49: o0oOOo0O0Ooo . iIii1 / OoO0O00 + II111iiii
 I11i1I1I = re . compile ( '{"id"(.+?)}' ) . findall ( url )
 for ii11i in I11i1I1I :
  oO0o0OOOO = re . compile ( ':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"' ) . findall ( ii11i ) [ 0 ]
  O0O0OoOO0 = re . compile ( ':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"' ) . findall ( ii11i ) [ 0 ]
  url = re . compile ( ':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"' ) . findall ( ii11i ) [ 0 ]
  O0O0OoOO0 = O0O0OoOO0 . replace ( '\\' , '' )
  i11i1I1 = 'https://www.filmon.com/tv/' + url
  III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , i11i1I1 , 2 , O0O0OoOO0 , iI111iI , '' )
  if 35 - 35: I1ii11iIi11i * I1iiiiI1iII - OoO0O00 % o0oOOo0O0Ooo
  if 87 - 87: OoOoOO00 * oO . OoOooOOOO
  if 51 - 51: iI1 % iIii1I11I1II1 - OoooooooOO % O0OOooO * iIii1I11I1II1 % OoO0O00
  if 99 - 99: o00oo * II111iiii * oO
  if 92 - 92: Oo0Ooo
  if 40 - 40: OoOoOO00 / iIii1
  if 79 - 79: OoO0O00 - iIii1I11I1II1 + OoOO - oO
def OoO ( url ) :
 if 35 - 35: OoOoOO00 + i11iIiiIii - II111iiii
 Ii1ii111i1 = 1
 url = 'http://hdvidmusic.com'
 i1i1i1I = o000o ( url )
 oOoo000 = re . compile ( '<a href="([^"]*)">>></a></div>' , re . DOTALL ) . findall ( i1i1i1I ) [ 0 ]
 oOoo000 = oOoo000 . replace ( '?page=' , '' )
 OooOo00o = int ( oOoo000 )
 if 20 - 20: i1IIi * oO + II111iiii % o0oOOo0O0Ooo % o00oo
 url = 'http://hdvidmusic.com/?page=' + str ( Ii1ii111i1 )
 while Ii1ii111i1 <= OooOo00o :
  if 13 - 13: Oo0Ooo
  url = 'http://hdvidmusic.com/?page=' + str ( Ii1ii111i1 )
  if 60 - 60: I1ii11iIi11i * I1IiiI
  o0O0O00 = o000o ( url )
  I11i1I1I = re . compile ( '<div class="cell_container">(.+?)<!--div class="video_rating">' , re . DOTALL ) . findall ( o0O0O00 )
  if 17 - 17: iI1 % Oo0Ooo / I1ii11iIi11i . iIii1 * iI1 - II111iiii
  for IIi1i11111 in I11i1I1I :
   oO0oO0 = re . compile ( '<a title="(.+?)" href=".+?">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   o0O0O00 = re . compile ( '<a title=".+?" href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   ooo0 = re . compile ( 'src="(.+?)"/>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   i1i1IIii1i1 = re . compile ( '<div class="video_quality">(.+?)</div>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   iIiiii = 'http://hdvidmusic.com' + o0O0O00
   oOoO00 = 'http://hdvidmusic.com' + ooo0
   oO0 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , iIiiii , 29 , oOoO00 , iI111iI , '' )
  Ii1ii111i1 = Ii1ii111i1 + 1
  if 40 - 40: o0oOOo0O0Ooo
def OOOooo ( url ) :
 if 99 - 99: II111iiii * iIii1 % iIii1I11I1II1 / OoOO
 iIiiii = o000o ( url ) . replace ( '?' , '' )
 OOO00O0oOOo = re . compile ( '<iframe id\=.+?www(.+?)aut' ) . findall ( iIiiii ) [ 0 ]
 id = OOO00O0oOOo . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 71 - 71: OoOooOOOO / o0oOOo0O0Ooo / oO % iI1
def O0oooo00o0Oo ( ) :
 OO00Oo = 'http://www.bigtop40.com/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&amp;' , 'and' ) . replace ( '&#39;' , "'" ) . replace ( '&quot;' , '"' )
 I11i1I1I = re . compile ( '<li data-chart-position=".+?"(.+?)</em>' , re . DOTALL ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  try :
   I1iii = re . compile ( '<a name="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ] . replace ( 'number' , 'Number' ) . replace ( '_' , ' ' )
   ooo0o00 = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   oO0o0O0Ooo0o = re . compile ( 'alt="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   OO00Oo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if not 'http' in OO00Oo :
    i11i1I1 = 'http://www.bigtop40.com' + OO00Oo
    oO0 ( "[COLOR red]" + I1iii + "[/COLOR]" + ' -- ' + "[COLOR lime]" + oO0o0O0Ooo0o + "[/COLOR]" , i11i1I1 , 47 , ooo0o00 , iI111iI , '' )
  except : pass
  if 21 - 21: oO - I1IiiI + OoOooOOOO
def ooOoo0o0O ( url ) :
 iIiiii = o000o ( url ) . replace ( '?' , '' )
 OOO00O0oOOo = re . compile ( '<iframe width=".+?" height="348" src="(.+?)"' ) . findall ( iIiiii ) [ 0 ]
 id = OOO00O0oOOo . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 77 - 77: o00oo
 if 64 - 64: Oo0Ooo * OoooooooOO . Oo0Ooo
 if 2 - 2: OoooooooOO % iI1
 if 63 - 63: I1IiiI % iIii1I11I1II1
 if 39 - 39: I1iiiiI1iII / II111iiii / I1ii11iIi11i % I1IiiI
 if 89 - 89: oO + OoooooooOO + oO * i1IIi + iIii1I11I1II1 % OoOooOOOO
 if 59 - 59: iI1 + i11iIiiIii
def oo0OOo0O ( ) :
 OO00Oo = 'http://www.hdmovieswatch.org/'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<li class="cat-item(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 39 - 39: OoooooooOO + o00oo % iI1 / iI1
 for oO0Oo in I11i1I1I :
  OO00Oo = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  oO0o0OOOO = re . compile ( 'title.+?">(.+?)</a>' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  IiII = 'https://www.dropbox.com/s/2b0j135ip39g89p/Movies.png?dl=1'
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 50 , IiII , iI111iI , '' )
  if 27 - 27: I1iiiiI1iII . OoOooOOOO . iIii1I11I1II1 . iIii1I11I1II1
def iIi1i ( url ) :
 if 4 - 4: oO / i11iIiiIii / iI1
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="item">(.+?)<span class="player">' , re . DOTALL ) . findall ( o0O0O00 )
 if 91 - 91: iIii1I11I1II1 % o0oOOo0O0Ooo . iIii1I11I1II1 % i1IIi / II111iiii * OoOoOO00
 for oO0Oo in I11i1I1I :
  try :
   url = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . split ( "Full" ) [ 0 ]
   oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , url , 51 , IiII , iI111iI , '' )
  except : pass
  if 10 - 10: II111iiii . I1iiiiI1iII
 try :
  iI1I = re . compile ( '<div class="nav-previous alignleft"><a href="(.+?)" ></a>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iI1I , 50 , IiII , iI111iI , '' )
 except : pass
 if 32 - 32: OoOO . iIii1 . OoooooooOO - OoO0O00 + o00oo
def ooO0oO00O0o ( url ) :
 if 70 - 70: oO
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
  if 16 - 16: I1iiiiI1iII - OoooooooOO % Oo0Ooo
def i11i1iIiii ( ) :
 if 71 - 71: I1ii11iIi11i % O0OOooO - I1IiiI % OoOooOOOO - O0
 OO00Oo = "http://www.afdah.bz/"
 o0O0O00 = o000o ( OO00Oo )
 OOo = re . compile ( '<li class="cat-item.+?<a href="(.+?)" >(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for OO00Oo , oO0o0OOOO in sorted ( OOo ) :
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 53 , IiII , iI111iI , '' )
  if 67 - 67: iI1 + Oo0Ooo
def OoOo000oOo0oo ( url ) :
 if 65 - 65: OoOoOO00 / OoO0O00 % iIii1
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="movie-preview-content">(.+?)Views</small>' , re . DOTALL ) . findall ( o0O0O00 )
 if 45 - 45: OoOoOO00
 for oO0Oo in sorted ( I11i1I1I , reverse = True ) :
  if not "<i class" in oO0Oo :
   i11i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = re . compile ( 'alt="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
   oO0o0OOOO = oO0o0OOOO . replace ( "Afdah" , "" )
   oO0o0OOOO = iii11 ( oO0o0OOOO )
   ooo0o00 = re . compile ( 'src="(.+?)"' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  try :
   i1i1IIii1i1 = re . compile ( 'title=.+?Quality">(.+?)<' , re . DOTALL ) . findall ( oO0Oo ) [ 0 ]
  except : i1i1IIii1i1 = "Unknown"
  oO0 ( "[COLOR lime]" + oO0o0OOOO + 'Quality = ' "[/COLOR]" "[COLOR yellow]" + i1i1IIii1i1 + "[/COLOR]" , i11i1I1 , 54 , ooo0o00 , iI111iI , '' )
  if 66 - 66: OoO0O00
 try :
  iI1I = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iI1I , 53 , IiII , iI111iI , '' )
 except : pass
 if 56 - 56: O0
def OOo00 ( url ) :
 if 37 - 37: i1IIi
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
  if 46 - 46: OoOoOO00 - OoOooOOOO - OoOO . i1IIi
def IiI1iii11iIi1 ( ) :
 if 40 - 40: OoOooOOOO % OoO0O00 . oO
 ii11i11i1 = ''
 OOO0oOOo00O = xbmc . Keyboard ( ii11i11i1 , 'Search For A Movie' )
 OOO0oOOo00O . doModal ( )
 if OOO0oOOo00O . isConfirmed ( ) :
  OO0o = OOO0oOOo00O . getText ( )
  III111i11IiI = OO0o
  ii11i11i1 = OO0o . replace ( ' ' , '+' )
  if not len ( ii11i11i1 ) > 1 :
   I11 . ok ( "STREAM ARMY" , "No search term was entered." )
   quit ( )
   if 71 - 71: OoOooOOOO / OoOooOOOO * o00oo * o00oo / II111iiii
  ii11i11i1 = ii11i11i1 . replace ( ' ' , '+' )
  OO00Oo = "http://housemovie.to/search?q=" + ii11i11i1
  o0O0O00 = o000o ( OO00Oo )
  I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
  if 35 - 35: iI1 * o0oOOo0O0Ooo * I1IiiI % Oo0Ooo . OoOoOO00
  for iIi in I11i1I1I :
   try :
    oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( iIi ) [ 0 ]
    OO00Oo = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( iIi ) [ 0 ]
    O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
    try :
     O00o00O = re . compile ( '<span class="imdb">(.+?)</span>' ) . findall ( iIi ) [ 0 ]
    except : O00o00O = "IMDB Rating Unknown"
    if not "http" in OO00Oo :
     OO00Oo = "http://housemovie.to" + OO00Oo
     oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR] - [COLOR yellow][I]" + O00o00O + "[/I][/COLOR]" , OO00Oo , 21 , O0O0OoOO0 , iI111iI , '' )
   except : pass
   if 3 - 3: iI1
def Iii ( url ) :
 if 84 - 84: OoOO / I1iiiiI1iII . iIii1 . iIii1 % OoOooOOOO
 o0O0O00 = o000o ( url )
 if 57 - 57: OoOO % II111iiii
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 67 - 67: O0OOooO + I1IiiI * i11iIiiIii - o00oo / iIii1 % I1iiiiI1iII
 for IIi1i11111 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   i11i1I1 = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   if "genres" in i11i1I1 :
    i11i1I1 = "http://housemovie.to" + i11i1I1
    iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11i1I1 , 19 , IiII , iI111iI , '' )
  except : pass
  if 92 - 92: OoOO - o00oo - O0OOooO % OoooooooOO / iI1
def iIIIiIii ( url ) :
 if 71 - 71: OoooooooOO
 o0O0O00 = o000o ( url )
 if 33 - 33: oO
 I11i1I1I = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 62 - 62: I1ii11iIi11i + OoOO + i1IIi / OoooooooOO
 for IIi1i11111 in I11i1I1I :
  try :
   oO0o0OOOO = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   O00o00O = re . compile ( 'imdb">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   if "(SOON)" in oO0o0OOOO :
    IIiiii = oO0o0OOOO . split ( "(SOON)" ) [ 0 ]
    oO0o0OOOO = IIiiii . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
   else : oO0o0OOOO = oO0o0OOOO . title ( )
   i11i1I1 = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( IIi1i11111 ) [ 0 ]
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   if "watch" in i11i1I1 :
    i11i1I1 = "http://housemovie.to" + i11i1I1
    oO0 ( "[COLOR lime]" + oO0o0OOOO + " [/COLOR]-[COLOR yellow][I] " + O00o00O + "[/I][/COLOR]" , i11i1I1 , 21 , O0O0OoOO0 , iI111iI , '' )
    if 37 - 37: o0oOOo0O0Ooo % O0OOooO
  except : pass
  if 83 - 83: iI1 . oO + o00oo - iI1 * oO / oO
def I11I1 ( name , url , iconimage ) :
 if 45 - 45: iIii1
 Ii1Iii111IiI1 = [ ]
 O00oOooo0 = [ ]
 OoOOiIII1I1i1i = [ ]
 o0OIIiI1I1 = [ ]
 I11I1IIiiII1 = [ ]
 if 31 - 31: I1IiiI * o00oo + OoooooooOO - I1iiiiI1iII / OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 19 - 19: iIii1 * O0OOooO * o0oOOo0O0Ooo + O0 / O0
 I11i1I1I = re . compile ( '<div class="fig_holder">(.+?)</div>' ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  name = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
  i11i1I1 = re . compile ( '<a href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  iconimage = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  try :
   O00o00O = re . compile ( 'imdb">(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
  except : O00o00O = "0.0"
  if "imdb" in O00o00O . lower ( ) :
   O00o00O = O00o00O . replace ( "IMDB: " , "" ) . replace ( " " , "" )
  if not "." in O00o00O :
   O00o00O = O00o00O + ".0"
   if 73 - 73: iIii1I11I1II1 / iIii1I11I1II1 - o00oo
  if "(SOON)" in name :
   IIiiii = name . split ( "(SOON)" ) [ 0 ]
   name = IIiiii . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
  else : name = name . title ( )
  i11i1I1 = "http://housemovie.to" + i11i1I1
  if 91 - 91: o00oo + I1IiiI
  Ii1Iii111IiI1 . append ( name )
  O00oOooo0 . append ( i11i1I1 )
  OoOOiIII1I1i1i . append ( iconimage )
  o0OIIiI1I1 . append ( O00o00O )
  I11I1IIiiII1 = list ( zip ( o0OIIiI1I1 , Ii1Iii111IiI1 , O00oOooo0 , OoOOiIII1I1i1i ) )
  if 59 - 59: I1IiiI + i11iIiiIii + i1IIi / OoOooOOOO
 I11iIiI1 = sorted ( I11I1IIiiII1 , reverse = True )
 if 86 - 86: o0oOOo0O0Ooo
 for O00o00O , name , i11i1I1 , iconimage in I11iIiI1 :
  if O00o00O == "0.0" :
   O00o00O = "IMDB Rating Unknown"
  else : O00o00O = "IMDB: " + O00o00O
  oO0 ( "[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + O00o00O + "[/I][/COLOR]" , i11i1I1 , 21 , iconimage , iI111iI , '' )
  if 27 - 27: O0 . o0oOOo0O0Ooo . I1ii11iIi11i . I1ii11iIi11i + I1ii11iIi11i * o0oOOo0O0Ooo
 try :
  oOo00oOOOOO = re . compile ( '<a href="([^"]*)" class="page_next">Next</a>' ) . findall ( o0O0O00 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , oOo00oOOOOO , 19 , IiII , iI111iI , '' )
 except : pass
 if 85 - 85: OoooooooOO - OoO0O00 - oO / O0OOooO - OoOooOOOO
def iIiI ( name , url , iconimage ) :
 if 5 - 5: Oo0Ooo * OoOoOO00
 iII11 = [ ]
 O0oO0 = [ ]
 iiIiii1IIIII = [ ]
 if 46 - 46: O0OOooO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 33 - 33: I1iiiiI1iII - II111iiii * OoooooooOO - Oo0Ooo - iI1
 IIi1i11111 = re . compile ( '<div class="md_full_cell">(.+?)</div>' ) . findall ( o0O0O00 )
 if 84 - 84: oO + Oo0Ooo - OoOoOO00 * OoOoOO00
 for o00o in IIi1i11111 :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( o00o ) [ 0 ]
   oO0oO0 = re . compile ( 'rel="nofollow">(.+?)</a>' ) . findall ( o00o ) [ 0 ]
   url = "http://housemovie.to" + url
   for Ooo in oo0o0O00 :
    if Ooo . lower ( ) in oO0oO0 . lower ( ) :
     if 65 - 65: Oo0Ooo / OoOooOOOO
     iII11 . append ( oO0oO0 )
     O0oO0 . append ( url )
     iiIiii1IIIII . append ( iconimage )
  except : pass
  if 12 - 12: OoOooOOOO % OoOoOO00
  if 48 - 48: I1iiiiI1iII . i11iIiiIii
 name = '[COLOR lime]' + name + '[/COLOR]'
 i11II1I11I1 = I11 . select ( name , iII11 )
 if i11II1I11I1 < 0 :
  quit ( )
 else :
  url = O0oO0 [ i11II1I11I1 ]
  url = str ( url )
  IiII = iiIiii1IIIII [ i11II1I11I1 ]
  IiII = str ( IiII )
  if 5 - 5: o00oo . I1ii11iIi11i . II111iiii . OoooooooOO
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 96 - 96: i11iIiiIii - iI1 % O0 / OoO0O00
  url = re . compile ( '<a href="([^"]*)" target="_blank" class="button_type_1">' ) . findall ( o0O0O00 ) [ 0 ]
  if 100 - 100: I1iiiiI1iII / OoOO - OoooooooOO % II111iiii - I1IiiI % OoOoOO00
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
   if 60 - 60: iIii1I11I1II1 + i1IIi
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - OoOO
def ooO000O ( url ) :
 if 53 - 53: o0oOOo0O0Ooo . I1iiiiI1iII / OoOO
 url = 'http://cmovieshd.com/library/'
 o0O0O00 = o000o ( url )
 if 39 - 39: OoOO % O0 % OoOoOO00 . i1IIi
 I11i1I1I = re . compile ( '<div class="movies-letter">(.+?)<div class="clearfix">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 oOo00OooO0oO = re . compile ( '<a(.+?)</a>' , re . DOTALL ) . findall ( I11i1I1I )
 for IIi1i11111 in oOo00OooO0oO :
  i11i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  I1IIi = re . compile ( 'href=".+?">(.+?)' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ] . replace ( '0' , '0-9' )
  iiiI1I11i1 ( "[COLOR lime]" + I1IIi + "[/COLOR]" , i11i1I1 , 63 , IiII , iI111iI , '' )
  if 69 - 69: OoOO + Oo0Ooo + II111iiii - I1IiiI / OoOooOOOO
def O0O0ooOOO ( url ) :
 if 70 - 70: O0OOooO . O0 . oO . O0 + i1IIi
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '\r' , '' )
 if 9 - 9: Oo0Ooo
 I11i1I1I = re . compile ( '<td class="mlnh-thumb">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  O0O00OOo = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  oO0oO0 = re . compile ( 'title="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , O0O00OOo , 53 , IiII , iI111iI , '' )
 try :
  oOo00oOOOOO = re . compile ( 'class="next"><a href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  I11 . ok ( "22" , str ( oOo00oOOOOO ) )
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , oOo00oOOOOO , 63 , IiII , iI111iI , '' )
 except : pass
 if 66 - 66: i11iIiiIii / o0oOOo0O0Ooo - OoooooooOO / i1IIi . i11iIiiIii
 if 16 - 16: Oo0Ooo % I1ii11iIi11i + OoOooOOOO - O0 . I1iiiiI1iII / oO
 if 35 - 35: o00oo / oO / II111iiii - iIii1I11I1II1 + II111iiii . oO
 if 81 - 81: I1iiiiI1iII * iI1 - I1ii11iIi11i * OoOO % OoOoOO00 * OoOoOO00
 if 59 - 59: iIii1I11I1II1
 if 7 - 7: iI1 * I1IiiI / o0oOOo0O0Ooo * i11iIiiIii
 if 84 - 84: iI1 . I1iiiiI1iII
def II1i111 ( url ) :
 if 50 - 50: iIii1 % i1IIi
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<a class="site_tag(.+?)/a>' ) . findall ( o0O0O00 )
 if 21 - 21: OoooooooOO - iIii1I11I1II1
 for o0O0O00 in I11i1I1I :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
  oO0o0OOOO = re . compile ( '/i>(.+?)<' ) . findall ( o0O0O00 ) [ 0 ]
  i11i1I1 = "http://xoxfuck.com" + url
  iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , i11i1I1 , 17 , IiII , iI111iI , '' )
  if 93 - 93: o00oo - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - O0OOooO
def O00ooOo ( ) :
 if 80 - 80: o0oOOo0O0Ooo - iI1 + OoooooooOO
 OO00Oo = 'http://www.pornhd.com/category'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '&amp;' , 'and' )
 I11i1I1I = re . compile ( '<ul class="tag-150-list">(.+?)<div class="footer-zone">' , re . DOTALL ) . findall ( o0O0O00 )
 OOo = re . compile ( '<li class="category">(.+?)</span>' , re . DOTALL ) . findall ( o0O0O00 )
 if 98 - 98: iI1 + i1IIi . I1IiiI - II111iiii - o0oOOo0O0Ooo
 for IIi1i11111 in OOo :
  ooo0o00 = re . compile ( 'data-original="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  oO0o0OOOO = re . compile ( 'alt="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  I1IIi = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  if not 'http' in I1IIi :
   iIiiii = 'http://www.pornhd.com' + I1IIi
   iiiI1I11i1 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , iIiiii , 42 , ooo0o00 , iI111iI , '' )
   if 24 - 24: Oo0Ooo - i1IIi + OoOooOOOO
def IiiIi ( url ) :
 if 10 - 10: OoO0O00 / Oo0Ooo
 I1i = url
 i1i1II = 0
 try :
  o0O , url = url . split ( '|' )
  if 50 - 50: o0oOOo0O0Ooo * OoOO % I1ii11iIi11i / Oo0Ooo - O0 % I1iiiiI1iII
 except : i1i1II = 1
 iI1i11Iiii = o000o ( url )
 if 48 - 48: I1IiiI + I1ii11iIi11i + II111iiii * i11iIiiIii
 I11i1I1I = re . compile ( '<section id="pageContent"(.+?)<div class="pager paging">' , re . DOTALL ) . findall ( iI1i11Iiii )
 OOo = re . compile ( '<a class="thumb"(.+?)<span class="add-to">' , re . DOTALL ) . findall ( iI1i11Iiii )
 if 13 - 13: OoooooooOO * o00oo - OoOO / iI1 + OoOooOOOO + iIii1
 if 39 - 39: iIii1I11I1II1 - OoooooooOO
 if 81 - 81: I1ii11iIi11i - O0 * OoooooooOO
 if 23 - 23: II111iiii / o00oo
 for IIi1i11111 in OOo :
  try :
   oO0oO0 = re . compile ( '<img alt="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if 28 - 28: Oo0Ooo * O0OOooO - OoO0O00
   if 19 - 19: OoOooOOOO
   Ooooo0OoO0 = re . compile ( '<time>(.+?)</time>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if 9 - 9: iI1 . iIii1
   O0O0OoOO0 = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   if 31 - 31: o00oo / iIii1I11I1II1
   if not "http" in O0O0OoOO0 :
    O0O0OoOO0 = re . compile ( 'data-original="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
    if 84 - 84: iI1
    if 87 - 87: O0OOooO + o0oOOo0O0Ooo
   o0O0O00 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
   if not 'http' in o0O0O00 :
    iIiiii = 'http://www.pornhd.com' + o0O0O00
    iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" "[COLOR red]" " :: Video Length :: " + Ooooo0OoO0 + "[/COLOR]" , iIiiii , 43 , O0O0OoOO0 , iI111iI , '' )
  except : pass
  if 28 - 28: iI1 * I1ii11iIi11i / o00oo
  if 64 - 64: o00oo - I1IiiI / I1iiiiI1iII - OoO0O00
 if i1i1II == 1 :
  try :
   ii11I = ""
   if not "=" in I1i :
    I1i = I1i + "?page=1"
    o0O , O00oO = I1i . split ( "=" )
    O0ooooo0OOOO0 = int ( O00oO ) + 1
    ii11I = o0O + "=" + str ( O0ooooo0OOOO0 )
    if 47 - 47: oO
    iiiI1I11i1 ( '[COLOR red]Next Page >>[/COLOR]' , ii11I , 42 , IiII , Iii1ii1II11i )
    if 95 - 95: OoO0O00 . i1IIi / i11iIiiIii
  except : pass
  if 38 - 38: Oo0Ooo - OoOooOOOO . Oo0Ooo
def ii1111i ( url , icon , fanart ) :
 if 75 - 75: iIii1 + II111iiii / o00oo - o00oo / OoooooooOO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( 'sources.+?{(.+?)}' , re . DOTALL ) . findall ( o0O0O00 )
 o0O = str ( I11i1I1I )
 I11i1I1I = o0O . replace ( '\\' , '' )
 iiii11ii = re . compile ( "720.+?'.+?'(.+?)'," ) . findall ( I11i1I1I ) [ 0 ]
 i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
 if 50 - 50: OoOO / OoOoOO00 * OoOO
 xbmc . Player ( ) . play ( iiii11ii , i11i1 , False )
 if 34 - 34: O0 * O0 % OoooooooOO + I1iiiiI1iII * iIii1I11I1II1 % OoOO
 quit ( 0 )
 if 25 - 25: OoOooOOOO + OoOoOO00 . o0oOOo0O0Ooo % OoOoOO00 * iI1
def ii1IiIi11 ( name , url , iconimage ) :
 if 22 - 22: o00oo
 ii1ii = name . split ( '(' ) [ 1 ]
 ii1ii = ii1ii . replace ( ')' , '' ) . replace ( "[/COLOR]" , '' )
 ii1ii = int ( ii1ii )
 oOoooO00O = url
 if 6 - 6: OoOO % i1IIi . OoOO * OoOO
 o0Oo = 0
 oo0ooO0 = 1
 IIi11i1i1iI1 = 0
 IIiiiiIiIIii = 6
 if 86 - 86: OoOooOOOO / o0oOOo0O0Ooo - o0oOOo0O0Ooo + I1ii11iIi11i + o00oo
 Oo0o0000o0o0 . create ( "STREAM ARMY" , "[COLOR lime]Getting video 1 of " + str ( ii1ii ) + "![/COLOR]" )
 Oo0o0000o0o0 . update ( 0 )
 while oo0ooO0 < 2000 :
  if 33 - 33: o0oOOo0O0Ooo . I1iiiiI1iII . iIii1 . i1IIi
  if IIi11i1i1iI1 == 0 :
   o0O0O00 = o000o ( oOoooO00O )
   if 49 - 49: I1ii11iIi11i
   I11i1I1I = re . compile ( '<div class="inner_block video_box">(.+?)</a>' ) . findall ( o0O0O00 )
   for iIi in I11i1I1I :
    i11i1I1 = re . compile ( 'href="(.+?)">' ) . findall ( iIi ) [ 0 ]
    name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( iIi ) [ 0 ]
    iconimage = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
    o0Oo = o0Oo + 1
    O0oOOo0o = 100 * int ( o0Oo ) / int ( ii1ii )
    Oo0o0000o0o0 . update ( O0oOOo0o , "[COLOR lime]Getting video " + str ( o0Oo ) + " of " + str ( ii1ii ) + "![/COLOR]" )
    oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , i11i1I1 , 18 , iconimage , iI111iI , '' )
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  else :
   url = oOoooO00O + '?load_more=10&loaded=' + str ( IIiiiiIiIIii )
   o0O0O00 = o000o ( url )
   o0O0O00 = o0O0O00 . replace ( '\\' , '' )
   if 50 - 50: I1iiiiI1iII . I1ii11iIi11i . OoO0O00 * OoOooOOOO + II111iiii % i11iIiiIii
   if "no_more_videos" in o0O0O00 :
    oo0ooO0 = 2001
    if 8 - 8: O0OOooO * O0
   I11i1I1I = re . compile ( '<div class="(.+?)</a>' ) . findall ( o0O0O00 )
   for iIi in I11i1I1I :
    if oo0ooO0 < 2000 :
     i11i1I1 = re . compile ( 'href="(.+?)">' ) . findall ( iIi ) [ 0 ]
     name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( iIi ) [ 0 ]
     iconimage = re . compile ( 'src="(.+?)"' ) . findall ( iIi ) [ 0 ]
     o0Oo = o0Oo + 1
     O0oOOo0o = 100 * int ( o0Oo ) / int ( ii1ii )
     Oo0o0000o0o0 . update ( O0oOOo0o , "[COLOR lime]Getting video " + str ( o0Oo ) + " of " + str ( ii1ii ) + "![/COLOR]" )
     oO0 ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , i11i1I1 , 18 , iconimage , iI111iI , '' )
   IIiiiiIiIIii = IIiiiiIiIIii + 10
  oo0ooO0 = oo0ooO0 + 1
 Oo0o0000o0o0 . close
 if 73 - 73: o0oOOo0O0Ooo / o00oo / OoOooOOOO / OoO0O00
def III1ii ( ) :
 if 41 - 41: O0OOooO . Oo0Ooo + I1IiiI
 OO00Oo = 'https://www.porn.com/categories'
 if 100 - 100: OoOO + OoO0O00
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="wrap grid categories">(.+?)<div class="listFilters listFiltersWide"' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<a class="thumbs" href="(.+?)" title="(.+?)"><img src="(.+?)"' ) . findall ( I11i1I1I )
 for O0O00OOo , oO0oO0 , Oo00o0OO in Ooo0o00o0o :
  if not 'http' in O0O00OOo :
   iIiiii = 'https://www.porn.com' + O0O00OOo
   iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , iIiiii , 66 , Oo00o0OO , iI111iI , '' )
   if 73 - 73: o0oOOo0O0Ooo - I1IiiI * i1IIi / i11iIiiIii * iI1 % II111iiii
def OooOoOOo0oO00 ( url ) :
 if 73 - 73: I1iiiiI1iII / I1ii11iIi11i % I1ii11iIi11i * OoOooOOOO / I1ii11iIi11i
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<ul class="listThumbs">(.+?)<div class="pager">' ) . findall ( o0O0O00 ) [ 0 ]
 OOo = re . compile ( '<img(.+?)<span class="added"' ) . findall ( I11i1I1I )
 for IIi1i11111 in OOo :
  try :
   iI1I11iIIi1 = re . compile ( '<a href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   Oo00o0OO = re . compile ( 'src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   oO0oO0 = re . compile ( 'class="title">(.+?)<' ) . findall ( IIi1i11111 ) [ 0 ]
   if not 'http' in iI1I11iIIi1 :
    iIIi1I = 'https://www.porn.com' + iI1I11iIIi1
    iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , iIIi1I , 67 , Oo00o0OO , iI111iI , '' )
  except : pass
  if 45 - 45: i1IIi - Oo0Ooo / O0 . I1ii11iIi11i
 try :
  oOo00oOOOOO = re . compile ( '<link rel="next" href="([^"]*)"' ) . findall ( o0O0O00 ) [ 0 ]
  if not 'http' in oOo00oOOOOO :
   iI1iIIiI1ii = 'https://www.porn.com' + oOo00oOOOOO
   iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , iI1iIIiI1ii , 66 , IiII , iI111iI , '' )
 except : pass
 if 78 - 78: O0 * iI1
def iIii1Ooo0oO0 ( url ) :
 if 86 - 86: O0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="dlRow">(.+?)<div class="bn">' ) . findall ( o0O0O00 ) [ 0 ]
 O0o0oOooOoOo = re . compile ( '<a href="(.+?)".+?</i>(.+?)<' ) . findall ( I11i1I1I )
 for I1iOo , i1i1IIii1i1 in O0o0oOooOoOo :
  if not 'http' in I1iOo :
   i11i1I1 = 'https://www.porn.com' + I1iOo
   if 'mp4' in i11i1I1 :
    oO0 ( i1i1IIii1i1 , i11i1I1 , 4 , O0O0OoOO0 , iI111iI , '' )
    if 29 - 29: O0 - i11iIiiIii - II111iiii + iI1 * iIii1
def IiI1ii1Ii ( name , url , iconimage ) :
 if 51 - 51: i11iIiiIii * o0oOOo0O0Ooo / I1IiiI
 iIiiii = o000o ( url )
 IIi1i11111 = re . compile ( '<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">' ) . findall ( iIiiii ) [ 0 ]
 oO0oO0 = re . compile ( '<title>(.+?)</title>' ) . findall ( iIiiii ) [ 0 ]
 oO0oO0 = oO0oO0 . split ( ' | ' ) [ 0 ]
 oO0oO0 = oO0oO0 . strip ( ' ' )
 i11i1 = xbmcgui . ListItem ( oO0oO0 , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( IIi1i11111 , i11i1 , False )
 if 40 - 40: I1IiiI
 if 36 - 36: O0OOooO / I1iiiiI1iII - iIii1 - iIii1
 if 82 - 82: I1ii11iIi11i
 if 29 - 29: iIii1
 if 66 - 66: Oo0Ooo
 if 97 - 97: i1IIi - OoooooooOO / oO * I1IiiI
 if 55 - 55: o0oOOo0O0Ooo . I1iiiiI1iII
def oOo00o00oO ( ) :
 OO00Oo = 'http://watchseries.cr/letters/A'
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '<a href="(.+?)".+?wpb_btn-small">(.+?)</a>' , re . DOTALL ) . findall ( o0O0O00 )
 O0O0OoOO0 = 'http://watchseries.cr/assets/wp-content/themes/Snaptube/images/new-logo.png'
 for o0O0O00 , oO0oO0 in I11i1I1I :
  if 'http' in o0O0O00 :
   iiiI1I11i1 ( oO0oO0 , o0O0O00 , 31 , O0O0OoOO0 , iI111iI , '' )
   if 95 - 95: I1IiiI
def O0OOO000o0o ( url ) :
 if 19 - 19: II111iiii - i1IIi - iI1 / iI1 + OoOoOO00
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<td><a style="font-size: 15px;" href="(.+?)">(.+?)</a></td>' , re . DOTALL ) . findall ( o0O0O00 )
 for o0O0O00 , oO0o0OOOO in I11i1I1I :
  iiiI1I11i1 ( oO0o0OOOO , o0O0O00 , 57 , O0O0OoOO0 , iI111iI , '' )
  if 51 - 51: Oo0Ooo % OoOoOO00 * OoooooooOO . i11iIiiIii
def oO000 ( url ) :
 if 7 - 7: iIii1 * I1IiiI + i1IIi + i11iIiiIii + Oo0Ooo % I1IiiI
 o0O0O00 = o000o ( url )
 ooo0o00 = re . compile ( '<img src="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 5 ]
 I11i1I1I = re . compile ( '<h2 class="video-module-title">(.+?)<a href="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
 for OO00OO0o0 , o0O0O00 in I11i1I1I :
  iiiI1I11i1 ( OO00OO0o0 , o0O0O00 , 58 , ooo0o00 , iI111iI , '' )
  if 52 - 52: I1ii11iIi11i % o00oo - i11iIiiIii
def i1III ( url ) :
 if 6 - 6: I1iiiiI1iII . OoOooOOOO + OoOO . oO
 o0O0O00 = o000o ( url )
 I11i1I1I = re . compile ( '<div class="vid_info">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  oO0oO0 = re . compile ( '</b>(.+?)</a>' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  iiiI1I11i1 ( oO0oO0 , url , 59 , O0O0OoOO0 , iI111iI , '' )
  if 70 - 70: OoO0O00
def i1iIi1111 ( url ) :
 if 13 - 13: OoO0O00
 o0O0O00 = o000o ( url )
 if 37 - 37: OoOO + oO - Oo0Ooo + OoOO
 I11i1I1I = re . compile ( '<td class="view_link">(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  Oo0o0Oo0O = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
  if 'watchseries' in Oo0o0Oo0O :
   iIiiii = o000o ( Oo0o0Oo0O )
   OOo = re . compile ( '<h1>(.+?)</a>' , re . DOTALL ) . findall ( iIiiii )
   if 63 - 63: iIii1I11I1II1
   for IIi1i11111 in OOo :
    II1Ii = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( IIi1i11111 ) [ 0 ]
    if 'daclips.in' in II1Ii :
     III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , II1Ii , 2 , O0O0OoOO0 , iI111iI , '' )
    elif 'vidzi.tv' in II1Ii :
     III1iII1I1ii ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , II1Ii , 2 , O0O0OoOO0 , iI111iI , '' )
     if 89 - 89: OoOoOO00 - OoO0O00
def IIIIoOo ( ) :
 if 86 - 86: II111iiii * i11iIiiIii * OoooooooOO + o00oo % iI1
 OO00Oo = 'http://sockshare.net/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div id="mainmenu2">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 I1IIi = re . compile ( '<a href="(.+?)"><img src="(.+?)">' , re . DOTALL ) . findall ( I11i1I1I )
 for O0O00OOo , Oo00o0OO in I1IIi :
  OOO0 = 0
  if not 'http' in I1IIi :
   I1ii11iI = [ 'genres' , 'countries' , 'years' , 'tv-series' , 'new-movies' , 'anime-series' ]
   for iIiIIi in I1ii11iI :
    if iIiIIi in O0O00OOo :
     OOO0 = 1
   if OOO0 == 0 :
    iIiiii = 'http://sockshare.net' + O0O00OOo
    III1I = 'http://sockshare.net' + Oo00o0OO
    if not iIiiii . endswith ( '/' ) :
     oO0oO0 = iIiiii . replace ( 'http://sockshare.net/' , '' ) . replace ( 'search-movies/2016' , 'New Releases' ) . replace ( 'new-movies' , 'Recently Added' ) . replace ( '.html' , '' ) . replace ( '-' , ' ' )
     oO0oO0 = oO0oO0 . title ( )
     OOO0 = 1
     iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , iIiiii , 61 , III1I , iI111iI , '' )
     if 11 - 11: O0OOooO - iI1 + O0OOooO * o00oo / I1IiiI
def OoOOOO ( url ) :
 if 18 - 18: O0OOooO % i11iIiiIii . iIii1I11I1II1 - I1iiiiI1iII
 OOOOoo = url
 if 29 - 29: o0oOOo0O0Ooo / i11iIiiIii / I1IiiI % o00oo % i11iIiiIii
 I1ii11iI = any ( i . isdigit ( ) for i in OOOOoo )
 if 18 - 18: iI1 + oO
 if 'http://sockshare.net/search-movies/2016.html' in url :
  OO0OO0O = url . replace ( '.html' , '' )
  ii11I = OO0OO0O + '/page-2.html'
  if 75 - 75: OoOooOOOO / o0oOOo0O0Ooo / iI1 / iIii1 % O0OOooO + II111iiii
 elif I1ii11iI == False :
  url = url . replace ( ".html" , "" )
  url = url + "/page-1.html"
  OOOOoo = url
  I1III111i = int ( filter ( str . isdigit , OOOOoo ) )
  oOo00oOOOOO = int ( I1III111i ) + 1
  if len ( str ( I1III111i ) ) == 1 :
   OOOOoo = OOOOoo [ : - 6 ]
  elif len ( str ( I1III111i ) ) == 2 :
   OOOOoo = OOOOoo [ : - 7 ]
  elif len ( str ( I1III111i ) ) == 3 :
   OOOOoo = OOOOoo [ : - 8 ]
  ii11I = OOOOoo + str ( oOo00oOOOOO ) + ".html"
 else :
  I1III111i = int ( filter ( str . isdigit , OOOOoo ) )
  oOo00oOOOOO = int ( I1III111i ) + 1
  if len ( str ( I1III111i ) ) == 1 :
   OOOOoo = OOOOoo [ : - 6 ]
  elif len ( str ( I1III111i ) ) == 2 :
   OOOOoo = OOOOoo [ : - 7 ]
  elif len ( str ( I1III111i ) ) == 3 :
   OOOOoo = OOOOoo [ : - 8 ]
  ii11I = OOOOoo + str ( oOo00oOOOOO ) + ".html"
  if 4 - 4: i1IIi + O0OOooO + i1IIi
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<li class="item">(.+?)/div>' ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  oO0oO0 = re . compile ( '<b>(.+?)</b>' ) . findall ( IIi1i11111 ) [ 0 ]
  iIiiii = re . compile ( 'href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  IiII = re . compile ( '<img src="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  iiiI1I11i1 ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , iIiiii , 64 , IiII , iI111iI , '' )
 try :
  if 31 - 31: OoOO
  iiiI1I11i1 ( "[COLOR red]Next Page -->[/COLOR]" , ii11I , 61 , IiII , iI111iI , '' )
 except : pass
 if 78 - 78: i11iIiiIii + o0oOOo0O0Ooo + oO / o0oOOo0O0Ooo % iIii1I11I1II1 % iIii1
def Oo0O0Oo00O ( url ) :
 if 9 - 9: o0oOOo0O0Ooo . I1IiiI - I1ii11iIi11i
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<p class="server_play">(.+?)</p>' ) . findall ( o0O0O00 )
 for IIi1i11111 in I11i1I1I :
  Oo0o0Oo0O = re . compile ( '<a href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
  if 'openload' in Oo0o0Oo0O :
   i11i1I1 = o000o ( Oo0o0Oo0O )
  elif 'vidto' in Oo0o0Oo0O :
   i11i1I1 = o000o ( Oo0o0Oo0O )
  try :
   IiiiI = re . compile ( 'Base64.decode.+?"(.+?)"' ) . findall ( i11i1I1 ) [ 0 ]
   iiIIi = base64 . decodestring ( IiiiI )
   II1Ii = re . compile ( 'src="(.+?)"' ) . findall ( iiIIi ) [ 0 ]
   oO0oO0 = II1Ii . replace ( 'https://' , '' ) . replace ( 'http://' , '' ) . replace ( '/' , '' ) . split ( '.' ) [ 0 ]
   oO0oO0 = oO0oO0 . title ( )
   if 'http' in II1Ii :
    III1iII1I1ii ( "[COLOR lime]" + oO0oO0 + "[/COLOR]" , II1Ii , 2 , O0O0OoOO0 , iI111iI , '' )
    if 36 - 36: OoOooOOOO . II111iiii
  except : pass
  if 25 - 25: o00oo
  if 34 - 34: OoOoOO00 . iIii1I11I1II1 % O0
def iI11Ii111 ( url ) :
 if 54 - 54: OoOoOO00 % I1iiiiI1iII . OoOoOO00 * iI1 + OoOoOO00 % i1IIi
 try :
  if not "http" in url :
   if "https://" in url :
    url = url . replace ( "https://" , "http://" )
   o0O0O00 = o000o ( url )
   oO0o0OOOO = re . compile ( '<title>(.+?)</title>' ) . findall ( o0O0O00 ) [ 0 ] . split ( ' (' ) [ 0 ]
   I1I1I11Ii = re . compile ( '<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">' ) . findall ( o0O0O00 )
   O0O0OoOO0 = re . compile ( '<meta property="og:image" content="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   if 48 - 48: OoooooooOO + o00oo % iIii1I11I1II1
   for url , oO0oO0 in I1I1I11Ii :
    oO0 ( oO0oO0 , url , 14 , O0O0OoOO0 , iI111iI , '' )
  else :
   o0O0O00 = o000o ( url )
   if 11 - 11: I1IiiI % OoOO - OoO0O00 - o00oo + o0oOOo0O0Ooo
   I11i1I1I = re . compile ( '<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>' ) . findall ( o0O0O00 ) [ 0 ]
   ii11i11i1 = str ( I11i1I1I )
   OOo = re . compile ( '<td width="100%" class="entry">(.+?)</td>' ) . findall ( ii11i11i1 )
   o0O0O0 = re . compile ( '<meta property="og:image" content="(.+?)"/>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   for iIi in OOo :
    oO0o0OOOO = re . compile ( 'title="(.+?)"' ) . findall ( iIi ) [ 0 ]
    url = re . compile ( '<a href="(.+?)"' ) . findall ( iIi ) [ 0 ]
    oO0oO0 = oO0o0OOOO . split ( ' - ' ) [ 1 ]
    if not 'http' in url : url = 'http:' + url
    oO0 ( "[COLOR lime]" + oO0o0OOOO . title ( ) + "[/COLOR]" , url , 14 , o0O0O0 , iI111iI , '' )
 except :
  I11 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
  if 55 - 55: O0 - oO
  if 58 - 58: OoOoOO00 - I1iiiiI1iII - OoooooooOO
  if 96 - 96: iIii1I11I1II1
  if 82 - 82: OoOoOO00 + O0 - iIii1 % o00oo * i11iIiiIii
  if 15 - 15: o0oOOo0O0Ooo
  if 39 - 39: iI1 / I1ii11iIi11i / I1IiiI * oO
  if 44 - 44: O0 + O0OOooO . iIii1I11I1II1 + Oo0Ooo / O0 - OoOooOOOO
def o0o0OoOOOOOo ( ) :
 if 39 - 39: OoooooooOO * iI1 * O0 . OoOooOOOO . OoO0O00 + O0OOooO
 OO00Oo = 'https://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
 if 9 - 9: OoOoOO00 + o00oo % OoooooooOO + o0oOOo0O0Ooo
 o0O0O00 = o000o ( OO00Oo )
 I11i1I1I = re . compile ( '{"start(.+?)}' ) . findall ( o0O0O00 )
 for iIi in I11i1I1I :
  if not 'event_status":""' in str ( iIi ) :
   ooOO0o = 1
  else : ooOO0o = 0
  oO0O0oO0 = re . compile ( 'date":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  I11Ii1iI11iI1 = re . compile ( 'competition_name":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  i1III1 = re . compile ( 'competition_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  Iii111IiIii = re . compile ( 'home_team":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  OooO0ooo0 = re . compile ( 'home_team_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  iIiIoO00Ooo0oO = re . compile ( 'home_team_slug":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  try :
   OOOo = re . compile ( 'event_status":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  except : OOOo = "null"
  o0ooOo00O = re . compile ( 'away_team":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  Ii1i1I1 = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  O0O00OooO = re . compile ( 'away_team_slug":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  I1IiI1iI11 = re . compile ( 'event_id":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  try :
   iIiii = re . compile ( 'game_minute":"(.+?)"' ) . findall ( iIi ) [ 0 ]
  except : iIiii = "null"
  O0O0o0oO0O00 = OooO0ooo0 . split ( "-" )
  o0O0oO0 = Ii1i1I1 . split ( "-" )
  Iii111IiIii = ""
  IIi11i1i1iI1 = 0
  for o0O in O0O0o0oO0O00 :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   Ooooo0OoO0 = len ( O0O0o0oO0O00 )
   if IIi11i1i1iI1 < Ooooo0OoO0 :
    Iii111IiIii = Iii111IiIii + " " + o0O
  o0ooOo00O = ""
  IIi11i1i1iI1 = 0
  for o0O in o0O0oO0 :
   IIi11i1i1iI1 = IIi11i1i1iI1 + 1
   Ooooo0OoO0 = len ( o0O0oO0 )
   if IIi11i1i1iI1 < Ooooo0OoO0 :
    o0ooOo00O = o0ooOo00O + " " + o0O
    if 77 - 77: O0 . OoOO
  oO0O0oO0 = oO0O0oO0 + "!"
  oO0O0oO0 , i1i1IiIi1 = oO0O0oO0 . split ( ' ' )
  i1i1IiIi1 = i1i1IiIi1 . replace ( ":00!" , "" )
  o0O , O00oO , O0ooooo0OOOO0 = oO0O0oO0 . split ( "-" )
  oO0O0oO0 = O0ooooo0OOOO0 + "-" + O00oO + "-" + o0O
  i1i1IiIi1 = "[COLOR red][B]" + i1i1IiIi1 + "[/B][/COLOR]"
  oO0O0oO0 = "[COLOR red][B]" + oO0O0oO0 + "[/B][/COLOR]"
  OO00Oo = 'https://soccerstreams.net/streams/' + I1IiI1iI11 + '/' + iIiIoO00Ooo0oO + '_vs_' + O0O00OooO
  oO0o0OOOO = '[COLOR lime][B]' + Iii111IiIii . title ( ) + ' vs ' + o0ooOo00O . title ( ) + '[/B][/COLOR]'
  OO00Oo = OO00Oo + "|SPLIT|" + oO0o0OOOO
  O0O0OoOO0 = 'https://soccerstreams.net/images/teams/' + OooO0ooo0
  if ooOO0o == 0 :
   oO0 ( i1i1IiIi1 + ' | ' + oO0o0OOOO + ' - ' + oO0O0oO0 + ' | [COLOR yellow]' + I11Ii1iI11iI1 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
  else :
   iIiii = iIiii . replace ( '&#039;' , "'" )
   oO0 ( "[COLOR red][B]" + iIiii + " " + OOOo + '[/B][/COLOR] | ' + oO0o0OOOO + ' - ' + oO0O0oO0 + ' | [COLOR yellow]' + I11Ii1iI11iI1 + '[/COLOR]' , OO00Oo , 56 , O0O0OoOO0 , iI111iI , '' )
   if 22 - 22: OoOooOOOO * O0 . II111iiii - OoO0O00
   if 90 - 90: o00oo
def O00OO ( name , url , iconimage ) :
 if 94 - 94: I1iiiiI1iII + OoOO % o0oOOo0O0Ooo
 I11 = xbmcgui . Dialog ( )
 if 1 - 1: OoOoOO00 % oO - iI1 + o00oo + O0 * o0oOOo0O0Ooo
 url , name = url . split ( "|SPLIT|" )
 o0OooOo = name
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 if 70 - 70: Oo0Ooo - o00oo . iIii1I11I1II1 % OoOooOOOO / OoOoOO00 - O0
 IIi11i1i1iI1 = 1
 IIiiiiIiIIii = 0
 iIiiii = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi1i11111 = re . compile ( '<tr class="(.+?)</tr>' , re . DOTALL ) . findall ( iIiiii )
 for o0O0oo0o in IIi1i11111 :
  url = re . compile ( 'data.+?="(.+?)"' ) . findall ( o0O0oo0o ) [ 0 ]
  O0oO0 . append ( url )
  iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
  IIi11i1i1iI1 = IIi11i1i1iI1 + 1
  if 12 - 12: OoOoOO00 % iIii1 % I1ii11iIi11i . i11iIiiIii * iIii1I11I1II1
 if IIi11i1i1iI1 == 1 :
  I11 . ok ( oO0o0o0ooO0oO , "Sorry no links found!" )
  quit ( )
  if 66 - 66: i11iIiiIii * iIii1I11I1II1 % OoooooooOO
 o0OooOo = '[COLOR mediumpurple]' + o0OooOo + '[/COLOR]'
 if 5 - 5: OoOoOO00 % OoooooooOO
 i11II1I11I1 = I11 . select ( o0OooOo , iII11 )
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
   if 60 - 60: OoOoOO00 . i1IIi % OoO0O00 % O0OOooO % iI1
def Ii111IIi ( ) :
 OO00Oo = 'http://mamahd.com/index.html'
 if 15 - 15: I1ii11iIi11i % oO + i11iIiiIii
 if 10 - 10: OoOO - OoOoOO00 . OoooooooOO . iI1 . OoO0O00 * I1iiiiI1iII
 if 78 - 78: o00oo / OoO0O00 - o00oo * OoooooooOO . OoOoOO00
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="standard row channels">(.+?)<div class="standard row">' ) . findall ( o0O0O00 ) [ 0 ]
 OOoooOoO0Oo = re . compile ( '<a href="(.+?)".+?<img src="(.+?)">.+?<span>(.+?)</span>' ) . findall ( I11i1I1I )
 for o0O0O00 , Oo00o0OO , oO0o0OOOO in OOoooOoO0Oo :
  OO00Oo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + o0O0O00 + '%26referer=no'
  oO0 ( "[COLOR lime]" + oO0o0OOOO + "[/COLOR]" , OO00Oo , 2 , Oo00o0OO , iI111iI , '' )
  if 78 - 78: OoooooooOO / iI1 % OoOoOO00 * OoooooooOO
  if 68 - 68: o00oo
def i11i11 ( url ) :
 if 18 - 18: iIii1I11I1II1 + OoOooOOOO * I1IiiI - iI1 / I1IiiI
 url = 'http://mamahd.com/index.html'
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I11i1I1I = re . compile ( '<div class="schedule">(.+?)<div id="pagination">' ) . findall ( o0O0O00 ) [ 0 ]
 o00iI1i1II = re . compile ( '<a(.+?)</a>' ) . findall ( I11i1I1I )
 for IIi1i11111 in o00iI1i1II :
  I1ii1ii1I = re . compile ( '<span class="day">(.+?)</span.+?span class="hours">(.+?)</span.+?span class="minutes">(.+?)</span.+?span class="seconds">(.+?)</span>' ) . findall ( IIi1i11111 )
  for iI1IIi11i1I1 , O00oo , OoOo0oO0o , o0OoOo00ooO in I1ii1ii1I :
   i111i = re . compile ( '<img src="(.+?)">' ) . findall ( IIi1i11111 ) [ 0 ]
   II1III1i1iiI = re . compile ( '<img src=".+?"><span>(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   I11i11i1 = re . compile ( '<div class="away cell">.+?<span>(.+?)</span>' ) . findall ( IIi1i11111 ) [ 0 ]
   OOO = re . compile ( 'href="(.+?)"' ) . findall ( IIi1i11111 ) [ 0 ]
   url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + OOO + '%26referer=no'
   oO0 ( "[COLOR lime]" + iI1IIi11i1I1 + "[/COLOR]" + "[COLOR lightseagreen]" + "-Days" + "[/COLOR]" + "  " + "[COLOR lime]" + O00oo + "[/COLOR]" + "[COLOR lightseagreen]" + "-Hours" + "[/COLOR]" + "  " + "[COLOR lime]" + OoOo0oO0o + "[/COLOR]" + "[COLOR lightseagreen]" + "-Minutes" + "[/COLOR]" + "   " + ":::" + "    " + "[COLOR yellow]" + II1III1i1iiI + "  " + "Vs" + "  " + I11i11i1 + "[/COLOR]" , url , 2 , i111i , iI111iI , '' )
   if 37 - 37: O0 - OoOooOOOO
def IiI1 ( ) :
 if 59 - 59: OoOooOOOO / Oo0Ooo / iI1 / O0 / OoOoOO00 + o0oOOo0O0Ooo
 OO00Oo = 'http://www.goalsarena.org/en/'
 o0O0O00 = o000o ( OO00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 I11i1I1I = re . compile ( '<div class="videos"(.+?)<div class="moduletable-none">' ) . findall ( o0O0O00 ) [ 0 ]
 Ooo0o00o0o = re . compile ( '<a title=".+?" href="(.+?)">(.+?)</a>' ) . findall ( I11i1I1I )
 if 13 - 13: o0oOOo0O0Ooo % o00oo / oO % oO % O0
 for O0O00OOo , o0 in Ooo0o00o0o :
  iiiI1I11i1 ( "[COLOR lime]" + o0 + "[/COLOR]" , O0O00OOo , 69 , IiII , iI111iI , '' )
  if 29 - 29: II111iiii . OoOoOO00 % o0oOOo0O0Ooo * II111iiii - o0oOOo0O0Ooo * iIii1I11I1II1
def iii1i1III ( url ) :
 if 65 - 65: iI1 - I1iiiiI1iII
 if 45 - 45: OoOO . OoooooooOO
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 if 27 - 27: OoOO * Oo0Ooo . OoOoOO00
 try :
  I11i1I1I = re . compile ( '<div id="videodetailsarea"(.+?)</div>' ) . findall ( o0O0O00 ) [ 0 ]
  OOo = re . compile ( '<script data-config="(.+?)"' ) . findall ( I11i1I1I ) [ 0 ]
  if not 'http' in OOo :
   Ii111Iiiii = 'http:' + ( OOo )
   iIii = o000o ( Ii111Iiiii )
   iii1IIiI = re . compile ( '"f4m":"(.+?)"' ) . findall ( iIii ) [ 0 ]
   i1i1Ii11Ii = o000o ( iii1IIiI )
   II1Ii = re . compile ( '<media url="(.+?)"' ) . findall ( i1i1Ii11Ii ) [ 2 ]
   i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
   xbmc . Player ( ) . play ( II1Ii , i11i1 , False )
   if 57 - 57: iI1 + oO % I1ii11iIi11i . OoO0O00 / OoO0O00 * O0
   if 6 - 6: i1IIi - II111iiii * o0oOOo0O0Ooo . OoO0O00
 except : pass
 quit ( 0 )
 if 68 - 68: o0oOOo0O0Ooo
 if 20 - 20: oO - oO
 if 37 - 37: iIii1
 if 37 - 37: Oo0Ooo / iIii1 * O0
 if 73 - 73: I1iiiiI1iII * I1iiiiI1iII / O0OOooO
 if 43 - 43: I1ii11iIi11i . i1IIi . iIii1 + O0 * OoOO * O0
 if 41 - 41: I1ii11iIi11i + OoOO % OoooooooOO . I1ii11iIi11i + I1iiiiI1iII . I1iiiiI1iII
 if 31 - 31: i11iIiiIii + II111iiii . I1iiiiI1iII * OoOoOO00
 if 66 - 66: OoOoOO00 + i1IIi % II111iiii . O0 * I1ii11iIi11i % I1ii11iIi11i
def O0oOO0o ( name , url , iconimage ) :
 if 6 - 6: iIii1I11I1II1 * OoooooooOO
 iconimage = "null"
 if 28 - 28: Oo0Ooo * o0oOOo0O0Ooo / oO
 IIi11i1i1iI1 = 0
 O0oO0 = [ ]
 iII11 = [ ]
 iiIiii1IIIII = [ ]
 if 52 - 52: O0 / o0oOOo0O0Ooo % I1iiiiI1iII * I1IiiI % iI1
 o0oOOOO0 = 1
 ii1I = 0
 if "http" in url :
  if 84 - 84: I1ii11iIi11i - iIii1I11I1II1 % O0 + I1iiiiI1iII
  Oo0o0000o0o0 . create ( "Stream Army" , "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]" )
  Oo0o0000o0o0 . update ( 0 )
  if 93 - 93: Oo0Ooo / iIii1 % I1ii11iIi11i
  while o0oOOOO0 < 11 :
   O0oOOo0o = 100 * int ( o0oOOOO0 ) / int ( 10 )
   Oo0o0000o0o0 . update ( O0oOOo0o , "" , "[COLOR lime]Connection attempt " + str ( o0oOOOO0 ) + " of 10[/COLOR]" )
   o0O0O00 = o000o ( url )
   if 77 - 77: i11iIiiIii % i1IIi % iIii1
   if ii1I == 0 :
    o0oOOOO0 = o0oOOOO0 + 1
    oO0oO0 = re . compile ( 'title="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
    oO0oO0 = oO0oO0 . split ( " - " ) [ 0 ]
    if 15 - 15: iIii1I11I1II1 . O0
    O0o0O = re . compile ( '<td class="entry">(.+?)target' ) . findall ( o0O0O00 )
    for o00o in O0o0O :
     ii111 = 1
     ooOo000OoO0o = len ( o00o )
     ooooo0O0 = 100 * int ( ii111 ) / int ( ooOo000OoO0o )
     Oo0o0000o0o0 . update ( ooooo0O0 , "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]" , "[COLOR lime]Filtering links " + str ( ii111 ) + " of " + str ( ooOo000OoO0o ) + " possible matches[/COLOR]" )
     if 10 - 10: OoOooOOOO - Oo0Ooo
     if not "putlocker.bypassed.info" in o00o :
      ooOOooo0ooo00 = re . compile ( '<a rel=".+?" href="(.+?)"' ) . findall ( o00o ) [ 0 ]
      IIi11i1i1iI1 = IIi11i1i1iI1 + 1
      iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
      O0oO0 . append ( ooOOooo0ooo00 )
      iiIiii1IIIII . append ( iconimage )
     ii1I = 1
     o0oOOOO0 = 12
     ii111 = ii111 + 1
     if 56 - 56: I1IiiI
   if Oo0o0000o0o0 . iscanceled ( ) :
    sys . exit ( )
   import time
   time . sleep ( 1 )
   o0oOOOO0 = o0oOOOO0 + 1
   if 12 - 12: I1IiiI - O0OOooO
 else :
  if 45 - 45: iIii1 / O0 / OoOoOO00 * iI1
  iIiiii = o000o ( url )
  IIi1i11111 = re . compile ( '<td class="entry">(.+?)</tr>' ) . findall ( iIiiii )
  if 18 - 18: iIii1I11I1II1 + iI1 + iIii1I11I1II1 . I1ii11iIi11i + oO . O0OOooO
  for o00o in IIi1i11111 :
   url = re . compile ( 'href="(.+?)"' ) . findall ( o00o ) [ 0 ]
   if not "putlocker.unblocked.ink" in url :
    IIi11i1i1iI1 = IIi11i1i1iI1 + 1
    iII11 . append ( "Link " + str ( IIi11i1i1iI1 ) )
    O0oO0 . append ( url )
    iiIiii1IIIII . append ( iconimage )
    if 7 - 7: I1ii11iIi11i + iIii1I11I1II1 * OoOooOOOO * OoOooOOOO / II111iiii - OoOO
    if 65 - 65: o00oo + OoOoOO00 + II111iiii
    if 77 - 77: II111iiii
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
   if 50 - 50: O0 . O0 . O0OOooO % Oo0Ooo
def ooo000oOO ( name , url , iconimage ) :
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = i11i1 )
 xbmc . Player ( ) . play ( url , i11i1 , False )
 if 87 - 87: OoOoOO00 % iIii1I11I1II1
def OOoOO0o0o0 ( name , url , iconimage ) :
 if 72 - 72: iI1 . iI1 - I1ii11iIi11i
 name = name . replace ( '  ' , '' )
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + IiII
 else : url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
 if 48 - 48: Oo0Ooo - O0OOooO + Oo0Ooo - I1IiiI * i11iIiiIii . I1iiiiI1iII
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
  if 35 - 35: iIii1 . O0 + Oo0Ooo + iI1 + i1IIi
def i11ii1ii11i ( name , url , iconimage ) :
 if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  Oo0O0OOO0o0O = url . split ( 'list=' ) [ 1 ]
  OOOOO0 = iiIIIII1i1iI + Oo0O0OOO0o0O + o0oO0
  iII11I1IiiIi = urllib2 . Request ( OOOOO0 )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   iI1I = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   OOOOO0 = oo00 + iI1I + o00 + Oo0O0OOO0o0O + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , OOOOO0 , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 79 - 79: II111iiii - O0OOooO . i1IIi + O0 % O0 * I1IiiI
  if 7 - 7: i1IIi + iI1 % I1iiiiI1iII / o0oOOo0O0Ooo + i1IIi
  if 41 - 41: OoOO + i11iIiiIii / iIii1 % I1ii11iIi11i
  if 22 - 22: OoOoOO00 % o0oOOo0O0Ooo * OoOO - I1ii11iIi11i + o0oOOo0O0Ooo - Oo0Ooo
  for name , iiIi1iiI1I in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + iiIi1iiI1I
   iconimage = 'https://i.ytimg.com/vi/' + iiIi1iiI1I + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     III1iII1I1ii ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 26 - 26: iIii1I11I1II1 + i1IIi / OoOoOO00 % I1ii11iIi11i
 if 'https://www.googleapis.com/youtube/v3' in url :
  Oo0O0OOO0o0O = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I11i1I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   iI1I = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   OOOOO0 = oo00 + iI1I + o00 + Oo0O0OOO0o0O + Oo0oO0ooo
   iiiI1I11i1 ( 'Next Page >>' , OOOOO0 , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 44 - 44: OoooooooOO . II111iiii . iI1 % OoooooooOO
  if 86 - 86: i11iIiiIii + O0 * iIii1 - OoO0O00 * iI1 + O0
  if 95 - 95: iIii1I11I1II1 . oO % I1iiiiI1iII - oO * II111iiii
  for name , iiIi1iiI1I in I11i1I1I :
   url = 'https://www.youtube.com/watch?v=' + iiIi1iiI1I
   iconimage = 'https://i.ytimg.com/vi/' + iiIi1iiI1I + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     III1iII1I1ii ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 89 - 89: I1iiiiI1iII . I1IiiI
     if 59 - 59: i1IIi % iIii1I11I1II1 + OoooooooOO
     if 97 - 97: I1ii11iIi11i / Oo0Ooo + oO
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 32 - 32: O0OOooO % oO * Oo0Ooo
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  i1II1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  i1II1 = liveresolver . resolve ( url )
 else : i1II1 = url
 i11i1 = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 i11i1 . setPath ( i1II1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11i1 )
 if 72 - 72: O0OOooO . I1iiiiI1iII - oO - OoOO % i1IIi
def oO0o00O0O0oo0 ( url ) :
 if 24 - 24: oO * o00oo
 try :
  oO0o0OOOO , url , O0O0OoOO0 = url . split ( "!SASPLIT!" )
  i11i1 = xbmcgui . ListItem ( oO0o0OOOO , iconImage = O0O0OoOO0 , thumbnailImage = O0O0OoOO0 )
  xbmc . Player ( ) . play ( url , i11i1 , False )
 except :
  xbmc . Player ( ) . play ( url )
  if 88 - 88: i11iIiiIii + I1iiiiI1iII * OoOoOO00 * I1iiiiI1iII + OoOooOOOO
def o000o ( url ) :
 try :
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  OO00OooO0OO . close ( )
  o0O0O00 = o0O0O00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 88 - 88: iI1 % Oo0Ooo - I1iiiiI1iII - OoOoOO00 % i11iIiiIii
  return o0O0O00
 except : quit ( )
 if 6 - 6: OoOO - OoO0O00 . I1IiiI - O0
def Oo0oOOo ( url ) :
 if 16 - 16: I1iiiiI1iII * I1iiiiI1iII % OoOO % I1IiiI
 if 48 - 48: iI1 / OoOO % OoO0O00 / iIii1 / oO
 try :
  iII11I1IiiIi = urllib2 . Request ( url )
  iII11I1IiiIi . add_header ( 'User-Agent' , 'obsession' )
  OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
  o0O0O00 = OO00OooO0OO . read ( )
  if 89 - 89: oO * o00oo
  Oo0oOOooO0o0O = o00O ( o0O0O00 )
  print "--------- decoded --------" , Oo0oOOooO0o0O
  OO00OooO0OO . close ( )
  Oo0oOOooO0o0O = Oo0oOOooO0o0O . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 92 - 92: iIii1I11I1II1 % OoooooooOO % iIii1
  return Oo0oOOooO0o0O
 except : quit ( )
 if 79 - 79: iIii1I11I1II1 + iIii1
def Oo0oO ( url ) :
 iII11I1IiiIi = urllib2 . Request ( url )
 iII11I1IiiIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 OO00OooO0OO = urllib2 . urlopen ( iII11I1IiiIi )
 o0O0O00 = OO00OooO0OO . read ( )
 OO00OooO0OO . close ( )
 if 61 - 61: iI1 / OoO0O00 + II111iiii . o00oo / Oo0Ooo * iI1
 return o0O0O00
 if 46 - 46: iIii1I11I1II1
def I111iiiii1 ( ) :
 OO0ooOoOO0OOo = [ ]
 OooOoooo0000 = sys . argv [ 2 ]
 if len ( OooOoooo0000 ) >= 2 :
  Ooo0OOoOoO0 = sys . argv [ 2 ]
  I1ii1i11i = Ooo0OOoOoO0 . replace ( '?' , '' )
  if ( Ooo0OOoOoO0 [ len ( Ooo0OOoOoO0 ) - 1 ] == '/' ) :
   Ooo0OOoOoO0 = Ooo0OOoOoO0 [ 0 : len ( Ooo0OOoOoO0 ) - 2 ]
  Oooooo0O00o = I1ii1i11i . split ( '&' )
  OO0ooOoOO0OOo = { }
  for IIi11i1i1iI1 in range ( len ( Oooooo0O00o ) ) :
   II11ii1 = { }
   II11ii1 = Oooooo0O00o [ IIi11i1i1iI1 ] . split ( '=' )
   if ( len ( II11ii1 ) ) == 2 :
    OO0ooOoOO0OOo [ II11ii1 [ 0 ] ] = II11ii1 [ 1 ]
 return OO0ooOoOO0OOo
 if 19 - 19: II111iiii - iIii1
def OOOOo000o00OO ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 Oo0 = name . partition ( '(' )
 oOo0O0o000Ooo = ""
 oooo00o0 = ""
 if len ( Oo0 ) > 0 :
  oOo0O0o000Ooo = Oo0 [ 0 ]
  oooo00o0 = Oo0 [ 2 ] . partition ( ')' )
 if len ( oooo00o0 ) > 0 :
  oooo00o0 = oooo00o0 [ 0 ]
 I1IiII1iI1 = metahandlers . MetaData ( )
 OoO0o = I1IiII1iI1 . get_meta ( 'movie' , name = oOo0O0o000Ooo , year = oooo00o0 )
 oOOO00OOOoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = OoO0o [ 'cover_url' ] , thumbnailImage = OoO0o [ 'cover_url' ] )
 i11i1 . setInfo ( type = "Video" , infoLabels = OoO0o )
 III = [ ]
 III . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i11i1 . addContextMenuItems ( III , replaceItems = False )
 if not OoO0o [ 'backdrop_url' ] == '' : i11i1 . setProperty ( 'fanart_image' , OoO0o [ 'backdrop_url' ] )
 else : i11i1 . setProperty ( 'fanart_image' , Iii1ii1II11i )
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO00OOOoOO , listitem = i11i1 , isFolder = isFolder , totalItems = itemcount )
 return iI1iI1IiIIiI
 if 53 - 53: oO + OoOoOO00
def iiiI1I11i1 ( name , url , mode , iconimage , fanart , description = '' ) :
 oOOO00OOOoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : oOOO00OOOoOO = url
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO00OOOoOO , listitem = i11i1 , isFolder = True )
 return iI1iI1IiIIiI
 if 15 - 15: oO
def oO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 oOOO00OOOoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO00OOOoOO , listitem = i11i1 , isFolder = False )
 return iI1iI1IiIIiI
 if 85 - 85: i11iIiiIii / i11iIiiIii . OoO0O00 . O0
def III1iII1I1ii ( name , url , mode , iconimage , fanart , description = '' ) :
 if 67 - 67: II111iiii / o0oOOo0O0Ooo . iI1 . OoooooooOO
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 oOOO00OOOoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  i11i1 . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : oOOO00OOOoOO = url
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO00OOOoOO , listitem = i11i1 , isFolder = False )
 return iI1iI1IiIIiI
 if 19 - 19: iIii1 . I1ii11iIi11i / OoOoOO00
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 68 - 68: O0OOooO / OoooooooOO * OoOooOOOO / o00oo
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 oOOO00OOOoOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 iI1iI1IiIIiI = True
 i11i1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i11i1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i11i1 . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  i11i1 . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : oOOO00OOOoOO = url
 iI1iI1IiIIiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOO00OOOoOO , listitem = i11i1 , isFolder = False )
 return iI1iI1IiIIiI
 if 88 - 88: o0oOOo0O0Ooo
def iI11 ( url ) :
 if 97 - 97: o00oo + Oo0Ooo * iI1 % Oo0Ooo
 ii = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( ii )
 sys . exit ( 1 )
 if 2 - 2: i1IIi * o00oo - o00oo + OoooooooOO % OoOoOO00 / OoOoOO00
def i11IiI1iiI11 ( text , pattern ) :
 if 85 - 85: I1ii11iIi11i - OoOoOO00 / I1ii11iIi11i + iI1 - I1iiiiI1iII
 iI1i11Iiii = ""
 try :
  IIii1III = re . findall ( pattern , text , flags = re . DOTALL )
  iI1i11Iiii = IIii1III [ 0 ]
 except :
  iI1i11Iiii = ""
  if 94 - 94: i11iIiiIii % OoooooooOO / I1IiiI
 return iI1i11Iiii
 if 24 - 24: I1IiiI * o00oo
def oooO ( str ) :
 if 85 - 85: II111iiii . O0OOooO % iI1 % OoOooOOOO
 try :
  import chardet
  str = str . decode ( chardet . detect ( str ) [ "encoding" ] ) . encode ( "utf-8" )
 except :
  try :
   str = str . encode ( "utf-8" )
  except :
   pass
 return str
 if 80 - 80: o00oo * OoOooOOOO / iIii1I11I1II1 % o00oo / iIii1I11I1II1
def IIiIi1iI ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 Iiii1 = xbmcgui . Window ( id )
 i1iiIIiiiII = 50
 while ( i1iiIIiiiII > 0 ) :
  try :
   xbmc . sleep ( 10 )
   i1iiIIiiiII -= 1
   Iiii1 . getControl ( 1 ) . setLabel ( heading )
   Iiii1 . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 5 - 5: OoooooooOO / o0oOOo0O0Ooo % OoOooOOOO % OoO0O00 * I1iiiiI1iII + iIii1I11I1II1
def I11iiI11iiI ( link ) :
 try :
  I11i1I1I = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 51 - 51: o00oo . iIii1I11I1II1 + OoO0O00 * OoOO + i1IIi
def iIIi1i1 ( ) :
 if 81 - 81: O0 - OoOO + Oo0Ooo
 OooO0 = xbmc . getInfoLabel ( "System.BuildVersion" )
 II11iiii1Ii = float ( OooO0 [ : 4 ] )
 if 67 - 67: OoOO
 if II11iiii1Ii >= 1.0 and II11iiii1Ii <= 16.9 :
  iIII11Iiii1 = 'Jarvis'
 elif II11iiii1Ii >= 17.0 and II11iiii1Ii <= 17.9 :
  iIII11Iiii1 = 'Krypton'
  if 95 - 95: I1IiiI
 if iIII11Iiii1 == "Jarvis" :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 elif iIII11Iiii1 == "Krypton" :
  xbmc . executebuiltin ( 'Container.SetViewMode(55)' )
 else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 99 - 99: O0
Ooo0OOoOoO0 = I111iiiii1 ( ) ; OO00Oo = None ; oO0o0OOOO = None ; O0oO0OOoO = None ; O00ooOOoO0O000O = None ; O0O0OoOO0 = None
try : O00ooOOoO0O000O = urllib . unquote_plus ( Ooo0OOoOoO0 [ "site" ] )
except : pass
try : OO00Oo = urllib . unquote_plus ( Ooo0OOoOoO0 [ "url" ] )
except : pass
try : oO0o0OOOO = urllib . unquote_plus ( Ooo0OOoOoO0 [ "name" ] )
except : pass
try : O0oO0OOoO = int ( Ooo0OOoOoO0 [ "mode" ] )
except : pass
try : O0O0OoOO0 = urllib . unquote_plus ( Ooo0OOoOoO0 [ "iconimage" ] )
except : pass
try : Iii1ii1II11i = urllib . unquote_plus ( Ooo0OOoOoO0 [ "fanart" ] )
except : pass
if 20 - 20: I1IiiI . OoOooOOOO
if O0oO0OOoO == None or OO00Oo == None or len ( OO00Oo ) < 1 : II1III ( )
elif O0oO0OOoO == 1 : o00oooO0Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif O0oO0OOoO == 2 : i11ii1ii11i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 3 : o00Oo0oooooo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 4 : ooo000oOO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 5 : SEARCH ( )
elif O0oO0OOoO == 6 : YOUTUBE_CHANNEL ( OO00Oo )
elif O0oO0OOoO == 7 : oO0o00O0O0oo0 ( OO00Oo )
elif O0oO0OOoO == 8 : i1iI ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 9 : iI11 ( OO00Oo )
elif O0oO0OOoO == 10 : Oo ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 11 : I1111i ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 12 : Ii111IIi ( )
elif O0oO0OOoO == 13 : iI11Ii111 ( OO00Oo )
elif O0oO0OOoO == 14 : O0oOO0o ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 15 : Iii ( OO00Oo )
elif O0oO0OOoO == 16 : II1i111 ( OO00Oo )
elif O0oO0OOoO == 17 : ii1IiIi11 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 18 : IiI1ii1Ii ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 19 : I11I1 ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 20 : o00oO0oo0OO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 , Iii1ii1II11i )
elif O0oO0OOoO == 21 : iIiI ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 22 : iIIIiIii ( OO00Oo )
elif O0oO0OOoO == 23 : IiI1iii11iIi1 ( )
elif O0oO0OOoO == 24 : Oooo0 ( OO00Oo )
elif O0oO0OOoO == 25 : Iiii ( OO00Oo )
elif O0oO0OOoO == 26 : iI1iIIIi1i ( )
elif O0oO0OOoO == 27 : ii1iI ( OO00Oo )
elif O0oO0OOoO == 28 : OoO ( OO00Oo )
elif O0oO0OOoO == 29 : OOOooo ( OO00Oo )
elif O0oO0OOoO == 30 : oOo00o00oO ( )
elif O0oO0OOoO == 31 : O0OOO000o0o ( OO00Oo )
elif O0oO0OOoO == 32 : I1OooooO0oOOOO ( )
elif O0oO0OOoO == 33 : iII1I1IiI11ii ( OO00Oo )
elif O0oO0OOoO == 34 : OoOooOoO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 35 : OOOO0OOO ( )
elif O0oO0OOoO == 36 : iiII1i11i ( OO00Oo )
elif O0oO0OOoO == 37 : III1I1Iii1iiI ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 38 : oO0oo000OOOoO ( )
elif O0oO0OOoO == 39 : ii1iIi1iIiI1i ( OO00Oo )
elif O0oO0OOoO == 40 : o0o0oOoOO0O ( OO00Oo )
elif O0oO0OOoO == 41 : O00ooOo ( )
elif O0oO0OOoO == 42 : IiiIi ( OO00Oo )
elif O0oO0OOoO == 43 : ii1111i ( OO00Oo , IiII , Iii1ii1II11i )
elif O0oO0OOoO == 44 : i11i11 ( OO00Oo )
elif O0oO0OOoO == 45 : OOooOO000 ( OO00Oo )
elif O0oO0OOoO == 46 : O0oooo00o0Oo ( )
elif O0oO0OOoO == 47 : ooOoo0o0O ( OO00Oo )
elif O0oO0OOoO == 48 : SCRAPE_SPORTSMAMA_PLAY ( OO00Oo )
elif O0oO0OOoO == 49 : oo0OOo0O ( )
elif O0oO0OOoO == 50 : iIi1i ( OO00Oo )
elif O0oO0OOoO == 51 : ooO0oO00O0o ( OO00Oo )
elif O0oO0OOoO == 52 : i11i1iIiii ( )
elif O0oO0OOoO == 53 : OoOo000oOo0oo ( OO00Oo )
elif O0oO0OOoO == 54 : OOo00 ( OO00Oo )
elif O0oO0OOoO == 55 : o0o0OoOOOOOo ( )
elif O0oO0OOoO == 56 : O00OO ( oO0o0OOOO , OO00Oo , O0O0OoOO0 )
elif O0oO0OOoO == 57 : oO000 ( OO00Oo )
elif O0oO0OOoO == 58 : i1III ( OO00Oo )
elif O0oO0OOoO == 59 : i1iIi1111 ( OO00Oo )
elif O0oO0OOoO == 60 : IIIIoOo ( )
elif O0oO0OOoO == 61 : OoOOOO ( OO00Oo )
elif O0oO0OOoO == 62 : ooO000O ( OO00Oo )
elif O0oO0OOoO == 63 : O0O0ooOOO ( OO00Oo )
elif O0oO0OOoO == 64 : Oo0O0Oo00O ( OO00Oo )
elif O0oO0OOoO == 65 : III1ii ( )
elif O0oO0OOoO == 66 : OooOoOOo0oO00 ( OO00Oo )
elif O0oO0OOoO == 67 : iIii1Ooo0oO0 ( OO00Oo )
elif O0oO0OOoO == 68 : IiI1 ( )
elif O0oO0OOoO == 69 : iii1i1III ( OO00Oo )
if 75 - 75: O0OOooO
if 29 - 29: I1ii11iIi11i
if 53 - 53: i11iIiiIii . I1ii11iIi11i % OoOO / O0OOooO % iIii1I11I1II1
if 6 - 6: Oo0Ooo - iI1 . iIii1I11I1II1
if 30 - 30: O0OOooO + O0OOooO % iIii1 - o0oOOo0O0Ooo - I1ii11iIi11i
if 36 - 36: OoOooOOOO % iI1
if 72 - 72: I1IiiI / I1iiiiI1iII - O0 + OoOooOOOO
if 83 - 83: O0
if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
if 40 - 40: OoO0O00 + OoO0O00
if 94 - 94: I1iiiiI1iII * iIii1I11I1II1 . OoOooOOOO
if 13 - 13: iIii1I11I1II1 * OoOoOO00 / oO % O0OOooO + o00oo
if 41 - 41: I1ii11iIi11i
if O0oO0OOoO == None or OO00Oo == None or len ( OO00Oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
