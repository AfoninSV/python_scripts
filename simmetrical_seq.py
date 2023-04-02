def make_list(count):
    seq = []
    for _ in range(count):
        seq.append(int(input("Число: ")))
    return seq


def symmetry_check(seq):
    absence = []
    flag = False
    # cut last same numbers
    counter = 0
    while True:
        if seq[-1] == seq[counter - 1]:
            counter -= 1
        else:
            break

    # check for symmetry through both list sides
    for right_num in range(len(seq) - 1, -1 + abs(counter), -1):
        left_num = len(seq) - 1 - right_num
        if flag:
            absence.insert(0, seq[left_num])
        elif seq[left_num] != seq[right_num]:
            flag = True
            absence.insert(0, seq[left_num])

    return absence


seq_count = int(input("Кол-во чисел: "))
sequence = make_list(seq_count)
absenced_nums = symmetry_check(sequence)

print(f"\nПоследовательность: {sequence}")
print(f"Нужно приписать чисел: {len(absenced_nums)}")
print(f"Сами числа: {absenced_nums}")
