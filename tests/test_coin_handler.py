from coin_handler.coin_handler import CoinHandler
import time

try:
    coin_pin = 17
    sorter_servo_pin = 18
    dispenser_pins = {
        1: 19,
        5: 20,
        10: 21,
        20: 22
    }

    handler = CoinHandler(coin_pin, sorter_servo_pin, dispenser_pins)

    while True:
        cmd = input("Enter ₱ value to dispense (or ENTER to wait for real coin): ")
        if cmd.strip().isdigit():
            handler.dispense_coin(int(cmd.strip()))
        else:
            print("Waiting for coin insertion... (CTRL+C to quit)")

except KeyboardInterrupt:
    print("\n[Main] Exiting.")
finally:
    handler.cleanup()
