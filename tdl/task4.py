#TASK 4 🎯#Group Dictionary Data by a Common Key
#Problem:
#You have a list of dictionaries and need to group values by a common key.
#Example Input:
from os import name


data = [
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "Charlie", "department": "IT"},
    {"name": "David", "department": "HR"},
]
# Expected Output:
#{
#    "HR": ["Alice", "David"],
#    "IT": ["Bob", "Charlie"]
#}

sorted_dict = {}

def main():
    for dict in data:
        if dict["department"] not in sorted_dict:
            sorted_dict[dict["department"]] = []
            sorted_dict[dict["department"]].append(dict["name"])
        else:
            sorted_dict[dict["department"]].append(dict["name"])
    print(sorted_dict)

if __name__ == '__main__':
    main()