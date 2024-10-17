import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

def map_range(value, in_min, in_max, out_min, out_max):
    input= (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    if(input>0):
        return input
    else:
         return 0

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    print(volume)
    sensor=map_range(volume,10000,40535,0,11)
    print(sensor)
    for x in range(0,sensor):
        leds[x].value = True
    
    sleep(0.5)

    for x in range(0,11):
        leds[x].value = False

    sleep(0.1)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?

