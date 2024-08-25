'''
an agenda with the following features
 - save tasks and events
 - has calculator +
 - daily record as a diary
 - can be locked with a password for safety
 - set up lists like to do or marketlist
 - works as a reminder
 - you can ceate an account or just use directly +
 project ID: time-manager-429407
'''

#Yapılanlar
'''
- Calculator
- Kişi Kayıt
- Etkinlik kaydetme
- Günlük
'''

'''
Yapılabilecek geliştirmeler
* Valid email check
* Send and verification email
'''
from datetime import datetime
import json
import os
import time 

current_date = datetime.now().strftime("%Y-%m-%d")
user = {}

def menu():
    while True:
        n = input("Please enter the number of the feature you want to use:\n1-Calculator\n2-Daily Track\n3-Diary\n4-Create list\n5-Close\n")
        if n == "1":
            calculator()
        elif n == "2":
            DailyTracker.main()
        elif n == "3":
            diary()
        elif n == "4":
            createlist.main()
        elif n == "5":
            break
        else:
            print("Please enter a number between 1-5.\n")
            return 
        
class firstep: 
    def newuser():
        user["name"] = input("Enter your name: ")
        user["email"] = input("Enter your email: ")
        user["password"] = input("Enter your password: ")
 
        return user

    def save_user(user, filename="users.json"):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                users = json.load(file)
        else:
            users = []
    
        users.append(user)
    
        with open(filename, 'w') as file:
            json.dump(users, file, indent=4)

    def main():
        user = firstep.newuser()
        firstep.save_user(user)
        print("Registiration completed succcesfully!")
        menu()

def registration():
    a = input("Welcome to Agenda!\n Create an account to track your actions.\n 1- Create an account\n 2- Continue without account\n")
    if a =="1":
        firstep.main()
    
    elif a == "2":
        menu()

    else:
        print("Please only enter 1 or 2 with numbers.")

def calculator():     
        while True:
            try:
                a = int(input("First number:\n"))
                operation = input("Operation (+, -, *, /,**):\n")
                b = int(input("Second number:\n"))

                if operation not in ['+', '-', '*', '/', '**']:
                    raise ValueError("Invalid operation")
            
                if operation == '+':
                    result = a + b
                elif operation == '-':
                    result = a - b
                elif operation == '*':
                    result = a * b
                elif operation == '/':
                    if b == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = a / b
                elif operation == '**':
                    result = a**b

                print(f"The result is: {result}")
                menu() 

            except ValueError as ve:
                print(f"Error: {ve}. Please enter valid numbers and operations.")
            except ZeroDivisionError as zde:
                print(f"Error: {zde}. Please enter a valid divisor.")
            except Exception as e:
                print(f"Unexpected error: {e}. Please try again.")

class DailyTracker:

    def __init__(self):
        self.activities = []

    def stopwatch(self): 
        input("Press Enter to start the timer")
        start_time = time.time()
        print("Timer started")

        input("Press Enter to stop the timer")
        end_time = time.time()
        print("Timer stopped.")

        elapsed_time = end_time - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        return f"Elapsed time: {int(hours):02}:{int(minutes):02}:{seconds:05.2f}"

    def new_activity(self):
        activity = {}
        activity["date"] = input("Enter the date: ")
        activity["activity"] = input("Enter the activity: ")
        activity["time spent"] = self.stopwatch()
        return activity

    def save_activity(self, activity, filename="my_activities.json"):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                my_activities = json.load(file)
        else:
            my_activities = []
    
        my_activities.append(activity)
    
        with open(filename, 'w') as file:
            json.dump(my_activities, file, indent=4)

    def main(self):
        activity = self.new_activity()
        self.save_activity(activity)
        print("Activity saved successfully!")

def diary():
    print (datetime.now().strftime("%Y-%m-%d"))
    d = input()
    with open('my_diary.txt', 'w') as file:
        file.write(f"{current_date}\n")
        file.write(f"{d}\n")

class createlist:
    def __init__(self):
        self.lists = []

    def new_list(self):
        mylist = {}
        mylist["name"] = input("Enter the name of the list: ")
        mylist["content"] = input("Enter list elements (separated by commas):\n").split(',')
        return mylist
    
    def save_list(self, mylist):
        filename = f"{mylist['name']}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.append(mylist)
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)

    def main(self):
        mylist = self.new_list()
        self.save_list(mylist)
        print("List created successfully!")


if __name__ == "__main__":
    registration()
