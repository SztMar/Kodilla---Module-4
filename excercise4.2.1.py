shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

sorted_items_1 = sorted(shopping_items, key=get_index_1_tuple_element)
sorted_items_2 = sorted(shopping_items, key=lambda given_tuple: given_tuple[1]) #using lambda
print(sorted_items_1)
print(sorted_items_2)

help(cus)