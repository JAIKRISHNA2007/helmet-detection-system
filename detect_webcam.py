from ultralytics import YOLO

# Load your trained model
model = YOLO("models/best.pt")

# Run live webcam detection
model.predict(
    source=0,      # 0 = default webcam
    show=True,
    conf=0.75
)