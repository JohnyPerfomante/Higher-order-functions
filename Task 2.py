# Реалізувати функцію: def calculate(operation, a, b): ... Використати: додавання, множення, піднесення до степеня.
def calculate(operation, a, b):
    return operation(a, b)

# Приклад
print(calculate(lambda a, b: a + b, 2, 3))
print(calculate(lambda a, b: a * b, 2, 3))
print(calculate(lambda a, b: a ** b, 2, 3))