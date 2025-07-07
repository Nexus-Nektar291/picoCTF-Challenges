from Crypto.Util.number import *

msg = [
    104,
    372,
    110,
    436,
    262,
    173,
    354,
    393,
    351,
    297,
    241,
    86,
    262,
    359,
    256,
    441,
    124,
    154,
    165,
    165,
    219,
    288,
    42,
]

charset = "_abcdefghijklmnopqrstuvwxyz012345678_"

pt = ""
for m in msg:
    m = m % 41
    m = inverse(m, 41)
    pt += charset[m % 37]

print(f"picoCTF{{{pt}}}")
