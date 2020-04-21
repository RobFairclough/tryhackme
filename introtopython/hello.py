#hello world
print('hello world')
if (True is True):
    print('true')
# while True:
    # print('lol')

# files
text = open('test.txt', 'w')
text.write('writing to a file')
text.writelines('again and ')
text.writelines('again and ')
text.writelines('again and ')
text.writelines('again')

# challenge
from base64 import *
encodedString = open('encodedflag.txt', 'r').read()
print(encodedString)


for i in range(0, 5):
    encodedString = b16decode(encodedString)
for i in range(0, 5):
    encodedString = b32decode(encodedString)
for i in range(0, 5):
    encodedString = b64decode(encodedString)
print(encodedString)