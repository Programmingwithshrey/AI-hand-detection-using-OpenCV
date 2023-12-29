import cv2
import keyboard as kb
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand_insta = hand.Hands()
drawLandmarks = mp.solutions.drawing_utils.draw_landmarks

while True:
    Available, frame = video.read()
    if not Available:
        print("cam aint responding - maybe its closed? or disabled access (check settings ofc)")
        break

    frame = frame[:, :, ::-1]

    HandFramePosition = Hand_insta.process(frame)
    frame = frame[:, :, ::-1]
    
    if HandFramePosition.multi_hand_landmarks:
        for landmarks in HandFramePosition.multi_hand_landmarks:
            drawLandmarks(frame, landmarks, hand.HAND_CONNECTIONS) # Hand_Connectionos makrs the points on the hand and connects them together. This is pretty cool
    cv2.imshow("Yoooo hand detection bro", frame)

    if cv2.waitKey(1) and kb.is_pressed("X"):
        break
cv2.destroyAllWindows()
