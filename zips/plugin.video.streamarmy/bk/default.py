import xbmc , xbmcaddon , xbmcgui , xbmcplugin , urllib , urllib2 , os , re , sys , datetime , shutil , urlresolver , random , liveresolver
from resources . libs . common_addon import Addon
import base64
from metahandler import metahandlers
if 64 - 64: i11iIiiIii
from pyDes import *
import base64
import os
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 73 - 73: II111iiii
# decoded = DecodeAES(cipher, data_to_be_decrypted)
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
i1111 = 'http://streamarmy.uk/Main/update.txt'
i11 = base64 . b64decode ( b'aHR0cDovL2dldGFmbGl4LnVzL2FkZG9uL3lvdXR1YmUucGhw' )
I11 = 'http://streamarmy.uk/Main/searchtext.xml'
if 98 - 98: I1111 * o0o0Oo0oooo0 / I1I1i1 * oO0 / IIIi1i1I
if 72 - 72: iii11iiII % i11IiIiiIIIII / IiiIII111ii / i1IIi . OoOoOO00
oOo0Oo = base64 . b64decode ( b"MzkyNjk5bGl2ZXJwb29sNQ==" )
if 66 - 66: oO0
if 78 - 78: OoO0O00
Iii1I111 = 16
if 60 - 60: I1111 * o0oOOo0O0Ooo % o0oOOo0O0Ooo % I1I1i1 * II111iiii + i1IIi
if 64 - 64: I1111 - O0 / II111iiii / o0oOOo0O0Ooo / iIii1I11I1II1
if 24 - 24: O0 % o0oOOo0O0Ooo + i1IIi + i11IiIiiIIIII + I1ii11iIi11i
if 70 - 70: Oo0Ooo % Oo0Ooo . iii11iiII % OoO0O00 * o0oOOo0O0Ooo % I1111
iiI1IiI = '{'
if 13 - 13: Oo0Ooo . i11iIiiIii - iIii1I11I1II1 - OoOoOO00
if 6 - 6: I1IiiI / Oo0Ooo % oO0
oo = lambda OO0O00 : OO0O00 + ( Iii1I111 - len ( OO0O00 ) % Iii1I111 ) * iiI1IiI
if 20 - 20: OoooooooOO
if 13 - 13: i1IIi - oO0 % I1111 / iIii1I11I1II1 % IIIi1i1I
if 97 - 97: i11iIiiIii
II1i1Ii11Ii11 = lambda iII11i , OO0O00 : base64 . b64encode ( iII11i . encrypt ( oo ( OO0O00 ) ) )
O0O00o0OOO0 = lambda iII11i , Ii1iIIIi1ii : iII11i . decrypt ( base64 . b64decode ( Ii1iIIIi1ii ) ) . rstrip ( iiI1IiI )
o0oo0o0O00OO = triple_des ( oOo0Oo , CBC )
if 80 - 80: i1IIi
def oOOO0o0o ( ) :
 iiI1 ( )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 i11Iiii = I1i1iiI1
 iI ( '[B][COLOR lime]S[/COLOR][COLOR white]earch[/COLOR][/B] [B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B]' , i11Iiii , 5 , iI1Ii11111iIi , iI111iI )
 I1i1I1II = i1IiIiiI ( I1i1iiI1 )
 I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( I1i1I1II )
 for oOO00oOO in I1I :
  try :
   if '<channel>' in oOO00oOO :
    OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
    iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
    Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
    i11Iiii = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oOO00oOO ) [ 0 ]
    iI ( OoOo , i11Iiii , 6 , iIo00O , Iii1ii1II11i )
   if '<sportsdevil>' in oOO00oOO :
    OOO0OOO00oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     i11Iiii = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO ) [ 0 ]
     Iii111II = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oOO00oOO ) [ 0 ]
     iiii11I = Iii111II
     Ooo0OO0oOO = "/"
     if not iiii11I . endswith ( Ooo0OO0oOO ) :
      ii11i1 = iiii11I + "/"
     else :
      ii11i1 = iiii11I
     I1i1I1II = 'plugin://plugin.video.SportsDevil/?mode=10&amp;item=catcher%3dstreams%26url=' + i11Iiii
     i11Iiii = I1i1I1II + '%26referer=' + ii11i1
     IIIii1II1II ( OoOo , i11Iiii , 4 , iIo00O , Iii1ii1II11i )
    elif len ( OOO0OOO00oo ) > 1 :
     OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     IIIii1II1II ( OoOo , url2 , 8 , iIo00O , Iii1ii1II11i )
     if 42 - 42: oO0 + I1111
     if 76 - 76: i11IiIiiIIIII - OoO0O00
   elif '<folder>' in oOO00oOO :
    oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
    for OoOo , i11Iiii , iIo00O , Iii1ii1II11i in oOooOOo00Oo0O :
     iI ( OoOo , i11Iiii , 1 , iIo00O , Iii1ii1II11i )
   else :
    OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
     O00oO = len ( I1I )
     for OoOo , i11Iiii , iIo00O , Iii1ii1II11i in oOooOOo00Oo0O :
      if 'youtube.com/playlist' in i11Iiii :
       iI ( OoOo , i11Iiii , 2 , iIo00O , Iii1ii1II11i )
      else :
       I11i1I1I ( OoOo , i11Iiii , 2 , iIo00O , Iii1ii1II11i )
    elif len ( OOO0OOO00oo ) > 1 :
     OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     Iii1ii1II11i = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     I11i1I1I ( OoOo , url2 , 3 , iIo00O , Iii1ii1II11i )
  except : pass
  oO0Oo ( I1i1I1II )
  if 54 - 54: o0oOOo0O0Ooo - I1IiiI + OoooooooOO
