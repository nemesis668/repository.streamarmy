# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0jIyMjIyMjIyMjIyMjIyMjIyMjIyBTVEFSVCBBRERPTiBJTVBPUlRTICMjIyMjIyMjIyMjIyMjIyMjIyMjDWltcG9ydCB4Ym1jDWltcG9ydCB4Ym1jYWRkb24NaW1wb3J0IHhibWNndWkNaW1wb3J0IHhibWNwbHVnaW4NaW1wb3J0IG9zDWltcG9ydCByZQ1pbXBvcnQgcmVxdWVzdHMNaW1wb3J0IHN5cw1pbXBvcnQgYmFzZTY0DWltcG9ydCBqc29uDWltcG9ydCB0aW1lDWltcG9ydCBkYXRldGltZQ1pbXBvcnQgcHl4Ym1jdC5hZGRvbndpbmRvdyBhcyBweXhibWN0DWZyb20gYWRkb24uY29tbW9uLmFkZG9uIGltcG9ydCBBZGRvbg1pbXBvcnQgcmVzb2x2ZXVybA1mcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA1yZWxvYWQoc3lzKQ1zeXMuc2V0ZGVmYXVsdGVuY29kaW5nKCJ1dGYtOCIpDWRpYWxvZyA9IHhibWNndWkuRGlhbG9nKCkNI2NhY2hlICAgICAgICAgICAgICAgPSBTdG9yYWdlU2VydmVyLlN0b3JhZ2VTZXJ2ZXIoImVudGVydGFpbm1lIiwgMC4yKQ0jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDSMjIyMjIyMjIyMjIyMjIyMjIyMjIFNFVCBBRERPTiBJRCAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNX2FkZG9uX2lkXyA9ICdwbHVnaW4udmlkZW8uRW50ZXJ0YWluTWUnDV9zZWxmXyA9IHhibWNhZGRvbi5BZGRvbihpZD1fYWRkb25faWRfKQ1EYXRlID0gdGltZS5zdHJmdGltZSgiJUEgJUIgJWQiKQ1BZGRvblRpdGxlID0gJ1tCXVtDT0xPUiByZWRdRVtDT0xPUiB5ZWxsb3ddbnRlcnRhaW4gTWVbL0JdWy9DT0xPUl0nDWRwID0geGJtY2d1aS5EaWFsb2dQcm9ncmVzcygpDWljb24gID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBfYWRkb25faWRfLCAnaWNvbi5wbmcnKSkNQWRkb25pY29uICA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXywgJ2ljb24ucG5nJykpDSMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNIyMjIyMjIyMjIyMjIyMjIyMjIyMgU0VUIEFERE9OIFRIRU1FIERJUkVDVE9SWSAjIyMjIyMjIyMjIyMjIw1fdGhlbWVfCQkJPSBfc2VsZl8uZ2V0U2V0dGluZygnVGhlbWUnKQ1faW1hZ2VzXwkJPSAnL3Jlc291cmNlcy8nICsgX3RoZW1lXwkNIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0jIyMjIyMjIyMjIyMjIyMjIyMjIyBTRVQgQURET04gVEhFTUUgSU1BR0VTICMjIyMjIyMjIyMjIyMjIyMjDUJhY2tncm91bmRfSW1hZ2UgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ2JnLmpwZycpKQ1TVGV4dCA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXyArIF9pbWFnZXNfLCAnc2VhcmNodHh0LnBuZycpKQ1CdXR0b25GcmFtZSA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXyArIF9pbWFnZXNfLCAnQnV0dG9uRnJhbWUucG5nJykpDUJ1dHRvbkZyYW1lUyA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXyArIF9pbWFnZXNfLCAnQnV0dG9uRnJhbWVTLnBuZycpKQ1CdXR0b25Nb3ZpZXMgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ01vdmllc19CdXR0b24ucG5nJykpDUJ1dHRvbk1vdmllc1MgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ01vdmllc19CdXR0b25TLnBuZycpKQ1CdXR0b25UdlNob3dzID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBfYWRkb25faWRfICsgX2ltYWdlc18sICdTaG93c19CdXR0b24ucG5nJykpDUJ1dHRvblR2U2hvd3NTID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBfYWRkb25faWRfICsgX2ltYWdlc18sICdTaG93c19CdXR0b25TLnBuZycpKQ1CdXR0b25TZWFyY2ggPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ2J1dHRvbl9zZWFyY2gucG5nJykpDUJ1dHRvblNlYXJjaFMgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ2J1dHRvbl9zZWFyY2hTLnBuZycpKQ1CdXR0b25RdWl0ID0geGJtYy50cmFuc2xhdGVQYXRoKG9zLnBhdGguam9pbignc3BlY2lhbDovL2hvbWUvYWRkb25zLycgKyBfYWRkb25faWRfICsgX2ltYWdlc18sICdRdWl0X0J1dHRvbi5wbmcnKSkNQnV0dG9uUXVpdFMgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ1F1aXRfQnV0dG9uUy5wbmcnKSkNTGlzdF9Gb2N1c2VkX2RlZmF1bHQgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJyArIF9hZGRvbl9pZF8gKyBfaW1hZ2VzXywgJ2xpc3QtYmctc2VsZWN0ZWQtZGVmYXVsdC5wbmcnKSkNTGlzdF9iZyA9IHhibWMudHJhbnNsYXRlUGF0aChvcy5wYXRoLmpvaW4oJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nICsgX2FkZG9uX2lkXyArIF9pbWFnZXNfLCAnbGlzdC1iZy5wbmcnKSkNTW92aWVCYXNlID0gJ2h0dHBzOi8vc2VlaGQub25saW5lLycNIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0jIyMjIyMjIyMjIEZ1bmN0aW9uIFRvIENhbGwgVGhhdCBTdGFydHMgVGhlIFdpbmRvdyAjIyMjIyMjIyMjDWRlZiBNYWluV2luZG93KCk6DQl3aW5kb3cgPSBNYWluKCdFbnRlcnRhaW5NZScpDQl3aW5kb3cuZG9Nb2RhbCgpDQlkZWwgd2luZG93DQ0NZGVmIHBvcChzZWxmKToNCWdsb2JhbCBsb2dvcw0JZ2xvYmFsIHVybHMNCWdsb2JhbCBtb3ZpZXRpdGxlcw0JbG9nb3MgPSBbXQ0JdXJscyA9IFtdDQltb3ZpZXRpdGxlcyA9IFtdDQloZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnfQ0JTW92aWVCYXNlID0gJ2h0dHBzOi8vc2VlaGQub25saW5lLycNCWxpbmsgPSByZXF1ZXN0cy5nZXQoTW92aWVCYXNlLGhlYWRlcnM9aGVhZGVycykudGV4dA0Jc291cCA9IEJlYXV0aWZ1bFNvdXAobGluaywgJ2h0bWwucGFyc2VyJykNCWRhdGEgPSBzb3VwLmZpbmQoJ2RpdicsIGNsYXNzXz17J3Nob3dwb3N0NCBwb3N0aG9tZSd9KQ0JdXJscy5hcHBlbmQoJycpDQltb3ZpZXRpdGxlcy5hcHBlbmQoJycpDQlsb2dvcy5hcHBlbmQoJycpDQlsaSA9IHhibWNndWkuTGlzdEl0ZW0oJ1tDT0xPUiByZWRdW0JdTEFURVNUIEFEREVEIE1PVklFUyAmIFNIT1dTWy9CXVsvQ09MT1JdJywgaWNvbkltYWdl'
love = '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'
god = 'SVNUMi5yZXNldCgpDQlsb2dvcyA9IFtdDQl1cmxzID0gW10NCW1vdmlldGl0bGVzID0gW10NCXNlbGYuTElTVDIuc2V0VmlzaWJsZShUcnVlKQ0Jc2VsZi5idXR0b24xLmNvbnRyb2xSaWdodChzZWxmLkxJU1QyKQ0Jc2VsZi5idXR0b24yLmNvbnRyb2xSaWdodChzZWxmLkxJU1QyKQ0Jc2VsZi5idXR0b240LmNvbnRyb2xMZWZ0KHNlbGYuTElTVDIpDQlzZWxmLmJ1dHRvbjMuY29udHJvbExlZnQoc2VsZi5MSVNUMikNCXNlbGYuTElTVC5zZXRWaXNpYmxlKEZhbHNlKQ0JdXJscy5hcHBlbmQoJycpDQltb3ZpZXRpdGxlcy5hcHBlbmQoJycpDQlsb2dvcy5hcHBlbmQoJycpDQlsaSA9IHhibWNndWkuTGlzdEl0ZW0oJ1tDT0xPUiByZWRdW0JdVFYgU0hPV1NbL0JdWy9DT0xPUl0nLCBpY29uSW1hZ2U9QWRkb25pY29uKQ0Jc2VsZi5MSVNUMi5hZGRJdGVtKGxpKQ0JaGVhZGVycyA9IHsnVXNlci1BZ2VudCc6ICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNjAuMC4zMTEyLjExMyBTYWZhcmkvNTM3LjM2J30NCWxpbmsgPSByZXF1ZXN0cy5nZXQodXJsLGhlYWRlcnM9aGVhZGVycykudGV4dA0Jc291cCA9IEJlYXV0aWZ1bFNvdXAobGluaywgJ2h0bWwucGFyc2VyJykNCWRhdGEgPSBzb3VwLmZpbmQoJ3NlY3Rpb24nLCBjbGFzc189eydzaG93cGVsaWN1bGFzIGNvbC1tdC04J30pDQlmb3IgaSBpbiBkYXRhLmZpbmRfYWxsKCdkaXYnLCBjbGFzc189eydwb3N0ZXItbWVkaWEtY2FyZCd9KToNCQluYW1lID0gaS5hWyd0aXRsZSddLnJlcGxhY2UoJ1dhdGNoIE9ubGluZSBGcmVlJywnJykNCQltZWRpYSA9IGkuYVsnaHJlZiddDQkJaWNvbiA9IGkuaW1nWydzcmMnXQ0JCWlmIG5vdCBNb3ZpZUJhc2UgaW4gaWNvbjogaWNvbiA9ICgnJXMlcycgJSAoTW92aWVCYXNlLGljb24pKQ0JCW1vdmlldGl0bGVzLmFwcGVuZChuYW1lKQ0JCXVybHMuYXBwZW5kKG1lZGlhKQ0JCWxvZ29zLmFwcGVuZChpY29uKQ0JCWxpID0geGJtY2d1aS5MaXN0SXRlbShuYW1lLCBpY29uSW1hZ2U9aWNvbikNCQlzZWxmLkxJU1QyLmFkZEl0ZW0obGkpDQl0cnk6DQkJcGFnZW51bWJlciA9IHVybC5zdHJpcCgnLycpWy0xXQ0JCXBhZ2VudW1iZXIgPSBpbnQocGFnZW51bWJlcikNCQluZXdudW1iZXIgPSBwYWdlbnVtYmVyICsgMQ0JCW5ld3VybCA9ICgnaHR0cHM6Ly9zZWVoZC5vbmxpbmUvY2F0ZWdvcnkvdHYtc2VyaWVzL3BhZ2UvJXMnICUgbmV3bnVtYmVyKQ0JCW5hbWUgPSAnTmV4dCBQYWdlJw0JCW1vdmlldGl0bGVzLmFwcGVuZChuYW1lKQ0JCXVybHMuYXBwZW5kKCdORVhUOjo6JXMnICUgbmV3dXJsKQ0JCWxvZ29zLmFwcGVuZChBZGRvbmljb24pDQkJbGkgPSB4Ym1jZ3VpLkxpc3RJdGVtKG5hbWUsIGljb25JbWFnZT1BZGRvbmljb24pDQkJc2VsZi5MSVNUMi5hZGRJdGVtKGxpKQ0JZXhjZXB0OiBwYXNzDQlzZWxmLnNldEZvY3VzKHNlbGYuTElTVDIpDWRlZiBNT1ZJRVMoc2VsZix1cmwsY2F0KToNDQlnbG9iYWwgbG9nb3MNCWdsb2JhbCB1cmxzDQlnbG9iYWwgbW92aWV0aXRsZXMNCXNlbGYuTElTVDIucmVzZXQoKQ0JbG9nb3MgPSBbXQ0JdXJscyA9IFtdDQltb3ZpZXRpdGxlcyA9IFtdDQlzZWxmLkxJU1QyLnNldFZpc2libGUoVHJ1ZSkNCXNlbGYuYnV0dG9uMS5jb250cm9sUmlnaHQoc2VsZi5MSVNUMikNCXNlbGYuYnV0dG9uMi5jb250cm9sUmlnaHQoc2VsZi5MSVNUMikNCXNlbGYuYnV0dG9uNC5jb250cm9sTGVmdChzZWxmLkxJU1QyKQ0Jc2VsZi5idXR0b24zLmNvbnRyb2xMZWZ0KHNlbGYuTElTVDIpDQlzZWxmLkxJU1Quc2V0VmlzaWJsZShGYWxzZSkNCXVybHMuYXBwZW5kKCcnKQ0JbW92aWV0aXRsZXMuYXBwZW5kKCcnKQ0JbG9nb3MuYXBwZW5kKCcnKQ0JbGkgPSB4Ym1jZ3VpLkxpc3RJdGVtKCdbQ09MT1IgcmVkXVtCXSVzIE1vdmllc1svQl1bL0NPTE9SXScgJSBjYXQsIGljb25JbWFnZT1BZGRvbmljb24pDQlzZWxmLkxJU1QyLmFkZEl0ZW0obGkpDQloZWFkZXJzID0geydVc2VyLUFnZW50JzogJ01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS82MC4wLjMxMTIuMTEzIFNhZmFyaS81MzcuMzYnfQ0JbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz1oZWFkZXJzKS50ZXh0DQlzb3VwID0gQmVhdXRpZnVsU291cChsaW5rLCAnaHRtbC5wYXJzZXInKQ0JZGF0YSA9IHNvdXAuZmluZCgnc2VjdGlvbicsIGNsYXNzXz17J3Nob3dwZWxpY3VsYXMgY29sLW10LTgnfSkNCWZvciBpIGluIGRhdGEuZmluZF9hbGwoJ2RpdicsIGNsYXNzXz17J3Bvc3Rlci1tZWRpYS1jYXJkJ30pOg0JCW5hbWUgPSBpLmFbJ3RpdGxlJ10ucmVwbGFjZSgnV2F0Y2ggT25saW5lIEZyZWUnLCcnKQ0JCW1lZGlhID0gaS5hWydocmVmJ10NCQlpY29uID0gaS5pbWdbJ3NyYyddDQkJaWYgbm90IE1vdmllQmFzZSBpbiBpY29uOiBpY29uID0gKCclcyVzJyAlIChNb3ZpZUJhc2UsaWNvbikpDQkJbW92aWV0aXRsZXMuYXBwZW5kKG5hbWUpDQkJdXJscy5hcHBlbmQobWVkaWEpDQkJbG9nb3MuYXBwZW5kKGljb24pDQkJbGkgPSB4Ym1jZ3VpLkxpc3RJdGVtKG5hbWUsIGljb25JbWFnZT1pY29uKQ0JCXNlbGYuTElTVDIuYWRkSXRlbShsaSkNCXRyeToNCQlwYWdlbnVtYmVyID0gdXJsLnN0cmlwKCcvJylbLTFdDQkJcGFnZW51bWJlciA9IGludChwYWdlbnVtYmVyKQ0JCW5ld251bWJlciA9IHBhZ2VudW1iZXIgKyAxDQkJbmV3dXJsID0gKCdodHRwczovL3NlZWhkLm9ubGluZS9jYXRlZ29yeS8lcy9wYWdlLyVzJyAlIChjYXQsbmV3bnVtYmVyKSkNCQluYW1lID0gJ05leHQgUGFnZScNCQltb3ZpZXRpdGxlcy5hcHBlbmQobmFtZSkNCQl1cmxzLmFwcGVuZCgnTkVYVDo6OiVzJyAlIG5ld3VybCkNCQlsb2dvcy5hcHBlbmQoQWRkb25pY29uKQ0JCWxpID0geGJtY2d1aS5MaXN0SXRlbShuYW1lLCBpY29uSW1hZ2U9QWRkb25pY29uKQ0JCXNlbGYuTElTVDIuYWRkSXRlbShsaSkNCWV4Y2VwdDogcGFzcw0Jc2VsZi5zZXRGb2N1cyhzZWxmLkxJU1QyKQ1kZWYgR2VucmUoc2VsZix1cmwpOg0JdWEgPSB7J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzYwLjAuMzExMi4xMTMgU2FmYXJpLzUzNy4zNid9DQljYXR1cmwgPSBbXSA7IGNhdG5hbWUgPSBbXQ0JbGluayA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz11YSkudGV4dA0Jc291cCA9IEJlYXV0aWZ1bFNvdXAobGluaywgJ2h0bWwucGFyc2VyJykNCWRhdGEgPSBzb3VwLmZpbmQoJ2RpdicsIGlkPXsnY2F0ZWdvcmllcy0yJ30pDQlmb3IgaSBpbiBkYXRhLmZpbmRfYWxsKCdsaScpOg0JCW5hbWUgPSBpLmEudGV4dA0JCXVybDIgPSBpLmFbJ2hyZWYnXQ0JCXVybDIgPSAoJyVzL3BhZ2UvMS8nICUgdXJsMikNCQljYXRuYW1lLmFwcGVuZChuYW1lKQ0JCWNhdHVybC5hcHBlbmQodXJsMikNCXNlbGVjdCA9IGRpYWxvZy5zZWxlY3QoJ0Nob29zZSBBIENhdGVnb3J5JyxjYXRuYW1lKQ0JaWYgc2VsZWN0IDwgMDogcXVpdCgpDQlNT1ZJRVMoc2VsZixjYXR1cmxbc2VsZWN0XSxjYXRuYW1lW3NlbGVjdF0pDWRlZiBraWxsYWRkb24oc2VsZik6DQl4Ym1jLmV4ZWN1dGVidWlsdGluKCJYQk1DLkNvbnRhaW5lci5VcGRhdGUocGF0aCxyZXBsYWNlKSIpDQl4Ym1jLmV4ZWN1dGVidWlsdGluKCJYQk1DLkFjdGl2YXRlV2luZG93KEhvbWUpIikNDSMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNIyMjIyMjIyMjIENsYXNzIENv'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))