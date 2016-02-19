'''
Caesar Ciphers are one of the most basic forms of encryption.
It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments
 - key and message - and returns the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same.
All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
'''

def encryptor(key, message):    
    return ''.join(crypt(c,key) if c.isalpha() else c for c in message)
    
def crypt(c,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    is_cap = c.istitle()
    
    index = (alphabet.index(c.lower()) + key) % 26    
    return alphabet[index].upper() if is_cap else alphabet[index] 



# Another solution that introduced me to anonymous functions (lambda).

# from string import ascii_lowercase as l, ascii_uppercase as u
# def encryptor(key, message):
#     process = lambda x, abc: x in abc and abc[(abc.index(x) + key) % 26]
#     return ''.join(process(c, l) or process(c, u) or c for c in message) 