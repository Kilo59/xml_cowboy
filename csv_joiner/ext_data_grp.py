# extensible data group
# allow multiple csv files to be "joined" together using a common field with unique values (like a SQL join)
import csv
import collections
import pprint
import copy
import os
# import itertools
# import sys


#################
# Class DEFINITION
#################


# combined_data_grp  holds 1 or more data_groups and "joins" them on a common field
class data_grp(object):
    # instiate object
    def __init__(self, key_field_name, core_filename, suppl_filename=None, report_fields=['all']):
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
            if report_fields[0] == 'all':
                self.report_fields = self.fields  # use all fields
            elif len(report_fields) > 1:  # use specified fields
                self.report_fields = report_fields
            self.report_obj = report_obj(self.get_dictionary(), self.report_fields)

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
            if self.key_field_name == data_grp_suppl.key_field_name:
                melded_dictionary = self.deep_update(core_dict, suppl_dict)
                self.num_data_grps = self.num_data_grps + 1
                return melded_dictionary
            else:
                print('*' * 10 + '\nERROR: KEYS do not match\n' + '*' * 10)
                return core_dict
        else:
            return core_dict

    def get_dictionary(self):
        returned_dict = copy.deepcopy(self.dictionary)
        # iterate through nested dictionary
        # remove fields not used in report
        if self.report_fields[0] != 'all':
            for record_d in returned_dict.values():
                # print('0', record_d)
                for field in list(record_d.keys()):
                    # print('1', field)
                    if field not in self.report_fields:
                        record_d.pop(field, 'POP')
        return returned_dict

    def str_dictionary(self):
        return pprint.pformat(self.get_dictionary)

    def make_report(self, report_name='report.csv'):
        self.report_obj.write_report(output_name=report_name)
        return


class data_object(object):
    # instiate object
    def __init__(self, key_field_name, filename):
        self.key_field_name = key_field_name
        self.filename = filename
        self.o_fields = []
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
                nested_dict[k] = v
                if k not in self.o_fields:
                    self.o_fields.append(k)
            key_value_list.append((dic[key_field_name], (nested_dict)))
        # End dictionary loop
        resultant_dict = dict(key_value_list)
        # pprint.pprint(resultant_dict) #  TEST STATEMENT
        return resultant_dict


class report_obj(object):
    # instiate object
    def __init__(self, r_dictionary, r_fields, report_name=None, r_type='DEFAULT', r_excld_fields=[]):
            self.report_name = report_name
            self.r_type = r_type
            self.r_dictionary = r_dictionary
            self.r_fields = r_fields
            self.r_excld_fields = r_excld_fields
            self.headers = True

    def mergedict(self, a, b):
        a.update(b)
        return a

    def write_report(self, output_name='report.csv'):
        with open(output_name, "w") as f:
            w = csv.DictWriter(f, self.r_fields, lineterminator='\n')
            w.writeheader()
            # sort by primary_key, write each record as a row
            for pk, record_d in sorted(self.r_dictionary.items()):
                w.writerow(record_d)
        return None
######################
#  END CLASS DEFINITION
######################


# TODO: allow for fields to be excluded from report
# TODO: pass report fields in make_report() function not during data_grp() creation
os.chdir('C:\\Users\\ggore\\Dropbox\\GitHub\\xml_cowboy\\csv_joiner')  # REMOVE BEFORE PULL
print(os.getcwd())
####################
# CSV output test
####################
report_fields2 = ['name', 'fav_food', 'hate_food']
dg2 = data_grp('person_id', 'foods.csv', 'drink.csv', report_fields=report_fields2)
print(dg2)
dg2.make_report(report_name='min_report.csv')
print('*' * 40)
report_fields3 = ['person_id', 'fav_food', 'hate_food', 'fav_drink', 'name']
dg3 = data_grp('person_id', 'foods.csv', 'drink.csv', report_fields=report_fields3)
print(dg2)
dg3.make_report(report_name='name_last.csv')
