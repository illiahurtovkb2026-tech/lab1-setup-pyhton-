# Завдання номер 1
print("Перевірка безпечного файлу (Легітимне ПЗ)")

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
print("Виявлено шкідливе ПЗ:", is_virus)

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

# 3.3 Шифрування

print("3.3 Шифрування")
surname = "Гуртов"

# 1. Перетворюємо текст у байти, а байти у число m
surname_bytes = surname.encode("utf-8")
m = int.from_bytes(surname_bytes, byteorder="big")

print(f"Прізвище: {surname}")
print(f"Числове значення m: {m}")

# 2. Шифрування за формулою: c = (m ^ e) mod n
c = pow(m, e, n)
print(f"Зашифроване число c: {c}\n")

# 3.4. Розшифрування

print("3.4 Розшифрування")
# 1. Розшифрування за формулою: m' = (c ^ d) mod n
m_decrypted = pow(c, d, n)
print(f"Розшифроване число m': {m_decrypted}")

# 2. Перетворюємо число назад у байти та текст
bytes_len = (m_decrypted.bit_length() + 7) // 8
decrypted_bytes = m_decrypted.to_bytes(bytes_len, byteorder='big')
decrypted_surname = decrypted_bytes.decode("utf-8")

print(f"Відновлений текст: {decrypted_surname}")
from pydoc import plaintext

# Завдання Номер 4 (Шифрування та розшифрування даних операцією XOR)
# 4.1 Підготовка даних
M = "Гуртов"
print("M = " + M)

# 4.2 Генерація ключа
# Перетворюємо в послідовність байт
seq_bytes = M.encode("utf-8")
print("seq_bytes =", seq_bytes.hex(" "))

# Визначаємо к-ть байт
seq_size = len(seq_bytes)
print("Довжина повідомлення в байтах =", seq_size)

# Перетворюємо байти в число
m = int.from_bytes(seq_bytes, byteorder="big")
print("message = ", hex(m))

from secrets import token_bytes

# Генеруємо випадкові байти
k = token_bytes(nbytes=seq_size)
# Перетворюємо байт в число
k = int.from_bytes(k, byteorder="big")

# 4.3 Шифруємо
c = m ^ k
print("chipertext = ", hex(c))

# 4.4 Розшифровуєм
p = c ^ k
print("p = ", hex(p))

# 4.5 Перевірка
# Перетворюємо число в байти
p = p.to_bytes(seq_size, byteorder="big")
# Перетворюємо в символи
plaintext = p.decode("utf-8")
print("plaintext = ", plaintext)

# Завдання Номер 5
import math

num_variant = input("Введіть ваш варіант: ")
student = input("Введіть ваше прізвище та ім'я: ")

# Введення та обчислення аргументів
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))

vyraz1 = math.sqrt(math.sin(x ** 2) + 16 * y * x)
vyraz2 = 16 * y * x
vyraz3 = math.exp(x + y)
vyraz4 = 1 / math.cos(y) + x
full_vyraz= vyraz1 + vyraz2 - vyraz3 - vyraz4

# Вивід інформації
print("             Звіт")
print(f"Номер варіанту: {num_variant}")
print(f"Прізвище та ім'я студента: {student}")
print(f"Введені значення аргументів: x = {x}, y = {y}")
print(f"Отриманий результат обчислення: {full_vyraz:.4f}")

# Завдання Номер 6

from rich.console import Console
from rich.table import Table


# 1. Вхідні дані для 10 варіанту

GPU_COUNT = 1

SEC_IN_HOUR = 3600
HOURS_IN_YEAR = 8760
SEC_IN_YEAR = SEC_IN_HOUR * HOURS_IN_YEAR

# Базові швидкості перебору хешів для 1 GPU (10 варіант)
md5_speed_1gpu = 40e9
sha1_speed_1gpu = 12.5e9
sha256_speed_1gpu = 4.0e9
pbkdf2_speed_1gpu = 4.2e6
bcrypt_speed_1gpu = 29000
argon2_speed_1gpu = 420

# Швидкості кластера
md5_cluster_speed = md5_speed_1gpu * GPU_COUNT
sha1_cluster_speed = sha1_speed_1gpu * GPU_COUNT
sha256_cluster_speed = sha256_speed_1gpu * GPU_COUNT
pbkdf2_cluster_speed = pbkdf2_speed_1gpu * GPU_COUNT
bcrypt_cluster_speed = bcrypt_speed_1gpu * GPU_COUNT
argon2_cluster_speed = argon2_speed_1gpu * GPU_COUNT

