#26.Given an unsorted integer array as input,
 #find the Kth largest/smallest element in the array

def kthbig(a):
    a.sort()
    k=input("enter the num:")
    return a[-k]
a=[7,3,6,5,8,9]
print(kthbig(a))

