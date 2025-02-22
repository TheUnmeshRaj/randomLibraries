n =  int(input("Enter n: "))

list=[0,1]
for i in range(n-2):
    list.append(list[i]+list[i+1])

print(list)