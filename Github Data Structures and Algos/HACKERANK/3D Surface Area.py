# https://www.hackerrank.com/challenges/3d-surface-area/problem
def main():
  m,n = tuple(map(int, input().split()))
  DP =[]
  for _ in range(m):
      DP.append(list(map(int, input().split())))
  SA = 0 

def validateSides(i,j,DP, SA):
    top = False 
    bottom = False 
    left = False 
    right = False 
    if i-1 <0 :
        SA += DP[i][j]
        top = True 
    if i + 1 >= m:
        SA += DP[i][j]
        bottom = True 
    if j-1 <0:
        SA += DP[i][j]
        left = True 
    if j + 1 >= n:
        SA += DP[i][j]
        right = True 

    if not right:
        SA += max(0,DP[i][j] - DP[i][j+1])
    if not left:
        SA += max(0,DP[i][j] - DP[i][j-1])
    if not top:
        SA += max(0,DP[i][j] - DP[i-1][j])
    if not bottom:
        SA += max(0,DP[i][j] - DP[i+1][j])

    return SA 




  for i in range(m):
      for j in range(n):
          SA = validateSides(i,j,DP,SA)

  print(SA + 2*(m*n))   
 
if __name__=="__main__":
  main()

        
        
       
