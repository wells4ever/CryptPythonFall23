#Encrypt and Decrypt using 'toy' RSA
import sys

n = 15706649310938939849
e = 9325357729146031921
d = 6624414207545416681

#convert plaintext into integer
p = 'secret'
p_bytes = p.encode('ascii')
p_int = int.from_bytes(p_bytes, 'big') #big endian
print('message: ' + p)

#encrypt the message
y = pow(p_int, e, n)
print('y = ' + str(y))

#y is sent to the recipient

#decrypt the message
p_int_r = pow(y, d, n)
print('p_int_r = '+ str(p_int_r))

#convert integer back into plaintext
int_size = sys.getsizeof(p_int_r)
p_bytes = p_int_r.to_bytes(int_size, 'big') #big endian
p_r = p_bytes.decode('ascii')
p_r = p_r.lstrip('\x00')
print('recovered message: ' + p_r)
