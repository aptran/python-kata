'''
In this kata, you will create an object that returns the positions and the values of the "peaks"
 (or local maxima) of a numeric array.

For example, the array arr = [ 0 , 1 , 2 , 5 , 1 , 0 ] has a peak in position 3 with a value of 5 (arr[3] = 5)

The output will be returned as an object with two properties: pos and peaks.
 Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) returns {pos:[3,7],peaks:[6,3]}

All input arrays will be valid numeric arrays (although it could still be empty),
 so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks
 (in the context of a mathematical function, we don't know what is after and before and therefore, 
    we don't know if it is a peak or not).

Also, beware of plateaus !!! [1,2,2,2,1] has a peak while [1, 2, 2, 2, 3] does not.
 In case of a plateau-peak, please only return the position and value of the beginning of the plateau.
  For example: pickPeaks([1,2,2,2,1]) returns {pos:[1],peaks:[2]}
'''


def pick_peaks(arr):
    pos = []
    peaks = []
    
    if not arr:
        return {'pos': pos, 'peaks': peaks}
    
    plats = []
    for i,n in enumerate(arr):
        if i > 0 and i < len(arr)-1:
            if n == arr[i+1] and n != arr[i-1]:
                plats.append([i,n])
            elif n == arr[i-1] and n != arr[i+1]:
                plats.append([i,n])
            elif n > arr[i-1] and n >= arr[i+1]:
                check_plats(plats,pos,peaks,arr)
                pos.append(i)
                peaks.append(n)

    check_plats(plats,pos,peaks,arr)

    return {'pos': pos, 'peaks': peaks}

def check_plats(plats,pos,peaks,arr):
    if len(plats) > 1:
        end = plats.pop()
        start = plats.pop()
        if end[0] < len(arr)-1 and start[0] > 1:
            if start[1] >= arr[start[0]-1] and end[1] >= arr[end[0]+1]:
                pos.append(start[0])
                peaks.append(start[1])                
    elif plats:
        plats.pop()


# Cleaner solution evaluating plateaus as they appear
# def pick_peaks(arr):
#     pos = []
#     prob_peak = False
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             prob_peak = i
#         elif arr[i] < arr[i-1] and prob_peak:
#             pos.append(prob_peak)
#             prob_peak = False
#     return {'pos':pos, 'peaks':[arr[i] for i in pos]}


