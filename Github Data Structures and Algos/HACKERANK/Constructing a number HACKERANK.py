n = int(input())
for _ in range(n):
    t = int(input())
    q = list(map(str, input().split()))
    sum = 0
    for i in q:
        for number in map(int, list(i)):
            sum += number
    if sum % 3:
        print("No")
    elif not sum % 3:
        print("Yes")
