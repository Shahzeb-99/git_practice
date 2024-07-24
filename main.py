# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print(sum_square(5))


def sum_square(n):
    print(any([True, False, False]))
    print(list(filter(lambda x: 0 , [1, 2, 3, 4, 5])))
    print(sum(map(lambda x: x * x, range(1,n))))
    return sum(i * i for i in range(1, n))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
