a = int(input('Enter a number: '))
b = int(input('Enter a second number: '))
operator = input('Enter an operator (+ or -): ')

addition = a + b
subtraction = a - b

if operator == '+' :
  print(a, 'plus', b, 'equals', str(addition))

elif operator == '-' :
  print(a, 'minus', b, 'equals', str(subtraction))

else:
  print('Invalid operator entered')