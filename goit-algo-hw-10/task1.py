import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

model += 1 * lemonade <= 50, "Sugar_Constraint"

model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Лимонаду треба виробити: {lemonade.varValue}")
print(f"Фруктового соку треба виробити: {fruit_juice.varValue}")
print(f"Загальна кількість продуктів: {lemonade.varValue + fruit_juice.varValue}")