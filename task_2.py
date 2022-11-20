def my_split(text):
    result = []
    word = ""
    for i in text:
        if i == " ":
            result.append(word)
            word = ""
        else:
            word += i
    if word:
        result.append(word)

    return result
