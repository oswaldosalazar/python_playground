print ('Hello, World')

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)

fruits = ['Banana', 'Pear', 'Lemon', 'Strawberry', 'Naranjilla']
loud_fruits = [fruit.upper() for fruit in fruits]
print(loud_fruits)

numbers = [2, 4, 6, 8, 10]
product = 1
for number in numbers:
    product = product * number

print('The product is: ', product)
