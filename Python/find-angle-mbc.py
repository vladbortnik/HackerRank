from math import atan2
from math import degrees

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    print(str(round(degrees(atan2(ab, bc)))) + '°'
