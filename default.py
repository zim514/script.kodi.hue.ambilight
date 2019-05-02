# -*- coding: utf-8 -*-
import logging
import sys

import xbmcaddon

from resources.lib import kodilogging
from resources.lib import core
from resources.lib import globals


# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()
ADDONID = ADDON.getAddonInfo('id')
ADDONVERSION = ADDON.getAddonInfo('version')

kodilogging.config()
logger = logging.getLogger(__name__)

logger.debug("Loading '%s' version '%s'" % (ADDONID, ADDONVERSION))


if globals.REMOTE_DBG:
    # Make pydev debugger works for auto reload.
    # Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
    
    try:

        sys.path.append('e:\dev\pysrc')
        import threading
        import pydevd

        threading.Thread.name = 'script.service.hue.menu'
        pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True, suspend=globals.REMOTE_DBG_SUSPEND)
                        #trace_only_current_thread=True, overwrite_prev_trace=True, patch_multiprocessing=False)

    except ImportError:
        logger.debug("Kodi Hue Remote Debug Error: " + 
                         "You must add org.python.pydev.debug.pysrc to your PYTHONPATH, or disable REMOTE_DBG")
        sys.exit(1)



core.menu()
logger.debug("'%s' shutting down menu" % ADDONID)


