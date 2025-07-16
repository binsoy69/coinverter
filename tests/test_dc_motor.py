import time
from gpiozero import Motor, PWMOutputDevice

MOTOR_IN1 = 16
MOTOR_IN2 = 20
PWM_PIN = 21

motor = Motor(forward=MOTOR_IN1, backward=MOTOR_IN2)
pwm_speed = PWMOutputDevice(PWM_PIN)

try:
    pwm_speed.value = 0.8
    print("[Motor Test] Forward for 2s")
    motor.forward()
    time.sleep(2)
    motor.stop()

    time.sleep(1)

    print("[Motor Test] Backward for 2s")
    motor.backward()
    time.sleep(2)
    motor.stop()

except KeyboardInterrupt:
    print("Stopped.")
finally:
    motor.stop()
    pwm_speed.close()
