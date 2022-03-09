# Mon0-RT


![Mon0-RT-General](https://user-images.githubusercontent.com/84548743/157490948-b5834a79-bc28-418b-b55f-0cb500ab5207.PNG)

There are many like it, but this is my own.

This tool uses built in resources from Windows and also relies on some portable apps. Such as Ccleaner,PuTTy, and others. This can be used to do quick virus scans, check open ports, check shares, do tune-ups, and more. All with a convinient one click GUI built using PySimpleGUI

This can be placed on a USB drive and taken from client to client for easy to use diagnosis and repair. Portable apps are used in this and can be found in the Python Source file or at the bottom of this Read Me. They are not required but functionality will be limited.

</br></br></br>
<b>Bottom Tray</b>

Visable from all Tabs

IP Address - Gives the current local IP Address of the machine

User - Shows the currently logged in Username

PC Name - Shows the name of the PC the application is running on

IP Address to Ping - The default is Google and great to test for connectivity to the internet. This value can be changed to any IP address to validate connectivity.

Start Ping - This will open a new Command Propt and ping the address entered into the IP Address to Ping box.

</br></br></br>
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

</br></br></br>
<b>Hardware Tab</b>

![Mon0-RT-Hardware](https://user-images.githubusercontent.com/84548743/157502417-6af9f785-ec4f-4ddb-84aa-459d131e9cc5.PNG)

Device Manager - Brings up the Device Manager built into Windows

Disk Management - Starts Disk Management built into Windows

Defragment - Starts the Defragment tool built into Windows

Disk Cleanup - Starts the Disk Cleanup tool built into Windows

Memory Diagnostic - Starts the Memory Diagnostic tool built into Windows. This will require a restart of the device and it will start upon restart.

LCD Test - This opens a folder within the parent directory and you can click on the first picture and full screen. Then after letting your eyes adjust you can go through the images and look for any dead pixels.

Battery Health - This will run the Power Config built into Windows, generate a report, and auto open the report.

Wise Data Recovery - This will launch the Wise Data Recovery tool and attempt to recover any deleted files. Limited but works in most situations.

Microsoft Services - Launches Microsoft Services built into Windows. Great for stopping the Printer Spooler if there are issues or if there are issues with any of the other running services.

</br></br></br>
<b>OS Repair Tab</b>

![Mon0-RT-OS](https://user-images.githubusercontent.com/84548743/157503566-5d19d060-be3e-49b4-ac23-7d133ef23e2a.PNG)

Autoruns - This will launch Autoruns and external program used to check startup programs on Windows

Event Viewer - Launch Event Viewer built into Windows

DISM System File Checker - This will launch a new Command Prompt and run "DISM.exe /Online /Cleanup-image /Restorehealth" after that has completed it will launch another Command Prompt window and run "sfc /scannow" to ensure completetion 

Blue Screen View (Dev) - Still under development

Registry Editor - Launch the Windows Registry Editor

Windows Update Repair - Launch the Windows Update Repair built into Windows to help with any issues that might be occuring due to updates.

Disk Cleanup - Removed due to redundency

CCleaner - This will launch an external Ccleaner to clean up temp files. Great for tuneups and can sometimes free up lots of space.

</br></br></br>
<b>Software Tab</b>

![Mon0-RT-Software](https://user-images.githubusercontent.com/84548743/157505496-0da7c1af-7664-4eba-9584-b4db04beb36d.PNG)

Sleep & Wake Info - This will open the Power Configuration in Windows. Great for if you need to keep something awake during long processes

Don't Sleep - Runs a few commnads to make sure the device stays awake. Normal Power Settings will be reverted after restart.

Uninstall Programs - Launch the Uninstaller built into Windows

ADW Virus Scan - Uses an external program Malwarebyte's ADW scanner for a quick virus scan the of the machine.

</br></br></br>
<b>Networking Tab</b>

![Mon0-RT-Networking](https://user-images.githubusercontent.com/84548743/157506073-96e4e25c-47ad-4de9-9143-f45ab882d04c.PNG)

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

SSH/Telnet/Serial Console - Uses external PuTTy

Up/Down Speed Test - Lanuched the default browser and opens Fast.com for an download and upload speed test

View Open Shared Files - This will launch a new Command Prompt and show any shared files on the local network

Continuous Ping Test - Brings up a new Command Prompt and starts a 100 count ping test to the desired IP Address. IP Address is set by the 'IP Address to Ping' input. This will eventually be replaced with BeepPing for easier testing from afar if the device has audio out.

</br></br></br>
<b>External Portable Apps</b>

These should be downloaded and installed in the directory where the .exe is located

Wise Data Recovery - https://portableapps.com/apps/utilities/wise-data-recovery-portable</br>
Autorun - https://portableapps.com/apps/utilities/autoruns-portable</br>
Ccleaner - https://portableapps.com/apps/utilities/ccportable</br>
ADW Virus Scan - https://www.malwarebytes.com/adwcleaner - Just an .exe and can be placed in the same folder the Mon0-RT.exe is located</br>
TCP & UDP Query - https://portableapps.com/apps/utilities/tcpview-portable</br>
View Open Ports - https://portableapps.com/apps/utilities/portexpert-portable</br>
PuTTy - https://portableapps.com/apps/internet/putty_portable</br>
