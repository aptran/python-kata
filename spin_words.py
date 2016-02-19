'''
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
    words = sentence.split(' ')
    reversed = [w[::-1] if len(w) > 4 else w for w in words]
    return ' '.join(reversed)

# One liner solution
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])