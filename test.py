cards = {'handCard':False,'kickingCard':False, 'slashingCard':False, 'battleaxCard':False, 'smollfirecard':False, 'fireCard':False, 'bluefireCard':False}


def skillsOfPlayer(nivel):
        for k,v in cards.items():
            print(cards.get(k))
            
skillsOfPlayer(1)