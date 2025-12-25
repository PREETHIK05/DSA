n1=input('enter n1:')
n2=input('enter n2:')
number1=int(n1)
number2=int(n2)
print('sum of the two numbers:',number1+number2)
print('difference of the two numbers:',number1-number2)
print('product of the two numbers:',number1*number2)
if(number1>number2):
    print('number 1 is greater')
elif (number2>number1):
    print('number 2 is greater')
else:
    print('numbers are equal')
