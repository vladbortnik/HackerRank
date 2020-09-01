if __name__ == '__main__':
    s = input()

    result = False
    for letter in s:
        if letter.isalnum():
            result = True
            break
    print(result)

    result = False
    for letter in s:
        if letter.isalpha():
            result = True
            break
    print(result)

    result = False
    for letter in s:
        if letter.isdigit():
            result = True
            break
    print(result)

    result = False
    for letter in s:
        if letter.islower():
            result = True
            break
    print(result)

    result = False
    for letter in s:
        if letter.isupper():
            result = True
            break
    print(result)
