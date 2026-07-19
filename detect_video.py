import cv2
from ultralytics import YOLO
import os

# -----------------------------
# Load YOLO Model
# -----------------------------
model = YOLO("models/best.pt")

# -----------------------------
# Input Video
# -----------------------------
video_path = input("Enter video path: ")

if not os.path.exists(video_path):
    print("Video not found!")
    exit()

cap = cv2.VideoCapture(video_path)

# -----------------------------
# Video Properties
# -----------------------------
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# -----------------------------
# Output Video
# -----------------------------
output_path = "output_video.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

print("Processing video...")

# -----------------------------
# Frame Loop
# -----------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # YOLO Prediction
    results = model.predict(
        frame,
        conf=0.25,
        verbose=False
    )

    # Draw Bounding Boxes
    annotated_frame = results[0].plot()

    # Write Frame
    out.write(annotated_frame)

    # Show Live Detection
    cv2.imshow("Helmet Detection", annotated_frame)

    # Press Q to Exit Early
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
out.release()
cv2.destroyAllWindows()

print("\nDone!")
print("Saved as:", output_path)