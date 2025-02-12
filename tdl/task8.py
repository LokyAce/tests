import operator
#Find the Most Frequent Elements in a List of Tuples
#🎯 Problem:
#You have a list of tuples representing items and their counts. Find the top 2 most frequent items.
#📝 Example Input:

data = [("apple", 5), ("banana", 3), ("orange", 7), ("apple", 2), ("banana", 6)]

#✅ Expected Output:
#[("banana", 9), ("apple", 7)]  # Sorted by frequency in descending order

tuples_list = []
tuple_dict = {}

def main():
    print('\n\n\nHello!\n\n\n')
    for tuple in data:
        if tuple[0] not in tuple_dict:
            tuple_dict.update({tuple[0]:tuple[1]})
        else:
            tuple_dict[tuple[0]] += tuple[1]

    sorted_tuple_dict = sorted(tuple_dict.items(), key=lambda item: (item[1], item[0]))
    print (sorted_tuple_dict[-1])
    print (sorted_tuple_dict[-2])
    print ('\n\n\n', sorted_tuple_dict)


if __name__ == '__main__':
    main()