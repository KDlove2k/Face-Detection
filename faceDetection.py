import cv2

# Tải Haar cascade cho phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Bắt đầu video từ webcam
cap = cv2.VideoCapture(0)

while True:
    # Lấy từng khung hình
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Chuyển đổi sang ảnh grayscale

    # Phát hiện khuôn mặt
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Vẽ hình chữ nhật quanh khuôn mặt phát hiện được
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Hiển thị khung hình
    cv2.imshow('Phat Hien Khuon Mat', frame)

    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng webcam
cap.release()
cv2.destroyAllWindows()