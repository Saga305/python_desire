from functools import reduce
numbers = [1, 2, 3, 4, 5]

cubed_numbers = list(map(lambda x: x ** 3, numbers))

even_of_cubed_numbers = list(filter(lambda x: x % 2 == 0, cubed_numbers))

mul_of_even_cubed_numbers = reduce(lambda x, y: x * y, even_of_cubed_numbers, 1)

print("numbers:",numbers)
print("cubed_numbers:",cubed_numbers)
print("even_of_cubed_numbers:",even_of_cubed_numbers)
print("mul_of_even_cubed_numbers:",mul_of_even_cubed_numbers)



