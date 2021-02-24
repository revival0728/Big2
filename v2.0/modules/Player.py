from . import *

class Player:
    def __init__(self, _name):
        self.cards = []
        self.name = _name
    def arrange(self):
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if self.cards[i] < self.cards[j]:
                    self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def playCard(self, card):
        mid, l, r = 0, 0, len(self.cards)
        while l <= r:
            mid = (l+r) / 2
            if self.cards[mid] == card:
                break
            elif self.cards[mid] < card:
                l = mid+1
            else:
                r = mid-1
        ret = self.cards[mid]
        del self.cards[mid]
        return ret
    def playCard(self, cardIndex):
        ret = self.cards[cardIndex]
        del self.cards[cardIndex]
        return ret
    def getCard(self, card):
        self.cards.append(card)
    def returnAllCards(self):
        return self.cards
    def getName(self):
        return self.name
