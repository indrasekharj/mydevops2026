# even_numbers= []
# for num in range (46):
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# odd_numbers= []
# for num in range (46):
#     if num % 2 != 0:
#         odd_numbers.append(num)
# print(odd_numbers)


# numbers = [5, 10, 15, 20]
# total = sum(numbers, start=10)
# print(total) # 60

lambda num: num ** 2
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]