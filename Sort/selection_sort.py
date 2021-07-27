import random

valuse= random.sample(range(1,50),10)
print("Before sorting : {}".format(valuse))
index=0
flag=False
for i in range(0,len(valuse)):
    min =valuse[i]
    for j in range(i,len(valuse)):
        if  min>valuse[j]:
            min,index,flag=valuse[j],j,True
    if flag:
        valuse[i],valuse[index],flag=valuse[index],valuse[i],False

print("After sorting : {}".format(valuse))
