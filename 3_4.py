"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
"""
dct = {"Палатка": 5, "Котелок": 1, "Вода": 5, "Спички": 0.2, "Консервы": 1, "Спальный мешок": 1.5, "Макароны": 0.3}
weight = float(input("Какой вес рюкзака: "))
weight_c = 0
lst = []
for key, value in dct.items():
    weight_c += value

if weight_c > weight:
    size = weight
    weight_c = 0
    for key, value in dct.items():
        if value <= size:
            size -= value
            weight_c += value
            lst.append(key)

    away = []
    for elem in dct:
        if elem not in lst:
            away.append(elem)
    print(f"Итого в рюкзак полезло {lst}, весом - {weight_c}. Не поместилось {away}")

else:
    print(f"Вместимость рюкзака ({weight}), а общий вес всех вещей ({weight_c}). Всё взяли и еще осталось место")