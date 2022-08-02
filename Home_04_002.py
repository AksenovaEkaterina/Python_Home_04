# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
import random

N = int(input('введите число '))
List_multipliers = []
NumRandom=[2,3,5,7]
while ((N%7)==0)or((N%5)==0)or((N%3)==0)or((N%2)==0):
    a = random.choice(NumRandom)
    if (N%a)==0:
        List_multipliers.append (a)
        N=N//a
    else:
        continue
List_multipliers.append (N)
print(List_multipliers)
