import random
lst1 =[random.randrange(1,20) for i in range(10)]
lst2 =[random.randrange(1,20) for i in range(10)]

s1=set(lst1)
s2=set(lst2)

s3=s1.intersection(s2)
print(lst1)
print(lst2)
print(s3)