import random
import matplotlib.pyplot as plt

fh = open("green dream.txt", "r")
text = fh.read()
ypoints = [0] * 26

for c in text:
	if c.isalpha():
		pos = ord(c.lower())-97
		ypoints[pos] = ypoints[pos] + 1

xpoints = []

for i in range(26):
	xpoints.append(chr(i+65))

plt.bar(xpoints, ypoints)
plt.show()


