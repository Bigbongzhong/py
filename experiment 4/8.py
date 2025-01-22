input_string = input("Enter a string: ")
output_string = ""
for char in input_string:
    if 'a' <= char <= 'z':
        output_string += chr(ord(char) - 32)  # convert to uppercase
    else:
        output_string += char
print("Converted string:", output_string)
