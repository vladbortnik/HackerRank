from itertools import chain


def print_one_line(letters, n):
    # generate the line of letters separated by hythen
    if len(letters) == 1:
        line = letters[0]
    else:
        left = ('-').join(letters[len(letters) - 1: 0: -1])
        right = ('-').join(letters[0: len(letters)])
        line = ('-').join([left, right])

    # center if needed
    if len(letters) == n:
        print(line)
    else:
        print(line.center(2 * (2 * n - 1) -1, '-'))


def print_rangoli(size):
    letters = [chr(97 + i) for i in range(n)]

    for i in chain(range(1, n), range(n, 0, -1)):
        print_one_line(letters[n - i::], n)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
