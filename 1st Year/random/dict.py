test = {}  # Creating an empty dictionary
lst = [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

for num in range(len(lst)):
    test[num] = lst[num]  # Adding each unique number as a key to the dictionary

# print(test)  # Printing the contents of the dictionary
print(test[3])
