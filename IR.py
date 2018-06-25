from picamera import PiCamera
from gpiozero import LED
from signal import pause
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

camera = PiCamera()
LED_PIN = 12
IR_PIN1 = 5 
IR_PIN2 = 6
IR_PIN3 = 13
IR_PIN4 = 19
IR_PIN5 = 26
IR_PIN6 = 21

ControlPin = [4,17,27,22]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

indicator = LED(LED_PIN)
GPIO.setup(IR_PIN1, GPIO.IN)
GPIO.setup(IR_PIN2, GPIO.IN)
GPIO.setup(IR_PIN3, GPIO.IN)
GPIO.setup(IR_PIN4, GPIO.IN)
GPIO.setup(IR_PIN5, GPIO.IN)
GPIO.setup(IR_PIN6, GPIO.IN)

seq1 = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]]

seq2 = [ [1,0,0,0],
        [1,0,0,1],
        [0,0,0,1],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

count = 1
current_position = 1
def rotate(current, detect):
    print(current)
    print(detect)
    if current == detect:
        range_num = 0
        seq = seq1
    elif current > detect:
        seq = seq1
        if current - detect == 1:
            range_num = 128
        elif current - detect == 2:
            range_num = 256
        elif current - detect == 3:
            range_num = 384
        elif current - detect == 4:
            range_num = 512
        elif current - detect == 6:
            range_num = 640
    elif current < detect:
        seq = seq2
        if detect - current == 1:
            range_num = 128
        elif detect - current == 2:
            range_num = 256
        elif detect - current == 3:
            range_num = 384
        elif detect - current == 4:
            range_num = 512
        elif detect - current == 5:
            range_num = 640
    for i in range(range_num):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq[halfstep][pin])
            time.sleep(0.001)
    camera.start_preview()
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
while True:
  detect_1 = GPIO.input(IR_PIN1)
  detect_2 = GPIO.input(IR_PIN2)
  detect_3 = GPIO.input(IR_PIN3)
  detect_4 = GPIO.input(IR_PIN4)
  detect_5 = GPIO.input(IR_PIN5)
  detect_6 = GPIO.input(IR_PIN6)
  if detect_1 == False:
    print("{:>3} Sensor1 Detected!".format(count))
    time.sleep(0.5)
    rotate(current_position, 1)
    current_position = 1
  elif detect_2 == False:
    print("{:>3} Sensor2 Detected!".format(count))
    rotate(current_position, 2)
    time.sleep(0.5)
    current_position = 2
  elif detect_3 == False:
    print("{:>3} Sensor3 Detected!".format(count))
    time.sleep(0.5)
    rotate(current_position, 3)
    current_position = 3
  elif detect_4 == False:
    print("{:>3} Sensor4 Detected!".format(count))
    time.sleep(0.5)
    rotate(current_position, 4)
    current_position = 4
  elif detect_5 == False:
    print("{:>3} Sensor5 Detected!".format(count))
    time.sleep(0.5)
    rotate(current_position, 5)
    current_position = 5
  elif detect_6 == False:
    print("{:>3} Sensor6 Detected!".format(count))
    time.sleep(0.5)
    rotate(current_position, 6)
    current_position = 6
  else:
    indicator.off()
    print("{:>3} Nothing detected".format(count))
  count += 1
  time.sleep(0.2)
  
GPIO.cleanup()