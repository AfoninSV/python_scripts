"""## Задача 10. Истина
### Что нужно сделать
К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python. Напишите программу, которая реализует алгоритм дешифровки этого текста. Расшифруйте текст с помощью своей программы, а затем найдите его в интернете.

`vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip`
### Что оценивается
- Результат вычислений корректен.
- Основной функционал описан в отдельной(-ых) функции(-ях)
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
"""
def caesar(shift, crypted_word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    encrypted_str = ''

    for sym in crypted_word.lower():
        if sym in alphabet:
            i_shifted = alphabet.index(sym) + shift
            if i_shifted > len(alphabet) - 1:
                i_shifted %= len(alphabet)
            encrypted_str += alphabet[i_shifted]
        else:
            encrypted_str += sym

    return encrypted_str


def shift_string(shift, unshifted_str):
    for _ in range(shift):
        unshifted_str = unshifted_str[-1] + unshifted_str[:-1]

    return f'{unshifted_str} '


crypted_str = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm ' \
              'yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef ' \
              'uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju ' \
              'fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj ' \
              'gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
              'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm ' \
              'fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg ' \
              'fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. ' \
              'fu(tm pe psfn gp tf"uip '

listed_msg = crypted_str.split()
caesar_shift = 25
inword_shift = 3
shifted_raw = ''

for i_word in listed_msg:
    encrypted_word = caesar(caesar_shift, i_word)
    letter_shift = shift_string(inword_shift, encrypted_word)
    shifted_raw += letter_shift

    if '/' in letter_shift:
        shifted_raw += '\n'
        inword_shift += 1

print(f'Зашифрованное сообщение: \n{shifted_raw}')

