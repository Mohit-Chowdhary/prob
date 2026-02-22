import random
import matplotlib.pyplot as plt

#average sum of a die thrown 5 times

n = 100000
k = 7

sums = []

for i in range(n):
    s = 0
    for _ in range(k):
        s += random.randint(1,6)
    sums.append(s)

plt.hist(sums,bins = range(k,6*k+2), density = True)
plt.title(f"Sum of {k} dies thrown")
plt.show()