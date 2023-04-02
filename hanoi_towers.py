def move_print(disk, frm_rod, to_rod):
    print('Переложить диск {} со стержня номер {} на стержень номер {}'
          .format(disk, frm_rod, to_rod))


def hanoi(disk, frm_rod, to_rod):
    if disk == 1:
        move_print(disk, frm_rod, to_rod)
        return None

    tmp = 6 - frm_rod - to_rod
    hanoi(disk - 1, frm_rod, tmp)
    move_print(disk, frm_rod, to_rod)
    hanoi(disk - 1, tmp, to_rod)


disk_count = int(input('Введите количество дисков: '))
hanoi(disk_count, 1, 3)
