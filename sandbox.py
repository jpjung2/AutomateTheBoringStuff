import copy

def print_lists():
    print("List 1:", list1)
    print("List 2:", list2)
    print()

def modify_lists():
    list2[len(list2) - 1] = 'bananas'

def foo(arr1, arr2):
    arr1.append('foo')
    temp = ['cats']
    arr2.clear()
    for thing in temp:
        arr2.append(thing)


list1 = ['apples', 'oranges']
list2 = ['bananas', list1]

print_lists()

list3 = copy.deepcopy(list2)

print(list3)
print()

list1[0] = 'watermelon'

print(list3)
print_lists()
