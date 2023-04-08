#function
def compdiscount(quantity, price, rate):
    discountamount = quantity * price * rate
    discountedprice = quantity * price - discountamount
    return discountamount, discountedprice

#input
quantity = int(input("Please enter the quantity: "))
price = float(input("Please enter the price: "))
rate = float(input("Please enter the discount rate (in decimal): "))

# Process
discountamount, discountedprice = compdiscount(quantity, price, rate)

# Output
print("Quantity: ", quantity)
print("Price: ", price)
print("Discount amount: ", discountamount)
print("Discounted price: ", discountedprice)