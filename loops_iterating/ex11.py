my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]
index = 0
while index < len(my_list):
  nested_index = 0
  nested_list = my_list[index]
  while nested_index < len(nested_list):
    number = nested_list[nested_index]
    if number % 2 == 0:
      print(number)
    nested_index += 1
  index += 1