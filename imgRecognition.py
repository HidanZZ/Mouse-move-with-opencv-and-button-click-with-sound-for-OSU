import cv2

cap = cv2.VideoCapture(0)
palm_cascade = cv2.CascadeClassifier("hand.xml")

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    palms = palm_cascade.detectMultiScale(gray_frame, 1.2, 3)
    for (x, y, w, h) in palms:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('pic.jpg',frame)
    cv2.imshow('frame', frame)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("fps:", fps)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
