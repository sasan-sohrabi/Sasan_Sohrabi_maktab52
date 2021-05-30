# Exercise 2

# import the relevant libraries
from Exercise_1 import *
import json


class Register:

    def __init__(self, first_name=None, last_name=None, email=None, phone=None, file_name=None) -> None:
        if not (first_name is None and last_name is None and email is None and phone is None):
            # print("You must Enter first name, last name, email and phone")
            assert name_validation(first_name), "First name pattern is incorrect!!! Ex.: Sasan or Sasan_Sa"
            self.first_name = first_name
            assert name_validation(last_name), "Last name pattern is incorrect!!! Ex.: Sohrabi or Sohra_bi"
            self.last_name = last_name
            assert email_validation(email), "Email pattern is incorrect!!! Ex.: name@mail.com"
            self.email = email
            assert phone_validation(phone), "Phone pattern is incorrect!!! Ex.: 09195145937 or +989195145937"
            self.phone = phone

    def __str__(self):
        return f"first_name: {self.first_name}" \
               f"last_name: {self.last_name}" \
               f"email: {self.email}" \
               f"phone: {self.phone}"

    def save_jason(self) -> None:
        with open('user_information.json', 'r') as json_file:
            user_information = json.load(json_file)

        with open('user_information.json', 'w') as json_file:
            user_information["users"].append({
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'phone': self.phone,
            })

            json.dump(user_information, json_file, indent=4)

    @staticmethod
    def register_json(file_name: str):
        with open(file_name) as json_file:
            user_information = json.load(json_file)
        users = []
        for user in user_information["users"]:
            users.append(Register(user["first_name"], user["last_name"], user["email"], user["phone"]))
        return users


# Example
# r1 = Register("Sasan", "Sohrabi", "Sasan.sp92@gmail.com", "+989195145937")
# r1.save_jason()
#
r2 = Register("Sasan", "Sohrabi", "Sasan.sp92@gmail.com", "+989195145937")
# r2.save_jason()
# r2 = Register("Alireza", "Sohrabi", "Sasan.sp92@gmail.com", "+989195145937")
for i in r2.register_json('user_information.json'):
    print(i)
