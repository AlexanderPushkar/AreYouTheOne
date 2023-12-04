
"""
@author: alexp
"""
#=-=-=-=-=-=-=-=-
'''
High Level

Each couple given compatability score:
    Important to understand A->B attraction is different then B->A, study this is based off
    indicates how different genders had different reactions, like how for females shared field 
    had almost no impact on likely hood to say yes, while for men it increased odds by nearly 1.7% and
    indicating a strong relationship. Also each individual has attributes they desire in another person
    which are different then their own and the attributes the other person desires. As such each players
    attraction to the other is calucated seperatly and averaged, with a certain weight given for the difference 
    as the closer a pairs "valued' the other the more likely they were to be compatiable. IE A->B is 96 while B->A is 30,
    the average 63, but due to the very large one sidedness of this, this would be a fairly inaccurate score so a weight of 
    somekind, in this case (A+B/2) - |A-B|^(3/4). (Arbitarily chosen). In our A,B example this 63 - 23.15  = 39.85. A much 
    more representative score. The smaller the differnce in scoring the smaller the weight that is applied.
    
Once each couple given a compatability score:
    Couple with highest score added to list, then next highest of avalible, etc cetera untill all contestents are paired.
    This system is not perfect as it will occasionaly take some individuals most compatiable and leave them with second or third.
    But unfortuantly the contestents are all that are given to work with, so its either settle with about a 50% good match rate, or
    match all contestents with a mediocare pariing and not their best to ensure that all contestents try to mostly stay above a certain
    compatability score, but frankly at that point I may as well just make a whole on dating app. 
'''
#=-=-=-=-=-=-=-=-



import math

def matchCouples(contestents):
    '''Returns set of tuple pairs (male, femaile) showing best pairs, after given List of 2 sets of females and males'''
    scoreValues = dict()
    matchedCouples = set()
    #Each male 
    for male in contestents[0]:
        scoreValues[male] = list()
        for female in contestents[1]:
            scoreValues[male].append((female, getScore(male, female)))
        
    for male in scoreValues:
        max = (None, -1)
        for score in scoreValues[male]:
            if not any(score[0] in tup for tup in matchedCouples):
                if score[1] > max[1]:
                    max = score
        matchedCouples.add((male, max[0]))
    return matchedCouples
                
                
                
def getScore(male, female):    
    '''Takes male and female contestent and finds compatability score'''
    maleScore = 0 
    femaleScore = 0
    
    #Field nearly 3x more deciding factor for males then females
    if male.getFeild() == female.getFeild():
        maleScore += 6
        femaleScore += 2


    #Race was shown to be more important for females then male on average ever so slightly
    if male.getRace() == female.getRace():
        maleScore += 4 + ((male.getImprace()-5)*1.2 )
        femaleScore += 5 + ((female.getImprace()-5)*2)


    #Religion overall was found to be very small impact, uses modifer of Importance of religion
    #to affect score 
    if male.getReligion() == female.getReligion():
        maleScore += 2 + ((male.getImprelig()-5)*0.4)
        femaleScore += 3 + ((female.getImprelig()-5)*0.6)
   
    
   #Finds 3 * (difference / 20000), then uses sigmoid function 1/(1+e^(Income/20000 - 5)) to give larger incomes more weight as study showed
    #That while smaller difference in income was the larger factor, higher income of the partner also did have a noticable affect on
    #likely hood to say yes.
    maleScore += 7*(abs(female.getIncome() - male.getIncome())//20000) * (1/(1 + math.exp((female.getIncome()//20000 -5))))
    femaleScore += 7*(abs(male.getIncome() - female.getIncome())//20000) * (1/(1 + math.exp((male.getIncome()//20000 -5))))


    #Generaly the more sociacble/outgoing pair is the more likely to get along
    maleScore += 7 - abs(male.getGoesOut() - female.getGoesOut())
    femaleScore += 7 - abs(female.getGoesOut() - female.getGoesOut())
 
    
 #Assigned for below calcs 
    maleAttr = male.getAttributeDistribution().values()
    femaleAttr = male.getAttributeDistribution().values()
    
    maleDesiredAttr = male.getAttributeDistribution()
    femaleDesiredAttr = female.getAttributeDistribution()
    
    maleIntrests = male.getIntrests().values()
    femaleIntrests = female.getIntrests().values()
    
    
    #Find difference in intrests for m and f, then subtracts from max of 170, 17 x 10. 
    #Divideas final value by 17
    intrestDifference = 0
    for mIntrests, fIntrests in zip(maleIntrests, femaleIntrests):
        intrestDifference += abs(mIntrests - fIntrests) 
    
    
    #Both males and females selected partner similerly w/ regards to intrests
    maleScore += intrestDifference / 30 * (0.01 * maleDesiredAttr["Shared Intrests"])
    femaleScore += intrestDifference / 30 * (0.01 * femaleDesiredAttr["Shared Intrests"])

    for fA,mDA in zip(femaleAttr, maleDesiredAttr.values()):
            maleScore += (100 - abs(fA-mDA)) * 0.1

    for mA,fDA in zip(maleAttr, femaleDesiredAttr.values()):
            femaleScore += (100 - abs(mA-fDA)) * 0.1
    

    return (((maleScore + femaleScore) / 2) - math.pow((abs(maleScore - femaleScore)), 0.75))
    
    