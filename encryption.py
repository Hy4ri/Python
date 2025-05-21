import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)

# enc
passwd = input("pass plz: ")
enc = ""

for letter in passwd:
    index = chars.index(letter)
    enc += key[index]

print(passwd)
print(enc)
# dec
enc = input("enc plz: ")
passwd = ""

for letter in enc:
    index = key.index(letter)
    passwd += chars[index]

print(enc)
print(passwd)
