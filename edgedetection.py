import cv2

# Open the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Show the grayscale frame in a window
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_frame, 100, 200)

    cv2.imshow("Edge Detect", edges)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()


