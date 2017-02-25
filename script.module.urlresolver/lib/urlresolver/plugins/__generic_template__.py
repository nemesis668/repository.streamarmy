"""
    Kodi urlresolver plugin
    Copyright (C) 2016  script.module.urlresolver

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

from lib import helpers
from urlresolver.resolver import UrlResolver, ResolverError


class TemplateResolver(UrlResolver):
    """
    Template Resolver
    - change class name from TemplateResolver to <UniqueName>Resolver
    ___
    name |str| : resolver name
    domains |list of str| : list of supported domains
    pattern |str| : supported uri regex pattern, match groups: 1=host, 2=media_id
    """
    name = 'template'
    domains = ['templ.ate']
    pattern = '(?://|\.)(templ\.ate)/(?:embed/)?([0-9a-zA-Z]+)'

    def get_media_url(self, host, media_id):
        """
        source scraping to get resolved uri goes here
        return |str| : resolved/playable uri or raise ResolverError
        ___
        helpers.get_media_url result_blacklist: |list of str| : list of strings to blacklist in source results
        """
        return helpers.get_media_url(self.get_url(host, media_id), result_blacklist=None)

    def get_url(self, host, media_id):
        """
        return |str| : uri to be used by get_media_url
        ___
        _default_get_url template: |str| : 'http://{host}/embed-{media_id}.html'
        """
        return self._default_get_url(host, media_id, template=None)
