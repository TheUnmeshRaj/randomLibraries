str1 = input("Enter the number: ")
sum=0
count=0
while (str1 != "done") and (str1 != "DONE"):
    if str1.isdigit():
     sum+=int(str1)
     count+=1
    str1=input("Enter the number: ")
    
print(f"The average is {sum/count}")