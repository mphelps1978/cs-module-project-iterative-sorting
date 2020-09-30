# Linear Time

animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Cat']

# Print all animals
# How much longer will this take to run as the size of the dataset increases?
# This is Linear Time, or O(n) It will increase or decrease dependant on the size of the dataset


def print_animals():
    for a in animals:  # O(n) over the number of animals
        print(a)


def print_animal(i):  # O(1) over the number of animals
    print(animals[i])


def print_animal2(i):  # O(1) over the number of animals
    for c in animals[i]:  # O(n) over the length of the string
        print(c)


def find_dupes():
    for i0 in range(len(animals)):   # n (over the number of animals)
        for i1 in range(len(animals)):  # n (over the number of animals)
            if i0 == i1:                 # 1 (over the number of animals)
                continue                   # 1 (over the number of animals)
            if animals[i0] == animals[i1]:   # 1 (over the number of animals)
                print(f"Duplicate: {animals[i0]}")   # 1 (over the number of animals)

# 1 Sequential block of uninterrupted processes, add the operations
# 1 + 1 + 1 + 1 = 4, drop the constants, we get O(1)
# Multiply over EACH loop (O(n * 1)) = O(n)
# TWO loops that are n over the size of the dataset (O(n*n) or O(n^2)


def print_animals_3():
    for a in animals:  # O(n)
        print(a)
    for a in animals:  # O(n)
        print(a)

# Because they are isolated, each loop is separate, so we add
# So O(n + n) = (O(2n)) - Drop the constants = O(n)


for i in range(1000000000000):  # O(1000000000000) = O(1)
    print(animals[0])  # O(1)

# Drop the constants, you get O(1 + 1) = O(1)


###############################

# Binary Search

animals.sort()  # O(n log n)


def binary_search():  # O(log n)
    pass


def find_animal(a):   # This is O(n) worst case - Linear Search
    for animal in animals:
        if animal == a:
            return True
        return False


####################################
# Insertion Sort
#          _ <-- defined as already sorted
my_list = [8, 2, 5, 4, 1, 3]


def insertion_sort_not_in_place(unsorted_list):   # Not in place (New storage)
    sorted_list = []

    for n in unsorted_list:
        if len(sorted_list) == 0:
            sorted_list.append(n)
            continue

        index = 0
        for i in range(len(sorted_list) - 1, -1, -1):
            if sorted_list[i] < n:
                index = i + 1
                break

            sorted_list.insert(index, n)

    return sorted_list


def insertion_sort(a):   # In place (Same storage)
    for i in range(1, len(a)):
        val = a[i]
        j = 1

        while j > 0 and val < a[j - 1]:
            a[j], a[j-1] = a[j-1], a[j]  # swap
            j -= 1
