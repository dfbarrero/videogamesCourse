import os

name = 'Pepe'
age = 25
city = 'Alcalá de Henares'

path = 'data' + os.sep + 'person.txt'

file = open(path, 'w', encoding='utf-8')

file.write('Name: ' + name + '\n')
file.write('Age: ' + str(age) + '\n')
file.write('City: ' + city + '\n')

file.close()
