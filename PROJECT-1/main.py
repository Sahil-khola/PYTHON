
'''
1 for snake
-1 for water
0 for gun

'''
computer = -1

user =(input("Enter your choice : "))

userdict = {
    's':1,
    'w':-1,
    'g':0
}

yourchoice = userdict[user]

if(computer == yourchoice):
    print("Match Draw")
elif(computer == 1 and yourchoice == -1):
    print("You Win")
elif(computer == -1 and yourchoice == 0):
    print("You Win")
elif(computer == 0 and yourchoice == 1):
    print("You Win")
else:
    print("You Lose")
