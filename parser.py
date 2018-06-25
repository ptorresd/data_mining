import numpy as np

print(12)
players=open("players.csv","r")
players.readline()

match=open("match.csv","r")
match.readline()

x=np.ndarray([50000,113])
y=np.ndarray([50000])
for i in range(50000):
    for j in range(10):
        hero = int(players.readline().split(",")[2])
        if j<5:
            x[i, hero] = 1
        else:
            x[i, hero] = -1

    if match.readline().split(",")[9]=="TRUE":
        y[i]=1
    else:
        y[i]=-1
np.save("picks",x)
np.save("winners",y)
