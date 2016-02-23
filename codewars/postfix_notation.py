'''
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation)
 should evaluate to 14.

Note that for simplicity you may assume that there are always spaces between numbers and operations,
 e.g. 1 3 + expression is valid, but 1 3+ isn't.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
'''

def calc(expr):
    if not expr:
        return 0
    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}
    array = [float(i) if i not in ops else i for i in expr.split(" ")]
    stack = []
    
    for e in array:
        if e not in ops:
            stack.append(e)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append(ops[e](y,x))
            
    return stack.pop()