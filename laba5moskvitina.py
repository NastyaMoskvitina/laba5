import random
print("Задача 1")
spisok = [7, 17, 10, 24, 0]
chislo = int(input("Введите число: "))
if chislo in spisok:
    print(spisok, "Поздравляю, Вы угадали чило!")
else:
    print(spisok, "Нет такого числа!")

def zadacha2():
    print("Задача 2")
    k = 0
    spisok2 = [2, 7, 12, 22, 26, 17, 7]
    for i in spisok2:
        if spisok2.count(i) > 1 and i != k:
            print("Найдено повторяющиеся число: ", i)
            k = i

def zadacha3():
    print("Задача 3")
    dni_nedeli = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    vopros = int(input("Сколько выходных на недели Вы хотите?"))
    print("Ваши выходные дни: ", *dni_nedeli[len(dni_nedeli) - vopros:])
    print("Ваши рабочие дни: ", *dni_nedeli[:len(dni_nedeli) - vopros])

def zadacha4():
    print("Задача 4")
    md25 = ["Москвитина", "Шакиров", "Фёдорова", "Тембай", "Краснокутская"]
    md20 = ["Сергеев", "Кашкадамов", "Иванов", "Басов", "Бадминов"]
    sport_comanda = tuple(random.sample(md25, 2) + random.sample(md20, 2))
    print("1-МД-25: ", ' '.join(md25))
    print("1-МД-20: ", ' '.join(md20))
    print("Состав спортивной команды:", *sport_comanda)
    print("Длина кортежа команды:", len(sport_comanda))
    po_alfavitu = sorted(sport_comanda)
    print("Сортировка кортежа команды по алфавиту: ", *po_alfavitu)
    if "Иванов" in sport_comanda:
        print("Иванов есть в команде!", "Встречается", sport_comanda.count("Иванов"), "раз.")
    else:
        print("Иванова нет в команде.")

zadacha2()
zadacha3()
zadacha4()