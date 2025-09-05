import re

def parse_expense(text):
    # Extract amount (numbers)
    amount_match = re.search(r'\d+', text)
    amount = float(amount_match.group()) if amount_match else None

    # Extract category (word after 'on' or last word)
    category_match = re.search(r'on (\w+)', text)
    category = category_match.group(1) if category_match else text.split()[-1]

    return amount, category
