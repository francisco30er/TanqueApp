import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#redespass
from ubidots import ApiClient
import math


api = ApiClient(token="972FUfeyLTXqbUKXlaLNgJ9jEHeuKl")
#variable metros cubicos
variable1 = api.get_variable("593ec67876254251716133ab")

variable = api.get_variable("593ec67876254251716133ab")


TRIG = 23  #PIN 16
ECHO = 24  #PIN 18

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

metros = 14.5 - distance 

print "Distance:",distance,"cm"

#calcula la cantidad de metros cubicos que contiene el tanque
metros = 14.89-distance

print "Hay",metros,"m3"

print "------------------------------------------------------"

if ( metros < 3) : print "Tanque vacio!"

if ( metros >= 12) : print "Tanque lleno!"

#limpia los pines GPIO
GPIO.cleanup()


response = variable1.save_value({"value": metros})

response = variable.save_value({"value": metros})

print response
time.sleep(1)
