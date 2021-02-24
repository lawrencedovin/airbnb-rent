from counties import cities
import os

sorted_cities = sorted(city.lower() for city in cities)

def find_kaiser_town(sorted_cities):
    answer = int(input('Alphabetical order type 1 check by town type 2 > '))

    if answer == 1:
        for index, city in enumerate(sorted_cities):
            print(f'{index + 1}. {city.title()}')
    if answer == 2:
        check_city = input('What city do you want to check if it exists in the Kaiser Area > ')
        print(f'{check_city.title()} is in Kaiser Area') if check_city.lower() in sorted_cities else print(f'{check_city.title()} is NOT in Kaiser Area')
    
    try_again = input('Type y to retry the program or n to exit > ').lower()

    if(try_again == 'y'):
        os.system('clear') # Linux - OSX
        os.system('cls') # Windows
        find_kaiser_town(sorted_cities)
    else:
        exit()

find_kaiser_town(sorted_cities)