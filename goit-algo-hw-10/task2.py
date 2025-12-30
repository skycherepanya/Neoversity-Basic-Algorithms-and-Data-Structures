import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
ax.grid()
plt.show()

# Перевірка функцією quad
result_quad, error = spi.quad(f, a, b)
print("Інтеграл: ", result_quad, error)

# Метод Монте-Карло
N = 100000
x_monte = np.random.uniform(a, b, N)
y_monte = np.random.uniform(0, f(b), N)

under_curve = np.sum(y_monte < f(x_monte))

sq_rect = (b - a) * f(b)

# Результат Монте-Карло
result = (under_curve / N) * sq_rect

print(f"Інтеграл (Монте-Карло):       {result}")
print(f"Абсолютна помилка:             {abs(result - result_quad)}")