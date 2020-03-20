def make_pizza(size,*toppings):
    print(str(size)+" size pizza we need")
    for topping in toppings:
        print("- "+topping)