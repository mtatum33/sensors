#!/usr/bin/python

# Description

# This program can control two DC motors in the 
# the forward and backwards direction, and at various
# speeds with the  use of PWM
#
# By: Muneer Tatum

# Libraries	
import RPi.GPIO as GPIO
from time import sleep

# Set up pins for output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
pwm1 = GPIO.PWM(12,50)
pwm2 = GPIO.PWM(15,50)

# 'x' is the number of seconds that you
# would like the motor to run
def forward(x):
    pwm1.start(20)
    GPIO.output(12, GPIO.HIGH)
    sleep(x)
    GPIO.output(12, GPIO.LOW)
    pwm1.stop()

# 'x' is the number of seconds that you
# would like the motor to run
def reverse(x):
    pwm2.start(20)
    GPIO.output(15, GPIO.HIGH)
    sleep(x)
    GPIO.output(15, GPIO.LOW)
    pwm2.stop()

# Test run
print("Forward")
forward(1)
print("Reverse")
reverse(1)

# Prevents pin assignment conflicts
GPIO.cleanup()


