"""

Define a function combine (list1, list2), which given two lists returns a list that
combines both lists, but eliminates duplicates. Example:
list1: [1, 2, 3, 4, 5, 6]
list2: [4, 5, 6, 7, 8, 9]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""


def combine_list(list1, list2):
    list3 = list1 + list2

    repeated = []
    counter = 0
    length = len(list3)
    while counter < length:
        if list3[counter] in repeated:
            del list3[counter]
            length -=1
        else:
            repeated.append(list3[counter])
            counter += 1

    return list3
