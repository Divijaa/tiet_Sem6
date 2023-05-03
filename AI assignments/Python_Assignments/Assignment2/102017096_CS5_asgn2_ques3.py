import copy
class EightPuzzle:
   def __init__(self,start_pos,goal_pos):
    self.mygrid=start_pos
    self.mygoal=goal_pos
    self.emptyIndex=self.getEmptyIndex()
    self.prevstate=None
    self.displayState()

   def up(self):
    if(self.emptyIndex==0 or self.emptyIndex==1 or self.emptyIndex==2):
        print("Cannot Move")
        return False
    else:
        self.prevstate=copy.deepcopy(self)
        self.mygrid[self.emptyIndex]=self.mygrid[self.emptyIndex-3]
        self.mygrid[self.emptyIndex-3]=0
        self.emptyIndex=self.emptyIndex-3
        self.displayState()
        return True

   def down(self):
    if(self.emptyIndex==6 or self.emptyIndex==7 or self.emptyIndex==8):
        print("Cannot Move")
        return False
    else:
        self.prevstate=copy.deepcopy(self)
        self.mygrid[self.emptyIndex]=self.mygrid[self.emptyIndex+3]
        self.mygrid[self.emptyIndex+3]=0
        self.emptyIndex=self.emptyIndex+3
        self.displayState()
        return True

   def left(self):
    if(self.emptyIndex==0 or self.emptyIndex==3 or self.emptyIndex==6):
        print("Cannot Move")
        return False
    else:
        self.prevstate=copy.deepcopy(self)
        self.mygrid[self.emptyIndex]=self.mygrid[self.emptyIndex-1]
        self.mygrid[self.emptyIndex-1]=0
        self.emptyIndex=self.emptyIndex-1
        self.displayState()
        return True

   def right(self):
    if(self.emptyIndex==2 or self.emptyIndex==5 or self.emptyIndex==8):
        print("Cannot Move")
        return False
    else:
        self.prevstate=copy.deepcopy(self)
        self.mygrid[self.emptyIndex]=self.mygrid[self.emptyIndex+1]
        self.mygrid[self.emptyIndex+1]=0
        self.emptyIndex=self.emptyIndex+1
        self.displayState()
        return True
   
   def __eq__(self,other):
       return self.mygrid==other.mygrid

   def getEmptyIndex(self):
     for i in range(0,9):
       if self.mygrid[i]==0:
         return i

   def displayState(self):
    for i in range(0,9,3):
      print(self.mygrid[i],self.mygrid[i+1],self.mygrid[i+2])
    print('')

   def PossibleNextStates(self):
       stateList=[]
       left_state= copy.deepcopy(self)
       if left_state.left():
           stateList.append(left_state)

       right_state= copy.deepcopy(self)
       if right_state.right():
           stateList.append(right_state)
        
       up_state= copy.deepcopy(self)
       if up_state.up():
           stateList.append(up_state)
        
       down_state= copy.deepcopy(self)
       if down_state.down():
           stateList.append(down_state)
       return stateList
    
   def isGoalReached(self):
       return self.mygrid == self.mygoal

def DFS(start_state):
    open=[]
    close=[]
    open.append(start_state)

    while(open):
        thisState=open.pop(0)
        thisState.displayState()
        if thisState not in close:
            close.append(thisState)
            if thisState.isGoalReached():
                print('Goal State found..................stopping depth first search')
                break
            nextStates=thisState.PossibleNextStates()
            for eachState in nextStates:
                if eachState not in open and eachState not in close:
                    open.append(eachState)


puzzle = EightPuzzle([1,2,3,8,0,4,7,6,5],[2,8,1,0,4,3,7,6,5])
DFS(puzzle)