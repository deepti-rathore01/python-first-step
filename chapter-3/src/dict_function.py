"""
@file : dict_function.py
@brief :Practice with dictionary functions functions clear(), get(), has_key(), items(), keys(), pop(),
            popitem(), update(), values()
"""
#clear()
a = { 'name': 'deepti',' dep': 'atutomation','location':'pune'}
a.clear()
print " it is empty:",a


#get()
a = {'city': 'bhopal', 'state':'m.p'}
print "Value : %s" %  a.get('city')
print "Value : %s" %  a.get('country','never')


#has_key()
a = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  a.has_key('Age')
print "Value : %s" %  a.has_key('Sex')



#items()
a ={'name':'ranu','rollno': ' 34'}
print"Value : %s" %  a.items()

#key()

a = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  a.keys()

#pop()

language = ['Python', 'Java', 'C++', 'French', 'C']
return_value = language.pop(3)
print('Return Value: ', return_value)
print('Updated List: ', language)



#values()

a = {'Name': 'Zara', 'Age': 7}

print "Value : %s" %  a.values()

#pop item

a ={ 'one': 1,'two':2}
print "values of popitem",a.popitem()
