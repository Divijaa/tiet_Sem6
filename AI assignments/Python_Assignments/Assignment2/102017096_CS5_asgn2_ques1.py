j1=int(input("Enter the capacity of jug1"))
j2=int(input("Enter the capacity of jug2"))
g=int(input("Enter the final goal capacity"))

def display():
    print("\n Select he rule to be applied ")
    print("Rule 1: Fill jug1")
    print("Rule 2: Fill jug2")
    print("Rule 3: Empty jug 1")
    print("Rule 4: Empty jug 2")
    print("Rule 5: Transfer whole content of jug 1 to jug 2")
    print("Rule 6: Transfer whole content of jug 2 to jug 2")
    print("Rule 7: Transfer some content of jug 1 to jug 2 untill jug 2 is full")
    print("Rule 8: Transfer some content of jug 2 to jug 1 untill jug 1 is full")
    
    
def applyrule(ch,x,y):
    if(ch==1):
        if(x<j1):
            return j1,y
        else:
            print("THe rule could not be applied")
            return x,y
    elif(ch==2):
        if(y<j2):
            return x,j2
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==3):
        if(x>0):
            return 0,y
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==4):
        if(y>0):
            return x,0
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==5):
        if(x>0 and any<=j2):
            return 0,x+y
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==6):
        if(y>0 and (x+y)<=j1):
            return x+y,0
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==7):
        if(x>0 and (x+y)>=j2):
            return x-(j2-y),j2
        else:
            print("The rule could not be applied")
            return x,y
    elif(ch==8):
        if(y>0 and (x+y)>=j1):
            return j1,y-(j1-x)
        else:
            print("The rule could not be applied")
            return x,y
    else:
      print("The choice is invalid!!")
x=y=0

while(True):
  if(((x==g) and (y==0)) or ((y==g) and (x==0))):

    print("GOAL STATE ACHIEVED SUCCESSFULLY!!")
    break
  else:
    display()
    ch=int(input("Enter the rule to be applied from the list : "))
    x,y=applyrule(ch,x,y)
    print("\nCurrent Status")
    print(x,y)     
  