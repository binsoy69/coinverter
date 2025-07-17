import RPi.GPIO as GPIO
import time
import keyboard  # Requires `pip install keyboard` and run as sudo

# Stepper Motor GPIOs (adjust as needed)
X_STEP = 20
X_DIR = 21
Y_STEP = 19
Y_DIR = 26

# Settings
STEPS_PER_MOVE = 100
STEP_DELAY = 0.001  # seconds per step pulse

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR], GPIO.OUT)

def move_stepper(step_pin, dir_pin, direction=True, steps=200, delay=0.001):
    GPIO.output(dir_pin, GPIO.HIGH if direction else GPIO.LOW)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

print("\n[Stepper Test - Key Control]")
print("Use arrow keys to move stepper motors:")
print("⬆️  Up = Y forward")
print("⬇️  Down = Y backward")
print("⬅️  Left = X backward")
print("➡️  Right = X forward")
print("Press 'q' to quit.\n")

try:
    while True:
        if keyboard.is_pressed("up"):
            print("[Y+] Moving Y forward")
            move_stepper(Y_STEP, Y_DIR, direction=True, steps=STEPS_PER_MOVE, delay=STEP_DELAY)

        elif keyboard.is_pressed("down"):
            print("[Y-] Moving Y backward")
            move_stepper(Y_STEP, Y_DIR, direction=False, steps=STEPS_PER_MOVE, delay=STEP_DELAY)

        elif keyboard.is_pressed("left"):
            print("[X-] Moving X backward")
            move_stepper(X_STEP, X_DIR, direction=False, steps=STEPS_PER_MOVE, delay=STEP_DELAY)

        elif keyboard.is_pressed("right"):
            print("[X+] Moving X forward")
            move_stepper(X_STEP, X_DIR, direction=True, steps=STEPS_PER_MOVE, delay=STEP_DELAY)

        elif keyboard.is_pressed("q"):
            print("[Exit] Quitting test.")
            break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n[Interrupted]")

finally:
    GPIO.cleanup()
    print("[Cleanup] GPIO reset.")
