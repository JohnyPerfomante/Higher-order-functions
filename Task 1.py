# Реалізувати: def apply(func, x): ... Перевірити: apply(lambda x: x * 2, 5), apply(lambda x: x + 10, 5)
def apply(func, x):
    return func(x)

# Приклад
print(apply(lambda x: x * 2, 5))   # 10
print(apply(lambda x: x + 10, 5))  # 15