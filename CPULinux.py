#!/usr/bin/env python
from linux_metrics import cpu_stat
import serial
import gc
import time
import os
import signal
import sys
import serial.tools.list_ports


lastnum = 1
oldnumc = 1
lastnumarr = 1
portarray = []
ports = list(serial.tools.list_ports.comports())

for p in ports:
    print(lastnum, ":", p)
    str(p).split(" ")
    portarray.append(p[0])
    lastnumarray =+ 1

ttypath = input("Select Serial device: ")
port = serial.Serial(portarray[int(ttypath)-1], 9600)

def signal_handler(signal, frame):
    x = lastnum
    while x >= 0:
        port.write([x])
        time.sleep(0.001)
        x = x - 1
    port.write([0])
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

while True:
    val = 255 * round(100 - cpu_stat.cpu_percents()['idle']) / 100
    os.system("clear")
    print(str(round((val / 255) * 100)), "%")

    if val != lastnum:
        port.write(bytes([int(round(val))]))
        lastnum = val
        oldnumc = 1
    else:
        print("Old Number", oldnumc)
        oldnumc += 1

    time.sleep(0.25)
    gc.collect()
