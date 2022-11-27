def is_palindrome(text):
    text = text.lower()
    text = text.split()
    text = "".join(text)
    lista = text[::-1]
    for i in range(len(text) // 2):
        if lista == text:
            return True
    return False
