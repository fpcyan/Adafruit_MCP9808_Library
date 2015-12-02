STLI is a Python command line app which was written to automate long term Time Lapse Digital Microscopy and Real-Time Thermosensing. This app was written first in June 2015 as a novice research project by [fpcyan][fpcyan] for use observing DNA Crystallization in Ned Seeman's [DNA Nanotechnology Lab][ned-link] at New York University. The original Arduino code was written by [Adafruit][adafruit], and modified for parallel temperature sensing.

Apologies for the ugly code! Because I don't have access to a equipment for testing, I am cleaning it up slowly because stability > a well-needed rewrite.

The current projects are build using:
* [Celestron USB Microscope][celestron-link]
* [AutoHotKey][ahk-link]
* [Arduino][arduino-link] IDE 1.6.4
* [Python 3.4.3][python-link]

To use this repo, you need an Arduino Uno and MCP9808 12C temperature sensor (or two).

[Click here][long-instructions] for extensive instructions intended for a general audience.
[Click here][limitations] for a brief explanation of the limitations of this analytical tool.

In brief:
* Set up your experiment under your microscope.
* upload the instructions in the provided Adafruit_MCP9808 library to the your Arduino.
* Verify that the active USB port is the same as in sensor_time_lapse_integration.py.
* Run sensor_time_lapse_integration.py, and make sure that it is watching whatever directory your microscope saves photos to.
* Run automate_time_lapse.ahk (default time lapse interval of 30min).
* Enjoy!



[fpcyan]: https://github.com/fpcyan
[adafruit]: https://github.com/adafruit
[ned-link]: http://seemanlab4.chem.nyu.edu/
[celestron-link]: http://www.celestron.com/browse-shop/microscopes/digital-microscopes/handheld-digital-microscope-pro
[ahk-link]: https://www.autohotkey.com/
[arduino-link]: https://www.arduino.cc/en/Main/Software
[python-link]: https://python.org
[long-instructions]: docs/installation_walkthrough.md
[limitations]: docs/limitations_and_troubleshootings.md
