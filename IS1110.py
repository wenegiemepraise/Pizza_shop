import random

print("Welcome to the pizza shop situated in Cork Airport. It's a pleasure to have you :) ")

fname = ""
sname = ""
p_number = ""
email = ""


def get_first_name():
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


def get_surname():
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


def get_phone_number():
    while True:
        global p_number
        p_number = input("\nCan you enter your phone number please: ")
        # Making sure the phone number is the required length
        if len(p_number) != 10 and p_number != p_number.isdigit():
            print(f"Sorry please enter a 10 digit number\n Try again.")
            continue
        choice3 = input(
            f"Is +353 ({p_number[1:3]}) {p_number[3:]} the correct phone number? "
            f"If it is not press N but if it is press any other key: ")
        if choice3.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "Perfect!"


def get_email():
    while True:
        global email
        email = input("\nFinally what is your email: ")
        # Check for the amounts of times @ is in the email
        # This was adapted from w3schools
        # Link here:
        # https://www.w3schools.com/python/ref_list_count.asp
        validation = email.count("@")
        if validation != 1 or len(email) < 4:
            print("Invalid email :( \n Make sure to add an  @ to the email")
            continue
        choice4 = input(f"Is {email} the correct email? If not press N but if it is press any other key: ")
        if choice4.upper() == "N":
            print("\n Ok lets take a step back")
            continue
        else:
            return "\nWe are almost there."


def pizza_cost(def_pizza, def_pizza_size):
    # Define the prices for each type of pizza
    prices = {
        "margherita": {"small": 10, "medium": 12, "large": 15},
        "pepperoni": {"small": 12, "medium": 14, "large": 17},
        "four seasons": {"small": 11.50, "medium": 13.50, "large": 16.50}
    }

    pcost = 0
    # Iterate through the selected pizzas
    for j in range(len(def_pizza)):
        selected_pizza = def_pizza[j]
        selected_pizza_size = def_pizza_size[j]

        pcost += prices[selected_pizza][selected_pizza_size]

    return pcost


def dips_toppings_cost(def_dip, def_topping):
    topping_prices = {"rucola": 1.50, "mushrooms": 2, "mushroom": 2}
    dip_prices = {"garlic": 3, "spicy mayo": 3}

    tcost = 0
    # Iterate through the selected pizzas
    for def_topping in topping_order:
        tcost += topping_prices[def_topping]

    for def_dip in dip_order:
        tcost += dip_prices[def_dip]

    return tcost


def drinks_sum(selected_drinks, selected_drink_sizes):
    # Define the prices for each type of drink
    prices_drinks = {
        "coke": {"small": 2, "medium": 2.50, "large": 3.50},
        "pepsi": {"small": 2, "medium": 2, "large": 3.50},
        "fanta": {"small": 2, "medium": 2.50, "large": 3.50},
        "7up": {"small": 2, "medium": 2.50, "large": 3.50},
        "water": {"small": 1, "medium": 2, "large": 2.50}
    }

    dcost = 0
    # Iterate through the indices of the lists
    for k in range(len(selected_drinks)):
        def_drinks = selected_drinks[k]
        def_drink_sizes = selected_drink_sizes[k]
        dcost += prices_drinks[def_drinks][def_drink_sizes]

    return dcost


def generate_receipt_number():
    # Generate a unique receipt number using a random number
    random_number = random.randint(1000, 9999)
    receipt_number = f"- {random_number}"
    return receipt_number


print(get_first_name())
print(get_surname())
print(get_phone_number())
print(get_email())

print(
    f"\nGreat! Nice to meet you {fname} {sname}. \n Your phone no. is: +353 ({p_number[1:3]}) {p_number[3:]}"
    f" and your email is {email}")

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
            print("Lets restart your order!")

        else:
            print("Perfect!")
            break

    except ValueError:
        print("\n Sorry, please enter a number not a word. :)")


print(f"Your total cost for the pizzas is: €{pizza_cost(def_pizza=pizza, def_pizza_size=pizza_size)}")

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
        print("Toppings                 € per pizza ")
        print("-------------------------------------")
        print("Rucola                       1.50    ")
        print("Mushrooms                     2      ")
        print("_____________________________________")


        print("_____________________________________")
        print("Dips                      € per pizza")
        print("-------------------------------------")
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
                topping_order = []
                dip_order = []
                want_extras = True

            print(f"The toppings you have ordered is {topping_order} and dips you have ordered is {dip_order}")
            restart_extras = str(input(
                "\n Do you want to restart your order on toppings and dip.\nIf you do "
                "please enter Y or else enter any key to continue: "))

            if restart_extras == "Y":
                print("\n Ok lets take a step back")
                topping_order = []
                dip_order = []
                want_extras = True

        except ValueError:
            print("\n Please use a number for the amount of toppings or dips you want.")
            want_extras = True


print(
    f"Your total cost for dips and toppings is: €{dips_toppings_cost(def_dip=dip_order, def_topping=topping_order)}")

