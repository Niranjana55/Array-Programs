#26.Given an unsorted integer array as input,
 #find the Kth largest/smallest element in the array

def kthsmal(a):
    a.sort()
    k=input("enter the num:")
    return a[k-1]
a=[7,3,6,5,8,9]
print(kthsmal(a))


