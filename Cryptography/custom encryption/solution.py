# p = 97
# g = 31
# a = 94
# b = 21


# def generator(g, x, p):
#     return pow(g, x) % p


# u = generator(g, a, p)
# v = generator(g, b, p)
# key = generator(v, a, p)
# b_key = generator(u, b, p)

# print("u = ", u)
# print("v = ", v)
# print("key = ", key)
# print("b_key = ", b_key)

shared_key = 47

test_key = "trudeau"


def dynamic_xor_decrypt(cipher_text, text_key):
    decrypted = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted += decrypted_char
    return decrypted[::-1]


def decrypt(ciphertext, key):
    plaintext = ""
    for value in ciphertext:
        original_ord = value // (key * 311)
        plaintext += chr(original_ord)
    return plaintext


cipher = [
    131553,
    993956,
    964722,
    1359381,
    43851,
    1169360,
    950105,
    321574,
    1081658,
    613914,
    0,
    1213211,
    306957,
    73085,
    993956,
    0,
    321574,
    1257062,
    14617,
    906254,
    350808,
    394659,
    87702,
    87702,
    248489,
    87702,
    380042,
    745467,
    467744,
    716233,
    380042,
    102319,
    175404,
    248489,
]

semi_plain = decrypt(cipher, shared_key)
plaintext = dynamic_xor_decrypt(semi_plain, test_key)
print(plaintext)
