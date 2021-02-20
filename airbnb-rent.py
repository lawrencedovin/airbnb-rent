from counties import cities

sorted_cities = sorted(city.lower() for city in cities)

answer = int(input('Alphabetical order type 1 check by town type 2 > '))

if answer == 1:
    for index, city in enumerate(sorted_cities):
        print(f'{index + 1}. {city.title()}')
if answer == 2:
    check_city = input('What city do you want to check if it exists > ')
    print(f'{check_city.title()} is in Kaiser Area') if check_city.lower() in sorted_cities else print(f'{check_city.title()} is NOT in Kaiser Area')