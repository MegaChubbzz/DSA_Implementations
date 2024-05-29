'''Double hashing formula (h1(key) + i * h2(key)) % N'''

i = 0
key = int(input("Input key: "))
h1 = int(input("Input h1: "))
h2 = int(input("Input h2: "))
N = int(input("Input table size: "))

while i >= 0:
    bucket = (key % h1 + i * (h2 - key % h2)) % N
    print(bucket)
    i = int(input("Input i: "))
