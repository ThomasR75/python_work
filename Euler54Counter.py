#Euler54  Poker Hands
from time import time
from collections import Counter
start = time()
#read the data
hands = []
player1count = 0
handsfile = open("p054_poker.txt", "r")
hands = handsfile.read().replace("\n", ' ').split(" ")
cards = {'2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9,
         'T': 10, 'J': 11, 'Q': 12, 'K': 13,
         'A': 14}
counter = 0
while counter < 20:
    hand1value = 0
    hand2value = 0
    #allocate cards to players 5x5
    player1 = hands[counter:counter+5]
    player2 = hands[counter+5:counter+10]
    #print(player1)
    #print(player2)
    player1suit = ""
    player1card = ""
    player2suit = ""
    player2card = ""
    hand1value = 0
    hand2value = 0
    #determine suit and hand for players
    for i in player1:
        player1suit += i[1:]
        player1card += i[:1]
    for i in player2:
        player2suit += i[1:]
        player2card += i[:1]
    #check of players have all in one suit
    if len(set(player1suit)) == 1:
        player1hand = 20
    else:
        player1hand = 1

    if len(set(player2suit)) == 1:
        player2hand = 400
    else:
        player2hand = 1

    #use Counter to count cards
    player1cards = Counter(player1card)
    print(player1cards)
    singles = [k for k, v in player1cards.items() if v == 1]
    print(singles)
    doubles = [k for k, v in player1cards.items() if v == 2]
    print(doubles)


    print(player1card, player2card)
    print(player1suit, player2suit)
    print(player1hand, player2hand)

    counter += 10
print(hands[0:20])
end = time()
print("Time: ", end - start)
