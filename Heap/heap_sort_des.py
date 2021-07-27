import random
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

ls=random.sample(range(1,50),40)
final=[]
def build_maxHeap(ls):
    for i in range((len(ls)//2),-1,-1):
        ls=heapify_maxHeap(ls,i)
    return ls

def heap_sort(ls):
    ls=build_maxHeap(ls)
    for i in range(len(ls),0,-1):
        ls[0],ls[len(ls)-1]=ls[len(ls)-1],ls[0]
        final.append(ls[len(ls)-1])
        ls.pop(len(ls)-1)
        ls=heapify_maxHeap(ls,0)



heap_sort(ls)
print(final)
