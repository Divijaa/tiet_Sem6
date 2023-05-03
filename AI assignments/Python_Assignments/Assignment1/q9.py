D={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
D[6]="Six"
del D[2]

for item in D.keys():
    if item==6:
        print("Key Present")
        break
else:
    print("Key not Present")

print(len(D))

count=0
for item in D.keys():
    count+=item

print(f"The Sum of keys is {count}")