import hashlib
import sys

# Allow large integer string parsing (needed for 10,000+ digit integers)
sys.set_int_max_str_digits(50000)

# Constants
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex(
    "42cbbce1487b443de1acf4834baed794f4bbd0dfe7d7086e788af7922b"
)


def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print("Decrypted flag: ", flag)


if __name__ == "__main__":
    # The large precomputed solution value (mod 10^10000) is stored in result.txt
    with open("result.txt", "r") as f:
        solution_value = int(f.read().strip())

    decrypt_flag(solution_value)
