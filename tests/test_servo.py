import RPi.GPIO as GPIO
import time

SERVO_PIN = 18  # Use PWM-capable pin like GPIO18 (Pin 12)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz
    pwm.start(0)

    try:
        while True:
            print("Dispense: Swing forward")
            pwm.ChangeDutyCycle(7.5)  # ~90 degrees
            time.sleep(0.5)

            print("Return: Swing backward")
            pwm.ChangeDutyCycle(5)  # ~0 degrees
            time.sleep(0.5)

            pwm.ChangeDutyCycle(0)  # Stop signal (avoid jitter)
            time.sleep(2)

    except KeyboardInterrupt:
        print("Stopping...")
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    setup()
