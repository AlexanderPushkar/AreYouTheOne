
"""
@author: alexp
"""
import random

def refinedPairing(game, contestents):
    '''Swaps one pair at a time and checks how it affects the total pairs correct'''
    foundPairs = set()
    unusedMales = list(contestents[0])
    unusedFemales = list(contestents[1])
    previousCorrect = -1
    currentCorrect = -1

    while True:
        if len(unusedMales) < 3:
            if len(unusedMales) == 0:
                return foundPairs
            elif len(unusedMales) == 1:
                foundPairs.add((unusedMales[0], unusedFemales[0]))
                return foundPairs
            elif len(unusedMales) == 2:
                pair1 = (unusedMales[0], unusedFemales[1])
                pair2 = (unusedMales[1], unusedFemales[0])

                if game.checkPair(pair1):
                    foundPairs.add(pair1)
                    foundPairs.add(pair2)
                else:
                    foundPairs.add((unusedMales[0], unusedFemales[0]))
                    foundPairs.add((unusedMales[1], unusedFemales[1]))

                return foundPairs

        index1, index2 = random.sample(range(len(unusedMales)), 2)
        temp1 = (unusedMales[index1], unusedFemales[index1])
        temp2 = (unusedMales[index2], unusedFemales[index2])
            
        new1 = (temp1[0], temp2[1])
        new2 = (temp2[0], temp1[1])

        if game.checkPair(new1):
            foundPairs.add(new1)
            unusedMales.remove(new1[0])
            unusedFemales.remove(new1[1])
        elif game.checkPair(new2):
            foundPairs.add(new2)
            unusedMales.remove(new2[0])
            unusedFemales.remove(new2[1])

        contestentPairs = [(m, f) for m, f in zip(unusedMales, unusedFemales)]
        yield foundPairs.union(set(contestentPairs))

        previousCorrect = currentCorrect
        currentCorrect = game.checkAllPairs(foundPairs.union(set(contestentPairs)))





def oneAtATime(game, contestents):
    '''Algorithem that guess randomly, but also guess if pair is correct and remove from pool for randomly guessing'''
    foundPairs = set()
    unusedMales = list(contestents[0])
    unusedFemales = list(contestents[1])
    while True:
        random.shuffle(unusedFemales)
        guessedPairs = set()
        for male, female in zip(unusedMales, unusedFemales):
            guessedPairs.add((male,female))
            
        yield foundPairs.union(guessedPairs)
        
        randomPair = random.choice(tuple(guessedPairs))
        if game.checkPair(randomPair):
            unusedMales.remove(randomPair[0])
            unusedFemales.remove(randomPair[1])
            foundPairs.add(randomPair)
    



def randomPairing(game, contestents):
    '''Algorithem that uses compeltly rarndom pair generation untill it hits all correct pairs'''
    femaleList = list(contestents[1])
    #Randomizes list of female, then pairs together contestents and checks if guess corrrect
    while True:    
        random.shuffle(femaleList)
        new_couples = set()
        for male, female in zip(contestents[0], femaleList):
            new_couples.add((male, female))
    
        
        yield new_couples
        
