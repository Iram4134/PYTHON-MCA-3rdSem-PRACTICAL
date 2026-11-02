string=input("Enter a string: ")
print("The original string is: ", string)

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in string:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of spaces:", spaces)
print("Number of special characters:", special)


