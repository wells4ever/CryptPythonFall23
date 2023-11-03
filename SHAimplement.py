from Crypto.Hash import SHA256

secret = 'Swordfish'
#message = secret + 'First' ->prefix 
message = 'First' + secret  #suffix
hash_object = SHA256.new(data=message.encode('ASCII'))
hash_object.update(b'Second')
hash_object.update(b'Third')
                   
print(hash_object.hexdigest())


total_message = secret + 'FirstSecondThird'
hash2 = SHA256.new(total_message.encode('ASCII'))

print(hash2.hexdigest())


#Bob verifies
r_message = 'FirstSecondThird' + secret
hash3 = SHA256.new(r_message.encode('ASCII'))
print(hash3.hexdigest())
