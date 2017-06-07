"""
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
from urlresolver.resolver import UrlResolver, ResolverError
from urlresolver.lib import kodi
from lib import helpers

try:
    from youtube_plugin.youtube.provider import Provider
    from youtube_plugin.kodion.impl import Context
except ImportError:
    Provider = Context = None


class YoutubeResolver(UrlResolver):
    name = "youtube"
    domains = ['youtube.com', 'youtu.be', 'youtube-nocookie.com']
    pattern = '''https?://(?:[0-9A-Z-]+\.)?(?:(youtu\.be|youtube(?:-nocookie)?\.com)/?\S*?[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['"][^<>]*>|</a>))[?=&+%\w.-]*'''

    def get_media_url(self, host, media_id):
        if Provider is None or Context is None:
            return 'plugin://plugin.video.youtube/play/?video_id=' + media_id
        else:
            provider = Provider()
            context = Context(plugin_id='plugin.video.youtube')
            client = provider.get_client(context=context)
            streams = client.get_video_streams(context=context, video_id=media_id)
            streams_no_dash = [item for item in streams if item['container'] != 'mpd']
            sorted_streams = sorted(streams_no_dash, key=lambda x: x.get('sort', 0), reverse=True)
            sorted_streams = [(item['title'], item['url']) for item in sorted_streams]
            return helpers.pick_source(sorted_streams)

    def get_url(self, host, media_id):
        return 'http://youtube.com/watch?v=%s' % media_id

    @classmethod
    def _is_enabled(cls):
        return cls.get_setting('enabled') == 'true' and kodi.has_addon('plugin.video.youtube')

    @classmethod
    def get_settings_xml(cls):
        xml = super(cls, cls).get_settings_xml()
        if Provider is None or Context is None:
            xml.append('<setting label="This plugin calls the youtube addon -change settings there." type="lsep" />')
        return xml
