"""
    OVERALL CREDIT TO:
        t0mm0, Eldorado, VOINAGE, BSTRDMKR, tknorris, smokdpi, TheHighway

    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0

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
import re
from lib import helpers
from urlresolver import common
from urlresolver.resolver import UrlResolver, ResolverError

class VidloxResolver(UrlResolver):
    name = "vidlox"
    domains = ['vidlox.tv']
    pattern = '(?://|\.)(vidlox\.tv)/(?:embed-|)([0-9a-zA-Z]+)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.IE_USER_AGENT, 'Referer': web_url}
        html = self.net.http_GET(web_url, headers=headers).content
        url = re.findall('sources\s*:\s*\[(.+?)\]', html)[0]
        url = re.findall('(?:\"|\')(http.+?)(?:\"|\')', url)
        url = [i for i in url if '.mp4' in i] + [i for i in url if '.m3u8' in i]

        if url:
            return url[0] + helpers.append_headers(headers)
        else:
            raise ResolverError('File not found')

    def get_url(self, host, media_id):
        return 'http://%s/embed-%s.html' % (host, media_id)
