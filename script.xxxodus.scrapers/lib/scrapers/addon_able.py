import datetime
import os
from sqlite3 import dbapi2 as db_lib

import xbmc
import xbmcaddon

db_dir = xbmc.translatePath("special://profile/Database")
db_path = os.path.join(db_dir, 'Addons27.db')

conn = db_lib.connect(db_path)
conn.text_factory = str


def set_enabled(newaddon, data=None):
    if xbmcaddon.Addon().getAddonInfo('version') > 16.5:
        setit = 1
        if data is None:
            data = ''
        now = datetime.datetime.now()
        date_time = str(now).split('.')[0]
        # sql = 'REPLACE INTO installed (addonID,enabled) VALUES(?,?)'
        sql = 'REPLACE INTO installed (addonID,enabled,installDate) VALUES(?,?,?)'
        conn.execute(sql, (newaddon, setit, date_time,))
        conn.commit()
        # xbmc.executebuiltin("InstallAddon(%s)" % newaddon)
        xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
    else:
        pass


def setall_enable():
    if xbmcaddon.Addon().getAddonInfo('version') > 16.5:
        addonfolder = xbmc.translatePath(os.path.join('special://home', 'addons'))
        contents = os.listdir(addonfolder)
        conn.executemany('update installed set enabled=1 WHERE addonID = (?)', ((val,) for val in contents))
        conn.commit()
    else:
        pass
