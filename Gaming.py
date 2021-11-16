from __future__ import print_function
import time
import os.path
import subprocess
import pygetwindow as gw
import psutil
from ahk import AHK
import socket
from Functions import checkifprocessrunning, setPrimaryMonitor, setPrimaryAudio

setPrimaryMonitor('middle')
setPrimaryAudio('headphones')

ahk = AHK()


# Close Express VPN and Flux
# check if running

# Close Express VPN
if checkifprocessrunning('ExpressVPN.exe'):
    os.startfile(r'C:\Program Files (x86)\ExpressVPN\expressvpn-ui\ExpressVPN.exe')
    time.sleep(1)
    EVPN = ahk.win_get(title='ExpressVPN')
    EVPN.restore()
    EVPN.move(0, 0)
    EVPN.activate()
    ahk.mouse_move(40, 50)
    ahk.click()
    time.sleep(1)
    ahk.mouse_move(40, 280)
    ahk.click()

# Close Flux
if checkifprocessrunning('flux.exe'):
    os.startfile(r'C:\Users\dmagn\AppData\Local\FluxSoftware\Flux\flux.exe')
    time.sleep(1)
    flux = gw.getWindowsWithTitle('f.lux: Reduce eyestrain, day and night ')[0]
    flux.close()
##


# minimize all windows except Discord and Steam
for i in gw.getAllWindows():
    if i.title == "":
        continue
    elif i.title == "Backup and Sync":
        continue
    elif "Discord" in i.title:
        i.maximize()
    elif "Steam" in i.title:
        i.maximize()
    else:
        i.minimize()

