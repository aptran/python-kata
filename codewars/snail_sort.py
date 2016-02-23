'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest;
 the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as [[]]
'''

def snail(array):
    if len(array[0]) == 0:
        return []
        
    snail_array = []
    n = len(array)
    start = 0
    while n > start:
        for i in xrange(start,n):
            snail_array.append(array[start][i])     
            
        for i in xrange(start+1,n):
            snail_array.append(array[i][n-1])

        snail_array.extend(array[n-1][start:n-1][::-1])

        start += 1
                
        for i in xrange(n-1,start,-1):
            snail_array.append(array[i-1][start-1])  
        n -= 1
        
    return snail_array


 # Recursive implementation with zip and reverse
 # def snail(array):
 #    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []


 # Iterative implementation
 # def snail(array):
 #    a = []
 #    while array:
 #        a.extend(list(array.pop(0)))
 #        array = zip(*array)
 #        array.reverse()
 #    return a


