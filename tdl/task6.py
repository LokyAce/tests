#TASK 6 🎯# Merge Two Dictionaries
#🎯 Problem:
#You have two dictionaries and need to merge them into one.

#📝 Example Input:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
#✅ Expected Output:
#{"a": 1, "b": 3, "c": 4}  # 'b' gets updated with new value

def main():
    dict3 = dict1 | dict2
    print(dict3)

if __name__ == '__main__':
  main()