print("Welcome to the pizza shop situated in Cork Airport. It's a pleasure to have you :) ")


def first_name():
    while True:
        global fname
        fname = input("First off, may I have your first name please: ").capitalize()
        # Checking if the first name takes too many characters
        if len(fname) > 30 or len(fname) == 0:
            print("Please enter a valid name")
            continue
        choice1 = input(f"\nIs {fname} the correct name? If it is not press N but if it is press any other key: ")
        if choice1.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "Great!"


print(first_name())


def surname():
    while True:
        global sname
        sname = input(f"\nNice to meet you {fname} and what is your surname: ").capitalize()
        # Checking if the surname takes too many characters or no characters
        if len(sname) > 30 or len(sname) == 0:
            print("The surname you have entered is invalid please try again.")
            continue
        choice2 = input(f"\nIs {sname} the correct name? If it is not press N but if it is press any other key: ")
        if choice2.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "Great!"


print(surname())


def phone_number():
    while True:
        global p_number
        p_number = input("\nCan you enter your phone number please: ")
        # Making sure the phone number is the required length
        if len(p_number) != 9 or len(p_number) == 0:
            print(f"Sorry your number is either too long or too short.\n Try again.")
            print("Remember not to use 0 at the start of your number.")
            continue
        # Checking if they put in an input
        choice3 = input(
            f"Is ({p_number[0:2]}) {p_number[2:-1]} the correct phone number? "
            f"If it is not press N but if it is press any other key: ")
        if choice3.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "Perfect!"


print(phone_number())


def get_email(): 
    while True:
        global email
        email = input("\nFinally what is your email: ")
        # Check for the amounts of times @ is in the email
        # This was adapted from w3schools
        # Link here:
        # https://www.w3schools.com/python/ref_list_count.asp
        validation = email.count("@")
        if validation != 1 or len(email) == 0:
            print("Invalid email :( \n Make sure to add an  @ to the email")
            continue
        choice4 = input(f"Is {email} the correct email? If not press N but if it is press any other key: ")
        if choice4.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "\nWe are almost there."


print(get_email())

print(
    f"\nGreat! Nice to meet you {fname} {sname}. \n Your phone no. is: +353 ({p_number[0:2]}) {p_number[2:-1]}"
    f" and email is: {email}")

print("\nTake a look at our wide selection of Pizzas")

print("_________________________________________________________________________")
print("Pizza Type           Small in €          Medium in €       Large in €    ")
print("-------------------------------------------------------------------------")
print("Margherita                10                   12               15       ")
print("Pepperoni                 12                   14               17       ")
print("Four Seasons             11.50                13.50            16.50     ")
print("_________________________________________________________________________")

pizza = []
pizza_size = []

while True:
    try:
        amount_of_pizza = int(input("\nHow many pizzas would you like: "))

        # Check if the input for the number of pizzas is less than 1
        if amount_of_pizza < 1:
            print("\n Please enter a valid number (1 or more).")
            continue
        # Loop through for the amount of times they ask
        for amount in range(amount_of_pizza):
            pizza_order = input("\n What type of pizza would you like: ").lower()

            if pizza_order not in ["margherita", "pepperoni", "four seasons"]:
                print("Please enter the correct pizza spelling.")
                continue

            order_size = input("\n What size pizza would you like: ").lower()

            if order_size not in ["small", "medium", "large"]:
                print("Please enter a valid size.")
                continue

            pizza.append(pizza_order)
            pizza_size.append(order_size)
            print("\n Order added!")

        if len(pizza_size) != amount_of_pizza:
            print("\n You did not fill in the order correctly please try again")
            pizza = []
            pizza_size = []
            continue

        print(f"\nYou have chosen these pizzas: {pizza} with these corresponding sizes: {pizza_size}")
        print("Is your order correct?")
        order_confirmation = input("\n If you want to reset your order enter 'N' or else press any key to continue: ")

        # If they enter 'n' restart the ordering of pizza
        if order_confirmation.upper() == "N":
            pizza = []
            pizza_size = []

        else:
            print("Perfect!")
            break

    except ValueError:
        print("\n Sorry, please enter a number not a word. :)")


