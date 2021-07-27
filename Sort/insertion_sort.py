import random

valuse= random.sample(range(1,50),10)
print("Before sorting : {}".format(valuse))
index=-100
flag=False
for i in range(1,len(valuse)):
    for j in range(i,-1,-1):
        if valuse[i]<valuse[j]:
            index=j
            flag=True
    if flag:
        temo_val=valuse.pop(i)
        valuse.insert(index,temo_val)
        flag=False
print("After sorting : {}".format(valuse))
