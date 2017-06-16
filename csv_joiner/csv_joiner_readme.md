# CSV "Joiner" Readme

Idea behind this script is to allow the grouping of multiple CSV files based on a common field with unique values.
This process is analogous to a **"Join"** in SQL.
<br>
>Note: This could also be made to work with XML files instead of CSV


Data from CSV files is stored in a *nested data dictionary*
```
{'01': {'fav_drink': 'Coke',
        'fav_food': 'pizza',
        'hate_food': 'peas',
        'name': 'Alex'},
 '02': {'fav_drink': 'Redbull',
        'fav_food': 'ice cream',
        'hate_food': 'dirt',
        'name': 'Brad'},
 'PRIMARY_KEY': 'person_id'}
 ```


The script is not dependent on the order of the fields/values to function properly.

### Example Input
>foods.csv
```
person_id,fav_food,hate_food
07,chicken,garbage
01,pizza,peas
02,ice cream,dirt
03,pasta,kale
04,steak,spinach
05,chocolate,spearmint
```

>drink.csv
```
person_id,fav_drink,name
01,Coke,Alex
02,Redbull,Brad
07,Dr.Pepper,Gary
03,Milk,Chuck
04,Whine,Dale
05,Milkshake,Eric
```

### Example Output
```
person_id,name,fav_food,hate_food,fav_drink
01,Alex,pizza,peas,Coke
02,Brad,ice cream,dirt,Redbull
03,Chuck,pasta,kale,Milk
04,Dale,steak,spinach,Whine
05,Eric,chocolate,spearmint,Milkshake
07,Gary,chicken,garbage,Dr.Pepper
```
---
#### Class Layout

3 major classes<br>
--`data_grp` <br>
---->`data_object`(s)<br>
---->`report_obj`

### data_grp

Top level class.
Result of the merging of 1 or more `data_object`s

Parameter      | Type
----------------|------
key_field_name | positional
core_filename | positional
suppl_filename=None | key word
excluded_fields=[] | key word

| Attribute |
|-----------|
|key_field_name|
|core_filename|
|suppl_filename|
|data_grp_core|
|num_data_grps |
|data_grp_suppl |
|dictionary |
|fields |
|excluded_fields |
|report_obj |



###### data_object
Virtual representation of a CSV file.
Parses and processes CSV file.

###### report obj*ect*

Contains details and instructions for producing the report.
Creates report.
