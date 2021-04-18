import random

names = input("Give me everybody's names, seperated by a comma")
#For example: Angela, Ben, James
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + ' is going to pay today')
