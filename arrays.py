shopping = [
    {"name": "Tomatoes", "quantity": 3},
    {"name": "Bread", "quantity": 1},
    {"name": "Eggs", "quantity": 6},
   # {"name": "Magic", "quantity": 1},
  #  {"name": "Something else", "quantity": 10},
]

productInfo = [
    {"name": "Tomatoes", "price": 0.2},
    {"name": "Bread", "price": 0.5},
    {"name": "Eggs", "price": 0.1}
]

def getPrice(name):
    for item in productInfo:
        itemName  = item["name"]
        if itemName == name:
            return item["price"]
    return 0

def bill(shopping):
    billedItems = []
    billingErrors = []

    for item in shopping:
        name = item["name"]
        price = getPrice(name)
        if price:
            quantity = item["quantity"]
            amount = quantity * price
            billedItems.append({"name": name, "quantity": quantity, "price": price, "amount": amount})
        else:
            billingErrors.append(item)

    if billedItems:
        print("")
        print("Bill")
        print(48 * "-")
        total = 0
        for item in billedItems:
            amount = item["amount"]
            total += amount
            print("%s %s x Eur %s \t Eur %s" % (item["name"].ljust(16), item["quantity"], item["price"], amount))
        print(48 * "=")
        print("%s Eur %s" % ("Total".ljust(32),total))
        print(48 * ".")

    if billingErrors:
        print("")
        print(">>>>")
        print("These items are not available:")
        print([item["name"] for item in billingErrors])


bill(shopping)
