from pwn import *

context.log_level = "Error"

keylen = 50000
io = remote("mercury.picoctf.net", 11188)

io.recvlines(2)
enc_flag = io.recvline()
io.sendlineafter(b"encrypt? ", b"A" * (keylen - 32))
io.sendlineafter(b"encrypt? ", bytes.fromhex(enc_flag.decode()))
io.recvline()

flag = bytes.fromhex(io.recvline().decode()).decode()
print(f"picoCTF{{{flag}}}")
