""" Напишите программу, которая принимает две строки вида “a/b” - дробь с
числителем и знаменателем. Программа должна возвращать сумму и произведение*
дробей. Для проверки своего кода используйте модуль fractions.
"""
import fractions
import math


number1 = input("Введите первую дробь a1/b1: ").split("/")
number2 = input("Введите вторую дробь a2/b2: ").split("/")

denominator = int(number1[1]) * int(number2[1])
res = int(number1[0]) * denominator // int(number1[1]) + int(number2[0]) * denominator // int(number2[1])
sum_frac = f"{res}/{denominator}"
print(f"Cложение дробей: {res}/{denominator}")
c1 = math.gcd(res, denominator)
print(res//c1, denominator//c1, sep='/')

num = int(number1[0]) * int(number2[0])
den = int(number1[1]) * int(number2[1])

c2 = math.gcd(num, den)
print(f"Произведение дробей: {num}/{den}")
print(num//c2, den//c2, sep='/')

fraction1 = fractions.Fraction(int(number1[0]), int(number1[1]))
fraction2 = fractions.Fraction(int(number2[0]), int(number2[1]))
print(f"Проверка сложения Fractions() {fraction1 + fraction2}")
print(f"Проверка произведения Fractions() {fraction1 * fraction2}")