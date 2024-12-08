def calculate_structure_sum(counting):
    b = 0
    if isinstance(counting, int) or isinstance(counting, float):
        return counting
    elif isinstance(counting, str):
        return len(counting)
    elif isinstance(counting, list):
        for item in counting:
            b += calculate_structure_sum(item)
        return b
    elif isinstance(counting, tuple):
        for item in counting:
            b += calculate_structure_sum(item)
        return b
    elif isinstance(counting, set):
        for item in counting:
            b += calculate_structure_sum(item)
        return b
    elif isinstance(counting, dict):
        for key in counting.items():
            b += calculate_structure_sum(key)

        return b
    else:
        return 0  # Возвращаем 0 для неподдерживаемых типов

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
