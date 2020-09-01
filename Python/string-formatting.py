def print_formatted(number):
    bin_length = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(f'{i: >{bin_length}}', end='')
        print(f'{oct(i)[2:]: >{bin_length + 1}}', end='')
        print(f'{hex(i)[2:]: >{bin_length + 1}}'.upper(), end='')
        print(f'{bin(i)[2:]: >{bin_length + 1}}', end='\n')

print_formatted(2)
print_formatted(17)
