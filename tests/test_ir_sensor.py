from gpiozero import DigitalInputDevice
import time

IR_SENSOR_PIN = 18  # Must match BillHandler config
sensor = DigitalInputDevice(IR_SENSOR_PIN)

print("[IR Test] Waiting for bill (LOW = detected)...")
try:
    while True:
        if not sensor.value:  # LOW means bill detected
            print("[IR Test] Bill detected!")
        else:
            print("[IR Test] No bill")
        time.sleep(0.3)
except KeyboardInterrupt:
    print("Stopped.")
