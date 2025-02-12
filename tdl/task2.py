#TASK 2 🎯#
# Convert Dictionary to List of Tuples
# You have a dictionary and need to convert it into a list of key-value tuples.
# Example Input:
# data = {"name": "Alice", "age": 25, "city": "New York"}
#Expected Output:
# data = [("name", "Alice"), ("age", 25), ("city", "New York")]

data = {"name": "Alice", "age": 25, "city": "New York"}
tuples_list = []

def main():
    tuples_list = data.items()
    print(tuples_list)

if __name__ == '__main__':
  main()