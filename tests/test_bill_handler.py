import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bill_handler.bill_handler import BillHandler
import time

if __name__ == "__main__":
    try:
        print("[Test] Initializing BillHandler...")
        handler = BillHandler()

        print("[Test] Ready to process bills. Insert a bill.")
        while True:
            handler.process_bill()
            time.sleep(1.5)

    except KeyboardInterrupt:
        print("\n[Test] Stopped by user.")

    finally:
        handler.cleanup()
