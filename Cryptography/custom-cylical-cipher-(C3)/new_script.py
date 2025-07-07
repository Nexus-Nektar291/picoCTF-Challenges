with open("code.txt", "r") as f:
    c = f.read()

b = 1
flag = ""
for i in range(len(c)):
    if i == b * b * b:
        flag += c[i]
        b += 1

print(f"picoCTF{{{flag}}}")
