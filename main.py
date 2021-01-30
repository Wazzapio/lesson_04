def my_f(symbol_1, symbol_2):
    return symbol_1 + symbol_2

random_str = ['a', 'b', 'c', 'd', 'e']
print(reduce(my_f, random_str))