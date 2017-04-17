import pyotp

shared_secret = 'udfasfterrdfdhqwshhjd'
user_id = 34623127
shared_prime = 7862958391

# generate token
totp = pyotp.TOTP(shared_secret, digits=8, interval=60)
# hotp = pyotp.HOTP(shared_secret)
token = int(totp.now())
# token = int(hotp.at(2))
print "%d" % token

barcode = user_id + shared_prime * token
print "%011d" % barcode