#LED  RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17
green = 22
blue = 27

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)


GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True) # 여기까지 초기화

try:
    while True:
     GPIO.output(red, False) # red on
     GPIO.output(green, True)
     GPIO.output(blue, True)
     time.sleep(1)

     GPIO.output(blue, False)#blue on
     GPIO.output(green, True)
     GPIO.output(red, True)
     time.sleep(1)

     GPIO.output(blue, True) # Green on
     GPIO.output(green, False)
     GPIO.output(red, True)
     time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

