a=[1,2,3,4,5]
print(a)
a.append(12)
print(a)
a.remove(4)
print(a)
s=0
for i in a:
    s+=i
a.append(s)
print(a)