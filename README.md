# MIDI-Player
ECE434 Final Project - Gaven Williams, Brendan Perez
## Setup
### Required software
This project uses a few programs to work: Fluidsynth, Alsa, and Pygame <br /><br />

Run ```install.sh``` as root to install these. <br /><br />

Next, do ```sudo nano /boot/uEnv.txt``` to enable the LCD device tree. Add the line ```uboot_overlay_addr4=/lib/firmware/BB-LCD-ADAFRUIT-24-SPI1-00A0.dtbo```, and save and close the file. <br /><br />

Next, move ```asoundrc``` to your home directory: <br />
```cd ~/MIDI-Player```<br />
```cp asoundrc ~/.asoundrc```<br /><br />

Finally, reboot your bone. 
This should be all the setup you need to use our program.
## Hardware
We are using a BeagleBone Black with a 32GB SD card. Keep this in mind when cloning the repo, since we included many large sound files.<br />
For the sound, this project used the Sabrent USB audio dongle ([Found Here!](https://www.amazon.com/dp/B002R33VWW?ref=nb_sb_ss_w_as-reorder-t1_ypp_rep_k0_1_6&amp=&crid=2I6QTTIB3SO00&amp=&sprefix=sabren))
Other audio dongles may be used, but are unknown if they work. <br />
Screen - 2.4" SPI TFT Module ([Found Here!](https://www.amazon.com/HiLetgo-Display-ILI9341-Touch-240x320/dp/B07WNLNRDN)) <br />
Illuminated Push Buttons ([Found Here!](https://www.amazon.com/Baomain-Button-Switch-Latching-Rectangular/dp/B01N1RGTPH/ref=sr_1_24?keywords=illuminated+push+buttons&qid=1675718947&sr=8-24))<br />
Any speaker that uses a 3.5mm headphone jack

![](lcdspi1.png)
