msg = [
    165,
    248,
    94,
    346,
    299,
    73,
    198,
    221,
    313,
    137,
    205,
    87,
    336,
    110,
    186,
    69,
    223,
    213,
    216,
    216,
    177,
    138,
]

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

pt = ""
for m in msg:
    pt += charset[m % 37]

print(f"picoCTF{{{pt}}}")
