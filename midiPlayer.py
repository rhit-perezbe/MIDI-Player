#! /usr/bin/env python3
import os
import random
import subprocess
import time
import gpiod
import sys
nums = 0

os.system('./setup.sh')

CONSUMER = 'getset'
CHIP = '1'
getoffsets = [28,18,16,17] #P9_12 P9_14 P9_15 P9_23
setoffsets = [13,12,15,14] #P8_11 P8_12 P8_15 P8_16
chip = gpiod.Chip(CHIP)
getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_RISING_EDGE)
setlines = chip.get_lines(setoffsets)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

setlines.set_values([0,0,0,0])

playing = False
shuffle = False
midi = True
insettings = False
settingstate = 0
currentMidi = ""
songIndex = 0
size = 0
def playmumsic():
    global playing
    global songIndex
    global size
    mumsic = os.listdir('./midis')
    soundfont = 'sf2files/n64.sf2'
    size = len(mumsic)
    if shuffle == True:
        currentMidi = mumsic[random.randint(0, size - 1)]
    else:
        currentMidi = mumsic[songIndex]
    whole_command = 'fluidsynth -a alsa -m alsa_seq -i ' + soundfont + ' midis/' + currentMidi  + '&'
    os.system(whole_command)
    playing = True

def stopmumsic():
    global playing
    #processes = subprocess.check_output("ps", shell = True)
    #procString = str(processes, 'utf-8')
    #procName = procString.find('fluidsynth')
    #pid = procString[(procName - 23):(procName - 19)]
    #print(procName)
    os.system('kill $(pidof fluidsynth)')
    time.sleep(2)
    playing = False

while True:
    songIndex
    ev_lines = getlines.event_wait(sec=1)
    vals = getlines.get_values()
    
    #setlines.set_values(vals)
    time.sleep(0.1)

    processes = subprocess.check_output("ps", shell = True)
    procString = str(processes, 'utf-8')
    procName = procString.find('fluidsynth')
    if insettings == True:
        dispArr = [1,0,0,1]
        if midi == True:
            dispArr[2] = 1
        if shuffle == True:
            dispArr[1] = 1
        if vals[0] == 0:
            print("sound")
        if vals[1] == 0:
            print("shuffle/seq")
            shuffle = not shuffle
        if vals[2] == 0:
            print("Midi/Wav")
            midi = not midi
        if vals[3] == 0:
            print("exit")
            insettings = False
        setlines.set_values(dispArr)
        continue


    if(procName == -1):
        playing = False
        setlines.set_values([1,0,1,1])
    if(vals[1] == 0 and playing == True):
        stopmumsic();
        setlines.set_values([1,0,1,1])
    if(vals[0] == 0 and playing == False):
        setlines.set_values([0,1,1,0])
        playmumsic();
    if(vals[2] == 0):
        songIndex = songIndex + 1
        songIndex = songIndex % size
        if(playing == True):
            stopmumsic();
            playmumsic();
    if(vals[3] == 0 and playing == False):
        print("entering menu")
        insettings = True
        settingstate = 0
        time.sleep(0.5)

            


