import random

def dogs(breed, size):
    print(f" A {breed} has the following size {size}.")
    if (size > 20) and (size < 50):
        print("This is a small size dog")
    elif (size >= 50) and (size <=90):
        print("This is a medium size dog")
    elif (size > 100):
        print("This is a large size dog")

def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
#    print(args)
    for items in args:
        print(f"You have ordered: {items}")
    print("You food will be delivered in 30 mins.")
    print("Enjoy the party.")

def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random minute spec on a random activity    
    '''
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0,60)
#   print(min)
    choice = random.choice(list(kwargs.keys()))
#   print(choice)
    print(f"You have to spend {min} for {kwargs[choice]}")