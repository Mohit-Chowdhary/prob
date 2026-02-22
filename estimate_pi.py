import random

n = 1
m = 10000
count = 0

for i in range(m):
    x = random.uniform(-n,n)
    y = random.uniform(-n,n)

    if x**2 + y**2 <= n**2:
        count+=1

print("est pi value is ",4*count/m)