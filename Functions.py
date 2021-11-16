import psutil
import os
import subprocess

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

def setPrimaryMonitor(monitor):
    if monitor == 'middle':
        # Set middle monitor as primary
        os.system(r'"C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\nircmd.exe" setprimarydisplay 3')
    elif monitor == 'right':
        # Set middle monitor as primary
        os.system(r'"C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\nircmd.exe" setprimarydisplay 1')

def setPrimaryAudio(device):
    if device == 'headphones':
        # Set Audio Device to Headphones
        p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\headphones.ps1'])
    if device == 'speakers':
        # Set Audio Device to Headphones
        p = subprocess.Popen(["powershell.exe", '-ExecutionPolicy', 'Unrestricted', '-File', r'C:\\Users\\dmagn\\Google Drive\\Projects\\Coding\\Python\\Windows Config\\Resources\\speakers.ps1'])