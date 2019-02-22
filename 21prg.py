#21.Given an unsorted integer array as input,
#  return the number of odd numbers in it.
v=[]
def odd(v):
    for i in range(0,5):
        x=input("enter the num:")
        if not(x%2==0):
            v.append(x)
    return v
print(odd(v))