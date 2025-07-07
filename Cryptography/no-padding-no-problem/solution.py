from pwn import *
from Crypto.Util.number import long_to_bytes

context.log_level = "Error"

io = remote("mercury.picoctf.net", 30048)

io.recvuntil(b"n: ")
n = int(io.recvline())

io.recvuntil(b"ciphertext: ")
ct = int(io.recvline())

payload = str(n + ct).encode()
io.sendline(payload)

io.recvuntil(b"Here you go: ")
flag = long_to_bytes(int(io.recvline().strip())).decode()
print(flag)

