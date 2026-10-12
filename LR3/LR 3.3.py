import secrets

# Вхідні набори символів зі скриншоту
low_char = "abcdefghijklmnopqrstuvwxyz"
spc_char = "!@#$%^&*_-"

# Введення даних користувачем
n_low = int(input("Введіть кількість малих латинських літер в паролі: "))
n_spc = int(input("Введіть кількість спеціальних символів !@#$_-%^* в паролі: "))

# Генерація вибірок за допомогою secrets.SystemRandom()
part_low = secrets.SystemRandom().sample(low_char, n_low)
part_spc = secrets.SystemRandom().sample(spc_char, n_spc)

# Об'єднання та перемішування всіх символів у випадковому порядку
all_chars = part_low + part_spc
secrets.SystemRandom().shuffle(all_chars)

# Формування підсумкового паролю
password = "".join(all_chars)

print(f"Password: {password}")