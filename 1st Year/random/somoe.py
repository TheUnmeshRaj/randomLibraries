# Step 1: Creating a file and writing into it

# Open the file in write mode ('w'). If the file doesn't exist, it will be created.
with open('example_file.txt', 'w') as file:
    # Write some data to the file
    file.write("Hello, this is a test file.\n")
    file.write("This file contains multiple lines of text.\n")
    file.write("Python is a versatile language.")

print("Data has been written to the file.")

# Step 2: Reading from the file

# Open the file in read mode ('r')
with open('example_file.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()

# Print the content of the file
print("Content of the file:")
print(content)
