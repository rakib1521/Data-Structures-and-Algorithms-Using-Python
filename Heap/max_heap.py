def heapify_maxHeap(ls,i):
    if len(ls)>((2*i)+2):
        if  ls[i]!=max(ls[i],ls[2*i+1],ls[2*i+2]) :
            if ls[2*i+1]==max(ls[i],ls[2*i+1],ls[2*i+2]):
                ls[i],ls[2*i+1]=ls[2*i+1],ls[i]
                ls=heapify_maxHeap(ls,2*i+1)
            else:
                ls[i],ls[2*i+2]=ls[2*i+2],ls[i]
                ls=heapify_maxHeap(ls,2*i+1)

    elif  len(ls)>((2*i)+1):
            if ls[i]!=max(ls[i],ls[2*i+1]):
                ls[i],ls[2*i+1]=ls[2*i+1],ls[i]
                ls=heapify_maxHeap(ls,2*i+1)


    return ls

ls=[5,1,-41,2,3]

for i in range((len(ls)//2),-1,-1):
    ls=heapify_maxHeap(ls,i)

print(ls)
