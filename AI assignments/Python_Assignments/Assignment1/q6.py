sal=int(input("Enter your basic salary\n"))
gsal=0
if(sal<=10000):
    hra=0.2*sal
    da=0.8*sal
elif sal<=20000:
    hra=0.25*sal
    da=0.9*sal
else:
    hra=0.3*sal
    da=0.95*sal
gsal=sal+hra+da
print(f"Your salary is {sal} and gross salary is {gsal}")