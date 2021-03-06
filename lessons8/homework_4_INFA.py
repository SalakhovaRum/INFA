import os
import requests 

result = requests.get("https://reqres.in/api/users?page-2").json()
dict_human = result ['data']
path = str(os.getcwd())+"users_data"
os.mkdir(path)

for i in range(0,len(dict_human)):
    number_folder = str(dict_human[i]['id'])
    os.mkdir(path + "/id" + number_folder)
    with open(path + "/id" + number_folder + "/user_info", "w") as file:
        for key in ["email", "first_name", "last_name"]:
            file.write(f'{dict_human[i][key]}\n')

    with open(path + "/id" + number_folder + "/avatar.jpg", "wb") as file:
        response = requests.get(dict_human[i]['avatar'])

        file.write(response.content)