# Значення ентропії в бітах (10 варіант)
entropy_weak_pass = 60
entropy_medium_pass = 73
entropy_strong_pass = 95

comb_weak = 2 ** entropy_weak_pass
comb_medium = 2 ** entropy_medium_pass
comb_strong = 2 ** entropy_strong_pass


# 2. Розрахунок часу підбору


# Час у годинах
hours_md5_weak = comb_weak / (md5_cluster_speed * SEC_IN_HOUR)
hours_sha1_weak = comb_weak / (sha1_cluster_speed * SEC_IN_HOUR)
hours_sha256_weak = comb_weak / (sha256_cluster_speed * SEC_IN_HOUR)
hours_pbkdf2_weak = comb_weak / (pbkdf2_cluster_speed * SEC_IN_HOUR)
hours_bcrypt_weak = comb_weak / (bcrypt_cluster_speed * SEC_IN_HOUR)
hours_argon2_weak = comb_weak / (argon2_cluster_speed * SEC_IN_HOUR)

hours_md5_medium = comb_medium / (md5_cluster_speed * SEC_IN_HOUR)
hours_sha1_medium = comb_medium / (sha1_cluster_speed * SEC_IN_HOUR)
hours_sha256_medium = comb_medium / (sha256_cluster_speed * SEC_IN_HOUR)
hours_pbkdf2_medium = comb_medium / (pbkdf2_cluster_speed * SEC_IN_HOUR)
hours_bcrypt_medium = comb_medium / (bcrypt_cluster_speed * SEC_IN_HOUR)
hours_argon2_medium = comb_medium / (argon2_cluster_speed * SEC_IN_HOUR)

hours_md5_strong = comb_strong / (md5_cluster_speed * SEC_IN_HOUR)
hours_sha1_strong = comb_strong / (sha1_cluster_speed * SEC_IN_HOUR)
hours_sha256_strong = comb_strong / (sha256_cluster_speed * SEC_IN_HOUR)
hours_pbkdf2_strong = comb_strong / (pbkdf2_cluster_speed * SEC_IN_HOUR)
hours_bcrypt_strong = comb_strong / (bcrypt_cluster_speed * SEC_IN_HOUR)
hours_argon2_strong = comb_strong / (argon2_cluster_speed * SEC_IN_HOUR)

# Час у роках
years_md5_weak = comb_weak / (md5_cluster_speed * SEC_IN_YEAR)
years_sha1_weak = comb_weak / (sha1_cluster_speed * SEC_IN_YEAR)
years_sha256_weak = comb_weak / (sha256_cluster_speed * SEC_IN_YEAR)
years_pbkdf2_weak = comb_weak / (pbkdf2_cluster_speed * SEC_IN_YEAR)
years_bcrypt_weak = comb_weak / (bcrypt_cluster_speed * SEC_IN_YEAR)
years_argon2_weak = comb_weak / (argon2_cluster_speed * SEC_IN_YEAR)

years_md5_medium = comb_medium / (md5_cluster_speed * SEC_IN_YEAR)
years_sha1_medium = comb_medium / (sha1_cluster_speed * SEC_IN_YEAR)
years_sha256_medium = comb_medium / (sha256_cluster_speed * SEC_IN_YEAR)
years_pbkdf2_medium = comb_medium / (pbkdf2_cluster_speed * SEC_IN_YEAR)
years_bcrypt_medium = comb_medium / (bcrypt_cluster_speed * SEC_IN_YEAR)
years_argon2_medium = comb_medium / (argon2_cluster_speed * SEC_IN_YEAR)

years_md5_strong = comb_strong / (md5_cluster_speed * SEC_IN_YEAR)
years_sha1_strong = comb_strong / (sha1_cluster_speed * SEC_IN_YEAR)
years_sha256_strong = comb_strong / (sha256_cluster_speed * SEC_IN_YEAR)
years_pbkdf2_strong = comb_strong / (pbkdf2_cluster_speed * SEC_IN_YEAR)
years_bcrypt_strong = comb_strong / (bcrypt_cluster_speed * SEC_IN_YEAR)
years_argon2_strong = comb_strong / (argon2_cluster_speed * SEC_IN_YEAR)


