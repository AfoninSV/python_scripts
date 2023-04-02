def multi_close(*args):
    for file in args:
        file.close()

def write_scores(filename, data):
    filename.write(data)


def next_tour(filename):
    pass_level = int(filename.readline())
    players_data = filename.readlines()
    return_string = str()

    temp_split = [[f'{word[0]}.'
                   if i_word == 1 else word
                   for i_word, word in enumerate(line.split())]
                  for line in players_data
                  if int(line[-3:]) > pass_level]
    temp_split.sort(reverse=True, key=lambda x: x[2])

    return_string += f'{len(temp_split)}\n'
    for item in temp_split:
        item[0], item[1] = item[1], item[0]
        return_string += ' '.join(item) + '\n'

    return return_string


players_file = open('first_tour.txt', 'r')
next_stage_file = open('second_tour.txt', 'w')
new_scores = next_tour(players_file)
write_scores(next_stage_file, new_scores)
multi_close(players_file, next_stage_file)
