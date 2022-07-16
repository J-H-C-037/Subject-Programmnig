"""Lesson 5 Simple Data structures

A single variable stores several data

Arrays: several data, same type.

Lists, tuples

records: some data, different type

Dictionaries, objects

Lists

Finite (depends on the memory and the OS), heterogeneous (data of different types), mutable (elements can be changed, added, deleted or modified), indexed by position, collection of elements
"""

list1 = [1, “hello”, 3.4, True, 1+2j]

"""

String

Finite, homogeneous, immutable and indexed by position, collection of characters


"""
import sys

sys.maxsize

"""
Ways to create a lists

Using literals to specify the elements

"""

list1 = [1, “hello”, 3.4, True, 1+2j]


#Using variables

a = 10
b = 20
c = 40

lists2 = [a,b,c]



#Using the +/* operator

list1 += [12]

list4 = list1 * 2 + list2

#Using loops and +

list5 = []

for i in range(0,100,2):
	list5 += [i]


for i in range(1000):
	list5 += [“hello”]

#Using List comprehension




"""

Operators and functions with lists

+ * []

in, not in 

print()
len()
del(list[position)

del(list) -> delete the list 


"""


list1[1,2,3,4,5]



list1[0:4] = [2] #[2,5]

list1[0:1] = [2,3,4] #[2,3,4,5]
#: all the values
list1[:] = [] #[]

3 in list1 #False

len(list1) #0

list1 = [1,2,3,4,5]

del(list1[0:2])

"""

List methods

list.method(...)

.append(element)

.insert(index,element) 

.extend(list2) -> list += list2

.append(list2) -> list2 as a single element

.index(element)

.index(element, start, end) end not included, it is optional 

start = start searching from this element 

.count(element)

.clean -> remove the elements 
.remove(element)

.pop(indiex) -> remove and return (the last element by default)

.reverse

.sort() ascending


Methods are changing the list

"""

list1.index(1) #0

list1[1, 5, 5.0, 5]

list1.sort()

list1  # [1,5,5.0,5]

#descendingly sorted

list1.sort() #We can't put list1.sort(). reverse() becaues sort() is not returning a list
list1.reverse()

