# Print the binary representation of a Number in Python

number = 13

# ✅ format number as binary (in base 2)
string = f'{number:b}'
print(string)  # 👉️ 1101

# ✅ Convert an integer to a binary string prefixed with 0b
string = bin(number)
print(string)  # 👉️ 0b1101

# ✅ convert an integer to a lowercase hexadecimal string prefixed with 0x
string = hex(number)
print(string)  # 👉️ 0xd