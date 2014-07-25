#!/usr/bin/env python
"""
AETHER
Autonomous Envelope-Tiltrotor Hybrid for Environmental Reconnaissance

AETHER is multipurpose UAS (Unmanned Aerial System) designed for both
proximal sensing and remote sensing of agricultural and environmental operations.
By utilizing a helium envelope, an agile tiltrotor propulsion system, and a
dedicted quadrotor lifting platform, AETHER is capable of stable and long-term flights.
"""

__author__ = 'Trevor Stanhope'
__version__ = '0.1'

# Modules
import cv2
import numpy as np
import serial
import gps
import pymongo
import json
from datetime import datetime

def format_time():
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S.%f')

class AETHER:
    def __init__(self, config):
        with open(config, 'w') as configfile
            self.config = json.loads(configfile.read())
    def update_gps(self):
        pass
    def navigate_to(self):
        pass
        
if __name__ == '__main__':
    session = AETHER('settings.json')
