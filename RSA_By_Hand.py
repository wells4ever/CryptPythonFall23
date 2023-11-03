#RSA Key Generation

from Crypto.Util import number
from os import urandom

base_size = 32

#generate p & q
p = number.getPrime(base_size, urandom)
q = number.getPrime(base_size, urandom)

print('p    = ' + str(p))
print('q    = ' + str(q))

#use p & q to calculate n
n = p * q
print('n    = ' + str(n))

phi = (p-1)*(q-1)
print('phi  = ' + str(phi))

#generate e
phi_bits = number.size(phi)
e = phi
while e>= phi:
    e = number.getPrime(phi_bits, urandom)
print('e    = ' + str(e))

#generate d
d = number.inverse(e,phi)
print('d    = ' + str(d))

#confirm that e & d are inverses
test = (e * d) % phi
print('test = ' + str(test))
