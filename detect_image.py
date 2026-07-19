from ultralytics import YOLO

# Load your trained model
model = YOLO("models/best.pt")

# Run detection on an image
results = model("test_images/bike.jpeg", show=True, save=True)

print("Detection completed!")