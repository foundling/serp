# Name a practical use for choosing to use a while loop over a for loop
# name as many immutable types as you can
# name as many mutable types as you can

def create_book_title(sentence, exclude=None):
    ''' capitalizes each word in the sentence, excepting any passed in via exclude iterable '''

    return


def remove_dashes(sentence, replacement_char=' '):
    ''' replace any dashes in sentence with replacement_char '''

    return


def encipher(content):
    ''' shift each character in the cipher text up by 7 '''

    cipher = ''

    for l in content:
        shifted = chr(ord(l) + 7)
        cipher += shifted

    return cipher


def decipher(cipher_text):
    ''' shift each character in the cipher text down by 7 '''

    deciphered_text = ''

    for l in cipher_text:
        deciphered_char = chr(ord(l) - 7)
        deciphered_text += deciphered_char 
    
    return deciphered_text
