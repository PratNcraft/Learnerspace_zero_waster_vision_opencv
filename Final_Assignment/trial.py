from ultralytics import YOLO
import cv2

model= YOLO("best.pt")

# Load video (0= webcam or provide video file path)
video_path="WhatsApp_trial_2.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on the current frame
    results = model.predict(source=frame, conf=0.3, save=False, verbose=False)

    # Annotate the frame with the results
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("finding place to throw trash", annotated_frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()