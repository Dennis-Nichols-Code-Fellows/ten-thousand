import random


class GameLogic:

    def calculate_score(self, roll):
        roll_dict = {}

    @staticmethod
    def roll_dice(number_dice):
        roll = []
        for i in range(number_dice):
            roll.append(random.randint(1, 6))
        return tuple(roll)






