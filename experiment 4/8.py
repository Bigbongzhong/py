input_string = input("Enter a string: ")
output_string = ""

for char in input_string:
    if char >= 'a' and char <= 'z': 
        output_string += char.upper() 
    else:
        output_string += char

print("Converted string:", output_string)
