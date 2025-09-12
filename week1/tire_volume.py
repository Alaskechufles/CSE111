"""I added the ability to record the customer number in the volumes.txt file if the user wants to purchase the tire"""
import math
import datetime

width = input("Enter the width of the tire in mm (ex 205): ")
aspect = input("Enter the aspect ratio of the tire (ex 60): ")
diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

width = float(width) 
aspect = float(aspect) 
diameter = float(diameter) 

volume = (math.pi * (width**2) * aspect * ((width*aspect)+(2540*diameter)))/10000000000

current_date_time = datetime.datetime.now()

print(f"The approximate volume is {volume:.2f} liters")

buy_decision = input(f"Do you want to buy this tire of width {width} mm, aspect ratio {aspect}, and diameter {diameter} inches? (yes/no): ")

if buy_decision.lower() == "yes":
    customer_number = input("Enter customer number: ")
    with open("week1/volumes.txt", "a") as volumes_file:
        print(f"{current_date_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {customer_number}", file=volumes_file)
else:
    with open("week1/volumes.txt", "a") as volumes_file:
        print(f"{current_date_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}", file=volumes_file)