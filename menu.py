#!/usr/bin/env python3
# Displays an analog clock on an LCD display
# From: https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer

import sys
import getpass
if getpass.getuser() != 'root':
    sys.exit("Must be run as root.")
import os
import pygame
import time
import math

class pymenu :
    screen = None;

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

        image = pygame.image.load(os.path.join('./images/spamt.png'))
        self.screen.blit(image, (20, 20))




        black_box_1 = pygame.Rect(230, 60, 30, 20)
        black_box_2 = pygame.Rect(230, 95, 30, 20)
        black_box_3 = pygame.Rect(230, 130, 30, 20)
        black_box_4 = pygame.Rect(230, 165, 30, 20)

        green_box = pygame.Rect(231, 61, 28, 18)
        red_box = pygame.Rect(231, 96, 28, 18)
        white_box = pygame.Rect(231, 131, 28, 18)
        orange_box = pygame.Rect(231, 166, 28, 18)

        pygame.draw.rect(self.screen, black, black_box_1)
        pygame.draw.rect(self.screen, black, black_box_2)
        pygame.draw.rect(self.screen, black, black_box_3)
        pygame.draw.rect(self.screen, black, black_box_4)

        pygame.draw.rect(self.screen, green, green_box)
        pygame.draw.rect(self.screen, red, red_box)
        pygame.draw.rect(self.screen, white, white_box)
        pygame.draw.rect(self.screen, orange, orange_box)



        title = myfont.render(
            "BIG SHOT", 
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


# Create an instance of the clock class
menu = pymenu()
menu.drawMenu()
pygame.time.wait(10000)
