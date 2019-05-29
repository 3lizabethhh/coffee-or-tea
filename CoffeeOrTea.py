__author__ = 'Dongzheng (Elizabeth) Xu'
#  This program prompts user about desired beverage. It displays the amount of money charged and then
#  describes the customer's beverage.

# prices
SMALL = 1.50
MEDIUM = 2.50
LARGE = 3.25
VANILLA = 0.25
CHOCOLATE = 0.75
MINT = 0.50
LEMON = 0.25

cost = 0
flavour = ""

# Gets user to input name and type of beverage
name = input("Please enter customer name: ")
if " " in name or name == "":  # no spaces in name
    print("ERROR: Invalid name input.")
    exit()
bevType = input("Please enter type:").lower()

if bevType == "coffee" or bevType == "c":  # Gets input for type of beverage
    bevType = "coffee"  # Converts varied input into one defined string for displayed output
elif bevType == "t" or bevType == "tea":
    bevType = "tea"
else:  # Handle invalid input
    print("ERROR: Invalid type specified.")
    exit()  # ends program

# Gets input and adjusts beverage price depending on beverage size
size = input("Please enter size of beverage: ").lower()
if size == "s" or size == "small":
    size = "small"
    cost = SMALL
elif size == "m" or size == "medium":
    size = "medium"
    cost = MEDIUM
elif size == "l" or size == "large":
    size = "large"
    cost = LARGE
else:  # Handle invalid input
    print("ERROR: Invalid size specified.")
    exit()  # ends program

# Asks for input of coffee flavours and adjusts beverage price based on flavours added
if bevType == "coffee":
    flavour = input("Enter added flavour of vanilla or chocolate: ").lower()
    if flavour == "v" or flavour == "vanilla":
        flavour = "vanilla"
        cost = cost+VANILLA  # adds extra cost for mint
    elif flavour == "c" or flavour == "chocolate":
        flavour = "chocolate"
        cost = cost+CHOCOLATE  # adds extra cost for chocolate
    elif flavour == "" or flavour == "none":
        flavour = "no flavour"  # no extra cost
    else:  # Handle invalid input
        print(" ERROR: Invalid coffee flavour specified.")
        exit()  # ends program

# Asks for input of tea flavours and adjusts beverage price based on flavours added
if bevType == "tea":
    flavour = input("Enter added flavour of lemon or mint: ").lower()
    if flavour == "m" or flavour == "mint":
        flavour = "mint"
        cost = cost + MINT  # adds extra cost for mint
    elif flavour == "l" or flavour == "lemon":
        flavour = "lemon"
        cost = cost+LEMON  # adds extra cost for lemon
    elif flavour == "" or flavour == "none":
        flavour = "no flavour"  # no extra cost
    else:  # Handle invalid input
        print("ERROR: Invalid tea flavour specified.")
        exit()  # ends program

cost = round(cost*1.13, 2)  # adds taxes to final value and rounds it to nearest cent
print("For %s , a %s %s, with %s is $ %s." % (name, size, bevType, flavour, cost))  # display order
