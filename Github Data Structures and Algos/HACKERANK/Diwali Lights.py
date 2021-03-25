'''
  https://www.hackerrank.com/challenges/diwali-lights/problem
'''
def lights(n):
    m = 10 ** 5
    return (( 2 ** n ) - 1 ) % m  
t= int(input())
for i in range(t):
    print(lights(int(input())))


