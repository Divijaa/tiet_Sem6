class MyEightPuzzle_Rishi:
    def __init__(self, Rishi_start_state, Rishi_final_state, Rishi_start_state2D, Rishi_final_state2D):
        self.Rishi_start_state=Rishi_start_state
        self.Rishi_final_state=Rishi_final_state
        self.Rishi_start_state2D=Rishi_start_state2D
        self.Rishi_final_state2D=Rishi_final_state2D

    # function for finding the euclidean distance
    def euclidean_dist(self):
        roll_102017096=0 
        # Finding the current state and the required state index to calculate the
        # euclidean distance
        for i in range(0, 3):
            for j in range(0, 3):
                RM_Fnode=self.Rishi_final_state2D[i][j]
                if RM_Fnode==0:
                    continue
                Rishi_Malik_X=i
                Rishi_Malik_Y=j
                for k in range(0, 3):
                    for l in range(0, 3):
                        RM_STnode=self.Rishi_start_state2D[k][l]
                        if RM_STnode==RM_Fnode:
                            Rishi_Malik_start_X=k
                            Rishi_Malik_start_Y=l
                            break
                # Finding the euclidean distance by applying the formula that is
                # by first squaring and taking their and finding the square root of their sum

                x=abs(Rishi_Malik_X-Rishi_Malik_start_X)
                y=abs(Rishi_Malik_Y-Rishi_Malik_start_Y)

                dist=( pow(x, 2) + pow(y, 2))**0.5
                roll_102017096+=dist
                print("Euclidean dist for ",RM_Fnode,"is" ,int(dist)) #Euclidean distance for each element is printed
        print("Heuristic function value for Euclidean dist = ",roll_102017096)
        
    def manhattan_dist(self):
        roll_102017096=0 #Total number of moves we need to make initialized to zero

        #finding number of moves required to reach goal state by each element
        for i in range(0, 9):
            RM_Fnode=self.Rishi_final_state[i]
            if RM_Fnode==0:
                continue
            goalIndex=i # This is the required index
            for j in range(0, 9):
                RM_STnode=self.Rishi_start_state[j]
                if RM_STnode==RM_Fnode:
                    startIndex=j #This is the current index
                    break

            # Taking the absolute difference of the current and the final state

            difference=abs(goalIndex-startIndex)

            # Number of moves to be made is dependent on the value of absolute difference
            # and are calculated ont basis of below shown criteria

            if difference<3:
                moves=difference
            elif difference>=3 and difference<6:
                moves=difference%3 + 1
            elif difference>=6 and difference<8:
                moves=difference%3 + 2
            roll_102017096+=moves #Adding total moves need to be done
            print("Manhattan dist for",self.Rishi_final_state[i],"is ",moves) #Manhattan distance for each element is printed
        print("Heuristic function value for Manhattan distance = ",roll_102017096)
            
    def minkowski_dist(self):
        roll_102017096=0
        # Taking the value of p from user
        p=float(input("Enter value of p: "))
        # p=1-->Manhattan 
        # p=2-->Euclidean distance

        # Finding the current state and the required state index to calculate the
        # Minkowski distance

        for i in range(0, 3):
            for j in range(0, 3):
                RM_Fnode=self.Rishi_final_state2D[i][j]
                if RM_Fnode==0:
                    continue
                Rishi_Malik_X=i
                Rishi_Malik_Y=j
                for k in range(0, 3):
                    for l in range(0, 3):
                        RM_STnode=self.Rishi_start_state2D[k][l]
                        if RM_STnode==RM_Fnode:
                            Rishi_Malik_start_X=k
                            Rishi_Malik_start_Y=l
                            break
                # Taking the absolute difference of the current and the final state
                x=abs(Rishi_Malik_X-Rishi_Malik_start_X)
                y=abs(Rishi_Malik_Y-Rishi_Malik_start_Y)

                # formula for Minkowski distance is applied below

                dist=pow( pow(x, p) + pow(y, p), 1/p )
                roll_102017096+=dist
                print("Minkowski dist for" ,RM_Fnode ,"is ",int(dist)) #Minkowski distance for each element is printed
        print("Heuristic function value for Minkowski dist= ",roll_102017096)
        


RM_start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
RM_final= [1, 2, 3, 8, 0, 4, 7, 6, 5]
RM_start2D=[[2, 0, 3], [1, 8, 4], [7, 6, 5]]
RM_final2D= [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

problem=MyEightPuzzle_Rishi(RM_start, RM_final, RM_start2D, RM_final2D)
problem.euclidean_dist()
problem.manhattan_dist()
problem.minkowski_dist()