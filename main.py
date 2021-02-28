import random
import matplotlib.pyplot as plt

xpoints = range(10)

ypoints = []

print("Hi")

for i in range(10):
	ypoints.append(random.randint(0,19))

plt.bar(xpoints, ypoints)
plt.show()


