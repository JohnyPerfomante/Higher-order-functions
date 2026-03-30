# Реалізація filter: def filter_custom(func, data): ...
def filter_custom(func, data):
    result = []
    for x in data:
        if func(x):
            result.append(x)
    return result

# Приклад
data = [1, 2, 3, 4, 5, 6]

print(filter_custom(lambda x: x % 2 == 0, data))  # [2, 4, 6]
print(filter_custom(lambda x: x > 3, data))       # [4, 5, 6]