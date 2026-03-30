# Умова: def process(data, transform, predicate): ... Використати: парні числа, квадрат значення.
def process(data, transform, predicate):
    result = []
    for x in data:
        if predicate(x):
            result.append(transform(x))
    return result

# Приклад
data = [1, 2, 3, 4, 5, 6]

print(process(
    data,
    lambda x: x ** 2,
    lambda x: x % 2 == 0
))