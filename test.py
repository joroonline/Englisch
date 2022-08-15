import random

print([f'{x+1}. {y}' for x, y in enumerate([random.randint(1,9) for i in range(10)])])