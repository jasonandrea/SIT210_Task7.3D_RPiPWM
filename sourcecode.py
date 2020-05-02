import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep

GPIO.setmode(GPIO.BCM)
sensor = DistanceSensor(trigger = 18, echo = 24)
GPIO.setup(21, GPIO.OUT)
p = GPIO.PWM(21, 50)
p.start(0)

try:
    while True:
        # Read data every 2 seconds
        sleep(2)
        distance = sensor.distance
        distance = round(sensor.distance, 1)
        distanceInCm = distance * 100
        p.ChangeDutyCycle(100 - distanceInCm)
except KeyboardInterrupt:
    pass
    
p.stop()
GPIO.cleanup()