'''

https://www.hackerrank.com/challenges/summing-the-n-series/problem
'''
def f(n):
    return (n**2 - (n-1) ** 2) % (10**9 + 7)
m = 10 ** 9 +7 
if __name__== "__main__":
    t = int(input())
    for i in range(t):
        answer = int(input()) ** 2
        print(answer % m)
        
