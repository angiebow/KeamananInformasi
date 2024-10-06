#Key Generator
import random

def generate_key():
    key = ""
    for i in range(64):
        bit = random.choice([0, 1])
        key += str(bit)
    return key
  
#Encryption
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_inv = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

def permute(block, table):
    return "".join([block[i-1] for i in table])

def xor(a, b):
    return "".join(['1' if i != j else '0' for i, j in zip(a, b)])

def f(R, K):
    R_expanded = permute(R, E)
    temp = xor(R_expanded, K)
    return temp[:32]

def encrypt(plain_text, keys):
    permuted_text = permute(plain_text, IP)
    L, R = permuted_text[:32], permuted_text[32:]

    for i in range(16):
        temp = R
        R = xor(L, f(R, keys[i]))
        L = temp

    combined = R + L

    cipher_text = permute(combined, IP_inv)
    return cipher_text