def iiI1 ( ) :
 O0o0 = OO00Oo ( i1111 )
 if len ( O0o0 ) > 1 :
  O0OOO0OOoO0O = xbmcaddon . Addon ( ) . getAddonInfo ( 'path' )
  O00Oo000ooO0 = os . path . join ( os . path . join ( O0OOO0OOoO0O , '' ) , 'compare.txt' )
  OoO0O00IIiII = open ( O00Oo000ooO0 )
  o0 = OoO0O00IIiII . read ( )
  if o0 == O0o0 : pass
  else :
   ooOooo000oOO ( '[B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B] [B][COLOR lime]I[/COLOR][COLOR white]nformation[/COLOR][/B]' , O0o0 )
   Oo0oOOo = open ( O00Oo000ooO0 , "w" )
   Oo0oOOo . write ( O0o0 )
   Oo0oOOo . close ( )
   if 58 - 58: II111iiii * o0o0Oo0oooo0 * I1ii11iIi11i / o0o0Oo0oooo0
   if 75 - 75: I1111
def I1III ( name , url , iconimage , fanart ) :
 if 63 - 63: o0o0Oo0oooo0 % I1111 * I1111 * OoO0O00 / I1ii11iIi11i
 print "------------ In get encrypted content ------------"
 o0ooO = url
 I1i1I1II = i1IiIiiI ( url )
 if 98 - 98: IIIi1i1I * IIIi1i1I / IIIi1i1I + I1I1i1
 print "------------ open_encrypted_url complete ------------"
 if 34 - 34: IiiIII111ii
 if 'XXX>yes</XXX' in I1i1I1II :
  if o0oOoO00o == '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Set Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    I1I1iIiII1 = IIi1i . getText ( )
    iIiiiI . setSetting ( 'password' , I1I1iIiII1 )
   else : quit ( )
   if 4 - 4: IiiIII111ii + O0 * o0o0Oo0oooo0
 if 'XXX>yes</XXX' in I1i1I1II :
  if o0oOoO00o <> '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Enter Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    I1I1iIiII1 = IIi1i . getText ( )
   if I1I1iIiII1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * I1111 - i11iIiiIii - oO0
 if 'con>yes</con' in I1i1I1II :
  if i1 == '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Set Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    ii1ii1ii = IIi1i . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , ii1ii1ii )
   else : quit ( )
   if 91 - 91: iii11iiII
 if 'con>yes</con' in I1i1I1II :
  if i1 <> '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Enter Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    ii1ii1ii = IIi1i . getText ( )
   if ii1ii1ii <> i1 :
    quit ( )
  else : quit ( )
  if 15 - 15: II111iiii
 print 'Now reading data'
 I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( I1i1I1II )
 if 18 - 18: i11iIiiIii . i1IIi % OoooooooOO / O0
 for oOO00oOO in I1I :
  print oOO00oOO
  try :
   if '<channel>' in oOO00oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oOO00oOO ) [ 0 ]
    iI ( name , url , 6 , iconimage , fanart )
   if '<image>' in oOO00oOO :
    if 75 - 75: OoOoOO00 % o0oOOo0O0Ooo % o0oOOo0O0Ooo . i11IiIiiIIIII
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oOO00oOO ) [ 0 ]
    iI ( name , iconimage , 9 , iconimage , fanart )
   if '<sportsdevil>' in oOO00oOO :
    if 5 - 5: o0oOOo0O0Ooo * IiiIII111ii + OoOoOO00 . o0o0Oo0oooo0 + OoOoOO00
    print '--------- sportsdevil add ---------'
    OOO0OOO00oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO ) [ 0 ]
     Iii111II = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oOO00oOO ) [ 0 ]
     iiii11I = Iii111II
     Ooo0OO0oOO = "/"
     if not iiii11I . endswith ( Ooo0OO0oOO ) :
      ii11i1 = iiii11I + "/"
     else :
      ii11i1 = iiii11I
     I1i1I1II = 'plugin://plugin.video.SportsDevil/?mode=10&amp;item=catcher%3dstreams%26url=' + url
     url = I1i1I1II + '%26referer=' + ii11i1
     IIIii1II1II ( name , url , 4 , iconimage , fanart )
    elif len ( OOO0OOO00oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     IIIii1II1II ( name , o0ooO , 8 , iconimage , fanart )
     if 91 - 91: O0
   elif '<folder>' in oOO00oOO :
    oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
    for name , url , iconimage , fanart in oOooOOo00Oo0O :
     iI ( name , url , 1 , iconimage , fanart )
   else :
    OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
     O00oO = len ( I1I )
     for name , url , iconimage , fanart in oOooOOo00Oo0O :
      if 'youtube.com/playlist' in url :
       iI ( name , url , 2 , iconimage , fanart )
      else :
       I11i1I1I ( name , url , 2 , iconimage , fanart )
    elif len ( OOO0OOO00oo ) > 1 :
     if 61 - 61: II111iiii
     print ( '---------------- simple file checking ----------------------------' )
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     I11i1I1I ( name , o0ooO , 3 , iconimage , fanart )
  except : pass
  oO0Oo ( I1i1I1II )
  if 64 - 64: IiiIII111ii / OoOoOO00 - O0 - I1I1i1
def O0oOoOOOoOO ( name , url , iconimage , fanart ) :
 if 38 - 38: i11IiIiiIIIII
 o0ooO = url
 I1i1I1II = i1IiIiiI ( url )
 if 'XXX>yes</XXX' in I1i1I1II :
  if o0oOoO00o == '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Adult Content' , 'You have opted to show adult content' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Set Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    I1I1iIiII1 = IIi1i . getText ( )
    iIiiiI . setSetting ( 'password' , I1I1iIiII1 )
   else : quit ( )
   if 7 - 7: O0 . IIIi1i1I % I1ii11iIi11i - I1IiiI - iIii1I11I1II1
 if 'XXX>yes</XXX' in I1i1I1II :
  if o0oOoO00o <> '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Adult Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Enter Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    I1I1iIiII1 = IIi1i . getText ( )
   if I1I1iIiII1 <> o0oOoO00o :
    quit ( )
  else : quit ( )
  if 36 - 36: iii11iiII % IiiIII111ii % Oo0Ooo - I1ii11iIi11i
 if 'con>yes</con' in I1i1I1II :
  if i1 == '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Conspiracy Content' , 'You have opted to show Conspiracy content' , '' , 'Due to the Nature of Content ,Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Set Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    ii1ii1ii = IIi1i . getText ( )
    iIiiiI . setSetting ( 'Conspiracy Password' , ii1ii1ii )
   else : quit ( )
   if 22 - 22: iIii1I11I1II1 / Oo0Ooo * I1ii11iIi11i % IIIi1i1I
 if 'con>yes</con' in I1i1I1II :
  if i1 <> '' :
   I1111I1iII11 = xbmcgui . Dialog ( )
   Oooo0O0oo00oO = I1111I1iII11 . yesno ( 'Conspiracy Content' , 'Please enter the password you set' , 'to continue' , '' , 'Cancel' , 'OK' )
   if Oooo0O0oo00oO == 1 :
    IIi1i = xbmc . Keyboard ( '' , 'Enter Password' )
    IIi1i . doModal ( )
   if ( IIi1i . isConfirmed ( ) ) :
    ii1ii1ii = IIi1i . getText ( )
   if ii1ii1ii <> i1 :
    quit ( )
  else : quit ( )
  if 85 - 85: I1111 % i11iIiiIii - IIIi1i1I * OoooooooOO / I1IiiI % I1IiiI
 I1I = re . compile ( '<item>(.+?)</item>' ) . findall ( I1i1I1II )
 for oOO00oOO in I1I :
  try :
   if '<channel>' in oOO00oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
    url = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oOO00oOO ) [ 0 ]
    iI ( name , url , 6 , iconimage , fanart )
   if '<image>' in oOO00oOO :
    name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
    iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
    fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
    url = re . compile ( '<image>(.+?)</image>' ) . findall ( oOO00oOO ) [ 0 ]
    iI ( name , iconimage , 9 , iconimage , fanart )
   if '<sportsdevil>' in oOO00oOO :
    OOO0OOO00oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO ) [ 0 ]
     Iii111II = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oOO00oOO ) [ 0 ]
     iiii11I = Iii111II
     Ooo0OO0oOO = "/"
     if not iiii11I . endswith ( Ooo0OO0oOO ) :
      ii11i1 = iiii11I + "/"
     else :
      ii11i1 = iiii11I
     I1i1I1II = 'plugin://plugin.video.SportsDevil/?mode=10&amp;item=catcher%3dstreams%26url=' + url
     url = I1i1I1II + '%26referer=' + ii11i1
     IIIii1II1II ( name , url , 4 , iconimage , fanart )
    elif len ( OOO0OOO00oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     IIIii1II1II ( name , o0ooO , 8 , iconimage , fanart )
     if 1 - 1: OoO0O00 - I1111 . I1I1i1 . OoO0O00 / Oo0Ooo + I1I1i1
   elif '<folder>' in oOO00oOO :
    oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
    for name , url , iconimage , fanart in oOooOOo00Oo0O :
     iI ( name , url , 1 , iconimage , fanart )
   else :
    OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oOO00oOO )
    if len ( OOO0OOO00oo ) == 1 :
     oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
     O00oO = len ( I1I )
     for name , url , iconimage , fanart in oOooOOo00Oo0O :
      if 'youtube.com/playlist' in url :
       iI ( name , url , 2 , iconimage , fanart )
      else :
       I11i1I1I ( name , url , 2 , iconimage , fanart )
    elif len ( OOO0OOO00oo ) > 1 :
     name = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
     iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
     fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( oOO00oOO ) [ 0 ]
     I11i1I1I ( name , o0ooO , 3 , iconimage , fanart )
  except : pass
  oO0Oo ( I1i1I1II )
  if 78 - 78: O0 . I1111 . II111iiii % o0o0Oo0oooo0
