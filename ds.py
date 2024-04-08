import re
import random
import string

def capital():
    first = random.choice(string.ascii_uppercase)
    symbol = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    last = random.choice(string.digits)
    final = first + symbol + last
    return final

sample = capital()
print(sample)
