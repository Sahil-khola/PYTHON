mark1 = int(input("Enter Marks 1: "))
mark2 = int(input("Enter Marks 2: "))
mark3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (mark1+mark2+mark3)/3

if(total_percentage>=40 and mark1>33 and mark2>33 and mark3>33):
    print("You are Pass ",total_percentage)

else:
    print('You are Fail, try again next year!',total_percentage)
# elif(total_percentage<=33):
#     print("You are Fail")