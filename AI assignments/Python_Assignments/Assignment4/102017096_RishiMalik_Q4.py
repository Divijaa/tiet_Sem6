# Rishi Malik 
# 102017096
# CS5

import copy
class RishiMalik96:
     def __init__(self, rishi_map):
          RishiMalik96.rishi_map=rishi_map
          self.current102017096=0
          self.goal102017096=6
          self.heuristic_RM=0
          self.visitedList_RM=[]
          self.visitedList_RM.append(self.current102017096)
          self.prev102017096=None
          
     #Display function to print the current and visited nodes at the given iteration
     def displayState(self):
          print(f"Current node:{self.current102017096}     Visited nodes={self.visitedList_RM}")

     def __gt__(self, other):#overloading the greater than operator
          return self.heuristic_RM>other.heuristic_RM

     def __lt__(self, other):#overloading the less than operator
          return self.heuristic_RM<other.heuristic_RM

     def __eq__(self, other):#overloading the equals to operator
          return self.visitedList_RM==other.visitedList_RM

     def isGoalReached(self):#Function to check if we have achieved our desired state
          if self.goal102017096 in self.visitedList_RM:
               return True
          else:
               return False

     def move_rishi(self, node):
          if node!=self.current102017096 and node not in self.visitedList_RM and RishiMalik96.rishi_map[self.current102017096][node]!=-1:
               print(f"Moving from node {self.current102017096} to {node}")
               self.heuristic_RM=RishiMalik96.rishi_map[self.current102017096][node]
               self.current102017096=node
               self.visitedList_RM.append(self.current102017096)
               return True
          else:
               #print("Already visited")
               return False

     def possibleNextStates(self): #Function to find the all the possible next states that can be achieved
          stateList=[]
          for i in range(0, len(RishiMalik96.rishi_map[0])):
               state=copy.deepcopy(self)
               if state.move_rishi(i):
                    self.prev102017096=copy.deepcopy(self)
                    stateList.append(state)
          
          return stateList
               
def rishi_path(goalState):
     print("The solution path from Goal to Start")
     while goalState is not None:
          goalState.displayState()
          goalState=goalState.prev102017096

def BeamSearch(startState, beta): # Beta is the beam width
     open=[]
     closed=[]
     flag=0
     B=beta

     open.append(startState)
     
     while(open):

          thisState=open.pop(0)
          thisState.displayState()

          if thisState not in closed:
               closed.append(thisState)

               if thisState.isGoalReached(): #checking if it is the goal state
                    print("Goal state found.. stopping search")
                    rishi_path(thisState)
                    flag=1
                    break

               nextStates=thisState.possibleNextStates() #Storing all the possible next sates
               for eachState in nextStates:
                    open.append(eachState)
               
               open.sort() 
               #Filtering out the choices according to the beam width
               if len(open)>B:
                    while len(open)!=B:
                         open.pop()

     if flag!=1:
          print("Error, we can't reach the required goal node")

rishi_map=[[-1,  1,  3, -1, -1, -1, -1], [-1, -1, -1,  2,  2, -1, -1],[-1, -1, -1, -1, -1,  3,  0], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1]]
beta=int(input("Enter B (2/3): ")) # Beta is the beam width
problem=RishiMalik96(rishi_map)
BeamSearch(problem, beta)