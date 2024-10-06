#Key Generator
import random

def generate_key():
    key = ""
    for i in range(64):
        bit = random.choice([0, 1])
        key += str(bit)
    return key
  
#