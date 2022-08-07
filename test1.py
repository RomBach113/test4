# Задайте натуральное число N. 
# Напишите программу, 
# которая составит список 
# простых множителей числа N.

N=int(input('Ведите натуральное число: '))
def faction (a):
    fact = []
    num=2
    while num*num <= a:
        if a%num == 0:
            fact.append(num)
            a//=num
        else:
            num+=1
    if a>1:
        fact.append(a)
    return fact

print(faction(N))
