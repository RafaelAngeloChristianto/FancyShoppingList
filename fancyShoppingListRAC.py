class ShoppingRAC:
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__standardPrice = {
            "Dry Cured Iberian Ham" : "$177.80",
            "Wagyu Steaks" : "$450.00",
            "Matsutake Mushrooms" : "$272.00",
            "Kopi Luwak Coffee" : "$306.50",
            "Moose Cheese" : "$487.20",
            "White Truffles" : "$3600.00",
            "Blue Fin Tuna" : "$3603.00",
            "Le Bonnotte Potatoes" : "$270.81"
        }
        self.calculatedPrice = 0.0
        
    def priceListRAC(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__standardPrice == "$177.80"
        elif self.__name == "Wagyu Steaks":
            self.__standardPrice == "$450.00"
        elif self.__name == "Matsutake Mushrooms":
            self.__standardPrice == "$272.00"
        elif self.__name == "Kopi Luwak Coffee":
            self.__standardPrice == "$306.50"
        elif self.__name == "Moose Cheese":
            self.__standardPrice == "$487.20"
        elif self.__name == "White Truffles":
            self.__standardPrice == "$3600.00"
        elif self.__name == "Blue Fin Tuna":
            self.__standardPrice == "$3603.00"
        elif self.__name == "Le Bonnotte Potatoes":
            self.__standardPrice == "$270.81"
        else:
            self.__standardPrice == "$0"
            
        
    def calculated_priceRAC(self):
        calculatedPrice = self.__amount * self.__standardPrice.values()
        return calculatedPrice
    
    def __str__(self):
        return f"Here's a summary of the items purchased \
            ============================================== \
            Item: {self.__name} \
            Amount ordered: {self.__amount} \
            Price per pound: {self.__name[self.__standardPrice]} \
            Price of order: {self.calculated_priceRAC()} \
            "         