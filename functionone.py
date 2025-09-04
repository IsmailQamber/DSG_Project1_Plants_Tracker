import csv 
import os
import uuid
from datetime import datetime

def add_plant():

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
        if watering_frequency.isdigit() and int(watering_frequency) > 0 and int(watering_frequency) < 4:
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

    #getting the type:
    type_options=['Cactus','Fern', 'Orchid', 'Herb', 'Chrysanthemum', 'Other' ]
    while True:
        type_of_plant= input('Enter the type of your plant ').strip().capitalize()
        if type_of_plant in type_options:
            type_of_plant= type_of_plant.capitalize()
            break
        else:
            print('invalid. enter again from the list provided')

    

    #saving the plants info:
    if os.path.exists('plants.csv'):
        with open('plants.csv', 'a', newline='') as file:
            writing =csv.writer(file)
            writing.writerow([plant_id, plant_name, location_ ,
                               date_acquired, watering_frequency, sunlight_need , type_of_plant])
    else:
        with open('plants.csv', 'w',newline='') as file:
            writing=csv.writer(file)
            writing.writerow(['id','plant_name/species', 'location in home',
                            'date_acquired', 'watering frequency in days',
                            'sunlight needs(low, medium, high)', 'type_of_plant' ])
            print('\n\n new plants.csv is created')

    # cheching for reminders:
    reminder()
       


def display_menue():
    print('Plants tracker')
    print('1. Add a new plant to the collection')
    print('2. Record a plant care activity')
    print('3. view plants due for care')
    print('4. Search plants by name or location')
    print('5. view all plants')
    print('6. Exit')
    return input('enter your choice(1,6): ')




def main():
    #the main function :
    print('this is Go Green!')
    print('this app helps you track and take care of your plnt')
    
    while True:
        choice= display_menue()
        
        if choice =='1':
            add_plant()
        elif choice =='2':
            record_activity()
        elif choice =='3':
            plants_care()
        elif choice =='4':
            plant_search()
        elif choice =='5':
            plant_view()
        elif choice =='6':
            print('Thank You!')
            break
        else:
            print('Eter a valid number between 1-6')
            
def diagnosis():

    #dictionary for the problems and a list of the symptoms for them 

    problems = {
        "underwatering": ["dry soil", "wilting", "crispy edges", "leaves curling"],
        "overwatering / Root Rot": ["yellow leaves", "wet soil", "mushy stem", "leaf drop"],
        "low humidity": ["brown tips", "crispy edges", "leaf curling"],
        "little light": ["leggy growth", "pale leaves", "slow growth"],
        "so Much Light": ["brown spots", "bleached patches", "crispy patches"],
        "Pests": ["sticky residue", "webbing", "tiny bugs", "deformed leaves"]
    }


    while True:
        try:
            user= input('enter the symptom and separate by a comma').lower().strip()
            if not user:
                print("No symptoms entered.") 
            
            # turning the input into a list
            symptoms = [s.strip() for s in user.split(",") if s.strip()]

        except ValueError :
            print("enter a valid input")
            continue
        

        #checking for matches, for each problem and its symptoms in the dictionary,
        # go to each symptom in the symptoms list created from the users input,
        # and check for matches in the problem_symptoms(the little list inside each problem in our dictionary)
        #if exists, append to to the matched []
        #if there are any symptoms matching. return the append the problem to  result []
        results = []
        for problem, problem_symptoms in problems.items():
            matched = []
            for s in symptoms:
                if s in problem_symptoms:
                    matched.append(s)

            if matched:  
                results.append(problem)

        # return results 
        return results
    


def reminder():
        # defining seasons by months
    season = ""
    month = datetime.today().month
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Autumn"

    
    '''care_rules = {
        "Cactus": "Needs less water in winter, careful not to overwater.",
        "Fern": "Needs more water and humidity in summer.",
        "Orchid": "Needs bright light in winter, careful of cold drafts.",
        "Herb": "Grows fast in summer, needs more trimming and water."
    }'''


    #rules for each type in each season
    care_rules = {
        
        "Cactus": 
        { "Winter": "Needs less water in winter, careful not to overwater.",
         "Summer": "Soil dries quickly; check sooner between waterings."},

        "Fern": 
        { "Summer": "Needs more water and humidity in summer.",
          "Winter": "Heaters dry air; keep soil evenly moist."},

        "Orchid": 
        { "Winter": "Needs bright light in winter, careful of cold drafts.",
          "Summer": "Protect from harsh sunlight; water more often."},

        "Herb": 
        { "Summer": "Grows fast in summer, needs more trimming and water."},

        "Chrysanthemum": 
        { "Autumn": "Mums bloom in fall; water regularly, deadhead spent flowers, and protect from frost."}

    }

    print(f"\n=== Seasonal Care Reminders for ({season}) :")
    found = False

    with open("plants.csv", "r") as file:
        reader = csv.DictReader(file)  # skip header row

        #looping over every row and getting the plant name and the type
        for row in reader:
            plant_name = row['plant_name/species']
            plant_type = row['type_of_plant']
        #check if the plant type from the row in the data existis in the dictionary, 
        # then check if the season is insied the little dictionary for this plant type
            if plant_type in care_rules and season in care_rules[plant_type]:
                print(f"- {plant_name} , ({plant_type}) : {care_rules[plant_type][season]}")
                found = True

    if not found:
        print("No seasonal care reminders for any plant in this season.")


add_plant()