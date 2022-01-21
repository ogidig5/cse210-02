import random

class Roll_user:

    def __init__(self):
        self.first_dice = ""
        self.second_dice = ""
        self.third_dice = ""
        self.fourth_dice = ""
        self.fifth_dice = ""

    def roll_dice(self):
        print(f"You rolled: {self.fifth_dice} {self.second_dice} {self.third_dice} {self.fourth_dice} {self.first_dice}")

class Scoring:

    def __init__(self, number):
        self.number = number
        self.score = int(0)

    def score_dice(self):
        if self.number == 1:
            self.score =  100
        elif self.number == 5:
            self.score = 50
        else:
            self.score = 0

def main():
    roll_score = int(0)
    total_score = int(0)
    roll_user = Roll_user()
    print("Welcome to the dice game!")
    rolling_dice = input("Roll dice? (y/n) ")
    while rolling_dice == "y":
        roll_user.first_dice = random.randint(1,6)
        roll_user.second_dice = random.randint(1,6)
        roll_user.third_dice = random.randint(1,6)
        roll_user.fourth_dice = random.randint(1,6)
        roll_user.fifth_dice = random.randint(1,6)
        roll_user.roll_dice()
        roll_score = int(0)
        scoring = Scoring(roll_user.first_dice)
        scoring.score_dice()
        roll_score += scoring.score
        scoring = Scoring(roll_user.second_dice)
        scoring.score_dice()
        roll_score += scoring.score
        scoring = Scoring(roll_user.third_dice)
        scoring.score_dice()
        roll_score += scoring.score
        scoring = Scoring(roll_user.fourth_dice)
        scoring.score_dice()
        roll_score += scoring.score
        scoring = Scoring(roll_user.fifth_dice)
        scoring.score_dice()
        roll_score += scoring.score
        if roll_score != 0:
            total_score += roll_score
            print(f"You scored {total_score} points!")
            print()
            rolling_dice = input("Roll dice? (y/n) ")
        else:
            rolling_dice = "n"
            print("You didn't score anything! The game is over.")
            print()
            

if __name__ == "__main__":
    main()