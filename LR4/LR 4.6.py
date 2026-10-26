import random
import math
import matplotlib.pyplot as plt
from Crypto.Util.number import getPrime

# 1. Генерація простих чисел p і q (по 820 біт) та модуля m
def get_blum_prime():
    while True:
        p = getPrime(820)
        if p % 4 == 3:
            return p

print("Генерація 820-бітних простих чисел Блума.")
p = get_blum_prime()
q = get_blum_prime()
m = p * q

# Підбір seed (s): взаємно просте з m (gcd(seed, m) == 1) та більше за 1
while True:
    seed = random.randint(2, m - 1)
    if math.gcd(seed, m) == 1:
        break

# Вивід згенерованих параметрів
print(f"\nЗГЕНЕРОВАНІ ПАРАМЕТРИ")
print(f"p = {p}")
print(f"q = {q}")
print(f"m = {m}")
print(f"seed = {seed}\n")

# 2. Генерація 20 000 біт алгоритмом Блум-Блум-Шуба
bit_stream = ""
x = (seed ** 2) % m

for _ in range(20_000):
    x = (x ** 2) % m
    bit_stream += str(x & 1)

print(f"Згенеровано біт: {len(bit_stream)}")

#3. ПЕРЕВІРКА ТЕСТАМИ
# Monobit Test (перевірка кількості одиниць)
ones_count = bit_stream.count('1')
monobit_passed = 9725 < ones_count < 10275
print(f"\nMONOBIT TEST")
print(f"Кількість одиниць: {ones_count}")
print(f"Результат: {'ПРОЙДЕНО' if monobit_passed else 'НЕ ПРОЙДЕНО'}")

# Long Run Test (перевірка максимальної довжини підряд однакових бітів)
max_run = 1
current_run = 1
for i in range(1, len(bit_stream)):
    if bit_stream[i] == bit_stream[i-1]:
        current_run += 1
        if current_run > max_run:
            max_run = current_run
    else:
        current_run = 1

long_run_passed = max_run < 26
print(f"\nLONG RUN TEST")
print(f"Максимальна довжина серії: {max_run}")
print(f"Результат: {'ПРОЙДЕНО' if long_run_passed else 'НЕ ПРОЙДЕНО'}\n")

# 4. Перетворення бітового потоку у байти
big_random_number = int(bit_stream, base=2)
seq_bytes = big_random_number.to_bytes(20_000 // 8, byteorder='big')

# 5. Побудова графіка
plt.figure()
plt.scatter(list(seq_bytes[::2]), list(seq_bytes[1::2]), color='skyblue')
plt.title("Розподіл випадкових значень на площині")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xlim([0, 255])
plt.ylim([0, 255])
plt.tight_layout()
plt.show()