# Реалізація map: def map_custom(func, data): ...
def map_custom(func, data):
    result = []
    for x in data:
        result.append(func(x))
    return result

# Приклад
data = [1, 2, 3, 4]

print(map_custom(lambda x: x * 2, data))   # [2, 4, 6, 8]
print(map_custom(lambda x: x ** 2, data))  # [1, 4, 9, 16]