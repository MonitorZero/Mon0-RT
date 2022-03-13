# MonitorZero's Repair Tool

![general](https://user-images.githubusercontent.com/84548743/157774250-51ac1554-93b9-477a-96cb-aac04ce3d1af.PNG)

There are many like it, but this is my own.

There is no warrenty with this and I am not responsible for any damage done to your computer or anyone else's. Use at your own risk.

<b>! IMPORTANT !</b> Make sure to unzip the Tools.zip where the EXE is located to have access to the external tools

As with most PC Diagnostic Tools it's best to run this as Admin when able to get the full functionality and intended use of the tool.

This tool uses built in resources from Windows and also relies on some portable apps. Such as Ccleaner,PuTTy, and others. This can be used to do quick virus scans, check open ports, check shares, do tune-ups, and more. All with a convinient one click GUI built using PySimpleGUI

I have many family members and friends come to me for help on thier computer for one reason or another. I built this to simply streamline the process of the usual things I do and to help with commands that I often forget if I haven't used them in a long time.

The whole thing can be placed on a USB as I usually have it on me but decided to put on here because sometimes I just leave things at home and wanted access to it.

</br></br>
<b>Bottom Tray</b>

Visable from all Tabs

IP Address - Gives the current local IP Address of the machine

User - Shows the currently logged in Username

PC Name - Shows the name of the PC the application is running on

IP Address to Ping - The default is Google and great to test for connectivity to the internet. This value can be changed to any IP address to validate connectivity.

Start Ping - This will open a new Command Propt and ping the address entered into the IP Address to Ping box.

</br></br>
<b>General Tab</b>

System Information - Brings up the default system info built into Windows

Resouce Monitor - Brings up the default Resource Monitor Built into Windows

Control Panel - Brings up the Control Panel built into Windows

Task Manager - Brings up the Task Manager built into Windows

PowerShell - Brings up a PowerShell terminal

Command Prompt (Admin) - Brings up an elevated Command Prompt running as Admin

Printers and Scanners - Brings up the Printers and Scanners windows built into Windows

Network and Sharing Center - Brings up the Network and Sharing Center built into Windows. Great for WiFi password, if connected, and setting up shares

Reboot - Safe Mode - This will give you a prompt asking if you want to restart the computer and boot into safe mode

</br></br>
<b>Hardware Tab</b>

![hardware](https://user-images.githubusercontent.com/84548743/157774359-64b7fcc2-fa6b-4bb9-b4ea-5f9ec9f63dd2.PNG)

Device Manager - Brings up the Device Manager built into Windows

Disk Management - Starts Disk Management built into Windows

Defragment - Starts the Defragment tool built into Windows

Disk Cleanup - Starts the Disk Cleanup tool built into Windows

Memory Diagnostic - Starts the Memory Diagnostic tool built into Windows. This will require a restart of the device and it will start upon restart.

LCD Test - This opens a folder within the parent directory and you can click on the first picture and full screen. Then after letting your eyes adjust you can go through the images and look for any dead pixels.

Battery Health - This will run the Power Config built into Windows, generate a report, and auto open the report.

Wise Data Recovery - This will launch the Wise Data Recovery tool and attempt to recover any deleted files. Limited but works in most situations.

Microsoft Services - Launches Microsoft Services built into Windows. Great for stopping the Printer Spooler if there are issues or if there are issues with any of the other running services.

Disk Health - Launches Crystal Disk Info for HDD & SSD Health

</br></br>
<b>OS Repair Tab</b>

![OS](https://user-images.githubusercontent.com/84548743/157774370-78f5f9b1-36b8-4930-82ef-8e42b3deee00.PNG)

Autoruns - This will launch Autoruns and external program used to check startup programs on Windows

Event Viewer - Launch Event Viewer built into Windows

DISM System File Checker - This will launch a new Command Prompt and have a pop up for the DISM and SFC. ( This is not the best way of doing it but it's still under dev until I can find a good way to launch it but it works for me.

Blue Screen View (Dev) - Still under development

Registry Editor - Launch the Windows Registry Editor

Wise Registry Cleaner - Launch Wise Registry Cleaner and this will look for blank entries and do a low level cleanup of the registry

Windows Update Repair - Launch the Windows Update Repair built into Windows to help with any issues that might be occuring due to updates.

CCleaner - Launch Ccleaner to clean up temp files. Great for tuneups and can sometimes free up lots of space.

</br></br>
<b>Software Tab</b>

![software](https://user-images.githubusercontent.com/84548743/157774452-3182ffbd-fad7-4e48-a2bf-3d06e843153c.PNG)

Sleep & Wake Info - This will open the Power Configuration in Windows. Great for if you need to keep something awake during long processes

Don't Sleep - Runs a few commnads to make sure the device stays awake. Normal Power Settings will be reverted after restart.

Uninstall Programs - Launch the Uninstaller built into Windows

ADW Virus Scan - Launch Malwarebyte's ADW scanner for a quick virus scan the of the machine.

</br></br>
<b>Networking Tab</b>

![networking](https://user-images.githubusercontent.com/84548743/157774483-eb6138e6-ec21-4a16-9baa-495a5184a9c4.PNG)

Reset TCP/IP and Windsock - This is always a long few commands I always forget. This will autorun the commands.

'netsh winsock reset'
'netsh int ip reset'
'ipconfig /release'
'ipconfig /renew'
'ipconfig /flushdns'

Windows Firewall - Bring up the Windows Firewall built into Windows

TCP & UDP Port Query - Uses external TCP View to test and show all open TCP and UDP ports

View Open Ports - Uses external Port Expert to show all open ports and what processes they're tied to. Good for virus diagnosis

Nmap (Dev) - Still under development but I would like to have the option to run ZenMap from the USB drive but haven't figured out how to accomplish that just yet.

SSH/Telnet/Serial Console - Launch PuTTY

Up/Down Speed Test - Lanuched the default browser and opens Fast.com for an download and upload speed test

View Open Shared Files - This will launch a new Command Prompt and show any shared files on the local network

Continuous Ping Test - Brings up a new Command Prompt and starts a 100 count ping test to the desired IP Address. IP Address is set by the 'IP Address to Ping' input. This will eventually be replaced with BeepPing for easier testing from afar if the device has audio out.

</br></br>
<b>EZ Tune</b>

![eztune](https://user-images.githubusercontent.com/84548743/157774612-947089ff-7e88-415e-996d-2a56dd3829cf.PNG)

This has options from other tabs but it's my usual go to's for "My computer is slow/not working right"

It may not fix everything but is a good base line to do and relatively easy to perform.
