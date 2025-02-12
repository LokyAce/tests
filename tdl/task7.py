#🔹 Task 7: Nested Dictionary Aggregation
#🎯 Problem:
#You have a list of dictionaries where each dictionary represents a product, and each product belongs to a category. Your goal is to group the products by category and sum their prices.

#📝 Example Input:

data = [
    {"category": "Electronics", "product": "Laptop", "price": 1200},
    {"category": "Electronics", "product": "Mouse", "price": 25},
    {"category": "Furniture", "product": "Chair", "price": 150},
    {"category": "Electronics", "product": "Keyboard", "price": 80},
    {"category": "Furniture", "product": "Table", "price": 300},
]
#✅ Expected Output:
#
#{
#    "Electronics": {
#        "products": ["Laptop", "Mouse", "Keyboard"],
#        "total_price": 1305
#    },
#    "Furniture": {
#  }
#}
groupped_dict ={}
#record = (key: {"products":[]},{"price":int})

def main():
    print('Hello!\n')
    for l_dict in data:
        if not l_dict["category"] in groupped_dict:
            #creating dynamic structures
            groupped_dict[l_dict["category"]] = {}
            groupped_dict[l_dict["category"]]["products"]=[]
            groupped_dict[l_dict["category"]]["total_price"] = 0
            #adding values
            groupped_dict[l_dict["category"]]["products"].append(l_dict["product"])
            groupped_dict[l_dict["category"]]["total_price"] += l_dict["price"]
        else:
            groupped_dict[l_dict["category"]]["products"].append(l_dict["product"])
            groupped_dict[l_dict["category"]]["total_price"] += l_dict["price"]
        #print(l_dict, "\n\n")
    print("\ngroupped_dict:\n\n")    
    print(groupped_dict)
    


if __name__ == '__main__':
    main()