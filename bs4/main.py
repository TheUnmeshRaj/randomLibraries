import requests
from bs4 import BeautifulSoup


def fetchToFile(url,path):
  r = requests.get(url)
  with open(path,'w') as f:
    f.write(r.text)

url = "https://www.amazon.in/s?k=bacca+bucci+shoes"
fetchToFile(url,'data.html')


import matplotlib.pyplot as plt
import numpy as np

max_iterations = 1000
step_size = 0.9

def f(x):
    return -x**2

def hillClimbing(initialX):
    currX = initialX
    iteration = 0
    current_value = f(currX)
    X = [currX]
    Y = [f(currX)]

    while iteration < max_iterations:
        neighbor_x = currX + step_size * np.random.uniform(-1, 1)
        neighbor_value = f(neighbor_x)

        if neighbor_value > current_value:
            currX = neighbor_x
            current_value = neighbor_value
            X.append(currX)
            Y.append(current_value)

        iteration += 1

    return currX, f(currX), X, Y

initialX = float(input("Enter the initial value for x: "))
bestSol, bestValue, X, Y = hillClimbing(initialX)

print(f"x = {bestSol}")
print(f"f(x) = {bestValue}")

originalX = np.linspace(min(X), max(X), 1000)
originaly = [f(x) for x in originalX]

plt.plot(originalX, originaly)
plt.plot(X, Y)
plt.title("Hill Climbing Algorithm")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()