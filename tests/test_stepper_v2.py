import RPi.GPIO as GPIO
import curses
import time

# === GPIO Pin Setup ===
STEP_PIN = 20
DIR_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# === Motion Settings ===
steps_per_revolution = 200
microsteps = 16
lead_screw_lead = 8.0

steps_per_mm = (steps_per_revolution * microsteps) / lead_screw_lead
mm_per_second = 160.0
step_delay = 1.0 / (steps_per_mm * mm_per_second)  # Delay between steps

def spin_motor(direction):
    GPIO.output(DIR_PIN, direction)
    for _ in range(int(steps_per_mm)):  # One mm worth of steps
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(step_delay / 2)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(step_delay / 2)

def main(stdscr):
    curses.cbreak()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    stdscr.addstr(0, 0, "Press ← for reverse, → for forward, q to quit")

    while True:
        key = stdscr.getch()
        if key == curses.KEY_RIGHT:
            print("Spinning motor forward")
            spin_motor(True)
        elif key == curses.KEY_LEFT:
            print("Spinning motor backward")
            spin_motor(False)
        elif key == ord('q'):
            break

curses.wrapper(main)
GPIO.cleanup()