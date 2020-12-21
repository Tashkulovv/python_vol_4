# dictionary - словари
'''new_dict = {}
new_dict2 = dict()
print(type(new_dict))

new_dict = {'key' : 'value', 'key1': 'value', 'Siymyk': '0709943799'}
print(new_dict)

capitals = {}
capitals['KG']='Bishkek'
capitals['RUS'] =  'Moscow'
capitals['RUS'] = 'SP'

print(capitals)



capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
print(capitals)
capitals = dict([('RUS', 'Moscow'), ('KG','Bishkek'), ('GB', 'London')])
print(capitals)'''

'''new_dict =dict(zip(['RUS', 'KG', 'GB'], ['Moskow','Bishkek', 'London']))
print(new_dict)'''

# method fromkeys создает словарь из ключей
dictionary = dict.fromkeys(['key1', 'key2'],[ "7", '8'])
print(dictionary)

# method get получает знач по ключу

'''capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
print(capitals.get('RUS'))

nums = {1:2, 3:4, 5:6}
print(nums[1])
nums [3 ] = 8888
print(nums[3])
print(nums)'''


# method keys выводит все ключи из словаря
# method values выводит все значения
# method items возвращает пару ключ и значение
# method pop удаляет по ключу и возвращвет ном значение

'''capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
print(capitals.values())
print(capitals.keys())
print(capitals.items())
print(capitals.pop('RUS'))

'''

# method update
'''capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
capitals2 = {'Belarus': 'Minsk', 'RUS': 'SPB'}
capitals.update(capitals2)
print(capitals)
'''

# method popitem удаляет последнии элемент
'''capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
gb = capitals.popitem()
print(gb)
print(capitals)
'''

# method setdefault
'''capitals = dict(RUS='Moscow', KG = 'Bishkek', GB='London')
new = capitals.setdefault('KG')
print(new)
print(capitals)'''

'''new_dict = {}
new_dict2 = dict()
print(type(new_dict2))'''
