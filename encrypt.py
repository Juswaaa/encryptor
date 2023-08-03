# Enter the message to be encrypted:
decrypted = input("What is the message you want to decrypt? ")
encrypted = ""

for i in range(len(decrypted)):
# Change "a" to "*"
    if decrypted[i] == "a":
        encrypted += "*"
# Change "e" to "&"
    elif decrypted[i] == "e":
        encrypted += "&"
# Change "i" to "#"
    elif decrypted[i] == "i":
        encrypted += "#"
# Change "o" to "+"
    elif decrypted[i] == "o":
        encrypted += "+"
# Change "u" to "!"
    elif decrypted[i] == "u":
        encrypted += "!"
    else:
        encrypted += decrypted[i]
# print encrypted text
print(encrypted)