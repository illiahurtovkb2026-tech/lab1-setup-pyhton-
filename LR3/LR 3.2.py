import colorama
from colorama import Fore

# Ініціалізація colorama
colorama.init(autoreset=True)

# Визначення наборів символів
low_char = "abcdefghijklmnopqrstuvwxyz"
spc_char = "!@#$%^&*_- "

# Висновок вимог до пароля
print("Введіть пароль довжиною не менше 9 символів.")
print("Вимоги до паролю:")
print("1. Маленькі літери латинські")
print("2. Спеціальні символи !@#$%^&*_-")

password = input(">>> ")

# 1. Перевірка довжини
is_len_ok = len(password) >= 9

# 2. Перевірка наявності маленьких літер
# Замінюємо всі маленькі літери порожнім рядком, використовуючи maketrans і translate
table_low = str.maketrans("", "", low_char)
has_low = len(password) > len(password.translate(table_low))

# 3. Перевірка наявності спеціальних символів
table_spc = str.maketrans("", "", spc_char)
has_spc = len(password) > len(password.translate(table_spc))

print()

# Виведення результатів перевірки
if is_len_ok:
    print(Fore.GREEN + "Довжина не менше 9 символів - OK!")
else:
    print(Fore.RED + "Довжина не менше 9 символів - FAIL!")

if has_low:
    print(Fore.GREEN + "Маленькі літери - OK!")
else:
    print(Fore.RED + "Маленькі літери - FAIL!")

if has_spc:
    print(Fore.GREEN + "Спеціальні символи - OK!")
else:
    print(Fore.RED + "Спеціальні символи - FAIL!")

print()

# Підсумковий вердикт
if is_len_ok and has_low and has_spc:
    print(Fore.GREEN + "Пароль валідний!")
else:
    print(Fore.RED + "Пароль не валідний!")