def Calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

print(Calculate(num1, num2, operator)) 


#Alternative way to write the code:

#num1 = input('Enter first number: ')
#num2 = input('Enter second numer: ')
#operator = input('Enter operator: ')
#print(eval(num1 + operator + num2))