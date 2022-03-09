# @author MonitorZero

import webbrowser
import PySimpleGUI as sg
import os
import pyautogui
import time
import socket

# Get the current IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Store the username for use throughout the program
USER = os.getlogin()

# Theme
sg.theme('Topanga')

generalLayout = [

[sg.Button('System Information',k='systemInformation',size=(30,4),font='Bold'),sg.Button('Resource Monitor',k='resourceMonitor',size=(30,4),font='Bold')],
[sg.Button('Control Panel',k='controlPanel',size=(30,4),font='Bold'), sg.Button('Task Manager',k='taskManager',size=(30,4),font='Bold')],
[sg.Button('PowerShell',k='powershell',size=(30,4),font='Bold'), sg.Button('Command Prompt (Admin)',k='cmd',size=(30,4),font='Bold')],
[sg.Button('Printers and Scanners',k='printers',size=(30,4),font='Bold'), sg.Button('Network & Sharing Center',k='network',size=(30,4),font='Bold')],
[sg.Button('Reboot - Safe Mode',k='rebootsafemode',size=(30,4),expand_x=True,font='Bold')],

]

hardwareLayout = [

[sg.Button('Device Manager',k='deviceManager',size=(30,4),font='Bold'), sg.Button('Disk Management',k='diskManagement',size=(30,4),font='Bold')],
[sg.Button('Defragment',k='defragment',size=(30,4),font='Bold'), sg.Button('Disk Cleanup',k='diskCleanup',size=(30,4),font='Bold')],
[sg.Button('Memory Diagnostic\n(Requires Restart)',k='memoryDiagnostic',size=(30,4),font='Bold'),sg.Button('LCD Test',k='lcdTest',size=(30,4),font='Bold') ],
[sg.Button('Battery Health',k='batteryHealth',size=(30,4),font='Bold'), sg.Button('Wise Data Recovery',k='dataRecovery',size=(30,4),font='Bold')],
[sg.Button('Microsoft Services',k='microsoftServices',size=(30,4),font='Bold')],

]

osrepairLayout = [

[sg.Button('Autoruns',k='autoRun',size=(30,4),font='Bold'), sg.Button('Event Viewer',k='eventViewer',size=(30,4),font='Bold')],
[sg.Button('DISM System File Checker',k='systemFileChecker',size=(30,4),font='Bold'), sg.Button('Blue Screen View (Dev)',k='bluescreenview',size=(30,4),font='Bold')],
[sg.Button('Registry Editor',k='registryEditor',size=(30,4),font='Bold'), sg.Button('Windows Update Repair',k='windowsUpdateRepair',size=(30,4),font='Bold')],
[sg.Button('CCleaner (Test Me)',k='ccleaner',size=(30,4),font='Bold')],

]

softwareLayout = [

[sg.Button('Sleep & Wake Info',k='sleepWakeInfo',size=(30,4),font='Bold'), sg.Button("Don't Sleep",k='donotsleep',size=(30,4),font='Bold')],
[sg.Button('Uninstall Programs',k='uninstallPrograms',size=(30,4),font='Bold'),sg.Button('ADW Virus Scan',k='stinger',size=(30,4),font='Bold')],


]

networkingLayout = [

[sg.Button('Reset TCP/IP & Windsock',k='resetTCPIP',size=(30,4),font='Bold'), sg.Button('Windows Firewall',k='firewall',size=(30,4),font='Bold')],
[sg.Button('TCP & UDP Port Query',k='portQuery',size=(30,4),font='Bold'),sg.Button('View Open Ports',k='viewOpenPorts',size=(30,4),font='Bold') ],
[sg.Button('Nmap (Dev)',k='nmap',size=(30,4),font='Bold'), sg.Button('SSH/Telnet/Serial Console',k='putty',size=(30,4),font='Bold')],
[sg.Button('Up/Down Speed Test (Fast.com)',k='lanSpeedTest',size=(30,4),font='Bold'), sg.Button('View Open Shared Files',k='viewOpenSharedFiles',size=(30,4),font='Bold')],
[sg.Button('Continuous Ping Test',k='continuousPingTest',size=(30,4),font='Bold') ],

]

tabgrp = [[

sg.TabGroup([[
sg.Tab('General',layout=generalLayout,element_justification='center'),
sg.Tab('Hardware',layout=hardwareLayout,element_justification='center'),
sg.Tab('OS Repair',layout=osrepairLayout,element_justification='center'),
sg.Tab('Software',layout=softwareLayout,element_justification='center'),
sg.Tab('Networking',layout=networkingLayout,element_justification='center')]],
tab_location='topleft'),

]]

infoColumn = [

[sg.Text(f'IP Address: {local_ip}',font='Bold',size=(30,1)),sg.Text('IP Address to Ping ',font='Bold'),sg.InputText(size=(15,1),key='ipAddress',default_text='8.8.8.8')],
[sg.Text(f'Username:   {USER}',font='Bold',size=(35,1)),sg.Button('Start Ping',font='Bold',size=(20,1),k='startPing')],
[sg.Text(f'PC Name:    {hostname}',font='Bold',size=(30,1))],

]

layout = [
        [sg.Column(tabgrp,)],
        [sg.Column(infoColumn)],
]

window = sg.Window('Mon0 Repair Tool',layout,icon='download.ico')

