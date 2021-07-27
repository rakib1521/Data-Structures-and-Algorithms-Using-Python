import random
valuse= random.sample(range(1,50),10)
def merge_sort(valuse):
    if len(valuse) > 1:
        mid = len(valuse) // 2
        left = valuse[:mid]
        right = valuse[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              valuse[k] = left[i]
              i += 1
            else:
                valuse[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            valuse[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            valuse[k]=right[j]
            j += 1
            k += 1

print("Before sorting : {}".format(valuse))
merge_sort(valuse)
print("After sorting : {}".format(valuse))
