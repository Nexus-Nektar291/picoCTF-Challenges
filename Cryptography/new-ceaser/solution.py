import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(cipher):
    dec = ""
    for c in range(0, len(cipher), 2):
        b = ""
        b += "{0:04b}".format(ALPHABET.index(cipher[c]))
        b += "{0:04b}".format(ALPHABET.index(cipher[c + 1]))
        dec += chr(int(b, 2))

    return dec


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for key in ALPHABET:
    s = ""
    for i, c in enumerate(enc):
        s += unshift(c, key[i % len(key)])
    s = b16_decode(s)
    print(s)

# e is the correct key:
# flag = picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}
