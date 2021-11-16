Requirements: Windows OS, Python, ExpressVPN, F.lux, AHK

Problem: When I created these scripts, my setup involved 3 monitors, with the middle one being shared between my work laptop and my gaming PC. When switching between work, playing video games, or just generally browsing while not during work hours, I would change several settings to optimize the PC accordingly.

Solution: I decided to utilize Python, Powershell, and AHK to automate the process at the (double)-click of a button. 

Three "modes" are available:

Gaming, 
Work, 
Weekend

The following items are changed based on the modes above:

Primary monitor, 
Primary audio device, 
VPN and Screen Warmer applications (open/close), 
Gaming-related applications (minimize/maximize)

How-to-use:

Using the EXAMPLE.bat file as reference, I created python files for each mode that update settings accordingly. I also created batch files on my desktop for each mode. Simply by double-clicking the apporpriate batch file, I can optimize my PC for that mode.
