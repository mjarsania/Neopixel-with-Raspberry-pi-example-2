import time
import board
import neopixel

# LED strip configuration:
LED_COUNT = 16   # Number of LED pixels.
LED_PIN = board.D18  # GPIO pin connected to the pixels (change as needed).
LED_BRIGHTNESS = 0.2  # Set the brightness (0.0 to 1.0)

# Create NeoPixel object with configuration above:
strip = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)

try:
    while True:
        # Set all LEDs to red
        strip.fill((255, 0, 0))
        strip.show()
        time.sleep(1)

        # Set all LEDs to green
        strip.fill((0, 255, 0))
        strip.show()
        time.sleep(1)

        # Set all LEDs to blue
        strip.fill((0, 0, 255))
        strip.show()
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up on keyboard interrupt
    strip.fill((0, 0, 0))
    strip.show()
