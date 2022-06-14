print("Wecome to online calculator!!")
num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))
operation = (input("Select the operation which you want to perform:\n"
      "1. Addition (+)\n"
      "2. Subtraction (-)\n"
      "3. multiplication (*)\n"
      "4. Division (/):"))
if operation=='+':
    print("The value is :" , num1+num2)
elif operation=='*':
    print("The value is :" ,num1*num2)
elif operation=='-':
    print("The value is :" ,num1-num2)
elif operation=='/':
    print("The value is :" ,num1/num2)
else:
    print("Please provide correct operation")

print("Thanyou, Have a Nice day!!")
