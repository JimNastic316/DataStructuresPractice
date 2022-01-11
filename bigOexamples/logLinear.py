#
# O(n*log(n))

from timethis import timethis
import time

@timethis
def split_in_two(i):
    for j in range (i):
        k=i
        while k > 1:
            k = k/2
            time.sleep(0.01) #We need to insert an arbitrary delay otherwise it is too fast

split_in_two(50)
split_in_two(100)
split_in_two(200)
split_in_two(400)
split_in_two(800)
split_in_two(1600)