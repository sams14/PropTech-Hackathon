setChartLibrary('google-chart');
setChartTitle('Your Graph Title');
setChartType('lineGraph');
add(183);
mul(0.0977);    
mul(1.8);
plotChart('time_stamp','temperature');

/*
The formula for converting temperature from Celcius to Fahrenheit is,
F = 1.8*C + 32

So, to show the reading in Fahrenheit, we will need to multiply the sensor reading by 1.8 and add 32 to it. 
*/
