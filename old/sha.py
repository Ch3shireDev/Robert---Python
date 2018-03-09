import hashlib as h

x = h.sha256(b"aaab").hexdigest()

print(x[1])