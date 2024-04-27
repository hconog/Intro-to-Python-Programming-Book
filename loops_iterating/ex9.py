def factorial(number):
  product = 1
  for factor in range(1, number + 1):
    product *= factor
  return product
print(factorial(5))