## To print 
num1,num2,sum=2,3,(2+3)

print("Sum of {0} and {1} = {2}".format(num1, num2, sum))
print(f"Sum of {num1} and {num2} = {sum}")
print("Sum of", num1, "and", num2, "=", sum)
print("Sum of {day:02d}".format(day=998))

## To round-off
num = 245.2345252
print(f"num={num:0.2f}")
print(f"num={round(num,2)}")