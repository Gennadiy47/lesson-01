# Задача 2
num = input('Введите 3-х значное число: ')
res = 0
if len(num) == 3:
     for i in num:
         res += int(i)
     print(res)
else:
     print('Вы ввели не 3-х значное число')

# Задача 4
k = input("Введите общее количество журавликов ");
ps = int(str(k))//6;
print("Петя и Сережа сделали по", ps, ", а Катя сделала", ps*4);

# Задача 6

s = str(input("Введите номер билета "))
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
  print('Счастливый')
else:
  print('Обычный')


# Задача 8

n, m, k = int(input('Введите  1-ю сторону: ')), int(input('Введите 2-ю сторону: ')), int(input('Введите кол-во долек: '))
if k%n == 0 or k%m == 0:
    print('Yes')
else: print('No')