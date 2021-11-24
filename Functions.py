import psutil
import os
import subprocess
import time
import pygetwindow
import pyautogui
import win32gui

def checkIfProcessRunning(processName):
    # Iterate over the all the running processes
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def toggleFlux(boolean):
    os.startfile(r'C:\Users\dmagn\AppData\Local\FluxSoftware\Flux\flux.exe')
    time.sleep(1)
    flux = pygetwindow.getWindowsWithTitle('f.lux: Reduce eyestrain, day and night ')[0]
    if boolean:
        flux.minimize()
    else:
        flux.close()

def startExpressVPN():
    os.startfile(r'C:\Program Files (x86)\ExpressVPN\expressvpn-ui\ExpressVPN.exe')
    time.sleep(3)
    EVPN = pygetwindow.getWindowsWithTitle('ExpressVPN')[0]
    EVPN.close()
    # stays open in system tray

def closeExpressVPN():
    if checkIfProcessRunning('ExpressVPN.exe'):
        os.startfile(r'C:\Program Files (x86)\ExpressVPN\expressvpn-ui\ExpressVPN.exe')
        time.sleep(1)
        EVPN = pygetwindow.getWindowsWithTitle('ExpressVPN')[0]
        EVPN.restore()
        EVPN.move(0, 0)
        EVPN.activate()
        pyautogui.leftClick(40, 50)
        time.sleep(1)
        pyautogui.leftClick(40, 280)
        time.sleep(4)

def setPrimaryMonitor(monitor):
    if monitor == 'middle':
        # Set middle monitor as primary
        os.system(r'"C:\\Users\\dmagn\\My Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\nircmd.exe" setprimarydisplay 3')
    elif monitor == 'right':
        # Set middle monitor as primary
        os.system(r'"C:\\Users\\dmagn\\My Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\nircmd.exe" setprimarydisplay 1')

def setPrimaryAudio(device):
    if device == 'headphones':
        # Set Audio Device to Headphones
        p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'C:\\Users\\dmagn\\My Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\headphones.ps1'])
    if device == 'speakers':
        # Set Audio Device to Headphones
        p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'C:\\Users\\dmagn\\My Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\speakers.ps1'])

def adjustWindows(mode):
    for i in pygetwindow.getAllWindows():
        if mode == 'gaming':
            # minimize all windows except Discord and Steam
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

        elif mode == 'work':
            # close Discord close Steam
            if "Discord" in i.title:
                i.close()
            elif "Steam" in i.title:
                i.close()
            elif "Friends List" in i.title:
                i.close()
