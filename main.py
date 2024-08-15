def print_params (a =1, b = 'строка', c = True):
    print(a, b, c)

print_params(3, 'hello')
print_params(-343, 'ffff', c = False)
print_params(b = 25)
print_params(c = [1, 2 , 3])
values_list = [False, 222, 'Hello']
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['Hi', 22]
print_params(*values_list_2, 42)