drinks = []
drink_sizes = []
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
                want_drinks = True
                continue

            for i in range(amount_drinks):
                choice_drinks = str(input("\n What drink would you like: ")).lower()
                if choice_drinks.lower() not in ["coke", "pepsi", "fanta", "7up", "water"]:
                    print("You have made an invalid choice please try again")
                else:
                    drinks.append(choice_drinks)
                choice_size_drinks = str(input("\n What size of drink would you like: ")).lower()
                if choice_size_drinks.lower() not in ["small", "medium", "large"]:
                    print("\n You have made an invalid choice please try again")
                else:
                    drink_sizes.append(choice_size_drinks)
                    print("\n Drink added!")

            print(f"The drinks you have chosen are {drinks} with the corresponding sizes {drink_sizes}.")
            restart_drinks = str(input("Do you want to restart your drink selection. Yes or No: ")).lower()
            if restart_drinks == "yes":
                drinks = []
                drink_sizes = []
                want_drinks = True
                print("Ok let's take a step back.")
            elif restart_drinks == "no":
                print("Ok lets continue!")
            if len(drinks) != amount_drinks or len(drink_sizes) != amount_drinks:
                print("You have seen to have made an error please try again.")
                want_drinks = True
        except ValueError:
            print("\n Sorry you need to use a number to indicate how many drinks you want.")
            want_drinks = True


print(f"\n Your total cost for drinks is: €{drinks_sum(selected_drinks=drinks, selected_drink_sizes=drink_sizes)}")

# Add a delivery service and the further out they are the higher the cost
while True:
    delivery_cost = 0
    try:
        delivery_in_cork = str(input("\n Do you live inside Cork yes or no: ")).lower()
        if delivery_in_cork.lower() == "yes":
            delivery = int(input("\n Great how many minutes away from the airport are you: "))
            if delivery <= 10:
                delivery_cost = 0
                break
            elif 10 < delivery <= 20:
                delivery_cost = 5
                break
            elif 20 < delivery <= 30:
                delivery_cost = 10
                break
            elif 30 < delivery < 60:
                delivery_cost = 20
                break
            else:
                delivery_cost = 30
                break

        elif delivery_in_cork.lower() == "no":
            delivery_cost = 40
            break

    except ValueError:
        print("Please enter a number. :)")
        continue

print(f"\n The cost of your delivery is: €{delivery_cost}")
end_cost = (
        delivery_cost + drinks_sum(selected_drinks=drinks, selected_drink_sizes=drink_sizes) + dips_toppings_cost(
            def_dip=dip_order,
            def_topping=topping_order) + pizza_cost(
            def_pizza=pizza, def_pizza_size=pizza_size))
discount = 0
if end_cost >= 35:
    discount = end_cost / 10
    end_cost -= discount
    print(f"\n Due to your price being high you have received a discount of {discount}.")
    print(f"\n Now your total price is {end_cost}")
    # If the cost is really high give additional discounts
elif end_cost >= 50:
    discount = end_cost / 15
    end_cost -= discount
    print(f"\n Due to your price being high you have received a discount of €{discount}.")
    print(f"\n Now your total price is €{end_cost}")

vat = round(end_cost * .23, 2)
print(f"\n Your vat cost is €{vat}")
amount_tip = 0
# Extra functionality asking if they want to tip
tip = str(input("Would you like to add a tip to show appreciation for our staff? Y/N: ")).upper()
if tip == "Y":
    amount_tip = input("Would you like to add a 5 or 10 euro tip? ")
    if amount_tip in ["five", "5"]:
        tip = 5
        end_cost += tip
    elif amount_tip in ["ten", "10"]:
        tip = 10
        end_cost += tip
else:
    print("That's fine maybe next time")

print(f"Your final cost is {end_cost}")


f = open("receipt.txt", "w")
f.write(f"{fname} {sname}")
f.write("\nContact Info:")
f.write(f"\nPhone number: +353 ({p_number[1:3]}) {p_number[3:]}")
f.write(f"\nEmail: {email}")
f.write(f"\nPizza cost: {pizza_cost(def_pizza=pizza, def_pizza_size=pizza_size)}")
f.write(f"\nTopping and extras cost: {dips_toppings_cost(def_dip=dip_order, def_topping=topping_order)}")
f.write(f"\nDrink cost: {drinks_sum(selected_drinks=drinks, selected_drink_sizes=drink_sizes)}")
f.write(f"\nDeliver cost: {delivery_cost}")
f.write(f"\nDiscount: {discount}")
f.write(f"\nVat: {vat}")
f.write(f"\nTip: {amount_tip}")
f.write(f"\nTotal cost: {end_cost}")
f.write(f"\nReceipt No: {generate_receipt_number()} ")
f.close()

print(f"\nThank you {fname} for ordering at our pizza shop. We hope you enjoy your food :D")
