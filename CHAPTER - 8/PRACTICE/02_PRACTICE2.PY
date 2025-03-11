
def converter(f):
    C = 5*(f-32)/9
    return C

f = int(input('Enter temperature in F : '))

print(f'The Temperature in f is {round(converter(f),2)} ')