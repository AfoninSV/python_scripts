"""
Reverse sequence between first and last appearance of character 'h' in a given string.
"""

text = input("Введите строку: ")
h_index = [i_sym for i_sym in range(len(text)) if text[i_sym] == 'h' ]
h_text = [text[h_index[-1] - 1 : h_index[0] : -1]]

print(h_text)