from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
# MenuItem = MenuItem()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
is_on = True

while is_on:
    options = Menu.get_items()    
    choice = input('What would youl like? (espresso / latte / cappucino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(choice)
        is_enough_ingredients = CoffeeMaker.is_resource_sufficient(drink)
        is_payment_succesful = MoneyMachine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_succesful:
            CoffeeMaker.make_coffee(drink)
