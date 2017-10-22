#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 - 2017 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

import logging
import sopare.config

class log():

    def __init__(self, debug, error):
        self.logger = logging.getLogger()
        self.logformat = '%(levelname)s: %(message)s'
        self.loglevel = logging.ERROR
        if (hasattr(sopare.config, 'LOGFORMAT')):
            self.logformat = sopare.config.LOGFORMAT
        if (debug == True):
            self.loglevel = logging.DEBUG
        elif (hasattr(sopare.config, 'LOGLEVEL')):
            self.loglevel = sopare.config.LOGLEVEL
        self.logger.setLevel(self.loglevel)
        ch = logging.StreamHandler()
        ch.setFormatter(self.logformat)
        if (error == True):
            logging.basicConfig(filename='error.log', filemode='a', loglevel=self.loglevel)

    def getlog(self):
        return self.logger