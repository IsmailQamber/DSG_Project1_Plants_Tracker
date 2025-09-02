import csv 
import uuid
from datetime import datetime

def add_plant():

    try:
        with open('plants.csv', 'r',newline='') as file:
            reading=csv.DictReader(file)
            for row in reading:
                row['watering_frequency'] = int(row['watering_frequency'])
        print('\nplants.csv existis')

    except:
        with open('plants.csv', 'w',newline='') as file:
            writing=csv.writer(file)
            writing.writerow(['id','plant_name/species', 'location in home',
                            'date_acquired', 'watering frequency in days', 
                            'sunlight needs(low, medium, high)' ])
            print('\n\n new plants.csv is created')
    print('\n====Add a New Plant====')

    # unique id for the plant
    plant_id = str(uuid.uuid4())[:8]
    
    #getting the plant name
    plant_name=input('enter the plant name species ')

    #getting the plant location
    location_ = input('enter the location in home ')

    #getting the date acquired
    while True:
        date_acquired = input('enter date acquired (YY-M-D) ').strip()
        try:
            datetime.strptime(date_acquired, '%y-%m-%d')
            break
        except ValueError:
            print('invalid date format enter again ')

    
    #getting the watering frequency:
    while True: 
        watering_frequency=input('enter the watering frequency (in days) ').strip()
        if watering_frequency.isdigit() and int(watering_frequency) > 0:
            watering_frequency=int(watering_frequency)
            break
        else :
            print('please enter a valid number that is positive ')

    #getting sunlight 
    need_options=['Low','Medium','High']
    while True:
        sunlight_need= input('how much sunlight does the plant needs (Low, Medium, High) ').strip().capitalize()
        if sunlight_need in need_options:
            sunlight_need= sunlight_need.capitalize()
            break
        else:
            print('invalid. please enter from the options ')

    #saving the plants info:
    with open('plants.csv', 'a', newline='') as file:
        writing =csv.writer(file)
        writing.writerow([plant_id, plant_name, location_ ,
                           date_acquired, watering_frequency, sunlight_need ])
        
    print(f'the plant {plant_name} was added successfully')


