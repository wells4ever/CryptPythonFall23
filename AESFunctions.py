#purpose: encrypt & decrypt using AES w/ counter mode

from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import urandom
from struct import unpack
from binascii import hexlify as hexa

#Encrypt message using AES Counter Mode
def encrypt(plaintext, key):
    
    #check plaintext type and convert if needed
    if type(plaintext) is str:
        plain_bytes = plaintext.encode('ascii')
    else:
        plain_bytes = plaintext

    #pick a starting value for counter
    nonce = unpack('<Q', urandom(8))[0]

    #instantiate a counter
    ctr = Counter.new(128, initial_value = nonce)

    #pick an instance of AES in counter mode, ctr as counter
    aes = AES.new(key, AES.MODE_CTR, counter = ctr)

    #encrypt byte representation of plaintext (plain_bytes)
    ciphertext = aes.encrypt(plain_bytes)

    return (ciphertext, nonce)

#decrypt message using AES Counter Mode
def decrypt(ciphertext, nonce, key):
    
    #instantiate a counter
    ctr = Counter.new(128, initial_value = nonce)

    #pick an instance of AES in Counter mode, ctr as counter
    aes = AES.new(key, AES.MODE_CTR, counter = ctr)

    #decrypt byte representation of ciphertext
    plain_bytes = aes.encrypt(ciphertext)

    return (plain_bytes)
    
if __name__ == '__main__':

    #generate a key
    key = urandom(32) #used for AES (256 bits)
    
    plaintext = 'Attack at dawn!'

    #encrypt the plaintext
    cipher_bytes1, cipher_nonce1 = encrypt(plaintext, key)
    print('c1: ', 'enc(%s) = %s' % (hexa(plaintext.encode('ascii')), hexa(cipher_bytes1)))
    
    #encrypt the bytes representation of plaintext
    msg_bytes = plaintext.encode('ascii')
    cipher_bytes2, cipher_nonce2 = encrypt(msg_bytes, key)
    print('c2: ','enc(%s) = %s' % (hexa(msg_bytes), hexa(cipher_bytes2)))

    #send the following to the recipient
        #cipher_bytes, cipher_nonce

    #decrypt the ciphertext
    recovered_msg = decrypt(cipher_bytes1, cipher_nonce1, key)
    print('c1: ','enc(%s) = %s' % (hexa(cipher_bytes1), hexa(recovered_msg)))
    print("recovered message = " + recovered_msg.decode('ascii'))
    
    #decrypt the ciphertext
    recovered_msg2 = decrypt(cipher_bytes2, cipher_nonce1, key)
    print('c2: ','enc(%s) = %s' % (hexa(cipher_bytes2), hexa(recovered_msg2)))
    print("recovered message = " + recovered_msg.decode('ascii'))
    
                    
