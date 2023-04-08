#function
def compcomtar(name, sales):
    if sales > 100000:
        commission = 0.10 * sales
    else:
        commission = 0.05 * sales

    target = 1.05 * sales

    return commission, target

#input
name = input("Please enter the salesperson's last name: ")
sales = float(input("Please enter the sales: "))

#call funtion
commission, target = compcomtar(name, sales)

#output
print("Salesperson's last name: ", name)
print("Commission: ", commission)
print("Next year's target: ", target)