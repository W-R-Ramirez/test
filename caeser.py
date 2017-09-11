# Caeser Cipher

def encrypt(plaintext,shiftAmount):

    ciphertext = ''
    for letter in plaintext:

        orderOfLetter = ord(letter)
        # shift capital letter
        if orderOfLetter > 64 and orderOfLetter < 91:
            # order of 'A' is 65
            # we first get a number between 0-25
            orderOfCipherLetter = ((orderOfLetter-65)+shiftAmount)%26
            # then we get the correct ascii order
            orderOfCipherLetter += 65
        # shift lower case
        elif orderOfLetter > 96 and orderOfLetter < 123:
            orderOfCipherLetter = ((orderOfLetter-97)+shiftAmount)%26
            orderOfCipherLetter += 97
        # everything else stays the same
        else:
            orderOfCipherLetter = orderOfLetter
        # get the letter from the order
        cipherLetter = chr(orderOfCipherLetter)

        ciphertext += cipherLetter
    return ciphertext

def decrypt(ciphertext,shiftAmount):
    return encrypt(ciphertext,-shiftAmount)
