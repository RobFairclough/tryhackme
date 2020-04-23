import socket
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/#cryptography.hazmat.primitives.ciphers.modes.GCM
def decrypt(key, iv, ciphertext, tag):
    algorithm = algorithms.AES(key)
    mode = modes.GCM(iv, tag)
    decryptor = Cipher(algorithm, mode, backend=default_backend()).decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

host = '10.10.91.28' # machine ip
port = 4000
resBytes = 2048
sock = socket.socket(
    socket.AF_INET, # internet
     socket.SOCK_DGRAM # udp
)
sock.connect((host, port))

payload1 = b'hello'
sock.send(payload1)
res = sock.recv(resBytes)
# You've connected to the super secret server, send a packet with the payload ready to receive more information

payload2 = b'ready'
sock.send(payload2)
res = sock.recv(resBytes)
# key:thisisaverysecretkeyl337 iv:secureivl337 to decrypt and find the flag that has a SHA256 checksum of {unreadable, saved in notes} send final in the next payload to receive all the encrypted flags
# should probably pull these out code-side
key = b'thisisaverysecretkeyl337'
iv = b'secureivl337'
# get this out in a nicer/more reliable way, regex? split somewhere? either kind of relies on knowing the response well enough that it's moot
checksum = res[104:136]
readableChecksum = checksum.hex()
finalPayload = b'final\n'

found = False
while found is False:
    # get encrypted plaintext
    sock.send(finalPayload)
    ciphertext = sock.recv(resBytes)
    # get encrypted tag
    sock.send(finalPayload)
    tag = sock.recv(resBytes)

    # decrypt
    decrypted = (decrypt(key, iv, ciphertext, tag))
    # confirm checksum matches 
    sha256 = hashlib.sha256(decrypted).hexdigest()
    if (sha256 == readableChecksum):
        print('this is the flag: ', decrypted)
        sock.close()
        found = True