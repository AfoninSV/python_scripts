def vowels_count(text):
    alphabet = ['a', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
    vowels = [sym for sym in text if sym.lower() in alphabet]
    return vowels


text = input("Введите текст: ")
text_vows = vowels_count(text)

print(f"\nСписок гласных букв: {text_vows}")
print(f"Длина списка: {len(text_vows)}")
