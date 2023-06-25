def palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input('Введите слово:  ')
print(palindrom(word))

