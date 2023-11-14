per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Ввести сумму вклада"))
depozit = []
for key in per_cent: 
   depozit.append(int(per_cent[key]*money/100))
print(depozit)
max_depozit = max(depozit)
print(max_depozit) #максимальная сумма по депозиту

