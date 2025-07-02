import csv


address_book = [
    ["name", "address", "mobile", "email"],
    ["Garvit Agarwal", "Jaipur", "7343324522", "garvit@example.com"],
    ["Nasir Ahmed", "Bhilwara", "9632442530", "nasir@example.com"],
    ["Krishna Awasthi", "Delhi", "9056432678", "krishna@example.com"]
]

with open("address_book.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print("CSV file 'address_book.csv' is created successfully.")