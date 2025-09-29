# bruteforce_salt_pin.py
import hashlib

target = "8d4c531eb4b0f54df72aa6839abbeaec".lower()

def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

found = False
for s in map(str, range(10)):        # '0' .. '9'
    print("Trying salt =", s)
    for i in range(1000000):        # 0 .. 999999
        pin = str(i).zfill(6)
        h = md5_hex(s + pin)        # MD5(salt || PIN)
        if h == target:
            print("FOUND! salt =", s, "pin =", pin)
            found = True
            break
    if found:
        break

if not found:
    print("No match found.")
