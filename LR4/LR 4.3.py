import colorama
from colorama import Fore

colorama.init(autoreset=True)

low_char = "abcdefghijklmnopqrstuvwxyz"
spc_char = "!@#$%^&*-"
allowed_chars = low_char + spc_char

print("Введіть пароль довжиною не менше 12 символів.")
print("Вимоги до паролю:")
print("1. Маленькі латинські літери та спеціальні символи")
print("2. Не менше 3 маленьких латинських літер")
print("3. Не більше 6 маленьких латинських літер")
print("4. Не менше 3 спеціальних символів")
print("5. Не більше 4 спеціальних символів")
print("6. Не більше 3 однакових маленьких латинських літер")
print("7. Не більше 3 однакових спеціальних символів підряд")

password = input(">>> ")

len_ok = len(password) >= 12
print(
    (Fore.GREEN if len_ok else Fore.RED)
    + "Довжина не менше 12 символів – "
    + ("OK!" if len_ok else "FAIL!")
)

# Допустимі символи
only_allowed = True
for ch in password:
  if ch not in allowed_chars:
    only_allowed = False
    break

print(
    (Fore.GREEN if only_allowed else Fore.RED)
    + "Пароль містить лише допустимі символи – "
    + ("OK!" if only_allowed else "FAIL!")
)

# Підрахунок кількості літер та спецсимволів
low_count = 0
spc_count = 0
for ch in password:
  if ch in low_char:
    low_count += 1
  elif ch in spc_char:
    spc_count += 1

# Правила 2 і 15 (маленькі літери)
r2 = low_count >= 3
print(
    (Fore.GREEN if r2 else Fore.RED)
    + "Не менше 3 маленьких латинських літер – "
    + ("OK!" if r2 else "FAIL!")
)

r15 = low_count <= 6
print(
    (Fore.GREEN if r15 else Fore.RED)
    + "Не більше 6 маленьких латинських літер – "
    + ("OK!" if r15 else "FAIL!")
)

# Правила 12 і 23 (спецсимволи)
r12 = spc_count >= 3
print(
    (Fore.GREEN if r12 else Fore.RED)
    + "Не менше 3 спеціальних символів – "
    + ("OK!" if r12 else "FAIL!")
)

r23 = spc_count <= 4
print(
    (Fore.GREEN if r23 else Fore.RED)
    + "Не більше 4 спеціальних символів – "
    + ("OK!" if r23 else "FAIL!")
)

# Правило 25: Не більше 3 однакових маленьких латинських літер (загалом)
max_same_low = 0
for l_ch in low_char:
  cnt = 0
  for ch in password:
    if ch == l_ch:
      cnt += 1
  if cnt > max_same_low:
    max_same_low = cnt

r25 = max_same_low <= 3
print(
    (Fore.GREEN if r25 else Fore.RED)
    + "Не більше 3 однакових маленьких латинських літер – "
    + ("OK!" if r25 else "FAIL!")
)

# Правило 34: Не більше 3 однакових спеціальних символів підряд
max_consec_spc = 0
current_consec = 0
for i in range(len(password)):
  if i > 0 and password[i] == password[i - 1] and password[i] in spc_char:
    current_consec += 1
  elif password[i] in spc_char:
    current_consec = 1
  else:
    current_consec = 0

  if current_consec > max_consec_spc:
    max_consec_spc = current_consec

r34 = max_consec_spc <= 3
print(
    (Fore.GREEN if r34 else Fore.RED)
    + "Не більше 3 однакових спеціальних символів підряд – "
    + ("OK!" if r34 else "FAIL!")
)

# Підсумок
print()
if (
    len_ok
    and only_allowed
    and r2
    and r15
    and r12
    and r23
    and r25
    and r34
):
  print(Fore.GREEN + "Пароль валідний!")
else:
  print(Fore.RED + "Пароль не валідний!")