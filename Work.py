from __future__ import print_function
import os.path
import subprocess
import time
import pygetwindow as gw
from ahk import AHK


ahk = AHK()

# Set right monitor as primary
os.system(r'"C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\nircmd.exe" setprimarydisplay 1')

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

# close Discord, close Steam
for i in gw.getAllWindows():
    if "Discord" in i.title:
        i.close()
    elif "Steam" in i.title:
        i.close()
    elif "Friends List" in i.title:
        i.close()