def i1iIi ( url ) :
 if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
 iii = i11 + url
 I1i1I1II = II1I ( iii )
 O0i1II1Iiii1I11 = "<video>(.*?)</video>"
 IIII = re . findall ( O0i1II1Iiii1I11 , I1i1I1II , re . DOTALL )
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 o00oooO0Oo = [ ]
 for o0O0OOO0Ooo in IIII :
  oOO00oOO = { }
  oOO00oOO [ "name" ] = iiIiI ( o0O0OOO0Ooo , "<name>([^<]+)</name>" )
  oOO00oOO [ "url" ] = base64 . b64decode ( b"cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9" ) + iiIiI ( o0O0OOO0Ooo , "<id>([^<]+)</id>" )
  oOO00oOO [ "author" ] = iiIiI ( o0O0OOO0Ooo , "<author>([^<]+)</author>" )
  oOO00oOO [ "iconimage" ] = iiIiI ( o0O0OOO0Ooo , "<iconimage>([^<]+)</iconimage>" )
  oOO00oOO [ "date" ] = iiIiI ( o0O0OOO0Ooo , "<date>([^<]+)</date>" )
  if 6 - 6: iii11iiII . I1111 * OoOoOO00 - oO0 - iii11iiII
  I11i1I1I ( '[COLOR white]' + oOO00oOO [ "name" ] + ' - on ' + oOO00oOO [ "date" ] + '[/COLOR]' , oOO00oOO [ "url" ] , 7 , oOO00oOO [ "iconimage" ] , Iii1ii1II11i )
  if 45 - 45: I1IiiI - OoooooooOO + iIii1I11I1II1 . I1IiiI * I1I1i1
  if 51 - 51: OoO0O00 / OoO0O00
