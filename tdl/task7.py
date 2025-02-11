#🔹 Task 1: Nested Dictionary Aggregation
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
