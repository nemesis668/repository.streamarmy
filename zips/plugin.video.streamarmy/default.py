import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , shutil , urlresolver , random , liveresolver , hashlib
from resources . libs . common_addon import Addon
from resources . libs . modules import regex
import base64
from metahandler import metahandlers
if 64 - 64: i11iIiiIii
import os
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
IiII1IiiIiI1 = 'plugin.video.streamarmy'
iIiiiI1IiI1I1 = Addon ( IiII1IiiIiI1 , sys . argv )
o0OoOoOO00 = xbmcaddon . Addon ( id = IiII1IiiIiI1 )
I11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'fanart.jpg' ) )
Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'icon.png' ) )
I1ii11iIi11i = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'search.jpg' ) )
I1IiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + IiII1IiiIiI1 , 'next.png' ) )
o0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' , 'plugin.video.sportsdevil' ) )
iIiiiI = base64 . b64decode ( b'aHR0cDovL3d3dy5zdHJlYW1hcm15LnVrL01haW4vTWVudS54bWw=' )
Iii1ii1II11i = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId='
iI111iI = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
IiII = 'https://www.googleapis.com/youtube/v3/playlistItems?pageToken='
iI1Ii11111iIi = '&part=snippet&playlistId='
i1i1II = '&maxResults=50&key=AIzaSyCebQaY3SIk6VlFNzDlYy4nqNva9c9N4CI'
O0oo0OO0 = o0OoOoOO00 . getSetting ( 'password' )
I1i1iiI1 = o0OoOoOO00 . getSetting ( 'Conspiracy Password' )
iiIIIII1i1iI = o0OoOoOO00 . getSetting ( 'enable_meta' )
o0oO0 = 'http://pastebin.com/raw/4B2BhvJz'
oo00 = base64 . b64decode ( b'aHR0cDovL2dldGFmbGl4LnVzL2FkZG9uL3lvdXR1YmUucGhw' )
#SEARCH_LIST     = 'http://streamarmy.uk/Main/searchtext.xml'
o00 = xbmcgui . Dialog ( )
Oo0oO0ooo = xbmcgui . DialogProgress ( )
o0oOoO00o = 'http://www.streamarmy.uk/Main/Exceptions/Exceptions.xml'
i1 = "[COLOR red][B]STREAM ARMY[/B][/COLOR]"
oOOoo00O0O = [ "aliez" , "alldebrid" , "allvid" , "anistream" , "anyfiles" , "apnasave" , "blazefile" , "castamp" , "clicknupload" , "cloudmailru" , "cloudy" , "daclips" , "dailymotion" , "divxstage" , "ecostream" , "estream" , "exashare" , "facebook" , "fastplay" , "filepup" , "fileweed" , "flashx" , "googlevideo" , "gorillavid" , "grifthost" , "hugefiles" , "indavideo" , "jetload" , "kingfiles" , "letwatch" , "letwatch" , "mailru" , "megadebrid" , "megamp" , "mersalaayitten" , "movdivx" , "movpod" , "movshare" , "mpengine" , "mpstream" , "mpupload" , "myvidstream" , "nosvideo" , "novamov" , "nowvideo" , "ok" , "ol_gmu" , "ol_openload" , "play_net" , "play_playedto" , "playhd" , "playwire" , "premiumize_me" , "purevid" , "putload" , "rapidvideo" , "rapidvideocom" , "realdebrid" , "rpnet" , "rutube" , "simplydebrid" , "speedplay" , "speedvideo" , "stagevu" , "streamcloud" , "streamenet" , "streaminto" , "streamplay" , "teramixer" , "thevid" , "thevideo" , "thevideos" , "trollvid" , "tudou" , "tunepk" , "tusfiles" , "twitch" , "uploadaf" , "uploadx" , "uploadz" , "uptobox" , "userscloud" , "usersfiles" , "veeHD" , "veeHD" , "oveoh" , "vidabc" , "vidcrazynet" , "videa" , "videobee" , "videocloud" , "videoget" , "videohut" , "videoraj" , "videorev" , "videoweed" , "videowood" , "videozoo" , "vidlox" , "vidmad" , "vidme" , "vidto" , "vidtodo" , "vidup_me" , "vidup_vidup_org" , "vidup_vidzi" , "vimeo" , "vivosx" , "vk" , "vshare" , "vshareeu" , "watchers" , "watchonline" , "watchpass" , "watchvideo" , "weshare" , "xvidstage" , "yourupload" , "youtube" , "youwatch" , "zevera" , "zstream" ]
if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( link , splitting = '\n' ) :
 O0Oo = urllib2 . Request ( link )
 try :
  oo = urllib2 . urlopen ( O0Oo )
 except IOError :
  return [ ]
  if 33 - 33: I1I1i1 * oO0 / OOo0o0 / OOoOoo00oo - iI1 + OoOooOOOO
 else :
  i11iiII = oo . read ( )
  return i11iiII . split ( splitting )
  if 34 - 34: oooO % ii1IiIi11 * iIii1I111I11I . O00OooO0 % Ooooo
o00o = O00o0o0000o0o ( o0oOoO00o )
if 41 - 41: iI111IiI111I + OoOo % oooO + oO0
try :
 iIi = xbmc . getInfoLabel ( "System.BuildVersion" )
 II = float ( iIi [ : 4 ] )
 if 14 - 14: I1I1i1 . I11iii11IIi / iIii1I111I11I
 if II >= 17.0 and II <= 17.9 :
  if 38 - 38: II111iiii % i11iIiiIii . OoOo - oooO + iIii1I111I11I
  Ooooo0Oo00oO0 = [ "special://cache" ,
 "special://temp/" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/Other" ,
 "/private/var/mobile/Library/Caches/AppleTV/Video/LocalAndRental" ]
  if 12 - 12: iIii1I11I1II1 * I11iii11IIi . OoOo % ii1IiIi11 + O0
  for O00 in Ooooo0Oo00oO0 :
   if "special" in O00 :
    O00 = xbmc . translatePath ( O00 )
   if os . path . exists ( O00 ) :
    o0OOOOO00o0O0 = os . path . join ( O00 , "archive_cache" )
    if not os . path . exists ( o0OOOOO00o0O0 ) :
     os . makedirs ( o0OOOOO00o0O0 )
except : pass
if 71 - 71: OoOo % O00OooO0 / OOoOoo00oo
def ii11i1iIII ( input_data , key ) :
 if 3 - 3: i1IIi / I11iii11IIi % ii1IiIi11 * i11iIiiIii / O0 * ii1IiIi11
 III1ii1iII = ""
 for oo0oooooO0 in input_data :
  III1ii1iII += chr ( ord ( oo0oooooO0 ) ^ key )
  if 19 - 19: ii1IiIi11 + OoOo
 return III1ii1iII
 if 53 - 53: OoooooooOO . i1IIi
def ii1I1i1I ( input_data , password ) :
 if 88 - 88: oO0 + O0 / OOo0o0 * O00OooO0
 iiiIi1i1I = 0
 for oo0oooooO0 in password :
  iiiIi1i1I ^= ( ( 2 * ord ( oo0oooooO0 ) + 3 ) & 0xff )
  if 80 - 80: OOo0o0 - oO0
 return ii11i1iIII ( input_data , iiiIi1i1I )
 if 87 - 87: OoOooOOOO / ii1IiIi11 - i1IIi * oooO / OoooooooOO . O0
def iii11I111 ( input_data , password = "liverpool" ) :
 if 63 - 63: oO0 * OoOooOOOO - O00OooO0 * O0
 return ii1I1i1I ( input_data , password )
 if 17 - 17: iI1 % II111iiii
def I1IIiiIiii ( ) :
 if 97 - 97: OoOo - oooO * i11iIiiIii / OOo0o0 % iI111IiI111I - OoooooooOO
 OoOo00o = xbmc . translatePath ( 'special://home/addons/' + IiII1IiiIiI1 + '/addon.xml' )
 o0OOoo0OO0OOO = open ( OoOo00o ) . read ( )
 iI1iI1I1i1I = o0OOoo0OO0OOO . replace ( '\n' , ' ' ) . replace ( '\r' , ' ' )
 iIi11Ii1 = re . compile ( 'name=".+?".+?version="(.+?)".+?provider-name=".+?">' ) . findall ( str ( iI1iI1I1i1I ) )
 for Ii11iII1 in iIi11Ii1 :
  Oo0O0O0ooO0O = Ii11iII1
  if 15 - 15: iI1 + OOo0o0 - OoooooooOO / oooO
 oo000OO00Oo = "http://www.streamarmy.uk/Plugins/addons.xml"
 if 51 - 51: Ooooo * OOoOoo00oo + ii1IiIi11 + oO0
 o0O0O00 = o000o ( oo000OO00Oo )
 iIi11Ii1 = re . compile ( '<addon id="' + IiII1IiiIiI1 + '" name=".+?" version="(.+?)" provider-name=".+?">' ) . findall ( o0O0O00 ) [ 0 ]
 if 7 - 7: OoOo * oO0 % OoOooOOOO . Ooooo
 Ii1iIiII1ii1 ( '[B][COLOR lime]Your Current Version: ' + str ( Oo0O0O0ooO0O ) + '[/COLOR] | [COLOR yellow]Our Latest Version: ' + iIi11Ii1 + '[/COLOR][/B]' , 'url' , 999 , Oo , O0O )
 if 62 - 62: iIii1I11I1II1 * OOo0o0
 i1OOO ( )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 oo000OO00Oo = iIiiiI
 if 59 - 59: II111iiii + OoooooooOO * OOo0o0 + i1IIi
 o0O0O00 = Oo0OoO00oOO0o ( iIiiiI )
 iIi11Ii1 = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 80 - 80: OoOooOOOO + oooO - oooO % O00OooO0
 for Ii11iII1 in iIi11Ii1 :
  try :
   if '<m3u>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 11 , II11i1I11Ii1i , I11i )
   elif '<pornscrape>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 16 , II11i1I11Ii1i , I11i )
   elif '<docs>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<docs>(.+?)</docs>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 24 , II11i1I11Ii1i , I11i )
   elif '<anime>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<anime>(.+?)</anime>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 32 , II11i1I11Ii1i , I11i )
   elif '<cartoons>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 35 , II11i1I11Ii1i , I11i )
   elif '<comics>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<comics>(.+?)</comics>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 38 , II11i1I11Ii1i , I11i )
   elif '<filmon>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 26 , II11i1I11Ii1i , I11i )
   elif '<music>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<music>(.+?)</music>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 28 , II11i1I11Ii1i , I11i )
   elif '<sportsmama>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<sportsmama>(.+?)</sportsmama>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 12 , II11i1I11Ii1i , I11i )
   elif "<soccerstreams>" in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 31 , II11i1I11Ii1i , I11i , '' )
   elif '<channel>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<channel>(.+?)</channel>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 6 , II11i1I11Ii1i , I11i )
   elif '<tvput>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<tvputsput>(.+?)</tvput>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 13 , II11i1I11Ii1i , I11i )
   elif '<moviescrape>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 15 , II11i1I11Ii1i , I11i )
   elif '<moviescrapenorm>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    oo000OO00Oo = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 22 , II11i1I11Ii1i , I11i )
   elif '<sportsdevil>' in Ii11iII1 :
    O0ooo0O0oo0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     oo000OO00Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 ) [ 0 ]
     oo0oOo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Ii11iII1 ) [ 0 ]
     o000O0o = oo0oOo
     iI1iII1 = "/"
     if not o000O0o . endswith ( iI1iII1 ) :
      oO0OOoo0OO = o000O0o + "/"
     else :
      oO0OOoo0OO = o000O0o
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + oo000OO00Oo
     oo000OO00Oo = o0O0O00 + '%26referer=' + oO0OOoo0OO
     Ii1iIiII1ii1 ( OoOO0oo0o , oo000OO00Oo , 4 , II11i1I11Ii1i , I11i )
    elif len ( O0ooo0O0oo0 ) > 1 :
     OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     Ii1iIiII1ii1 ( OoOO0oo0o , O0ii1ii1ii , 8 , II11i1I11Ii1i , I11i )
     if 91 - 91: Ooooo
   elif '<folder>' in Ii11iII1 :
    OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    O0ii1ii1ii = re . compile ( '<folder>(.+?)</folder>' ) . findall ( Ii11iII1 ) [ 0 ]
    II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    if 15 - 15: II111iiii
    if O0ii1ii1ii in o00o :
     O000O0oOO0 ( OoOO0oo0o , O0ii1ii1ii , 1 , II11i1I11Ii1i , I11i )
    else :
     O000O0oOO0 ( OoOO0oo0o , O0ii1ii1ii , 20 , II11i1I11Ii1i , I11i )
   else :
    if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
    O0ooo0O0oo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
     ooOO0O0ooOooO = len ( iIi11Ii1 )
     for OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i , I11i in OO0OoO0o00 :
      if 'youtube.com/playlist' in oo000OO00Oo :
       O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 2 , II11i1I11Ii1i , I11i )
      else :
       oOOOo00O00oOo ( OoOO0oo0o , oo000OO00Oo , 2 , II11i1I11Ii1i , I11i )
    elif len ( O0ooo0O0oo0 ) > 1 :
     OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     I11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     oOOOo00O00oOo ( OoOO0oo0o , O0ii1ii1ii , 3 , II11i1I11Ii1i , I11i )
     if 34 - 34: O0 + oooO + I1I1i1
     if 16 - 16: O00OooO0 . O0 . O00OooO0 % iI1 - I11iii11IIi - iIii1I11I1II1
  except : pass
  if 36 - 36: Ooooo % OoOo % I1I1i1 - iI1
  Ii1I ( o0O0O00 )
  if 77 - 77: O00OooO0 % O00OooO0 * OoOooOOOO - i11iIiiIii
  if 93 - 93: OoooooooOO / I11iii11IIi % i11iIiiIii + iI1 * oO0
def i1OOO ( ) :
 I1 = iI11Ii ( o0oO0 )
 if len ( I1 ) > 1 :
  i1iIIIi1i = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  iI1iIIiiii = os . path . join ( os . path . join ( i1iIIIi1i , '' ) , 'compare.txt' )
  i1iI11i1ii11 = open ( iI1iIIiiii )
  OOooo0O00o = i1iI11i1ii11 . read ( )
  if OOooo0O00o == I1 : pass
  else :
   oOOoOooOo ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , I1 )
   O000oo = open ( iI1iIIiiii , "w" )
   O000oo . write ( I1 )
   O000oo . close ( )
   if 20 - 20: oooO % iIii1I111I11I / iIii1I111I11I + iIii1I111I11I
