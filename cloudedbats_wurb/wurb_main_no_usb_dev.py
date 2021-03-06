#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org
# Copyright (c) 2016-2018 Arnold Andreasson 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import wurb_core

if __name__ == "__main__":
    """ Main module for CloudedBats WURB, 
        Wireless Ultrasonic Recorder for Bats.
        
        To be used when using the internal SD card to record sound. 
        For example when using 'Raspberry Pi Zero'. """
        
    wurb_app = wurb_core.WurbApplication(usb_memory_used=False)

# TODO: For development.
    import time
    print('TEST - Started')
    time.sleep(1.0)
#     wurb_app.perform_event('test_rec_on')
#     time.sleep(5.5) 
    wurb_app.perform_event('test_rec_on')
    time.sleep(25.5) 
    wurb_app.perform_event('test_rec_off')
    time.sleep(1.0)
    wurb_app.stop()
    print('TEST - Finished')
