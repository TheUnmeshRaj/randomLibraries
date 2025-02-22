def sum(*num):
    s  = 0
    for i in num:
        s+=i
    print(s)

sum(2,4)
sum(2,4,5)
sum(2,4,5,6)
sum(2,4,5,6,10)

def sample(**args):
    print(args)
    
sample(Banana=12,Apple=123)
sample(Banana=12,Apple=98,Pineapple=99)