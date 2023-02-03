#! /usr/bin/env python3
import os
import random
while True:
    print(os.listdir('./midis'))
    mumsic = os.listdir('./midis')
    soundfont = 'sf2files/Sonic_And_Knuckles_-Updated-.sf2'
    size = len(mumsic)
    sound = mumsic[random.randint(0, size - 1)]
    whole_command = 'fluidsynth -a alsa -m alsa_seq -i ' + soundfont + ' midis/' + 'ruby4.mid'
    print(sound)
    os.system(whole_command)
    print("midi done")
    break

