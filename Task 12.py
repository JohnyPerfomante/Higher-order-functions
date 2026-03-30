# Розширена композиція: def compose_many(*funcs): ...
def compose_many(*funcs):
    def composed(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed

# Приклад
def double(x):
    return x * 2

def add_three(x):
    return x + 3

def square(x):
    return x ** 2

composed_func = compose_many(square, add_three, double)

print(composed_func(2))
# double(2) = 4
# add_three(4) = 7
# square(7) = 49