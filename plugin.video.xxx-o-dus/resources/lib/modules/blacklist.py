import xbmc,xbmcgui,os,re,urllib,time
import adultresolver
adultresolver = adultresolver.streamer()
dialog = xbmcgui.Dialog()
def Blacklistcheck(url):

	if '3movs.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'hclips.com' in url:
		adultresolver.resolve(url)
		quit()
	else:
		return url