def III1IiiI ( name , url , iconimage , fanart ) :
 O0ii1ii1ii = url
 o0O0O00 = o000o ( url )
 if 'XXX>yes</XXX' in o0O0O00 :
  if O0oo0OO0 == '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Set Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    i1I = i1IIIII11I1IiI . getText ( )
    o0OoOoOO00 . setSetting ( 'password' , i1I )
   else : quit ( )
   if 72 - 72: i1IIi / oO0 + OoooooooOO - I1I1i1
 if 'XXX>yes</XXX' in o0O0O00 :
  if O0oo0OO0 <> '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Enter Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    i1I = i1IIIII11I1IiI . getText ( )
   if i1I <> O0oo0OO0 :
    quit ( )
  else : quit ( )
  if 29 - 29: iI1 + OoOooOOOO % O0
 if 'con>yes</con' in o0O0O00 :
  if I1i1iiI1 == '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Set Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    I1I11 = i1IIIII11I1IiI . getText ( )
    o0OoOoOO00 . setSetting ( 'Conspiracy Password' , I1I11 )
   else : quit ( )
   if 34 - 34: I11iii11IIi . oooO * iI1 + iI111IiI111I
 if 'con>yes</con' in o0O0O00 :
  if I1i1iiI1 <> '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Enter Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    I1I11 = i1IIIII11I1IiI . getText ( )
   if I1I11 <> I1i1iiI1 :
    quit ( )
  else : quit ( )
  if 31 - 31: O00OooO0 % O00OooO0 % ii1IiIi11
 iIi11Ii1 = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 if 69 - 69: oO0 - I1I1i1 + i1IIi / iI111IiI111I
 if 49 - 49: O0 . O00OooO0
 if 11 - 11: Ooooo * I11iii11IIi . iIii1I11I1II1 % OoooooooOO + O00OooO0
 for Ii11iII1 in iIi11Ii1 :
  try :
   if 78 - 78: oO0 . oooO + oO0 / ii1IiIi11 / oO0
   if '<regex>' in Ii11iII1 :
    oO0O00OoOO0 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( Ii11iII1 )
    oO0O00OoOO0 = '' . join ( oO0O00OoOO0 )
    OoO = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0O00OoOO0 )
    oO0O00OoOO0 = urllib . quote_plus ( oO0O00OoOO0 )
    if 88 - 88: O00OooO0 . II111iiii * II111iiii % iI111IiI111I
    iiIIiiIi1Ii11 = hashlib . md5 ( )
    for Oo0 in oO0O00OoOO0 : iiIIiiIi1Ii11 . update ( str ( Oo0 ) )
    iiIIiiIi1Ii11 = str ( iiIIiiIi1Ii11 . hexdigest ( ) )
    if 70 - 70: ii1IiIi11
    Ii11iII1 = Ii11iII1 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    Ii11iII1 = re . sub ( '<regex>.+?</regex>' , '' , Ii11iII1 )
    Ii11iII1 = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , Ii11iII1 )
    Ii11iII1 = re . sub ( '<link></link>' , '' , Ii11iII1 )
    if 45 - 45: O0
    name = re . sub ( '<meta>.+?</meta>' , '' , Ii11iII1 )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 26 - 26: ii1IiIi11 - iIii1I11I1II1 - I11iii11IIi / oO0 . OOo0o0 % iIii1I11I1II1
    try : OO = re . findall ( '<date>(.+?)</date>' , Ii11iII1 ) [ 0 ]
    except : OO = ''
    if re . search ( r'\d+' , OO ) : name += ' [COLOR red] Updated %s[/COLOR]' % OO
    if 25 - 25: oO0
    try : oOo0oO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , Ii11iII1 ) [ 0 ]
    except : oOo0oO = Oo
    if 51 - 51: I1I1i1 - OoOooOOOO + II111iiii * iIii1I111I11I . ii1IiIi11 + OoOooOOOO
    try : OoO0o = re . findall ( '<fanart>(.+?)</fanart>' , Ii11iII1 ) [ 0 ]
    except : OoO0o = O0O
    if 78 - 78: OoOooOOOO % O0 % iIii1I111I11I
    try : ii = re . findall ( '<meta>(.+?)</meta>' , Ii11iII1 ) [ 0 ]
    except : ii = '0'
    if 5 - 5: OoOo - II111iiii - OoooooooOO % iIii1I111I11I + I11iii11IIi * iIii1I11I1II1
    try : url = re . findall ( '<link>(.+?)</link>' , Ii11iII1 ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % ii )
    url = '<preset>search</preset>%s' % ii if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % ii )
    url = '<preset>searchsd</preset>%s' % ii if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 37 - 37: Ooooo % OoOo + OOo0o0 + OOoOoo00oo * ii1IiIi11 % O0
    if not oO0O00OoOO0 == '' :
     hash . append ( { 'regex' : iiIIiiIi1Ii11 , 'response' : oO0O00OoOO0 } )
     url += '|regex=%s' % oO0O00OoOO0
     if 61 - 61: I11iii11IIi - oooO . OoOooOOOO / oooO + I1I1i1
    I1i11i ( name , url , 10 , oOo0oO , OoO0o , "" )
    if 64 - 64: oooO % iIii1I11I1II1 * OoOooOOOO
   elif '<sportsmama>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<sportsmama>(.+?)</sportsmama>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 12 , iconimage , fanart )
   elif "<soccerstreams>" in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 31 , iconimage , fanart , '' )
   elif '<m3u>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 11 , iconimage , fanart )
   elif '<anime>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 35 , iconimage , fanart )
   elif '<docs>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 24 , iconimage , fanart )
   elif '<filmon>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 26 , iconimage , fanart )
   elif '<music>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 28 , iconimage , fanart )
   elif '<pornscrape>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 16 , iconimage , fanart )
   elif '<tvput>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 13 , iconimage , fanart )
   elif '<moviescrape>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 22 , iconimage , fanart )
   elif '<channel>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in Ii11iII1 :
    O0ooo0O0oo0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 ) [ 0 ]
     oo0oOo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Ii11iII1 ) [ 0 ]
     o000O0o = oo0oOo
     iI1iII1 = "/"
     if not o000O0o . endswith ( iI1iII1 ) :
      oO0OOoo0OO = o000O0o + "/"
     else :
      oO0OOoo0OO = o000O0o
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + oO0OOoo0OO
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0ooo0O0oo0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     Ii1iIiII1ii1 ( name , O0ii1ii1ii , 8 , iconimage , fanart )
     if 79 - 79: O0
   elif '<folder>' in Ii11iII1 :
    OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
    for name , url , iconimage , fanart in OO0OoO0o00 :
     if url in o00o :
      O000O0oOO0 ( name , url , 1 , iconimage , fanart )
     else :
      O000O0oOO0 ( name , url , 20 , iconimage , fanart )
      if 78 - 78: iI1 + oooO - iI111IiI111I
   else :
    O0ooo0O0oo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
     ooOO0O0ooOooO = len ( iIi11Ii1 )
     for name , url , iconimage , fanart in OO0OoO0o00 :
      if 'youtube.com/playlist' in url :
       O000O0oOO0 ( name , url , 2 , iconimage , fanart )
      else :
       oOOOo00O00oOo ( name , url , 2 , iconimage , fanart )
    elif len ( O0ooo0O0oo0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     oOOOo00O00oOo ( name , O0ii1ii1ii , 3 , iconimage , fanart )
  except : pass
 Ii1I ( o0O0O00 )
 if 38 - 38: OOoOoo00oo - OoOooOOOO + iIii1I11I1II1 / OOo0o0 % I1I1i1
 if 57 - 57: oO0 / OoOo
def Ii1I1Ii ( name , url , iconimage , fanart ) :
 if 69 - 69: I11iii11IIi / OOoOoo00oo . Ooooo * iI111IiI111I % iIii1I111I11I - OOoOoo00oo
 if 13 - 13: iIii1I111I11I . i11iIiiIii
 O0ii1ii1ii = url
 o0O0O00 = Oo0OoO00oOO0o ( url )
 if 56 - 56: iI1 % O0 - I11iii11IIi
 if 100 - 100: iIii1I111I11I - O0 % OoOooOOOO * oooO + I11iii11IIi
 if 88 - 88: OoooooooOO - oO0 * O0 * OoooooooOO . OoooooooOO
 if 'XXX>yes</XXX' in o0O0O00 :
  if O0oo0OO0 == '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Set Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    i1I = i1IIIII11I1IiI . getText ( )
    o0OoOoOO00 . setSetting ( 'password' , i1I )
   else : quit ( )
   if 33 - 33: iI111IiI111I + O00OooO0 * OoOooOOOO / iIii1I11I1II1 - I11iii11IIi
 if 'XXX>yes</XXX' in o0O0O00 :
  if O0oo0OO0 <> '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Enter Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    i1I = i1IIIII11I1IiI . getText ( )
   if i1I <> O0oo0OO0 :
    quit ( )
  else : quit ( )
  if 54 - 54: iI111IiI111I / oooO . OoOooOOOO % O00OooO0
 if 'con>yes</con' in o0O0O00 :
  if I1i1iiI1 == '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Set Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    I1I11 = i1IIIII11I1IiI . getText ( )
    o0OoOoOO00 . setSetting ( 'Conspiracy Password' , I1I11 )
   else : quit ( )
   if 57 - 57: i11iIiiIii . iI1 - iIii1I111I11I - OoOooOOOO + OOo0o0
 if 'con>yes</con' in o0O0O00 :
  if I1i1iiI1 <> '' :
   o00 = xbmcgui . Dialog ( )
   iI = o00 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if iI == 1 :
    i1IIIII11I1IiI = xbmc . Keyboard ( '' , 'Enter Password' )
    i1IIIII11I1IiI . doModal ( )
   if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
    I1I11 = i1IIIII11I1IiI . getText ( )
   if I1I11 <> I1i1iiI1 :
    quit ( )
  else : quit ( )
  if 63 - 63: OOo0o0 * O00OooO0
 iIi11Ii1 = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
 for Ii11iII1 in iIi11Ii1 :
  try :
   if 69 - 69: O0 . oO0
   if '<regex>' in Ii11iII1 :
    oO0O00OoOO0 = re . compile ( '(<regex>.+?</regex>)' , re . MULTILINE | re . DOTALL ) . findall ( Ii11iII1 )
    oO0O00OoOO0 = '' . join ( oO0O00OoOO0 )
    OoO = re . compile ( '(<listrepeat>.+?</listrepeat>)' , re . MULTILINE | re . DOTALL ) . findall ( oO0O00OoOO0 )
    oO0O00OoOO0 = urllib . quote_plus ( oO0O00OoOO0 )
    if 49 - 49: I11iii11IIi - ii1IiIi11
    iiIIiiIi1Ii11 = hashlib . md5 ( )
    for Oo0 in oO0O00OoOO0 : iiIIiiIi1Ii11 . update ( str ( Oo0 ) )
    iiIIiiIi1Ii11 = str ( iiIIiiIi1Ii11 . hexdigest ( ) )
    if 74 - 74: iIii1I11I1II1 * iI1 + OOo0o0 / i1IIi / II111iiii . I1I1i1
    Ii11iII1 = Ii11iII1 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' ) . replace ( '&nbsp;' , '' )
    Ii11iII1 = re . sub ( '<regex>.+?</regex>' , '' , Ii11iII1 )
    Ii11iII1 = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , Ii11iII1 )
    Ii11iII1 = re . sub ( '<link></link>' , '' , Ii11iII1 )
    if 62 - 62: OoooooooOO * I11iii11IIi
    name = re . sub ( '<meta>.+?</meta>' , '' , Ii11iII1 )
    try : name = re . findall ( '<title>(.+?)</title>' , name ) [ 0 ]
    except : name = re . findall ( '<name>(.+?)</name>' , name ) [ 0 ]
    if 58 - 58: OOo0o0 % OOoOoo00oo
    try : OO = re . findall ( '<date>(.+?)</date>' , Ii11iII1 ) [ 0 ]
    except : OO = ''
    if re . search ( r'\d+' , OO ) : name += ' [COLOR red] Updated %s[/COLOR]' % OO
    if 50 - 50: iI111IiI111I . OOoOoo00oo
    try : oOo0oO = re . findall ( '<thumbnail>(.+?)</thumbnail>' , Ii11iII1 ) [ 0 ]
    except : oOo0oO = Oo
    if 97 - 97: O0 + OOo0o0
    try : OoO0o = re . findall ( '<fanart>(.+?)</fanart>' , Ii11iII1 ) [ 0 ]
    except : OoO0o = O0O
    if 89 - 89: OOoOoo00oo + oO0 * ii1IiIi11 * iIii1I111I11I
    try : ii = re . findall ( '<meta>(.+?)</meta>' , Ii11iII1 ) [ 0 ]
    except : ii = '0'
    if 37 - 37: OoooooooOO - O0 - OOoOoo00oo
    try : url = re . findall ( '<link>(.+?)</link>' , Ii11iII1 ) [ 0 ]
    except : url = '0'
    url = url . replace ( '>search<' , '><preset>search</preset>%s<' % ii )
    url = '<preset>search</preset>%s' % ii if url == 'search' else url
    url = url . replace ( '>searchsd<' , '><preset>searchsd</preset>%s<' % ii )
    url = '<preset>searchsd</preset>%s' % ii if url == 'searchsd' else url
    url = re . sub ( '<sublink></sublink>|<sublink\s+name=(?:\'|\").*?(?:\'|\")></sublink>' , '' , url )
    if 77 - 77: oooO * iIii1I11I1II1
    if not oO0O00OoOO0 == '' :
     hash . append ( { 'regex' : iiIIiiIi1Ii11 , 'response' : oO0O00OoOO0 } )
     url += '|regex=%s' % oO0O00OoOO0
     if 98 - 98: I11iii11IIi % iIii1I111I11I * OoooooooOO
    I1i11i ( name , url , 10 , oOo0oO , OoO0o , "" )
    if 51 - 51: iIii1I11I1II1 . OOo0o0 / OoOooOOOO + OOoOoo00oo
   elif '<sportsmama>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<sportsmama>(.+?)</sportsmama>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 12 , iconimage , fanart )
   elif "<soccerstreams>" in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<soccerstreams>(.+?)</soccerstreams>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 31 , iconimage , fanart , '' )
   elif '<m3u>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<m3u>(.+?)</m3u>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 11 , iconimage , fanart )
   elif '<docs>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<docs>(.+?)</docs>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 24 , iconimage , fanart )
   elif '<anime>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<anime>(.+?)</anime>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 32 , iconimage , fanart )
   elif '<comics>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<comics>(.+?)</comics>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 38 , iconimage , fanart )
   elif '<cartoons>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<cartoons>(.+?)</cartoons>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 35 , iconimage , fanart )
   elif '<music>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<music>(.+?)</music>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 28 , iconimage , fanart )
   elif '<filmon>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<filmon>(.+?)</filmon>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 26 , iconimage , fanart )
   elif '<tvput>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<tvput>(.+?)</tvput>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 13 , iconimage , fanart )
   elif '<pornscrape>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<pornscrape>(.+?)</pornscrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 16 , iconimage , fanart )
   elif '<moviescrape>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<moviescrape>(.+?)</moviescrape>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 15 , iconimage , fanart )
   elif '<moviescrapenorm>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<moviescrapenorm>(.+?)</moviescrapenorm>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 22 , iconimage , fanart )
   elif '<moviessearch>yes</moviessearch>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , 'url' , 23 , iconimage , fanart )
   elif '<channel>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , url , 6 , iconimage , fanart )
   elif '<image>' in Ii11iII1 :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( Ii11iII1 ) [ 0 ]
    O000O0oOO0 ( name , iconimage , 9 , iconimage , fanart )
   elif '<sportsdevil>' in Ii11iII1 :
    O0ooo0O0oo0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 ) [ 0 ]
     oo0oOo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Ii11iII1 ) [ 0 ]
     o000O0o = oo0oOo
     iI1iII1 = "/"
     if not o000O0o . endswith ( iI1iII1 ) :
      oO0OOoo0OO = o000O0o + "/"
     else :
      oO0OOoo0OO = o000O0o
     o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
     url = o0O0O00 + '%26referer=' + oO0OOoo0OO
     Ii1iIiII1ii1 ( name , url , 4 , iconimage , fanart )
    elif len ( O0ooo0O0oo0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     Ii1iIiII1ii1 ( name , O0ii1ii1ii , 8 , iconimage , fanart )
     if 33 - 33: OoOo . II111iiii % O00OooO0 + OOoOoo00oo
   elif '<folder>' in Ii11iII1 :
    OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
    for name , url , iconimage , fanart in OO0OoO0o00 :
     if url in o00o :
      O000O0oOO0 ( name , url , 1 , iconimage , fanart )
     else :
      O000O0oOO0 ( name , url , 20 , iconimage , fanart )
   else :
    O0ooo0O0oo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( Ii11iII1 )
    if len ( O0ooo0O0oo0 ) == 1 :
     OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
     ooOO0O0ooOooO = len ( iIi11Ii1 )
     for name , url , iconimage , fanart in OO0OoO0o00 :
      if 'youtube.com/playlist' in url :
       O000O0oOO0 ( name , url , 2 , iconimage , fanart )
      else :
       oOOOo00O00oOo ( name , url , 2 , iconimage , fanart )
    elif len ( O0ooo0O0oo0 ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 ) [ 0 ]
     oOOOo00O00oOo ( name , O0ii1ii1ii , 3 , iconimage , fanart )
  except : pass
 Ii1I ( o0O0O00 )
 if 71 - 71: I1I1i1 % oooO
 if 98 - 98: ii1IiIi11 % i11iIiiIii % OoOo + iIii1I111I11I
 if 78 - 78: iI1 % OoOooOOOO / O00OooO0 - iIii1I11I1II1
 if 69 - 69: iI111IiI111I
 if 11 - 11: I11iii11IIi
 if 16 - 16: iIii1I111I11I + Ooooo * O0 % i1IIi . I11iii11IIi
 if 67 - 67: OoooooooOO / I11iii11IIi * iIii1I111I11I + ii1IiIi11
 if 65 - 65: OoooooooOO - iI1 / OoOo / II111iiii / i1IIi
 if 71 - 71: iI111IiI111I + iIii1I111I11I
 if 28 - 28: oooO
 if 38 - 38: OoOo % II111iiii % ii1IiIi11 / oO0 + OOo0o0 / i1IIi
 if 54 - 54: iIii1I11I1II1 % iI1 - oooO / OoOooOOOO - oO0 . ii1IiIi11
 if 11 - 11: iI1 . oO0 * Ooooo * OoooooooOO + OoOo
 if 33 - 33: O0 * OOoOoo00oo - iI111IiI111I % iI111IiI111I
 if 18 - 18: iI111IiI111I / I1I1i1 * iI111IiI111I + iI111IiI111I * i11iIiiIii * iI1
 if 11 - 11: OoOo / OOo0o0 - Ooooo * OoooooooOO + OoooooooOO . OOo0o0
 if 26 - 26: iIii1I111I11I % iI1
 if 76 - 76: Ooooo * O00OooO0
 if 52 - 52: oooO
 if 19 - 19: I11iii11IIi
 if 25 - 25: iIii1I111I11I / OoOo
 if 31 - 31: oooO . O0 % I11iii11IIi . OOoOoo00oo + Ooooo
 if 71 - 71: iI111IiI111I . II111iiii
def oo0 ( name , url , iconimage ) :
 if 61 - 61: OOo0o0 - oooO - i1IIi
 i1iI11i1ii11 , IiI1iIiIIIii = re . findall ( '(.+?)\|regex=(.+?)$' , url ) [ 0 ]
 i1iI11i1ii11 += urllib . unquote_plus ( IiI1iIiIIIii )
 url = regex . resolve ( i1iI11i1ii11 )
 if 53 - 53: i1IIi
 o0OOOoO0 ( name , url , iconimage )
 if 73 - 73: ii1IiIi11 % i11iIiiIii - I11iii11IIi
 if 7 - 7: O0 * i11iIiiIii * iIii1I111I11I + OoOo % oO0 - OoOo
def II1IIIIiII1i ( ) :
 i1IIIII11I1IiI = xbmc . Keyboard ( '' , '[COLOR lime]S[/COLOR][COLOR white]earch[/COLOR] [B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B]' )
 i1IIIII11I1IiI . doModal ( )
 if ( i1IIIII11I1IiI . isConfirmed ( ) ) :
  i1II1 = i1IIIII11I1IiI . getText ( )
  i1II1 = i1II1 . upper ( )
 else : quit ( )
 o0O0O00 = o000o ( SEARCH_LIST )
 i11i1 = re . compile ( '<link>(.+?)</link>' ) . findall ( o0O0O00 )
 for oo000OO00Oo in i11i1 :
  O0ii1ii1ii = oo000OO00Oo
  o0O0O00 = Oo0OoO00oOO0o ( oo000OO00Oo )
  IiiiiI1i1Iii = re . compile ( '<item>(.+?)</item>' ) . findall ( o0O0O00 )
  for Ii11iII1 in IiiiiI1i1Iii :
   iIi11Ii1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 )
   for oo00oO0o in iIi11Ii1 :
    oo00oO0o = oo00oO0o . upper ( )
    if i1II1 in oo00oO0o :
     try :
      if '<sportsdevil>' in Ii11iII1 :
       OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
       II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
       oo000OO00Oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Ii11iII1 ) [ 0 ]
       oo0oOo = re . compile ( '<referer>(.+?)</referer>' ) . findall ( Ii11iII1 ) [ 0 ]
       o0O0O00 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + oo000OO00Oo
       oo000OO00Oo = o0O0O00 + '%26referer=' + oo0oOo
       if 'tp' in oo000OO00Oo :
        oOOOo00O00oOo ( OoOO0oo0o , oo000OO00Oo , 4 , II11i1I11Ii1i , O0O )
      elif '<folder>' in Ii11iII1 :
       OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
       for OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i , I11i in OO0OoO0o00 :
        if 'tp' in oo000OO00Oo :
         O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 1 , II11i1I11Ii1i , O0O )
      else :
       O0ooo0O0oo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( Ii11iII1 )
       if len ( O0ooo0O0oo0 ) == 1 :
        OO0OoO0o00 = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( Ii11iII1 )
        ooOO0O0ooOooO = len ( iIi11Ii1 )
        for OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i , I11i in OO0OoO0o00 :
         if 'youtube.com/playlist' in oo000OO00Oo :
          O000O0oOO0 ( OoOO0oo0o , oo000OO00Oo , 2 , II11i1I11Ii1i , O0O )
         else :
          if 'tp' in oo000OO00Oo :
           oOOOo00O00oOo ( OoOO0oo0o , oo000OO00Oo , 2 , II11i1I11Ii1i , O0O )
       elif len ( O0ooo0O0oo0 ) > 1 :
        OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( Ii11iII1 ) [ 0 ]
        II11i1I11Ii1i = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Ii11iII1 ) [ 0 ]
        oOOOo00O00oOo ( OoOO0oo0o , O0ii1ii1ii , 3 , II11i1I11Ii1i , O0O )
     except : pass
     if 31 - 31: oooO
     if 23 - 23: iI111IiI111I . Ooooo
