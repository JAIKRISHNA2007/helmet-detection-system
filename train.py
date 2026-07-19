from ultralytics import YOLO

def main():
    # Load the pretrained YOLOv8 nano model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data="helmet_dataset/data.yaml",
        epochs=30,
        imgsz=640,
        batch=4,
        workers=0,
        name="helmet_detection"
    )

if __name__ == "__main__":
    main()