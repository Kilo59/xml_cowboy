# join_csv_test.py
# Protoype the joining of 2 different CSV files based on a common item.


import csv


############
# Functions
############

def return_dictnry_list(filename):

    list_dict1 = []

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        # print(type(reader))
        for row in reader:
            # print(row)
            list_dict1.append(row)

    return list_dict1


# Create 2 item tuple (key_field, value) use to create dictionary
def setup_keyfield(dictionary_list, key_field):
    key_value_list = []
    key_value_list2 = []
    for dic in dictionary_list:
        # Test 1 item list
        print('hate_food', dic['hate_food'], end=' ')
        test_list2 = {'hate_food': dic['hate_food'],
                      'fav_food': dic['fav_food']}
        print(test_list2)
        key_value_list2.append((dic[key_field],
                                (test_list2)))
        print('TestL', key_value_list2)
        resultant_dict2 = dict(key_value_list2)
        print('TestD', resultant_dict2)

        key_value_list.append((dic[key_field],
                               ('hate_food', dic['hate_food'])))
    resultant_dict = dict(key_value_list)
    print('Orginal', resultant_dict)
    return resultant_dict


# def setup_keyfield(dictionary_list, key_field):
#     key_value_list = []
#     for dic in dictionary_list:
#         # print(key_field, dic[key_field])
#         key_value_list.append((dic[key_field], key_field))
#     resultant_dict = dict(key_value_list)
#     return resultant_dict


def populate_dictionary(input_dict, resultant_dict):
    pass
    return
###########


file1 = return_dictnry_list('foods.csv')
file2 = return_dictnry_list('drink.csv')

# print(file2)
# print(file1)
setup_keyfield(file1, 'person_id')
