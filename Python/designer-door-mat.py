N, M = map(int, input().split())

dick = '.|.'

for i in range(1, N, 2):
    dicks = dick * i
    print(dicks.center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N - 2, -1, -2):
    dicks = dick * i
    print(dicks.center(M, '-'))
