import random

valuse= random.sample(range(1,50),40)
print("Before sorting : {}".format(valuse))
k=1

for i in range(0,len(valuse)):
    k=k+1
    flag=False
    for j in range(0,len(valuse)-k):
        if valuse[j]>valuse[j+1]:
            valuse[j],valuse[j+1]=valuse[j+1],valuse[j]
            flag=True
    #print("pass {} {}".format(k,valuse))
    if flag==False:
        break
print("Pass Needed {} times".format(k))
print("After sorting : {}".format(valuse))
