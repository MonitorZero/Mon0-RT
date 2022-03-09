# Mon0-RT
<strong>MonitorZero's Repair Tool</strong>

![Mon0-RT-General](https://user-images.githubusercontent.com/84548743/157490948-b5834a79-bc28-418b-b55f-0cb500ab5207.PNG)

There are many tools like it but this is my own.

This tool uses built in resources from Windows and also relies on some portable apps. Such as Ccleaner,PuTTy, and others. This can be used to do quick virus scans, check open ports, check shares, do tune-ups, and more. All with a convinient one click GUI built using PySimpleGUI


<b>Bottom Tray</b>

IP Address - Gives the current local IP Address of the machine

User - Shows the currently logged in Username

PC Name - Shows the name of the PC the application is running on

IP Address to Ping - The default is Google and great to test for connectivity to the internet. This value can be changed to any IP address to validate connectivity.

Start Ping - This will open a new Command Propt and ping the address entered into the IP Address to Ping box.


<b>The General Tab</b>

System Information - Brings up the default system info built into Windows

Resouce Monitor - Brings up the default Resource Monitor Built into Windows

Control Panel - Brings up the Control Panel built into Windows

Task Manager - Brings up the Task Manager built into Windows

PowerShell - Brings up a PowerShell terminal

Command Prompt (Admin) - Brings up an elevated Command Prompt running as Admin

Printers and Scanners - Brings up the Printers and Scanners windows built into Windows

Network and Sharing Center - Brings up the Network and Sharing Center built into Windows. Great for WiFi password, if connected, and setting up shares

Reboot - Safe Mode - This will give you a prompt asking if you want to restart the computer and boot into safe mode


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
