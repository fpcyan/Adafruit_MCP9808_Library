This explains briefly how to install and operate the programs necessary to run all of the equipment for Time Lapse Observation of Crystal Growth with Real-Time Temperature Reporting. 

This has been designed for an experimental setup for Ned Seeman's Structural DNA Nanotechnology Lab.
The Arduino MCP9808 Arduino instruction code has been modified from Adafruit's code, available on git and through their website.

This is project was undertaken by a novice (me), and as such is ugly and inefficient. Feel free to offer fixes, optimizations, and feedback to me so that I can learn for the future. 

The current implementation uses: 
Celestron (brand) USB Microscope and its software (Here)
AutoHotKey (to implement time lapse microscopy over long periods)
Arduino IDE 1.6.4 (to upload instructions to the Arduino)
Python 3.4.3 (to get the current temperature at every interval a picture is taken)

Below is a step-by-step way to use this exact set-up for someone with no programming knowledge. Again, feedback is appreciated.

Contents:
* Software Set-up
* Running the experimental
* Important variables and how to change them



~~Software Installation~~

Arduino & MCP9808 Arduino software install walkthrough:
- Follow the steps on www.arduino.cc to download and install Arduino IDE software and test the Arduino.
	This particular set-up has been tested to work on Windows 7 and 8.1, but can be modified to work on any Operating System
- Follow the steps on www.arduino.cc to install the "Adafruit_MCP9808_Library-master" library.
	The zip file is included in this folder.
- After installation, replace files "Adafruit_MCP9808.cpp" and "Adafruit_MCP9808.h" in the Arduino "library" folder with the ones included in this package


Setting up Python:
- Download and Install Python 3.4.3
- How to open Python from cmd line in Windows: https://docs.python.org/3.4/using/windows.html
- Use pip to install serial, watchdog, and tkinter. Walkthrough here: https://docs.python.org/3/installing/


Setting up autohotkey:
- Follow instructions at https://www.autohotkey.com/docs/Tutorial.htm


Setting up the microscope:
- Use the install disc to install the Celestron software to the computer
- Take note of the file path for saved images
On startup:
- Go to Resolution and set to the highest setting.
- Follow the instructions that came with the microscope to calibrate it. Take a picture of the calibration and save it in a different folder to use for scale later (only need to do once)
- Make sure the Photo folder is empty before startup (if there are pictures in there, move them and back them up)

