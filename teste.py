import math
import time
from list.linkedList import LinkedList
import time

def SieveOfEratosthenes(n):
    # 1 #2 #3 4 #5 6 #7 8 9 10 #11 12 #13

    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
   
    prime = [True for i in range(n+1)]
    
     
    p = 2
    while(p * p <= n):
          
        # If prime[p] is not changed, then it is
       # a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c  

def is_prime(x):

    if x < 2: 
        return False

    if x == 2:
        return True

    elif x % 2 == 0: 
        return False

    i = 2
    root = math.sqrt(x)
    while i <= root:
        if x % i == 0: return False
        i += 1

    return True

def calc(n):
    c = 0
    for j in range(n + 1):
        if is_prime(j):
            c += 1 

    return c
 
# Driver function
# t0 = time.time()
# print("start")
# c = SieveOfEratosthenes(1000000000)

# print("Total prime numbers in range:", c)
 


# import random
# list = [0, 1, 2, 3, 4, 5, 6]  

# for i in list[4:]:
#     pass
#     print(i)

#print(list[random.randint(2, 6)])


# p = 11 ** 17
# while True:
#     t0 = time.time()
#     if is_prime(p):
#         print(f"{p} é primo")
#         t1 = time.time()
#         print("tempo:", t1 - t0)  
        
#     p += 1

# file = open("prime\\safe filtered.txt")
# content = file.read()

# characters = ' ' # caracteres que serão substituídos

# for x in range(len(characters)):
#     content = content.replace(characters[x],"\n") # segundo argumento: caractere que será escrito

# print(content)

file = open("prime\\safest.txt", "r")

list = file.read().split()



print(list)