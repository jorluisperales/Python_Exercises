# Variable Length Arguments *args (Non keyword Arguments)

# in order to store multiple args, will add the arg with * at the begining, this will be stored as a tuple (inmutable)

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for items in args:
        print(f"You have ordered: {items}")
    print("You food will be delivered in 30 mins.")
    print("Enjoy the party.")

order_food("Salad", "Burgers", "Pizza", "Hot Dogs")

