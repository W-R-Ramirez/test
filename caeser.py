# Caeser Cipher

def encrypt(plaintext,shiftAmount):

    ciphertext = ''
    for letter in plaintext:

        # spaces stay spaces
        if letter == ' ':
            ciphertext += letter
        else:
            orderOfLetter = ord(letter)
            # shift capital letter
            if orderOfLetter < 91:
                # order of 'A' is 65
                # we first get a number between 0-25
                orderOfCipherLetter = ((orderOfLetter-65)+shiftAmount)%26
                # then we get the correct ascii order
                orderOfCipherLetter += 65
            # shift lower case
            else:
                orderOfCipherLetter = ((orderOfLetter-97)+shiftAmount)%26
                orderOfCipherLetter += 97
            # get the letter from the order
            cipherLetter = chr(orderOfCipherLetter)

            ciphertext += cipherLetter
    return ciphertext

def decrypt(ciphertext,shiftAmount):
    # negate the shiftAmount 
    return encrypt(ciphertext,-shiftAmount)
