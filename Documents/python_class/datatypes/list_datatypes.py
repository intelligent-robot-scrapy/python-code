my_list = ["string", 1, 0.1, ("tetosterone", 5343, 342.49374, True, ), False]
tuple_item = my_list[3]
print(tuple_item)
print(my_list)
tuple_item = list(tuple_item)
tuple_item[1] = 5000
tuple_item = tuple(tuple_item)
print(tuple_item)
my_list[3] = tuple_item

print(my_list)
# popped = my_list.pop(3)
# doublepop= []
# doublepop.insert(popped)
# doublepop.index(5343)
# print(my_list)