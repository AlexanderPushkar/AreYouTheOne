
"""
@author: alexp
"""

import unittest 
from ContestentClass import Contestent
from GameSim import GameSim
from MatchMaker import getScore
from Algorithems import randomPairing, oneAtATime, refinedPairing


class testContestent(unittest.TestCase):
                  
    
    
    def testContestentGen(self):
        
        pass
            
    def testGameSim(self):
        
        pass
    
    def testMatchMaker(self):
        male1 = Contestent(0)
        female1 = Contestent(1)
        print(male1)
        print(female1)
        print(getScore(male1, female1))
        pass
    
    def testAlgorithems(self):
        Game1 = GameSim()
        print("Random Pairing")
        print("\t{}".format(Game1.runSim(randomPairing)))
        print("One At A Time Pairing")
        print("\t{}".format(Game1.runSim(oneAtATime)))
        print("Refined Pairing")
        print("\t{}".format(Game1.runSim(refinedPairing)))
        pass

 
unittest.main()
        