def ooOOO0 ( ) :
 IIi1i = xbmc . Keyboard ( '' , '[COLOR lime]S[/COLOR][COLOR white]earch[/COLOR] [B][COLOR lime]S[/COLOR][COLOR white]tream[/COLOR][/B] [B][COLOR lime]A[/COLOR][COLOR white]rmy[/COLOR][/B]' )
 IIi1i . doModal ( )
 if ( IIi1i . isConfirmed ( ) ) :
  o0o = IIi1i . getText ( )
  o0o = o0o . upper ( )
 else : quit ( )
 I1i1I1II = II1I ( I11 )
 O0OOoO00OO0o = re . compile ( '<link>(.+?)</link>' ) . findall ( I1i1I1II )
 for i11Iiii in O0OOoO00OO0o :
  o0ooO = i11Iiii
  I1i1I1II = II1I ( i11Iiii )
  I1111IIIIIi = re . compile ( '<item>(.+?)</item>' ) . findall ( I1i1I1II )
  for oOO00oOO in I1111IIIIIi :
   I1I = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO )
   for Iiii1i1 in I1I :
    Iiii1i1 = Iiii1i1 . upper ( )
    if o0o in Iiii1i1 :
     try :
      if '<sportsdevil>' in oOO00oOO :
       OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
       iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
       i11Iiii = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( oOO00oOO ) [ 0 ]
       Iii111II = re . compile ( '<referer>(.+?)</referer>' ) . findall ( oOO00oOO ) [ 0 ]
       I1i1I1II = 'plugin://plugin.video.SportsDevil/?mode=10&amp;item=catcher%3dstreams%26url=' + i11Iiii
       i11Iiii = I1i1I1II + '%26referer=' + Iii111II
       if 'tp' in i11Iiii :
        I11i1I1I ( OoOo , i11Iiii , 4 , iIo00O , iI111iI )
      elif '<folder>' in oOO00oOO :
       oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
       for OoOo , i11Iiii , iIo00O , Iii1ii1II11i in oOooOOo00Oo0O :
        if 'tp' in i11Iiii :
         iI ( OoOo , i11Iiii , 1 , iIo00O , iI111iI )
      else :
       OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( oOO00oOO )
       if len ( OOO0OOO00oo ) == 1 :
        oOooOOo00Oo0O = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( oOO00oOO )
        O00oO = len ( I1I )
        for OoOo , i11Iiii , iIo00O , Iii1ii1II11i in oOooOOo00Oo0O :
         if 'youtube.com/playlist' in i11Iiii :
          iI ( OoOo , i11Iiii , 2 , iIo00O , iI111iI )
         else :
          if 'tp' in i11Iiii :
           I11i1I1I ( OoOo , i11Iiii , 2 , iIo00O , iI111iI )
       elif len ( OOO0OOO00oo ) > 1 :
        OoOo = re . compile ( '<title>(.+?)</title>' ) . findall ( oOO00oOO ) [ 0 ]
        iIo00O = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( oOO00oOO ) [ 0 ]
        I11i1I1I ( OoOo , o0ooO , 3 , iIo00O , iI111iI )
     except : pass
     if 84 - 84: I1IiiI . iIii1I11I1II1 % OoooooooOO + oO0 % OoooooooOO % OoO0O00
     if 42 - 42: OoO0O00 / I1I1i1 / o0oOOo0O0Ooo + IIIi1i1I / OoOoOO00
