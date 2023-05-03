lp1=int(input("Enter the lower limit of year\n"))
lp2=int(input("Enter the upper limit of year\n"))
lst=list()
i=lp1
while i<lp2:
    if(i%4==0 and i%100 !=0):
        lst.append(i)
    elif(i%400)==0:
        lst.append(i)
    i+=1
print(lst)