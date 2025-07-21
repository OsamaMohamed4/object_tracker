import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

ret, frame = cap.read()
if not ret:
    print("❌ Failed to grab frame")
    exit()

bbox = cv2.selectROI("Select Object to Track", frame, False)

if bbox == (0, 0, 0, 0):
    print("❌ Invalid ROI selected")
    exit()

tracker = cv2.legacy.TrackerCSRT_create()  # استخدم legacy
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    success, box = tracker.update(frame)

    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    cv2.imshow("Object Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
