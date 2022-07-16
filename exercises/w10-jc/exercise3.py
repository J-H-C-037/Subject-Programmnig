"""Create a function that receives as parameters a list and an element and returns a tuple with the
positions of the element in the list, or the empty tuple if the element is not in the list. Invoking
this function, create another one that receives two lists and an element and returns if any of the
appearances of the element is at the same position in both lists.
"""


def in_the_list(element, list):
    if element in list:
        return list.index(element),
    else:
        return tuple()


def in_the_same_position(element,list2, list1):
    info1 = in_the_list(element,list2)
    info2 = in_the_list(element, list1)

    if len(info1) == len(info2) == 0:
        return False
    if info1 == info2:
        return True
    else:
        return False

