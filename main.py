import requests
from datetime import datetime
import os

current_date = datetime.now()
formatted_date = current_date.strftime("%d/%m/%y")
formatted_hour = current_date.strftime("%H:%M")

APP_ID = "3dcff444"
APP_KEY = "c3d5697a8a8801e28dbe7f41c3c7952c"
sheety_username = "d37a51f16f09413469f9f8d8075d6199"
sheety_project_name = "copyOfMyWorkouts"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}
exercise_parameters = {
    "query": input("What exercises did you do today: "),
    "gender": input("What is your gender: "),
    "weight_kg": input("Enter your weight in kg: "),
    "height_cm": input("Enter your height in cm: "),
    "age": input("Enter your age: "),
}
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=exercise_parameters)
data = response.json()

exercise_data_list = data["exercises"]
for i in range(len(exercise_data_list)):
    new_row_parameters = {
        "workout": {
            "date": formatted_date,
            "time": formatted_hour,
            "exercise": exercise_data_list[i]["name"].title(),
            "duration": exercise_data_list[i]["duration_min"],
            "calories": exercise_data_list[i]["nf_calories"],

        }
    }
    add_row_header = {
        "Authorization": "Bearer )(!@48085!*Msr",
    }
    requests.post(url="https://api.sheety.co/d37a51f16f09413469f9f8d8075d6199/copyOfMyWorkouts/workouts", json=new_row_parameters, headers=add_row_header)

print(data)
print(data['exercises'][0]['name'].title())


