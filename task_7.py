n = int(input("Введите число до которого нужно произвести вычисления факторилов: "))
def fact(n):
    num = 1
    n += 1
    for el in range(1, n):
            answer = num * el
            num = answer
            print(f'{el}! = {answer}')
    return answer

def generator():
    for el in fact(n):
        yield el
g = generator()
for el in g:
    print(el)
"""
Программа срабатывает до конца, но хоть убей не пойму как исправить ошибку.
"""