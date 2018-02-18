# import RPi.GPIO as GPIO
# 
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11,GPIO.OUT)
# 
# pwm=GPIO.PWM(11,50)
# pwm.start(5)
# pwm.ChangeDutyCycle(10)
from servosix import ServoSix
import time

ss = ServoSix()

period = 0.5

try:
  while (True):  
    ss.set_servo(1, 0)
    time.sleep(period)
    ss.set_servo(1, 180)
    time.sleep(period)
                                                
finally:
        ss.cleanup()
