from __future__ import print_function
import time
import os.path
import subprocess
import pygetwindow as gw
import psutil
from ahk import AHK
import socket

# get computer name
computer = socket.gethostname()

# computer-specific file paths
if computer == "Big-Bertha":
    # Set middle monitor as primary
    os.system(r'"C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\nircmd.exe" setprimarydisplay 1')

    # Set Audio Device to Headphones
    p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\headphones.ps1'])
elif computer == "Black-Betty":

    # Set Audio Device to Headphones
    p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'D:\\Google Drive\\Projects\\Coding\\headphones.ps1'])

ahk = AHK()


# Close Express VPN and Flux
# check if running


def checkifprocessrunning(processname):
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processname.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


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

