from argparse import ArgumentParser, ArgumentTypeError
import sys


ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_INDEX = {char: index for index, char in enumerate(ALPHABET)}

def parse_key(value: str) -> int:
    ivalue = int(value)
    min_value = 1
    max_value = len(ALPHABET) - 1
    if ivalue < min_value or max_value < ivalue:
        raise ArgumentTypeError(f"Key value {ivalue} is not allowed, possible values between {min_value} and {max_value}")
    return ivalue

ENCRYPT = "encrypt"
DECRYPT = "decrypt"

parser = ArgumentParser()
parser.add_argument("--key", type=parse_key, required=True)
parser.add_argument("--action", choices=[ENCRYPT, DECRYPT], default=ENCRYPT)

args = parser.parse_args()


def encrypt(value: str, key: int) -> str:
    value = value.upper()
    result = []
    for c in value:
        index_in_alphabet = ALPHABET_INDEX.get(c)
        if index_in_alphabet is not None:
            new_index = (index_in_alphabet + key) % len(ALPHABET)
            result.append(ALPHABET[new_index])
            stop = True
        else:
            result.append(c)

    return "".join(result)


def decrypt(value: str, key: int) -> str:
    value = value.upper()
    result = []
    for c in value:
        index_in_alphabet = ALPHABET_INDEX.get(c)
        if index_in_alphabet is not None:
            new_index = (index_in_alphabet - key) % len(ALPHABET)
            result.append(ALPHABET[new_index])
            stop = True
        else:
            result.append(c)

    return "".join(result)


if args.action == ENCRYPT:
    for line in sys.stdin:
        print(encrypt(line.strip("\n"), args.key), file=sys.stdout)
elif args.action == DECRYPT:
    for line in sys.stdin:
        print(decrypt(line, args.key), file=sys.stdout)
