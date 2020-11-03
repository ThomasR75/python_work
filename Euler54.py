#Euler54  Poker Hands
from time import time
start = time()
#read the data
hands = []
handsfile = open("p054_poker.txt", "r")
hands = handsfile.read().replace("\n", ' ').split(" ")
cards = {'2': 2, '3': 3, '4': 4, '5': 5,
         '6': 6, '7': 7, '8': 8, '9': 9,
         'T': 10, 'J': 11, 'Q': 12, 'K': 13,
         'A': 14}
counter = 0
while counter < 20:

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
        player2hand = 20
    else:
        player2hand = 1
    #translate hand into values
    player1values = []
    player2values = []

    for i in player1card:
        player1values.append(cards[i])
    player1values.sort()

    for i in player2card:
        player2values.append(cards[i])
    player2values.sort()
    #check for differences
    diff1 = [player1values[4] - player1values[3], player1values[3] - player1values[2],
             player1values[2] - player1values[1], player1values[1] - player1values[0]]
    diff2 = [player2values[4] - player2values[3], player2values[3] - player2values[2],
             player2values[2] - player2values[1], player2values[1] - player2values[0]]
    #check for straight
    if len(set(diff1)) == 1:
           hand1value = 2000 * player1values[4] * player1hand
    if len(set(diff2)) == 1:
           hand2value = 2000 * player2values[4] * player2hand
    #check for four of a kind
    if player1values[0] == player1values[3] or player1values[1] == player1values[4]:
        hand1value = 1500 * player1values[1]
    if player2values[0] == player2values[3] or player2values[1] == player2values[4]:
        hand2value = 1500 * player2values[1]
    #check for full house
    if (player1values[0] == player1values[2] and player1values[3] == player1values[4]) or\
            (player1values[0] == player1values[1] and player1values[2] == player1values[4]):
        hand1value = 100 * player1values[1] + 100 * player1values[4]
    if (player2values[0] == player2values[2] and player2values[3] == player2values[4]) or\
            (player2values[0] == player2values[1] and player2values[2] == player2values[4]):
        hand2value = 100 * player2values[1] + 100 * player2values[4]


    print(player1card, player2card)
    print(player1suit, player2suit)
    print(player1hand, player2hand)
    print(player1values, player2values)
    print(diff1, diff2)
    print(hand1value, hand2value)
    counter += 10
print(hands[0:20])
end = time()
print("Time: ", end - start)
