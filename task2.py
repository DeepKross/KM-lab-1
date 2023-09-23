# Імпорт бібліотеки для візуалізації
import matplotlib.pyplot as plt

# Кількість прямокутників
n = 1000
# Ширина кожного прямокутника
h = 1.0 / n


def f(x):
    """Функція, яку ми інтегруємо"""
    from math import exp, sqrt  # Імпортуємо exp та sqrt з вбудованої бібліотеки math
    return exp(x) / sqrt(x) if x > 0 else 0  # Додаємо умову для випадку, коли x = 0


# Ініціалізація суми для зберігання результату
integral_sum = 0.0

# Масиви для візуалізації
x_points = []
y_points = []

# Обчислення інтеграла
for i in range(n):
    x = i * h  # Початкова точка i-го прямокутника
    mid_point = x + h / 2  # Середина i-го прямокутника
    # Обчислення площі i-го прямокутника та додавання до суми
    integral_sum += f(mid_point) * h

    # Зберігання точок для візуалізації
    x_points.append(mid_point)
    y_points.append(f(mid_point))

# Візуалізація
plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, color='b', label='f(x)')
plt.bar(x_points, y_points, width=h, alpha=0.3, align='center', color='r', edgecolor='black')
plt.title('Квадратурна формула середніх прямокутників')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Результат обчислення інтеграла
print(integral_sum)
