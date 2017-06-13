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
            print(row)
            list_dict1.append(row)

    return list_dict1


# Create 2 item tuple (key_field, value) use to create dictionary
def setup_keyfield(dictionary_list, key_field):
    key_value_list = []
    for dic in dictionary_list:
        # print(key_field, dic[key_field])
        print('hate_food', dic['hate_food'])
        key_value_list.append((dic[key_field],
                              ('hate_food', dic['hate_food'])))
    resultant_dict = dict(key_value_list)
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
print(setup_keyfield(file1, 'person_id'))
