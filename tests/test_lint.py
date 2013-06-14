#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Vibhav Sinha vsinha@webdweb.com
# This file is distributed under the license LGPL version 3 or later
### END LICENSE

import unittest
import subprocess

class TestPylint(unittest.TestCase):
    def test_project_errors_only(self):
        '''run pylint in error only mode
        
        your code may well work even with pylint errors
        but have some unusual code'''
        return_code = subprocess.call(["pylint", '-E', 'lamp_controlpanel'])
        # not needed because nosetests displays pylint console output
        #self.assertEqual(return_code, 0)

    # un-comment the following for loads of diagnostics   
    #~ def test_project_full_report(self):
        #~ '''Only for the brave
#~ 
        #~ you will have to make judgement calls about your code standards
        #~ that differ from the norm'''
        #~ return_code = subprocess.call(["pylint", 'lamp_controlpanel'])

if __name__ == '__main__':
    'you will get better results with nosetests'
    unittest.main()
