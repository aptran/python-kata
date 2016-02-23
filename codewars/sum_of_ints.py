'''
Write this function

for i from 1 to n, do i % m and return the sum

f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
You'll need to get a little clever with performance, since n can be a very large number
'''

def f(n, m):
	n = int(n)
    m = int(m)
    res = triangle(m-1)
    res *= (n/m)
    res += triangle(n%m)
  
    return res
  
def triangle(n):
    return (n*(n+1))/2


# Another solution that introduced me to the divmod function
# def f(n, m):
#     re, c = divmod(n,m) 
#     return m*(m-1)/2*re + (c+1)*c/2