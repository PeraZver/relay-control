from gpiozero import LED
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
# relay control GPIO
relay = LED(17)
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
AIN = 2
AIN_LOW = 11100
AIN_HIGH = 27750

batteryEmpty = False

print('Reading ADS1x15 values, press Ctrl-C to quit...')


while True:
	
	batteryVoltage = adc.read_adc(AIN, gain=GAIN)
	
	if (batteryVoltage < AIN_LOW):
		if batteryEmpty:
			print('Battery discharged. Running on grid supply.')
		else:		
			print('Battery is getting empty. Switching to grid supply.')
			batteryEmpty = True
			relay.on()
	
	elif (batteryVoltage > AIN_HIGH):
		if batteryEmpty:			
			print('It seems like battery is fully charged and back on.')
			batteryEmpty = False
			relay.off()
		else:
			print('Battery charged and working normally.')
			
	else:
		print('Battery charging ... Voltage: {.2}'.format(batteryVoltage))
	
	time.sleep(1)
