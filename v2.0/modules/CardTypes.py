from . import *

class Cards:    #for all the CardType init
    def __init__(self, data):
        self.cards = data
        self.iterAt = 0
    def arrange(self):
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if self.cards[i] < self.cards[j]:
                    self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
    def reverseCards(self):
        self.cards.reverse()
    def getCards(self):
        return self.cards
    def __getitem__(self, index):
        return self.cards[index]
    def __iter__(self):
        return self
    def __next__(self):
        if not self.iterAt == len(self.cards):
            LastIterAt = self.iterAt
            self.iterAt += 1
            return self.cards[LastIterAt]
        else:
            return StopIteration

def isPair(cards):
    if not len(cards) == 2:
        return False
    if cards[0].get_card()[1] == cards[1].get_card()[1]:
        return True
    return False

class Pair:
    def __init__(self, cards):
        cards.arrange()
        self.pair = tuple(cards)
    def __lt__(self, other):
        return self.pair[-1] < other.pair[-1]

def make_Pair(cards):
    return Pair(cards)

_Junko_Rank = {
        [3, 4, 5, 6, 7] : 0,
        [4, 5, 6, 7, 8] : 1,
        [5, 6, 7, 8, 9] : 2,
        [6, 7, 8, 9, 10] : 3,
        [7, 8, 9, 10, 11] : 4,
        [8, 9, 10, 11, 12] : 5,
        [9, 10, 11, 12, 13] : 6,
        [1, 2, 3, 4, 5] : 7
        }

def isJunko(cards):
    if not len(cards) == 5:
        return False
    cards.arrange()
    if cards in _Junko_Rank:
        return True
    return False

class Junko:
    def __init__(self, cards):
        cards.arrange()
        self.junko = cards
        self.junkoNumber = []
        for i in cards:
            self.junkoNumber.append(i.get_card()[1])
        self.junkoRank = _Junko_Rank[self.junkoNumber]
    def __lt__(self, other):
        if self.junkoRank == other.junkoRank:
            if self.junkoRank == 7:
                return self.junko[1] < other.junko[1]
            return self.junko[-1] < other.junko[-1]
        return self.junkoRank < other.junkoRank

def make_Junko(cards):
    return Junko(cards)

def isGourd(cards):
    if not len(cards) == 5:
        return False
    cards.arrange()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        return True
    if cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        return True
    return False

class Gourd:
    def __init__(self, cards):
        cards.arrange()
        self.gourd = {
                "head" : [],
                "tail" : [],
                }
        for i in cards:
            if len(self.gourd["head"]) == 0 and len(self.gourd["tail"]) == 0:
                self.gourd["head"].append(i)
            elif self.gourd["head"][0].get_card()[1] == i.get_card()[1]:
                self.gourd["head"].append(i)
            else:
                self.gourd["tail"].append(i)
        if len(self.gourd["head"]) < len(self.gourd["tail"]):
            self.gourd["head"], self.gourd["tail"] = self.gourd["tail"], self.gourd["head"]
    def __lt__(self, other):
        return self.gourd["head"] < other.gourd["head"]

def make_Gourd(cards):
    return Gourd(cards)

def isQuadrupe(cards):
    if not len(cards) == 5:
        return False
    cards.arrange()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[2] == cards[3]:
        return True
    if cards[1] == cards[2] and cards[2] == cards[3] and cards[3] == cards[4]:
        return True
    return False

class Quadrupe:
    def __init__(self, cards):
        cards.arrange()
        self.quadrupe = {
                "head" : [],
                "tail" : [],
                }
        for i in cards:
            if len(self.quadrupe["head"]) == 0 and len(self.quadrupe["tail"]) == 0:
                self.quadrupe["head"].append(i)
            elif self.quadrupe["head"][0].get_card()[1] == i.get_card()[1]:
                self.quadrupe["head"].append(i)
            else:
                self.quadrupe["tail"].append(i)
        if len(self.quadrupe["head"]) < len(self.quadrupe["tail"]):
            self.quadrupe["head"], self.quadrupe["tail"] = self.quadrupe["tail"], self.quadrupe["head"]
    def __lt__(self, other):
        return self.quadrupe["head"] < other.quadrupe["head"]

def make_Quadrupe(cards):
    return Quadrupe(cards)

def isSFJunko(cards):
    if not len(cards) == 5:
        return False
    SF = cards[0].get_card()[0]
    for i in cards:
        if not i == SF:
            return False
    return isJunko(cards)

class SFJunko:
    def __init__(self, cards):
        self.sfJunko = Junko(cards)
        self.flowerRank = Card.Cmp[cards[0].get_card()[0]]
    def __lt__(self, other):
        if self.flowerRank == other.flowerRank:
            return self.sfJunko < other.sfJunko
        return self.flowerRank < other.flowerRank

def make_SFJunko(cards):
    return SFJunko(cards)

CardTypesIterater = [[isPair, make_Pair], [isGourd, make_Gourd], [isJunko, make_Junko], [isQuadrupe, make_Quadrupe], [isSFJunko, make_SFJunko]] #[Chekcer, Maker]

def toCardType(cards): #type(cards) == list
    lenOfCards = len(cards)
    cards = Cards(cards)
    for i in CardTypesIterater:
        if i[0](cards):
            return i[1](cards)
    if lenOfCards == 1:
        return cards[0]
    return None
