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
		services = [('apache2', self.ui.toggleaction1), ('mysql', self.ui.toggleaction2), ('ssh', self.ui.toggleaction3)]
		for service in services :
			p = Popen(['service', service[0], 'status'], stdout=PIPE)
			out = p.communicate()[0]
			if 'NOT' in out or 'stop in ':
				print out
			else :
				print out + 'set it to on'
		
	def on_toggleaction1_toggled(self, widget, data=None):
		if (widget.get_active()):
			self.run_command(['gksudo', 'service', 'apache2', 'start'])
		else:
			self.run_command(['gksudo', 'service', 'apache2', 'stop'])


	def on_button1_clicked(self, widget, data=None):
			self.run_command(['gksudo', 'service', 'apache2', 'restart'])
			label2.setText(p.communicate()[0])

	def on_toggleaction2_toggled(self, widget, data=None):
		if (widget.get_active()):
			self.run_command(['gksudo', 'service', 'mysql', 'start'])
		else:
			self.run_command(['gksudo', 'service', 'mysql', 'stop'])


	def on_button2_clicked(self, widget, data=None):
			self.run_command(['gksudo', 'service', 'mysql', 'restart'])


	def on_toggleaction3_toggled(self, widget, data=None):
		if (widget.get_active()):
			self.run_command(['gksudo', 'service', 'ssh', 'start'])
		else:
			self.run_command(['gksudo', 'service', 'ssh', 'stop'])


	def on_button3_clicked(self, widget, data=None):
			self.run_command(['gksudo', 'service', 'ssh', 'restart'])

	def run_command(item, cmd):
		for i in cmd:
			print i
		p = subprocess.Popen(cmd, stdout=PIPE)
		item.ui.label2.set_text(p.communicate()[0])



