# Комбінування: reduce_custom(lambda acc, x: acc + x, map_custom(lambda x: x * x, [1,2,3,4]), 0)
def map_custom(func, data):
    result = []
    for x in data:
        result.append(func(x))
    return result

def reduce_custom(func, data, initial):
    result = initial
    for x in data:
        result = func(result, x)
    return result

# Приклад
data = [1, 2, 3, 4]

result = reduce_custom(
    lambda acc, x: acc + x,
    map_custom(lambda x: x * x, data),
    0
)

print(result)  # 30