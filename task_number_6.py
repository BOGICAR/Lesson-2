# Задание №6 - сделано
entered_number = float(input())
abs_entered_number = abs(entered_number)
available_list = list(range(10, 101, 10)) # Если я правильно сделал, то список записан как кортеж
# print(available_list)  - смотрел правильность состовления списка
if abs_entered_number in available_list:
    print('The entered number is in the list')
else:
    print('The entered number is not in the list')