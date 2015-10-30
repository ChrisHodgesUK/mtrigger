#mtdemo.py
#demo code for mtrigger.py
#Written in 2015 by Chris Hodges, code@c-hodges.co.uk
#To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
#You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 

from time import sleep
import mtrigger

#The following code runs a timelapse at 1 second intervals until aborted.
#On Linux, ls /dev/tty/ will return a list of serial ports, look for entries 
#starting ttyusb or ttyacm for USB serial ports
#On Windows, use control panel.
#python serial.tools.list_ports may also be useful.
#It doesn't try to prefocus, and because of the short press of the trigger
#May not take every time in AF mode (it's quite unlikely to take the first time)
T=mtrigger.mtrigger('COM3')
while True:
	sleep(1)
	T.shoot(.1)
	
	