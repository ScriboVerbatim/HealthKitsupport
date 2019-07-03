import serial
from time import sleep
from NeuroPy import NeuroPy
import datetime


f = open('test.csv', 'wb')

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'
ser.open()

neuropy = NeuroPy("/dev/rfcomm0", 115200)
neuropy.start()
sleep(5)


while True:

	try:
		print(datetime.datetime.now())
  		bpm=ser.read()  
  		if bpm:
    			print('Beats per minute= ',ord(bpm))
    
    
  		temp=ser.read() 
  		if temp:
    			print('Temperature= ',ord(temp))
  
  
    
          
            	m = neuropy.meditation
            	a = neuropy.attention
            	#r = neuropy.rawValue
            	d = neuropy.delta
            	t = neuropy.theta
            	#la = neuropy.lowAlpha
            	#ha = neuropy.highAlpha
            	#lb = neuropy.lowBeta
            	#hb = neuropy.highBeta
            	#lg = neuropy.lowGamma
            	#mg = neuropy.midGamma
            	#bs = neuropy.blinkStrength
            	#s = neuropy.poorSignal
            	print('Attention= ',a)
            	print('Meditation= ',m)
            	print('Delta= ',d)
            	print('Theta= ',t)
            	
             
            	sleep(1) # sleep for 1s
            
  except KeyboardInterrupt:
            neuropy.stop()
            break
            print("exiting!")
            
            
f.close()
