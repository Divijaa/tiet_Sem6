import random
res =[random.randrange(100,900) for i in range(100)]
ocount=0
ecount=0
pcount=0
odd=list()
even=list()
prime=list()
for item in res:
    if(item%2==0):
        ecount+=1
        even.append(item)
    else:
        for i in range(2,int(item/2)+1):
            if(item%i)==0:
                ocount+=1
                odd.append(item)
                break
        else:
            pcount+=1
            prime.append(item)

print(f"There are {ocount} odd numbers and are:\n{odd}")
print(f"There are {ecount} even numbers and are:\n{even}")
print(f"There are {pcount} prime numbers and are:\n{prime}")