from binascii import hexlify as hexa
from os import urandom
import AESFunctions
import MACFunctions

if __name__ == '__main__':
    
    #generate keys
    key1 = urandom(32) #MAC 
    key2 = urandom(32) #AES

    plaintext = 'Attacck at dawn!'

    #generate MAC and nonce
    mac_bytes, mac_nonce = macFunctions.generateMAC(plaintext, key1)
    print("mac(%s) = %s" % (hexa(plaintext.encode('ascii')), hexa(mac_bytes)))

    #combine plaintext with MAC and nonce -- structure is not important as long as both sender and receiver know the structuring
    combined = mac_bytes + mac_nonce + plaintext.encoded('ascii')

    #encrypt the combined MAC, nonce, and plaintext
    cipher_bytes, cipher_nonce = aesFunctions.encrypt(combined, key2)
    print("enc(%s) = %s" % (hexa(plaintext.encode('ascii')), hexa(cipher_bytes)))

    #send the following to the recipient:
    #cipher_bytes, cipher_nonce

    #decrypt ciphertext
    recovered_bytes = aesFunctions.decrypt(cipher_bytes, cipher_nonce, key2)

    r_mac_bytes = recovered_bytes[0:16]
    r_mac_nonce = recovered_bytes[16:32]
    r_message = recovered_bytes[32:]

    if macFunctions.verifyMAC(r_message, r_mac_bytes, r_mac_nonce, key1):
        print("Message: '" + r+message.decode('ascii') + "' is valid")
    else:
        print('Message is invalid')
