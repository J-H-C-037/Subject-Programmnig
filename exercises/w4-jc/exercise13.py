"""

Exercise 13. Create a program to simulate a calculator. It must ask for two numbers and the operator (+
- * / // **) and show the result. If the operator is not a valid one, it must print the wrong operator
and finish.

"""

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
operator = input("Select the operator(+,-,*,/):")

if(operator == "+"):
    print(a + b)
elif(operator == "-"):
    print(a - b)
elif(operator == "*"):
    print(a * b)
elif(operator == "/"):
    print(a/b)
else:
    print("Wrong operator" + operator)
