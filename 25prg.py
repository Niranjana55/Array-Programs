#25.Given an unsorted integer array as input,
# find the second largest/smallest element in the array.

def lar_sml(a):
    #length=len(a)
    a.sort()#a=[4,5,6,7,8,9]
    print("lar num:",a[-1] )
    print("second lar num:",a[-2] )
    print("sml num:",a[0])
    print("second sml num:",a[1])

a=[5,7,9,8,6,4]
print(lar_sml(a))