def pizza_cost(pizza, pizza_size):
    # Define the prices for each type of pizza
    prices = {
        "margherita": {"small": 10, "medium": 12, "large": 15},
        "pepperoni": {"small": 12, "medium": 14, "large": 17},
        "four seasons": {"small": 11.50, "medium": 13.50, "large": 16.50}
    }

    pcost = 0
    # Iterate through the selected pizzas
    for i in range(len(pizza)):
        p = pizza[i]
        s = pizza_size[i]

        # Check if the pizza type and size are valid
        if p in prices and s in prices[p]:
            pcost += prices[p][s]

    return pcost


print(f"your total cost for the pizzas is: €{pizza_cost(pizza=pizza, pizza_size=pizza_size)}")

topping_order = []  # Initialize an empty list for toppings
dip_order = []  # Initialize an empty list for dips
# Ask if they want dips if yes show table if no do not show table
want_extras = True
while want_extras:
    want_extras = False
    dips_toppings_choice = input(
        "\n Would you like dips or toppings on your pizza. If you don't enter N if you do press any key: ")
    if dips_toppings_choice.upper() == "N":
        print("No problem")
        break
    else:
        print("Take a look at our choice of toppings and dips")
        print("\nHere are our dips and toppings:")
        print("_____________________________________")
        print("Toppings/Dips            € per pizza ")
        print("-------------------------------------")
        print("Rucola                       1.50    ")
        print("Mushrooms                     2      ")
        print("Garlic                        3      ")
        print("Spicy mayo                    3      ")
        print("_____________________________________")
        try:
            choice_toppings = int(input("\nHow many extra toppings do you want? "))
            choice_dips = int(input("How many dips do you want? "))

            for i in range(choice_toppings):
                topping = input("\n What topping would you like? ").lower()

                if topping not in ["rucola", "mushrooms", "mushroom"]:
                    print("\nInvalid topping. Please try again :C ")
                    continue

                topping_order.append(topping)
                print("\n Topping added!")

            for i in range(choice_dips):
                dip = input("\n What type of dip would you like? ").lower()

                if dip not in ["garlic", "spicy mayo"]:
                    print("\nInvalid dip. Please try again :C ")
                    continue

                dip_order.append(dip)
                print("\n Dip added!")

            # Check if they have entered the right amount of topping if they have not reset topping
            if len(topping_order) != choice_toppings or len(dip_order) != choice_dips:
                print("\n You have made an error in your inputs, so we will restart")
                want_extras = True

            print(f"The toppings you have ordered is {topping_order} and dips you have ordered is {dip_order}")
            restart_extras = str(input(
                "\n Do you want to restart your order on toppings and dip.\nIf you want to enter, "
                "please enter Y or else enter any key: "))

            if restart_extras == "Y":
                print("\n Ok lets take a step back")
                topping_order = []
                dip_order = []
                want_extras = True

        except ValueError:
            print("\n Please use a number for the amount of toppings or dips you want.")


def dips_toppings_cost(dip, topping):
    topping_prices = {"rucola": 1.50, "mushrooms": 2, "mushroom": 2}
    dip_prices = {"garlic": 3, "spicy mayo": 3}

    tcost = 0
    # Iterate through the selected pizzas
    for topping in topping_order:
        if topping in topping_prices:
            tcost += topping_prices[topping]

    for dip in dip_order:
        if dip in dip_prices:
            tcost += dip_prices[dip]

    return tcost


print(
    f"Your total cost for dips and toppings is: €{dips_toppings_cost(dip=dip_order, topping=topping_order)}")

