my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

new_list = list(my_list)
new_list.sort()
print(new_list)


desc_list = list(my_list)
desc_list.sort(reverse=True)
print(desc_list)

even_list = new_list[::2]
print(even_list)

odd_list = new_list[1::2]
print(odd_list)

multiply_of_3 = new_list[2::3]
print(multiply_of_3)