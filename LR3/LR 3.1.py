ukr_letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

key = 10
encrypted_text = "щшцрхфр чсфшхр чм щшїрччс пицшїґаїиярює."

# Зсув назад (ліворуч) для розшифрування
decrypted_letters = ukr_letters[-key:] + ukr_letters[:-key]

# Створення таблиці підстановки
translation_table = str.maketrans(ukr_letters, decrypted_letters)

# Розшифрування
decrypted_text = encrypted_text.translate(translation_table)

print(f"Розшифровано: {decrypted_text}")
