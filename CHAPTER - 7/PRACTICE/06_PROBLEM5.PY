num = int(input('Enter the Number: '))

product = 1
for i in range(1,num+1):
    product = product*i

print(f"the factorial of {num} is {product}")    