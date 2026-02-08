balance= 3000
def buy_items(item, price):
    global balance
    if price <= balance:
        balance -= price
        return f"Purchased {item} for ${price}. Remaining balance: ${balance}."
    else:
        return "Insufficient funds to make the purchase."
    
buy_items("Headphones", 150)

print(balance)