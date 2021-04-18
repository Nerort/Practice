quantity_of_numbers = int(input('what will be the last number?')) + 1
for number in range(1, quantity_of_numbers):
    if number % 3 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'   
    print(number)
    

    
