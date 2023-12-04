# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:59:41 2023

@author: alexp
"""
import timeit
from GameSim import GameSim 
from Algorithems import randomPairing, oneAtATime, refinedPairing
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    while True:
        try:
            numContestents = int(input("How Many Contestants? Selection must be an even, non negative int\n"))
        except ValueError:
            print("Invalid Input, Not an Integer, Please Try Again")
        if numContestents%2 == 1 or numContestents < 0:
            print("\Invalid Input, Integer does not meet criteria")
        else:
            break
    
    while True:
        try:
            trials = int(input("How Many Trials? Selection must be a non negative int\n"))
        except ValueError:
            print("Invalid Input, Not an Integer, Please Try Again")
        if trials%2 == 1 or trials < 0:
            print("\Invalid Input, Integer does not meet criteria")
        else:   
            break
    
    data = generateResults(numContestents, trials)
    
    tupRNG = None
    tupOne = None
    tupRefined = None  
    
    for key in data:
        averageRounds = 0   
        averageTime = 0
        for value in data[key]:
            averageRounds += value[0]
            averageTime += value[1]
    
        averageRounds = averageRounds//trials
        averageTime = averageTime//trials
    
        if not tupRNG:
            tupRNG = "({},{})".format(averageRounds, averageTime)
            
        elif not tupOne:
            tupOne = "({},{})".format(averageRounds, averageTime)
            
        elif not tupRefined:
            tupRefined =  "({},{})".format(averageRounds, averageTime) 
            
        
    
    
    print("=|="*32)
    print("-"*96)

    
    print("{:^17}{:<2}{:^9}{:<2}{:^22}{:<1}{:^22}{:<1}{:^20}".format("Trials", "|", "Players", "|", "Random", "|", "One At A Time", "|", "Refined Pairing"))
    print("- -"*32)
    print('                 |          |      Rounds, Time     |     Rounds, Time     |    Rounds, Time     ')
    print("-"*96)
    
    
    
    lines = 0
    
    print('                 |          |                       |                      |    ')
    lines+=1
    print("{:^17}{:<1}{:^10}{:3}{:^19}{:^5}{:^18}{:^5}{:^15}".format(trials, "|", numContestents, "|", tupRNG, "|", tupOne, "|", tupRefined))
    print('                 |          |                       |                      |    ')
    if lines%2==0:  
        print("-"*90)
    
    




#Possible graphing of data to show round distribution 
'''
def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid Input, Not an Integer, Please Try Again")
            continue

        if value % 2 == 1 or value < 0:
            print("Invalid Input, Integer does not meet criteria")
        else:
            break

    return value

def generate_results(numContestents=16, trials=50):
    data = {"randomPairing": list(), "oneAtATime": list(), "refinedPairing": list()}

    for func in data:
        for _ in range(trials):
            game = GameSim(numContestents)
            data[func].append(timeFunc(func, game))

    return data

def plot_results(data):
    players = list(data.keys())
    rounds_data = [np.mean(data[player]) for player in players]
    std_dev_data = [np.std(data[player]) for player in players]

    plt.bar(players, rounds_data, yerr=std_dev_data, capsize=5)
    plt.xlabel('Algorithm')
    plt.ylabel('Average Rounds')
    plt.title('Average Rounds for Different Algorithms')
    plt.show()

    numContestents = get_input("How Many Contestants? Selection must be an even, non-negative int\n")
    trials = get_input("How Many Trials? Selection must be a non-negative int\n")

    data = generate_results(numContestents, trials)

    plot_results(data)
'''    
    
    
def generateResults(numContestents = 16, trials = 50):
    
    data = {randomPairing:list(), oneAtATime:list(), refinedPairing:list()}
    
    #Stores data for 3 algorithems
    for func in data:
        #Stores data for 1 algorithem at a timez
        for i in range(trials):
            game = GameSim(numContestents)
            
            data[func].append(timeFunc(func, game))
            
    return data
    
    
def timeFunc(func, game):
#Takes a function, and list and finds time taken to run, and # of swaps, returing them in a tuple
    start = timeit.default_timer()
    rounds = game.runSim(func)
    return (rounds, round(100000*(timeit.default_timer() - start), 4))    
    
    
    
    
if __name__ == "__main__":
    main()