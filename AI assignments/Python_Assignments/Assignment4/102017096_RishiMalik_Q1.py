# Rishi Malik 
# 102017096
# CS5

import copy
class Rishi102017096Class:
    def __init__(self, start, goal):
        self.current102017096=start
        self.goal102017096=goal
        self.prev102017096=None

    def isGoalReached(self): #checks if the required goal state is achieved or not
        for i in range(0, 4):
            if self.current102017096[i]==goal: #if the current state is equal to required state then we return true
                return True
        return False

    def displayState(self): #Display function for printing the current state
        for i in range(0, 4):
            if self.current102017096[i]!=[]:
                print(f"Stack {i}:")
                print(self.current102017096[i])

    def _eq_(self, other): #Overloading equals to operator 
        return self.current102017096==other.current102017096

    def movefromStackXtoStackY(self, x, y):
        if self.current102017096[x]!=[] and len(self.current102017096[y])!=4:
            self.prev102017096=copy.deepcopy(self)
            block=self.current102017096[x].pop()
            self.current102017096[y].append(block)
            return True
        else:
            return False

    def possible102017096(self):#this func find all the possible next states that stack can achieve
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
            if self.current102017096[i]!=[]:
                if self.current102017096[i][0]==self.goal102017096[0]:
                    value+=1
                else:
                    value-=1

        
        for i in range(0, 4):
            goalBlock=self.goal102017096[i]
            goalBlockIndex=i
            for j in range(0, 4):
                flag=0
                for k in range(0, len(self.current102017096[j])):
                    if self.current102017096[j]!=[]: 
                        if self.current102017096[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break
                if flag==1:
                    flag=0
                    break
            
            if self.current102017096[currentBlockIndexX][currentBlockIndexY-1]==self.goal102017096[goalBlockIndex-1] and currentBlockIndexY!=0 and goalBlockIndex!=0:
                value+=1
            else:
                if currentBlockIndexY!=0:
                    value-=1
                
        return value

def rishi_path(goal102017096):
    print("Displaying path from start to goal")
    while goal102017096:
        goal102017096.displayState()
        goal102017096=goal102017096.prev102017096
    
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

        thisState.displayState() #Displaying our current state

        #Step 4
        if thisState.isGoalReached(): #Checking if it is current state
            print("Goal state found stopping search")
            returnVal=rishi_path(thisState)
            break

        #Step 5
        nextStates=thisState.possible102017096() #Storing all the possible next states

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
problem=Rishi102017096Class(start, goal)
HillClimbing(problem)