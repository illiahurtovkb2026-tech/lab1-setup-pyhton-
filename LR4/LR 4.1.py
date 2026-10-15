a = 30128
b = 67324
n = 85527

print("Пунтк A: Квадрати чисел менші за n ")
i = 1
squares = []
while i * i < n:
    squares.append(str(i * i))
    i += 1
print(" ".join(squares))

print("\nПункт B: Степені двійки менші за n")
power = 1
powers_of_two = []
while power < n:
    powers_of_two.append(str(power))
    power *= 2
print(" ".join(powers_of_two))

print("\nПункт C: Сума всіх парних чисел між a та b")
sum_even = 0
for num in range(a, b + 1):
    if num % 2 == 0:
        sum_even += num
print(f"Результат: {sum_even}")

print("\nПункт D: Сума всіх непарних чисел кратних 3 між a та b")
sum_odd_mult3 = 0
for num in range(a, b + 1):
    if num % 2 != 0 and num % 3 == 0:
        sum_odd_mult3 += num
print(f"Результат: {sum_odd_mult3}")

print("\nПункт E: Сума всіх непарних цифр числа n")
sum_odd_digits = 0
temp_n = n
while temp_n > 0:
    digit = temp_n % 10
    if digit % 2 != 0:
        sum_odd_digits += digit
    temp_n //= 10
print(f"Для числа {n} сума непарних цифр дорівнює: {sum_odd_digits}")
