def heapify_minHeap(ls,i):
    if len(ls)>((2*i)+2):
        if  ls[i]!=min(ls[i],ls[2*i+1],ls[2*i+2]) :
            if ls[2*i+1]==min(ls[i],ls[2*i+1],ls[2*i+2]):
                ls[i],ls[2*i+1]=ls[2*i+1],ls[i]
                ls=heapify_minHeap(ls,2*i+1)
            else:
                ls[i],ls[2*i+2]=ls[2*i+2],ls[i]
                ls=heapify_minHeap(ls,2*i+1)

    elif  len(ls)>((2*i)+1):
            if ls[i]!=min(ls[i],ls[2*i+1]):
                ls[i],ls[2*i+1]=ls[2*i+1],ls[i]
                ls=heapify_minHeap(ls,2*i+1)


    return ls

ls=random.sample(range(1,50),40)

for i in range((len(ls)//2),-1,-1):
    ls=heapify_minHeap(ls,i)

print(ls)
