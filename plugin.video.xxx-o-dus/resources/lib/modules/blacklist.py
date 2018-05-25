import xbmc,xbmcgui,os,re,urllib,time
import adultresolver
import linkfinder
adultresolver = adultresolver.streamer()
dialog = xbmcgui.Dialog()
def Blacklistcheck(url):

	if '3movs.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'hclips.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'watchxxxfree.tv' in url:
		linkfinder.find(url)
		quit()
	elif 'youngpornvideos.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'javhihi.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'txxx.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'vrsumo.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'anysex.com' in url:
		adultresolver.resolve(url)
		quit()
	elif 'pandamovie.cc' in url:
		adultresolver.resolve(url)
		quit()
	else:
		return url
		