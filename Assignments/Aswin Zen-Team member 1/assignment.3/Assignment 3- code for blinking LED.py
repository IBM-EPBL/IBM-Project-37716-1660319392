import RPI.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, ini

while True:
    GPIO.output(7, GPIO.HIG
    print("LED ob")
    sleep(1)
    GPIO.output("LED off")
    sleep(1)            
            
           
