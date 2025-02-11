#TASK 1 🎯#
# #You have a list of tuples where each tuple contains a key-value pair. Convert it into a dictionary.
#Input:
# data = [("name", "Alice"), ("age", 25), ("city", "New York")]
#Expected Output:
#{"name": "Alice", "age": 25, "city": "New York"}

data = [("name", "Alice"), ("age", 25), ("city", "New York")]
   
def main():
   dictionary = {}
   dictionary.update(data)
   print (dictionary) 


if __name__ == '__main__':
  main()