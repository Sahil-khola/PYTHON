num = int(input("Enter the Number : "))

for i in range (2,num):
    if(num%i)==0:
        print("Number is not prime number")
        break
else:
    print('Number is prime Number')