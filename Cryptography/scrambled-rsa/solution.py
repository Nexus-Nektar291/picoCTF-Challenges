from pwn import *
import string

alphabet = string.ascii_lowercase + string.digits + "CTF{_}"

plain_flag = ""
known = []

io = remote("mercury.picoctf.net", 50075)

io.recvuntil(b"flag: ")
cipher_flag = io.recvline().strip().decode()
io.recvlines(2)

while "}" not in plain_flag:
    for c in alphabet:
        payload = plain_flag + c
        io.sendafter(b"give me: ", payload + "\n")
        io.recvuntil(b"Here you go: ")
        cipher = io.recvline().strip().decode()
        for chunk in known:
            cipher = cipher.replace(chunk, "")

        if cipher in cipher_flag:
            cipher_flag = cipher_flag.replace(cipher, "")
            known.append(cipher)
            plain_flag += c
            print(plain_flag)
            break
