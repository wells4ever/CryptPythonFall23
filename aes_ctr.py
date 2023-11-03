#Philip Wells
#COSC 4367.001
#Homework 03
#Date of Submission 10/02/2023



from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack


key = urandom(16)   #generate 16 bit key
print('key = %s' % hexa(key))


def encrypt(plaintext,key):
    p = plaintext.encode() #convert string to bytes
    nonce = unpack('<Q', urandom(8))[0] #generate nonce
    ctr = Counter.new(128,initial_value=nonce) #instantiate counter
    aes = AES.new(key, AES.MODE_CTR, counter=ctr) #create AES instance
    ciphertext = aes.encrypt(p)
    print('enc(%s) = %s' % (hexa(p), hexa(ciphertext))) #prints encrypted value
    return (ciphertext, nonce)

def decrypt(ciphertext,key, nonce):
    ctr = Counter.new(128, initial_value=nonce) #instantiate counter
    aes = AES.new(key, AES.MODE_CTR, counter=ctr) #create AES instance
    p = aes.encrypt(ciphertext)
    print('enc(%s) = %s' % (hexa(ciphertext), hexa(p))) #prints decrypted values
    plaintext = p.decode() #convert bytes to string
    return (plaintext)

if __name__ == '__main__':
    plaintext = input('enter message')
    ciphertext, nonce = encrypt(plaintext,key)
    receivedtext = decrypt(ciphertext,key,nonce)
    print(receivedtext)
