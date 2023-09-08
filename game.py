import random

class Stone_Paper_Scissors():

    def __init__(self):
        self.vals = {
            2:"stone",
            1:"paper",
            0:"scissors"
        }

    def play(self, h_ans):
        # [bot_ans, h_ans]
        bot_ans = random.randint(0,2)
        if (bot_ans == h_ans ):
            return [0,0,bot_ans] 
        else:
            if (bot_ans == 0 and h_ans == 1): # Scissors and paper
                return [1,0,bot_ans]
            elif (bot_ans == 0 and h_ans == 2): # Scissors and Stone
                return [0,1, bot_ans]
            elif (bot_ans == 1 and h_ans == 0): # Paper and Scissors
                return [0,1,bot_ans]
            elif (bot_ans == 2 and h_ans == 0): # Stone and Scissors
                return [1,0,bot_ans]
            elif (bot_ans == 1 and h_ans == 2): # Paper and Stone
                return [1,0,bot_ans]
            elif (bot_ans == 2 and h_ans == 1): # Stone and Paper
                return [0,1,bot_ans]
            else:
                pass

