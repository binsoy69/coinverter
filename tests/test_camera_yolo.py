import cv2
from ultralytics import YOLO

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
    print(f"[{model.model}] → {label} ({conf*100:.2f}%)")
    return label, conf

frame = capture()
if frame is not None:
    print("Running UV model...")
    run_inference(uv_model, frame, uv_labels)
    
    print("Running Denomination model...")
    run_inference(denom_model, frame, denom_labels)
else:
    print("Failed to capture frame")
