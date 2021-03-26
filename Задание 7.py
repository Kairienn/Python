import json
profit = {}
gain = {}
prof = 0
prof_average = 0
counter = 0
with open('my_file_7.txt', 'r') as file:
    for l in file:
        name, firm, earning, costs = l.split()
        profit[name] = int(earning) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            counter += 1
    if counter != 0:
        prof_average = prof / counter
        print(f'Прибыль средняя - {prof_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    gain = {'средняя прибыль': round(prof_average)}
    profit.update(gain)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')