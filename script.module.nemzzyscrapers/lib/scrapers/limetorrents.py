# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgcmUNCmltcG9ydCB4Ym1jDQppbXBvcnQgeGJtY2d1aQ0KaW1wb3J0IHRpbWUNCmZyb20gcmFuZG9tIGltcG9ydCByYW5kaW50DQpkaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpDQpmcm9tIGNsb3Vkc2NyYXBlcjIgaW1wb3J0IENsb3VkU2NyYXBlcg0KQ0YgPSBDbG91ZFNjcmFwZXIuY3JlYXRlX3NjcmFwZXIoKQ0KY2xhc3MgU2NyYXBlcjoNCglkZWYgX19pbml0X18oc2VsZik6DQoJCXNlbGYuQmFzZSA9ICdodHRwczovL3d3dy5saW1ldG9ycmVudHMuaW5mby8nDQoJCXNlbGYuU2VhcmNoID0gKCcvc2VhcmNoL2FsbC8lcy9sZWVjaHMvMS8nKQ0KCQlzZWxmLmxpbmtzID0gW10NCg0KCWRlZiBJbmRleChzZWxmLHR5cGUsIHRlcm0seWVhcixpbWRiLHRvcnJlbnRzKToNCgkJaWYgdHlwZSA9PSAnVFYnOg0KCQkJTW92aWVOYW1lID0gdGVybQ0KCQkJI3Rlcm0gPSB0ZXJtLnJlcGxhY2UoJ1RWfHx8JywnJykNCgkJCXRlcm0gPSB0ZXJtLnJlcGxhY2UoJyAnLCctJykNCgkJCWxpbmsgPSBDRi5nZXQoc2VsZi5CYXNlK3NlbGYuU2VhcmNoICV0ZXJtLCBoZWFkZXJzPXsiVXNlci1BZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4z'
love = 'AvNbF0uHGHjfVTkcn2HtE2Iwn28cVRAbpz9gMF83Zv4jYwZ2ZwLhZGVkVSAuMzSlnF81ZmphZmLvsFxhL29hqTIhqN0XPDxWoJS0L2ttCFOlMF5znJ5xLJkfXPqHo3WlMJ50VR5uoJH8Y3AjLJ4+XP4dClx8MTy2VTyxCFWlnJqbqTWupvV+WlkfnJ5eYTMfLJqmCKWyYxECIRSZGPyoZS0APtxWPKOuqUEypz4tCFOlWlpanUWyMw1oWlWqXSgrWlWqXlyoWlWqWlpaQDbWPDyaMKEfnJ5eplN9VUWyYzMcozEuoTjbpTS0qTIlovkgLKEwnPxAPtxWPJyzVT5iqPOaMKEfnJ5epmbtpzI0qKWhVRMuoUAyQDbWPDyzo3VtoTyhnlOcovOaMKEfnJ5epmbAPtxWPDycMvOmMJkzYxWup2Htoz90VTyhVTkcozftLJ5xVPphnUEgoPptnJ4toTyhnmbAPtxWPDxWoTyhnlN9VUAyoTLhDzSmMFgfnJ5eQDbWPDxWPJyzVPq1nTDaVTyhVTkcozfhoT93MKVbXGbtp29lqPN9VPp1WlN7VUS1LJjtCFNaARftIHuRWj0XPDxWPDyyoTyzVPplZGLjWlOcovOfnJ5eYzkiq2IlXPx6VUAipaDtCFNaAFp7VUS1LJjtCFNaARftIHuRWj0XPDxWPDyyoTyzVPpkZQtjWlOcovOfnJ5eYzkiq2IlXPx6VUAipaDtCFNaAvp7VUS1LJjtCFNaZGN4ZPpAPtxWPDxWMJkcMvNaAmVjWlOcovOfnJ5eYzkiq2IlXPx6VUAipaDtCFNaAlp7VUS1LJjtCFNaAmVjWj0XPDxWPDyyoUAyVQbt'
god = 'c29ydCA9ICc4JzsgcXVhbCA9ICdTRCcNCgkJCQkJdGl0bGUgPSAnTGltZVRvcnJlbnRzICggUmVhbCBEZWJyaWQgKSB8ICcgKyBxdWFsICsgJyB8ICcgK01vdmllTmFtZQ0KCQkJCQlzZWxmLmxpbmtzLmFwcGVuZCh7J3RpdGxlJzogdGl0bGUsICd1cmwnOiBsaW5rLCAncXVhbGl0eScgOiBzb3J0fSkNCgkJCXJldHVybiBzZWxmLmxpbmtzDQoJCWVsc2U6DQoJCQlNb3ZpZU5hbWUgPSB0ZXJtDQoJCQl0ZXJtID0gdGVybS5yZXBsYWNlKCcgJywnKycpDQoJCQlsaW5rID0gQ0YuZ2V0KHNlbGYuQmFzZStzZWxmLlNlYXJjaCAldGVybSwgaGVhZGVycz17IlVzZXItQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzIuMC4zNjI2LjEyMSBTYWZhcmkvNTM3LjM2In0pLmNvbnRlbnQNCgkJCW1hdGNoID0gcmUuZmluZGFsbCgnVG9ycmVudCBOYW1lPC9zcGFuPiguKj8pPGRpdiBpZD0icmlnaHRiYXIiPicsbGluayxmbGFncz1yZS5ET1RBTEwpWzBdDQoJCQlwYXR0ZXJuID0gcicnJ2hyZWY9WyciXShbXiciXSspWyciXScnJw0KCQkJZ2V0bGlua3MgPSByZS5maW5kYWxsKHBhdHRlcm4sbWF0Y2gpDQoJCQlpZiBub3Qg'
destiny = 'M2I0oTyhn3Z6VUWyqUIlovOTLJkmMD0XPDxWMz9lVTkcozftnJ4tM2I0oTyhn3Z6QDbWPDxWnJLtp2IfMv5PLKAyVT5iqPOcovOfnJ5eVTShMPNaYzu0oJjaVTyhVTkcozf6QDbWPDxWPJyzVUyyLKVhp3ElnKNbXFOcovOfnJ5eBt0XPDxWPDxWoTyhnlN9VUAyoTLhDzSmMFgfnJ5eQDbWPDxWPDycMvNaqJuxWlOcovOfnJ5eYzkiq2IlXPx6VUAipaDtCFNaAFptBlOkqJSfVQ0tWmEYVSIVEPpAPtxWPDxWPJIfnJLtWmVkAwNaVTyhVTkcozfhoT93MKVbXGbtp29lqPN9VPp1WmftpKIuoPN9VPp0FlOIFRDaQDbWPDxWPDyyoTyzVPpkZQtjWlOcovOfnJ5eYzkiq2IlXPx6VUAipaDtCFNaAvp7VUS1LJjtCFNaZGN4ZPpAPtxWPDxWPJIfnJLtWmplZPptnJ4toTyhnl5fo3qypvtcBvOmo3W0VQ0tWmpaBlOkqJSfVQ0tWmplZPpAPtxWPDxWPJIfp2HtBvOmo3W0VQ0tWmtaBlOkqJSfVQ0tW1ARWj0XPDxWPDxWqTy0oTHtCFNaJ0ACGR9FVUyyoTkiq11ZnJ1yIT9lpzIhqUZtXPOFMJSfVREyLaWcMPNcVUjtJl9QG0kCHy0aVPftpKIuoPNeVPptsPNaVPgAo3McMH5uoJHAPtxWPDxWPKAyoTLhoTyhn3ZhLKOjMJ5xXUfaqTy0oTHaBvO0nKEfMFjtW3IloPp6VTkcozffVPqkqJSfnKE5WlN6VUAipaE9XD0XPDxWpzI0qKWhVUAyoTLhoTyhn3ZAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))