#!/usr/bin/env python

import TCA9548A as TCA

tca = TCA.TCA9548A() # Set to default address of 0x70

tca.select_i2c_device(2) # Select channel 2 of the multiplexor

###############
#
# Code to operate a device connected to channel 2 of the multiplexor
#
###############


tca.select_i2c_device(0) # Select channel 0 of the multiplexor

###############
#
# Code to operate a device connected to channel 0 of the multiplexor
#
###############
