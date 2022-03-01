#!/usr/bin/env python

"""
TCA9548A.py
Function: A simple class to operate a TCA9548A I2C multiplexor on an RPi with Python
Author: Benjamin Walt
Date: 12/16/2021
Version: 0.1
Copyright (c) Benjamin Thomas Walt
Licensed under the MIT license.
Note: This was written for Python 2.x, so it may require some modification for later versions.
"""

import smbus


class TCA9548A:
	"""Class to control the TCA9548A I2C multiplexor"""
	def __init__(self, address=0x70):
		self._address = address
		try:
			self._bus = smbus.SMBus(1) # Channel = 1
			if(self._bus.read_byte(self._address) == 0):
				print("Connected to TCA9548A")
		except:
			print("Failed to connect to TCA9548A")

		self._current_channel = 0

	def select_i2c_device(self, i2c_channel):
		"""Select the desired channel 0-7"""
		if i2c_channel < 0 or i2c_channel >7:
			print("TCA9548A channel out of range.  Cannot set to {}".format(i2c_channel))
			i2c_channel = self._current_channel
		else:
			self._channel = i2c_channel
		new_device = 0x01 << i2c_channel
		self._bus.write_byte(self._address, new_device)
