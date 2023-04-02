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

start = int(input("Введите первый год: "))
finish = int(input("Введите второй год: "))
print(f"\nГоды от {start} до {finish} с тремя одинаковыми цифрами:")
num_counter(start, finish)