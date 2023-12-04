# Contestent Class
import uuid
import names
import random


class Contestent:
    
    

    def _generateAttributeScores(self):
        '''Distributes 100 points into list of length 6, with each index corsponding to attribute'''
        attributeValsTemp = []
        for i in range (6):
            attributeValsTemp.append(random.random())


        attributeVals = []
        for i in range(5):
            attributeVals.append(int(1 + attributeValsTemp[i-1]*94.0/sum(attributeValsTemp)))
        attributeVals.append(100-sum(attributeVals))    
    	
        #-=- Index to Attribute -=-
        #0 - Attractive		
        #1 - Sincere		
        #2 - Intelligent		
        #3 - Fun			
        #4 - Ambitious		
        #5 - Shared Interests5
        attributeDict = {"Attractive": attributeVals[0], "Sincere": attributeVals[1], "Intelligent":attributeVals[2],
                         "Fun": attributeVals[3], "Ambitious": attributeVals[4], "Shared Intrests": attributeVals[5]}
    

        return attributeDict
        

    def _generateIntrestList(self):
        '''Populates and returns dictionary of intrests with values from 1-10}'''
        intrestListDict = {"Sports":0, "TVSports":0, "Excersize":0, "Dining":0, "Mueseums":0,
    					   "Arts":0, "Hiking":0, "Gaming":0, "Clubbing":0, "Reading":0, "TV":0,
    					   "Theater":0, "Movies":0, "Concerts":0, "Music":0, "Shopping":0, 
    					   "Yoga":0}
        for key in intrestListDict:
            intrestListDict.update([(key, random.randrange(1, 10))])

        return intrestListDict

    #Find better way to do this
    #Possibly make some values based on prob distribution 
    #Cannot use random.randrange() as for some reason values set as nonmutable and therefore 
    #permuate across multiple user generations causing repeat values
    def __init__(self, gender = None, name = None, age = None, height = None, feild = None, 
                 race = None, imprace = None, imprelig = None, religion = None,
                 income = None, goesOut = None, career = None, intrests = None,
                 attributeDistribution = None, desiredAttributeDistribution = None):
        
    
        if gender is None:
            self._gender = random.randrange(0,1)
        else:
            self._gender = gender
        
        if name is None:
            if self._gender == 0:
                self._name = names.get_full_name(gender = 'male')
            else:
                self._name = names.get_full_name(gender = 'female')
        else:
            self._name = name
        
        if age is None:
            self._age = random.randrange(18,35)
        else:
            self._age = name
        
        if height is None:
            self._height = random.randrange(60, 74)
        else:
            self._height = height
        
        if feild is None:
            self._feild = random.randrange(1, 18)
        else:
            self._feild = feild
        
        if race is None:
            self._race = random.randrange(1,6) 
        else:
            self._race = race
            
        if imprace is None:
            self._imprace = random.randrange(1, 10) 
        else:
            self._imprace = imprace
        
        if imprelig is None:
            self._imprelig = random.randrange(1, 10) 
        else:
            self._imprelig = imprelig
        
        if religion is None:
            self._religion = random.randrange(1,5)
        else:
            self._religion = religion
        
        if income is None:
            self._income = random.randrange(20000, 150000, 1000) 
        else:
            self._income = income
        
        if goesOut is None:
            self._goesOut = random.randrange(0,1)
        else:
            self._goesOut = goesOut
        
        if career is None:
            self._career = random.randrange(1,17) 
        else:
            self._career = career
            
        if intrests is None:
            self._intrests = self._generateIntrestList() 
        else:
            self._intrests = intrests
        
        if attributeDistribution is None:
            self._attributeDistribution = self._generateAttributeScores()
        else:
            self._attributeDistribution = attributeDistribution
        
        if desiredAttributeDistribution is None:
            self._desiredAttributeDistribution = self._generateAttributeScores()
        else:
            self._desiredAttributeDistribution = desiredAttributeDistribution()
        
        self._iid = uuid.uuid4()
        



    def __repr__(self):
        '''
        print("Name: " + self._name)
        print("Age: " + str(self._age))
        print("Height: " + str(self._height))
        print("Gender: " + str(self._gender))
        print("Feild: " + str(self._feild))
        print("Race: " + str(self._race))
        print("Imp Race: " + str(self._imprace))
        print("Religion: " +str(self._religion))
        print("Imp Relig: " + str(self._imprelig))
        print("Income: " + str(self._income))
        print("Goes Out?: " + str(self._goesOut))
        print("Career: " + str(self._career))
        print("Intrests: ")
        for key in self._intrests:
            print("\t{}: {}".format(key, self._intrests[key]))
        print("Attributes: ")
        for key in self._attributeDistribution:
            print("\t{}: {}".format(key, self._attributeDistribution[key]))
        print("Des Attributes: ")
        for key in self._desiredAttributeDistribution:
            print("\t{}: {}".format(key, self._desiredAttributeDistribution[key]))
        print("IID: " + str(self._iid))
        '''
        return self._name
    
    def __str__(self):
        return self._name

    #Below Blocks are getter functions for Contestent class
    def getName(self):
        return self._name
     
    def getAge(self):
        return self._age

    def getHeight(self):
        return self._height

    def getGender(self):
        return self._gender

    def getFeild(self):
        return self._feild

    def getRace(self):
        return self._race

    def getImprace(self):
        return self._imprace

    def getReligion(self):
        return self._religion

    def getImprelig(self):
        return self._imprelig

    def getIncome(self):
        return self._income

    def getGoesOut(self):
        return self._goesOut

    def getCareer(self):
        return self._career

    def getIntrests(self):
        return self._intrests

    def getAttributeDistribution(self):
        return self._attributeDistribution

    def getDesiredAttributeDistribution(self):
        return self._desiredAttributeDistribution
    
    def getIID(self):
        return self._iid


