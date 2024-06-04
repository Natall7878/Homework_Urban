first = (int(input('Введите первое число: ')))
second = (int(input('Введите второе число: ')))
third = (int(input('Введите третье число: ')))

if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second and first != third and second != third:
    print('0')

# elif not (first== second) and  not(first ==third) and not (second == third):
#     print ('0') Можно так, раз в условии задачи указан not, но это более громоздко, на мой взгляд
