my_dict = {1:'bar', 2:'bar', 3:'foo', 4:'qux'}
keys_to_remove=[1,3]
new_dict={}

print(f"Before deletion : {my_dict}")

for key,value in my_dict.items():
    if key in keys_to_remove:
        continue
    else:
        new_dict[key]=value

my_dict = new_dict

print(f"After deletion : {my_dict}")