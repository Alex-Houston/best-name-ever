print("Привет, мир!")
a = 'Привет'
b = 'программист'
print(f'{a}, {b}!') 
print(2+2)
print(10/3)

name = input('Vvedite imya: ')
print(f'Privet, {name}, kak dela?')

list1 = [3, 5, 7 ,9, 10.5]
print(list1)
list1.append("Python")
print(list1)
print(len(list1))
print(list1.count(6))
print(list1[1])
print(list1[-1])
print(list1[-6])
print(list1[5])
print(3 in list1)
print('3' in list1)
del list1[1]
list1.remove(3)
print(list1)

print(' ')
print(' ')

my_first_dictionary = {"city": "Москва", "temperature": "20",}
print(my_first_dictionary["city"])
my_first_dictionary["temperature"] = str(int(my_first_dictionary["temperature"])+5)
print(my_first_dictionary)
print(my_first_dictionary.get("country"))
print(my_first_dictionary.get("country", "Россия"))
print(my_first_dictionary)
my_first_dictionary["date"] = '27.05.2019'
print(', '.join(my_first_dictionary.values()))
print(len(my_first_dictionary))
