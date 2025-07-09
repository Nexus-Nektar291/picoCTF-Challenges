from Crypto.Util.number import *
from pwn import *
import itertools
import hashlib
import sys


def proof_of_work(prefix, desired):
    for c in itertools.combinations_with_replacement(string.ascii_letters, 6):
        guess = prefix + "".join(c)
        if hashlib.md5(guess.encode()).hexdigest()[-6:] == desired:
            return guess


io = remote("mercury.picoctf.net", 41175)
io.recvuntil(b'starts with "')
prefix = io.recv(5).decode()

io.recvuntil(b"six hex digits: ")
desired = io.recv(6).decode()

print("Proof of work with prefix ", prefix, " and desired ", desired)
ans = proof_of_work(prefix, desired)
print("Sending solution : ", ans)
io.sendline(str(ans).encode())

io.recvuntil(b"Public Modulus :  ")
n = int(io.recvline())

io.recvuntil(b"Clue :  ")
e = int(io.recvline())

print("Got values of n & e.")
# =================================================================================

while True:
    m = getPrime(20)
    print("Trying : ", str(m))
    m1 = pow(m, e, n)
    dp = 1
    for i in range(1 << 20):
        dp = (dp * m1) % n
        g = GCD(dp - m, n)
        print(i, dp, g)
        if g != 1:
            p = g
            q = n // p
            print("p : ", p)
            print("q : ", q)
            io.sendline(str(p + q).encode())
            print(io.recvline())
            sys.exit()
