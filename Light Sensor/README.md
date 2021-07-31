# Light Monitoring using LDR (Light dependent resistor)

## Things used in this project

### Hardware components
- Bolt IoT Bolt WiFi Module
- LDR (Light Dependent Resistor)
- Resistor 10k ohm
- Jumper wires
### Software apps and online services
- Bolt Cloud
- Bolt IoT Android App or Bolt IoT iOS App

## Working principle
This project is based on the principle that whenever the light falling on the sensor changes, the resistance of sensor changes which is then converted into a 
change in voltage. The ADC pin on Bolt WiFi Module converted this analog voltage level into digital values which are shown on the graphs.

We connect the LDR between 5v pin and the analog input pin (A0), so that when light intensity increases, the resistance of LDR decreases so the voltage across 
the LDR decreases and as a result, the voltage on the analog input pin increases.

This means that as the light intensity increases, the voltage on the analog input pin also increases. The Bolt then converts that the voltage a 10 bit 
(10 places in binary number system) digital value that varies from 0-1024 (0 to 2 raised to 10).
