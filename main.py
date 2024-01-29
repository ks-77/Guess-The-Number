"""
HW9 (add)
Savchenko Kirill
"""
from colorama import init
init(autoreset=True)
# GUESS THE NUMBER


def guess_num(arr) -> int:
    first_index = 0
    last_index = len(arr) - 1
    attempts = 0
    while first_index < last_index:
        mid_index = (first_index + last_index) // 2
        attempts += 1
        choice = input(f"\nYour number is {str(arr[mid_index])}?\nWrite '+' for yes, '-' for no: ")
        if choice == "+":
            print(f"Wow, i guessed it from the {attempts} attempt!")
            return -1
        elif choice == "-":
            area = input(f"\nWrite '+' if bigger, or '-' if smaller than {str(arr[mid_index])}: ")
            if area == '+':
                first_index = mid_index
            elif area == '-':
                last_index = mid_index
            else:
                attempts -= 1
                print('\033[1;31m'"\nENTER ONLY '+' OR '-'!\n")
        else:
            attempts -= 1
            print('\033[1;31m'"\nENTER ONLY '+' OR '-'!\n")
    print('\033[1m'"\nI guess you gave the wrong answer to some of my questions\nTry to reload the program")
    return -1


nums = list(range(101))
guess_num(nums)
