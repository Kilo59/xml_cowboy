# extensible data group
# allow multiple csv files to be "joined" together using a common field with unique values (like a SQL join)
import csv
import collections
import pprint
import copy
# import itertools
# import sys


#################
# Class DEFINITION
#################


# combined_data_grp  holds 1 or more data_groups and "joins" them on a common field
class data_grp(object):
    # instiate object
    def __init__(self, key_field_name, core_filename, suppl_filename=None, excluded_fields=[]):
            self.key_field_name = key_field_name
            self.core_filename = core_filename
            self.suppl_filename = suppl_filename
            self.data_grp_core = data_object(self.key_field_name, self.core_filename)
            self.num_data_grps = 1
            if self.suppl_filename is not None:
                self.data_grp_suppl = data_object(self.key_field_name, self.suppl_filename)
                self.dictionary = self.melder(self.data_grp_core, self.data_grp_suppl)
                self.fields = list(set(self.data_grp_core.o_fields + self.data_grp_suppl.o_fields))
            else:
                self.dictionary = self.data_grp_core.dictionary
                self.fields = self.data_grp_core.o_fields
            self.excluded_fields = excluded_fields

            self.report_obj = report_obj(self.get_dictionary(), r_excld_fields=self.excluded_fields)

    def __str__(self):
        # return pprint.pformat(self.melded_dictionary)
        return 'data_grps: ' + str(self.num_data_grps) + '\nKey: ' + self.key_field_name + '\n' \
            + pprint.pformat(self.dictionary)

    def deep_update(self, d, u):
        for k, v in u.items():
            if isinstance(d, collections.Mapping):
                if isinstance(v, collections.Mapping):
                    r = self.deep_update(d.get(k, {}), v)
                    d[k] = r
                else:
                    d[k] = u[k]
            else:
                d = {k: u[k]}
        return d

    def melder(self, data_grp_core, data_grp_suppl):
        core_dict = data_grp_core.dictionary
        if self.suppl_filename is not None:
            suppl_dict = data_grp_suppl.dictionary
            # check for key_field
            if self.key_field_name == suppl_dict['PRIMARY_KEY']:
                melded_dictionary = self.deep_update(core_dict, suppl_dict)
                self.num_data_grps = self.num_data_grps + 1
                return melded_dictionary
            else:
                print('*' * 10 + '\nERROR: KEYS do not match\n' + '*' * 10)
                return core_dict
        else:
            return core_dict

    def get_dictionary(self, strip_pkey=True):
        returned_dict = copy.deepcopy(self.dictionary)
        if strip_pkey is True:
            returned_dict.pop('PRIMARY_KEY')
        return returned_dict

    def str_dictionary(self, strip_key=True):
        return pprint.pformat(self.get_dictionary(strip_key))


class data_object(object):
    # instiate object
    def __init__(self, key_field_name, filename):
        self.key_field_name = key_field_name
        self.filename = filename
        self.o_fields = [self.key_field_name]
        self.dictionary = self.setup_keyfield(self.return_dictnry_list(self.filename), self.key_field_name)

    def __str__(self):
        return 'Key: ' + self.key_field_name + '\n' + pprint.pformat(self.dictionary)

    def return_dictnry_list(self, filename):

        list_dict1 = []

        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_dict1.append(row)
        return list_dict1

    # Create 2 item tuple (key_field, value) use to create dictionary
    def setup_keyfield(self, dictionary_list, key_field_name):
        key_value_list = []
        for dic in dictionary_list:
            # Pull all k,v pairs except the key_field
            nested_dict = {}
            for k, v in dic.items():
                if k != key_field_name:
                    nested_dict[k] = v
                    if k not in self.o_fields:
                        self.o_fields.append(k)

            key_value_list.append((dic[key_field_name], (nested_dict)))
            resultant_dict = dict(key_value_list)
            resultant_dict.update({'PRIMARY_KEY': key_field_name})

        return resultant_dict


class report_obj(object):
    # instiate object
    def __init__(self, r_dictionary, report_name=None, r_type='DEFAULT', r_excld_fields=[]):
            self.report_name = report_name
            self.r_type = r_type
            self.r_dictionary = r_dictionary
            self.r_excld_fields = r_excld_fields
            self.headers = True

    def mergedict(a, b):
        a.update(b)
        return a
######################
#  END CLASS DEFINITION
######################


xdg2 = data_grp('person_id', 'foods.csv', 'drink.csv')
print(xdg2)
# xdg1 = data_grp('person_id', 'foods.csv')
# print(xdg1)
dict2 = xdg2.dictionary
print(xdg2.str_dictionary())
print(xdg2.fields)

####################
# CSV output test
####################


def mergedict(a, b):
    a.update(b)
    return a


header_list = ['person_id', 'name', 'fav_food', 'hate_food', 'fav_drink']

with open("test_output.csv", "w") as f:
    w = csv.DictWriter(f, header_list)
    w.writeheader()
    for k, d in sorted(dict2.items()):
        if k != 'PRIMARY_KEY':  # TODO: strip this field from dictionary
            w.writerow(mergedict({header_list[0]: k}, d))

print()
