def add(a,b):
    print(f"{a} + {b} = {a+b}")
    
num1,num2 = input("Enter the num1: "),input("Enter the num2: ")

if "." in num1:
    num1=float(num1)
else: num1 = int(num1)

if "." in num2:
    num2=float(num2)
else: num2 = int(num2)

add(num1,num2)