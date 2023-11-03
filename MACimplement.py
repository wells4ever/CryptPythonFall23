from Crypto.Hash import HMAC, SHA256

#On the sender side, generate the MAC

secret = 'Swordfish'
message = 'Hello'

hex_secret = secret.encode('ASCII')
hex_message = message.encode('ASCII')

mac = HMAC.new(hex_secret, digestmod=SHA256)
mac.update(hex_message)
print(mac.hexdigest())

#receiving hex_message and the MAC 'mac'

recalc_mac = HMAC.new(hex_secret, digestmod=SHA256)
recalc_mac.update(hex_message)
print(recalc_mac.hexdigest())

try:
    recalc_mac.hexverify(mac.hexdigest())
    print("The message  '%s' is authentic" % message)
except ValueError:
    print("The message or key is wrong")

