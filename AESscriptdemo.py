#!/usr/bin/env python   
    #run program as a script
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import hexlify as hexa
from os import urandom
from struct import unpack

k = urandom(16)
print(" k = %s " % hexa(k))

#pick a starting value for counter

nonce = unpack('<Q', urandom(8))[0]

#instantiate a counter function
ctr = Counter.new(128, initial_value = nonce)

#pick an instance of AES in CTR mode, using ctr as counter
aes = AES.new(k, AES.MODE_CTR, counter = ctr)
#non need for an entire block with CTR mode
p = b'secret message'

#encrypt p
c = aes.encrypt(p)
print('enc(%s) = %s' % (hexa(p), hexa(c)))

#c and nonce are sent to recipient...

#decrypt using the encrypt function
ctr = Counter.new(128, initial_value = nonce)
aes = AES.new(k, AES.MODE_CTR, counter = ctr)
p = aes.encrypt(c)
print('enc(%s) = %s' % (hexa(c), hexa(p)))
print(str(p))
