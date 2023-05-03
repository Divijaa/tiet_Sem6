def factorial(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    return n*factorial(n-1)

x=int(input("Enter the value of x\n"))
n=int(input("Enter the value of n\n"))

count=0
for i in range(n+1):
    count+=(x**i)/factorial(i)

print(f"The Sum of sries for given value of x and n is {count}")