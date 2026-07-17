num1=float(input("Enter a num1 value:"))
num2=float(input("Enter a num2 value:"))
print("choose operation:")
print("+: Addition")
print("-: Subtraction")
print("*: Multiplication")
print("/: Division")
choice=input("Enter operation(+,-,*,/):")
if choice=="+":
    result=num1+num2
    print(result)
elif choice=="-":
    result=num1-num2
    print(result)
elif choice=="*":
    result=num1*num2
    print(result)
elif choice=="/":
    if num2 != 0:
        result=num1/num2
        print(result)
    else:
        print("Division by zero is not allowed!")
else:
    print("invalid operation.")