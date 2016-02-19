'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

def is_isogram(string):
    string = string.lower()
    for i,s in enumerate(string):
        if s in string[i+1:]:
            return False
    return True


# Another person's solution that introduced me to the set() method
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))