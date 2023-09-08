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

vals = {
    2: "stone",
    1: "paper",
    0: "scissors"
}
player = 0
bot = 0

print()
x = int(input("Enter the No. of Points: "))

while (player<x and bot<x):
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

            print("You: Scissors  \nBot: {}\n\n".format(vals[points[2]]))

            time.sleep(2)
            player+=points[1]
            bot+=points[0]
            cap.release()
            cv2.destroyAllWindows()
            cap = cv2.VideoCapture(0)
            cap.set(3, wcam)
            cap.set(5, hcam)
            continue

        elif val[0] == 2:
            points = obj.play(val[0] - 1)

            print("You: Paper  \nBot: {}\n\n".format(vals[points[2]]))
            time.sleep(2)
            player+=points[1]
            bot+=points[0]
            cap.release()
            cv2.destroyAllWindows()
            cap = cv2.VideoCapture(0)
            cap.set(3, wcam)
            cap.set(5, hcam)
            continue

        elif val[0] == 3:
            points = obj.play(val[0] - 1)
            print("You: Stone  \nBot: {}\n\n".format(vals[points[2]]))
            
            time.sleep(2)
            player+=points[1]
            bot+=points[0]
            cap.release()
            cv2.destroyAllWindows()
            cap = cv2.VideoCapture(0)
            cap.set(3, wcam)
            cap.set(5, hcam)
            continue

        if (player==x or bot==x):
            break

    cv2.imshow("Image", img)
    cv2.waitKey(1)

if (bot>player):
    print("You Lost, Bot won the Match!")
    print("Your Score: ", player)
    print("Bot Score: ", bot)
elif (bot==player):
    print("Its a Tie game")
    print("Your Score: ", player)
    print("Bot Score: ", bot)
else:
    print("Congratulations! You Won the game!")
    print("Your Score: ", player)
    print("Bot Score: ", bot)
