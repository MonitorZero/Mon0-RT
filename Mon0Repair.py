# @author MonitorZero

from xml.dom.minidom import Element
import PySimpleGUI as sg
import os
import sys
import time
import pyautogui
import win32com.client as shell
import time

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
[sg.Button('Memory Diagnostic',k='memoryDiagnostic',size=(30,4),font='Bold'),sg.Button('LCD Test',k='lcdTest',size=(30,4),font='Bold') ],
[sg.Button('Battery Health',k='batteryHealth',size=(30,4),font='Bold')]

]

osrepairLayout = [

[sg.Button('Autoruns',k='autoRun',size=(30,4),font='Bold')]

]

tabgrp = [[sg.TabGroup([[
           sg.Tab('General',layout=generalLayout,element_justification='center'),
           sg.Tab('Hardware',layout=hardwareLayout,element_justification='center'),
           sg.Tab('OS Repair',layout=osrepairLayout,element_justification='center')]],
           tab_location='top-left')]]


window = sg.Window('Mon0 Repair Tool',tabgrp)

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
        os.system('powershell')
    if event == 'cmd':
        pyautogui.hotkey('win','r')
        time.sleep(5)
        pyautogui.typewrite('cmd')
        pyautogui.hotkey('ctrl','shift','enter')
    if event == 'printers':
        os.system('control printers')
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
        os.system('devmgmt.msc')
    if event == 'diskManagement':
        os.system('diskmgmt.msc')
    if event == 'defragment':
        os.system('defrag')
    if event == 'diskCleanup':
        os.system('cleanmgr /tuneup:1')
    if event == 'memoryDiagnostic':
        os.system('mdsched')
    if event == 'lcdTest':
        # This works but it's not as nice as I'd like it to be..
        os.startfile('lcdtest')
    if event == 'batteryHealth':
        os.system('powercfg /batteryreport')
        os.startfile('C:\\Windows\\System32\\battery-report')
    