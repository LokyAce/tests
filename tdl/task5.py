#TASK 5 🎯# Find the Tuple with the Maximum Value
#You have a list of tuples containing names and scores. Find the tuple with the highest score.

#📝 Example Input:
data = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
#✅ Expected Output:
#("Bob", 92)

def main():
    max_score = ('', 0) 
    for data_value in data:        
        if max_score[1] < data_value[1]:
            max_score = data_value
    print(max_score)

if __name__ == '__main__':
  main()