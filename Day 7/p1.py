import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "test@example.com"
print(re.match(email_pattern, email))

mobile_pattern = r'^\d{10}$'
mobile = "9876543210"
print(re.match(mobile_pattern, mobile))

alphanumeric_pattern = r'^[a-zA-Z0-9]+$'
text = "abc123XYZ"
print(re.match(alphanumeric_pattern, text))

text_with_numbers = "Order 123 shipped on 2023-01-01"
numbers = re.findall(r'\d+', text_with_numbers)
print(numbers)