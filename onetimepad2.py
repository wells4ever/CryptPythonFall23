from binascii import hexlify as hexa
from os import urandom

def genKey(length):
    return urandom(length)

def encrypt(plaintext,key):
    raw = plaintext.encode()
    print('raw = %s' % hexa(raw))

    ciphertext = bytes([raw[i] ^ key[i] for i in range(len(raw))])
    print('ciphertext = %s' % hexa(ciphertext))

    return ciphertext

def decrypt(ciphertext,key):
    raw = []
    for i in range(len(ciphertext)):
        raw.append(ciphertext[i] ^ key[i])
    print('bytes list = ' + str(raw))
    raw2 = bytes(raw)

    print('raw2  = %s' % hexa(raw2))
    plaintext = raw2.decode('ASCII')
    
    return plaintext

    

if __name__ == '__main__':
    plaintext = 'ATTACKATDAWN'
    key = genKey(len(plaintext))
    print('key = %s' % hexa(key))

    ciphertext = encrypt(plaintext,key)
    
    plaintext2 = decrypt(ciphertext,key)
    print('plaintext2 = ' + plaintext2)
