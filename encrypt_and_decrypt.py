import random
import time

# Encryption

def encrypt(plaintext: str, key: int):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ciphertext = ""
  for i in range(0,len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range (0,key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext

# Decryption

def decrypt(ciphertext: str, key: int):
  plaintext = ""
  count = 0
  for i in ciphertext:
    if count % (key+1) == 0:
      plaintext = plaintext + i
    count += 1
  return plaintext

# Input plaintext for encryption

plaintext = input("Enter a message to encrypt (plaintext) ")

# Input key (1-10)

key = int(input("Input a key as a number between 1 and 10 "))

#Error

while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input a key as a number between 1 and 10"))

# "Loading"

print("Encrypting plaintext...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

# Print output

print("Ciphertext: " + ciphertext)

# Input plaintext for encryption

ciphertext = input("Enter a message to decrypt (ciphertext) ")

# Input key (1-10)

key = int(input("Input your key as a number between 1 and 10 "))

# Error

while not (key>=1 and key<=10):
  print("Invalid key, try again!")
  key = int(input("Input your key as a number between 1 and 10"))

# "Loading"

print("Decrypting ciphertext...")
time.sleep(1)
plaintext = decrypt(ciphertext, key)

# Print output

print("Plaintext: " + plaintext)