def o0OoOO000ooO0 ( name , url , iconimage ) :
 o0o0o0oO0oOO = [ ]
 ii1Ii11I = [ ]
 o00o0 = [ ]
 I1i1I1II = II1I ( url )
 ii = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1i1I1II ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii ) [ 0 ]
 OOO0OOO00oo = re . compile ( '<link>(.+?)</link>' ) . findall ( ii )
 OOooooO0Oo = 1
 for OO in OOO0OOO00oo :
  iIiIIi1 = OO
  if '(' in OO :
   OO = OO . split ( '(' ) [ 0 ]
   I1IIII1i = str ( iIiIIi1 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   o0o0o0oO0oOO . append ( OO )
   ii1Ii11I . append ( I1IIII1i )
  else :
   o0o0o0oO0oOO . append ( OO )
   ii1Ii11I . append ( 'Link ' + str ( OOooooO0Oo ) )
  OOooooO0Oo = OOooooO0Oo + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 I1111I1iII11 = xbmcgui . Dialog ( )
 I1I11i = I1111I1iII11 . select ( name , ii1Ii11I )
 if I1I11i < 0 :
  quit ( )
 else :
  url = o0o0o0oO0oOO [ I1I11i ]
  print url
  if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : Ii1I1I1i1Ii = urlresolver . HostedMediaFile ( url ) . resolve ( )
  elif liveresolver . isValid ( url ) == True : Ii1I1I1i1Ii = liveresolver . resolve ( url )
  else : Ii1I1I1i1Ii = url
  i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  i1Oo0oO00o . setPath ( Ii1I1I1i1Ii )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1Oo0oO00o )
  if 13 - 13: I1I1i1 * Oo0Ooo * IiiIII111ii
def iI11iI1IiiIiI ( name , url , iconimage ) :
 if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * i11IiIiiIIIII * O0
 o00oO0oo0OO = 'plugin://plugin.video.SportsDevil/?mode=10&amp;item=catcher%3dstreams%26url='
 o0o0o0oO0oOO = [ ]
 ii1Ii11I = [ ]
 o00o0 = [ ]
 O0O0OOOOoo = [ ]
 I1i1I1II = II1I ( url )
 ii = re . compile ( '<title>' + re . escape ( name ) + '</title>(.+?)</item>' , re . DOTALL ) . findall ( I1i1I1II ) [ 0 ]
 OOO0OOO00oo = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( ii )
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( ii ) [ 0 ]
 OOooooO0Oo = 1
 if 74 - 74: I1ii11iIi11i + II111iiii / OoO0O00
 for OO in OOO0OOO00oo :
  iIiIIi1 = OO
  if '(' in OO :
   OO = OO . split ( '(' ) [ 0 ]
   I1IIII1i = str ( iIiIIi1 . split ( '(' ) [ 1 ] . replace ( ')' , '' ) )
   o0o0o0oO0oOO . append ( OO )
   ii1Ii11I . append ( I1IIII1i )
   O0O0OOOOoo . append ( 'Stream ' + str ( OOooooO0Oo ) )
  else :
   o0o0o0oO0oOO . append ( OO )
   ii1Ii11I . append ( 'Link ' + str ( OOooooO0Oo ) )
  OOooooO0Oo = OOooooO0Oo + 1
 name = '[COLOR lime]' + name + '[/COLOR]'
 I1111I1iII11 = xbmcgui . Dialog ( )
 I1I11i = I1111I1iII11 . select ( name , ii1Ii11I )
 if I1I11i < 0 :
  quit ( )
 else :
  iiii11I = ii1Ii11I [ I1I11i ]
  Ooo0OO0oOO = "/"
  if not iiii11I . endswith ( Ooo0OO0oOO ) :
   ii11i1 = iiii11I + "/"
  else :
   ii11i1 = iiii11I
  url = o00oO0oo0OO + o0o0o0oO0oOO [ I1I11i ] + "%26referer=" + ii11i1
  print url
  if 100 - 100: OoOoOO00 * iIii1I11I1II1
  xbmc . Player ( ) . play ( url )
  if 86 - 86: OoO0O00 * o0o0Oo0oooo0 . IIIi1i1I
def iIO0O0Oooo0o ( name , url , iconimage ) :
 oOOoo00O00o = True
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; i1Oo0oO00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOOoo00O00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = i1Oo0oO00o )
 xbmc . Player ( ) . play ( url , i1Oo0oO00o , False )
 if 98 - 98: o0o0Oo0oooo0 + iii11iiII + I1111 % OoooooooOO
