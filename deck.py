import card
import random

class Deck:
    def __init__(self):
        # we will create a standard 52 deck card
        self.deck = []
        self.play = []
        self.discard = []
        # loop suits
        for s in range(0,4):
            # loop values
            for v in range(1,14):
                self.deck.append(card.card(s,v))


    def draw(self):
        if not self.deck:
            return None
        else:
            d = self.deck.pop()
            self.play.insert(0,d)
            return d

    def discard(self, c):
        if c in self.deck:
            self.deck.remove(c)
            self.discard.insert(0,c)
        elif c in self.play:
            self.play.remove(c)
            self.discard.insert(0,c)


    def shuffle(self):
    # shuffles without play deck
        tempDeck = self.deck + self.discard
        random.shuffle(tempDeck)
        self.deck = tempDeck
        self.discard = []

    def shuffleAll(self):
    # includes play deck in shuffle
        tempDeck = self.deck + self.play + self.discard
        random.shuffle(tempDeck)
        self.deck = tempDeck
        self.play = []
        self.discard = []
        
                
    def printDeck(self):
        for card in self.deck:
            print(str(card.suit) + "-" + str(card.face))
    
