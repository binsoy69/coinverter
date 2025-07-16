import time
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor

SORTER_STEP = 25
SORTER_DIR = 24
TRIG = 6
ECHO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SORTER_STEP, GPIO.OUT)
GPIO.setup(SORTER_DIR, GPIO.OUT)

sensor = DistanceSensor(echo=ECHO, trigger=TRIG, max_distance=2.0)

BIN_DISTANCES = {
    "50php": 5.7,
    "100php": 14.05,
    "200php": 22.4,
    "500php": 30.8,
    "1000php": 36.8,
    "1000php_polymer": 37.0
}

TOLERANCE = 1.5

def get_avg_dist(samples=5):
    return round(sum(sensor.distance for _ in range(samples)) / samples * 100, 2)

def move_stepper(direction=True, steps=200, delay=0.001):
    GPIO.output(SORTER_DIR, GPIO.LOW if direction else GPIO.HIGH)
    for _ in range(steps):
        GPIO.output(SORTER_STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(SORTER_STEP, GPIO.LOW)
        time.sleep(delay)

def align_to_bin(target_dist):
    print(f"Aligning to {target_dist}cm...")
    for _ in range(1000):
        current = get_avg_dist()
        error = current - target_dist
        print(f"Current: {current} cm (error: {error:.2f})")

        if abs(error) <= TOLERANCE:
            print("Aligned!")
            return True

        move_stepper(direction=(error > 0), steps=100)

    print("Failed to align.")
    return False

if __name__ == "__main__":
    try:
        target = input("Enter bin name (e.g. 100php): ").strip()
        if target in BIN_DISTANCES:
            align_to_bin(BIN_DISTANCES[target])
        else:
            print("Unknown bin.")
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        GPIO.cleanup()
