
'''
  Hackerank fibonacci modified 
'''
t1,t2,n = tuple(map(int, input().split()))

def f(n, memset= {1: t1, 2:t2}):
    if n in memset:
        return memset[n]
    else:
        return f(n-1) ** 2 + f(n-2) 
    
for i in range(n):
    a = f(n)


    
print(f(n))
    
