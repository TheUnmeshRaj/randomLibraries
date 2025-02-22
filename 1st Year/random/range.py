def checkPrime(a):
    if a<2:
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

for i in range(lower,upper+1):
    if checkPrime(i):
        print(i)