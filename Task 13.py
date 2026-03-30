# Pipeline: def pipeline(data, steps): ... Використання: pipeline ([1,2,3,4,5], [lambda xs: list(filter(lambda x: x%2==0, xs)), lambda xs: list(map(lambda x: x*x, xs))])
def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result

# Приклад
data = [1, 2, 3, 4, 5]

result = pipeline(
    data,
    [
        lambda xs: list(filter(lambda x: x % 2 == 0, xs)),
        lambda xs: list(map(lambda x: x * x, xs))
    ]
)

print(result)  # [4, 16]