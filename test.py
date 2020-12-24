cards = {'handCard':False,('kickingCard','slashingCard'):False, 'battleaxCard':False, 'smollfirecard':False, 'fireCard':False, 'bluefireCard':False}


# method to search what skills the player had.
def skillsOfPlayer(nivel):
        count = 1
        for (k,v) in cards.items():
            if(count <= nivel):
                v = True
                cards[k] = v
            count += 1

# moving the cards, just to put the firts card of the player,
# in the midle to help in the display of the cards
def movingCards():
    copy = dict(cards)
    middlePos = len(cards)//2 - 1
    cards.clear()
    count = 1
    for (k,v) in copy.items():
        if(k == 'handCard'):
            holdKey = k
            holdValue = v
        else:
            cards[k] = v

        if(middlePos == count):
            cards[holdKey] = holdValue
        count += 1
    print(cards)
     
def distibutinTheCardsForTheDisplay():
    leftCards = {}
    rightCards = {}
    middlePos = len(cards)//2 -1
    count = 0
    # right cards
    for (k,v) in cards.items():
        if (middlePos > count):
            leftCards[k] = v
        elif (middlePos < count):
            rightCards[k] = v  
        count += 1
    

    # going to reverse the elements of this dictionary
    updateRigth = {}    
    for i in range(len(rightCards)*3):
        if (len(rightCards)==0):
            break
        else:
            count = 0
            for (k, v) in rightCards.items():
                if(count == len(rightCards)-1):
                    updateRigth[k] = v
                count += 1
        del rightCards[k]
    rightCards = updateRigth
    del updateRigth

distibutinTheCardsForTheDisplay()
skillsOfPlayer(2)