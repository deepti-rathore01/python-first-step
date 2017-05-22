"""
@file : dict_update_add_delete.py
@brief : the program to add, remove and update elements in dictionary
"""
a = {'name': 'deepti','company': 'vvdn', 'location': 'chennai'}
print a
#update
a['location']= "banglore";
print"after update\n", a

#add
a['deparment']  = "automation";
print" add this to dict\n", a

#delete
del a['name'] # remove entry with key 'Name'
print" that the name key is deleted\n", a
a.clear()    # remove all entries in dict
print" all entries is deleted\n", a
#del a       # delete entire dictionary_
#print" deleted entire dictionary\n", a
