def calc(str):
 lower=0
 upper=0
 for i in str:
     if 'a'<=i<='z':
         lower+=1
     if 'A'<=i<='Z':
         upper+=1
 print(f"Number of lower characters = {lower}")
 print(f"Number of upper characters = {upper}")

str="Thiis is a SAMPLE string WHich is therE for A RESONH"
calc(str)