Problem: When I created these scripts, my setup involved 3 monitors, with the middle one being shared between my work laptop and my gaming PC. When switching between work, playing video games, or generally browsing during off-work hours, I would change several settings to optimize my gaming PC accordingly.

Solution: I decided to utilize Python, Powershell, and nircmd to automate the process at the (double)-click of a button on my Windows-based gaming PC.

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

I created python files for each mode that, when executed, update settings accordingly. I also created batch files on my desktop for each mode (use EXAMPLE.bat in RESOURCES folder as reference).
Then, simply by double-clicking the apporpriate batch file, my gaming PC is optimized for that mode.
