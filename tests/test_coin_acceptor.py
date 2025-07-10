import RPi.GPIO as GPIO
import time

COIN_PIN = 17  # GPIO17 (Pin 11)

def coin_detected(channel):
    print(f"[{time.strftime('%H:%M:%S')}] Coin inserted!")

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(COIN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(COIN_PIN, GPIO.FALLING, callback=coin_detected, bouncetime=100)

    print("Coin acceptor test started. Insert a coin to see detection...")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    setup()
