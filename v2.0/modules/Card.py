from . import *

Cmp = {
        "flowerButtom" : -1,
        "\u2663" : 0,
        "\u2666" : 1,
        "\u2665" : 2,
        "\u2660" : 3,
        "numberButtom" : -1,
        "3" : 0,
        "4" : 1,
        "5" : 2,
        "6" : 3,
        "7" : 4,
        "8" : 5,
        "9" : 6,
        "10" : 7,
        "11" : 8,
        "12" : 9,
        "13" : 10,
        "1" : 11,
        "2" : 12
        }

_flower_bank_ = ["\u2663", "\u2666", "\u2665", "\u2660"]
_number_bank_ = ["3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "1", "2"]

class Card:
    def __init__(self, _flower, _number):
        self.flower = _flower
        self.number = _number
    def get_card(self):
        return self.flower, self.number
    def __lt__(self, other):
        if Cmp[self.number] == Cmp[other.number]:
            return Cmp[self.flower] < Cmp[other.flower]
        return Cmp[self.number] < Cmp[other.number]
    def __str__(self):
        return self.flower + self.number

def make_Card(flower = 0, number = 0): #generate by card rank
    return Card(_flower_bank_[flower], _number_bank_[number])
def debug_flower_bank_():
    print(_flower_bank_)
