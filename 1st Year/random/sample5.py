str1 = int(input("Enter the number: "))
sum=0
count=0
while str1 != 0:
    sum+=int(str1)
    count+=1
    str1=int(input("Enter the number: "))
    
print(f"The average is {sum/count}")