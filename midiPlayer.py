#! /usr/bin/env python3
import os
import random
import subprocess
import time
nums = 0
while True:
    #print(os.listdir('./midis'))
    mumsic = os.listdir('./midis')
    soundfont = 'sf2files/8bitsf.SF2'
    size = len(mumsic)
    sound = mumsic[random.randint(0, size - 1)]
    whole_command = 'fluidsynth -a alsa -m alsa_seq -i ' + soundfont + ' midis/' + 'crab.mid'  + '&'
    #print(sound)
    os.system(whole_command)
    processes = subprocess.check_output("ps", shell = True)
    print(processes)
    print(type(processes))
    procString = str(processes, 'utf-8')
    procName = procString.find('fluidsynth')
    print(procString[(procName - 23):(procName - 19)])
    time.sleep(5)
    #os.system('kill ' + procString[(procName - 23):(procName -19)])
    print("midi done")
    time.sleep(2)
    nums = nums + 1
    if nums > 0:
        break

