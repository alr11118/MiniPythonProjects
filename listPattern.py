import time
import string

alphabet = list(string.ascii_lowercase)
alphabet_backwards = list(reversed(alphabet))
final = ""
for letter in alphabet:
    final += letter
    print(final)
    time.sleep(0.1)

final = " " * len(final) + "".join(alphabet_backwards)
print(final)
time.sleep(0.1)

for i in range (len(alphabet_backwards),len(final)):
    final = final[:i] + " " + final[i+1:]
    print(final)
    time.sleep(0.1)