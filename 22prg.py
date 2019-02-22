#22.Given an unsorted integer array as input,
#  return the number of even numbers in it.

v=[]
def even(v):
    for i in range(0,5):
        x=input("enter the num:")
        if(x%2==0):
            v.append(x)
    return v
print(even(v))