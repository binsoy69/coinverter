import RPi.GPIO as GPIO
import time
from datetime import datetime

# GPIO Pin
COIN_PIN = 24

# Timing thresholds
COIN_TIMEOUT = 0.5  # seconds to wait before assuming pulse group is done

# Pulse data
pulse_count = 0
last_pulse_time = time.time()
pulse_start_time = None

# Pulse-to-coin mapping
COIN_MAP = {
    1: "1 PHP",
    5: "5 PHP",
    10: "10 PHP",
    20: "20 PHP"
}

def coin_pulse_callback(channel):
    global pulse_count, last_pulse_time, pulse_start_time

    now = time.time()
    if now - last_pulse_time > COIN_TIMEOUT:
        # Too long since last pulse; reset count and start time
        pulse_count = 0
        pulse_start_time = now
    elif pulse_count == 0:
        # First pulse of new group
        pulse_start_time = now

    pulse_count += 1
    last_pulse_time = now

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(COIN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(COIN_PIN, GPIO.FALLING, callback=coin_pulse_callback, bouncetime=1)

print("Waiting for coin insert... Press Ctrl+C to stop.")

try:
    while True:
        now = time.time()
        if pulse_count > 0 and (now - last_pulse_time > COIN_TIMEOUT):
            coin_value = COIN_MAP.get(pulse_count, f"Unknown ({pulse_count} pulses)")
            duration = last_pulse_time - pulse_start_time if pulse_start_time else 0
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Coin inserted: {coin_value}")
            print(f"  -> Time elapsed during pulses: {duration:.3f} seconds")
            # Reset for next coin
            pulse_count = 0
            pulse_start_time = None
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()
