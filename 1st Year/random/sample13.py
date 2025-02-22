D = {5: 1, 3: 15, 4: 4, 8: 20, 10: 60}
list=[]
for key,value in D.items():
    list.append(key+value)
print(list)

print(f"Total Sum = {sum(list)}")
print(D.keys())