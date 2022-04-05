from heapq import heappush, heappop
from bisect import bisect, insort
n = int(input())


def getNumOfInversions(A):
    N = len(A)
    if N <= 1:
        return 0
 
    sortList = []
    result = 0
 
    # heapsort, O(N*log(N))
    for i, v in enumerate(A):
        heappush(sortList, (v, i))
 
    x = []  # create a sorted list of indexes
    while sortList:  # O(N)
        v, i = heappop(sortList)  # O(log(N))
        # find the current minimum's index
        # the index y can represent how many minimums on the left
        y = bisect(x, i)  # O(log(N))
        # i can represent how many elements on the left
        # i - y can find how many bigger nums on the left
        result += i - y
 
        insort(x, i)  # O(log(N))
 
    return result
 
while(n>0):
    n-=1
    l = int(input())
    vagoes = list(map(int, input().split()))
    result = getNumOfInversions(vagoes)
    print('Optimal train swapping takes %d swaps.' % result)
 

        




