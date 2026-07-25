# 🪖 Helmet Detection System

An AI-powered Helmet Detection System built using **YOLOv8**, **Streamlit**, and **OpenCV**.

## Features

- 🖼️ Image Detection
- 🎥 Video Detection
- 📷 Live Webcam Detection
- 📊 Detection Summary
- 🎯 Adjustable Confidence Threshold
- ⚡ Real-Time YOLOv8 Inference

---

## Tech Stack

- Python
- YOLOv8 (Ultralytics)
- Streamlit
- OpenCV
- Pillow
- streamlit-webrtc

---

## Project Structure

```
YOLO-Project/
│
├── app.py
├── detect_image.py
├── detect_video.py
├── detect_webcam.py
├── models/
│   └── best.pt
├── requirements.txt
├── README.md
├── .gitignore
└── helmet_dataset/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOLO-Project.git
cd YOLO-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Features Demonstrated

- Image Detection
- Video Detection
- Webcam Detection
- Object Counting
- Helmet Detection
- No Helmet Detection

---

## Model

The project uses a custom-trained **YOLOv8** model trained on a helmet detection dataset.

Current classes:

- Helmet
- Motor
- No Helmet
- Person

---

## Application Results

### Image Detection

![Image Detection](screenshots/image_detection.png)

### Video Detection

![Video Detection](screenshots/video_detection.png)

---

## 📈 Model Training Results

The YOLO model was trained on a custom helmet detection dataset. The following visualizations summarize the model's training performance and evaluation.

### Training Metrics

The figure below shows the model's learning progress throughout training, including training loss, validation loss, precision, recall, mAP@50, and mAP@50-95.

![Training Results](training_results/results.png)

---

### Confusion Matrix

The confusion matrix illustrates how accurately the trained YOLO model classified each object category.

![Confusion Matrix](training_results/confusion_matrix.png)

---

### Normalized Confusion Matrix

The normalized confusion matrix provides a percentage-based view of prediction accuracy across all classes.

![Normalized Confusion Matrix](training_results/confusion_matrix_normalized.png)

---

### Dataset Label Distribution

This visualization summarizes the distribution of object labels and bounding box locations within the training dataset.

![Dataset Labels](training_results/labels.jpg)

---

## Future Improvements

- Improved dataset
- Higher model accuracy
- Rider-Helmet matching
- Vehicle tracking
- Violation screenshot capture
- License plate recognition
- Deployment on Streamlit Cloud

---

## Internship Information

This project was developed as part of the AI Internship at **Codtech IT Solutions Private Limited**.

- **Intern ID:** CTTS162
- **Intern:** JAI KRISHNA S

---

## Author

JAI KRISHNA S
