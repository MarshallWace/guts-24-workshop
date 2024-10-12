import binascii
from Crypto.Cipher import DES
import os
import sys
import re

# If you're getting ModuleNotFoundError, try `pip install pycryptodome`

# I was looking into this hashing scheme called LANMAN the other day, wanted to make a lil
# challenge out of it, but it seemed a bit OP...
# For FLAG_EASY you should be able to bruteforce
# For FLAG_HARD brute force may still work with optimisation or if you know what you're doing with CUDA
# alternatively rainbow tables are a thing...

def prepare_des_key(key, complexity):
    # Convert the key to a binary string
    key = ''.join([bin(ord(char))[2:].zfill(8) for char in key])
    # Add parity bits to the key
    des_key = ''
    for i in range(0, len(key), complexity):
        chunk = key[i:i+complexity]
        parity_bit = '0' if chunk.count('1') % 2 == 0 else '1'
        des_key += chunk + parity_bit
    # Convert the binary string to bytes
    des_key = int(des_key, 2).to_bytes(8, byteorder='big')
    return des_key

def des_encrypt(clear_text, complexity):
    key = prepare_des_key(clear_text, complexity)
    des = DES.new(key, DES.MODE_ECB)
    encrypted_text = des.encrypt(b"KGS!@#$%")
    return binascii.hexlify(encrypted_text).decode('utf-8')

def lm_hash(password, complexity):
    if password is None:
        print('No password provided')
        sys.exit(1)
    if len(password) > complexity*2 or not bool(re.match(r'^[A-Z0-9]+$', password)):
        print('This password is too strong you maniac! We have no need for such complexity!')
        sys.exit(1)
    password = password.upper().ljust(complexity*2, '\0')
    part1, part2 = password[:complexity], password[complexity:]
    hash1, hash2 = des_encrypt(part1, complexity), des_encrypt(part2, complexity)
    return hash1 + hash2

flag_easy = os.getenv("FLAG_EASY")
flag_hard = os.getenv("FLAG_HARD")

print(lm_hash(flag_easy, complexity=4))
print(lm_hash(flag_hard, complexity=7))

# Output:
# d7f067637cd1df3e8731141dcca0f05d
# f889e2f3f596b67dfca021fafdcf0885

# Nb. the flag is not in the standard format. The cracked hash is the answer.
