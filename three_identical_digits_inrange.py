"""
A program that finds and displays all four-digit numbers within the given range that contain exactly three identical digits.
"""

def num_counter(start, finish):
    for number in range(start, finish + 1):
        temp_str = ""
        symbol_flag = ""
        #temp_number = 0
        for symbol in str(number):
            if symbol not in temp_str:
                temp_str += symbol
            else:
                symbol_flag += symbol
        if symbol_flag:
            counter = 0
            for symbol in symbol_flag:
                for num in str(number):
                    if symbol == num:
                        counter += 1
                else:
                    if counter == 3:
                        print(number)

start = int(input("Input first year: "))
finish = int(input("Input second year: "))
print(f"\nYears from {start} to {finish} with three identical digits:")
num_counter(start, finish)