import hashlib
from string import ascii_lowercase, digits

# Цільовий хеш
target_hash = "111f05b2330a3fc2aff30a18421f8fd461b49bcc9e482fe743eb40fc5bb4ba00"

# Зменшений набір символів (або всі малі літери і цифри: ascii_lowercase + digits)
chars = ascii_lowercase + digits

print("Пошук пароля розпочато...")

found = False
# 6 вкладених циклів для 6 символів
for s1 in chars:
    for s2 in chars:
        for s3 in chars:
            for s4 in chars:
                for s5 in chars:
                    for s6 in chars:
                        # Збираємо пароль з 6 символів
                        psw = s1 + s2 + s3 + s4 + s5 + s6

                        # Рахуємо хеш
                        generate_hash = hashlib.sha256(psw.encode()).hexdigest()

                        # Перевіряємо
                        if generate_hash == target_hash:
                            print(f"Пароль знайдено: {psw}")
                            found = True
                            break  # Вихід з найглибшого циклу
                    if found:
                        break
                if found:
                    break
            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("Пароль не знайдено.")