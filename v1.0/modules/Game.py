from . import *
import random

class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.topCardPlayer = -1
        self.rank = []
        self.topCard = Card.Card("flowerButtom", "numberButtom")
    def updatePlayers(self, pls):
        self.players = pls
    def license(self):
        cardBank = []
        for i in range(4):
            for j in range(13):
                cardBank.append(Card.make_Card(i, j))
        random.shuffle(cardBank)
        for i in range(52):
            self.players[i%4].getCard(cardBank[i])
        for i in range(4):
            self.players[i].arrange()
    def nextPlayer(self):
        self.turn += 1
        if self.turn >= 4:
            self.turn -= 4
    def lastPlayer(self):
        self.turn -= 1
        if self.turn < 0:
            self.turn += 4
    def getNowPlayer(self):
        return self.players[self.turn]
    def nowPlayerPlayCard(self, card):
        self.topCard = self.players[self.turn].playCard(card)
        self.topCardPlayer = self.turn
    def nowPlayerPlayCard(self, cardIndex):
        self.topCard = self.players[self.turn].playCard(cardIndex)
        self.topCardPlayer = self.turn
    def isPlayerWin(self):
        for i in self.players:
            if len(i.returnAllCards()) == 0:
                return True
    def returnTurn(self):
        return self.turn
    def getTopCard(self):
        return self.topCard
    def isNowPlayerCanPlay(self):
        for i in self.players[self.turn].returnAllCards():
            if not i < self.topCard:
                return True
        return False
    def isNowPlayerGetFreeRound(self):
        if self.turn == self.topCardPlayer:
            return True
        return False
    def resetTopCard(self):
        self.topCard = Card.Card("flowerButtom", "numberButtom")
    def getRank(self):
        for i in self.players:
            self.rank.append(tuple([len(i.returnAllCards()), i.getName()]))
        self.rank.sort()
        return tuple(self.rank)
