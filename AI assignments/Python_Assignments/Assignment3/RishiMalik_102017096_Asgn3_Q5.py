import copy
class ShortestPath:
    def __init__(self, thisMap, startCity, goalCity):
        ShortestPath.thisMap=thisMap
        self.currentCity=startCity
        self.goalCity=goalCity
        self.visitedList=[]
        self.cost=0
        self.visitedList=[]
        self.visitedList.append(self.currentCity)
        self.prevState=None
        
    def displayState(self):
        print('-------------')
        print('current city:',self.currentCity,"Cost:",self.cost)
        print('Visited Cities:',self.visitedList)
        print('-------------')
    
    def __eq__(self, other):
        return self.visitedList==other.visitedList
    
    def __lt__(self, other):
        return self.cost<other.cost

    def __gt__(self, other):
        return self.cost>other.cost
    
    def isGoalReached(self):
        if self.goalCity in self.visitedList:
            return True
        else:
            return False
        
    def move(self,city):
        if(city!=self.currentCity and city not in self.visitedList):
            self.prevState=copy.deepcopy(self)
            print("moving from city",self.currentCity,"to",city)
            self.cost=self.cost+ShortestPath.thisMap[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(city)
            return True
        else:
            print('Already Visited',city)
            return False
        
    def isGoalReached(self):
        if len(ShortestPath.thisMap[0])==len(self.visitedList):
            return True
        else:
            return False
        
    def possibleNextStates(self):
        stateList=[]
        for i in range(0,4):
            newState=copy.deepcopy(self)
            if newState.move(i):
                stateList.append(newState)
        return stateList

isopen=[]
closed=[]
def UCS(state):
    isopen.append(state)
    while isopen:
        thisState=isopen.pop(0)
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal state found.. stopping search")
                constructPath(thisState)
                break
            else:
                nextStates=thisState.possibleNextStates()
                for eachState in nextStates:
                    if eachState not in isopen and eachState not in closed:
                        isopen.append(eachState)
                        isopen.sort()
                    elif eachState in isopen:
                        index=isopen.index(eachState)
                        if isopen[index].cost>eachState.cost:
                            isopen.pop(index)
                            isopen.append(eachState)
                            isopen.sort()
                    elif eachState in closed:
                        index=closed.index(eachState)
                        if closed[index].cost>eachState.cost:
                            closed.pop(index)
                            closed.append(eachState)
                            propogateImprovement(eachState)

def propogateImprovement(state):
    nextStates=state.possibleNextStates()
    for eachState in nextStates:
        if eachState in isopen:
            index=isopen.index[eachState]
            if isopen[index].cost>eachState.cost:
                isopen.pop(index)
                isopen.append(eachState)
                isopen.sort()
            if eachState in closed:
                index=closed.index(eachState)
                if closed[index].cost>eachState.cost:
                    closed.pop(index)
                    closed.append(eachState)
                    propogateImprovement(eachState)

thisMap=[[0, 1, 5, 15, 0], [1, 0, 0, 0, 10], [5, 0, 0, 0, 5], [15, 0, 0, 0, 5], [0, 10, 5, 5, 0]]
startState=0
goalState=4
problem=ShortestPath(thisMap, startState, goalState)
UCS(problem)