# 3. Розрахунок витрат на електроенергію


POWER_CONSUMPTION_KW = 0.115
ELECTRICITY_COST_PER_KWH_UAH = 8.50
USD_TO_UAH = 45.0

electricity_cost_per_kwh_usd = ELECTRICITY_COST_PER_KWH_UAH / USD_TO_UAH

def calculate_electricity_cost(hours):
    energy_kwh = hours * POWER_CONSUMPTION_KW * GPU_COUNT
    return energy_kwh * electricity_cost_per_kwh_usd

cost_md5_weak = calculate_electricity_cost(hours_md5_weak)
cost_sha1_weak = calculate_electricity_cost(hours_sha1_weak)
cost_sha256_weak = calculate_electricity_cost(hours_sha256_weak)
cost_pbkdf2_weak = calculate_electricity_cost(hours_pbkdf2_weak)
cost_bcrypt_weak = calculate_electricity_cost(hours_bcrypt_weak)
cost_argon2_weak = calculate_electricity_cost(hours_argon2_weak)

cost_md5_medium = calculate_electricity_cost(hours_md5_medium)
cost_sha1_medium = calculate_electricity_cost(hours_sha1_medium)
cost_sha256_medium = calculate_electricity_cost(hours_sha256_medium)
cost_pbkdf2_medium = calculate_electricity_cost(hours_pbkdf2_medium)
cost_bcrypt_medium = calculate_electricity_cost(hours_bcrypt_medium)
cost_argon2_medium = calculate_electricity_cost(hours_argon2_medium)

cost_md5_strong = calculate_electricity_cost(hours_md5_strong)
cost_sha1_strong = calculate_electricity_cost(hours_sha1_strong)
cost_sha256_strong = calculate_electricity_cost(hours_sha256_strong)
cost_pbkdf2_strong = calculate_electricity_cost(hours_pbkdf2_strong)
cost_bcrypt_strong = calculate_electricity_cost(hours_bcrypt_strong)
cost_argon2_strong = calculate_electricity_cost(hours_argon2_strong)


# 4. Вивід таблиць у консоль


# Широкий консольний вивід, щоб таблиця не стискалася
console = Console(width=200)

# Таблиця 1: Години
table_hours = Table(
    title=f"Час підбору пароля на кластері з {GPU_COUNT:,}x GPU (у годинах)",
    show_header=True,
    header_style="bold cyan",
    expand=False
)

table_hours.add_column("Алгоритм", style="white", justify="left", overflow="fold")
table_hours.add_column("Швидкість кластера, H/год", style="bold yellow", justify="center", overflow="fold")
table_hours.add_column("Слабкий (60 біт), год.", style="bold yellow", justify="center", overflow="fold")
table_hours.add_column("Середній (73 біти), год.", style="bold yellow", justify="center", overflow="fold")
table_hours.add_column("Сильний (95 біт), год.", style="bold yellow", justify="center", overflow="fold")

table_hours.add_row("MD5",
                    f"{int(md5_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_md5_weak):,}",
                    f"{int(hours_md5_medium):,}",
                    f"{int(hours_md5_strong):,}")

table_hours.add_row("SHA-1",
                    f"{int(sha1_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_sha1_weak):,}",
                    f"{int(hours_sha1_medium):,}",
                    f"{int(hours_sha1_strong):,}")
table_hours.add_row("SHA-256",
                    f"{int(sha256_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_sha256_weak):,}",
                    f"{int(hours_sha256_medium):,}",
                    f"{int(hours_sha256_strong):,}")
table_hours.add_row("PBKDF2-WPA2",
                    f"{int(pbkdf2_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_pbkdf2_weak):,}",
                    f"{int(hours_pbkdf2_medium):,}",
                    f"{int(hours_pbkdf2_strong):,}")
table_hours.add_row("bcrypt",
                    f"{int(bcrypt_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_bcrypt_weak):,}",
                    f"{int(hours_bcrypt_medium):,}",
                    f"{int(hours_bcrypt_strong):,}")
table_hours.add_row("Argon2",
                    f"{int(argon2_cluster_speed * SEC_IN_HOUR):,}",
                    f"{int(hours_argon2_weak):,}",
                    f"{int(hours_argon2_medium):,}",
                    f"{int(hours_argon2_strong):,}")

console.print(table_hours)
console.print()