drinks = {}
want_drinks = True
while want_drinks:
    want_drinks = False
    # Ask if they want drinks if yes give em drinks if no do not show table
    add_drinks = str(input("\n Would you like any drinks. Enter N if you don't or press any key if you do: "))

    if add_drinks.upper() == "N":
        print("\n That's completely fine.")

    else:
        print("\n Here is our collection of drinks")

        print("_______________________________________________________________")
        print("Drink        Small in €         Medium in €        Large in €  ")
        print("---------------------------------------------------------------")
        print("Coke             2                   2.50              3.50    ")
        print("Pepsi            2                   2.50              3.50    ")
        print("Fanta            2                   2.50              3.50    ")
        print("7up              2                   2.50              3.50    ")
        print("Water            1                    2                2.50    ")
        print("_______________________________________________________________")

        try:
            amount_drinks = int(input("\n How many drinks do you want? "))

            if amount_drinks < 1:
                print("\n Please enter a valid amount of drinks.")

            if amount_drinks < 1:
                print("\n Please enter a valid amount of drinks.")

            for i in range(amount_drinks):
                choice_drinks = str(input("\n What drink would you like: "))
                if choice_drinks.lower() not in ["coke", "pepsi", "fanta", "7up", "water"]:
                    print("You have made an invalid choice please try again")
                else:
                    choice_size_drinks = str(input("\n What size of drink would you like: "))
                    if choice_size_drinks.lower() not in ["small", "medium", "large"]:
                        print("\n You have made an invalid choice please try again")
                    else:
                        drinks[choice_drinks] = choice_size_drinks
                        print("\n Drink added!")

            print(f"The drinks you have chosen are {drinks}.")
            restart_drinks = str(input("Do you want to restart your drink selection. Yes or No: ")).lower()
            if restart_drinks == "yes":
                drinks = {}
                want_drinks = True
            elif restart_drinks == "no":
                print("Ok lets continue!")

        except ValueError:
            print("\n Sorry you need to use a number to indicate how many drinks you want.")
            want_drinks = True


def drinks_sum(drinks_dict):
    # Define the prices for each type of drink
    prices_drinks = {
        "coke": {"small": 2, "medium": 2.50, "large": 3.50},
        "pepsi": {"small": 2, "medium": 2, "large": 3.50},
        "fanta": {"small": 2, "medium": 2.50, "large": 3.50},
        "7up": {"small": 2, "medium": 2.50, "large": 3.50},
        "water": {"small": 1, "medium": 2, "large": 2.50}
    }

    dcost = 0
    # Iterate through the selected drinks and sizes in the dictionary
    for drink, size in drinks_dict.items():
        if drink in prices_drinks and size in prices_drinks[drink]:
            dcost += prices_drinks[drink][size]

    return dcost


print(f"\n Your total cost for drinks is: €{drinks_sum(drinks_dict=drinks)}")

# Add a delivery service and the further out they are the higher the cost
while True:
    delivery_cost = 0
    try:
        delivery_in_cork = str(input("\n Do you live inside Cork yes or no: "))
        if delivery_in_cork.lower() == "yes":
            towns_in_cork = ()
            delivery = int(input("\n Great how many minutes away from the airport are you: "))
            if delivery <= 10:
                delivery_cost = 0
                break
            elif 10 < delivery <= 20:
                delivery_cost = 10
                break
            elif 20 < delivery <= 30:
                delivery_cost = 15
                break
            elif 30 < delivery < 60:
                delivery_cost = 30
                break
            else:
                delivery_cost = 45
                break

        elif delivery_in_cork.lower() == "no":
            delivery_cost = 50
            break

    except ValueError:
        print("Please enter a number. :)")
        continue

print(f"\n The cost of your delivery is: €{delivery_cost}")

cost_before_vat = (delivery_cost + drinks_sum(drinks_dict=drinks) + dips_toppings_cost(dip=dip_order,
                                                                                       topping=topping_order) + pizza_cost(
    pizza=pizza, pizza_size=pizza_size))
if cost_before_vat >= 35:
    discount = cost_before_vat / 10
    cost_before_vat -= discount
    print(f"\n Due to your price being high you have received a discount of {discount}.")
    print(f"\n Now your total price before vat is {cost_before_vat}")
elif cost_before_vat >= 50:
    discount = cost_before_vat / 15
    cost_before_vat -= discount
    print(f"\n Due to your price being high you have received a discount of €{discount}.")
    print(f"\n Now your total price before vat is €{cost_before_vat}")

cost_with_vat = cost_before_vat * 1.23
print(f"\n Your cost with vat is €{round(cost_with_vat, 2)}")
print("Thanks for ordering at our pizza shop. We hope you enjoy your food :D")

# Which is a better mechanic press any key or force them to press Y to continue and handle errors if they don't
# Currency converter from euro to pounds or dollars
# Create a GB settings at the start and if they choose gb then change phone number and also currency
