from Crypto.Util.number import long_to_bytes, bytes_to_long

ctxt = long_to_bytes(
    0x57657535570C1E1C612B3468106A18492140662D2F5967442A2960684D28017931617B1F3637
)
key = b"Africa!"
random_strs = [
    b"my encryption method",
    b"is absolutely impenetrable",
    b"and you will never",
    b"ever",
    b"break it",
]


def encrypt(ptxt, key):
    ctxt = b""
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt


for _ in range(2):
    ctxt = encrypt(ctxt, random_strs[0])
    for _ in range(2):
        ctxt = encrypt(ctxt, random_strs[1])
        for _ in range(2):
            ctxt = encrypt(ctxt, random_strs[2])
            for _ in range(2):
                ctxt = encrypt(ctxt, random_strs[3])
                for _ in range(2):
                    ctxt = encrypt(ctxt, random_strs[4])
                    a = encrypt(ctxt, key)
                    print(a)
