import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,datetime,time
import base64
import HTMLParser

addon_id        = 'plugin.video.sportsworld'
AddonTitle      = '[COLOR orange][B]Sports World[/B][/COLOR]'
dialog          = xbmcgui.Dialog()
dp              = xbmcgui.DialogProgress()

def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
        response = urllib2.urlopen(req, timeout=5)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')
        return link
    except:quit()


def Devil_Checker(url):
    try:

        if 'bundesliga-streams' in url:
            return url
        elif 'atdee' in url:
            return url
        elif 'acestream://' in url:
            return url
        elif 'goolsport' in url:
            return url
        elif 'buffstream' in url:
            return url
        elif 'dimsports' in url:
            return url
        elif 'dinozaptv' in url:
            return url
        elif 'firstrow' in url:
            return url
        elif 'firstrowsports' in url:
            return url
        elif 'livefootball' in url:
            return url
        elif 'livesportstreams' in url:
            return url
        elif 'livetv' in url:
            return url
        elif 'lshunter' in url:
            return url
        elif 'rojadirecta' in url:
            return url
        elif 'slipstreamtv' in url:
            return url
        elif 'sportstream365' in url:
            return url
        elif 'sportlemon' in url:
            return url
        elif 'stopstream' in url:
            return url
        elif 'streamsports' in url:
            return url
        elif 'tumarcador' in url:
            return url
        elif 'epllivestream' in url:
            return url
        elif 'vipbox' in url:
            return url
        elif 'vipgoal' in url:
            return url
        elif 'sporttwin' in url:
            try:
                link = open_url(url)
                url = re.compile('file: "(.+?)"').findall(link)[0]
                return url
            except IndexError:
                url = 'NOTSUPPORTED'
        elif 'soccerlivestream' in url:
            try:
                link = open_url(url).replace('\n', '').replace('\r','').replace('\t','')
                match = re.compile('<iframe class=.+?src="(.+?)"').findall(link)[0]
                link2 = open_url(match)
                url = re.compile ('source: "(.+?)"').findall(link2)[0]
                return url
            except IndexError:
                url = 'NOTSUPPORTED'
        elif 'ripple' in url:
            try:
                link = open_url(url)
                match = re.compile ('<iframe.+?src="(.+?)"').findall(link)[0]
                link2 = open_url(match)
                grab = re.compile ('src=\'(.+?)\'').findall(link2)[0]
                link3 = open_url(grab)
                url = re.compile ('<source src="(.+?)"').findall(link3)[0]
                return url
            except : return url
        elif 'sporttube' in url:
            try:
                url = url.replace('no-preload', '')
                link = open_url(url)
                url = re.compile ('<source src="(.+?)"').findall(link)[0]
                return url
            except : return url
        elif 'playwire' in url:
            try:
                link2 = open_url(url)
                get = re.compile ('{"f4m":"(.+?)"').findall(link2)[0]
                link3 = open_url(get)
                url = re.compile ('<media url="(.+?)"').findall(link3)[2]
                return url
            except : return url
        elif 'yalla' in url:
            try:
                link = open_url(url)
            except:
                url = 'NOTSUPPORTED'
                return url
            try:
                grab2 = re.compile ('<iframe(.+?)</iframe>').findall(link)[0]
                result = re.compile ('src="(.+?)"').findall(grab2)[0]
            except IndexError:
                url = 'NOTSUPPORTED'
                return url
            if not 'http' in result:
                result = 'http:' + result
            link3 = open_url(result)
            try:
                url = re.compile ('source: "(.+?)"').findall(link3)[0]
            except IndexError:
                try:
                    playable = re.compile ('src="(.+?)"').findall(link3)[0]
                    link4 = open_url(playable)
                    url = re.compile ('source: "(.+?)"').findall(link4)[0]
                except IndexError:
                    url = 'NOTSUPPORTED'
            return url
        elif 'livestreamsonline' in url:
            embed_id = url.replace ('http://plr.livestreamsonline.net/embed/','')
            url = None
            if url:
                r = open_url(url)
                r = re.findall(r'<a\s*href="([^"]+)', r, re.DOTALL)
                r = [i.replace('http://firstrowas.co/embed/','') for i in r if '/embed/' in i]
                r = ['http://www.04stream.com/weed.js?stream=%s&width=600&height=460&str=is&link=1&cat=1' % i for i in r]
                for i in r:
                    data = open_url(i)
                    function = re.findall("function\s*([^\(]+)", data)[0]
                    ret = re.findall('return "([^"]+)', data)[0]
                    src = re.findall("src=([^']+)", data)[0]
                    ids = re.findall("\(\)\+'(.+?)&idom", data)[0]
                    Part_Two = src + function + ids
                    s = open_url(Part_Two)
                    url = re.compile ('file=(.+?)"').findall(s)[0]
                    return url
            else:
                if embed_id:
                    r = 'http://www.04stream.com/weed.js?stream=%s&width=600&height=460&str=is&link=1&cat=1' % embed_id
                    data = open_url(r)
                    try:
                        function = re.findall("function\s*([^\(]+)", data)[0]
                    except IndexError:
                        url = False
                        return url
                    ret = re.findall('return "([^"]+)', data)[0]
                    src = re.findall("src=([^']+)", data)[0]
                    ids = re.findall("\(\)\+'(.+?)&idom", data)[0]
                    Part_Two = src + function + ids
                    s = open_url(Part_Two)
                    try:
                        url = re.compile ('file=(.+?)"').findall(s)[0]
                    except IndexError:
                        url = False
                    return url
        else:
            return False

    except:
        url = False
        return url
