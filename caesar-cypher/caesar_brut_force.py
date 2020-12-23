from subprocess import run, PIPE
import sys

input = []
for line in sys.stdin:
    input.append(line)

input = "".join(input)

for key in range(1, 32):
    print(f"Trying to decrypt with key={key}")
    print(f"----------------------------------")
    run(["python3", "caesar.py", "--action", "decrypt", "--key", str(key)], check=True, input=input.encode("UTF-8"))
    print("")
