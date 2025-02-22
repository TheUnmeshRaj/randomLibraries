def fact(n):
    pdt=1
    for i in range(1,n+1):
        pdt*=i
    return pdt

print(f"Fact of 5 is {fact(5)}")
print(f"Fact of 4 is {fact(4)}")
print(f"Fact of 10 is {fact(10)}")