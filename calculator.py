#Python program for calculator

#function to add two numbers
def add(n1,n2):
    return n1 + n2
#function to subtract two numbers
def sub(n1,n2):
    return n1 - n2
#function to multiply two numbers
def mult(n1,n2):
    return n1 * n2
#function to divide two numbers
def div(n1,n2):
    return n1 / n2
print('Please choose one operation -\n'
      "1. Add\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" )
#take the input from the user
choose = int(input("Choose operations from 1,2,3,4 :"))

num1 = int(input("Enter first number :"))
num2 = int(input("Enter the second number :"))

if choose == 1:
    print(num1, "+", num2, "=",add(num1,num2))

elif choose == 2:
    print(num1, "-", num2,  "=", sub(num1,num2))
  
elif choose == 3:
    print(num1, "*", num2, "=", mult(num1,num2))

elif choose == 4:
    print(num1, "/", num2, "=",div(num1,num2))

else:
    print("Invalid input")