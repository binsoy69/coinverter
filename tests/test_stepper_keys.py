import RPi.GPIO as GPIO
import time
import curses

# Stepper Motor GPIOs
X_STEP = 20
X_DIR = 21
Y_STEP = 19
Y_DIR = 26

# Movement settings
STEPS = 100
DELAY = 0.001

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([X_STEP, X_DIR, Y_STEP, Y_DIR], GPIO.OUT)

def move_stepper(step_pin, dir_pin, direction=True, steps=STEPS, delay=DELAY):
    GPIO.output(dir_pin, GPIO.HIGH if direction else GPIO.LOW)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.addstr(0, 0, "[Stepper Test - ncurses]")
    stdscr.addstr(2, 0, "Use arrow keys to move:")
    stdscr.addstr(3, 0, "↑ Y Forward    ↓ Y Backward")
    stdscr.addstr(4, 0, "← X Backward   → X Forward")
    stdscr.addstr(6, 0, "Press 'q' to quit.\n")

    try:
        while True:
            key = stdscr.getch()

            if key == curses.KEY_UP:
                stdscr.addstr(8, 0, "[Y+] Moving Y forward   ")
                move_stepper(Y_STEP, Y_DIR, True)

            elif key == curses.KEY_DOWN:
                stdscr.addstr(8, 0, "[Y-] Moving Y backward  ")
                move_stepper(Y_STEP, Y_DIR, False)

            elif key == curses.KEY_LEFT:
                stdscr.addstr(8, 0, "[X-] Moving X backward  ")
                move_stepper(X_STEP, X_DIR, False)

            elif key == curses.KEY_RIGHT:
                stdscr.addstr(8, 0, "[X+] Moving X forward   ")
                move_stepper(X_STEP, X_DIR, True)

            elif key == ord('q'):
                stdscr.addstr(10, 0, "[Exit] Quitting test.")
                stdscr.refresh()
                break

            stdscr.refresh()
            time.sleep(0.05)

    except Exception as e:
        stdscr.addstr(12, 0, f"[Error] {str(e)}")

    finally:
        GPIO.cleanup()
        stdscr.addstr(13, 0, "[Cleanup] GPIO reset.")
        stdscr.refresh()
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(main)
