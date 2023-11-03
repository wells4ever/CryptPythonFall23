from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from binascii import hexlify as hexa
from os import urandom

def generateMAC(message, secret_key):
    if type(message) is str:
        msg = message.encode('ascii')
    else:
        msg = message

    mac = Poly1305.new(key = secret_key, cipher = AES)
    mac.update(msg)

    return(mac.digest(), mac.nonce)


def verifyMAC(msg_bytes, mac_bytes, mac_nonce, secret_key):
    mac = Poly1305.new(key = secret_key, nonce = mac_nonce, cipher = AES, data = msg_bytes)

    try:
        mac.verify(mac_bytes)
        return True
    except ValueError:
        return False

    

if __name__ == '__main__':

#generate key
    key = urandom(32)
    
    plaintext = 'Attack at dawn!'
    msg_bytes = plaintext.encode('ascii')

#generate MAC and nonce using string message
    mac_bytes1, mac_nonce1 = generateMAC(plaintext, key)

    print(mac_bytes1)
    print(type(mac_bytes1))
    print(mac_nonce1)
    print(type(mac_nonce1))
    print("mac(%s) = %s" % (hexa(plaintext.encode('ascii')),hexa(mac_bytes1)))

#generate MAC and nonce using byte encoded message
    mac_bytes2, mac_nonce2 = generateMAC(msg_bytes, key)

    print("mac(%s) = %s" % (hexa(msg_bytes),hexa(mac_bytes2)))


#send following to recipient
#msg_bytes, mac_bytes, nonce

#verify MAC for first MAC and nonce
    if verifyMAC(msg_bytes, mac_bytes1, mac_nonce1, key):
        print("Message: '" + msg_bytes.decode('ascii') + "' is valid")

    else:
        print("Error: Message is invalid")

#verify MAC for second MAC and nonce
    if verifyMAC(msg_bytes, mac_bytes2, mac_nonce2, key):
        print("Message: '" + msg_bytes.decode('ascii') + "' is valid")

    else:
        print("Error: Message is invalid")
    

