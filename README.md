# MIDI-Player
ECE434 Final Project - Gaven Williams, Brendan Perez
## Setup
### Required software
This project uses two programs to work: Fluidsynth and Alsa
To install Fluidsynth run the following command: <br /> ```sudo apt-get install fluidsynth``` <br />
To install Alsa, use the following command: <br />
```sudo apt-get install libasound2 alsa-utils alsa-oss``` <br />
Next, do ```sudo nano /boot/uEnv.txt``` to enable the LCD device tree. Add the line ```uboot_overlay_addr4=/lib/firmware/BB-LCD-ADAFRUIT-24-SPI1-00A0.dtbo```, and save and close the file. <br />
This should be all the setup you need to use our program.
## Hardware
For the sound, this project used the Sabrent USB audio dongle ([Found Here!](https://www.amazon.com/dp/B002R33VWW?ref=nb_sb_ss_w_as-reorder-t1_ypp_rep_k0_1_6&amp=&crid=2I6QTTIB3SO00&amp=&sprefix=sabren))
Other audio dongles may be used, but are unknown if they work. <br />
Screen - 2.4" SPI TFT Module ([Found Here!](https://www.amazon.com/HiLetgo-Display-ILI9341-Touch-240x320/dp/B07WNLNRDN)) <br />
Illuminated Push Buttons ([Found Here!](https://www.amazon.com/Baomain-Button-Switch-Latching-Rectangular/dp/B01N1RGTPH/ref=sr_1_24?keywords=illuminated+push+buttons&qid=1675718947&sr=8-24))

