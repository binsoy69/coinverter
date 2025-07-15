import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coin_handler.coin_handler import CoinHandler
import time

try:
    coin_pin = 24
    sorter_servo_pin = 18
    dispenser_pins = {
        1: 19,
        5: 20,
        10: 21,
        20: 22
    }

    handler = CoinHandler(coin_pin, sorter_servo_pin, dispenser_pins)

    print("\n[INSTRUCTIONS]")
    print("Press ENTER to wait for a real coin to be inserted.")
    print("Type a denomination (e.g. 1, 5, 10, 20) to trigger dispenser manually.")
    print("Press Ctrl+C to quit.\n")

    while True:
        cmd = input("Enter denomination to dispense or press ENTER to wait: ").strip()

        if cmd.isdigit():
            handler.dispense_coin(int(cmd))
        elif cmd == "":
            print("🪙 Waiting for coin insertion... Press Ctrl+C to exit.\n")
            # Just idle so coin handler handles GPIO interrupts
            while True:
                time.sleep(1)
        else:
            print("[Invalid] Please enter a valid number or just press ENTER.")

except KeyboardInterrupt:
    print("\n[EXIT] Stopping test.")
finally:
    handler.cleanup()
