import hashlib

test= "hap54./.1py"
result = hashlib.md5(test.encode())

print(result.hexdigest())