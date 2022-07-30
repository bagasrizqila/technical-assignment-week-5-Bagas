 import LiquidCrystal_I2C  
 from time import sleep  
 import RPi.GPIO as gp  
 gp.setmode(gp.BOARD)  
 gp.setup(7,gp.IN)  
 lcd=LiquidCrystal_I2C.lcd()  
 lcd.clear()  
 lcd.display("Initiating Mic...",1,0)  
 sleep(1)  
 lcd.display("Listening",2,4)  
 sleep(1)  
 while True:  
   try:  
     while(gp.input(7)==1):  
       print("SPEAKING...")  
       lcd.display("SPEAKING",1,1)  
     else:  
       lcd.clear()  
   except KeyboardInterrupt:  
     gp.cleanup()  
     break  