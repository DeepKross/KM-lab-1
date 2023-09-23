import math
import matplotlib.pyplot as plt

# Визначимо крок інтеграції та інші константи
step = math.pi / 36
end = math.pi / 2


# Функція для обчислення інтегралу методом Сімпсона
def simpson_integral(func, a, b, n):
    h = (b - a) / n  # Ширина підінтервалу
    integral = func(a) + func(b)  # Додаємо значення функції на краях інтервалу

    # Обчислюємо інтеграл методом Сімпсона
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral


def integrand(t):
    return -math.log(abs(math.cos(t)))


# Обчислюємо інтеграл на кожному підінтервалі та додаємо до кумулятивного інтегралу
results = []
cumulative_integral = 0
x = 0
while x <= end:
    # Обчислюємо інтеграл на підінтервалі [x, x + step] з 4 підінтервалами (для формули Сімпсона)
    integral = simpson_integral(integrand, x, x + step, 4)
    cumulative_integral += integral

    # Зберігаємо результати
    results.append((x, cumulative_integral))
    x += step


# Функція для обчислення кількості значущих цифр та похибки для числа
def significant_digits_and_error(value, desired_error=0.0005):
    if value == 0:
        return 0, 0  # Немає значущих цифр для числа 0

    # Визначаємо кількість знаків до крапки у числі
    integer_part_digits = len(str(int(abs(value))))

    # Якщо число вже має достатню кількість значущих цифр, повертаємо їх кількість та дійсну похибку
    if integer_part_digits >= 4 or value >= desired_error * 2000:
        return integer_part_digits, 0.5 * 10 ** (integer_part_digits - 4)

    # Якщо число менше, ніж бажана похибка, то число не має значущих цифр
    if value < desired_error:
        return 0, desired_error

    # Обчислюємо кількість значущих цифр та похибку для числа
    error = desired_error
    digits = integer_part_digits
    while error > value * 0.1 and digits < 4:
        error *= 0.1
        digits += 1

    return digits, error


# Обчислюємо кількість значущих цифр та похибку для кожного значення в таблиці
table_with_error = []
for x, value in results:
    digits, error = significant_digits_and_error(value)
    table_with_error.append((x, value, digits, error))

# Повертаємо таблицю з похибками та значущими цифрами
print(table_with_error)

# Візуалізація результатів
x_vals = [x for x, _, _, _ in table_with_error]
y_vals = [y for _, y, _, _ in table_with_error]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b')
plt.title('Таблиця функції Лобачевського')
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.grid(True)
plt.xticks(x_vals, rotation=45)
plt.tight_layout()

# Додаємо значення та похибки до графіку
for x, y, digits, error in table_with_error:
    plt.text(x, y, f"{y:.{digits}f}±{error:.1e}", fontsize=9, ha='right', va='bottom')

plt.show()

