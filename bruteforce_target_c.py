# bruteforce_target_c.py
import hashlib

TARGET = "b20f8b0405b88e2b0b50eb3356d34ba7".lower()

def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

found = False
for s in map(str, range(10)):  # '0'..'9'
    print("Trying salt =", s)
    for i in range(1000000):   # 0..999999
        pin = str(i).zfill(6)
        h0 = s + pin
        h1 = md5_hex(h0)
        h2 = md5_hex(h1)
        h3 = md5_hex(h2)
        if h3 == TARGET:
            print("FOUND! salt =", s, "pin =", pin)
            found = True
            break
    if found:
        break

if not found:
    print("No match found.")
