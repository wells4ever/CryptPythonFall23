import hashlib

h_a = hashlib.sha256(b'SPREADTHENET').hexdigest()
h_b = hashlib.sha512(b'b').hexdigest()
h_c = hashlib.sha512(b'c').hexdigest()

print(h_a)
print(h_b)
print(h_c)
