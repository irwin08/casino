import deck
import card

class Blackjack:


    def __init__(self):
        self.dealerHand = []
        self.hiddenCard = None
        self.playerHand = []
        self.mainDeck = deck.Deck()
        self.gameover = False
        self.finished = False # reveal card

    def deal(self):
        self.mainDeck.shuffle()
        self.playerHand.append(self.mainDeck.draw())
        self.hiddenCard = self.mainDeck.draw() 
        self.playerHand.append(self.mainDeck.draw())
        self.dealerHand.append(self.mainDeck.draw())

    def printState(self):
        total = 0
        if self.finished:
            total = self.hiddenCard.face
        dealerString = ""
        if self.finished:
            dealerString = str(self.hiddenCard.suit) + "-" + str(self.hiddenCard.face)
        if not self.finished:
            dealerString = "#-#"
        for c in self.dealerHand:
            dealerString += " "
            dealerString += str(c.suit) + "-" + str(c.face)

            if c.face >= 10:
                total += 10
            elif c.face == 1:
                if (total + 11) < 22:
                    total += 11
                else:
                    total += 1
            else:
                total += c.face
            

        dealerString += " Total: " + str(total)
        print("Dealer:")
        print(dealerString)

        totalp = 0
        playerString = ""
        for c in self.playerHand:
            playerString += " "
            playerString += str(c.suit) + "-" + str(c.face)

            if c.face >= 10:
                totalp += 10
            elif c.face == 1:
                if (totalp + 11) < 22:
                    totalp += 11
                else:
                    totalp += 1

            else:
                totalp += c.face
        playerString += " Total: " + str(totalp)
        print("Player:")
        print(playerString)

    def checkGameover(self):
        total = 0
        for c in self.playerHand:
            if c.face >= 10:
                total += 10
            elif c.face == 1:
                if (total + 11) < 22:
                    total += 11
                else:
                    total += 1
            else:
                total += c.face

        if total > 21:
            self.gameover = True

    def getDealerTotal(self):
        total = self.hiddenCard.face
        for c in self.dealerHand:
            if c.face >= 10:
                total += 10
            if c.face == 1:
                if (total + 11) < 22:
                    total += 11
                else:
                    total += 1
            else:
                total += c.face
        return total
                
    def hit(self):
        self.playerHand.append(self.mainDeck.draw())
