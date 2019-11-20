import requests

url1 = 'http://hp-api.herokuapp.com/api/characters'
#view all characters
url2 = 'http://hp-api.herokuapp.com/api/characters/students'
#view all characters who are Hogwarts students during the book series
url3 = 'http://hp-api.herokuapp.com/api/characters/staff'
#view all characters who are Hogwarts staff during the book series
url4 = 'http://hp-api.herokuapp.com/api/characters/house/gryffindor'
#view all characters in a certain house, e.g. /slytherin

response = requests.get(url1)
All_characters = response.json()
response = requests.get(url2)
Hogwarts_students = response.json()
response = requests.get(url3)
Hogwarts_staff = response.json()
response = requests.get(url4)
All_characters_house = response.json()

length_dic = []
length_dic.append(len(All_characters))
length_dic.append(len(Hogwarts_students))
length_dic.append(len(Hogwarts_staff))
length_dic.append(len(All_characters_house))

All_characters[1]