# Pyhon program for create a simple calculator

# 3 Steps to build calcularor program :
#   1. Function for operation
#   2. User input
#   3. Print result

# Step 1 : Create function

# Function add two number

def add(num1,num2):
    return num1 + num2

# Function substract two number

def sub(num1,num2):
    return num1 - num2

# Function multiply two number

def multiply(num1,num2):
    return num1 * num2

# Function devide two number

def devide(num1,num2):
    return num1 / num2

# Function average two number

def avg(num1,num2):
    return (num1 + num2)/2

#Step 2 : User input


print("Please select a operation:\n " \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n")

select = int(input("select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Step 3 : Print the result

if select == 1:
    print(number1, "+", number2, "=", \
          add(number1, number2))
    
elif select == 2:
    print(number1, "-", number2, "=", \
          sub(number1, number2))
    
elif select == 3:
    print(number1, "*", number2, "=", \
          multiply(number1, number2))
    
elif select == 4:
    print(number1, "/", number2, "=", \
          devide(number1, number2))
    
elif select == 5:
    print("(",number1, "+", number2,")", "/", "2", "=", \
          avg(number1, number2))
    
else:
    print("Invalid operation! Please select again!")

