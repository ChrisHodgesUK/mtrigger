#mtrigger.py
#A minimal trigger for DSLR and other cameras with electronic cable releases
#See accompanying mtdemo.py for an example of use, and mtrigger.pdf for the necessary hardware.
#Written in 2015 by Chris Hodges, code@c-hodges.co.uk
#To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
#You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 

import serial as ser
from time import sleep

class mtrigger:
	"""A minimal trigger for DSLR and other cameras with electronic shutter releases"""
	def __init__(self, port):
		"""Opens a port for use as a trigger.  serial.tools.list_ports may be of interest""" 
		self.S=ser.Serial(port)
		self.S.setRTS(False)
		self.S.setDTR(False)
		return None

	def focus(self, t=-1.0):
		"""Attempts to focus (half-press) for the time (float seconds) specified
		If no time is specified or t<0 , acts like holding down the half-press.
		Use focus(0) to release in this case
		"""
		self.S.setDTR(True)
		if t>=0:
			sleep(t)
			self.S.setDTR(False)

	def shoot(self, t=-1.0):
		"""Attempts to shoot (full-press) for the time (float seconds) specified
		If no time is specified or t<0 , acts like holding down the trigger.
		Use shoot(0) to release in this case.
		shoot(0) on it's own may not fire the trigger.
		shoot(0.1) is recommended as equivalent to tapping the trigger.
		Should work in bulb mode but test it - the precision may not be good.
		"""
		self.S.setRTS(True)
		if t>=0:
			sleep(t)
			self.S.setRTS(False)
