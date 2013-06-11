# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('lamp_controlpanel')

from lamp_controlpanel_lib import Window
from lamp_controlpanel.AboutLampControlpanelDialog import AboutLampControlpanelDialog
from lamp_controlpanel.PreferencesLampControlpanelDialog import PreferencesLampControlpanelDialog

# See lamp_controlpanel_lib.Window.py for more details about how this class works
class LampControlpanelWindow(Window):
    __gtype_name__ = "LampControlpanelWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(LampControlpanelWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutLampControlpanelDialog
        self.PreferencesDialog = PreferencesLampControlpanelDialog

        # Code for other initialization actions should be added here.

