#include <Wire.h>
#include "Adafruit_MCP9808.h"

// Create the MCP9808 temperature sensor object
Adafruit_MCP9808_1 tempsensor1 = Adafruit_MCP9808_1();
Adafruit_MCP9808_2 tempsensor2 = Adafruit_MCP9808_2();
void setup() {
  Serial.begin(9600);

  tempsensor1.begin();
  tempsensor2.begin();

}

void loop() {
  // Read and print out the temperature, then convert to *C
  if (Serial.available()) {
    int b = Serial.read();

    float c = tempsensor1.readTempC();
    float c2 = tempsensor2.readTempC();
    Serial.print("Sensor 1 Temp:,"); Serial.print(c); Serial.print(",");
    Serial.print("Sensor 2 Temp:,"); Serial.print(c2); Serial.print(",");
    delay(250);

    tempsensor1.shutdown_wake(1); // shutdown MSP9808 - power consumption ~0.1 mikro Ampere
    tempsensor2.shutdown_wake(1); // shutdown MSP9808 - power consumption ~0.1 mikro Ampere
    delay(1000);

    tempsensor1.shutdown_wake(0);
    tempsensor2.shutdown_wake(0);
  }

}
