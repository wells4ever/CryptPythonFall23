from Crypto.Cipher import AES
from os import urandom

if __name__ == '__main__':
    #generate a key
    key = urandom(32)

    header = 'Header Information'
    plaintext = 'Attack at dawn'

    #convert strings to bytes
    headerBytes = header.encode('ascii')
    plainBytes = plaintext.encode('ascii')

    # Instantiate cipher
    cipher = AES.new(key, AES.MODE_GCM) #nonce auto generates if not specified
    cipher.update(headerBytes)
    ciphertext, authTag = cipher.encrypt_and_digest(plainBytes)
    genNonce = cipher.nonce

    #assume key was securely shared beforehand
    #ciphertext, authTag, nonce, and headerBytes sent
    #receiver authenticates then decrypts
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce = genNonce)
        cipher.update(headerBytes)
        plaintext = cipher.decrypt_and_verify(ciphertext, authTag)
        print('Message received: ' + plaintext.decode('ascii'))
    except(ValueError, KeyError):
        print('Error, incorrect decryption')
