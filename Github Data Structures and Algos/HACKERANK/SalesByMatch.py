'''
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''

def pairs(arr):
    pairdict = dict()
    for i in arr:
        if i in pairdict:
            pairdict[i] +=1 
        else:
            pairdict[i] = 1 
        
    s=0
    for i in pairdict:
        s += pairdict[i] // 2 
    return s

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  print(pairs(arr))
