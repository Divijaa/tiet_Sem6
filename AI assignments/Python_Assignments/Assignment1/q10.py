from pip import main


def compoundInterest(p,rate,t):
    amount=p*((1+(rate/100))**t)
    ci=amount-p
    return ci

if __name__=='__main__':
    p=int(input("Enter the principal amount\n"))
    r=int(input("Enter the rate of interest\n"))
    t=int(input("Enter the duration\n"))

    print(f"The compound interest is {compoundInterest(p,r,t)}")