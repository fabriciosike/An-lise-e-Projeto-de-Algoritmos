n = int(input())

def mdc(a, b):
    return a if not b else mdc(b, a % b)
    
for i in range(0, n):

    x,y = map(int, input().split())
   

    print(mdc(x, y)) 
    