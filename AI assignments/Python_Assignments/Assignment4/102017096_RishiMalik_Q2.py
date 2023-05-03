# Rishi Malik 
# 102017096
# CS5

import copy
class Rishi102017096:
    def __init__(self, start, goal):
        self.currentRM96=start
        self.goalRM96=goal
        self.prevRM96=None

    def isGoalReached(self):#Function to check if the required goal is achieved
        for i in range(0, 4):
            if self.currentRM96[i]==goal:
                return True
        
        return False

    def displayState(self): #Display function to print the each state
        for i in range(0, 4):
            if self.currentRM96[i]!=[]:
                print(f"Stack {i}:")
                print(self.currentRM96[i])

    def _eq_(self, other): #Overloading equals to operator
        return self.currentRM96==other.currentRM96

    def movefromStackXtoStackY(self, x, y):
        if self.currentRM96[x]!=[] and len(self.currentRM96[y])!=4:
            self.prevRM96=copy.deepcopy(self)
            block=self.currentRM96[x].pop()
            self.currentRM96[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self): # Finds the possible next states that can be achieved
        #print("Over here")
        stateList=[]
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    stateList.append(copy_state)
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 4):
            goalBlock=self.goalRM96[i]
            goalBlockIndex=i

            for j in range(0, 4):
                flag=0
                if self.currentRM96[j]!=[]:
                    for k in range(0, len(self.currentRM96[j])):
                        if self.currentRM96[j][k]==goalBlock:
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

def Rishi_path(goalRM96):
    print("Displaying path from start to goal")
    while goalRM96:
        goalRM96.displayState()
        goalRM96=goalRM96.prevRM96
    return 1

def HillClimbing(startState):
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
        if thisState.isGoalReached(): #Checking for the goal state
            print("Goal state found.. stopping search")
            returnVal=Rishi_path(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates() #Storing all the possible next sates

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
    
    if returnVal!=1:
        print("Error: Local Maxima")

start=[[2, 3, 4, 1], [], [], []]
goal=[1, 2, 3, 4]
problem=Rishi102017096(start, goal)
HillClimbing(problem)