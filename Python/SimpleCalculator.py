#this is a simple calculator for adding
#Subtracting, multiplying and Dividing two numbers
print('This project is basic and only allow you to add two numbers\n')
print ("What do you want to perform? \n(1)\tAdd \n(2)\tSubtract \n(3)\tMultiply \n(4)\tDivide")
userChoice = input('What is your Choice?')
if userChoice == 1:
    number1 = input('What is the first Number?')
    number2 = input('What is the Second Number?')
    answer = int(number1 + number2)
    print(f'The sum of your first and second entry is {answer}')