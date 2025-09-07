import random
import string
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"Chars: {chars}")
#print(f"Key: {key}")

#ENCRYPT
plain_text = input("Enter a messege to encrypt: ")
chiper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    chiper_text += key[index]

print(f"Original messege: {plain_text}")
print(f"Encrypted messege: {chiper_text}")

#DECRYPT
chiper_text = input("Enter a messege to encrypt: ")
plain_text = ""

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted messege: {chiper_text}")
print(f"Original messege: {plain_text}")