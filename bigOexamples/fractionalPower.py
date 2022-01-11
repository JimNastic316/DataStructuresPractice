'''
In this code sample we loop to sqrt(n) and do constant work at every step of the way. This can used to check whether a number is prime
'''

# O(sqrt(n))

from timethis import timethis
import time

@timethis
def is_prime(i):
    k = 2
    while k*k <= i:
        if (i%k == 0):
            return False
        k = k + 1
        time.sleep(0.01) #We need to insert an arbitrary delay otherwise it is too fast
    return True

print(is_prime(2))
print(is_prime(257))
print(is_prime(51031))
print(is_prime(9907))