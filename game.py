import random

class Stone_Paper_Scissors():

    def __init__(self):
        self.vals = {
            0:"stone",
            1:"paper",
            2:"scissors"
        }

    def play(self, h_ans):
        # [bot_ans, h_ans]
        ans = random.randint(0,2)
        bot_ans = self.vals[ans]

        if (bot_ans == h_ans ):
            return [0,0] 
        else:
            if (bot_ans == 0 and h_ans == 1):
                return [0,1]
            elif (bot_ans == 0 and h_ans == 2):
                return [1,0]
            elif (bot_ans == 1 and h_ans == 0):
                return [1,0]
            elif (bot_ans == 2 and h_ans == 0):
                return [0,1]
            elif (bot_ans == 1 and h_ans == 2):
                return [0,1]
            elif (bot_ans == 2 and h_ans == 1):
                return [1,0]

