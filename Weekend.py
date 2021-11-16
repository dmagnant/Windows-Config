from __future__ import print_function
import time
import os.path
import subprocess
import pygetwindow as gw
import psutil
from ahk import AHK

ahk = AHK()

# Set Audio Device to Speakers
p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'D:\\Google Drive\\Projects\\Coding\\speakers.ps1'])

# Start ExpressVPN
os.startfile(r'C:\Program Files (x86)\ExpressVPN\expressvpn-ui\ExpressVPN.exe')
time.sleep(3)
EVPN = ahk.win_get(title='ExpressVPN')
EVPN.close()
# Start Flux
os.startfile(r'C:\Users\dmagn\AppData\Local\FluxSoftware\Flux\flux.exe')
time.sleep(1)
flux = ahk.win_get(title='f.lux: Reduce eyestrain, day and night')
flux.minimize()

# Set middle monitor as primary
os.system(r'"D:\\Google Drive\\Projects\\Coding\\nircmd.exe" setprimarydisplay 1')