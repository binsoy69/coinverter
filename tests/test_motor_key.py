import time
import curses
from gpiozero import Motor, PWMOutputDevice

# GPIO Pin Configuration
MOTOR_IN1 = 20
MOTOR_IN2 = 21
PWM_PIN = 16

# Initialize motor and speed control
motor = Motor(forward=MOTOR_IN1, backward=MOTOR_IN2)
pwm_speed = PWMOutputDevice(PWM_PIN)
pwm_speed.value = 1  # Default speed (0.0 - 1.0)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    stdscr.addstr(0, 0, "[Arrow Key Control] ←: Reverse, →: Forward, q: Quit")

    try:
        while True:
            key = stdscr.getch()

            if key == curses.KEY_LEFT:
                stdscr.addstr(2, 0, "[Motor] Reverse")
                motor.backward()

            elif key == curses.KEY_RIGHT:
                stdscr.addstr(2, 0, "[Motor] Forward")
                motor.forward()

            elif key == -1:
                motor.stop()

            elif key == ord('q'):
                break

            stdscr.refresh()

    except KeyboardInterrupt:
        pass
    finally:
        motor.stop()
        pwm_speed.close()

if __name__ == "__main__":
    curses.wrapper(main)