def OO0000o ( name , url , iconimage ) :
 if 42 - 42: I1I1i1
 oo000O0OoooO = urllib2 . Request ( url )
 oo000O0OoooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' )
 oo = urllib2 . urlopen ( oo000O0OoooO )
 o0O0O00 = oo . read ( )
 oo . close ( )
 oo = o0O0O00
 oo = oo . replace ( '#AAASTREAM:' , '#A:' )
 oo = oo . replace ( '#EXTINF:' , '#A:' )
 O0o = re . compile ( '^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( oo )
 I1i11II1i = [ ]
 for o0o0OoOo0O0OO , iIi1I11I , url in O0o :
  Iii1 = { "params" : o0o0OoOo0O0OO , "display_name" : iIi1I11I , "url" : url }
  I1i11II1i . append ( Iii1 )
 list = [ ]
 for ooO in I1i11II1i :
  Iii1 = { "display_name" : ooO [ "display_name" ] , "url" : ooO [ "url" ] }
  O0o = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( ooO [ "params" ] )
  for o0o00OOo0 , I1IIii1 in O0o :
   Iii1 [ o0o00OOo0 . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = I1IIii1 . strip ( )
  list . append ( Iii1 )
 for ooO in list :
  name = OO0o0oOOO0O ( ooO [ "display_name" ] )
  url = OO0o0oOOO0O ( ooO [ "url" ] )
  url = url . replace ( '\\r' , '' ) . replace ( '\\t' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' ) . replace ( ' ' , '' ) . replace ( 'm3u8' , 'm3u8' )
  I1i11i ( name , url , 2 , Oo , I11i , '' )
  if 49 - 49: iI1 . OOoOoo00oo . II111iiii
  if 98 - 98: O00OooO0
  if 68 - 68: iIii1I11I1II1 * iIii1I11I1II1 . OOoOoo00oo / II111iiii % I1I1i1
def i1i11I11 ( name , url , iconimage ) :
 iiiiII1I = [ ]
 ooo00Ooo = [ ]
 Oo0o0O00 = [ ]
 o0O0O00 = Oo0OoO00oOO0o ( url )
 ii1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii1 ) [ 0 ]
 O0ooo0O0oo0 = re . compile ( '<link>(.+?)</link>' ) . findall ( ii1 )
 Oo0 = 1
 for I1i11 in O0ooo0O0oo0 :
  OOo0O0oo0OO0O = I1i11
  if '(' in I1i11 :
   I1i11 = I1i11 . split ( '(' ) [ 0 ]
   OO0 = str ( OOo0O0oo0OO0O . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiiiII1I . append ( I1i11 )
   ooo00Ooo . append ( OO0 )
  else :
   iiiiII1I . append ( I1i11 )
   ooo00Ooo . append ( 'Link ' + str ( Oo0 ) )
  Oo0 = Oo0 + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 o00 = xbmcgui . Dialog ( )
 o0O = o00 . select ( name , ooo00Ooo )
 if o0O < 0 :
  quit ( )
 else :
  url = iiiiII1I [ o0O ]
  if 74 - 74: i11iIiiIii . I11iii11IIi
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : iiI = liveresolver . resolve ( url )
  else : iiI = url
  oO = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  oO . setPath ( iiI )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oO )
  if 10 - 10: I1I1i1 / I1I1i1 / iI111IiI111I . iI111IiI111I
def OOoo ( name , url , iconimage ) :
 if 50 - 50: oO0
 if 43 - 43: II111iiii . OoOooOOOO / iI1
 i1iI1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
 iiiiII1I = [ ]
 ooo00Ooo = [ ]
 Oo0o0O00 = [ ]
 i11ii1ii11i = [ ]
 o0O0O00 = o000o ( url )
 ii1 = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 O0ooo0O0oo0 = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( ii1 )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii1 ) [ 0 ]
 Oo0 = 1
 if 70 - 70: i1IIi - O00OooO0 + I1I1i1
 for I1i11 in O0ooo0O0oo0 :
  OOo0O0oo0OO0O = I1i11
  if '(' in I1i11 :
   I1i11 = I1i11 . split ( '(' ) [ 0 ]
   OO0 = str ( OOo0O0oo0OO0O . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   iiiiII1I . append ( I1i11 )
   ooo00Ooo . append ( OO0 )
   i11ii1ii11i . append ( 'Stream ' + str ( Oo0 ) )
  else :
   iiiiII1I . append ( I1i11 )
   ooo00Ooo . append ( 'Link ' + str ( Oo0 ) )
   if 12 - 12: OOoOoo00oo - iI1 % OOo0o0 * ii1IiIi11
  Oo0 = Oo0 + 1
 name = '[COLOR red]' + name + '[/COLOR]'
 o00 = xbmcgui . Dialog ( )
 o0O = o00 . select ( name , ooo00Ooo )
 if o0O < 0 :
  quit ( )
 else :
  o000O0o = ooo00Ooo [ o0O ]
  iI1iII1 = "/"
  if not o000O0o . endswith ( iI1iII1 ) :
   oO0OOoo0OO = o000O0o + "/"
  else :
   oO0OOoo0OO = o000O0o
  url = i1iI1 + iiiiII1I [ o0O ] + "%26referer=" + oO0OOoo0OO
  print url
  if 44 - 44: O00OooO0 % iIii1I111I11I
  xbmc . Player ( ) . play ( url )
  if 41 - 41: i1IIi - ii1IiIi11 - iIii1I111I11I
  if 8 - 8: oO0 + iI111IiI111I - OOoOoo00oo % I1I1i1 % OOoOoo00oo * OoOooOOOO
def IIIi11I11 ( url ) :
 if 44 - 44: II111iiii
 try :
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
  OoOO0oo0o = url . split ( '/' ) [ 2 ]
  OoOO0oo0o = OoOO0oo0o . replace ( '.html' , '' )
  OOOO0OOO = re . compile ( '<div class="schedule">(.+?)<br><div id="pagination">' ) . findall ( o0O0O00 ) [ 0 ]
  i1i1ii = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)"></div>.+?<div class="home cell">.+?<span>(.+?)</span>.+?<span>(.+?)</span>.+?</a>' ) . findall ( OOOO0OOO )
  for url , II11i1I11Ii1i , iII1ii1 , I1i1iiiI1 in i1i1ii :
   url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url + '%26referer=no'
   oOOOo00O00oOo ( iII1ii1 + ' vs ' + I1i1iiiI1 , url , 2 , II11i1I11Ii1i , O0O , '' )
 except :
  o00 . ok ( "Stream Army" , "Damn, No Links available at the moment, come back closer to the event!" )
  quit ( )
  if 24 - 24: OoOooOOOO / i11iIiiIii + OoOooOOOO
  if 20 - 20: ii1IiIi11 + iIii1I111I11I / O0 % iIii1I11I1II1
  if 88 - 88: OOo0o0 / II111iiii
def OOOOO0O00 ( ) :
 if 30 - 30: iIii1I11I1II1 . I11iii11IIi . oooO / OOoOoo00oo
 oo000OO00Oo = 'http://www.animetoon.org/dubbed-anime'
 if 42 - 42: I1I1i1
 o0O0O00 = o000o ( oo000OO00Oo )
 II1IIiiIiI = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 1 - 1: O00OooO0
 for O0ooo0O0oo0 in II1IIiiIiI :
  try :
   oo000OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O0O0Ooo = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O000O0oOO0 ( "[COLOR lime]" + O0O0Ooo + "[/COLOR]" , oo000OO00Oo , 33 , II11i1I11Ii1i , O0O , '' )
  except : pass
  if 77 - 77: OOoOoo00oo / OoooooooOO
def IIii11I1i1I ( url ) :
 if 99 - 99: O00OooO0
 o0O0O00 = o000o ( url )
 II11i1I11Ii1i = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 iIi11Ii1 = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 II1IIiiIiI = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( iIi11Ii1 )
 if 76 - 76: oO0 * I11iii11IIi
 for o0o0OO0Oooooo in II1IIiiIiI :
  try :
   OoOO0oo0o = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( o0o0OO0Oooooo ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( o0o0OO0Oooooo ) [ 0 ]
   oOOOo00O00oOo ( "[COLOR lime]" + OoOO0oo0o + "[/COLOR]" , url , 34 , II11i1I11Ii1i , O0O , '' )
  except : pass
  if 36 - 36: I11iii11IIi - ii1IiIi11
def i11i11111i1i ( name , url , iconimage ) :
 if 72 - 72: oooO % iI1 + oO0 / OoOooOOOO + Ooooo
 o0O0O00 = o000o ( url )
 I1I1i = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 1 - 1: ii1IiIi11 % oooO + O0 + i1IIi - oO0
 if 22 - 22: I11iii11IIi % iI1
 o0oo0O ( name , I1I1i , iconimage )
 if 13 - 13: i11iIiiIii + i1IIi * iIii1I11I1II1 % OoooooooOO - II111iiii * oooO
def iiIi1iI1iIii ( ) :
 if 68 - 68: oooO
 oo000OO00Oo = 'http://www.toonget.net/cartoon'
 if 82 - 82: iIii1I11I1II1 + I1I1i1 . iIii1I11I1II1 % Ooooo / iIii1I111I11I . iIii1I111I11I
 o0O0O00 = o000o ( oo000OO00Oo )
 II1IIiiIiI = re . compile ( '<td>(.+?)</td>' , re . DOTALL ) . findall ( o0O0O00 )
 if 14 - 14: OOoOoo00oo . oooO . ii1IiIi11 + OoooooooOO - oooO + Ooooo
 for O0ooo0O0oo0 in II1IIiiIiI :
  try :
   oo000OO00Oo = re . compile ( '<a href="(.+?)">' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O0O0Ooo = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O000O0oOO0 ( "[COLOR lime]" + O0O0Ooo + "[/COLOR]" , oo000OO00Oo , 36 , II11i1I11Ii1i , O0O , '' )
  except : pass
  if 9 - 9: iIii1I111I11I
def oooooOOO000Oo ( url ) :
 if 52 - 52: II111iiii % Ooooo . OOo0o0 * iIii1I11I1II1
 o0O0O00 = o000o ( url )
 II11i1I11Ii1i = re . compile ( 'img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 2 ]
 iIi11Ii1 = re . compile ( '<div id="videos">(.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 II1IIiiIiI = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( iIi11Ii1 )
 if 50 - 50: OoOo - iI111IiI111I * Ooooo . iI1
 for o0o0OO0Oooooo in II1IIiiIiI :
  try :
   OoOO0oo0o = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( o0o0OO0Oooooo ) [ 0 ]
   url = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( o0o0OO0Oooooo ) [ 0 ]
   oOOOo00O00oOo ( "[COLOR lime]" + OoOO0oo0o + "[/COLOR]" , url , 37 , II11i1I11Ii1i , O0O , '' )
  except : pass
  if 37 - 37: OoOo % i11iIiiIii % II111iiii . O0 . iIii1I111I11I
def OO0oOOoo ( name , url , iconimage ) :
 if 52 - 52: OOoOoo00oo % I1I1i1
 o0O0O00 = o000o ( url )
 I1I1i = re . compile ( '<iframe src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 64 - 64: O0 % ii1IiIi11 % O0 * oO0 . OoOooOOOO + I11iii11IIi
 if 75 - 75: ii1IiIi11 . OoooooooOO % OOoOoo00oo * ii1IiIi11 % OoooooooOO
 o0oo0O ( name , I1I1i , iconimage )
 if 13 - 13: Ooooo / i11iIiiIii % II111iiii % ii1IiIi11 . iI1
def iIIIii ( ) :
 if 58 - 58: OOoOoo00oo / Ooooo . OOo0o0 / OoooooooOO + iI111IiI111I
 oo000OO00Oo = 'http://www.readcomics.tv/comic-list'
 o0O0O00 = o000o ( oo000OO00Oo )
 iIi11Ii1 = re . compile ( '<div class="serie-box" id="others">(.+?)<h2>Read Comics Online</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 II1IIiiIiI = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( iIi11Ii1 )
 if 86 - 86: ii1IiIi11 * I11iii11IIi + ii1IiIi11 + II111iiii
 for O0ooo0O0oo0 in II1IIiiIiI :
  try :
   OoOO0oo0o = re . compile ( '<a href=".+?">(.+?)</a>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   oo000OO00Oo = re . compile ( '<a href="(.+?)">.+?</a>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O000O0oOO0 ( "[COLOR lime]" + OoOO0oo0o + "[/COLOR]" , oo000OO00Oo , 39 , II11i1I11Ii1i , O0O , '' )
  except : pass
  if 8 - 8: iI111IiI111I - O00OooO0 / OoOo
def oo0oOoo ( url ) :
 if 57 - 57: OOo0o0 - iI1
 o0O0O00 = o000o ( url )
 I11iiI11 = re . compile ( '<div class="manga-image"><img src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 OoOO0oo0o = re . compile ( '<h2>(.+?)</h2>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ] . replace ( 'Read ' , '' ) . replace ( 'Online' , '' )
 o00oOoOo0 = re . compile ( '<a class="stread" href="(.+?)">' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0OOoo0OO0OOO = o00oOoOo0 . split ( '/' ) [ - 1 ]
 iI1iI1I1i1I = o0OOoo0OO0OOO . replace ( 'chapter-' , ' ' )
 iI1iI1I1i1I = int ( iI1iI1I1i1I )
 O000O0oOO0 ( "[COLOR lime]Issue " + str ( iI1iI1I1i1I ) + "[/COLOR]" , o00oOoOo0 , 40 , I11iiI11 , O0O , '' )
 iIi11Ii1 = re . compile ( '<ul class="ml-list">(.+?)</ul>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 II1IIiiIiI = re . compile ( '<li>(.+?)</li>' , re . DOTALL ) . findall ( iIi11Ii1 )
 for O0ooo0O0oo0 in sorted ( II1IIiiIiI ) :
  iI1iI1I1i1I = iI1iI1I1i1I + 1
  url = re . compile ( '<a href="(.+?)"' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
  O000O0oOO0 ( "[COLOR lime]Issue " + str ( iI1iI1I1i1I ) + "[/COLOR]" , url , 40 , I11iiI11 , O0O , '' )
  if 72 - 72: iI111IiI111I
def OO0ooo0oOO ( url ) :
 if 97 - 97: I11iii11IIi / O00OooO0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' )
 Oooo0 = re . compile ( '<div class="label">of (.+?)</div>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 if 59 - 59: OoooooooOO
 Oooo0 = int ( Oooo0 )
 i1iiiii1 = re . compile ( '<img id="main_img" src="(.+?)"' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
 o0OOoo0OO0OOO = i1iiiii1 . replace ( '.jpg' , '' ) . replace ( 'http://' , '' )
 iI1iI1I1i1I = o0OOoo0OO0OOO . split ( '/' )
 O0iII1 = len ( iI1iI1I1i1I )
 IIII1i = O0iII1 - 1
 Ii1IIIIi1ii1I = 1
 IiiIiI1Ii1i = ""
 for i1iIi in iI1iI1I1i1I :
  if Ii1IIIIi1ii1I <= IIII1i :
   IiiIiI1Ii1i = IiiIiI1Ii1i + "/" + i1iIi
   Ii1IIIIi1ii1I = Ii1IIIIi1ii1I + 1
   if 30 - 30: O0 - iIii1I11I1II1 / OoooooooOO
 O0000OOO0 = 1
 IiiIiI1Ii1i = "http://" + IiiIiI1Ii1i + "/"
 if 51 - 51: I11iii11IIi / Ooooo / iIii1I111I11I
 while O0000OOO0 <= Oooo0 :
  url = IiiIiI1Ii1i + str ( O0000OOO0 ) + ".jpg"
  I1i11i ( "[COLOR lime]Page " + str ( O0000OOO0 ) + "[/COLOR]" , url , 9 , url , url , '' )
  O0000OOO0 = O0000OOO0 + 1
  if 6 - 6: iIii1I111I11I - OoOo * oooO . O00OooO0 / O0 * OoOo
def II11iI111i1 ( ) :
 if 95 - 95: OoooooooOO - Ooooo * I11iii11IIi + OOo0o0
 oo000OO00Oo = 'http://soccerstreams.net/getAllEvents/24?draw=1&columns[0][data]=start_date&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=competition_name&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=home_team&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=event_status&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=away_team&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=event_id&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=false&columns[5][search][value]=&columns[5][search][regex]=false&start=0&length=-1&search[value]=&search[regex]=false'
 if 10 - 10: OOoOoo00oo / i11iIiiIii
 o0O0O00 = o000o ( oo000OO00Oo )
 iIi11Ii1 = re . compile ( '{"start(.+?)}' ) . findall ( o0O0O00 )
 for o0o0OO0Oooooo in iIi11Ii1 :
  if not 'event_status":""' in str ( o0o0OO0Oooooo ) :
   o00oO = 1
  else : o00oO = 0
  O00O0Ooooo00 = re . compile ( 'date":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  O000 = re . compile ( 'competition_name":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  ooo0o000O = re . compile ( 'competition_logo":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  OOOO0o = re . compile ( 'home_team":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  oo0o0O0Oooooo = re . compile ( 'home_team_logo":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  i11IIIiI1I = re . compile ( 'home_team_slug":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  try :
   o0 = re . compile ( 'event_status":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  except : o0 = "null"
  iiiI1I1iIIIi1 = re . compile ( 'away_team":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  Iii = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  I1iiiiI1iI = re . compile ( 'away_team_logo":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  iIiiiii1i = re . compile ( 'event_id":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  try :
   iiIi1IIiI = re . compile ( 'game_minute":"(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
  except : iiIi1IIiI = "null"
  i1oO0OO0 = oo0o0O0Oooooo . split ( "-" )
  o0O0Oo00 = Iii . split ( "-" )
  OOOO0o = ""
  Oo0 = 0
  for o0OOoo0OO0OOO in i1oO0OO0 :
   Oo0 = Oo0 + 1
   O0Oo0o000oO = len ( i1oO0OO0 )
   if Oo0 < O0Oo0o000oO :
    OOOO0o = OOOO0o + " " + o0OOoo0OO0OOO
  iiiI1I1iIIIi1 = ""
  Oo0 = 0
  for o0OOoo0OO0OOO in o0O0Oo00 :
   Oo0 = Oo0 + 1
   O0Oo0o000oO = len ( o0O0Oo00 )
   if Oo0 < O0Oo0o000oO :
    iiiI1I1iIIIi1 = iiiI1I1iIIIi1 + " " + o0OOoo0OO0OOO
    if 99 - 99: OoOooOOOO * II111iiii * iI111IiI111I
  O00O0Ooooo00 = O00O0Ooooo00 + "!"
  O00O0Ooooo00 , oOooO0 = O00O0Ooooo00 . split ( ' ' )
  oOooO0 = oOooO0 . replace ( ":00!" , "" )
  o0OOoo0OO0OOO , iI1iI1I1i1I , O0iII1 = O00O0Ooooo00 . split ( "-" )
  O00O0Ooooo00 = O0iII1 + "-" + iI1iI1I1i1I + "-" + o0OOoo0OO0OOO
  oOooO0 = "[COLOR yellow][B]" + oOooO0 + "[/B][/COLOR]"
  O00O0Ooooo00 = "[COLOR red][B]" + O00O0Ooooo00 + "[/B][/COLOR]"
  oo000OO00Oo = 'http://soccerstreams.net/streams/' + iIiiiii1i + '/' + i11IIIiI1I + '_vs_' + I1iiiiI1iI
  OoOO0oo0o = '[COLOR lime][B]' + OOOO0o . title ( ) + ' vs ' + iiiI1I1iIIIi1 . title ( ) + '[/B][/COLOR]'
  oo000OO00Oo = oo000OO00Oo + "|SPLIT|" + OoOO0oo0o
  II11i1I11Ii1i = 'http://soccerstreams.net/images/teams/' + oo0o0O0Oooooo
  if o00oO == 0 :
   oOOOo00O00oOo ( oOooO0 + ' | ' + OoOO0oo0o + ' - ' + O00O0Ooooo00 + ' | [COLOR yellow]' + O000 + '[/COLOR]' , oo000OO00Oo , 30 , II11i1I11Ii1i , O0O , '' )
  else :
   iiIi1IIiI = iiIi1IIiI . replace ( '&#039;' , "'" )
   oOOOo00O00oOo ( "[COLOR red][B]" + iiIi1IIiI + " " + o0 + '[/B][/COLOR] | ' + OoOO0oo0o + ' - ' + O00O0Ooooo00 + ' | [COLOR yellow]' + O000 + '[/COLOR]' , oo000OO00Oo , 30 , II11i1I11Ii1i , O0O , '' )
   if 79 - 79: oO0 - iIii1I11I1II1 + iIii1I111I11I - iI111IiI111I
def OoOiIIiii ( name , url , iconimage ) :
 if 61 - 61: Ooooo . i1IIi / iI111IiI111I % i11iIiiIii * O00OooO0
 url , name = url . split ( "|SPLIT|" )
 i1i1i1I = name
 iiiiII1I = [ ]
 ooo00Ooo = [ ]
 Oo0o0O00 = [ ]
 if 83 - 83: OoOooOOOO + OoooooooOO
 Oo0 = 0
 I111IiiIi1 = 0
 o00oIi1IIiiIIi = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 O0ooo0O0oo0 = re . compile ( '<td class=""(.+?)<i class="fa fa-thumbs-up' , re . DOTALL ) . findall ( o00oIi1IIiiIIi )
 if 88 - 88: OoooooooOO + ii1IiIi11 * II111iiii % I1I1i1
 for I1I1iIi11i1II in O0ooo0O0oo0 :
  try :
   name = re . compile ( '<td class="clickable">(.+?)<' ) . findall ( I1I1iIi11i1II ) [ 1 ]
  except :
   name = re . compile ( '<td class="clickable">(.+?)</td>' ) . findall ( I1I1iIi11i1II ) [ 1 ]
  url = re . compile ( '<a href="(.+?)"' ) . findall ( I1I1iIi11i1II ) [ 0 ]
  ii1IIIIiI11 = re . compile ( '<td class="clickable">(.+?)</td>' ) . findall ( I1I1iIi11i1II ) [ 3 ]
  try :
   type = re . compile ( '<span class="tag stream-type-tag">(.+?)</span>' ) . findall ( I1I1iIi11i1II ) [ 0 ]
  except : type = "Unknown"
  iI1IIIii = re . compile ( '<td class="clickable"><img src=".+?" alt="(.+?)"></td>' ) . findall ( I1I1iIi11i1II ) [ 0 ]
  try :
   I1i11ii11 = re . compile ( '<span class="tag quality-tag">(.+?)</span>' ) . findall ( I1I1iIi11i1II ) [ 0 ]
  except : I1i11ii11 = "Unknown"
  name = name . lstrip ( " " )
  name = name . replace ( "  " , "" ) . replace ( " " , "" ) . replace ( '<img src="http://soccerstreams.net/images/verified.png" alt="">' , "" )
  if "1080" in I1i11ii11 : I1i11ii11 = "[COLOR white][B]1080P[/B][/COLOR]"
  elif "720" in I1i11ii11 : I1i11ii11 = "[COLOR dodgerblue][B]720P[/B][/COLOR]"
  elif "520" in I1i11ii11 : I1i11ii11 = "[COLOR yellow][B]520P[/B][/COLOR]"
  elif "480" in I1i11ii11 : I1i11ii11 = "[COLOR green][B]480P[/B][/COLOR]"
  elif "ace" in I1i11ii11 . lower ( ) : I1i11ii11 = "[COLOR red][B]ACESTREAM[/B][/COLOR]"
  else : I1i11ii11 = "[COLOR grey][B]UNKNOWN[/B][/COLOR]"
  if "acestream" in url :
   I1i11ii11 = "[COLOR red][B]ACESTREAM[/B][/COLOR]"
  if "ace" in type . lower ( ) :
   type = ""
  name = "[COLOR red]" + iI1IIIii . upper ( ) + "[/COLOR] - [COLOR blue][B]" + name . title ( ) + "[/B][/COLOR] - " + I1i11ii11 + " [COLOR orange]" + type + "[/COLOR] | [COLOR white]Bitrate: " + ii1IIIIiI11 + "[/COLOR]"
  if "acestream" in url :
   I111IiiIi1 = I111IiiIi1 + 1
   if os . path . exists ( PLEXUS_PATH ) :
    iiiiII1I . append ( url )
    ooo00Ooo . append ( name )
    Oo0 = Oo0 + 1
  else :
   iiiiII1I . append ( url )
   ooo00Ooo . append ( name )
   Oo0 = Oo0 + 1
   if 81 - 81: oooO - ii1IiIi11 % OoOo - oO0 / I1I1i1
 o00 = xbmcgui . Dialog ( )
 if Oo0 == 0 :
  if I111IiiIi1 >= 1 :
   o00 . ok ( i1 , "There are acestream links available, however you do not have Plexus set up. Please install Plexus to use these links." )
  else :
   o00 . ok ( i1 , "Sorry, there are no streams available at this time." )
 else :
  i1i1i1I = '[COLOR mediumpurple]' + i1i1i1I + '[/COLOR]'
  if 4 - 4: OoooooooOO - i1IIi % iIii1I111I11I - oooO * OOoOoo00oo
  o0O = o00 . select ( i1i1i1I , ooo00Ooo )
  if o0O < 0 :
   quit ( )
  else :
   url = iiiiII1I [ o0O ]
   o000O0o = ooo00Ooo [ o0O ]
   name = urllib . quote_plus ( ooo00Ooo [ o0O ] )
   import liveresolver
   import urlresolver
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
    oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
    oO . setPath ( iiI )
    xbmc . Player ( ) . play ( iiI , oO , False )
   elif liveresolver . isValid ( url ) == True :
    url = liveresolver . resolve ( url )
    oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
    oO . setPath ( iiI )
    xbmc . Player ( ) . play ( iiI , oO , False )
   elif "acestream" in url :
    o00 . ok ( "22" , url )
    url = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+" + name
   else :
    if '.m3u8' in url :
     url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
    elif '.ts' in url :
     url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + iconimage
    else :
     i1iI1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=' + name + '%26url='
     iI1iII1 = "/"
     if not o000O0o . endswith ( iI1iII1 ) :
      oO0OOoo0OO = o000O0o + "/"
     else :
      oO0OOoo0OO = o000O0o
     url = i1iI1 + iiiiII1I [ o0O ] + "%26referer=" + oO0OOoo0OO
    oO = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
    oO . setPath ( url )
    xbmc . Player ( ) . play ( url , oO , False )
    if 85 - 85: OoooooooOO * iIii1I11I1II1 . O00OooO0 / OoooooooOO % I11iii11IIi % O0
def I1iii ( url ) :
 if 86 - 86: iI1 * O0 * Ooooo
 Ooo0oo = 1
 url = 'http://hdvidmusic.com'
 IIi11IIiIii1 = o000o ( url )
 I1iIII1 = re . compile ( '<a href="([^"]*)">>></a></div>' , re . DOTALL ) . findall ( IIi11IIiIii1 ) [ 0 ]
 I1iIII1 = I1iIII1 . replace ( '?page=' , '' )
 iIii = int ( I1iIII1 )
 if 84 - 84: OoOooOOOO % i1IIi
 url = 'http://hdvidmusic.com/?page=' + str ( Ooo0oo )
 while Ooo0oo <= iIii :
  if 70 - 70: I1I1i1 . OoooooooOO - O00OooO0
  url = 'http://hdvidmusic.com/?page=' + str ( Ooo0oo )
  if 30 - 30: iI1 % I11iii11IIi
  o0O0O00 = o000o ( url )
  iIi11Ii1 = re . compile ( '<div class="cell_container">(.+?)<!--div class="video_rating">' , re . DOTALL ) . findall ( o0O0O00 )
  if 89 - 89: iI111IiI111I + OoooooooOO + iI111IiI111I * i1IIi + iIii1I11I1II1 % ii1IiIi11
  for O0ooo0O0oo0 in iIi11Ii1 :
   oo00oO0o = re . compile ( '<a title="(.+?)" href=".+?">' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   o0O0O00 = re . compile ( '<a title=".+?" href="(.+?)">' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   oOo0oOIIi1IIIIi = re . compile ( 'src="(.+?)"/>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   OOOoO = re . compile ( '<div class="video_quality">(.+?)</div>' , re . DOTALL ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   o00oIi1IIiiIIi = 'http://hdvidmusic.com' + o0O0O00
   I1i = 'http://hdvidmusic.com' + oOo0oOIIi1IIIIi
   I1i11i ( "[COLOR lime]" + oo00oO0o + "[/COLOR]" , o00oIi1IIiiIIi , 29 , I1i , O0O , '' )
  Ooo0oo = Ooo0oo + 1
  if 12 - 12: OoooooooOO
  if 20 - 20: i1IIi - ii1IiIi11
def ii1ii11 ( url ) :
 if 84 - 84: O0 . ii1IiIi11 - II111iiii . OoOo / II111iiii
 o00oIi1IIiiIIi = o000o ( url ) . replace ( '?' , '' )
 iii1 = re . compile ( '<iframe id\=.+?www(.+?)aut' ) . findall ( o00oIi1IIiiIIi ) [ 0 ]
 id = iii1 . split ( '/' ) [ - 1 ]
 url = 'plugin://plugin.video.youtube/play/?video_id=' + id
 xbmc . Player ( ) . play ( url )
 if 32 - 32: iIii1I111I11I . Ooooo . OoooooooOO - oO0 + OoOooOOOO
def ooO0oO00O0o ( url ) :
 if 70 - 70: iI111IiI111I
 if 16 - 16: O00OooO0 - OoooooooOO % I1I1i1
 o0O0O00 = o000o ( url ) . replace ( '&amp;' , 'and' )
 if 36 - 36: oooO
 if 84 - 84: iI111IiI111I . oO0 . II111iiii . ii1IiIi11 / iIii1I111I11I % iI1
 if 57 - 57: I11iii11IIi % ii1IiIi11 - oooO . I11iii11IIi / I1I1i1 % O00OooO0
 if 56 - 56: OoOooOOOO . O00OooO0 . Ooooo * OOo0o0 . OoOo / O0
 if 23 - 23: i1IIi + O00OooO0 + Ooooo + oO0
 if 12 - 12: iIii1I11I1II1 - iI1 + i11iIiiIii
 if 10 - 10: I11iii11IIi - i1IIi - OoOo % I1I1i1
 iIi11Ii1 = re . compile ( '<li.+?href="(.+?)".+?>(.+?)</a.+?li>' ) . findall ( o0O0O00 )
 for O0ii1ii1ii , oo00oO0o in iIi11Ii1 :
  if O0ii1ii1ii . find ( 'categ' ) != - 1 :
   iIIII1i = url + O0ii1ii1ii
   O000O0oOO0 ( "[COLOR lime]" + oo00oO0o + "[/COLOR]" , iIIII1i , 25 , Oo , O0O , '' )
   if 76 - 76: O00OooO0 + OoOo
def Iiii11iIi1 ( url ) :
 if 40 - 40: ii1IiIi11 % oO0 . iI111IiI111I
 o00oIi1IIiiIIi = o000o ( url ) . replace ( '&#8217;' , "'" )
 OOO0oOOo00O = re . compile ( '<div class="post-thumbnail".+?<a href="(.+?)".+?src="(.+?)".+?alt="(.+?)"' , re . DOTALL ) . findall ( o00oIi1IIiiIIi )
 for url , oOo0oOIIi1IIIIi , OoOO0oo0o in OOO0oOOo00O :
  OO0o = o000o ( url )
  III111i11IiI = re . compile ( '<div class=\'video\'><iframe width=".+?" height=".+?" src="(.+?)"' ) . findall ( OO0o )
  for O0000 in III111i11IiI :
   try :
    ooO00O0O0 = O0000 . split ( "/embed/" ) [ 1 ]
    iII1I1 = "plugin://plugin.video.youtube/play/?video_id=" + ooO00O0O0
    I1i11i ( "[COLOR lime]" + OoOO0oo0o . title ( ) + "[/COLOR]" , iII1I1 , 7 , oOo0oOIIi1IIIIi , O0O , '' )
   except : pass
   if 85 - 85: O00OooO0 * OOoOoo00oo
 try :
  ii1iii11i1 = re . compile ( '<link rel="next" href="(.+?)" />' , re . DOTALL ) . findall ( o00oIi1IIiiIIi ) [ 0 ]
  O000O0oOO0 ( "[COLOR red]Next Page -->[/COLOR]" , ii1iii11i1 , 25 , Oo , O0O , '' )
 except : pass
 if 4 - 4: Ooooo . Ooooo % iI1 % iIii1I111I11I / iIii1I111I11I
def II11iIiiI1111 ( url ) :
 if 71 - 71: OOoOoo00oo % iIii1I111I11I - II111iiii * OoooooooOO
 o0O0O00 = o000o ( url )
 iIi11Ii1 = re . compile ( '<a class="site_tag(.+?)/a>' ) . findall ( o0O0O00 )
 if 69 - 69: OOoOoo00oo / I1I1i1
 for o0O0O00 in iIi11Ii1 :
  url = re . compile ( 'href="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
  OoOO0oo0o = re . compile ( '/i>(.+?)<' ) . findall ( o0O0O00 ) [ 0 ]
  O0ii1ii1ii = "http://xoxfuck.com" + url
  O000O0oOO0 ( "[COLOR lime]" + OoOO0oo0o . title ( ) + "[/COLOR]" , O0ii1ii1ii , 17 , Oo , O0O , '' )
  if 43 - 43: iI1 . I11iii11IIi / OoooooooOO % OoooooooOO
def iIIIII1iiiiII ( name , url , iconimage ) :
 if 54 - 54: i1IIi
 ii1I11 = name . split ( '(' ) [ 1 ]
 ii1I11 = ii1I11 . replace ( ')' , '' ) . replace ( "[/COLOR]" , '' )
 ii1I11 = int ( ii1I11 )
 oO0OO00o00 = url
 if 39 - 39: iI111IiI111I / I1I1i1 % oO0 % i11iIiiIii
 o0o0Ooo0 = 0
 OoO000O = 1
 Oo0 = 0
 I111IiiIi1 = 6
 if 94 - 94: OOo0o0 . O0 / iIii1I111I11I . iI1 - i1IIi
 Oo0oO0ooo . create ( "STREAM ARMY" , "[COLOR lime]Getting video 1 of " + str ( ii1I11 ) + "![/COLOR]" )
 Oo0oO0ooo . update ( 0 )
 while OoO000O < 2000 :
  if 26 - 26: oO0 - oooO . OOoOoo00oo
  if Oo0 == 0 :
   o0O0O00 = o000o ( oO0OO00o00 )
   if 65 - 65: iI1 % O0 % iIii1I11I1II1 * iIii1I111I11I
   iIi11Ii1 = re . compile ( '<div class="inner_block video_box">(.+?)</a>' ) . findall ( o0O0O00 )
   for o0o0OO0Oooooo in iIi11Ii1 :
    O0ii1ii1ii = re . compile ( 'href="(.+?)">' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    iconimage = re . compile ( 'src="(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    o0o0Ooo0 = o0o0Ooo0 + 1
    iIIIIIiI1I1 = 100 * int ( o0o0Ooo0 ) / int ( ii1I11 )
    Oo0oO0ooo . update ( iIIIIIiI1I1 , "[COLOR lime]Getting video " + str ( o0o0Ooo0 ) + " of " + str ( ii1I11 ) + "![/COLOR]" )
    I1i11i ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , O0ii1ii1ii , 18 , iconimage , O0O , '' )
   Oo0 = Oo0 + 1
  else :
   url = oO0OO00o00 + '?load_more=10&loaded=' + str ( I111IiiIi1 )
   o0O0O00 = o000o ( url )
   o0O0O00 = o0O0O00 . replace ( '\\' , '' )
   if 15 - 15: iIii1I111I11I * I1I1i1 % iI1 * iIii1I11I1II1 - i11iIiiIii
   if "no_more_videos" in o0O0O00 :
    OoO000O = 2001
    if 60 - 60: I11iii11IIi * iI111IiI111I % oO0 + OoOooOOOO
   iIi11Ii1 = re . compile ( '<div class="(.+?)</a>' ) . findall ( o0O0O00 )
   for o0o0OO0Oooooo in iIi11Ii1 :
    if OoO000O < 2000 :
     O0ii1ii1ii = re . compile ( 'href="(.+?)">' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
     name = re . compile ( '<h2.+?>(.+?)<' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
     iconimage = re . compile ( 'src="(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
     o0o0Ooo0 = o0o0Ooo0 + 1
     iIIIIIiI1I1 = 100 * int ( o0o0Ooo0 ) / int ( ii1I11 )
     Oo0oO0ooo . update ( iIIIIIiI1I1 , "[COLOR lime]Getting video " + str ( o0o0Ooo0 ) + " of " + str ( ii1I11 ) + "![/COLOR]" )
     I1i11i ( "[COLOR lime]" + name . title ( ) + "[/COLOR]" , O0ii1ii1ii , 18 , iconimage , O0O , '' )
   I111IiiIi1 = I111IiiIi1 + 10
  OoO000O = OoO000O + 1
 Oo0oO0ooo . close
 if 52 - 52: i1IIi
def o000 ( ) :
 if 94 - 94: OOoOoo00oo + O0 / ii1IiIi11 . I11iii11IIi + oooO . iIii1I11I1II1
 oo000OO00Oo = 'http://www.filmon.com/tv/bbc-news'
 if 62 - 62: OOo0o0 / I11iii11IIi - iI1 - I11iii11IIi + i11iIiiIii + i1IIi
 o0O0O00 = o000o ( oo000OO00Oo )
 iIi11Ii1 = re . compile ( '{"group_id"(.+?)channels_count' ) . findall ( o0O0O00 )
 for I1i11II in iIi11Ii1 :
  OoOO0oo0o = re . compile ( 'title":"(.+?)"' ) . findall ( I1i11II ) [ 0 ]
  O000O0oOO0 ( "[COLOR lime]" + OoOO0oo0o + "[/COLOR]" , I1i11II , 27 , Oo , O0O , '' )
  if 31 - 31: OoOooOOOO / Ooooo * OOoOoo00oo . II111iiii
def oooOO0OO0O ( url ) :
 if 78 - 78: iIii1I111I11I / II111iiii % OOo0o0
 iIi11Ii1 = re . compile ( '{"id"(.+?)}' ) . findall ( url )
 for oO00OoOO in iIi11Ii1 :
  OoOO0oo0o = re . compile ( ':.+?big_logo":".+?".+?title":"(.+?)".+?alias":".+?"' ) . findall ( oO00OoOO ) [ 0 ]
  II11i1I11Ii1i = re . compile ( ':.+?big_logo":"(.+?)".+?title":".+?".+?alias":".+?"' ) . findall ( oO00OoOO ) [ 0 ]
  url = re . compile ( ':.+?big_logo":".+?".+?title":".+?".+?alias":"(.+?)"' ) . findall ( oO00OoOO ) [ 0 ]
  II11i1I11Ii1i = II11i1I11Ii1i . replace ( '\\' , '' )
  O0ii1ii1ii = 'https://www.filmon.com/tv/' + url
  oOOOo00O00oOo ( "[COLOR lime]" + OoOO0oo0o + "[/COLOR]" , O0ii1ii1ii , 2 , II11i1I11Ii1i , O0O , '' )
  if 18 - 18: OoOo - OOo0o0 % i1IIi + O0 + i11iIiiIii + i1IIi
def oOo0o0O ( name , url , iconimage ) :
 if 83 - 83: OOoOoo00oo / oooO / oooO + OOoOoo00oo * iI111IiI111I + OOoOoo00oo
 o00oIi1IIiiIIi = o000o ( url )
 O0ooo0O0oo0 = re . compile ( '<video class="video_tag_item" poster=".+?" preload="auto" controls="" src="(.+?)">' ) . findall ( o00oIi1IIiiIIi ) [ 0 ]
 oo00oO0o = re . compile ( '<title>(.+?)</title>' ) . findall ( o00oIi1IIiiIIi ) [ 0 ]
 oo00oO0o = oo00oO0o . split ( ' | ' ) [ 0 ]
 oo00oO0o = oo00oO0o . strip ( ' ' )
 oO = xbmcgui . ListItem ( oo00oO0o , iconImage = iconimage , thumbnailImage = iconimage )
 xbmc . Player ( ) . play ( O0ooo0O0oo0 , oO , False )
 if 36 - 36: OOo0o0 + OOoOoo00oo - OoooooooOO . OoOooOOOO . OoooooooOO / I1I1i1
def o00O ( url ) :
 if 48 - 48: O00OooO0 . i11iIiiIii
 try :
  if not "http" in url :
   if "https://" in url :
    url = url . replace ( "https://" , "http://" )
   o0O0O00 = o000o ( url )
   OoOO0oo0o = re . compile ( '<title>(.+?)</title>' ) . findall ( o0O0O00 ) [ 0 ] . split ( ' (' ) [ 0 ]
   IIi = re . compile ( '<td width="100%" class="entry"><a href="(.+?)" title="(.+?)">' ) . findall ( o0O0O00 )
   II11i1I11Ii1i = re . compile ( '<meta property="og:image" content="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   if 58 - 58: II111iiii
   for url , oo00oO0o in IIi :
    I1i11i ( oo00oO0o , url , 14 , II11i1I11Ii1i , O0O , '' )
  else :
   o0O0O00 = o000o ( url )
   if 19 - 19: iI1 - ii1IiIi11 . II111iiii - oO0 . Ooooo * OoooooooOO
   iIi11Ii1 = re . compile ( '<a class="addthis_counter addthis_pill_style"></a>(.+?)<strong>Sponsored Content</strong>' ) . findall ( o0O0O00 ) [ 0 ]
   IiiIiI1Ii1i = str ( iIi11Ii1 )
   II1IIiiIiI = re . compile ( '<td width="100%" class="entry">(.+?)</td>' ) . findall ( IiiIiI1Ii1i )
   O0oOo0OOOoO = re . compile ( '<meta property="og:image" content="(.+?)"/>' , re . DOTALL ) . findall ( o0O0O00 ) [ 0 ]
   for o0o0OO0Oooooo in II1IIiiIiI :
    OoOO0oo0o = re . compile ( 'title="(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    url = re . compile ( '<a href="(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    oo00oO0o = OoOO0oo0o . split ( ' - ' ) [ 1 ]
    if not 'http' in url : url = 'http:' + url
    I1i11i ( "[COLOR lime]" + OoOO0oo0o . title ( ) + "[/COLOR]" , url , 14 , O0oOo0OOOoO , O0O , '' )
 except :
  o00 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
  if 11 - 11: OOoOoo00oo * oO0
def iIi1IiI ( ) :
 if 14 - 14: Ooooo % OoOooOOOO % I1I1i1 - i11iIiiIii
 IiiIiI1Ii1i = ''
 o0OO000ooOo = xbmc . Keyboard ( IiiIiI1Ii1i , 'Search For A Movie' )
 o0OO000ooOo . doModal ( )
 if o0OO000ooOo . isConfirmed ( ) :
  oOo00OooO0oO = o0OO000ooOo . getText ( )
  I1IIi = oOo00OooO0oO
  IiiIiI1Ii1i = oOo00OooO0oO . replace ( ' ' , '+' )
  if not len ( IiiIiI1Ii1i ) > 1 :
   o00 . ok ( "STREAM ARMY" , "No search term was entered." )
   quit ( )
   if 69 - 69: iIii1I111I11I + I1I1i1 + II111iiii - I11iii11IIi / ii1IiIi11
  IiiIiI1Ii1i = IiiIiI1Ii1i . replace ( ' ' , '+' )
  oo000OO00Oo = "http://housemovie.to/search?q=" + IiiIiI1Ii1i
  o0O0O00 = o000o ( oo000OO00Oo )
  iIi11Ii1 = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
  if 74 - 74: ii1IiIi11 - oooO + i1IIi . I11iii11IIi + oooO - ii1IiIi11
  for o0o0OO0Oooooo in iIi11Ii1 :
   try :
    OoOO0oo0o = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    oo000OO00Oo = re . compile ( '<a href="(.+?)" class="fig_holder">' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    II11i1I11Ii1i = re . compile ( 'src="(.+?)"' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    try :
     Ii = re . compile ( '<span class="imdb">(.+?)</span>' ) . findall ( o0o0OO0Oooooo ) [ 0 ]
    except : Ii = "IMDB Rating Unknown"
    if not "http" in oo000OO00Oo :
     oo000OO00Oo = "http://housemovie.to" + oo000OO00Oo
     I1i11i ( "[COLOR lime]" + OoOO0oo0o . title ( ) + "[/COLOR] - [COLOR yellow][I]" + Ii + "[/I][/COLOR]" , oo000OO00Oo , 21 , II11i1I11Ii1i , O0O , '' )
   except : pass
   if 15 - 15: O0 + O0 / I1I1i1 . OoOooOOOO * ii1IiIi11 - iI1
   if 95 - 95: oO0 - oooO / II111iiii % iI1 . OOoOoo00oo
def iii1IIII1iii11I ( url ) :
 if 97 - 97: OoooooooOO - iI111IiI111I
 o0O0O00 = o000o ( url )
 if 58 - 58: iIii1I11I1II1 + O0
 iIi11Ii1 = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 30 - 30: OoOo % O00OooO0 * oooO - iI1 * iIii1I111I11I % OoOo
 for O0ooo0O0oo0 in iIi11Ii1 :
  try :
   OoOO0oo0o = re . compile ( '<a href=".+?">(.+?)</a>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   O0ii1ii1ii = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   if "genres" in O0ii1ii1ii :
    O0ii1ii1ii = "http://housemovie.to" + O0ii1ii1ii
    O000O0oOO0 ( "[COLOR lime]" + OoOO0oo0o . title ( ) + "[/COLOR]" , O0ii1ii1ii , 19 , Oo , O0O , '' )
  except : pass
  if 46 - 46: i11iIiiIii - O0 . OoOooOOOO
def Oo0O ( url ) :
 if 1 - 1: O0 / O00OooO0 % iI111IiI111I . I1I1i1 + Ooooo
 o0O0O00 = o000o ( url )
 if 27 - 27: iI111IiI111I % OoooooooOO + Ooooo % i1IIi / OoOooOOOO / OoooooooOO
 iIi11Ii1 = re . compile ( '<li>(.+?)</li>' ) . findall ( o0O0O00 )
 if 11 - 11: oooO % iIii1I111I11I - i11iIiiIii - OoOooOOOO + OoOo + Ooooo
 for O0ooo0O0oo0 in iIi11Ii1 :
  try :
   OoOO0oo0o = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   Ii = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   if "(SOON)" in OoOO0oo0o :
    o0ooOo0OOOO0o = OoOO0oo0o . split ( "(SOON)" ) [ 0 ]
    OoOO0oo0o = o0ooOo0OOOO0o . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
   else : OoOO0oo0o = OoOO0oo0o . title ( )
   O0ii1ii1ii = re . compile ( '<a href="(.+?)">.+?</a>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   II11i1I11Ii1i = re . compile ( 'src="(.+?)"' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
   if "watch" in O0ii1ii1ii :
    O0ii1ii1ii = "http://housemovie.to" + O0ii1ii1ii
    I1i11i ( "[COLOR lime]" + OoOO0oo0o + " [/COLOR]-[COLOR yellow][I] " + Ii + "[/I][/COLOR]" , O0ii1ii1ii , 21 , II11i1I11Ii1i , O0O , '' )
    if 98 - 98: oooO + i1IIi . I11iii11IIi - II111iiii - OOoOoo00oo
  except : pass
  if 24 - 24: I1I1i1 - i1IIi + ii1IiIi11
  if 38 - 38: OoooooooOO / iI1 . O0 / i1IIi / I1I1i1 + iIii1I11I1II1
  if 96 - 96: O00OooO0
def i1I11iIII1i1I ( name , url , iconimage ) :
 if 63 - 63: I1I1i1 + iI111IiI111I - II111iiii
 i1iIIi1I1I11 = [ ]
 iii1III1i = [ ]
 iiiIi = [ ]
 II1Iii = [ ]
 O0oooo0OoO0oo = [ ]
 if 16 - 16: I11iii11IIi * II111iiii / iIii1I11I1II1 - O00OooO0
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 3 - 3: I11iii11IIi * OoOo + II111iiii - oO0
 iIi11Ii1 = re . compile ( '<div class="fig_holder">(.+?)</div>' ) . findall ( o0O0O00 )
 for O0ooo0O0oo0 in iIi11Ii1 :
  name = re . compile ( '<span class="item_name">(.+?)</span>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
  O0ii1ii1ii = re . compile ( '<a href="(.+?)"' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
  iconimage = re . compile ( 'src="(.+?)"' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
  try :
   Ii = re . compile ( 'imdb">(.+?)</span>' ) . findall ( O0ooo0O0oo0 ) [ 0 ]
  except : Ii = "0.0"
  if "imdb" in Ii . lower ( ) :
   Ii = Ii . replace ( "IMDB: " , "" ) . replace ( " " , "" )
  if not "." in Ii :
   Ii = Ii + ".0"
   if 97 - 97: iI1 / OoOooOOOO - OOoOoo00oo - I11iii11IIi - I11iii11IIi
  if "(SOON)" in name :
   o0ooOo0OOOO0o = name . split ( "(SOON)" ) [ 0 ]
   name = o0ooOo0OOOO0o . title ( ) + '[COLOR red](Coming Soon)[/COLOR]'
  else : name = name . title ( )
  O0ii1ii1ii = "http://housemovie.to" + O0ii1ii1ii
  if 54 - 54: I1I1i1 + I11iii11IIi / O00OooO0 . I11iii11IIi * OOo0o0
  i1iIIi1I1I11 . append ( name )
  iii1III1i . append ( O0ii1ii1ii )
  iiiIi . append ( iconimage )
  II1Iii . append ( Ii )
  O0oooo0OoO0oo = list ( zip ( II1Iii , i1iIIi1I1I11 , iii1III1i , iiiIi ) )
  if 1 - 1: OOo0o0 * oO0 . i1IIi / I1I1i1 . iI1 + I1I1i1
 IIiIi1 = sorted ( O0oooo0OoO0oo , reverse = True )
 if 91 - 91: II111iiii % O00OooO0 % Ooooo + II111iiii / OoOooOOOO
 for Ii , name , O0ii1ii1ii , iconimage in IIiIi1 :
  if Ii == "0.0" :
   Ii = "IMDB Rating Unknown"
  else : Ii = "IMDB: " + Ii
  I1i11i ( "[COLOR lime]" + name + " [/COLOR]-[COLOR yellow][I] " + Ii + "[/I][/COLOR]" , O0ii1ii1ii , 21 , iconimage , O0O , '' )
  if 62 - 62: OoooooooOO - i11iIiiIii
 try :
  Iii1oOO = re . compile ( '<a href="([^"]*)" class="page_next">Next</a>' ) . findall ( o0O0O00 ) [ 0 ]
  O000O0oOO0 ( "[COLOR red]Next Page -->[/COLOR]" , Iii1oOO , 19 , Oo , O0O , '' )
 except : pass
 if 32 - 32: OOo0o0 * I11iii11IIi % OoOo * iIii1I111I11I . O0
def i11i1i1I1iI1 ( name , url , iconimage ) :
 if 53 - 53: oooO + I11iii11IIi / i11iIiiIii - OOoOoo00oo * OoOooOOOO / OoooooooOO
 ooo00Ooo = [ ]
 iiiiII1I = [ ]
 Oo0o0O00 = [ ]
 if 89 - 89: iIii1I11I1II1 / I11iii11IIi - II111iiii / iIii1I111I11I . i11iIiiIii . iIii1I111I11I
 o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 48 - 48: O0 + O0 . iI111IiI111I - OoOo
 O0ooo0O0oo0 = re . compile ( '<div class="md_full_cell">(.+?)</div>' ) . findall ( o0O0O00 )
 if 63 - 63: OoOooOOOO
 for ii1 in O0ooo0O0oo0 :
  try :
   url = re . compile ( '<a href="(.+?)"' ) . findall ( ii1 ) [ 0 ]
   oo00oO0o = re . compile ( 'rel="nofollow">(.+?)</a>' ) . findall ( ii1 ) [ 0 ]
   url = "http://housemovie.to" + url
   for Oo0OOo0Oo0OOo0 in oOOoo00O0O :
    if Oo0OOo0Oo0OOo0 . lower ( ) in oo00oO0o . lower ( ) :
     if 19 - 19: ii1IiIi11 + II111iiii
     ooo00Ooo . append ( oo00oO0o )
     iiiiII1I . append ( url )
     Oo0o0O00 . append ( iconimage )
  except : pass
  if 84 - 84: O0 - II111iiii . I1I1i1 / OoOooOOOO . OoooooooOO + i11iIiiIii
  if 86 - 86: ii1IiIi11 / OOoOoo00oo - OOoOoo00oo + iI1 + OoOooOOOO
 name = '[COLOR lime]' + name + '[/COLOR]'
 o0O = o00 . select ( name , ooo00Ooo )
 if o0O < 0 :
  quit ( )
 else :
  url = iiiiII1I [ o0O ]
  url = str ( url )
  Oo = Oo0o0O00 [ o0O ]
  Oo = str ( Oo )
  if 33 - 33: OOoOoo00oo . O00OooO0 . Ooooo . i1IIi
  o0O0O00 = o000o ( url ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 49 - 49: iI1
  url = re . compile ( '<a href="([^"]*)" target="_blank" class="button_type_1">' ) . findall ( o0O0O00 ) [ 0 ]
  if 84 - 84: ii1IiIi11 - I1I1i1 / O0 - iI111IiI111I
  try :
   import urlresolver
   if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
    iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
    oO = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
    oO . setPath ( iiI )
    xbmc . Player ( ) . play ( iiI , oO , False )
   else : o00 . ok ( i1 , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
  except :
   o00 . ok ( i1 , "[COLOR yellow]Sorry, It seems the source link is down,\n Please try another link!\n Report The Dead Link To\n @Nemzzy668 and @_Manc_[/COLOR]" )
   if 21 - 21: O0 * O0 % iI1
def o00ooo ( name , url , iconimage ) :
 if 31 - 31: O0 * OOoOoo00oo % OOoOoo00oo / OoOooOOOO / ii1IiIi11 / oO0
 iconimage = "null"
 if 11 - 11: OOo0o0 + Ooooo - OoooooooOO / oO0
 Oo0 = 0
 iiiiII1I = [ ]
 ooo00Ooo = [ ]
 Oo0o0O00 = [ ]
 if 34 - 34: OoOo
 i1iI1IIi11i1II = 1
 OO0ooo0o0 = 0
 if "http" in url :
  if 69 - 69: iI1 - iI111IiI111I
  Oo0oO0ooo . create ( "Stream Army" , "[COLOR white][B]Status: [/B][/COLOR][COLOR red]NOT CONNECTED[/COLOR]" )
  Oo0oO0ooo . update ( 0 )
  if 16 - 16: I1I1i1
  while i1iI1IIi11i1II < 11 :
   iIIIIIiI1I1 = 100 * int ( i1iI1IIi11i1II ) / int ( 10 )
   Oo0oO0ooo . update ( iIIIIIiI1I1 , "" , "[COLOR lime]Connection attempt " + str ( i1iI1IIi11i1II ) + " of 10[/COLOR]" )
   o0O0O00 = o000o ( url )
   if 14 - 14: i1IIi - O0 % I1I1i1
   if OO0ooo0o0 == 0 :
    i1iI1IIi11i1II = i1iI1IIi11i1II + 1
    oo00oO0o = re . compile ( 'title="(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
    oo00oO0o = oo00oO0o . split ( " - " ) [ 0 ]
    if 92 - 92: iIii1I111I11I % O00OooO0 / iI1 % iI1 * I11iii11IIi
    OooO00oOOo0Oo = re . compile ( '<td class="entry">(.+?)target' ) . findall ( o0O0O00 )
    for ii1 in OooO00oOOo0Oo :
     IIiIIIIii = 1
     iIiI1 = len ( ii1 )
     iIIiI1ii = 100 * int ( IIiIIIIii ) / int ( iIiI1 )
     Oo0oO0ooo . update ( iIIiI1ii , "[COLOR white][B]Status: [/B][/COLOR][COLOR lime]CONNECTED[/COLOR]" , "[COLOR lime]Filtering links " + str ( IIiIIIIii ) + " of " + str ( iIiI1 ) + " possible matches[/COLOR]" )
     if 78 - 78: O0 * oooO
     if not "putlocker.bypassed.info" in ii1 :
      iIii1 = re . compile ( '<a rel=".+?" href="(.+?)"' ) . findall ( ii1 ) [ 0 ]
      Oo0 = Oo0 + 1
      ooo00Ooo . append ( "Link " + str ( Oo0 ) )
      iiiiII1I . append ( iIii1 )
      Oo0o0O00 . append ( iconimage )
     OO0ooo0o0 = 1
     i1iI1IIi11i1II = 12
     IIiIIIIii = IIiIIIIii + 1
     if 62 - 62: iIii1I11I1II1 + O00OooO0 . I1I1i1 / Ooooo % O0 . iI111IiI111I
   if Oo0oO0ooo . iscanceled ( ) :
    sys . exit ( )
   import time
   time . sleep ( 1 )
   i1iI1IIi11i1II = i1iI1IIi11i1II + 1
   if 93 - 93: i11iIiiIii % iIii1I11I1II1 % i11iIiiIii + OOoOoo00oo / OOoOoo00oo / II111iiii
 else :
  if 49 - 49: oooO . iI1 . i11iIiiIii - II111iiii / iIii1I111I11I
  o00oIi1IIiiIIi = o000o ( url )
  O0ooo0O0oo0 = re . compile ( '<td class="entry">(.+?)</tr>' ) . findall ( o00oIi1IIiiIIi )
  if 62 - 62: oooO
  for ii1 in O0ooo0O0oo0 :
   url = re . compile ( 'href="(.+?)"' ) . findall ( ii1 ) [ 0 ]
   if not "putlocker.unblocked.ink" in url :
    Oo0 = Oo0 + 1
    ooo00Ooo . append ( "Link " + str ( Oo0 ) )
    iiiiII1I . append ( url )
    Oo0o0O00 . append ( iconimage )
    if 1 - 1: Ooooo / Ooooo - i11iIiiIii
    if 87 - 87: I1I1i1 / O0 * Ooooo / OOoOoo00oo
    if 19 - 19: iI111IiI111I + i1IIi . I11iii11IIi - I1I1i1
 if Oo0 == 0 :
  o00 . ok ( "Stream Army" , "Man Down, Man Down we couldn't get a stream!" )
  quit ( )
 name = '[COLOR lime]' + name + '[/COLOR]'
 o0O = o00 . select ( name , ooo00Ooo )
 if o0O < 0 :
  quit ( )
 else :
  url = iiiiII1I [ o0O ]
  url = str ( url )
  Oo = Oo0o0O00 [ o0O ]
  Oo = str ( Oo )
  import urlresolver
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
   oO = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
   oO . setPath ( iiI )
   xbmc . Player ( ) . play ( iiI , oO , False )
   if 16 - 16: OoOooOOOO + OoOo / OOoOoo00oo
   if 82 - 82: Ooooo * i11iIiiIii % II111iiii - OoooooooOO
   if 90 - 90: I1I1i1 . OoOooOOOO * i1IIi - i1IIi
   if 16 - 16: I11iii11IIi * i1IIi - OOoOoo00oo . Ooooo % ii1IiIi11 / OOoOoo00oo
def Ii11iI1ii1111 ( name , url , iconimage ) :
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = oO )
 xbmc . Player ( ) . play ( url , oO , False )
 if 19 - 19: II111iiii - i1IIi - oooO / oooO + OOo0o0
def o0OOOoO0 ( name , url , iconimage ) :
 if 51 - 51: I1I1i1 % OOo0o0 * OoooooooOO . i11iIiiIii
 name = name . replace ( '  ' , '' )
 if not 'f4m' in url :
  if '.m3u8' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + Oo
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url + '&amp;iconImage=' + Oo
 else : url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
 if 77 - 77: II111iiii
 import urlresolver
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
  oO = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  oO . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oO , False )
  quit ( )
 else :
  iiI = url
  oO = xbmcgui . ListItem ( name , iconImage = Oo , thumbnailImage = Oo )
  oO . setPath ( iiI )
  xbmc . Player ( ) . play ( iiI , oO , False )
  quit ( )
  if 42 - 42: iIii1I111I11I * iI111IiI111I . Ooooo * I11iii11IIi + OOo0o0
  if 25 - 25: ii1IiIi11 . I11iii11IIi + OoOooOOOO
  if 75 - 75: Ooooo - OOoOoo00oo % O00OooO0 + i11iIiiIii
  if 100 - 100: ii1IiIi11 + OOoOoo00oo - i11iIiiIii - II111iiii
def o0oo0O ( name , url , iconimage ) :
 if 40 - 40: OOo0o0 % oO0
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  i1II1 = url . split ( 'list=' ) [ 1 ]
  oo0O0o00 = Iii1ii1II11i + i1II1 + iI111iI
  oo000O0OoooO = urllib2 . Request ( oo0O0o00 )
  oo000O0OoooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  oo = urllib2 . urlopen ( oo000O0OoooO )
  o0O0O00 = oo . read ( )
  oo . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  iIi11Ii1 = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   ii1iii11i1 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   oo0O0o00 = IiII + ii1iii11i1 + iI1Ii11111iIi + i1II1 + i1i1II
   O000O0oOO0 ( 'Next Page >>' , oo0O0o00 , 2 , I1IiI , I11i )
  except : pass
  if 70 - 70: oO0
  if 46 - 46: ii1IiIi11 - i1IIi
  if 46 - 46: iI111IiI111I % iIii1I111I11I
  if 72 - 72: iIii1I11I1II1
  for name , iI1I1II1 in iIi11Ii1 :
   url = 'https://www.youtube.com/watch?v=' + iI1I1II1
   iconimage = 'https://i.ytimg.com/vi/' + iI1I1II1 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOOOo00O00oOo ( name , url , 2 , iconimage , I11i )
     if 92 - 92: OoooooooOO - OoooooooOO * oO0 % I11iii11IIi
 if 'https://www.googleapis.com/youtube/v3' in url :
  i1II1 = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  oo000O0OoooO = urllib2 . Request ( url )
  oo000O0OoooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  oo = urllib2 . urlopen ( oo000O0OoooO )
  o0O0O00 = oo . read ( )
  oo . close ( )
  o0O0O00 = o0O0O00 . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  iIi11Ii1 = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( o0O0O00 )
  try :
   ii1iii11i1 = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( o0O0O00 ) [ 0 ]
   oo0O0o00 = IiII + ii1iii11i1 + iI1Ii11111iIi + i1II1 + i1i1II
   O000O0oOO0 ( 'Next Page >>' , oo0O0o00 , 2 , I1IiI , I11i )
  except : pass
  if 77 - 77: iIii1I11I1II1 - i1IIi . OoOooOOOO
  if 26 - 26: OOoOoo00oo * Ooooo . i1IIi
  if 59 - 59: O0 + i1IIi - OOoOoo00oo
  for name , iI1I1II1 in iIi11Ii1 :
   url = 'https://www.youtube.com/watch?v=' + iI1I1II1
   iconimage = 'https://i.ytimg.com/vi/' + iI1I1II1 + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     oOOOo00O00oOo ( name , url , 2 , iconimage , I11i )
     if 62 - 62: i11iIiiIii % oooO . Ooooo . oooO
     if 84 - 84: i11iIiiIii * oO0
     if 18 - 18: oooO - iIii1I111I11I - OOo0o0 / iI111IiI111I - O0
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 30 - 30: O0 + iI1 + II111iiii
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  iiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True :
  iiI = liveresolver . resolve ( url )
 else : iiI = url
 oO = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 oO . setPath ( iiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oO )
 if 14 - 14: OOoOoo00oo / oooO - iIii1I11I1II1 - OoOooOOOO % OoOo
def I1iIiI1IiIIII ( url ) :
 if 18 - 18: OoOo % i11iIiiIii . iIii1I11I1II1 - O00OooO0
 try :
  OoOO0oo0o , url , II11i1I11Ii1i = url . split ( "!SASPLIT!" )
  oO = xbmcgui . ListItem ( OoOO0oo0o , iconImage = II11i1I11Ii1i , thumbnailImage = II11i1I11Ii1i )
  xbmc . Player ( ) . play ( url , oO , False )
 except :
  xbmc . Player ( ) . play ( url )
  if 80 - 80: I11iii11IIi + OoOooOOOO - i1IIi . iIii1I111I11I / OOoOoo00oo / I11iii11IIi
def o000o ( url ) :
 try :
  oo000O0OoooO = urllib2 . Request ( url )
  oo000O0OoooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
  oo = urllib2 . urlopen ( oo000O0OoooO )
  o0O0O00 = oo . read ( )
  oo . close ( )
  o0O0O00 = o0O0O00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 1 - 1: ii1IiIi11 + i11iIiiIii - I11iii11IIi / oooO + iI111IiI111I
  return o0O0O00
 except : quit ( )
 if 80 - 80: OoOooOOOO + OOoOoo00oo * iIii1I111I11I + oO0
def Oo0OoO00oOO0o ( url ) :
 if 75 - 75: ii1IiIi11 / OOoOoo00oo / oooO / Ooooo % OoOo + II111iiii
 if 4 - 4: O00OooO0 - I1I1i1 - Ooooo - ii1IiIi11 % i11iIiiIii / oO0
 try :
  oo000O0OoooO = urllib2 . Request ( url )
  oo000O0OoooO . add_header ( 'User-Agent' , 'obsession' )
  oo = urllib2 . urlopen ( oo000O0OoooO )
  o0O0O00 = oo . read ( )
  if 50 - 50: OoOo + i1IIi
  i11IiIIi11I = iii11I111 ( o0O0O00 )
  print "--------- decoded --------" , i11IiIIi11I
  oo . close ( )
  i11IiIIi11I = i11IiIIi11I . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  if 78 - 78: Ooooo
  return i11IiIIi11I
 except : quit ( )
 if 83 - 83: iIii1I11I1II1 % OOo0o0 % OOoOoo00oo % iI111IiI111I . iI1 % O0
def iI11Ii ( url ) :
 oo000O0OoooO = urllib2 . Request ( url )
 oo000O0OoooO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36' )
 oo = urllib2 . urlopen ( oo000O0OoooO )
 o0O0O00 = oo . read ( )
 oo . close ( )
 if 47 - 47: OOoOoo00oo
 return o0O0O00
 if 66 - 66: I11iii11IIi - Ooooo
def iiIii ( ) :
 iIiIii1ii = [ ]
 IIiI1i = sys . argv [ 2 ]
 if len ( IIiI1i ) >= 2 :
  o0o0OoOo0O0OO = sys . argv [ 2 ]
  iII1 = o0o0OoOo0O0OO . replace ( '?' , '' )
  if ( o0o0OoOo0O0OO [ len ( o0o0OoOo0O0OO ) - 1 ] == '/' ) :
   o0o0OoOo0O0OO = o0o0OoOo0O0OO [ 0 : len ( o0o0OoOo0O0OO ) - 2 ]
  O000O = iII1 . split ( '&' )
  iIiIii1ii = { }
  for Oo0 in range ( len ( O000O ) ) :
   Oo00OO0 = { }
   Oo00OO0 = O000O [ Oo0 ] . split ( '=' )
   if ( len ( Oo00OO0 ) ) == 2 :
    iIiIii1ii [ Oo00OO0 [ 0 ] ] = Oo00OO0 [ 1 ]
 return iIiIii1ii
 if 72 - 72: i1IIi / OoOooOOOO * iI111IiI111I
 if 40 - 40: iIii1I111I11I - OOo0o0 * OOo0o0 . OOo0o0 + OoooooooOO
def Oo0o0OOOOO0O ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 I1I1IiIi1 = name . partition ( '(' )
 oOO0o0oo0 = ""
 oOo000O = ""
 if len ( I1I1IiIi1 ) > 0 :
  oOO0o0oo0 = I1I1IiIi1 [ 0 ]
  oOo000O = I1I1IiIi1 [ 2 ] . partition ( ')' )
 if len ( oOo000O ) > 0 :
  oOo000O = oOo000O [ 0 ]
 iII = metahandlers . MetaData ( )
 ii = iII . get_meta ( 'movie' , name = oOO0o0oo0 , year = oOo000O )
 ooO0o0O0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = ii [ 'cover_url' ] , thumbnailImage = ii [ 'cover_url' ] )
 oO . setInfo ( type = "Video" , infoLabels = ii )
 IiiIIi = [ ]
 IiiIIi . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 oO . addContextMenuItems ( IiiIIi , replaceItems = False )
 if not ii [ 'backdrop_url' ] == '' : oO . setProperty ( 'fanart_image' , ii [ 'backdrop_url' ] )
 else : oO . setProperty ( 'fanart_image' , I11i )
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0o0O0Oo , listitem = oO , isFolder = isFolder , totalItems = itemcount )
 return i111i1i
 if 71 - 71: Ooooo + i1IIi * I1I1i1 % I1I1i1 / I1I1i1
def O000O0oOO0 ( name , url , mode , iconimage , fanart , description = '' ) :
 ooO0o0O0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 oO . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : ooO0o0O0Oo = url
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0o0O0Oo , listitem = oO , isFolder = True )
 return i111i1i
 if 55 - 55: OoooooooOO + iI111IiI111I + OoooooooOO * OoOo
def I1i11i ( name , url , mode , iconimage , fanart , description = '' ) :
 ooO0o0O0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO . setProperty ( 'fanart_image' , fanart )
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0o0O0Oo , listitem = oO , isFolder = False )
 return i111i1i
 if 68 - 68: O0
def oOOOo00O00oOo ( name , url , mode , iconimage , fanart , description = '' ) :
 if 2 - 2: oO0 + O0 * oO0 - iIii1I111I11I + OoOooOOOO
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 ooO0o0O0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  oO . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : ooO0o0O0Oo = url
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0o0O0Oo , listitem = oO , isFolder = False )
 return i111i1i
 if 43 - 43: iI1 - OOo0o0
def Ii1iIiII1ii1 ( name , url , mode , iconimage , fanart , description = '' ) :
 if 36 - 36: iI1 - O00OooO0
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 ooO0o0O0Oo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 i111i1i = True
 oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  oO . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : ooO0o0O0Oo = url
 i111i1i = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ooO0o0O0Oo , listitem = oO , isFolder = False )
 return i111i1i
 if 24 - 24: OOoOoo00oo + OoOo + ii1IiIi11 - iIii1I11I1II1
def I11 ( url ) :
 if 99 - 99: O0 + O0 * ii1IiIi11 + O0 * OoOooOOOO
 oOoO0O00oo = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( oOoO0O00oo )
 sys . exit ( 1 )
 if 93 - 93: iI1 % OOo0o0 . O0 / O00OooO0 * OoOooOOOO
def i1iii1ii ( text , pattern ) :
 if 18 - 18: oO0 . II111iiii % OOo0o0 % iIii1I111I11I
 III1ii1iII = ""
 try :
  oo0i1iIIi1II1iiI = re . findall ( pattern , text , flags = re . DOTALL )
  III1ii1iII = oo0i1iIIi1II1iiI [ 0 ]
 except :
  III1ii1iII = ""
  if 31 - 31: OOoOoo00oo % ii1IiIi11 + iIii1I11I1II1 + i11iIiiIii * iI111IiI111I
 return III1ii1iII
 if 45 - 45: oooO * iI111IiI111I . OoOo - iI111IiI111I + Ooooo
 if 34 - 34: oooO . I1I1i1
 if 78 - 78: iI1 % I11iii11IIi / OoooooooOO % oooO - O00OooO0
def OO0o0oOOO0O ( str ) :
 if 2 - 2: iIii1I11I1II1
 try :
  import chardet
  str = str . decode ( chardet . detect ( str ) [ "encoding" ] ) . encode ( "utf-8" )
 except :
  try :
   str = str . encode ( "utf-8" )
  except :
   pass
 return str
 if 45 - 45: OoooooooOO / i11iIiiIii
def oOOoOooOo ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 I11I1i1iI = xbmcgui . Window ( id )
 O00oO0O0oO00o = 50
 while ( O00oO0O0oO00o > 0 ) :
  try :
   xbmc . sleep ( 10 )
   O00oO0O0oO00o -= 1
   I11I1i1iI . getControl ( 1 ) . setLabel ( heading )
   I11I1i1iI . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 17 - 17: iIii1I111I11I
def Ii1I ( link ) :
 try :
  iIi11Ii1 = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 39 - 39: OoOo . II111iiii
o0o0OoOo0O0OO = iiIii ( ) ; oo000OO00Oo = None ; OoOO0oo0o = None ; iIiIi1iI11iiI = None ; iiI1Ii11II1I = None ; II11i1I11Ii1i = None
try : iiI1Ii11II1I = urllib . unquote_plus ( o0o0OoOo0O0OO [ "site" ] )
except : pass
try : oo000OO00Oo = urllib . unquote_plus ( o0o0OoOo0O0OO [ "url" ] )
except : pass
try : OoOO0oo0o = urllib . unquote_plus ( o0o0OoOo0O0OO [ "name" ] )
except : pass
try : iIiIi1iI11iiI = int ( o0o0OoOo0O0OO [ "mode" ] )
except : pass
try : II11i1I11Ii1i = urllib . unquote_plus ( o0o0OoOo0O0OO [ "iconimage" ] )
except : pass
try : I11i = urllib . unquote_plus ( o0o0OoOo0O0OO [ "fanart" ] )
except : pass
if 44 - 44: iIii1I111I11I % i11iIiiIii - O00OooO0 * iI1 + I1I1i1 * oooO
if iIiIi1iI11iiI == None or oo000OO00Oo == None or len ( oo000OO00Oo ) < 1 : I1IIiiIiii ( )
elif iIiIi1iI11iiI == 1 : III1IiiI ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i , I11i )
elif iIiIi1iI11iiI == 2 : o0oo0O ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 3 : i1i11I11 ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 4 : Ii11iI1ii1111 ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 5 : II1IIIIiII1i ( )
elif iIiIi1iI11iiI == 6 : YOUTUBE_CHANNEL ( oo000OO00Oo )
elif iIiIi1iI11iiI == 7 : I1iIiI1IiIIII ( oo000OO00Oo )
elif iIiIi1iI11iiI == 8 : OOoo ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 9 : I11 ( oo000OO00Oo )
elif iIiIi1iI11iiI == 10 : oo0 ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 11 : OO0000o ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 12 : IIIi11I11 ( oo000OO00Oo )
elif iIiIi1iI11iiI == 13 : o00O ( oo000OO00Oo )
elif iIiIi1iI11iiI == 14 : o00ooo ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 15 : iii1IIII1iii11I ( oo000OO00Oo )
elif iIiIi1iI11iiI == 16 : II11iIiiI1111 ( oo000OO00Oo )
elif iIiIi1iI11iiI == 17 : iIIIII1iiiiII ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 18 : oOo0o0O ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 19 : i1I11iIII1i1I ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 20 : Ii1I1Ii ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i , I11i )
elif iIiIi1iI11iiI == 21 : i11i1i1I1iI1 ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 22 : Oo0O ( oo000OO00Oo )
elif iIiIi1iI11iiI == 23 : iIi1IiI ( )
elif iIiIi1iI11iiI == 24 : ooO0oO00O0o ( oo000OO00Oo )
elif iIiIi1iI11iiI == 25 : Iiii11iIi1 ( oo000OO00Oo )
elif iIiIi1iI11iiI == 26 : o000 ( )
elif iIiIi1iI11iiI == 27 : oooOO0OO0O ( oo000OO00Oo )
elif iIiIi1iI11iiI == 28 : I1iii ( oo000OO00Oo )
elif iIiIi1iI11iiI == 29 : ii1ii11 ( oo000OO00Oo )
elif iIiIi1iI11iiI == 31 : II11iI111i1 ( )
elif iIiIi1iI11iiI == 30 : OoOiIIiii ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 32 : OOOOO0O00 ( )
elif iIiIi1iI11iiI == 33 : IIii11I1i1I ( oo000OO00Oo )
elif iIiIi1iI11iiI == 34 : i11i11111i1i ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 35 : iiIi1iI1iIii ( )
elif iIiIi1iI11iiI == 36 : oooooOOO000Oo ( oo000OO00Oo )
elif iIiIi1iI11iiI == 37 : OO0oOOoo ( OoOO0oo0o , oo000OO00Oo , II11i1I11Ii1i )
elif iIiIi1iI11iiI == 38 : iIIIii ( )
elif iIiIi1iI11iiI == 39 : oo0oOoo ( oo000OO00Oo )
elif iIiIi1iI11iiI == 40 : OO0ooo0oOO ( oo000OO00Oo )
if 41 - 41: O0 * OoOo - OOo0o0 . iIii1I111I11I
if iIiIi1iI11iiI == None or oo000OO00Oo == None or len ( oo000OO00Oo ) < 1 : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = False )
else : xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) , cacheToDisc = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
