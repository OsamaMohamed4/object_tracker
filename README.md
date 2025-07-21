# 🧠 Object Tracking using OpenCV (CSRT Tracker)

This project demonstrates a basic object tracking system using **OpenCV** and the **CSRT tracker**. The user selects a **Region of Interest (ROI)** in the first frame from the webcam, and the tracker follows it in real time.

---

## 🚀 How to Run the Project

### ✅ Requirements

- Python 3.7 or higher  
- OpenCV ≥ 4.5 (must include `cv2.legacy` module)  
- A working webcam  

---

### 🧩 Install Dependencies

Use the following command to install the required libraries:

```bash
pip install opencv-python opencv-contrib-python
```

> ⚠️ Do **not** use `opencv-python-headless` — it disables GUI functions like `cv2.imshow()` and `cv2.selectROI()`.

---

### ▶️ Run the Tracker

Run the Python script:

```bash
python object_tracker.py
```
# 🧠 Object Tracking using OpenCV (CSRT Tracker)

This project demonstrates a basic object tracking system using **OpenCV** and the **CSRT tracker**. The user selects a **Region of Interest (ROI)** in the first frame from the webcam, and the tracker follows it in real time.

---

## 🚀 How to Run the Project

### ✅ Requirements

- Python 3.7 or higher  
- OpenCV ≥ 4.5 (must include `cv2.legacy` module)  
- A working webcam  

---

### 🧩 Install Dependencies

Use the following command to install the required libraries:

```bash
pip install opencv-python opencv-contrib-python
```

> ⚠️ Do **not** use `opencv-python-headless` — it disables GUI functions like `cv2.imshow()` and `cv2.selectROI()`.

---

### ▶️ Run the Tracker

Run the Python script:

```bash
python object_tracker.py
```

Then follow these steps:

1. A window will open showing your webcam feed.
2. Use your mouse to select the object you want to track.
3. Press `ENTER` or `SPACE` to confirm the selection.
4. The CSRT tracker will begin tracking the selected object in real time.

---

## 🛠️ Notes

- If the camera fails to start, make sure it's not being used by another app.
- If you see an error like `cv2.error: (-215:Assertion failed)`, make sure the frame is not empty and your webcam is working.
- If you get `AttributeError: module 'cv2' has no attribute 'TrackerCSRT_create'`, your OpenCV version might be incompatible. Use `cv2.legacy.TrackerCSRT_create()` instead.
- This script uses `cv2.legacy.TrackerCSRT_create()` — make sure your OpenCV version supports it.

---

✅ Tested on:
- Python 3.11
- OpenCV 4.12.0
- Windows 10 / Ubuntu 22.04

Then follow these steps:

1. A window will open showing your webc
