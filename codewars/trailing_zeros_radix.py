'''
How many zeroes are at the end of the factorial of 10? 10! = 3628800, i.e. there are two zeroes.
16! in hexadecimal would be 0x130777758000, which results in three zeroes.

Unfortunately machine integer numbers has not enough precision for larger values.
Floats drops the tail we need. We can fall back to arbitrary-precision ones - built-ins or from a library,
 but calculating the full product isn't an efficient way to find the tail of the factorial.
Calculating 100'000! takes around 10 seconds on my machine, let alone 1'000'000!.

Your task is to write a function, which will find number of zeroes at the end of (number)
 factorial in arbitrary radix = base for larger numbers.

base is an integer from 2 to 256
number is an integer from 1 to 1'000'000
'''

def zeroes (base, number):
    prime_fac = pf(base)
    prime_fac = dict((x,prime_fac.count(x)) for x in set(prime_fac))
    count = []
    for k,v in prime_fac.iteritems():
        num = number
        i = 0
        while num > 0:
            num = num / k
            i += num
        count.append(i/v)

    return min(count)
  
def pf(n):
    i = 2
    prime_fac = []
    num = n
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_fac.append(i)
    if n > 1:
        prime_fac.append(n)
    return prime_fac