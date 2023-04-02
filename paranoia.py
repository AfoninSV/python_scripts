import os

def caesar(crp_line, shift):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    encrypted_str = ''
    shift = shift + shift

    for sym in crp_line:
        if sym in alphabet:
            i_shifted = alphabet.index(sym) + shift
            if i_shifted > len(alphabet) - 1:
                i_shifted %= len(alphabet)
            encrypted_str += alphabet[i_shifted]
        else:
            encrypted_str += sym

    return encrypted_str


decr_file = open('text.txt', 'r')   # decrypted filename here
encr_file = open('cipher_text.txt', 'a')    # crypted file name
shift = 1

for line in decr_file.readlines():
    new_line = caesar(line, shift)
    encr_file.write(new_line)
    shift += 1

decr_file.close()
encr_file.close()