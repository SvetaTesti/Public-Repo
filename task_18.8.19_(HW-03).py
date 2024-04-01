ticket = 0

quant = (int(input("Количество билетов:")))

for age in range(quant):
    age = (int(input("Возраст посетителя:")))
    if age < 18:
        ticket += 0
    elif age >= 18 and age <= 25:
        ticket += 990
    elif age > 25:
        ticket += 1390


print("Сумма", ticket)
if quant > 3:
    discount = ticket * 0.1
    print("Скидка 10%", discount)
    print("Сумма к оплате", ticket - discount)