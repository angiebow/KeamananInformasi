from des import DES


des = DES(key=193)
number = 123456
ciphertext = des.encryptNumber(number)
decrypted = des.decrypt_number(ciphertext)

print('Message:', number)
print('Encrypted:', ciphertext)
print('Decrypted', decrypted)
