from modules import *
import random
import os

rankList = ["Gold", "Silver", "Bronze", "unRated"]

def getInput(T, msg="", endMsg=""):
    try:
        print(msg, end=endMsg)
        ipt = input()
        ipt = T(ipt)
        return ipt
    except ValueError:
        return getInput(T, msg, endMsg)
def printList(List, step=" ", end="\n"):
    for i in List:
        print(formatMsg.format(i), end=step)
    print(end, end="")
def printCards(cards):
    for i in range(len(cards)):
        print("({}){}".format(i+1, cards[i]), end=" ")
    print("({}) Pass".format(len(cards)+1))
def inputCards(nowPlayer): #return list
    try:
        cards = []
        Legal = False
        while not Legal:
            Legal = True
            ipt = getInput(str, msg="Chose the cards you to play : ", endMsg='\n')
            cards = list(map(int, ipt.strip().split()))
            for i in cards:
                if not (0 <= i and i <= len(nowPlayer.returnAllCards())):
                    Legal = False
        return cards
    except ValueError:
        return inputCards(nowPlayer)

if __name__ == "__main__":
    game = Game.Game()
    playerNumber = getInput(int, msg="Enter Player Number : ", endMsg="")
    playerlist = []
    for i in range(playerNumber):
        playerName = getInput(str, msg="Enter Player{}'s Name : ".format(i+1), endMsg="")
        playerlist.append(Player.Player(playerName))
    for i in range(len(playerlist), 4, 1):
        playerlist.append(Player.Player("Computer"+str(i)))
    game.updatePlayers(playerlist)
    game.license()

    while not game.isPlayerWin():
        nowPlayer = game.getNowPlayer()
        allCards = nowPlayer.returnAllCards()
        if game.isNowPlayerGetFreeRound():
            game.resetTopCard()
            print("{} got a Free Round!".format(nowPlayer.getName()))
        if game.returnTurn() < playerNumber:
            printCards(allCards)
            cards = inputCards(nowPlayer)
            if len(card) == 1 and cards[0] == len(allCards):
                print("{} passed".format(nowPlayer.getName()))
                game.nextPlayer()
                continue
            isPassed = False
            while allCards[playCardIndex] < game.getTopCard():
                print("Please pick a bigger one or pass")
                playCardIndex = inputCards(nowPlayer)
                if playCardIndex == len(allCards):
                    print("{} passed".format(nowPlayer.getName()))
                    game.nextPlayer()
                    isPassed = True
                    break
            if isPassed:
                continue
        else:
            if not game.isNowPlayerCanPlay():
                print("{} passed".format(nowPlayer.getName()))
                game.nextPlayer()
                continue
            playCardIndex = random.randint(0, len(allCards)-1)
            while allCards[playCardIndex] < game.getTopCard():
                playCardIndex = random.randint(0, len(allCards)-1)
        print("{} played {}".format(nowPlayer.getName(), allCards[playCardIndex]), end="")
        cardLeft = game.getNowPlayer().returnAllCards()
        game.nowPlayerPlayCard(playCardIndex)
        if len(cardLeft) == 0:
            print(" and played all cards!!!")
            break
        elif len(cardLeft) == 1:
            print(", has 1 card left!")
        else:
            print(", has {} cards left".format(len(cardLeft)))
        game.nextPlayer()
    rank = game.getRank()
    rankAt = -1
    lastCardLeft = -1
    print("------------")
    for cl, name in rank:
        if cl != lastCardLeft:
            rankAt += 1
        lastCardLeft = cl
        print("{} is {}".format(name, rankList[rankAt]))
    os.system("pause")
