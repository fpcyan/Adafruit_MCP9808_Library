# Limitations and Troubleshooting

## Limitations:
* Due to lag time in communicating to the Arduino and receiving the response, intervals less than 1 minute can cause de-syncing between image capture and recording the temperature.
  - The current default capture interval is 30minutes, and has been tested to 10minutes.

* MCP9808 12C temperature sensors are not calibrated, and should be calibrated to an external standard.
  - The incubators in Ned Lab, to my knowlege, do not have any internal calibration method, and have never been verified or accuracy or precision. Use as your own risk.

## Troubleshooting:
* Problem: Arduino IDE is throwing an "instruction upload" error.
  - Make sure the Arduio is plugged in and the COM port is correctly set.

* Problem: sensor_time_lapse_integration.py is throwing an error.
  - Solution: Make sure the Arduino instructions were properly uploaded first!
  - Solution: Make sure the DEFAULT_PORT matches the one that the Arduino IDE uploaded instructions to.

* Problem: Nothing works!?!
  - Solution: Are you in lab? Did you plug anything in? Did you buy an Arduin yet? Yes? Email me.
