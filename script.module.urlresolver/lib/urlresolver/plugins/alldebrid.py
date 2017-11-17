"""
    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0, JUL1EN094

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

import os
import re
import urllib
import json
from lib import helpers
from urlresolver import common
from urlresolver.common import i18n
from urlresolver.resolver import UrlResolver, ResolverError

logger = common.log_utils.Logger.get_logger(__name__)
logger.disable()

class AllDebridResolver(UrlResolver):
    name = "AllDebrid"
    domains = ['*']
    profile_path = common.profile_path
    cookie_file = os.path.join(profile_path, '%s.cookies' % name)
    media_url = None

    def __init__(self):
        self.hosts = None
        self.net = common.Net()
        try:
            os.makedirs(os.path.dirname(self.cookie_file))
        except OSError:
            pass

    def get_media_url(self, host, media_id):
        source = None
        logger.log('in get_media_url %s : %s' % (host, media_id))
        url = 'http://www.alldebrid.com/service.php?link=%s' % (media_id)
        html = self.net.http_GET(url).content
        if html == 'login':
            raise ResolverError('alldebrid: Authentication Error')
    
        try: js_data = json.loads(html)
        except: js_data = {}
        if js_data.get('error'):
            raise ResolverError('alldebrid: %s' % (js_data['error']))
        
        if 'streaming' in js_data:
            source = helpers.pick_source(js_data['streaming'].items())
        elif 'link' in js_data:
            source = js_data['link']
        else:
            match = re.search('''class=["']link_dl['"][^>]+href=["']([^'"]+)''', html)
            if match:
                source = match.group(1)
        
        if source:
            return source.encode('utf-8')
        else:
            raise ResolverError('alldebrid: no stream returned')

    def get_url(self, host, media_id):
        return media_id

    def get_host_and_id(self, url):
        return 'www.alldebrid.com', url

    @common.cache.cache_method(cache_limit=8)
    def get_all_hosters(self):
        url = 'http://alldebrid.com/api.php?action=get_host'
        html = self.net.http_GET(url).content
        html = html.replace('"', '')
        return html.split(',')

    def valid_url(self, url, host):
        if self.hosts is None:
            self.hosts = self.get_all_hosters()
            
        logger.log_debug('in valid_url %s : %s' % (url, host))
        if url:
            match = re.search('//(.*?)/', url)
            if match:
                host = match.group(1)
            else:
                return False

        if host.startswith('www.'): host = host.replace('www.', '')
        if host and any(host in item for item in self.hosts):
            return True

        return False

    def login(self):
        username = self.get_setting('username')
        password = self.get_setting('password')
        login_data = urllib.urlencode({'action': 'login', 'login_login': username, 'login_password': password})
        url = 'http://alldebrid.com/register/?%s' % (login_data)
        html = self.net.http_GET(url).content
        if '>Control panel<' in html:
            self.net.save_cookies(self.cookie_file)
            self.net.set_cookies(self.cookie_file)
            return True
        else:
            return False

    @classmethod
    def get_settings_xml(cls):
        xml = super(cls, cls).get_settings_xml(include_login=False)
        xml.append('<setting id="%s_login" type="bool" label="%s" default="false"/>' % (cls.__name__, i18n('login')))
        xml.append('<setting id="%s_username" enable="eq(-1,true)" type="text" label="%s" default=""/>' % (cls.__name__, i18n('username')))
        xml.append('<setting id="%s_password" enable="eq(-2,true)" type="text" label="%s" option="hidden" default=""/>' % (cls.__name__, i18n('password')))
        return xml

    @classmethod
    def isUniversal(self):
        return True
