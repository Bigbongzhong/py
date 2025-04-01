import re

def is_palindrome(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # Remove non-alphanumeric characters
    return cleaned_s == cleaned_s[::-1]  # Compare with reversed string

# Example usage
s = input("Enter a string: ")
print(is_palindrome(s))
