
import sys


print(sys.argv)

if len(sys.argv) <= 1:
    raise Exception("No arguments provided. Input args needs to be provided")

name = sys.argv[1]
id = int(sys.argv[2])
dist = float(sys.argv[3])

print(name)
print(id)
print(dist)

# Usage is "python cmd_args.py abcd 1234 111.1"