def oooooo0O000o ( name , url , iconimage ) :
 if 64 - 64: I1IiiI . o0oOOo0O0Ooo - i11IiIiiIIIII / OoooooooOO
 if not 'http' in url : url = 'http://' + url
 if 'youtube.com/playlist' in url :
  o0o = url . split ( 'list=' ) [ 1 ]
  O0O0ooOOO = iiIIIII1i1iI + o0o + o0oO0
  oOOo0O00o = urllib2 . Request ( O0O0ooOOO )
  oOOo0O00o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  iIiIi11 = urllib2 . urlopen ( oOOo0O00o )
  I1i1I1II = iIiIi11 . read ( )
  iIiIi11 . close ( )
  I1i1I1II = I1i1I1II . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( I1i1I1II )
  try :
   OOO = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( I1i1I1II ) [ 0 ]
   O0O0ooOOO = oo00 + OOO + o00 + o0o + Oo0oO0ooo
   iI ( 'Next Page >>' , O0O0ooOOO , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 32 - 32: i1IIi / II111iiii . Oo0Ooo
  if 62 - 62: OoooooooOO * I1IiiI
  if 58 - 58: OoOoOO00 % o0oOOo0O0Ooo
  if 50 - 50: i11IiIiiIIIII . o0oOOo0O0Ooo
  for name , ooO0OO in I1I :
   url = 'https://www.youtube.com/watch?v=' + ooO0OO
   iconimage = 'https://i.ytimg.com/vi/' + ooO0OO + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     I11i1I1I ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 54 - 54: iii11iiII + oO0 % OoO0O00 + OoooooooOO - O0 - o0oOOo0O0Ooo
 if 'https://www.googleapis.com/youtube/v3' in url :
  o0o = re . compile ( 'playlistId=(.+?)&maxResults' ) . findall ( url ) [ 0 ]
  oOOo0O00o = urllib2 . Request ( url )
  oOOo0O00o . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
  iIiIi11 = urllib2 . urlopen ( oOOo0O00o )
  I1i1I1II = iIiIi11 . read ( )
  iIiIi11 . close ( )
  I1i1I1II = I1i1I1II . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '  ' , '' )
  I1I = re . compile ( '"title": "(.+?)".+?"videoId": "(.+?)"' , re . DOTALL ) . findall ( I1i1I1II )
  try :
   OOO = re . compile ( '"nextPageToken": "(.+?)"' ) . findall ( I1i1I1II ) [ 0 ]
   O0O0ooOOO = oo00 + OOO + o00 + o0o + Oo0oO0ooo
   iI ( 'Next Page >>' , O0O0ooOOO , 2 , i1i1II , Iii1ii1II11i )
  except : pass
  if 77 - 77: o0o0Oo0oooo0 * iIii1I11I1II1
  if 98 - 98: I1IiiI % oO0 * OoooooooOO
  if 51 - 51: iIii1I11I1II1 . OoOoOO00 / I1111 + o0oOOo0O0Ooo
  for name , ooO0OO in I1I :
   url = 'https://www.youtube.com/watch?v=' + ooO0OO
   iconimage = 'https://i.ytimg.com/vi/' + ooO0OO + '/hqdefault.jpg'
   if not 'Private video' in name :
    if not 'Deleted video' in name :
     I11i1I1I ( name , url , 2 , iconimage , Iii1ii1II11i )
     if 33 - 33: IiiIII111ii . II111iiii % IIIi1i1I + o0oOOo0O0Ooo
     if 71 - 71: Oo0Ooo % o0o0Oo0oooo0
     if 98 - 98: I1I1i1 % i11iIiiIii % IiiIII111ii + oO0
 if "plugin://" in url :
  url = "PlayMedia(" + url + ")"
  xbmc . executebuiltin ( url )
  quit ( )
  if 78 - 78: I1ii11iIi11i % I1111 / IIIi1i1I - iIii1I11I1II1
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) : Ii1I1I1i1Ii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 elif liveresolver . isValid ( url ) == True : Ii1I1I1i1Ii = liveresolver . resolve ( url )
 else : Ii1I1I1i1Ii = url
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
 i1Oo0oO00o . setPath ( Ii1I1I1i1Ii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1Oo0oO00o )
 if 69 - 69: i11IiIiiIIIII
def ii1I1 ( url ) :
 if 93 - 93: O0 % i1IIi . o0o0Oo0oooo0 / I1IiiI - i11IiIiiIIIII / I1IiiI
 xbmc . Player ( ) . play ( url )
 if 36 - 36: I1111 % I1111 % i1IIi / i1IIi - IiiIII111ii
def II1I ( url ) :
 try :
  oOOo0O00o = urllib2 . Request ( url )
  oOOo0O00o . add_header ( 'User-Agent' , 'obsession' )
  iIiIi11 = urllib2 . urlopen ( oOOo0O00o )
  I1i1I1II = iIiIi11 . read ( )
  iIiIi11 . close ( )
  I1i1I1II = I1i1I1II . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  print I1i1I1II
  return I1i1I1II
 except : quit ( )
 if 30 - 30: I1I1i1 / I1IiiI
