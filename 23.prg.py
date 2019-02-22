# #23.Given an unsorted integer array as input,
# # return the number of prime numbers in it.


# prime=[]
# for i in range(2,21):
#     isPrime =True
    
#     for n in range(2,i):
#         if (i%n==0):
#          isPrime=False
#         if isPrime:
#          prime.append(i)
# print (i)
# def prime(x):

#         prime=[]

#         for i in range(0,11):
        
#                 isPrime=True
#                 for j in range(2,i):
#                         if(i%j==0):
#                                 isPrime=False
#                                 break
#         if isPrime:
#                 prime.append(i)
# x=int(input("enter the num:"))
# print(prime)


def isprime(array):
        
        prime=[]
        for x in range(0,len(array)):
                isprime=False
                for j in range(0,len(array)):
                        if not(x%j==True):
                                prime.append(x)
        return prime

array=[1,5,3,2,8,9]
print(isprime(array))
