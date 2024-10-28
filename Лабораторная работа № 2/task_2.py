salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Изначально подушка безопасности равна нулю
required_safety_capital = 0

for _ in range(months):
    required_safety_capital += spend - salary  # Добавляем разницу между тратами и зарплатой
    spend *= (1 + increase)  # Увеличиваем траты на 3% для следующего месяца

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(required_safety_capital))
