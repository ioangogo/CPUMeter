#!/usr/bin/env python
from linux_metrics import cpu_stat
import serial,gc
import time
lastnum=1
portarray=[]
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(lastnum, p)
    portarray.append(p)
    lastnum =+ 1
ttypath = input("Enter Aurdino tty path from above, ignore the /dev/: ")
port = serial.Serial('/dev/'+ttypath, 9600)
import signal
import sys
def signal_handler(signal, frame):
        x=lastnum
        while x>=0:
           port.write([x])
           time.sleep(0.001)
           x = x - 1
        port.write([0])
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
while True:
    idle = cpu_stat.cpu_percents()['idle']
    val = round(idle)/100
    printval = int(val * 100 - 1)
    val = 255 * (1-val)
    val = int(val)
    print("Actual value: "+ str(printval) + '% Data To Arduino: '+ str(val))
    lastnum=val
    port.write(bytes([val]))

    time.sleep(0.25)
    gc.collect()
