name=['Вася', 'Нина', 'Валя', 'Петя', 'Сергей']
salary=[12000, 23000, 15456, 25000, 45620]
bonus=['10.25%', '15.00%', '12.23%', '10.00%', '25.00%']

res={n: s for n, s in zip(name, [s*(float(b[:-1])/100) for s, b in zip(salary, bonus)])}
print(res)