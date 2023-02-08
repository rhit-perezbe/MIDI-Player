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
getoffsets = [28,18,16,17]
setoffsets = [13,12,15,14]
chip = gpiod.Chip(CHIP)
getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_FALLING_EDGE)
setlines = chip.get_lines(setoffsets)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

print("written")

while True:
    mumsic = os.listdir('./midis')
    soundfont = 'sf2files/hgss.sf2'
    size = len(mumsic)
    sound = mumsic[random.randint(0, size - 1)]
    whole_command = 'fluidsynth -a alsa -m alsa_seq -i ' + soundfont + ' midis/' + 'meteor.mid'  + '&'
    os.system(whole_command)
    
    processes = subprocess.check_output("ps", shell = True)
    procString = str(processes, 'utf-8')
    procName = procString.find('fluidsynth')
    pid = procString[(procName - 23):(procName - 19)]

    time.sleep(5)
    #os.system('kill ' + pid)
    time.sleep(2)
    
    nums = nums + 1
    if nums > 0:
        break
print("closing")
while True:
    ev_lines = getlines.event_wait(sec=1)
    vals = getlines.get_values()
    vals[2] = vals[2] ^ 1
    print(vals)
    setlines.set_values(vals)
    time.sleep(0.1)


