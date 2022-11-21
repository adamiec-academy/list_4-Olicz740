def my_split(text):
    result = []
    word = ""
    for i in text:
        if i == " " and len(word) >= 1:
            result.append(word)
            word = ""
        elif i != " ":
            word += i
    if word:
        result.append(word)

    return result
print(my_split("   ala ma duzego"))
