import RPi.GPIO as GPIO
import time

button = 24
count = 0
red = 17; green = 22;  blue = 27 #Ground 역할 

def clickHndler(channel):
    global count
    count = count + 1
    if (count % 2 ==0):
        GPIO.output(red, GPIO.LOW)
    else:
        GPIO.output(red, GPIO.HIGH)

    print(count)

GPIO.setwarnings(False) # 쓸데없는 경고표시 사라짐
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button, GPIO.RISING, callback= clickHndler)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT) 

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True) # 여기까지 초기화


while (True):
    time.sleep(1)