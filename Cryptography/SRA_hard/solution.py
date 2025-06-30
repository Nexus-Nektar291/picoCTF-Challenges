from Crypto.Util.number import *
from sympy import divisors
from itertools import combinations
from math import log2

from pwn import *


def all_primes(modulus: int):
    result = []
    for d in divisors(modulus - 1):
        if isPrime(d + 1):
            result.append(d + 1)

    return result


def keep_127bit(prime_list):
    return [p for p in prime_list if log2(p) // 1 == 127]


def find_correct_pq(list, d):
    for p, q in combinations(list, 2):
        if d == inverse(65537, (p - 1) * (q - 1)):
            return p, q

    return None


io = remote("saturn.picoctf.net", 55000)
io.recvuntil(b"anger = ")
ct = int(io.recvline().strip())
io.recvuntil(b"envy = ")
d = int(io.recvline().strip())

e = 65537

p, q = find_correct_pq(keep_127bit(all_primes(d * e)), d)

N = p * q

pt = long_to_bytes(pow(ct, d, N))
io.sendline(pt)
io.interactive()
