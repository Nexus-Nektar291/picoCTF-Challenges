chars = ""
with open("ciphertext") as f:
    for line in f:
        chars += line

i = 0
b = 1
while (b**3) < len(chars):
    print(chars[b**3], end="")
    b += 1
