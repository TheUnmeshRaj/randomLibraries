str1 = "This is sample text being written to check whether my sample program works or not or whether it is complete failure."

list1 = str1.split()
list2 = set()

word1 = list1[0]  # Save the first word
list2.add(list1[0])

for i in range(len(list1)):
    list3 = list(list2)  # Create a copy of list2
    for item in list3:  # Iterate over the copy
        if item in list1[i]:
            list1[i] = list1[i].replace(item, "RVCE")
        else:
            list2.add(list1[i])  # Add unique words to list2

# Reset the first word
list1[0] = word1

# Final print
ans = " ".join(list1)
print(ans)
