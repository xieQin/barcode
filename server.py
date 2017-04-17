import sys
import pyotp
import time

shared_secret = 'udfasfterrdfdhqwshhjd'
user_id = 34623127
shared_prime = 7862958391

try:
    barcode = int(sys.argv[1])
except:
    barcode = 0

income_uid = barcode % shared_prime
print "%d" % income_uid
token = barcode / shared_prime
print "%d" % token

totp = pyotp.TOTP(shared_secret, digits=8, interval=60)
# hotp = pyotp.HOTP(shared_secret)

# time.sleep(0)
result = ( income_uid == user_id ) and totp.verify( str(token).zfill(6))

if result:
    print 'Accept'
else:
    print 'Reject'