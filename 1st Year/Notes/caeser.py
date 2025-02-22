import random

text = input("Enter something: ")

text = list(text)
ran = random.randint(1, 26)
print(f"Cipher shift is {ran}")
for i in range(len(text)):
    text[i] = chr(((ord(text[i]) - 97 + ran) % 26) + 97)

result = ""

for i in range(len(text)):
    result += text[i]

print(result)
