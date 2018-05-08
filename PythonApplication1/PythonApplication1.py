from math import sin, cos, radians
import sys

def dot_pattern(x):
    return ' ' * int(cos(radians(x))*10) + 'o';

def main():
    print("Hello World")
    for i in range(3000):
        print(dot_pattern(i))


    input()

if __name__ == "__main__":
    sys.exit(int(main() or 0))