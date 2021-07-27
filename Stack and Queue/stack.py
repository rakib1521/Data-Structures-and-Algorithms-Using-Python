def push(stack,l,value):
    if len(stack)==l:
        print("stack overflow")
    else:
        stack.append(value)
    return stack

def pop(stack):
    if len(stack)==0:
        value="stack underflow"
        return stack ,value
    else:
        value=stack[len(stack)-1]
        stack.pop(len(stack)-1)
        return stack ,value
print("Enter stack length: ")
l=int(input())
stack=[]
flag=True
while(flag):
    print("Enter Value: ")
    print("1.PUSH ")
    print("2.POP ")
    print("3.Show Stack")
    print("4.Exit ")
    uInput=int(input())

    if uInput==1:
        value=int(input("Enter value: "))
        stack=push(stack,l,value)

    elif uInput==2:
        stack,value=pop(stack)
        print(value)
    elif uInput==4:
        flag=False
    else:
        print(stack)
