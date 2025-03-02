import random;
print("For Start A Game Enter -Ready")
player=input()
if(player=="Ready"):
    AI=0
    Your_point=0
    while(True):
        print("For go Enter- Go\nFor End The Game Enter- Exit\n For Check Score Enter -Score")
        statement=input()
        if(statement=="Go"):
            print("Enter your choice-Rock || Paper|| scissors.")
            a=input()
            a=[a]
            game=("Rock","Paper","scissors")
            your_choice=[random.choice(game)]
            print(your_choice)
            if(a==your_choice):
                print("no loss no win")                
            elif(a==['Rock'] and your_choice==['paper']):
                print("AI WIN")
                AI=AI+1
            elif(a==['Rock'] and your_choice==['scissors']):
                print("YOU WIN")
                Your_point=Your_point+1
            elif(a==['Paper'] and your_choice==['scissors']):
                print("AI WIN")
                AI=AI+1
            elif(a==['Paper'] and your_choice==['Rock']):
                print("YOU WIN")
                Your_point=Your_point+1
            elif(a==['scissors'] and your_choice==['Paper']):
                print("YOU WIN")
                Your_point=Your_point+1
            elif(a==['scissors'] and your_choice==['Rock']):
                print("AI WIN")
                AI=AI+1
            elif(a==['Rock'] and your_choice==['scissors']):
                print("YOU WIN")
                Your_point=Your_point+1
            else:
                print("INVALID INPUT")
        elif(statement=="Exit"):
            print("Thanks for playing game!!!")
            break;
        elif(statement=="Score"):
            print("AI point ==",AI)
            print("your_point ==",Your_point)
        else:
            print("Invalid Input\n Try Again!!!!!")
else:
    print("Sorry {Invalid Input}")