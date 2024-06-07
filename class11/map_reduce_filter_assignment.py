from functools import reduce
numbers = [1, 2, 3, 4, 5]

cubed_numbers = list(map(lambda x: x ** 3, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

mul_of_numbers = reduce(lambda x, y: x * y, numbers, 0)

print("cubed_numbers:",cubed_numbers)
print("even_numbers:",even_numbers)
print("mul_of_numbers:",mul_of_numbers)



