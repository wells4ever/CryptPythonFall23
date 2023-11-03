import random

def genKey(length) :
    key = ''
    for i in range(length):
        key += chr(ord('A') + random.randint(0,25))

    return key

def encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise Exception("Error: key length does not match plaintext length!")

           
    ciphertext = ''
    for i in range(len(plaintext)):
        c = ord(plaintext[i]) + (ord(key[i]) - ord('A'))
        if c > ord('Z'):
            c = c - 26

        ciphertext += chr(c)

    return ciphertext

def decrypt(ciphertext,key):
    if len(ciphertext) != len(key):
        raise Exception("Error: key length does not match ciphertext length!")

           
    plaintext = ''
    for i in range(len(ciphertext)):
        p = ord(ciphertext[i]) - ord(key[i]) - ord('A'))
        if p < ord('A'):
            p = p + 26

        plaintext += chr(p)

    return plaintext

if __name__ == '__main__':
    plaintext = 'ATTACKATDAWN'
    key = genKey(len(plaintext))
    print(key)

    ciphertext = encrypt(plaintext,key)
    print(ciphertext)

    plaintext2 = decrypt(ciphertext,key)
    print(plaintext2)

    

    
