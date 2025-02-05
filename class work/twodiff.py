listPalindrome = []
listArmstrong = []
setPalindrome = set()
setArmstrong = set()

for i in range(0, 1000):
    # Palindrome check
    str_i = str(i)
    if str_i == str_i[::-1]:
        listPalindrome.append(i)
        setPalindrome.add(i)
    
    # Armstrong number check
    num_str = str(i)
    num_digits = len(num_str)
    armstrongSum = sum(int(digit) ** num_digits for digit in num_str)
    
    if armstrongSum == i:
        listArmstrong.append(i)
        setArmstrong.add(i)

toupPalindrome = tuple(listPalindrome)
toupArmstrong = tuple(listArmstrong)

print("Palindrome numbers in List:", listPalindrome)
print("Armstrong numbers in List:", listArmstrong)
print("Palindrome numbers in Set:", setPalindrome) 
print("Armstrong numbers in Set:", setArmstrong)  
print("Palindrome numbers in Tuple:", toupPalindrome)
print("Armstrong numbers in Tuple:", toupArmstrong)
