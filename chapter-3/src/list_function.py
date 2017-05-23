"""
@file :  list_function
@brief: Use list functions append(), count(), extend(), index(), insert(), pop(), remove(), reverse() and sort()
@authore : deepti
@date: 19-5-17
"""
# append function
alist = ['name','age','gender']
alist.append('idnumber')
print"update list:",alist

#count function
alist = [11 ,22,33,11,11,22,10 ,2]
print "count for 11", alist.count(11)
print "count for 22",alist.count(22)

#extend function
alist =['ranu','shanu','monu','richa','rohit']
blist = ['monku''roho']
alist.extend(blist)
print "Extended List : ", alist 


#index function
alist =[123,22,33,14]
print "Index for 123 : ", alist.index( 123 )
print "Index for 33 : ", alist.index( 33)


#insert function
alist = [123, 'xyz', 'zara', 'abc']

alist.insert( 3, 2009)

print "Final List : ", alist

# pop function
alist = [' abc','adb','ajk','ajm']
print "list", alist.pop()
print"list", alist.pop(1)


#remove function

alist = [ 'ranu','shanu','monu']
alist.remove('shanu');
print "List : ", alist


#reverse function

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.reverse();
print "List : ", aList


#sort function

alist = [ 'ranu','shanu','monu']
alist.sort();
print "List : ", alist


