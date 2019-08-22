class card:
    def __init__(self, s, f):
        self.setSuit(s)
        self.setFace(f)


    def setSuit(self, s):
        # 0 - Diamonds
        # 1 - Clubs
        # 2 - Hearts
        # 3 - Spades
        self.suit = s

    def setFace(self, f):
        # 1-10 - Ace through 10
        # 11 - Jack
        # 12 - Queen
        # 13 - King
        self.face = f
