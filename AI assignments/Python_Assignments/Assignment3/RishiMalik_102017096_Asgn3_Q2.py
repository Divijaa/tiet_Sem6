import copy
class MyEightPuzzle:
    def __init__(self,Rishi_start_state,Rishi_goal_state):
        self.RishiCurr_state=Rishi_start_state
        self.Rishi_goal_state=Rishi_goal_state
        self.Rishi_empty_idx=self.emptyTileIndex()
        self.Rishi_prev_state=None
    def up(self):
        if self.Rishi_empty_idx==6 or self.Rishi_empty_idx==7 or self.Rishi_empty_idx==8:
            print("cannot move")
            return False
        else:
            self.Rishi_prev_state=copy.deepcopy(self)
            self.RishiCurr_state[self.Rishi_empty_idx]=self.RishiCurr_state[self.Rishi_empty_idx+3]
            self.RishiCurr_state[self.Rishi_empty_idx+3]=0
            self.Rishi_empty_idx=self.Rishi_empty_idx+3
            print('Action Up')
            return True
    def down(self):
        if self.Rishi_empty_idx==0 or self.Rishi_empty_idx==1 or self.Rishi_empty_idx==2:
            print("cannot move")
            return False
        else:
            self.Rishi_prev_state=copy.deepcopy(self)
            self.RishiCurr_state[self.Rishi_empty_idx]=self.RishiCurr_state[self.Rishi_empty_idx-3]
            self.RishiCurr_state[self.Rishi_empty_idx-3]=0
            self.Rishi_empty_idx=self.Rishi_empty_idx-3
            print('Action down')
            return True
    def left(self):
        if self.Rishi_empty_idx==2 or self.Rishi_empty_idx==5 or self.Rishi_empty_idx==8:
            print('cannot move')
            return False
        else:
            self.Rishi_prev_state=copy.deepcopy(self)
            self.RishiCurr_state[self.Rishi_empty_idx]=self.RishiCurr_state[self.Rishi_empty_idx+1]
            self.RishiCurr_state[self.Rishi_empty_idx+1]=0
            self.Rishi_empty_idx=self.Rishi_empty_idx+1
            print('Action left')
            return True
    def right(self):
        if self.Rishi_empty_idx==0 or self.Rishi_empty_idx==3 or self.Rishi_empty_idx==6:
            print('cannot move')
            return False
        else:
            self.Rishi_prev_state=copy.deepcopy(self)
            self.RishiCurr_state[self.Rishi_empty_idx]=self.RishiCurr_state[self.Rishi_empty_idx-1]
            self.RishiCurr_state[self.Rishi_empty_idx-1]=0
            self.Rishi_empty_idx=self.Rishi_empty_idx-1
            print('Action right')
            return True
    def emptyTileIndex(self):
        for i in range(0,9):
            if(self.RishiCurr_state[i]==0):
                return i
    def isGoalReached(self):
        if(self.RishiCurr_state==self.Rishi_goal_state):
            return True
        else:
            return False
    def displayState(self):
        print('-------------------')
        for i in range(0,8,3):

            print(self.RishiCurr_state[i],self.RishiCurr_state[i+1],self.RishiCurr_state[i+2])
        print('-------------------')
    def __eq__(self,other):
        return self.RishiCurr_state==other.RishiCurr_state
    
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
def heuristic(self):
    cnt=0
    for i in range(0,9):
        if self.Rishi_goal_state[i]!=0 and self.Rishi_goal_state[i]!=self.RishiCurr_state[i]:
            cnt=cnt+1
    return cnt

def BestFirstSearch(Rishi_start_state):
    isopen=[]
    closed=[]
    nextStates=[]
    isopen.append(Rishi_start_state)
    while isopen:
        thisState=isopen.pop(0)
        thisState.displayState()
        print('Value of heuristic :',heuristic(thisState))
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
                    isopen.sort(key=heuristic)
                    
def constructPath(gstate):
    print('The solution path from ----goal to start----')
    while gstate is not None:
        gstate.displayState()
        gstate=gstate.Rishi_prev_state

start=[1,0,4,8,3,2,7,6,5]
goal=[1,2,3,8,0,4,7,6,5]
problem=MyEightPuzzle(start,goal)
BestFirstSearch(problem)