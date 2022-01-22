'''
Authors: Dan Allred, George Ogidi(Team 04),
Edit 1/22/2022 10:08am EST. - DA - original commit
'''

import random
# To create a python class, use the keyword 'class'
# Use the __init__() function to assign values to object properties


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __gt__(self, comparing_card):
        result = self.value > comparing_card.value
        return result

    def __lt__(self, comparing_card):
        result = self.value < comparing_card.value
        return result

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            # Ace, Jack, queen and King need comparible. or we could just name them 1, 11, 12, 13
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for n in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, n)
            self.cards[n], self.cards[r] = self.cards[r], self.cards[n]

    def drawCard(self):
        return self.cards.pop()


class Person(object):
    def __init__(self):
        self.hand = []

    def __gt__(self, comparing_obj):

        result = self.hand[-1] > comparing_obj.nextcard[-1]
        return result

    def __lt__(self, comparing_obj):

        result = self.hand[-1] < comparing_obj.nextcard[-1]
        return result

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def show(self):
        for card in self.hand:
            card.show()


class NextCard(object):
    def __init__(self):
        self.nextcard = []

    def draw(self, deck):
        self.nextcard.append(deck.drawCard())
        return self

    def show(self):
        for card1 in self.nextcard:
            card1.show()


deck = Deck()
deck.shuffle()

human = Person()
playerHand = human.draw(deck)

newcard = NextCard()
nextCard = newcard.draw(deck)


play = input("Do you want to play High/Low? Y or N? ")
while play.lower() == "y":
    card = playerHand
    print("The current card is: ", str(card.show()))
    guess = input("Guess H for high or L for low.")
    if guess.lower() == "h":
        if card > nextCard:
            print(f"correct! The the card is {card.show()}")
            play = input("Play again? Y or N? ")

        if card < nextCard:
            print(f"You lost! The card was {nextCard.show()}")
            play = input("Play again? Y or N? ")

    if guess.lower() == "l":
        if card > nextCard:
            print(f"You lost! card was {nextCard.show()}")
            play = input("Play again? Y or N? ")

        if card < nextCard:
            print(f"correct! The the card is {nextCard.show()}")
else:
    print("The game is over.")
