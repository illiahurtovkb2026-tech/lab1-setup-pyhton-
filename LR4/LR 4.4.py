alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
n = len(alphabet)

# Параметри шифру
a, b = 17, 5

# Обернене значення a^-1 mod n (для 17 за модулем 32 це буде 17)
a_inv = pow(a, -1, n)

ciphertext = "гж а ьдпчш аїлдіьч фкщжьрїд ьдяючх."

decrypted_text = ''
for c in ciphertext:
    if c not in alphabet:
        decrypted_text += c
    else:
        y = alphabet.index(c)
        dec_y = (a_inv * (y - b)) % n
        decrypted_text += alphabet[dec_y]

print("Розшифрований текст:", decrypted_text)