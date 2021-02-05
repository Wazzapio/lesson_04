from sys import argv

script_name, time, bet, bonus = argv

print("Имя скрипта: ", script_name)
print("Кол-во отработанных часов: ", time)
print("Ставка в час: ", bet)
print("Премия: ", bonus)

def wage():
    answer = (float(time) * float(bet)) + float(bonus)
    return answer

print(f'Заработная плата составляет: {wage()}')