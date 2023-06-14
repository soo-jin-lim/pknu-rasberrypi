# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18

#GPIO.setmode(GPIO.BOARD) # 1~40
GPIO.setmode(GPIO.BCM) #GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT)

while (True):
        GPIO.output(signal_pin, True) #GPIO 핀에 전압시그널 온
        time.sleep(2) #2초 동안 불킴내
        GPIO.output(signal_pin,  False) #GPIO18 핀에 전압시그널 오프
        time.sleep(1)#1초동안 불끈 상태로 대기