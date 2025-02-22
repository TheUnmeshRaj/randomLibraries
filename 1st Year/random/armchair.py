n=input("Enter a number: ")
size = len(n)
og = int(n)
temp=0
for i in n:
    temp+=int(i)**size

if(og==temp):
    print("It is an armchair number")
else:
    print("neh")