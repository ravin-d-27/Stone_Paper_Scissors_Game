import cv2
from ML_model import ML_Selector
import HandTracker as ht
from game import Stone_Paper_Scissors
import time

wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(5, hcam)

detector = ht.Hand_Detector()

tips = [4, 8, 12, 16, 20]
model = ML_Selector("hands_data.csv")
model.run()

player = 0
bot = 0

vals = {
    2: "stone",
    1: "paper",
    0: "scissors"
}

lock = 1
while lock:
    success, img = cap.read()
    img = detector.Discover_Hand(img)
    locs = detector.location(img)

    cv2.putText(img, "Player: {}".format(player), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
    cv2.putText(img, "Bot: {}".format(bot), (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)

    if len(locs) != 0:
        fingers = []

        if locs[tips[0]][1] > locs[tips[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for tip in range(1, 5):
            if locs[tips[tip]][2] < locs[tips[tip] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        val = model.find(fingers)

        obj = Stone_Paper_Scissors()

        if val[0] == 1:
            points = obj.play(val[0] - 1)
            print(points)
            cv2.putText(img, "You: Scissors  Bot: {}".format(vals[points[2]]), (10, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 2)
            time.sleep(1)
        elif val[0] == 2:
            points = obj.play(val[0] - 1)
            print(points)
            cv2.putText(img, "You: Paper  Bot: {}".format(vals[points[2]]), (10, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 2)
            time.sleep(1)
        elif val[0] == 3:
            points = obj.play(val[0] - 1)
            print(points)
            cv2.putText(img, "You: Stone  Bot: {}".format(vals[points[2]]), (10, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 2)
            time.sleep(1)
        else:
            pass

    cv2.imshow("Image",img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
