start = 100
stop = 1000
step = 2
stop = stop + step
new_list = [el for el in range(start, stop, step)]
print(new_list)
from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, new_list))