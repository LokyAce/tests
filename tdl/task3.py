#TASK 3 🎯# Extract Unique Values from List of Dictionaries
#You have a list of dictionaries, and you need to find all unique values for a specific key.
#Example Input:
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 35}
]
key = "name"
#Expected Output:
#{"Alice", "Bob"}  # A set of unique names

def main():
#Solution: put everything in a SET        
    data_set = set()
    for dict in data:
        data_set.add(dict["name"])
    print(sorted(data_set))

if __name__ == '__main__':
  main()