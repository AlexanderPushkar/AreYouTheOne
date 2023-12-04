
"""
@author: alexp
"""

from ContestentClass import Contestent
from MatchMaker import matchCouples


class GameSim:
    '''Used to simulate game'''    
    
    
    def __init__(self, numContestents = 16):
        '''Initalizes parameter of optional numContestents that defaults to 20, allows list of contestents if desired'''
        if numContestents % 2 == 1:
            raise ValueError("Number Of Contestents Must Be Even")
        
        #Index 0 is males, Index 1 is Females
        contestents = [list(), list()]
        for i in range(numContestents):
            contestents[i%2].append(Contestent(i%2))
            
        self._contestents = contestents 
        #matchedCouples stores (male, female) tuple in set
        self._matchedCouples = matchCouples(self._contestents)
        
    
    def runSim(self, algorithem):        
        '''Runs actual sim, allows you to select algorithem that is used to run, take name of algorithem, and returns # of rounds'''
        round = 0
        for answer in algorithem(self, self._contestents):
            round+=1
            if self.guessAnswer(answer):
                return round
        #print(round)
        return round
        

    
    def guessAnswer(self, answer):
        return set(answer) == self._matchedCouples
            
    
    def checkPair(self, pair):
        '''Checks if one pair is correct and returns false or true'''
        return pair in self._matchedCouples
        
        
    def checkAllPairs(self, currentCouples):
        '''Checks all current pairs to see how many are correctly matched'''
        correctCouples = 0
        for couple in currentCouples:
            if couple in self._matchedCouples:
                correctCouples += 1 
        return correctCouples
                
    
    def __str__(self):
        '''Used for debugging purposes '''
        print("Males")
        for x in self._contestents[0]:
            print("\t{}".format(x.getName()))
        print("Females")
        for x in self._contestents[1]:
            print("\t{}".format(x.getName()))
        print("\nCouples:")
        for x in self._matchedCouples:
            print("\t{}, {}".format(x[0].getName(), x[1].getName()))
        return ""
        #return "{}\n{}".format(self._contestents[0], self._contestents[1])