# Event code
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Exit' or event == 'Exit0':
        break

    # General Tab
    if event == 'systemInformation':
        os.system('control system')
    if event == 'resourceMonitor':
        os.system('resmon')
    if event == 'controlPanel':
        os.system('control')
    if event == 'taskManager':
        os.system('taskmgr')
    if event == 'powershell':
        os.system('start powershell')
    if event == 'cmd':
        pyautogui.hotkey('win','r')
        time.sleep(5)
        pyautogui.typewrite('cmd')
        pyautogui.hotkey('ctrl','shift','enter')
    if event == 'printers':
        os.system('Start ms-settings:printers')
    if event == 'network':
        os.system('control.exe /name Microsoft.NetworkandSharingCenter')
    if event == 'rebootsafemode':
        # Creat a popup windo from the sg library
        sg.popup_yes_no('Are you sure you want to reboot into safe mode?',title='Reboot to Safe Mode')
        # Get the response
        button, values = sg.Window('Reboot to Safe Mode').read()
        if button == 'Yes':
            os.system('bcdedit /set {current} safeboot')
            os.system('shutdown /r')
        else:
            pass

    # Hardware Tab
    if event == 'deviceManager':
        os.system('start devmgmt.msc')
    if event == 'diskManagement':
        os.system('start diskmgmt.msc')
    if event == 'defragment':
        os.system('start dfrgui')
    if event == 'diskCleanup':
        os.system('start cleanmgr /tuneup:1')
    if event == 'memoryDiagnostic':
        os.system('mdsched')
    if event == 'lcdTest':
        # This works but it's not as nice as I'd like it to be..
        os.startfile('lcdtest')
    if event == 'batteryHealth':
        os.system("powercfg /BATTERYREPORT")
        os.startfile(f"C:\\Users\\{USER}\\battery-report.html")
    if event == 'dataRecovery':
        # https://portableapps.com/apps/utilities/wise-data-recovery-portable
        os.startfile('Z:\WiseDataRecoveryPortable\WiseDataRecoveryPortable.exe')
    if event == 'microsoftServices':
        os.system('start services.msc')

    # OS Repair Tab
    if event == 'autoRun':
        # https://portableapps.com/apps/utilities/autoruns-portable
        os.startfile('Z:\AutorunsPortable\AutorunsPortable.exe')
    if event == 'eventViewer':
        os.system('eventvwr')
    if event == 'systemFileChecker':
        os.system('start cmd "DISM.exe /Online /Cleanup-image /Restorehealth"')
        os.system('start cmd "sfc /scannow"')
        # Create popup for completion of scan
        sg.popup('Scan Complete!',title='System File Checker')
    #if event == 'bluescreenview':
        # Still under development
        # http://www.nirsoft.net/utils/blue_screen_view.html
    if event == 'registryEditor':
        os.system('start regedit')
    if event == 'windowsUpdateRepair':
        os.system('start msdt.exe /id WindowsUpdateDiagnostic')
    if event == 'ccleaner':
        # https://portableapps.com/apps/utilities/ccportable
        # Changed this to a relative path as the USB drive letter does not stay persistent - NOT TESTED
        os.startfile('ccPortable\ccPortable.exe')
        continue
    # Software Tab
    if event == 'sleepWakeInfo':
        os.system('powercfg.cpl')
    if event == 'donotsleep':
        os.system('powercfg /change monitor-timeout-ac 0')
        os.system('powercfg /change monitor-timeout-dc 0')
        os.system('powercfg /change standby-timeout-ac 0')
        os.system('powercfg /change standby-timeout-dc 0')
    if event == 'uninstallPrograms':
        os.system('appwiz.cpl')
    if event == 'stinger':
        # https://portableapps.com/apps/security/mcafee-stinger-portable
        # Also possible Malwarebytes ADWCleaner https://www.malwarebytes.com/adwcleaner
        os.startfile('Z:\\adwcleaner.exe')
        continue

    # Networking Tab
    if event == 'resetTCPIP':
        os.system('netsh winsock reset')
        os.system('netsh int ip reset')
        os.system('ipconfig /release')
        os.system('ipconfig /renew')
        os.system('ipconfig /flushdns')
    if event == 'firewall':
        os.system('start wf.msc')
    if event == 'portquery':
        # https://portableapps.com/apps/utilities/tcpview-portable
        os.startfile('Z:\TcpViewPortable\TcpViewPortable.exe')
        continue
    if event == 'viewOpenPorts':
        # https://portableapps.com/apps/utilities/portexpert-portable
        os.startfile('Z:\PortExpertPortable\PortExpertPortable.exe')
        continue
    if event == 'putty':
        # https://portableapps.com/apps/internet/putty_portable
        os.startfile('Z:\PuttyPortable\PuttyPortable.exe')
        continue
    if event == 'lanSpeedTest':
        webbrowser.open('https://www.fast.com/')
        continue
    if event == 'viewSharedFiles':
        os.system('cmd /k "net share"')
        os.system('control.exe /name Microsoft.NetworkandSharingCenter')
    if event == 'continuousPingTest':
        # get the IP address from the ipAddress key
        ipAddress = values['ipAddress']
        os.system(f'start cmd /k "ping -n 100 {ipAddress}')
    if event == 'nmap':
        # https://nmap.org/
        continue

    # Bottom Tray
    if event == 'startPing':
        ipAddress = values['ipAddress']
        os.system(f'start cmd /k "ping {ipAddress}"')