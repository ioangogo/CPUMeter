#!/usr/bin/env python
from linux_metrics import cpu_stat
import serial
import time

port = serial.Serial('/dev/ttyACM0', 9600)
import signal
import sys
def signal_handler(signal, frame):
        port.write([0])
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
while True:
    idle = cpu_stat.cpu_percents()
    idle = idle['idle']/100
    val = 255 * (1-idle)
    val = int(str(val).split('.')[0])
    print(val)
    port.write(bytes([val]))

    time.sleep(0.25)
