# Temperature monitoring system using LM35 (Temperature sensor)

## Things used in this project

### Hardware components

- Bolt IoT Bolt WiFi Module

- LM35 sensor

- Jumper wires

### Software apps and online services

- Bolt IoT Bolt Cloud

- Bolt IoT Android App or Bolt IoT iOS App

## Working principle

Here in our system, LM35 is the sensor that senses the temperature of its environment and based on it's value it generates an analog output voltage. This analog voltage produced by the LM35 is then given as input to the Bolt A0 pin. The Bolt then converts the analog value into a 10 bit digital value that varies from 0-1023. This digital data is sent to the cloud via Bolt device.

