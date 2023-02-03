#! /usr/bin/env python3
import os
print("test")
soundfont = 'sf2files/8bitsf.SF2'
sound = 'midis/ruby.mid'
whole_command = 'fluidsynth -a alsa -m alsa_seq -i ' + soundfont + ' ' + sound
os.system(whole_command)
print("midi done")

