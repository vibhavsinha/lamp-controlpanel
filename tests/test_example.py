#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Vibhav Sinha vsinha@webdweb.com
# This file is distributed under the license LGPL version 3 or later
### END LICENSE

import sys
import os.path
import unittest
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from lamp_controlpanel import AboutLampControlpanelDialog

class TestExample(unittest.TestCase):
    def setUp(self):
        self.AboutLampControlpanelDialog_members = [
        'AboutDialog', 'AboutLampControlpanelDialog', 'gettext', 'logger', 'logging']

    def test_AboutLampControlpanelDialog_members(self):
        all_members = dir(AboutLampControlpanelDialog)
        public_members = [x for x in all_members if not x.startswith('_')]
        public_members.sort()
        self.assertEqual(self.AboutLampControlpanelDialog_members, public_members)

if __name__ == '__main__':    
    unittest.main()
