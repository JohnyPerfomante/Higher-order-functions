# Compose: def compose(f, g): ...
def compose(f, g):
    return lambda x: f(g(x))

# Приклад
def double(x):
    return x * 2

def add_three(x):
    return x + 3

double_after_add = compose(double, add_three)

print(double_after_add(5))  # (5 + 3) * 2 = 16