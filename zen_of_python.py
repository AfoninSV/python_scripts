zen_file = open('zen.txt', 'r')
data = zen_file.read().split('\n')
zen_file.close()

for i_line in range(len(data) - 1, 0, -1):
    print(data[i_line])