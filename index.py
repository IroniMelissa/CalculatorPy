#python program for simple calculator
#function to add two numbers
def add(num1, num2):
    return num1 + num2

#function to subract two numbers
def sub (num1, num2):
    return num1 - num2

#function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

#function to divide two numbers
def div(num1, num2):
    return num1/num2

print("Please select correct operation \n")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n" )

#take input from the user
select = int(input("Select operation from 1 to 4 : "))

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))

if select == 1:
    print(num_1, "+", num_2, "=", add(num_1,num_2))

elif select == 2:
    print(num_1,"-", num_2, "=", sub(num_1,num_2))

elif select == 3:
    print(num_1,"*", num_2, "=", multiply(num_1,num_2))

elif select == 4:
    print(num_1, "/", num_2, "=", div(num_1,num_2))

else:
    print("Invalud Input.")
