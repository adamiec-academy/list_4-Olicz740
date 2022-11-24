def is_palindrome(text):
    text = text.lower()
    text = text.split()
    list =[]
    for i in text:
        list.insert(0, i)
    for i in range(len(text)):
        if list[i] != text[i]:
            return False
    return True
