import copy
class MyEightPuzzle:
    def __init__(self,startState,goalState):
        self.currentState=startState
        self.goalState=goalState
        self.emptyIndex=self.emptyTileIndex()
        self.prevState=None
    def up(self):
        if self.emptyIndex==6 or self.emptyIndex==7 or self.emptyIndex==8:
            print("cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex+3]
            self.currentState[self.emptyIndex+3]=0
            self.emptyIndex=self.emptyIndex+3
            print('Action Up')
            return True
    def down(self):
        if self.emptyIndex==0 or self.emptyIndex==1 or self.emptyIndex==2:
            print("cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex-3]
            self.currentState[self.emptyIndex-3]=0
            self.emptyIndex=self.emptyIndex-3
            print('Action down')
            return True
    def left(self):
        if self.emptyIndex==2 or self.emptyIndex==5 or self.emptyIndex==8:
            print('cannot move')
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex+1]
            self.currentState[self.emptyIndex+1]=0
            self.emptyIndex=self.emptyIndex+1
            print('Action left')
            return True
    def right(self):
        if self.emptyIndex==0 or self.emptyIndex==3 or self.emptyIndex==6:
            print('cannot move')
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex-1]
            self.currentState[self.emptyIndex-1]=0
            self.emptyIndex=self.emptyIndex-1
            print('Action right')
            return True
    def emptyTileIndex(self):
        for i in range(0,9):
            if(self.currentState[i]==0):
                return i
    def isGoalReached(self):
        if(self.currentState==self.goalState):
            return True
        else:
            return False
    def displayState(self):
        print('-------------------')
        for i in range(0,8,3):
            print(self.currentState[i],self.currentState[i+1],self.currentState[i+2])
        print('-------------------')
    def __eq__(self,other):
        return self.currentState==other.currentState
    
    def possible_nextstates(self):
        stateList=[]
        left_state=copy.deepcopy(self)
        if left_state.left():
            stateList.append(left_state)
        right_state=copy.deepcopy(self)
        if right_state.right():
            stateList.append(right_state)
        up_state=copy.deepcopy(self)
        if up_state.up():
            stateList.append(up_state)
        down_state=copy.deepcopy(self)
        if down_state.down():
            stateList.append(down_state)
        return stateList
    
def heuristic_manhattan(self):
    sum=0
    for i in range(0, 9):
        goalNode=self.goalState[i]
        if goalNode==0:
            continue
        goalIndex=i
        for j in range(0, 9):
            currentNode=self.currentState[j]
            if currentNode==goalNode:
                currentIndex=j
                break
        diff=abs(goalIndex-currentIndex)
        if diff<3:
            moves=diff
        elif diff>=3 and diff<6:
            moves=diff%3 + 1
        elif diff>=6 and diff<8:
            moves=difference%3 +2
        sum+=moves
        return sum


def BestFirstSearch(startState):
    isopen=[]
    closed=[]
    nextStates=[]
    isopen.append(startState)
    while isopen:
        thisState=isopen.pop(0)
        thisState.displayState()
        print('Value of heuristic :',heuristic_manhattan(thisState))
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print('Goal state is found ..stopping search')
                constructPath(thisState)
                break
            nextStates=thisState.possible_nextstates()
            for eachstate in nextStates:
                if eachstate not in closed and eachstate not in isopen:
                    isopen.append(eachstate)
                    isopen.sort(key=heuristic_manhattan)
                    
def constructPath(gstate):
    print('The solution path from ----goal to start----')
    while gstate is not None:
        gstate.displayState()
        gstate=gstate.prevState
start=[2,0,3,1,8,4,7,6,5]
goal=[1,2,3,8,0,4,7,6,5]
problem=MyEightPuzzle(start,goal)
BestFirstSearch(problem)