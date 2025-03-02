import random;
x=int(input("Enter length of password"))
e=input("Enter the type of password  \n [low type]->low or LOW \n [medium type]-> medium or MEDIUM\n [hard type]->hard or HARD\n")
password=[]
if(e=="low"):
    for i in range(1,x+1):
        a=random.randint(1,9)
        password=password+[a]
elif(e=="medium"):
    medium="!@#$%^&_"
    password=[random.choice(medium)]
    for i in range(1,x):  
        a=random.randint(0,9)
        password=password+[a]    
elif(e=="hard"):
    for i in range(1,x+1):
        hard="!@#~$%_^&*"
        password+=[(random.choice(hard))]
elif(e=="LOW"):
    for i in range(1,x+1):
        a=random.randint(1,9)
        password=password+[a]
elif(e=="MEDIUM"):
    medium="!@#$%^&_"
    password=[random.choice(medium)]
    for i in range(1,x):
        a=random.randint(0,9)
        password=password+[a]  
elif(e=="HARD"):
    for i in range(1,x+1):
        hard="!@#~$%_^&*"
        password+=[(random.choice(hard))]
else:
    print("Invalid Input")
result = ''.join(map(str, password))
print(result)