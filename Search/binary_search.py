import random
ls=[]
for i in range(0,50):
    ls.append(random.randint(1,55))
ls.sort()
flag=True
uInput=int(input("Enter Number : "))
fi=0
li=len(ls)-1
current_index=(fi+li)//2
while(flag):
    if ls[current_index]==uInput:
        print("Found")
        flag=False
    elif  ls[current_index]>uInput:
        fi=0
        li=current_index-1
        current_index=(fi+li)//2
    else:
        fi=current_index+1
        li=len(ls)-1
        current_index=(fi+li)//2
