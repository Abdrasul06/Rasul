import re 
import string
import random
def capital():
    y = re.findall("[A-Z].{6}[a-z][0-9]")
    print(y)


