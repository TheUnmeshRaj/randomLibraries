num = int(input("Enter the number: "))
og = num
list=[]
for i in range(num,0,-1):
    list.append(i)
for i in range(num+1):
    list.append(i)
    
print(list)