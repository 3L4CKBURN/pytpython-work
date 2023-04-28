def is_palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

s = "A man, a plan, a canal, Panama!"
if is_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.") 