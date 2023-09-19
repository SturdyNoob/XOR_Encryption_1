print(ord("A"))
print(chr(65))
print(hex(65))

import base64

plaintext = "A"
password = "B"

ascii_decimal = ord(plaintext) ^ ord(password)

ascii_human = chr(ascii_decimal)

ascii_hex = hex(ascii_decimal)

base64_encoded = base64.b64encode(ascii_human.encode('utf-8')).decode('utf-8')

print(ascii_decimal)
print(ascii_human)
print(ascii_hex)
print(base64_encoded)