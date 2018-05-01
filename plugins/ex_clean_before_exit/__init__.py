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

## Fix
## RuntimeWarning: This channel is already in use, continuing anyway.

#import RPi.GPIO as GPIO

## Use BCM GPIO references.
## instead of physical pin numbers.
#GPIO.setmode(GPIO.BCM)
#PIN = 17
#GPIO.setup(PIN,GPIO.OUT)
#GPIO.output(PIN, False)

def run(readable_results, data, rawbuf):
    #if ('on' in readable_results):
    #   GPIO.output(PIN, True)
    #elif ('off' in readable_results):
    #   GPIO.output(PIN, False)

    ## do somthing.
    pass

def exit():
    ## GPIO need cleanup before exit.
    #GPIO.cleanup()
    pass
