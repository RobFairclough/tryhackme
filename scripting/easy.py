from base64 import b64decode
base64 = open('easychallenge.txt', 'r').read()
decode = base64
for i in range(0, 50):
    decode = b64decode(decode)
print(decode)