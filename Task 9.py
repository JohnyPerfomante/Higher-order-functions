# Генератор функцій: def multiplier(n): ...
def multiplier(n):
    def inner(x):
        return x * n
    return inner

# Приклад
times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50