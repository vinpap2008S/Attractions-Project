import time
start_time = time.time()
c = 1
for i in range(1, 8):
    c *= i
print(c**c**c)
print("--- %s seconds ---" % (time.time() - start_time))

