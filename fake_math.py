def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first/second

result1 = divide(69, 3)
result2 = divide(3, 0)

print(divide(69, 3))
print(divide(3, 0))