'''
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * 4 ... N

zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
that has 2 trailing zeros 4790016(00)
Be careful 1000! has length of 2568 digital numbers.
'''

def zeros(n):
    count = 0
    acc = n
    while acc > 0:
        acc = acc / 5
        count += acc
    return count


# Recursive solution
# def zeros(n):
#     x = n/5
#     return x+zeros(x) if x else 0