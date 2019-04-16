# -*- coding: utf-8 -*-

import pkgutil
import os.path
import xbmc

def sources():
    try:
        sourceDict = []
        for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.dirname(__file__)]):
            if is_pkg:
                continue
            try:
                module = loader.find_module(module_name).load_module(module_name)
                sourceDict.append((module_name, module.Scraper()))
            except Exception as e:
                xbmc.log('Could not load "%s": %s' % (module_name, e), xbmc.LOGNOTICE)
        return sourceDict
    except:
        return []


