"""

Create a program that creates functions which are your own versions of the list methods. Do not
make use of any built-in list methods to implement them. Your program must do all the
necessary checks to make sure that all the functions work. For functions modifying the original
list, the list must no be changed, but a modified version of it must be returned.

count(list1, x): returns the number of elements with the specified value.
index(list1, x): returns the index of the first element with the specified value. If the value
does not exist, the function returns None.
append(list1, x): adds an element at the end of the list.
insert(list1, x, index): adds an element at the specified position.
remove(list1, x): removes the first element in the list with the specified value.
removeAll(list1, x): removes all the elements in the list with the specified value.
clear(list1): removes all the elements from the list.
pop(list1): removes the last element of the list and returns its value

"""


def my_count(list1, x):
    count = 0
    for i in list1:
        if i == x:
            count += 1
    return count


def my_index(list1, x):
    for i in range(len(list1)):
        if list1[i] == x:
            return i

    return None


def my_append(list1, x):
    list2 = list1 + [x]
    return list2


def my_insert(list1, x, index):
    list2 = list1[0:index+1] + [x] + list1[index:]

    return list2


def my_remove(list1, x):
    for i in range(len(list1)):
        if list1[i] == x:
            list2 = list1[0:i] + list1[i +1:]
            return list2


def my_removeAll(list1, x):
    list2 = list1
    for i in list1:
        if i == x:
            list2 = list2[0:i] + list2[i + 1:]
    return list2


def my_clear(list1):
    return []


def my_pop(list1):
    last = list1[-1]
    list1 = list1[:-2]
    return last


print(my_count([1, 2, 3], 1))
print(my_index([1, 2, 3], 2))
print(my_append([1, 2, 3], 2))
print(my_insert([1, 2, 3], 2, 1))
print(my_remove([1, 2, 3], 2))
print(my_removeAll([1, 2, 3,2,3], 2))
print(my_clear([1, 2, 3]))
print(my_pop([1, 2, 3]))
