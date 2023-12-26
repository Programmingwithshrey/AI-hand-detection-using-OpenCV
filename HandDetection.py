import cv2
import keyboard as kb

cap = cv2.VideoCapture(0)

while True:
    Available, frame = cap.read()
    if not Available:
        print("cam aint responding - maybe its closed? or disabled access (check settings ofc)")
        break

    cv2.imshow("Yoooo hand detection bro", frame)

    if cv2.waitKey(1) and kb.is_pressed("X"):
        break

cv2.destroyAllWindows()
