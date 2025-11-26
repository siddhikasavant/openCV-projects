import cv2
import dlib

# Load face detector and landmarks predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        # Draw rectangle around face
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # blue rectangle
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    landmarks = predictor(gray, face)
    for n in range(48,68):  # 68 landmarks
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
        cv2.imshow("Frame", frame)

cap.release()
cv2.destroyAllWindows()
