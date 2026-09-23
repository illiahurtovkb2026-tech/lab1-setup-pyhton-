'''# Завдання номер 1
print("\n Перевірка безпечного файлу (Легітимне ПЗ)")

# 1.1 Ініціалізація вхідних булевих ознак
is_exe = True
is_temp_dir = False
is_signed = True
high_entropy = False
network_connection = True
modifies_registry = False
creates_hidden_file = False
disables_security = False
injects_code = False
known_bad_hash = False
mass_file_renaming = False
uses_powershell = False
detects_debugger = False
shadow_copy_deletion = False
reads_passwords = False
double_extension = False
autorun_usb = False
camera_mic_access = False
clears_event_logs = False

# 1.2 Формування логічних умов
rule_3 = (autorun_usb and creates_hidden_file) and (is_temp_dir or modifies_registry)
rule_10 = shadow_copy_deletion and high_entropy and network_connection
rule_16 = ((disables_security and injects_code) or (high_entropy and is_temp_dir and modifies_registry))
rule_21 = uses_powershell and disables_security and (creates_hidden_file or clears_event_logs)
rule_26 = is_exe and (camera_mic_access or reads_passwords) and (not is_signed)

# 1.3 Підсумкова логічна умова детекції
is_virus = rule_3 or rule_10 or rule_16 or rule_21 or rule_26

# 1.4 Вивід результатів аналізу
print("Правило 3  (USB-атака):", rule_3)
print("Правило 10 (Скритовий шифрувальник):", rule_10)
print("Правило 16 (Асиметрична комбінація):", rule_16)
print("Правило 21 (Скриптовий вірус):", rule_21)
print("Правило 26 (Непідписаний шпигун):", rule_26)
print("--> Виявлено шкідливе ПЗ:", is_virus)

# Завдання номер 2
# 2.1 Ваші дані
year = "2008"
month = "10"
day = "31"

# Формуємо число РРРРММДД
num = int(year + month + day)
print("2.1. Десяткове число:", num)

# 2.2 Переведення у двійкову та шістнадцяткову форми
# Префікс [2:] прибирає технічні символи '0b' та '0x'
dviyk = bin(num)[2:]
shist = hex(num)[2:]

print("2.2. Двійкова форма:", dviyk)
print("     Шістнадцяткова форма:", shist)

# 2.3 Рахуємо біти та байти
bits = len(dviyk)  # довжина двійкового рядка — це і є кількість бітів
beyts = (bits + 7) // 8  # просте ділення на 8 з округленням угору

print("2.3. Кількість бітів:", bits)
print("     Кількість байтів:", beyts)


# Завдання Номер 3
# 3.1. Генерація ключів
# Беремо достатньо великі p і q, щоб модуль n був великим (40+ цифр)
p = 100000000000000000039
q = 100000000000000000129

n = p * q
pu = (p - 1) * (q - 1)

e = 65537
d = pow(e, -1, pu)  # Секретна експонента: d = e^-1 mod pu

print("3.1. КЛЮЧІ ЗГЕНЕРОВАНО")
print(f"n = {n}\ne = {e}\nd = {d}\n")

# 3.2. Аналіз параметрів ключа (n, e, d)

def analyze(name, val):
    hex_val = hex(val)[2:].upper()
    dec_digits = len(str(val))
    bin_bits = val.bit_length()
    hex_digits = len(hex_val)

    print(f"Параметр: {name}")
    print(f"а) Hex-формат: {hex_val}")
    print(f"б) Кількість цифр у десятковій: {dec_digits}")
    print(f"   Розрядність у двійковій (біти): {bin_bits}")
    print(f"   Кількість цифр у шістнадцятковій: {hex_digits}\n")

print("3.2. АНАЛІЗ ПАРАМЕТРІВ")
analyze("n (модуль)", n)
analyze("e (відкрита експонента)", e)
analyze("d (секретна експонента)", d)

# 3.3. Шифрування

print("3.3. ШИФРУВАННЯ")
surname = "Гуртов"

# 1. Перетворюємо текст у байти, а байти у число m
surname_bytes = surname.encode('utf-8')
m = int.from_bytes(surname_bytes, byteorder='big')

print(f"Прізвище: {surname}")
print(f"Числове значення m: {m}")

# 2. Шифрування за формулою: c = (m ^ e) mod n
c = pow(m, e, n)
print(f"Зашифроване число c: {c}\n")

# 3.4. Розшифрування

print("3.4. РОЗШИФРУВАННЯ")
# 1. Розшифрування за формулою: m' = (c ^ d) mod n
m_decrypted = pow(c, d, n)
print(f"Розшифроване число m': {m_decrypted}")

# 2. Перетворюємо число назад у байти та текст
bytes_len = (m_decrypted.bit_length() + 7) // 8
decrypted_bytes = m_decrypted.to_bytes(bytes_len, byteorder='big')
decrypted_surname = decrypted_bytes.decode('utf-8')

print(f"Відновлений текст: {decrypted_surname}")
from pydoc import plaintext

# Завдання Номер 4  (Шифрування та розшифрування даних операцією XOR)
# 4.1 Підготовка даних
M = "Hurtov"
print("M = " + M)

# 4.2 Генерація ключа
# Перетворюємо в послідовність байт
seq_bytes = M.encode('utf-8')
print('seq_bytes =', seq_bytes.hex(' '))

# Визначаємо к-ть байт
seq_size = len(seq_bytes)
print("Довжина повідомлення в байтах =", seq_size)

# Перетворюємо байти в число
m = int.from_bytes(seq_bytes, byteorder='big')
print("message = ", hex(m))

from secrets import token_bytes

# Генеруємо випадкові байти
k = token_bytes(nbytes=seq_size)
# Перетворюємо байт в число
k = int.from_bytes(k, byteorder='big')

# 4.3 Шифруємо
c = m ^ k
print("chipertext = ", hex(c))

# 4.4 Розшифровуєм
p = c ^ k
print("p = ", hex(p))

# 4.5 Перевірка
# Перетворюємо число в байти
p = p.to_bytes(seq_size, byteorder='big')
# Перетворюємо в символи
plaintext = p.decode('utf-8')
print("plaintext = ", plaintext)'''
