# Closure: def make_filter(n): ... Використати: greater_than_10 = make_filter(10)
def make_filter(n):
    def inner(x):
        return x > n
    return inner

# Приклад
greater_than_10 = make_filter(10)

data = [5, 12, 7, 20]

filtered = list(filter(greater_than_10, data))

print(filtered)  # [12, 20]