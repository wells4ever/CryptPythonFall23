from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from binascii import unhexlify

#sender
secret = b'Thirtytwo very very secret bytes'
mac = Poly1305.new(key=secret, cipher=AES)
mac.update(b'Hello')
print('Nonce: ' , mac.nonce.hex())
print('MAC:   ', mac.hexdigest())

#receiver receives message, the MAC 'mac_tag_hex' , nonce 'nonce_hex'
message = b'Hello'
mac_tag_hex = mac.hexdigest()
nonce_hex = mac.nonce.hex()

nonce = unhexlify(nonce_hex)
recalc_mac = Poly1305.new(key=secret, nonce=nonce, cipher=AES, data=message)

try:
    recalc_mac.hexverify(mac_tag_hex)
    print("The message '%s' is authentic" % message)
except ValueError:
    print("The message is not authentic")

