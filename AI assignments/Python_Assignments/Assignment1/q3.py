n1=int(input("Enter first number\n"))
n2=int(input("Enter second number\n"))
ans=list()
i=n1
while(i<n2):
    for k in range(2,int(i/2)+1):
        if(i%k)==0:
            break
    else:
        ans.append(i)
    i+=1

print(ans)