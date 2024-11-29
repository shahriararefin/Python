def key_exists(dictionary, key):
    return key in dictionary

my_dict = {'name': 'Alice', 
           'age': 25, 
           'city': 'New York'}

print(key_exists(my_dict, 'name')) 
print(key_exists(my_dict, 'address'))
