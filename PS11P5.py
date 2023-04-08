#function
def comptotaltax(qty, unitprice):
    global total, tax
    total = quantity * unitprice
    tax = 0.07 * total

#input
quantity = int(input("Please enter the quantity: "))
unitprice = float(input("Please enter the unit price: "))

#call function
comptotaltax(quantity, unitprice)

#output
print("Total: ", total)
print("Tax: ", tax)