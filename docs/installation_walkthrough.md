# Installation and Set-up Walkthrough
<sub>Feedback is appreciated! Let me know if any of the instructions are unclear! </sub>

This guide is intended for people who have never used Python or Arduinos. It is intended for researchers who want to replicate this analytical set-up, not developers.

----

## Software Set-up

Four programs are required for the experimental set-up:
* [Celestron][celestron-link] Handheld Digital Microscope PRO (or whatever you have on hand)
* [Arduino IDE][arduino-link]
* [AutoHotKey][ahk-link]
* [Python 3.4.3][python-link] (any Python 3.4.x should work)

### Celestron install

1. Put the CD that came with the microscope into the CD-Drive.
2. Install the software.
3. Done! You have a very simple interface for using the microscope now!

### Arduino install

1. Follow the steps on the provided link aboce to install the Arduino IDE software
2. Follow the [Getting Started][started-link] instructions.
3. Install the MCP9808 thermosensor library.
  - Open the Arduin IDE.
  - Go to Sketch -> Libraries -> Add Library from Zip
  - Choose the Adafruit_MCP9808_Library-master zip in the lib directory.
4. Follow the [directions][started-link] to find the correct port (e.g. COM 4)

### Python install

1. Download and install Python 3.4.x.
2. Download and install the custom libraries via terminal
  - Open window command prompts
  - Type the following:
    `cd C:\Python34`
    `python -m pip install pyserial`
    `python -m pip install watchdog`
    Note: wait for each installation to complete before moving on
3. Right click sensor_time_lapse_integration.py and "Edit with IDLE".
  - Change the DEFAULT_PORT to the port that your Arduino is connected to.
  - Save the file

### AutoHotKey install

1. Follow the [installation instructions][ahk-tutorial].
  - Refer to the tutorial if you want to edit the default time lapse interval


## Running the Experiment

1. Make sure the Arduino is connected to the computer via USB
2. Open twosensors.ino
3. Upload the instructions to the Arduino

4. Run sensor_time_lapse_integration.py
5. Choose the directory to watch (typically Documents\\Microcapture_Photo)

6. Run automate_time_lapse.ahk
  - Hotkeys:
    * Start: Windows key + Space
    * Stop: Hit "F1" or "P"
  Note: The microscopes software **MUST** be the active window during this experiment, or the program will not capture photos.

7. Run the Celestron software
8. Set the resolution to maximum
9. Make sure your experimental crystal drop is in focus and correctly *sealed*.
10. Close and run the incubator however you programmed it.

11. Start the time-lapse with the ahk hotkey ( Windows key + Space )
  Note: Make sure python program created the log! (Typically made in the same directory at the python file). Make sure the incubator ramp and experimental conditions are documented in your lab notebook!

12. Leave the experiment to run its course.

13. When finished, press "F1" or "P" to end the experiment.
14. Press Control + C in IDLE or the command prompt to end the program.

15. Move all of the pictures to a new, labeled folder (otherwise the microscope will freeze the next time you try to open the program).
16. Move the tempsensing.csv file to a new, labeled folder.
17. Move the testlog to the new folder.
18. Repeat!



[celestron-link]: http://www.celestron.com/browse-shop/microscopes/digital-microscopes/handheld-digital-microscope-pro
[arduino-link]: https://www.arduino.cc/en/Main/Software
[ahk-link]: https://www.autohotkey.com/
[python-link]: https://www.python.org/downloads/release/python-343/
[started-link]: https://www.arduino.cc/en/Guide/Windows
[ahk-turorial]: https://www.autohotkey.com/docs/Tutorial.htm
