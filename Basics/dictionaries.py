# Dictionary, Methods

dict1 = {
    'name': 'John',
    'surname': 'Isner',
    'age': 30,
    'job': 'tennis',
    'hobby': 'surfing',
}

print(f"{dict1['name']} is a {dict1['age']} year old {dict1['job']} player with hobby for {dict1['hobby']}.")

del dict1['hobby']
print("%s" % str(dict1))  # {'name': 'John', 'surname': 'Isner', 'age': 30, 'job': 'tennis'}

print(len(dict1))  # 4
print(type(dict1))  # <class 'dict'>

# Methods
dict1 = {'name': 'Peter', 'age': 15}

dict2 = dict1.copy(); print(dict2)  # {'name': 'Peter', 'age': 15}

dict2.clear(); print(dict2)  # {}

keySequence = ('name', 'age', 'job')
dict2 = dict.fromkeys(keySequence); print("%s" % str(dict2))  # {'name': None, 'age': None, 'job': None}
dict2.clear(); dict2 = dict.fromkeys(keySequence, 10); print(dict2)  # {'name': 10, 'age': 10, 'job': 10}

print(dict1.get('age'))  # 15
print(dict1.get('hobby', 'Never'))  # Never (default value if it does not exist)

print('age' in dict1)  # True (old has_key method)

print(dict1.keys(), dict1.values())  # dict_keys(['name', 'age']) | dict_values(['Peter', 15])
print(dict1.items())  # dict_items([('name', 'Peter'), ('age', 15)])

dict1.setdefault('hobby', None); print(dict1)  # {'name': 'Peter', 'age': 15, 'hobby': None}
dict2 = {'gender': 'Male'}; dict1.update(dict2)
print(dict1)  # {'name': 'Peter', 'age': 15, 'hobby': None, 'gender': 'Male'}
