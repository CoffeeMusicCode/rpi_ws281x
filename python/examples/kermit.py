import time

from neopixel import *

# import argparse
# import signal
import sys

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)


# LED strip configuration:
LED_COUNT      = 120      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 1     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering


LO = 29 # Left Outside
LT = 4 # Left Top
LI = 22 # Left Inside
BB = 10 # Bottom
RI = 22 # Right Inside
RT = 4 # Right Top
RO = 29 # Right Outside


def showCount():
    return LO + LT + LI + BB + RI + RT + RO, LED_COUNT


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=100):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def turnOff(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()


# Main program logic follows:
if __name__ == '__main__':

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    print ('(LEDs Used, Total Count)')
    print (showCount())
    print ('Press Ctrl-C to quit.')
    while True:
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        turnOff(strip)
        colorWipe(strip, Color(0, 255, 0))  # Green wipe
        turnOff(strip)
        colorWipe(strip, Color(0, 0, 255))  # Blue wipe
        turnOff(strip)
