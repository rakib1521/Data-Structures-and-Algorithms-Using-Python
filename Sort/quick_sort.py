import random
valuse= random.sample(range(1,50),10)

def quick_sort(low, high):
    if low <high:
        p = partition(low, high)
        quick_sort(low, p-1)
        quick_sort(p+1, high)

def partition(low, high):
    pivot = valuse[low]
    i = low + 1
    j = high

    while i <= j:

        while i <= j and valuse[j] >= pivot:
            j = j - 1


        while i <= j and valuse[i] <= pivot:
            i = i + 1


        if i <= j:
            valuse[i], valuse[j] = valuse[j], valuse[i]



    valuse[low], valuse[j] = valuse[j], valuse[low]

    return j



print("Before sorting : {}".format(valuse))
quick_sort(0, len(valuse) - 1)
print("After sorting : {}".format(valuse))
