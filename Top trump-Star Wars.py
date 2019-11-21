# Star Wars API
# Home Page: https://swapi.co/api/
# 'Star Wars' dictionary has 6 keys: people, planets, films, species, vehicles, startships
# Choose 'people': https://swapi.co/api/people/
# 'People' is a dictionary has 4 keys: count, next, previous, results
# The value of 'results' is a list, which has 87 dictionaries.
# Each dictionary represents a person
# There are 16 keys in each dictionary: name, height, mass, hair_color, skin_color, eye_color,
# birth_year, gender, homeworld, films, species, vehicles,starships,created, edited, url
# Only 'height' and 'mass' can be compared

import requests
import random

# Get the information from API
def get_people():

    people_name = []
    people_height = []
    people_mass = []

    # there are 9 websites
    for page in range(1,10):
        url = 'https://swapi.co/api/people/?page=' + str(page)
        response = requests.get(url)
        people = response.json()
        people_results = people['results']# extract the 'results' key

        # create 3 lists - 'name', 'height' and 'mass'
        for person in people_results:
            people_name.append(person['name'])
            people_height.append(person['height'])
            people_mass.append(person['mass'])

    return [people_name, people_height, people_mass]

# Run get_people() function
people_three_stat = get_people()
people_name = people_three_stat[0]
people_height = people_three_stat[1]
people_mass = people_three_stat[2]
people_mass[15] = 1358 # there is a mistake in dictionary, the original value is '1,358'

# Get random person
def get_random_person():

    random_number = random.randint(0,86)

    return{
        'name': people_name[random_number],
        'height': people_height[random_number],
        'mass': people_mass[random_number]
    }

# Input the stat, including the solution when input wrong words
def input_stat():

    stat_choice = input('Which stat do you want to use? (height & mass)  ')

    if stat_choice != 'height' and stat_choice != 'mass':#only input 'height' or 'mass' available
        print("Please input 'height' or 'mass'")
        stat_choice = input_stat()

    return stat_choice

# Ask the user whether to play again, including the solution when input the wrong word
def try_again():

    i = input('Would you like to try again? (y/n) ')

    if i == 'y':
        run()
    elif i == 'n':
        print('Thank you!')
    else:
        print('Please input y or n')
        try_again()

    return

# Play the game
def run():

    random_people = get_random_person()

    print('You were given {}'.format(random_people['name']))
    stat_choice = input_stat()

    opponent_people = get_random_person()
    print('The opponent chose {}'.format(opponent_people['name']))

    my_stat = random_people[stat_choice]
    opponent_stat = opponent_people[stat_choice]

    # there are 'unknown' values in 'height' and 'mass' lists
    if my_stat == 'unknown' or opponent_stat == 'unknown':
        print("your choice: {} is {}, opponent's choice: {} is {}".format(stat_choice, my_stat, stat_choice,
                                                                          opponent_stat))
        print("Oops! Someone doesn't want to tell you the {}, please try again!".format(stat_choice))
        # not all the value are integer, so cannot use int()
    elif float(my_stat) > float(opponent_stat):
        print("your choice: {} is {}, opponent's choice: {} is {}".format(stat_choice, my_stat, stat_choice,
                                                                          opponent_stat))
        print('You Win!')
    elif float(my_stat) < float(opponent_stat):
        print("your choice: {} is {}, opponent's choice: {} is {}".format(stat_choice, my_stat, stat_choice,
                                                                          opponent_stat))
        print('You Lose!')
    else:
        print("your choice: {} is {}, opponent's choice: {} is {}".format(stat_choice, my_stat, stat_choice,
                                                                          opponent_stat))
        print('Draw!')

    try_again()

    return

# Run the whole game
run()

# The whole process:
# 1. The user given a random person
# 2. User selects 'height' or 'mass' as stat (if input other words, input again)
# 3. Another random person selected by computer as user's opponent
# 4. The stats for the two cards are compared
# 5. If there is 'unknown' value in either stat, show tips and ask the user to try again
# If there is not 'unknown' value, the user with the stat higher than the opponent wins'
# 6. Ask the user to try again by inputting 'y' or 'n' (if input other words, input again)