def i1IiIiiI ( url ) :
 if 35 - 35: II111iiii % o0o0Oo0oooo0 . IiiIII111ii + IiiIII111ii % II111iiii % II111iiii
 print "--------- open_encrypted_url --------"
 try :
  oOOo0O00o = urllib2 . Request ( url )
  oOOo0O00o . add_header ( 'User-Agent' , 'obsession' )
  iIiIi11 = urllib2 . urlopen ( oOOo0O00o )
  I1i1I1II = iIiIi11 . read ( )
  print "--------- link --------" , I1i1I1II
  ooOoO00 = O0O00o0OOO0 ( o0oo0o0O00OO , I1i1I1II )
  print "--------- decoded --------" , ooOoO00
  iIiIi11 . close ( )
  ooOoO00 = ooOoO00 . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
  print ooOoO00
  return ooOoO00
 except : quit ( )
 if 14 - 14: i1IIi - o0oOOo0O0Ooo % O0 - OoO0O00
 if 72 - 72: oO0
def OO00Oo ( url ) :
 oOOo0O00o = urllib2 . Request ( url )
 oOOo0O00o . add_header ( 'User-Agent' , 'obsession' )
 iIiIi11 = urllib2 . urlopen ( oOOo0O00o )
 I1i1I1II = iIiIi11 . read ( )
 iIiIi11 . close ( )
 print I1i1I1II
 return I1i1I1II
 if 1 - 1: OoO0O00 * iii11iiII * OoooooooOO + IiiIII111ii
def IiII111i1i11 ( ) :
 i111iIi1i1II1 = [ ]
 oooO = sys . argv [ 2 ]
 if len ( oooO ) >= 2 :
  i1I1i111Ii = sys . argv [ 2 ]
  ooo = i1I1i111Ii . replace ( '?' , '' )
  if ( i1I1i111Ii [ len ( i1I1i111Ii ) - 1 ] == '/' ) :
   i1I1i111Ii = i1I1i111Ii [ 0 : len ( i1I1i111Ii ) - 2 ]
  i1i1iI1iiiI = ooo . split ( '&' )
  i111iIi1i1II1 = { }
  for OOooooO0Oo in range ( len ( i1i1iI1iiiI ) ) :
   Ooo0oOooo0 = { }
   Ooo0oOooo0 = i1i1iI1iiiI [ OOooooO0Oo ] . split ( '=' )
   if ( len ( Ooo0oOooo0 ) ) == 2 :
    i111iIi1i1II1 [ Ooo0oOooo0 [ 0 ] ] = Ooo0oOooo0 [ 1 ]
 return i111iIi1i1II1
 if 61 - 61: OoOoOO00 - o0o0Oo0oooo0 - i1IIi
 if 25 - 25: O0 * I1I1i1 + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
def oOooO ( name , url , mode , iconimage , itemcount , isFolder = False ) :
 IIIIiI11I11 = name . partition ( '(' )
 oo00o0 = ""
 i11II1I11I1 = ""
 if len ( IIIIiI11I11 ) > 0 :
  oo00o0 = IIIIiI11I11 [ 0 ]
  i11II1I11I1 = IIIIiI11I11 [ 2 ] . partition ( ')' )
 if len ( i11II1I11I1 ) > 0 :
  i11II1I11I1 = i11II1I11I1 [ 0 ]
 OOoOO0ooo = metahandlers . MetaData ( )
 II1iIi11 = OOoOO0ooo . get_meta ( 'movie' , name = oo00o0 , year = i11II1I11I1 )
 I11iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 oOOoo00O00o = True
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = II1iIi11 [ 'cover_url' ] , thumbnailImage = II1iIi11 [ 'cover_url' ] )
 i1Oo0oO00o . setInfo ( type = "Video" , infoLabels = II1iIi11 )
 O0i1iI = [ ]
 O0i1iI . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i1Oo0oO00o . addContextMenuItems ( O0i1iI , replaceItems = False )
 if not II1iIi11 [ 'backdrop_url' ] == '' : i1Oo0oO00o . setProperty ( 'fanart_image' , II1iIi11 [ 'backdrop_url' ] )
 else : i1Oo0oO00o . setProperty ( 'fanart_image' , Iii1ii1II11i )
 oOOoo00O00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11iiii , listitem = i1Oo0oO00o , isFolder = isFolder , totalItems = itemcount )
 return oOOoo00O00o
 if 29 - 29: I1IiiI % o0o0Oo0oooo0 - I1IiiI / o0o0Oo0oooo0 . i1IIi
def iI ( name , url , mode , iconimage , fanart , description = '' ) :
 I11iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOOoo00O00o = True
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo0oO00o . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 i1Oo0oO00o . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' in url : I11iiii = url
 oOOoo00O00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11iiii , listitem = i1Oo0oO00o , isFolder = True )
 return oOOoo00O00o
 if 31 - 31: i11IiIiiIIIII
 if 88 - 88: OoO0O00 - IiiIII111ii + o0o0Oo0oooo0 * I1IiiI % iIii1I11I1II1 + Oo0Ooo
 if 76 - 76: I1IiiI * IIIi1i1I % i11IiIiiIIIII
