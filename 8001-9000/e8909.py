count = 0

# Встановлюємо нескінченний цикл
while True:
    # Зчитуємо число
    n = int(input())
    # Перевіряємо, чи дорівнює воно нулю. Якщо так, виходимо з циклу
    if n == 0:
        break
    # Якщо число не нуль, додаємо до лічильника одиницю
    count += 1

# Друкуємо результат - кількість успішно пройдених ітерацій циклу
print(count)