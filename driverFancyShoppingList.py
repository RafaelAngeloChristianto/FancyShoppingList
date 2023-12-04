from fancyShoppingListRAC import ShoppingRAC

def driver():
    shopList = []
    
    while True:
        firstQuestion = int(input("How many items will you order today? "))
        if firstQuestion <= 0:
            print("Number of items must be at least 1")
            firstQuestion = input("How many items will you order today? ")
        else:
            pass
        
        secondQuestion = input("Item #1 - Enter food: ")
        thirdQuestion = int(input("Enter amount of pounds: "))
        
        
        
    return shopList

driver()