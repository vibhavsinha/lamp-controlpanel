# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Vibhav Sinha vsinha@webdweb.com
# This file is distributed under the license LGPL version 3 or later
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging, subprocess
from subprocess import PIPE, Popen
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
        p = Popen(['service', 'apache2', 'status'], stdout=PIPE)
        output = p.communicate()[0] = ""
        
    def on_toggleaction1_toggled(self, widget, data=None):
    	if (widget.get_active()):
    		run_command(['gksudo', 'service', 'apache2', 'start'])
    		self.ui.label2.set_text(p.communicate()[0])
    	else:
    		run_command(['gksudo', 'service', 'apache2', 'stop'])
    		self.ui.label2.set_text(p.communicate()[0])


	def on_button1_clicked(self, widget, data=None):
    		run_command(['gksudo', 'service', 'apache2', 'restart'])
    		label2.setText(p.communicate()[0])

    def on_toggleaction2_toggled(self, widget, data=None):
    	if (widget.get_active()):
    		run_command(['gksudo', 'service', 'mysql', 'start'])
    		label2.setText(p.communicate()[0])
    	else:
    		run_command(['gksudo', 'service', 'mysql', 'stop'])
    		label2.setText(p.communicate()[0])


	def on_button2_clicked(self, widget, data=None):
    		run_command(['gksudo', 'service', 'mysql', 'restart'])

	def run_command(cmd, notify):
		p = Popen(cmd, stdout=PIPE)
		self.ui.label2.set_text(p.communicate()[0])
