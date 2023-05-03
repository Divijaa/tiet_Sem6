# Rishi Malik 
# 102017096
# CS5

import copy

class Rishi102017096:
    def __init__(self, start, goal):
        self.current102017096=start
        self.goal102017096=goal
        self.prev102017096=None

    def isGoalReached(self):#Function to check if the required goal is reached 
        for i in range(0, 3):
            if self.current102017096[i]==goal:
                return True
        
        return False

    def displayState(self):# Function to display the each state untill the goal state is achieved
        for i in range(0, 3):
            if self.current102017096[i]!=[]:
                print(f"Stack {i}:")
                print(self.current102017096[i])

    def __gt__(self, other): #Overloading the greater than operator
        return self.heuristic()>other.heuristic()

    def __lt__(self, other):
        return self.heuristic()<other.heuristic()#Overloading the less than operator

    def _eq_(self, other):#Overloading the equals to operator
        return self.current102017096==other.current102017096

    def movefromStackXtoStackY(self, x, y):
        if self.current102017096[x]!=[] and len(self.current102017096[y])!=3:
            self.prev102017096=copy.deepcopy(self)
            block=self.current102017096[x].pop()
            self.current102017096[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):#This function finds all the possible next states that can be achieved
        #print("Over here")
        stateList=[]
        for i in range(0, 3):
            for j in range(0, 3):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    stateList.append(copy_state)
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 3):
            goalBlock=self.goal102017096[i]
            goalBlockIndex=i

            for j in range(0, 3):
                flag=0
                if self.current102017096[j]!=[]:
                    for k in range(0, len(self.current102017096[j])):
                        if self.current102017096[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break

                if flag==1:
                    flag=0
                    break
            
            if currentBlockIndexY!=goalBlockIndex:
                value-=currentBlockIndexY
            else:
                value+=currentBlockIndexY
                
        return value

def Rishi_path(goal102017096):
    print("Displaying path from start to goal")
    while goal102017096:
        goal102017096.displayState()
        goal102017096=goal102017096.prev102017096
    
    return 1

def SteepestHillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)


    #Step 2
    returnVal=0
    while open:

        #
        thisState=open.pop(0)
        #print("Printing thisState")
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():#Checking if it is goal state
            print("Goal state found stopping search")
            returnVal=Rishi_path(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()#Storing all the possible next sates

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
        
        #Step 7
        open.sort(reverse=True) #Sort in descending order
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[3, 1], [2], []]
goal=[1, 2, 3]
problem=Rishi102017096(start, goal)
SteepestHillClimbing(problem)