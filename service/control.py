import os
os.environ["DISPLAY"] = ":0"

import RPi.GPIO as gpio

IN_1 = 17
IN_2 = 22
IN_3 = 23
IN_4 = 24
EN_A = 12
EN_B = 13

def init():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    #gpio.setup(EN_A, gpio.OUT)
    #gpio.setup(EN_B, gpio.OUT)
    gpio.setup(IN_1, gpio.OUT)
    gpio.setup(IN_2, gpio.OUT)
    gpio.setup(IN_3, gpio.OUT)
    gpio.setup(IN_4, gpio.OUT)
    #gpio.output(EN_A, gpio.HIGH)
    #gpio.output(EN_B, gpio.HIGH)
    return

def clear():
    gpio.output(IN_1, gpio.LOW)
    gpio.output(IN_2, gpio.LOW)
    gpio.output(IN_3, gpio.LOW)
    gpio.output(IN_4, gpio.LOW)

def forward(stop=False):
    if stop == True:
        clear()
    else:
        gpio.output(IN_1, gpio.LOW)
        gpio.output(IN_2, gpio.HIGH)
        gpio.output(IN_3, gpio.HIGH)
        gpio.output(IN_4, gpio.LOW)

def backward(stop=False):
    if stop == True:
        clear()
    else:
        gpio.output(IN_1, gpio.HIGH)
        gpio.output(IN_2, gpio.LOW)
        gpio.output(IN_3, gpio.LOW)
        gpio.output(IN_4, gpio.HIGH)

def left(stop=False):
    if stop == True:
        clear()
    else:
        gpio.output(IN_1, gpio.HIGH)
        gpio.output(IN_2, gpio.LOW)
        gpio.output(IN_3, gpio.HIGH)
        gpio.output(IN_4, gpio.LOW)

def right(stop=False): 
    if stop == True:
        clear()
    else:
        gpio.output(IN_1, gpio.LOW)
        gpio.output(IN_2, gpio.HIGH)
        gpio.output(IN_3, gpio.LOW)
        gpio.output(IN_4, gpio.HIGH)

def move(action, stop=False):
    if action == "up":
        forward(stop)
    elif action == "down":
        backward(stop)
    elif action == "left":
        left(stop)
    elif action == "right":
        right(stop)

init()
