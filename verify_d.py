import hashlib
pin = "202345"
print(hashlib.md5(pin.encode()).hexdigest())
