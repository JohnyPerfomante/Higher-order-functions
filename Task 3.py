# Переписати код: result = [] for x in data: result.append(x * 2) у вигляді: def transform(data, func): ...
def transform(data, func):
    result = []
    for x in data:
        result.append(func(x))
    return result

# Приклад
data = [1, 2, 3, 4, 5]

print(transform(data, lambda x: x * 2))   # [2, 4, 6, 8, 10]
print(transform(data, lambda x: x + 1))   # [2, 3, 4, 5, 6]