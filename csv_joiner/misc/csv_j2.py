# csv_j2.py
# Protoype the joining of 2 different CSV files based on a common item.
import csv
import collections
import pprint


############
# Functions
############
# TODO: Check for key_field
# TODO: Automaticly parse CSV files that have the key_field
# TODO: Add key_name field name  as key_name : key_field

def return_dictnry_list(filename):

    list_dict1 = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_dict1.append(row)

    return list_dict1


# Create 2 item tuple (key_field, value) use to create dictionary
def setup_keyfield(dictionary_list, key_field):
    key_value_list = []
    for dic in dictionary_list:
        # Pull all k,v pairs except the key_field
        nested_dict = {}
        for k, v in dic.items():
            if k != key_field:
                nested_dict[k] = v

        key_value_list.append((dic[key_field], (nested_dict)))
        resultant_dict = dict(key_value_list)

    return resultant_dict


def populate_dictionary(input_dict, resultant_dict):
    pass
    return


# https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(d, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = deep_update(d.get(k, {}), v)
                d[k] = r
            else:
                d[k] = u[k]
        else:
            d = {k: u[k]}
    return d
###########


file1 = return_dictnry_list('foods.csv')
file2 = return_dictnry_list('drink.csv')

dict1 = setup_keyfield(file1, 'person_id')
dict2 = setup_keyfield(file2, 'person_id')

print('food.csv')
pprint.pprint(dict1)
print('drink.csv')
pprint.pprint(dict2)

deep_update(dict1, dict2)
print('Combined')
pprint.pprint(dict1)

dict3 = setup_keyfield(return_dictnry_list('foods.csv'), 'person_id')
print('Test3')
pprint.pprint(dict3)
