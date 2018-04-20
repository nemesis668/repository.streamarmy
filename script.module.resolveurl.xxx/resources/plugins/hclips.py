'''
    resolveurl XBMC Addon
    Copyright (C) 2016 Gujal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import re
from resolveurl import common
from resolveurl.plugins.lib import helpers
from resolveurl.resolver import ResolveUrl, ResolverError
import xbmc,xbmcgui

dialog = xbmcgui.Dialog()
class HClipsResolver(ResolveUrl):
    name = 'hclips'
    domains = ['hclips.com']
    pattern = '(?://|\.)(hclips\.com)/((?:videos|embed)/[\w\-]+)'
    
    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        headers = {'User-Agent': common.RAND_UA}
        web_url = self.get_url(host, media_id)
        html = self.net.http_GET(web_url, headers=headers).content
        dialog.ok("Web",str(web_url))
        dialog.ok("media",str(media_id))
        if html:
            try:
                if media_id.startswith('videos/'):
                    html = self.net.http_GET(media_id, headers=headers).content
                    sources = re.findall('''video_url="(.*?)"''', html)
                    dialog.ok("Source",str(sources))
                if sources:
                    sources = [(i[1], i[0]) for i in sources]
                    return self.net.http_GET(helpers.pick_source(sources), headers=headers).get_url() + helpers.append_headers(headers)
                    
            except Exception as e:
                raise ResolverError(e)
                
        raise ResolverError('File not found')
    
    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://www.{host}/{media_id}')
            
    @classmethod
    def _is_enabled(cls):
        return True