# Таблиця 2: Роки
table_years = Table(
    title=f"Час підбору пароля на кластері з {GPU_COUNT:,}x GPU (у роках)",
    show_header=True,
    header_style="bold cyan",
    expand=False
)

table_years.add_column("Алгоритм", style="white", justify="left", overflow="fold")
table_years.add_column("Швидкість кластера, H/рік", style="bold yellow", justify="center", overflow="fold")
table_years.add_column("Слабкий (60 біт), років", style="bold yellow", justify="center", overflow="fold")
table_years.add_column("Середній (73 біти), років", style="bold yellow", justify="center", overflow="fold")
table_years.add_column("Сильний (95 біт), років", style="bold yellow", justify="center", overflow="fold")

table_years.add_row("MD5",
                    f"{int(md5_cluster_speed * SEC_IN_YEAR):,}",
                    f"{years_md5_weak:,.4f}",
                    f"{int(years_md5_medium):,}",
                    f"{int(years_md5_strong):,}")
table_years.add_row("SHA-1",
                    f"{int(sha1_cluster_speed * SEC_IN_YEAR):,}",
                    f"{years_sha1_weak:,.4f}",
                    f"{int(years_sha1_medium):,}",
                    f"{int(years_sha1_strong):,}")
table_years.add_row("SHA-256",
                    f"{int(sha256_cluster_speed * SEC_IN_YEAR):,}",
                    f"{years_sha256_weak:,.4f}",
                    f"{int(years_sha256_medium):,}",
                    f"{int(years_sha256_strong):,}")
table_years.add_row("PBKDF2-WPA2",
                    f"{int(pbkdf2_cluster_speed * SEC_IN_YEAR):,}",
                    f"{int(years_pbkdf2_weak):,}",
                    f"{int(years_pbkdf2_medium):,}",
                    f"{int(years_pbkdf2_strong):,}")
table_years.add_row("bcrypt",
                    f"{int(bcrypt_cluster_speed * SEC_IN_YEAR):,}",
                    f"{int(years_bcrypt_weak):,}",
                    f"{int(years_bcrypt_medium):,}",
                    f"{int(years_bcrypt_strong):,}")
table_years.add_row("Argon2",
                    f"{int(argon2_cluster_speed * SEC_IN_YEAR):,}",
                    f"{int(years_argon2_weak):,}",
                    f"{int(years_argon2_medium):,}",
                    f"{int(years_argon2_strong):,}")

console.print(table_years)
console.print()

# Таблиця 3: Вартість електрики
table_cost = Table(
    title=f"Вартість електрики для підбору пароля на кластері з {GPU_COUNT:,}x GPU (у USD)",
    show_header=True,
    header_style="bold cyan",
    expand=False
)

table_cost.add_column("Алгоритм", style="white", justify="left", overflow="fold")
table_cost.add_column("Слабкий (60 біт), USD", style="bold yellow", justify="center", overflow="fold")
table_cost.add_column("Середній (73 біти), USD", style="bold yellow", justify="center", overflow="fold")
table_cost.add_column("Сильний (95 біт), USD", style="bold yellow", justify="center", overflow="fold")

table_cost.add_row("MD5",
                   f"{int(cost_md5_weak):,}",
                   f"{int(cost_md5_medium):,}",
                   f"{int(cost_md5_strong):,}")
table_cost.add_row("SHA-1",
                   f"{int(cost_sha1_weak):,}",
                   f"{int(cost_sha1_medium):,}",
                   f"{int(cost_sha1_strong):,}")
table_cost.add_row("SHA-256",
                   f"{int(cost_sha256_weak):,}",
                   f"{int(cost_sha256_medium):,}",
                   f"{int(cost_sha256_strong):,}")
table_cost.add_row("PBKDF2-WPA2",
                   f"{int(cost_pbkdf2_weak):,}",
                   f"{int(cost_pbkdf2_medium):,}",
                   f"{int(cost_pbkdf2_strong):,}")
table_cost.add_row("bcrypt",
                   f"{int(cost_bcrypt_weak):,}",
                   f"{int(cost_bcrypt_medium):,}",
                   f"{int(cost_bcrypt_strong):,}")
table_cost.add_row("Argon2",
                   f"{int(cost_argon2_weak):,}",
                   f"{int(cost_argon2_medium):,}",
                   f"{int(cost_argon2_strong):,}")

console.print(table_cost)