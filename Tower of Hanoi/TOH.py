def TOH(n,i,j,k):
    if n==1:
        print("Move top disk {} to {}".format(i,k))
    else:
        TOH(n-1,i,k,j)
        print("Move top disk {} to {}".format(i,k))
        TOH(n-1,j,i,k)

n=int(input("Enter Number of disk: "))
TOH(n,"A","B","C")
