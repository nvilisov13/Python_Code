import sys


def path_python():
    print(sys.executable)


def multiply():
    for x in range(1, 11):
        for y in range(1, 11):
            print(x*y, end='\t||\t')
        print()


if __name__ == '__main__':
    multiply()
    path_python()
