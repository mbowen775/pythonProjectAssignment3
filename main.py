# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import random
def CoinToss():
    number = input("Make a selection of '1' or '0': ")
    recordList = []
    heads = 1
    tails = 0
    for amount in range(number):
         flip = random.randint(1, 0)
         if (flip == 1):
              print("Heads")
              recordList.append("Heads")
         if (flip == 0):
              print("Tails")
              recordList.append("Tails")
    print(str(recordList))
    print(str(recordList.count("Heads")) + str(recordList.count("Tails")))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
