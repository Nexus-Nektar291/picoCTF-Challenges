# split into blocks of 3 according to hint given in challenge:
# ['heT', 'fl ', 'g a', 's i', 'icp', 'CTo', '{7F', '4NR', 'P05', '1N5', '_16', '_35',
#  'P3X', '51N', '3_V', '091', 'B0A', 'E}2']

# looking at first block:
# h   e   t
# t   h   e

# scrambled[0] = original[1]
# scrambled[1] = original[2]
# scrambled[2] = original[0]

cipher = [
    "heT",
    "fl ",
    "g a",
    "s i",
    "icp",
    "CTo",
    "{7F",
    "4NR",
    "P05",
    "1N5",
    "_16",
    "_35",
    "P3X",
    "51N",
    "3_V",
    "091",
    "B0A",
    "E}2",
]


def unscramble_block(scrambled):
    return scrambled[2] + scrambled[0] + scrambled[1]


plaintext = ""
for scrambled in cipher:
    plaintext += unscramble_block(scrambled)

print(plaintext)
