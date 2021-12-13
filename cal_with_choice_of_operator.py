print('Calculator')

try:
    num1 = int(input("Enter the First Number: "))
except ValueError:
    print('Please Enter in Digits. Start Again !! ')
    quit()

op = input('Enter the operator (+,-,*,/): ')

try:
    num2 = int(input("Enter the Second Number: "))
except ValueError:
    print('Please Enter in Digits. Start Again !! ')
    quit()

if op == '+':
    sum = num1 + num2
    print(f'The sum of {num1} and {num2} is {sum}.')
elif op == '-':
    diff = num1 - num2
    print(f'The difference between {num1} and {num2} is {diff}.')
elif op == '*':
    prod = num1 * num2
    print(f'The product of {num1} and {num2} is {prod}.')
elif op == '/':
    div = num1 / num2
    print(f'The quotient of {num1} and {num2} is {div}.')
else:
    print(f'You have entered the wrong OPERATOR. Please try again.')