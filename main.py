import RPi.GPIO as GPIO
import time

## This works and tells me which one called what
## Perfectly functional

numbers = [4, 1, 2, 3]
buttons = [13, 16, 20, 19]

def callback(chnl):
    print(f"well {numbers[buttons.index(chnl)]} was called")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for btn in buttons:
    GPIO.add_event_detect(btn, GPIO.RISING, callback=callback, bouncetime=1000)

time.sleep(45)

GPIO.cleanup()