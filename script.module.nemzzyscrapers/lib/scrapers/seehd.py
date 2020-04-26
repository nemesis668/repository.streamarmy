# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgeGJtY2d1aQ0KaW1wb3J0IHhibWMNCmltcG9ydCB4Ym1jYWRkb24NCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwDQppbXBvcnQgU3RvcmFnZVNlcnZlcg0KaW1wb3J0IHJlDQpjYWNoZSA9IFN0b3JhZ2VTZXJ2ZXIuU3RvcmFnZVNlcnZlcigic2VlaGQiLCAwLjIpDQpkaWFsb2cgPSB4Ym1jZ3VpLkRpYWxvZygpDQoNCg0KI0hlYWRlcnMgPSB7J1VzZXItQWdlbnQnIDogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnIH0NCkdvb2RGaWxlcyA9IFsnLm1wNCcsICcubWt2J10NCg0KDQpjbGFzcyBTY3JhcGVyOg0KCWRlZiBfX2luaXRfXyhzZWxmKToNCgkJc2VsZi5CYXNlID0gJ2h0dHBzOi8vc2VlaGQucGwnDQoJCXNlbGYuU2VhcmNoID0gKCcvJXMtd2F0Y2gtb25saW5lJykNCgkJc2VsZi5saW5rcyA9IFtdDQoJDQoJZGVmIEluZGV4KHNlbGYsdHlwZSx0ZXJtLHllYXIsaW1kYix0b3JyZW50cyk6DQoJCWRlZiBHZXRUb2tlbnMoKToNCgkJCWZyb20gY2xvdWRzY3JhcGVyMiBpbXBvcnQgQ2xvdWRTY3JhcGVyDQoJCQlzY3JhcGVyID0gQ2xvdWRTY3JhcGVyLmNyZWF0ZV9zY3JhcGVyKCkNCgkJCX'
love = 'IuVQ0tW01irzyfoTRiAF4jVPuKnJ5xo3qmBlOIBlOKnJ5xo3qmVR5HVQHhZGftMJ4gE0V7VUW2BwRhBF4jYwZcVRqyL2giYmVjZQtjBGV0ZGptEzylMJMirP8mYwNhZlpAPtxWPKAwpzSjMKVhnTIuMTIlpl51pTEuqTHbrlqIp2IlYHSaMJ50WmbtqJS9XD0XPDxWL29in2yyplN9VUAwpzSjMKVhM2I0XPqbqUEjBv8iq3q3YaAyMJuxYaOfY3qjYJAioaEyoaDiqTuyoJImY2gcL2gup3ZgoJIxnJSmpTSwMF9zLKMcL29hYaOhMlpcYzAio2gcMKZhM2I0K2EcL3DbXD0XPDxWpzI0qKWhVPuwo29enJImYPO1LFxAPtxWnJLtqUyjMFN9CFNaGH9JFHHaBt0XPDxWqUW5Bt0XPDxWPKEypz0tCFO0MKWgYaWypTkuL2HbWlNaYPpgWlxhpzIjoTSwMFtaBvpfWlHmDFpcQDbWPDxWL29in2yypljtqJRtCFOwLJAbMF5wLJAbMHM1ozA0nJ9hXRqyqSEin2IhplxAPtxWPDybMJSxMKWmVQ0trlqIp2IlYHSaMJ50WmbtqJS9QDbWPDxWoTyhnlN9VUWypKIyp3EmYzqyqPumMJkzYxWup2Hep2IfMv5GMJSlL2ttWFO0MKWgYPOwo29enJImCJAio2gcMKZfVTuyLJEypaZ9nTIuMTIlplxhqTI4qN0XPDxWPJMcoT1hLJ1yVQ0tqTIloF50nKEfMFtcQDbWPDxWpTS0qTIlovN9VUVaWlpbC2xcCTyzpzSgMF4eC3AlLm0vXP4dClxvWlpaQDbWPDxWMzyhMTkcozgmVQ0tpzHhMzyhMTSfoPujLKE0MKWhYTkcozffMzkuM3Z9pzHhER9HDHkZ'
god = 'KQ0KCQkJCWZvciBsaW5rcyBpbiBmaW5kbGlua3M6DQoJCQkJCWlmICcyNGhkLmJlJyBpbiBsaW5rczoNCgkJCQkJCWtleSA9IGxpbmtzLnJzcGxpdCgnLycsMSlbMV0NCgkJCQkJCXJlZiA9IGxpbmtzDQoJCQkJCQloZWFkZXJzID0geydVc2VyLUFnZW50JyA6ICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzguMC4zOTA0LjEwOCBTYWZhcmkvNTM3LjM2JywNCgkJCQkJCQkJCSdYLVJlcXVlc3RlZC1XaXRoJyA6ICdYTUxIdHRwUmVxdWVzdCcsDQoJCQkJCQkJCQknUmVmZXJlcicgOiByZWZ9DQoJCQkJCQlsaW5rID0gcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly8yNGhkLmJlL2FwaS9zb3VyY2UvJXMnICUga2V5LCBoZWFkZXJzPWhlYWRlcnMpLmpzb24oKQ0KCQkJCQkJZm9yIGkgaW4gbGlua1snZGF0YSddOg0KCQkJCQkJCXNvdXJjZSA9IGlbJ2ZpbGUnXQ0KCQkJCQkJCXF1YWwgPSBpWydsYWJlbCddDQoJCQkJCQkJc291cmNlID0gc291cmNlKyd8VXNlci1BZ2VudD1Nb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzguMC4zOTA0LjEwOCBTYWZhcmkvNTM3LjM2Jw0KCQkJCQkJCWlmIC'
destiny = 'pkZQtjWlOcovOkqJSfBt0XPDxWPDxWPDy0nKEfMFN9VPtaH0ISFRDtXPORFIWSD1DtXFO8VRMVEPO8VPImWlNyVTMcoT1hLJ1yXD0XPDxWPDxWPDykqJSfnKE5VQ0tWmVaQDbWPDxWPDxWMJkcMvNaAmVjWlOcovOkqJSfBt0XPDxWPDxWPDy0nKEfMFN9VPtaH0ISFRDtXPORFIWSD1DtXFO8VRuRVUjtWKZaVPHtMzyfoJ5uoJHcQDbWPDxWPDxWPKS1LJkcqUxtCFNaZlpAPtxWPDxWPDyyoUAyBt0XPDxWPDxWPDy0nKEfMFN9VPtaH0ISFRDtXPORFIWSD1DtXFO8VSARVUjtWKZaVPHtMzyfoJ5uoJHcQDbWPDxWPDxWPKS1LJkcqUxtCFNaAPpAPtxWPDxWPDymMJkzYzkcozgmYzSjpTIhMPu7W3EcqTkyWmbtqTy0oTHfVPq1pzjaBvOmo3IlL2HfVPqkqJSfnKE5WmbtpKIuoTy0rK0cQDbWPDxWPJIfp2H6QDbWPDxWPDy0nKEfMFN9VPtaH0ISFRDtXPOFMKAioUMyIKWfVPxtsPOVEPO8VPImWlNyVTMcoT1hLJ1yXD0XPDxWPDxWpKIuoTy0rFN9VPpmWj0XPDxWPDxWp2IfMv5fnJ5epl5upUOyozDbrlq0nKEfMFp6VUEcqTkyYPNaqKWfWmbtoTyhn3ZfVPqkqJSfnKE5WmbtpKIuoTy0rK0cQDbWPDxWpzI0qKWhVUAyoTLhoTyhn3ZAPtxWPJI4L2IjqPOSrTAypUEco24tLKZtLmbAPtxWPDy4Lz1wYzkiMltvEIWFG1VtBwb6VPImVvNyLlNfVTkyqzIfCKuvoJZhGR9UGx9HFHASXD0XPDyyoUAyBvOjLKAmQDbWQDbAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))