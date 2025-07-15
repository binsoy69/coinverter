import RPi.GPIO as GPIO
import time
import threading

FORWARD = 170
BACKWARD = 0

class CoinHandler:
    def __init__(self, coin_pin, sorter_servo_pin, dispenser_pins, pulse_timeout=1.0):
        self.coin_pin = coin_pin
        self.sorter_servo_pin = sorter_servo_pin
        self.dispenser_pins = dispenser_pins
        self.pulse_timeout = pulse_timeout

        self.pulse_count = 0
        self.last_pulse_time = 0
        self.timer_thread = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.coin_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        

        # Sorter servo setup
        GPIO.setup(self.sorter_servo_pin, GPIO.OUT)
        self.sorter_servo = GPIO.PWM(self.sorter_servo_pin, 50)
        self.sorter_servo.start(0)
        self.center_sorter()

        # Dispenser servos setup
        self.dispenser_pins = dispenser_pins  # { denomination: pin }
        self.dispenser_servos = {}  # { pin: servo }
        self.init_dispensers()

        GPIO.add_event_detect(self.coin_pin, GPIO.FALLING, callback=self.pulse_detected, bouncetime=50)

        print("[CoinHandler] Ready")

    # --- General servo function ---
    def set_angle(self, servo, angle):
        duty = 2 + (angle / 18)
        servo.ChangeDutyCycle(duty)
        time.sleep(0.002)
        servo.ChangeDutyCycle(0)
      
    # --- Coin detection + sorting ---
    def pulse_detected(self, channel):
        now = time.time()
        self.pulse_count += 1
        self.last_pulse_time = now
        print(f"[Pulse] {self.pulse_count}")

        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.wait_for_coin_end)
            self.timer_thread.start()

    def wait_for_coin_end(self):
        while True:
            if time.time() - self.last_pulse_time > self.pulse_timeout:
                self.process_coin()
                self.pulse_count = 0
                break
            time.sleep(0.1)

    def process_coin(self):
        value = self.pulse_count
        print(f"[Coin] Detected: ₱{value}")

        if value in [1, 5]:
            print(f"[Sort] Sorting ₱{value} coin")
            self.sort_left()
        elif value in [10, 20]:
            print(f"[Sort] Sorting ₱{value} coin")
            self.sort_right()
        else:
            print(f"[Warning] Unknown ₱{value}")
            self.center_sorter()

    def sort_left(self):
        print("[Sort] LEFT")
        self.set_angle(self.sorter_servo, 95)
        self.center_sorter()

    def sort_right(self):
        print("[Sort] RIGHT")
        self.set_angle(self.sorter_servo, 35)
        self.center_sorter()

    def center_sorter(self):
        print("[Sort] CENTER")
        self.set_angle(self.sorter_servo, 65)

    def init_dispensers(self):
        """Initialize dispenser servos, store PWM objects, and reset to BACKWARD angle."""
        for denom, pin in self.dispenser_pins.items():
            GPIO.setup(pin, GPIO.OUT)
            servo = GPIO.PWM(pin, 50)
            servo.start(0)
            self.dispenser_servos[pin] = servo
            self.set_angle(servo, BACKWARD)
            print(f"[Init] Dispenser for ₱{denom} on GPIO {pin} initialized to BACKWARD")

    # --- Dispenser sweeping logic ---
    def dispense_coin(self, denom):
        pin = self.dispenser_pins.get(denom)
        servo = self.dispenser_servos.get(pin)

        if not servo:
            print(f"[Error] No initialized servo for ₱{denom}")
            return

        print(f"[Dispense] Sweeping servo for ₱{denom} coin...")
        for pos in range(BACKWARD, FORWARD):
            self.set_angle(servo, pos)
        for pos in range(FORWARD, BACKWARD - 1, -1):
            self.set_angle(servo, pos)
        print(f"[Dispense] ₱{denom} complete.\n")


    # --- Cleanup ---
    def cleanup(self):
        print("[Cleanup] Releasing resources...")
        GPIO.cleanup()
