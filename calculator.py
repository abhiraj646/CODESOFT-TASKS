a=int(input("Enter a First Number"))
b=int(input("Enter a Second Number"))
c=input("Select opertaion")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)    
elif(c=="%"):
    print(a%b)    
elif(c=="**"):
    print(a**b)    
elif(c=="&"):
    print(a&b) 
else:
    print("Invalid Input")   