def I11i1I1I ( name , url , mode , iconimage , fanart , description = '' ) :
 if 57 - 57: iIii1I11I1II1 - i1IIi / i11IiIiiIIIII - O0 * OoooooooOO % II111iiii
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 I11iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOOoo00O00o = True
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo0oO00o . setProperty ( 'fanart_image' , fanart )
 if 'plugin://' not in url :
  i1Oo0oO00o . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : I11iiii = url
 oOOoo00O00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11iiii , listitem = i1Oo0oO00o , isFolder = False )
 return oOOoo00O00o
 if 68 - 68: OoooooooOO * I1I1i1 % OoOoOO00 - iii11iiII
def IIIii1II1II ( name , url , mode , iconimage , fanart , description = '' ) :
 if 34 - 34: i11IiIiiIIIII . iIii1I11I1II1 * OoOoOO00 * I1111 / i11IiIiiIIIII / I1ii11iIi11i
 if '.ts' in url :
  url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
 I11iiii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
 oOOoo00O00o = True
 i1Oo0oO00o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo0oO00o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1Oo0oO00o . setProperty ( "Fanart_Image" , fanart )
 if 'plugin://' not in url :
  i1Oo0oO00o . setProperty ( "IsPlayable" , "true" )
 if 'plugin://' in url : I11iiii = url
 oOOoo00O00o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11iiii , listitem = i1Oo0oO00o , isFolder = False )
 return oOOoo00O00o
 if 78 - 78: Oo0Ooo - o0oOOo0O0Ooo / OoOoOO00
def I11IIIi ( url ) :
 if 15 - 15: I1ii11iIi11i * OoO0O00
 i1II1i = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( i1II1i )
 sys . exit ( 1 )
 if 83 - 83: OoOoOO00 - oO0 / I1I1i1 / i11IiIiiIIIII + I1111 - O0
def iiIiI ( text , pattern ) :
 if 4 - 4: o0o0Oo0oooo0 * OoO0O00 % i1IIi * i11iIiiIii % Oo0Ooo - I1111
 OOoOoOo = ""
 try :
  o000ooooO0o = re . findall ( pattern , text , flags = re . DOTALL )
  OOoOoOo = o000ooooO0o [ 0 ]
 except :
  OOoOoOo = ""
  if 40 - 40: I1ii11iIi11i + i1IIi * o0o0Oo0oooo0
 return OOoOoOo
 if 85 - 85: oO0 * Oo0Ooo . O0 - i11iIiiIii
 if 18 - 18: oO0 + iii11iiII - O0
 if 53 - 53: i1IIi
def ooOooo000oOO ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 Ooo00Oo = xbmcgui . Window ( id )
 oO00Oooo0O0o0 = 50
 while ( oO00Oooo0O0o0 > 0 ) :
  try :
   xbmc . sleep ( 10 )
   oO00Oooo0O0o0 -= 1
   Ooo00Oo . getControl ( 1 ) . setLabel ( heading )
   Ooo00Oo . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 14 - 14: o0oOOo0O0Ooo % O0 * IIIi1i1I + oO0 + Oo0Ooo * oO0
def oO0Oo ( link ) :
 try :
  I1I = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if layout == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 3 - 3: OoOoOO00 * Oo0Ooo
i1I1i111Ii = IiII111i1i11 ( ) ; i11Iiii = None ; OoOo = None ; oOoO00oo0O = None ; oooiiI = None ; iIo00O = None
try : oooiiI = urllib . unquote_plus ( i1I1i111Ii [ "site" ] )
except : pass
try : i11Iiii = urllib . unquote_plus ( i1I1i111Ii [ "url" ] )
except : pass
try : OoOo = urllib . unquote_plus ( i1I1i111Ii [ "name" ] )
except : pass
try : oOoO00oo0O = int ( i1I1i111Ii [ "mode" ] )
except : pass
try : iIo00O = urllib . unquote_plus ( i1I1i111Ii [ "iconimage" ] )
except : pass
try : Iii1ii1II11i = urllib . unquote_plus ( i1I1i111Ii [ "fanart" ] )
except : pass
if 56 - 56: Oo0Ooo . I1ii11iIi11i . I1IiiI
if oOoO00oo0O == None or i11Iiii == None or len ( i11Iiii ) < 1 : oOOO0o0o ( )
elif oOoO00oo0O == 1 : O0oOoOOOoOO ( OoOo , i11Iiii , iIo00O , Iii1ii1II11i )
elif oOoO00oo0O == 10 : I1III ( OoOo , i11Iiii , iIo00O , Iii1ii1II11i )
elif oOoO00oo0O == 2 : oooooo0O000o ( OoOo , i11Iiii , iIo00O )
elif oOoO00oo0O == 3 : o0OoOO000ooO0 ( OoOo , i11Iiii , iIo00O )
elif oOoO00oo0O == 4 : iIO0O0Oooo0o ( OoOo , i11Iiii , iIo00O )
elif oOoO00oo0O == 5 : ooOOO0 ( )
elif oOoO00oo0O == 6 : i1iIi ( i11Iiii )
elif oOoO00oo0O == 7 : ii1I1 ( i11Iiii )
elif oOoO00oo0O == 8 : iI11iI1IiiIiI ( OoOo , i11Iiii , iIo00O )
elif oOoO00oo0O == 9 : I11IIIi ( i11Iiii )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3