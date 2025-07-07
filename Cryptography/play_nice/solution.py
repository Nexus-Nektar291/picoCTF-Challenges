SQUARE_SIZE = 6

def generate_square(alphabet):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    matrix = []

    for i, letter in enumerate(alphabet):
        if i % SQUARE_SIZE == 0:
            row = []
        row.append(letter)

        if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
            matrix.append(row)
    return matrix


def get_index(letter, matrix):
    for row in range(SQUARE_SIZE):
        for col in range(SQUARE_SIZE):
            if matrix[row][col] == letter:
                return (row, col)
    print("letter not found in matrix.")
    exit()


def decrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:
        # Same row → shift left
        return (
            matrix[p1[0]][(p1[1] - 1) % SQUARE_SIZE]
            + matrix[p2[0]][(p2[1] - 1) % SQUARE_SIZE]
        )
    elif p1[1] == p2[1]:
        # Same column → shift up
        return (
            matrix[(p1[0] - 1) % SQUARE_SIZE][p1[1]]
            + matrix[(p2[0] - 1) % SQUARE_SIZE][p2[1]]
        )
    else:
        # Rectangle → swap columns
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


def decrypt_string(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i : i + 2], matrix)
    return plaintext


alphabet = "irlgektq8ayfp5zu037nov1m9xbc64shwjd2"
ciphertext = "h5a1sqeusdi38obzy0j5h3ift7s2r2"

matrix = generate_square(alphabet)
pt = decrypt_string(ciphertext, matrix)
print(pt)
