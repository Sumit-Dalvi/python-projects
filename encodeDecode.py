message = input("Enter a message to Encode or Decode: ")
message = message.upper()
output = " "
for letter in message:
    if letter.isupper():
        value = ord(letter) + 13
        letter = chr(value)
        if not letter.isupper():
                value -=26
                letter = chr(value)
    output  += letter
print("output message: ", output)
