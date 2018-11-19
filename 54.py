from collections import Counter

games = []
values = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
colors = {'C':0,'H':1,'D':2,'S':3}
with open('storage//54_poker.txt','r') as f:
    for line in f:
        cards = line.replace('\n','').split(' ')
        player1 = cards[:5]
        player2 = cards[5:]
        player1 = [[values[i[0]] for i in player1],[colors[i[1]] for i in player1]]
        player2 = [[values[i[0]] for i in player2],[colors[i[1]] for i in player2]]
        games.append([player1, player2])
# games = [game1,game2,game3]
# game1 = [player1, player2]
# player1 = [values, colors]
# values = [1,5,2,7,5]  colors = [0,3,2,2,1]
def value(cards):
    values = Counter(cards[0])
    colors = Counter(cards[1])

    isstraight = sorted(values.keys()) == list(range(min(values.keys()), max(values.keys())+1))
    samesuit = 5 in colors.values()
    # flush
    if samesuit and not isstraight:
        return 500 + max(values.keys())

    maxcounter = 0
    for v in values.values():
        if v > maxcounter:
            maxcounter = v
    # High Card, Straight, Straight Flush, Royal Flush
    if maxcounter == 1:
        if isstraight:
            # Straight Flush, Royal Flush
            if samesuit:
                # Royal Flush
                if min(values.keys()) == 8:
                    return 900
                # Straight Flush
                else:
                    return 800 + max(values.keys())
            # Straight
            else:
                return 400 + max(values.keys())
        # High Card
        else:
            return max(values.keys())
    # One Pair, Two Pairs
    elif maxcounter == 2:
        maxpair = 0
        numberofpairs = 0
        for k,v in values.items():
            if v == 2:
                numberofpairs += 1
                if k > maxpair:
                    maxpair = k
        # One Pair
        if numberofpairs == 1:
            return 100 + maxpair
        # Two Pairs
        else:
            return 200 + maxpair
        
    # Three of a kind, Full House
    elif maxcounter == 3:
        ispair = False
        for v in values.values():
            if v == 2:
                ispair = True

        # Full House
        if ispair:
            return 600 + max([k for k,v in values.items() if v == 3])
        # Three of a kind
        else:
            return 300 + max([k for k,v in values.items() if v == 3])

    # Four of a kind
    else:
        return 700 + max([k for k,v in values.items() if v == 4])
    return 0
    
count = 0
for game in games:
    if value(game[0]) > value(game[1]):
        count += 1
print(count)