import cv2
from ultralytics import YOLO

# Load models
uv_model = YOLO("uv_cls_v2_ncnn_model", task='classify')
denom_model = YOLO("denom-cls-v2_ncnn_model", task='classify')

uv_labels = uv_model.names
denom_labels = denom_model.names

def capture():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Camera not accessible")
        return None
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None

def run_inference(model, frame, labels):
    resized = cv2.resize(frame, (480, 480))
    result = model.predict(resized, verbose=False)[0]
    if result.probs is None:
        return None, 0.0
    label = labels[int(result.probs.top1)]
    conf = float(result.probs.top1conf)
    print(f"[{model.model}] → {label} ({conf * 100:.2f}%)")
    return label, conf

def main():
    while True:
        print("\nChoose which YOLO model to test:")
        print("1. UV Model (for authentication)")
        print("2. Denomination Model")
        print("q. Quit")

        choice = input("Your choice: ").strip().lower()

        if choice == '1':
            print("Capturing image for UV model...")
            frame = capture()
            if frame is not None:
                run_inference(uv_model, frame, uv_labels)
            else:
                print("Failed to capture frame.")

        elif choice == '2':
            print("Capturing image for Denomination model...")
            frame = capture()
            if frame is not None:
                run_inference(denom_model, frame, denom_labels)
            else:
                print("Failed to capture frame.")

        elif choice == 'q':
            print("Exiting...")
            break

        else:
            print("Invalid input. Please choose 1, 2, or q.")

if __name__ == "__main__":
    main()
