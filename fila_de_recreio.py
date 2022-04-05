n = int(input())

while(n>0):
    n-=1
    m = int(input())
    p = list(map(int, input().split()))
    aux = sorted(p, reverse = True)


    cont=0
    
    for i in range(0,m): 
        if p[i]==aux[i]:
            cont+=1
    
    print(cont)
