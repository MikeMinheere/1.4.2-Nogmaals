import time
i = 50
o = 0
f = 0
while f < 1000:
    f=i+o
    o=o+i
    i=i+1
    time.sleep(1)
    print(str(i)+", "+str(f))