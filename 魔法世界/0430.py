import random

num = random.choice([1, 2])

for _ in range(20):
    num = random.choice([1, 2, 5, 45, 67])
    print(num)
