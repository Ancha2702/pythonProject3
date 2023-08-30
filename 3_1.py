"""
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""
dct = {"Ваня": ("Палатка", "Спички", "Консервы", "Нож", "Вода"),
        "Вася": ("Палатка", "Котелок", "Топор", "Вода"),
        "Оля": ("Палатка", "Котелок", "Спички", "Консервы", "Соль"),
        }
sets = set()
for key in dct:
    if not sets:
        sets = set(dct[key])
    else:
        sets = sets.intersection(set(dct[key]))
print(f'Всё что взяли друзья:', *sets)

friends = dct.keys()
unc_set = set()
for friend in friends:
    to_remove = set(dct[friend])
    one_set = set()
    unc_set = set(dct[friend])
    for other_friend in friends:
        if other_friend != friend:
            unc_set = unc_set.difference(set(dct[other_friend]))
            if not one_set:
                one_set = set(dct[other_friend])
            else:
                one_set = one_set.intersection(set(dct[other_friend]))
    one_set -= to_remove
    if unc_set:
        print(f'Уникальные вещи у: {friend} -', *unc_set)
    if one_set:
        print(*one_set, f'есть у всех, кроме {friend}')