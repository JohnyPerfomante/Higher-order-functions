# Реалізація reduce: def reduce_custom(func, data, initial): ...
def reduce_custom(func, data, initial):
    result = initial
    for x in data:
        result = func(result, x)
    return result

# Приклад
data = [1, 2, 3, 4]

print(reduce_custom(lambda a, b: a + b, data, 0))      # 10
print(reduce_custom(lambda a, b: a * b, data, 1))      # 24