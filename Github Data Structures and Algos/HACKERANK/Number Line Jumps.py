x1, v1, x2, v2 = list(map(int, input().split()))
y=False
if v1 > v2 :
    while x2 > x1:
        x1 += v1
        x2 += v2 
        if x1 == x2:
            print("YES")
            y=True 
elif v2 > v1:
    while x1 > x2:
        x1 += v1
        x2 += v2
        if x1 == x2:
            print("YES")
            y=True 
if not y:
    print("NO")
