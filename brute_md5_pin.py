# brute_md5_pin.py
import hashlib

target = "0110b96270248f746ecca06f1ce09746" 

for i in range(1000000):                # 0 .. 999999
    pin = str(i).zfill(6)               # "000000" .. "999999"
    h = hashlib.md5(pin.encode()).hexdigest()
    if h == target:
        print("FOUND PIN:", pin)
        break
else:
    print("PIN tidak ditemukan")
