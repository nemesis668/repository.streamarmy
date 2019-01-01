# -*- coding: utf-8 -*-
"""
    Yify Movies HD Kodi Addon
    Copyright (C) 2018 RickSanchez137

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
import datetime
import os
import re
import threading
import urllib
import urllib2
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
from operator import itemgetter
from resolveurl.hmf import HostedMediaFile
import json

action = None
language = xbmcaddon.Addon().getLocalizedString
setSetting = xbmcaddon.Addon().setSetting
getSetting = xbmcaddon.Addon().getSetting
addonName = xbmcaddon.Addon().getAddonInfo("name")
addonVersion = xbmcaddon.Addon().getAddonInfo("version")
addonId = xbmcaddon.Addon().getAddonInfo("id")
addonPath = xbmcaddon.Addon().getAddonInfo("path")
addonFullId = addonName + addonVersion
addonDesc = language(30450).encode("utf-8")
addonIcon = os.path.join(addonPath, 'icon.png')
addonFanart = os.path.join(addonPath, 'fanart.jpg')
addonArt = os.path.join(addonPath, 'resources/art')
addonGenres = os.path.join(addonPath, 'resources/art/genres.png')
addonYears = os.path.join(addonPath, 'resources/art/years.png')
addonNext = os.path.join(addonPath, 'resources/art/next.png')
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % addonId)


class Main:
    def __init__(self):
        global action
        params = {}
        splitparams = sys.argv[2][sys.argv[2].find('?') + 1:].split('&')
        for param in splitparams:
            if len(param) > 0:
                splitparam = param.split('=')
                key = splitparam[0]
                try:
                    value = splitparam[1].encode("utf-8")
                except:
                    value = splitparam[1]
                params[key] = value

        try:
            action = urllib.unquote_plus(params["action"])
        except:
            action = None
        try:
            name = urllib.unquote_plus(params["name"])
        except:
            name = None
        try:
            url = urllib.unquote_plus(params["url"])
        except:
            url = None
        try:
            query = urllib.unquote_plus(params["query"])
        except:
            query = None

        if action is None:
            Root().get()
        elif action == 'trailer':
            ContextMenu().trailer(name, url)
        elif action == 'movies':
            Movies().get(url)
        elif action == 'movies_title':
            Movies().title()
        elif action == 'movies_release':
            Movies().release()
        elif action == 'movies_added':
            Movies().added()
        elif action == 'movies_rating':
            Movies().rating()
        elif action == 'movies_views':
            Movies().views()
        elif action == 'movies_search':
            Movies().search(query)
        elif action == 'genres_movies':
            Genres().get()
        elif action == 'years_movies':
            Years().get()
        elif action == 'play':
            Resolver().run(url)

        if action is not None:
            if action.startswith('movies'):
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')

        xbmcplugin.setPluginFanart(int(sys.argv[1]), addonFanart)
        xbmcplugin.endOfDirectory(int(sys.argv[1]))

        return


class GetUrl(object):
    def __init__(self, url, close=True, proxy=None, post=None, mobile=False, referer=None, cookie=None, output='', timeout='10'):
        if proxy is not None:
            proxy_handler = urllib2.ProxyHandler({'http': '%s' % proxy})
            opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
        if output == 'cookie' or not close:
            import cookielib
            cookie_handler = urllib2.HTTPCookieProcessor(cookielib.LWPCookieJar())
            opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
            urllib2.install_opener(opener)
        if post is not None:
            request = urllib2.Request(url, post)
        else:
            request = urllib2.Request(url, None)
        if mobile:
            request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1')
        else:
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        if referer is not None:
            request.add_header('Referer', referer)
        if cookie is not None:
            request.add_header('cookie', cookie)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = str(response.headers.get('Set-Cookie'))
        elif output == 'geturl':
            result = response.geturl()
        else:
            result = response.read()
        if close:
            response.close()
        self.result = result


class Thread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)


class Player:
    def __init__(self):
        pass

    @staticmethod
    def run(url):
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


class Common:
    def __init__(self):
        pass

    @staticmethod
    def replaceHTMLCodes(txt):
        import HTMLParser
        txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
        txt = HTMLParser.HTMLParser().unescape(txt)
        txt = txt.replace("&quot;", "\"")
        txt = txt.replace("&amp;", "&")
        txt = txt.replace("&lt;", "<")
        txt = txt.replace("&gt;", ">")
        txt = txt.replace("&#39;", "'")
        txt = txt.replace("\\'", "'")
        blacklist = ['\n', '\r', '\t']
        for ch in blacklist:
            txt = txt.replace(ch, '')
        txt = txt.strip()
        return txt

    @staticmethod
    def getUserInput(title=u"Input", default=u"", hidden=False):
        result = None

        # Fix for when this functions is called with default=None
        if not default:
            default = u""

        keyboard = xbmc.Keyboard(default, title)
        keyboard.setHiddenInput(hidden)
        keyboard.doModal()

        if keyboard.isConfirmed():
            result = keyboard.getText()

        return result
    

class Index:
    def __init__(self):
        pass

    @staticmethod
    def infoDialog(_str, header=addonName, duration=3000):
        try:
            xbmcgui.Dialog().notification(header, _str, addonIcon, duration, sound=False)
        except:
            xbmc.executebuiltin("Notification(%s, %s, %s, %s)" % (header, _str, duration, addonIcon))

    @staticmethod
    def okDialog(str1, str2, header=addonName):
        xbmcgui.Dialog().ok(header, str1, str2)

    @staticmethod
    def selectDialog(_list, header=addonName):
        select = xbmcgui.Dialog().select(header, _list)
        return select

    @staticmethod
    def yesnoDialog(str1, str2, header=addonName, str3='', str4=''):
        answer = xbmcgui.Dialog().yesno(header, str1, str2, '', str4, str3)
        return answer

    @staticmethod
    def getProperty(_str):
        _property = xbmcgui.Window(10000).getProperty(_str)
        return _property

    @staticmethod
    def setProperty(str1, str2):
        xbmcgui.Window(10000).setProperty(str1, str2)

    @staticmethod
    def clearProperty(_str):
        xbmcgui.Window(10000).clearProperty(_str)

    @staticmethod
    def addon_status(_id):
        check = xbmcaddon.Addon(id=_id).getAddonInfo("name")
        if not check == addonName:
            return True

    @staticmethod
    def container_refresh():
        xbmc.executebuiltin("Container.Refresh")

    @staticmethod
    def rootList(root_list):
        total = len(root_list)
        for i in root_list:
            try:
                name = language(i['name']).encode("utf-8")
                image = '%s/%s' % (addonArt, i['image'])
                _action = i['action']
                u = '%s?action=%s' % (sys.argv[0], _action)

                item = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=image)
                item.setInfo(type="Video", infoLabels={"Label": name, "Title": name, "Plot": addonDesc})
                item.setProperty("Fanart_Image", addonFanart)
                item.addContextMenuItems([], replaceItems=False)
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=item, totalItems=total, isFolder=True)
            except:
                pass

    @staticmethod
    def pageList(page_list):
        if page_list is None:
            return

        total = len(page_list)
        for i in page_list:
            try:
                name, url, image = i['name'], i['url'], i['image']
                sysname, sysurl, sysimage = urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(image)

                u = '%s?action=movies&url=%s' % (sys.argv[0], sysurl)

                item = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=image)
                item.setInfo(type="Video", infoLabels={"Label": name, "Title": name, "Plot": addonDesc})
                item.setProperty("Fanart_Image", addonFanart)
                item.addContextMenuItems([], replaceItems=False)
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=item, totalItems=total, isFolder=True)
            except:
                pass

    @staticmethod
    def nextList(next_list):
        try:
            _next = next_list[0]['next']
        except:
            return
        if _next == '':
            return
        name, url, image = language(30361).encode("utf-8"), _next, addonNext
        sysurl = urllib.quote_plus(url)

        u = '%s?action=movies&url=%s' % (sys.argv[0], sysurl)

        item = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=image)
        item.setInfo(type="Video", infoLabels={"Label": name, "Title": name, "Plot": addonDesc})
        item.setProperty("Fanart_Image", addonFanart)
        item.setProperty("art(poster)", image)
        item.setArt({'poster': image})
        item.addContextMenuItems([], replaceItems=False)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=item, isFolder=True)

    @staticmethod
    def movieList(movie_list):
        if movie_list is None:
            return

        total = len(movie_list)
        for i in movie_list:
            try:
                name, url, image, fanart, title, year, imdb, genre, plot, trailer, runtime, rating, mpa_rating = i['name'], i['url'], i['image'], i['fanart'], i['title'], i['year'], i['imdb'], i['genre'], i['plot'], i['trailer'], i['runtime'], i['rating'], i['mpa_rating']

                sysname, sysurl, sysimage, systitle, sysimdb = urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(image), urllib.quote_plus(title), urllib.quote_plus(imdb)
                u = '%s?action=play&name=%s&url=%s&t=%s' % (sys.argv[0], sysname, sysurl, datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))

                meta = {'label': title, 'title': title, 'year': year, 'imdb_id': imdb, 'genre': genre, 'plot': plot,
                        'poster': image, 'backdrop_url': fanart, 'duration': runtime, 'mpaa': mpa_rating,
                        'rating': rating, 'mediatype': 'movie', 'cover_url': image, 'overview': plot}

                if not trailer == '0':
                    meta['trailer'] = 'plugin://plugin.video.youtube/play/?video_id=%s' % trailer

                cm = [(language(30416).encode("utf-8"), 'RunPlugin(%s?action=trailer&name=%s&url=%s)' % (sys.argv[0], sysname, trailer))]

                item = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=image)
                item.setInfo(type="Video", infoLabels=meta)
                item.setProperty("IsPlayable", "true")
                item.setProperty("Video", "true")
                item.setProperty("art(poster)", image)
                item.setProperty("Fanart_Image", fanart)
                item.setArt({'poster': image})
                item.addContextMenuItems(cm, replaceItems=True)
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=item, totalItems=total, isFolder=False)
            except:
                pass


class ContextMenu:
    def __init__(self):
        pass

    @staticmethod
    def trailer(name, url):
        url = Trailer().run(name, url)
        if not url:
            return
        item = xbmcgui.ListItem(path=url)
        item.setProperty("IsPlayable", "true")
        xbmc.Player().play(url, item)


class Root:
    def __init__(self):
        pass

    @staticmethod
    def get():
        root_list = [{'name': 30503, 'image': 'release.png', 'action': 'movies_release'},
                     {'name': 30504, 'image': 'added.png', 'action': 'movies_added'},
                     {'name': 30505, 'image': 'rating.png', 'action': 'movies_rating'},
                     {'name': 30506, 'image': 'views.png', 'action': 'movies_views'},
                     {'name': 30507, 'image': 'genres.png', 'action': 'genres_movies'},
                     {'name': 30508, 'image': 'years.png', 'action': 'years_movies'},
                     {'name': 30511, 'image': 'search.png', 'action': 'movies_search'}]

        Index().rootList(root_list)


class Link:
    def __init__(self):
        if getSetting('use_proxy') == 'true':
            self.yify_base = 'https://ytss.unblocked.si'
        else:
            self.yify_base = 'https://yts.am'
        self.yify_title = '%s/api/v2/list_movies.json?sort_by=title' % self.yify_base
        self.yify_release = '%s/api/v2/list_movies.json?sort_by=year' % self.yify_base
        self.yify_added = '%s/api/v2/list_movies.json?sort_by=date_added' % self.yify_base
        self.yify_rating = '%s/api/v2/list_movies.json?sort_by=rating' % self.yify_base
        self.yify_views = '%s/api/v2/list_movies.json?sort_by=downloads' % self.yify_base
        self.yify_genre = '%s/api/v2/list_movies.json?sort_by=latest&genre=' % self.yify_base
        self.yify_year = '%s/api/v2/list_movies.json?sort_by=year&query_term=' % self.yify_base
        self.yify_search = '%s/api/v2/list_movies.json?query_term=' % self.yify_base


class Genres:
    def __init__(self):
        self.list = []

    def get(self):
        self.list = self.yify_list()
        # self.list = cache3(self.yify_list)
        self.list = sorted(self.list, key=itemgetter('name'))
        Index().pageList(self.list)

    def yify_list(self):
        _genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
                   'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
                   'Reality-TV', 'Romance', 'Sci-Fi', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']

        for genre in _genres:
            try:
                name = Common.replaceHTMLCodes(genre)
                name = name.encode('utf-8')

                url = '%s%s' % (Link().yify_genre, genre)
                url = Common.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = addonGenres.encode('utf-8')

                self.list.append({'name': name, 'url': url, 'image': image})
            except:
                pass

        return self.list


class Years:
    def __init__(self):
        self.list = []

    def get(self):
        self.list = self.yify_list()
        # self.list = cache2(self.yify_list)
        self.list = sorted(self.list, key=itemgetter('name'))
        self.list = self.list[::-1]
        Index().pageList(self.list)

    def yify_list(self):
        year = datetime.datetime.now().year
        while int(year) >= 1952:
            name = str(year)
            name = Common.replaceHTMLCodes(name)
            name = name.encode('utf-8')

            url = '%s%s' % (Link().yify_year, year)
            url = Common.replaceHTMLCodes(url)
            url = url.encode('utf-8')

            image = addonYears.encode('utf-8')

            self.list.append({'name': name, 'url': url, 'image': image})
            year -= 1

        return self.list


class Movies:
    def __init__(self):
        self.list = []
        self.data = []

    def get(self, url):
        self.list = self.yify_list(url)
        # self.list = cache(self.yify_list, url)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def title(self):
        self.list = self.yify_list(Link().yify_title)
        # self.list = cache(self.yify_list, Link().yify_title)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def release(self):
        self.list = self.yify_list(Link().yify_release)
        # self.list = cache(self.yify_list, Link().yify_release)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def added(self):
        self.list = self.yify_list(Link().yify_added)
        # self.list = cache(self.yify_list, Link().yify_added)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def rating(self):
        self.list = self.yify_list(Link().yify_rating)
        # self.list = cache(self.yify_list, Link().yify_rating)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def views(self):
        self.list = self.yify_list(Link().yify_views)
        # self.list = cache(self.yify_list, Link().yify_views)
        Index().movieList(self.list)
        Index().nextList(self.list)

    def search(self, query=None):
        if query is None:
            query = Common.getUserInput(language(30362).encode("utf-8"), '')
        if not (query is None or query == ''):
            query = Link().yify_search + urllib.quote_plus(query)
            self.list = self.yify_list(query)
            Index().movieList(self.list)

    def yify_list(self, url):
        try:
            result = GetUrl(url, timeout='30').result
            js_data = json.loads(result)
            if js_data.get('status').lower() == 'ok':
                js_data = js_data.get('data')
                if js_data.get('movie_count', 0) > 0:
                    _movies = js_data.get('movies')
                else:
                    return
            else:
                return
        except:
            return

        try:
            page_number = js_data.get('page_number', 1)
            if js_data.get('movie_count', 20) > page_number * js_data.get('limit', 20):
                _next = '%s&page=%s' % (url, page_number + 1)
                _next = Common.replaceHTMLCodes(str(_next))
                _next = _next.encode('utf-8')
            else:
                _next = ''
        except:
            _next = ''

        for movie in _movies:
            if movie.get('state').lower() == 'ok':
                try:
                    title = movie.get('title')
                    title = re.sub(r'[^\x00-\x7F]+', '', title)
                    title = Common.replaceHTMLCodes(title)
                    title = title.encode('utf-8')

                    year = movie.get('year')
                    year = re.sub('[^0-9]', '', str(year))
                    year = year.encode('utf-8')

                    # name = title
                    name = movie.get('title_long', '%s (%s)' % (title, year))
                    name = Common.replaceHTMLCodes(name)
                    name = name.encode('utf-8')

                    url = movie.get('url')
                    url = Common.replaceHTMLCodes(url)
                    url = url.encode('utf-8')

                    image = movie.get('large_cover_image', addonIcon)
                    image = Common.replaceHTMLCodes(image)
                    image = image.encode('utf-8')

                    fanart = movie.get('background_image', addonFanart)
                    fanart = Common.replaceHTMLCodes(fanart)
                    fanart = fanart.encode('utf-8')

                    imdb = movie.get('imdb_code', '0')
                    imdb = Common.replaceHTMLCodes(imdb)
                    imdb = imdb.encode('utf-8')

                    trailer = movie.get('yt_trailer_code', '0')
                    trailer = Common.replaceHTMLCodes(trailer)
                    trailer = trailer.encode('utf-8')

                    runtime = movie.get('runtime', 0)
                    runtime = int(runtime) * 60

                    rating = movie.get('rating')

                    mpa_rating = movie.get('mpa_rating')

                    try:
                        genre = movie.get('genres')
                        genre = [i.strip() for i in genre]
                        genre = " / ".join(genre)
                        genre = Common.replaceHTMLCodes(genre)
                        genre = genre.encode('utf-8')
                    except:
                        genre = ''

                    try:
                        plot = movie.get('summary')
                        plot = Common.replaceHTMLCodes(plot)
                        plot = plot.encode('utf-8')
                    except:
                        plot = ''

                    self.list.append({'name': name, 'url': url, 'image': image, 'fanart': fanart, 'title': title,
                                      'year': year, 'imdb': imdb, 'genre': genre, 'plot': plot, 'next': _next,
                                      'trailer': trailer, 'runtime': runtime, 'rating': rating,
                                      'mpa_rating': mpa_rating})
                except:
                    pass

        return self.list

    def thread(self, url, i):
        try:
            result = GetUrl(url, timeout='30').result
            self.data[i] = {'html': result, 'url': url}
        except:
            return


class Trailer:
    def __init__(self):
        pass

    def run(self, name, url):
        Index().infoDialog('Loading trailer...', duration=5000)
        try:
            if url.startswith('tt'):
                url = self.trakt_search(url)
                if url is None:
                    url = self.youtube_search(name)

            if url is not None:
                url = self.youtube(url)
                if url is not None:
                    return url
            raise Exception()
        except:
            Index().infoDialog("Trailer not found")
            return None

    @staticmethod
    def trakt_search(imdb):
        try:
            url = 'https://trakt.tv/search/imdb?query=%s' % imdb
            result = GetUrl(url).result
            result = re.search('href="(https?://(?:w{3}\.)?youtube\.com/watch\?v=[a-zA-Z0-9_-]+)', result).groups()[0]
            return result
        except:
            return None

    @staticmethod
    def youtube_search(name):
        try:
            query = urllib.quote_plus(name)
            url = 'https://www.youtube.com/results?search_query=%s' % query
            result = GetUrl(url).result
            result = re.search('href="(/watch\?v=[a-zA-Z0-9_-]+)"', result).groups()[0]
            return result
        except:
            return None

    @staticmethod
    def youtube(url):
        try:
            # video_id = url.split("?v=")[-1].split("/")[-1].split("?")[0].split("&")[0]
            # url = 'plugin://plugin.video.youtube/play/?video_id=%s' % video_id
            if not url.lower().startswith('http'):
                url = 'https://www.youtube.com/watch?v=%s' % url
            url = HostedMediaFile(url=url).resolve()
            return url
        except:
            return None


class Resolver:
    def __init__(self):
        pass

    def run(self, url):
        try:
            urls = self.yify(url)
            # urls = cache(self.yify, url)
            if urls is None:
                raise Exception()

            if getSetting("autoplay") == 'false' and len(urls) > 1:
                mirrors = list()
                for url in urls:
                    mirrors.extend([url[1].replace('Download', 'Stream')])

                dialog = xbmcgui.Dialog()
                src = dialog.select('Choose a Source', mirrors)

                if src == -1:
                    return

                url = HostedMediaFile(url=urls[src][0]).resolve()
                Player().run(url)
                return url
            else:
                url = HostedMediaFile(url=urls[0][0]).resolve()
                Player().run(url)
                return url
        except:
            if not Index().getProperty('PseudoTVRunning') == 'True':
                Index().infoDialog(language(30318).encode("utf-8"))
            return

    @staticmethod
    def yify(url):
        try:
            result = GetUrl(url).result
            sources = re.findall('''href=["'](magnet:\?[^"']+).+?title=["']([^"']+)''', result, re.I)
            sources.reverse()
            return sources
        except:
            pass


Main()
