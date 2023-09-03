"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""
lst = [1, 2, 4, 5, 6, 4, 2, 6, 4]
unic = set()
duplicate_lst ={ x for x in lst if x in unic or (unic.add(x) or False)}

print(duplicate_lst)
