import random
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
final=[]
def build_minHeap(ls):
    for i in range((len(ls)//2),-1,-1):
        ls=heapify_minHeap(ls,i)
    return ls

def heap_sort(ls):
    ls=build_minHeap(ls)
    for i in range(len(ls),0,-1):
        ls[0],ls[len(ls)-1]=ls[len(ls)-1],ls[0]
        final.append(ls[len(ls)-1])
        ls.pop(len(ls)-1)
        ls=heapify_minHeap(ls,0)



heap_sort(ls)
print(final)
