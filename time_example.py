import time

t1 = time.time()

#assume a list of N values
n = 100

for i in range(n):
    for j in range(n):
        time.sleep(0.001)

t2 = time.time()
print(t2-t1)
