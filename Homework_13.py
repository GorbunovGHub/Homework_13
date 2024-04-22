def print_params(a=1, b='string', c=True):
    print(a, b, c)

values_list = [1, 'string_2', False]
values_dict = {'a': 1, 'b': 'string_2', 'c': False}
values_list_2 = [1, True]

print_params()
print_params(a=2, c=False, b=2)
print_params(b='apple')

print_params(b=25)
print_params(c=[1, 2, 3])

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)
