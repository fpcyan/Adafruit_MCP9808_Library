This has been designed for an experimental setup for Ned Seeman's Structural DNA Nanotechnology Lab. It is designed to do long term Time Lapse Microscopy for DNA crystallization.
The Arduino MCP9808 Arduino instruction code has been modified from Adafruit's code, available on git and through their website.

This is project was undertaken by a novice (me), and is ugly and inefficient. Feel free to offer fixes, optimizations, and feedback to me so that I can learn for the future. 

The current implementation uses: 
Celestron (brand) USB Microscope and its software (Here)
AutoHotKey (to implement time lapse microscopy over long periods)
Arduino IDE 1.6.4 (to upload instructions to the Arduino)
Python 3.4.3 (to get the current temperature at every interval a picture is taken)

Further installation and use instructions are in the provided text files names "Installation and Set-up Walkthrough" and "Program Limitations and Troubleshooting". PM me if you need assistant extending the functionality or something else.