import random
ls=[]
for i in range(0,50):
    ls.append(random.randint(1,55))

uInput=int(input("Enter Number : "))

for i in range(len(ls)):
    if ls[i]==uInput:
        print("Found at {}".format(i))
        break
