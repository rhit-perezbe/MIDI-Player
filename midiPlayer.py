#! /usr/bin/env python3
import os
import random
import subprocess
import time
import gpiod
import sys
import pygame
import math
import getpass
if getpass.getuser() != 'root':
    sys.exit("Must be run as root you silly little goober")
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
soundfont = "sf2files/n64.sf2"
songIndex = 0
size = 0
sfIndex = 0
sfSize = 0

class pymenu :
    screen = None;
    imagename = "start.jpg"
    title = "tezt"

    def __init__(self):
        os.putenv('SDL_NOMOUSE', '1')
        pygame.display.init()
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print("Framebuffer size: ", size[0], "x", size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))   
        # Turn off cursor
        pygame.mouse.set_visible(False)
        # Initialise font support
        pygame.font.init()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
    def updatePicture(self, pictureName):
        self.imagename = pictureName
    def updateTitle(self, title):
        self.title = title

    def drawMenu(self):
        xmax = pygame.display.Info().current_w
        ymax = pygame.display.Info().current_h
        
        print("xmay, ymax: ", xmax, "x", ymax)
        
        # Set center of clock
        
        # https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
        myfont = pygame.font.SysFont('Impact', 18)

        xcent = int(xmax/2)
        ycent = int(ymax/2)
        print("xcent, ycent: ", xcent, "x", ycent)
        
        # minScale = 0.85     # Size of minute hand relative to second
        # hourScale = 0.5
        # width = 2           # Width of hands
        
        # rad = 100   # Radius
        # len = 15    # Length of ticks
        
        backgroundC = (173,216,230)
        faceC = (0, 0, 255)

        self.screen.fill(backgroundC)

        
        
        green = (0, 255, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)
        orange = (255, 162, 0)
        black = (0, 0, 0)

        black_box_0 = image = pygame.Rect(18, 18, 204, 204)
        pygame.draw.rect(self.screen, black, black_box_0)

        #placeholder rectangle for song image

        image = pygame.image.load(os.path.join('./images/' + self.imagename))
        self.screen.blit(image, (20, 20))




        black_box_1 = pygame.Rect(230, 60, 30, 20)
        black_box_2 = pygame.Rect(230, 95, 30, 20)
        black_box_3 = pygame.Rect(230, 130, 30, 20)
        black_box_4 = pygame.Rect(230, 165, 30, 20)

        green_box = pygame.Rect(231, 61, 28, 18)
        red_box = pygame.Rect(231, 96, 28, 18)
        orange_box = pygame.Rect(231, 131, 28, 18)
        white_box = pygame.Rect(231, 166, 28, 18)

        pygame.draw.rect(self.screen, black, black_box_1)
        pygame.draw.rect(self.screen, black, black_box_2)
        pygame.draw.rect(self.screen, black, black_box_3)
        pygame.draw.rect(self.screen, black, black_box_4)

        pygame.draw.rect(self.screen, green, green_box)
        pygame.draw.rect(self.screen, red, red_box)
        pygame.draw.rect(self.screen, orange, orange_box)
        pygame.draw.rect(self.screen, white, white_box)



        title = myfont.render(
            self.title, 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(title,(50, 2))

        start = myfont.render(
            "Start", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(start,(270, 65))

        stop = myfont.render(
            "Stop", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(stop,(270, 100))

        next = myfont.render(
            "Next", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(next,(270, 135))

        options = myfont.render(
            "Optns", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(options,(270, 170))



        pygame.display.update()
        
    def drawSettings(self):
        xmax = pygame.display.Info().current_w
        ymax = pygame.display.Info().current_h
        
        print("xmay, ymax: ", xmax, "x", ymax)
        
        # https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
        myfont = pygame.font.SysFont('Impact', 30)

        xcent = int(xmax/2)
        ycent = int(ymax/2)
        print("xcent, ycent: ", xcent, "x", ycent)
        
        # minScale = 0.85     # Size of minute hand relative to second
        # hourScale = 0.5
        # width = 2           # Width of hands
        
        # rad = 100   # Radius
        # len = 15    # Length of ticks
        
        backgroundC = (173,216,230)
        faceC = (0, 0, 255)

        self.screen.fill(backgroundC)

        
        
        green = (0, 255, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)
        orange = (255, 162, 0)
        black = (0, 0, 0)

        black_box_1 = pygame.Rect(50, 40, 30, 20)
        black_box_2 = pygame.Rect(200, 40, 30, 20)
        black_box_3 = pygame.Rect(50, 100, 30, 20)
        black_box_4 = pygame.Rect(200, 100, 30, 20)

        # green_box = pygame.Rect(231, 61, 28, 18)
        # red_box = pygame.Rect(231, 96, 28, 18)
        # orange_box = pygame.Rect(231, 131, 28, 18)
        # white_box = pygame.Rect(231, 166, 28, 18)

        pygame.draw.rect(self.screen, black, black_box_1)
        pygame.draw.rect(self.screen, black, black_box_2)
        pygame.draw.rect(self.screen, black, black_box_3)
        pygame.draw.rect(self.screen, black, black_box_4)

        # pygame.draw.rect(self.screen, green, green_box)
        # pygame.draw.rect(self.screen, red, red_box)
        # pygame.draw.rect(self.screen, orange, orange_box)
        # pygame.draw.rect(self.screen, white, white_box)

        title = myfont.render(
            "SETTINGS", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(title,(50, 2))

        start = myfont.render(
            "SOUNDFONT", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(start,(50, 70))

        stop = myfont.render(
            "SHUFFLE", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(stop,(230, 70))

        next = myfont.render(
            "Next", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(next,(270, 135))

        options = myfont.render(
            "Optns", 
            False, (0, 0, 0), backgroundC)
        self.screen.blit(options,(270, 170))



        pygame.display.update()


menu = pymenu()
menu.updatePicture("start.jpg")
menu.updateTitle("ECE434 Beagle Screamer")
menu.drawMenu()
oldvals = [1,1,1,1]
newvals = [1,1,1,1]


def playmumsic():
    global playing
    global songIndex
    global size
    global soundfont
    global currentMidi
    mumsic = os.listdir('./midis')
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

def fixscreen(songName, screen):
    screen.updateTitle(songName)
    images = os.listdir('./images')
    if (songName + ".jpg") in images:
        screen.updatePicture(songName + ".jpg")
    else:
        screen.updatePicture("cachemiss.jpg")
    screen.drawMenu()

while True:
    songIndex
    ev_lines = getlines.event_wait(sec=1)
    oldvals = newvals
    newvals = getlines.get_values()
    vals = [1,1,1,1]
    for i in range(4):
        vals[i] = not (oldvals[i] ^ newvals[i])
        if oldvals[i] == 0 and newvals[i] == 1:
            vals[i] = 1

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
            sounds = os.listdir('./sf2files')
            sfSize = len(sounds)
            soundfont = 'sf2files/' + sounds[sfIndex]
            sfIndex = sfIndex + 1
            sfIndex = sfIndex  % sfSize
            print("Now playing: " + soundfont)
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
        fixscreen(currentMidi[0:len(currentMidi) - 4], menu)
    if(vals[2] == 0):
        songIndex = songIndex + 1
        songIndex = songIndex % size
        if(playing == True):
            stopmumsic();
            playmumsic();
            print(currentMidi)
            fixscreen(currentMidi[0:len(currentMidi) - 4], menu)

    if(vals[3] == 0 and playing == False):
        print("entering menu")
        insettings = True
        settingstate = 0
        time.sleep(0.5)

            

