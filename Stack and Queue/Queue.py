def isEmpty(queue):
    if len(queue)==0:
        return True
    else:
        return False
def isFull(queue,l):
    if len(queue)==l:
        return True
    else:
        return False

def Enqueue(queue,l,value):
    if isFull(queue,l):
        print("Queue Full")
    else:
        queue.append(value)
    return queue

def Dequeue(queue):
    if isEmpty(queue):
        value="Queue Empty"
        return queue ,value
    else:
        value=queue[0]
        queue.pop(0)
        return queue ,value

def peak(queue):
    if isEmpty(queue):
        value="Queue Empty"
        return value
    else:
        value=queue[0]
        return value



print("Enter Queue length: ")
l=int(input())
queue=[]
flag=True
while(flag):
    print("Enter Value: ")
    print("1.Enqueue ")
    print("2.Dequeue ")
    print("3.Peak")
    print("4.Exit ")
    uInput=int(input())

    if uInput==1:
        value=int(input("Enter value: "))
        queue=Enqueue(queue,l,value)

    elif uInput==2:
        queue,value=Dequeue(queue)
        print(value)
    elif uInput==3:
        value=peak(queue)
        print(value)
    else:
        flag=False
