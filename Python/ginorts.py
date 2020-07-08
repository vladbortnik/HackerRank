string = input()


def custom_sorting(letter):
    if letter.islower():
        return ord(letter) - 32
    elif letter.isupper():
        return ord(letter) + 32
    elif letter.isdigit():
        if int(letter) % 2 == 0:
            return ord(letter) + 200
        else:
            return ord(letter) + 100

print(*sorted(string, key=custom_sorting), sep='')
