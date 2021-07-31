
setChartLibrary('google-chart');
setChartTitle('Light Sensor');
setChartType('lineGraph');
plotChart('time_stamp','temperature');

/*
When light intensity increases, the voltage on the analog input pin also increases. The Bolt then converts that the voltage a 10 bit (10 places in binary number system) 
digital value that varies from 0-1024 (0 to 2 raised to 10).

This digital data is then sent to the cloud where it is plotted for visual representation.
*/
