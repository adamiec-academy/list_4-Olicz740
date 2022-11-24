def is_palindrome(text):
    text = text.lower()
    text = list(text)
    lista =[]
    for i in text:
        lista.insert(0, i)
    for i in range(len(text)):
        if lista[i] == text[i]:
            return True
    return False
