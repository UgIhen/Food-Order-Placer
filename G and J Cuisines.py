morningMenu = {"1" : "Chocolate Croissant", "2" :"French Toast", "3" :"Waffles", "4" :"Chicken Salad", "5" :"Cereal", "6" :"Baked Potatoes", "7" :"Poached Eggs"}
midMenu = {"1" : "Fried Rice", "2" : "Jollof Rice", "3" : "Chicken", "4" : "Fish", "5" : "Beans Porridge", "6" : "Plantain Porridge", "7" : "Yam Porridge", "8" : "Risotto Rice", "9" : "Chinese Rice"}
eveMenu = {"1" : "Avocado Slices", "2" : "Ham and Egg", "3" : "Fruit Salad", "4" : "Potato Salad", "5" : "Boiled Corn", "6" : "Light Noodles", "7" : "Steamed Veges"}
name_of_customer = []
names = []
order = []


''' Definition of functions to assist in displaying the saved menu items''' 
def displayMorningMenu():
    for x, y in morningMenu.items():
        print(x+". "+y)



def displayAfternoonMenu():
    for x, y in midMenu.items():
        print(x+". "+y)


def displayEveningMenu():
    for x, y in eveMenu.items():
        print(x+". "+y)


def menuOption(choice):
    if choice == 1:
        displayMorningMenu()
    elif choice == 2:
        displayAfternoonMenu()
    elif choice == 3:
        displayEveningMenu()
    global cdo #cdo = Choice Display Order
    cdo = choice 
    




''' Prints out the saved menu, retrives customer name and collects information about quantity of the order the customer will place '''
def getOrder():
    name = input("Name of customer: ")

    print("="*20)
    print("1. Morning Menu")
    print("2. Afternoon Menu")
    print("3. Evening Menu \n")
    menuChoice = int(input("Select Menu(i.e 3 for evening menu): "))
    print("="*20)

    menuOption(menuChoice)
    if menuChoice > 3: 
        print("Wrong selection")
        return getOrder()
    else: 
        name_of_customer.append(name)
    orderAmount = int(input("How many items do you wish to buy: "))
    print("="*20)
    makeYourOrder(orderAmount)


    print("="*20)



''' Placing the order '''
def makeYourOrder(choice):
    for i in range(0, choice):
        foodChoice = (input("Select your choice: ")) 
        icdo = int(cdo)
        if icdo == 1:
            for x,y in morningMenu.items():
                if foodChoice in x: 
                    if y not in names:
                        names.append(y)
                        if len(names) > choice:
                            if i != choice: 
                                names.pop()
                        else: 
                            print("Order Placed")

                    else: 
                        print("Meal already selected \n Your first 4 orders will be picked")
                        makeYourOrder(choice)
                        exit()

        elif icdo == 2:
            for x,y in midMenu.items():
                if foodChoice in x:
                    if y not in names:
                        names.append(y)
                        if len(names) > choice:
                            if i != choice: 
                                names.pop()
                        else: 
                            print("Order Placed")
                    else: 
                        print("Meal already selected \n Your first 4 orders will be picked")
                        makeYourOrder(choice)
                        exit()
        elif icdo == 3:
            for x,y in eveMenu.items():
                if foodChoice in x:
                    if y not in names:
                        names.append(y)
                        if len(names) > choice:
                            if i != choice: 
                                names.pop()
                        else: 
                            print("Order Placed")

                    else: 
                        print("Meal already selected \n Your first 4 orders will be picked")
                        makeYourOrder(choice)
                        exit()
    
    print("="*20)
    print("Your order for:", names[:], "has been placed.", "\n Thank you", name_of_customer[0], "for choosing GJ Cuisines!")



getOrder()
