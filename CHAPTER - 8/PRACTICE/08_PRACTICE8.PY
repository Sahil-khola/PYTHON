def multiple(n):
    for i in range (1,n+1):
        print(f"{n} X {i} = {n*i}")

n = int(input('Enter the Number : '))
multiple(n)

'''

'''
def pattern(n):
    for i in range(1,n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

pattern(5)