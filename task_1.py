def is_palindrome(text):
    text = text.lower()
    x = text.split()
    for i in range(0, int(text[len(text)/2])):
        if text[i] == text[len(text)+1]:
            text[len(text)] = text[len(text)] - 1
            return True
        else:
            return False
print(is_palindrome("ala"))
