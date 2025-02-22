with open('myfile.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        words = line.split(" ")  # Split each line into words
        print(words)  # Print the list of words
