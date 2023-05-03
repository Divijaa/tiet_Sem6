# PASSWORD VALIDATION
import re 
pas=input("Enter the password to be validated\n")
regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')

digit=False
lowercase=False
uppercase=False
specialchar=False
if len(pas)>16 or len(pas)<6:
    pass

elif(regex.search(pas)==None):
    pass

else:
    for i in pas:
        if i.isdigit():
            digit=True
        if i.islower():
            lowercase=True
        if i.isupper():
            uppercase=True

if(digit==True and uppercase==True and lowercase==True):
    print("Valid Password")
else:
    print("Invalid Password")