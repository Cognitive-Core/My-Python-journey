Num_1 = float(input("Enter the first number: "))
Num_2 = float(input("Enter the second number: "))
operation = input("enter the operation (+,-,*,/,**,%,//)")

if operation == "+":
    print(f'The sum of {Num_1} and {Num_2} is {Num_1 + Num_2}')
elif operation == "-":
    print(f'The difference of {Num_1} and {Num_2} is {Num_1 - Num_2}')
elif operation == "*":
     print(f'The product of {Num_1} and {Num_2} is {Num_1*Num_2}')
elif operation == "/":
     print(f'The division of {Num_1} and {Num_2} is {Num_1/Num_2}')
elif operation == "**":
      print(f'The exponentiation of {Num_1} and {Num_2} is {Num_1**Num_2}')
elif operation == "%":
      print(f'The reminder of {Num_1} and {Num_2} is {Num_1%Num_2}')
elif operation == "//":
      print(f'The floored integer of {Num_1} and {Num_2} is {Num_1//Num_2}')
else:
     print("Please enter a valid operation")
     