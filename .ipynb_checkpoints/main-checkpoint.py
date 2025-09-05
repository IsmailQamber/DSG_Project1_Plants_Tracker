
import pandas as pd
import uuid
from datetime import datetime, date, timedelta
import os
import csv 
file_name = "plants.csv"
## function 1 - yaqeen
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
        type_of_plant= input('Enter the type of your plant (cactus, fern, orchid, herb,Chrysanthemum, other )').strip().capitalize()
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
            writing.writerow([plant_id, plant_name, location_ ,
                               date_acquired, watering_frequency, sunlight_need , type_of_plant])
            print('\n\n new plants.csv is created')
    # growth tracking part 
    add_plant_growth(plant_name)
    # cheching for reminders:
    reminder()
    
##############################################

## function 2
def record_activity():
    plant_df = pd.read_csv('plants.csv')

    name = input('What is the name of the plant you took care of? type [exit] to quit: ').strip()

    if name.lower() == "exit":
        print('\nReturning to the menu')
        return 

    if name not in plant_df['plant_name/species'].values: 
        print('\nThis plant does not exist! Please check the name.')
        return  # exit if plant not found

    all_activities = ["Watering", "Fertilizing", "Repotting", "Pruning"]
    activity = input('\nWhich activity have you performed? Choose from [Watering - Fertilizing - Repotting - Pruning]: ').strip().capitalize()

    while activity not in all_activities:
        print("\nThis activity does not exist! Please choose again")
        activity = input('\nWhich activity have you performed? Choose from [Watering - Fertilizing - Repotting - Pruning]: ').strip().capitalize()

    # safer date handling
    date_input = input('\nWhen did you perform this activity? Enter the date in this format (YYYY-MM-DD): ').strip()  
    try:
        activity_date = datetime.strptime(date_input, '%Y-%m-%d').date()
    except ValueError:
        print("Date format is invalid!")
        return

    plant_id = plant_df.loc[plant_df["plant_name/species"] == name, "id"].values[0]

    # check if care.csv exists, if not create it
    if not os.path.exists('care.csv'):
        with open('care.csv', 'w', newline='') as file:
            writing = csv.writer(file)
            writing.writerow(['plant_id', 'Activity', 'Activity_Date'])

    # append new record
    with open('care.csv', 'a', newline='') as file:
        writing = csv.writer(file)
        writing.writerow([plant_id, activity, activity_date])

    print(f'\n{activity} was added for the plant {name} on the date {activity_date} successfully.')
###############################################      
def search_by_name(search_name):

    with open('plants.csv', mode='r') as file:
        content = csv.DictReader(file)
        for plant in content:
            print("name in db: ", plant["plant_name/species"].lower(), " , user name: ", search_name)
            if plant["plant_name/species"].lower() == search_name.lower():
                return plant["plant_name/species"]
        return None
    
##############################################
    
## function 3 - ali sameer
def plant_care():
    try:
        plants_DF = pd.read_csv('plants.csv')
        if not os.path.exists("care.csv"):
            print("No care records found yet. Please record some activities first.")
            return main()
            
        care_DF = pd.read_csv('care.csv')
        Vtoday = datetime.today().date()
        Vactivity_date = pd.to_datetime(care_DF["Activity_Date"]).dt.date

        for i , row in plants_DF.iterrows():
            Vplant_id = row['id']
            Vplant_name = row['plant_name/species']
            Vwatering_freq = row['watering_frequency_in_days']

            watered = care_DF[(care_DF["plant_id"] == Vplant_id ) & (care_DF["Activity"] == "Watering") & (care_DF["Activity_Date"] == Vtoday)]
            if care_DF.shape[0] < Vwatering_freq:
                print(f'Plant {Vplant_name} needs to be watered {Vwatering_freq - care_DF.shape[0]} more time')
    
    except FileNotFoundError:
        print('There is no recorrd for any plant, please add plants first')
        

##############################################

## function 4 - ismaeel Qamber

def plant_search():
    
    search_name = input("Enter the name of the plant or the location the plant is placed in: ")
        
    found = []
    with open(file_name, mode='r') as file:
        content = csv.DictReader(file)
        for plant in content:
            if plant["plant_name/species"] == search_name or plant["location in home"] == search_name:
                found.append(plant)
            else:
                print("No plants found!!")
                
    if len(found) > 0:
        df = pd.DataFrame(found)
        print(df)
        
## showing all plants
def plant_view():
    if os.path.exists(file_name):
        with open(file_name, mode='r') as file:
            content = csv.DictReader(file)
            df = pd.DataFrame(content)
            print(df)
    else:
        print("File does not exist")

# strech questions

# question 1 
# ali


def plant_growth():
    if not os.path.exists('growth.csv'):
        with open('growth.csv', 'w', newline='') as file:
            writing = csv.writer(file)
            writing.writerow(['id', 'growth', 'date'])
            
    while True:
        print("Select one of these: ")
        print("1. Add growth record to an existing plant")
        print("2. View growth record of an existing plant")
        print("3. Exit this function")
        
        userInput_raw = input("Your choice is: ")
        try:
            userInput = int(userInput_raw)
        except ValueError:
            print("Please enter a number (1–3)")
            continue
        
        if userInput == 1:
            plant_name = input("Enter the name of the plant: ")
            if search_by_name(plant_name) is not None:
                add_plant_growth(plant_name)
            else:
                print("Plant not found1.")

        elif userInput == 2:
            plant_name = input("Enter the name of the plant: ")
            plant_id = None
            record = []
            if search_by_name(plant_name) is not None:
                with open('plants.csv', mode='r') as file:
                    content = csv.DictReader(file)
                    for plant in content:
                        if plant["plant_name/species"] == plant_name:
                            plant_id = plant['id']

                with open('growth.csv', mode='r') as file:
                    content = csv.DictReader(file)
                    for plant in content:
                        if plant["id"] == plant_id:
                            record.append(plant)
                print(record)
            else:
                print("Plant not found2.")

        elif userInput == 3:
            return

        else:
            print("Invalid choice")


def add_plant_growth(name):
    if not os.path.exists('growth.csv'):
        with open('growth.csv', 'w', newline='') as file:
            writing = csv.writer(file)
            writing.writerow(['id', 'growth', 'date'])
    # find plant info 
    while True:
        height = input("Enter the current height of the plant(number): ")
        try:
            heightInt = int(height)
            break
        except ValueError:
            print("invalid height input, should be a number")
            
    id = None
    today_date = date.today()
    formatted_today_date =  today_date.strftime("%y-%m-%d").lstrip("0").replace("-0", "-")
    with open('plants.csv', mode='r') as file:
        content = csv.DictReader(file)
        for plant in content:
            if plant["plant_name/species"] == name:
              id = plant['id']
        
    
    with open('growth.csv', 'a', newline='') as file:
            writing =csv.writer(file)
            writing.writerow([id, heightInt, formatted_today_date])
            print("New plant grow record added!!")
    
    
    # try:
    #     plants_DF = pd.read_csv('plants.csv')
    #     if "Growth" not in plants_DF.columns:
    #         plants_DF['Growth'] = ""
    #         Aplant = input('Enter the plant name you would like to track its growth: ')
    #         for i , row in plants_DF.iterrows():
    #             if row['plant_name/species'] == Aplant:
    #                 Aplant_id = row['id']
    #                 try:
    #                     AGrowth = float(input('Enter the plant\'s height in cetimeter: '))
    #                     plants_DF.loc[i, "Growth"] = AGrowth
    #                     plants_DF.to_csv("plants.csv", index=False)
    #                     print('plant growth recorrded successfully')
    #                 except ValueError:
    #                     print('pleas enter a positve float number')
    #                     return
    #             else:
    #                 print('Plant does not exist')    except FileNotFoundError:
    #     print('There is no recorrd for any plant, please add plants first')
###########################################################################

# question 2
# yaqeen 
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
###########################################################################

#question 3 
# fatima
def add_image():
    
    #creating a new csv file for images
    try:
        with open("photo.csv","r",newline="") as file:
            reader = csv.DictReader(file)
    except FileNotFoundError:
        with open("photo.csv","w",newline="") as file:
            writing =csv.writer(file)
            writing.writerow(['plant_id', 'image_path', 'image_date'])
            print('\n\nnew photo.csv was created.')

    
    #asking the user for the name of the plant they wish to add an image for
    plant_df= pd.read_csv('plants.csv')
    
    plant_name= input("\n\nWhich plant do you wish to add a photo for? ")
    
    if plant_name not in plant_df['plant_name/species'].values: 
        print('\nThis plant does not exist! Please check the name.')
        plant_name= input("Which plant do you wish to add a photo for? ")

    
    #taking the id from the name provided by the user
    plant_id = plant_df.loc[plant_df["plant_name/species"] == plant_name, "id"].values[0]

    #asking the user for the image file path
    image_path= input("\n\nAdd a photo of your plant to document its progress: ")
    
    #the date of adding the image
    image_date=datetime.now().strftime('%y-%m-%d')
    
            
    with open("photo.csv","a",newline="") as file:
            writing =csv.writer(file)
            writing.writerow([ plant_id , image_path, image_date])
        
    print(f"\nA new photo for the plant '{plant_name}' was added successfully!")
###########################################################################

# question 4 
# ismail

# the function is dependant on the type of the plant -> a new column will be added to the plants row based on the type
def adjust_care():
    seasons = ["Winter", "Spring","Summer", "Autumn"]
    while True:
        current_season = input("Enter the current Season [Winter, Spring, Summer, Autumn]").strip().capitalize()
        if current_season in seasons:
            break
        else:
            print("Invalid Season input!!")
        
    care_adjustment = {
        
        "Cactus": 
        { "Winter": -1,
         "Summer": 1},

        "Fern": 
        { "Summer": 2,
          "Winter": 0},

        "Orchid": 
        { "Winter": 0,
          "Summer": 3},

        "Herb": 
        { "Summer": 2},

        "Chrysanthemum": 
        { "Autumn": 3}

    }

    adjusted = []
    with open("plants.csv", "r") as file:
        reader = csv.DictReader(file)  # skip header row
        for row in reader:
            plant_name = row['plant_name/species']
            plant_type = row['type_of_plant']
            watering_freq = int(row['watering frequency in days'])
            adjusted_watering = int(row['watering frequency in days']) + care_adjustment[plant_type][current_season]
        
            if plant_type in care_adjustment and current_season in care_adjustment[plant_type]:
                if watering_freq != adjusted_watering:
                    print(f"{plant_name}, of type: {plant_type} watering frequency changes from {watering_freq} to {adjusted_watering}")
    
###########################################################################

# question 5 
# yaqeen
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
        break

    # return results
    if len(results) > 0:
        print("Your plant is suffering from: ")
        for index, result in enumerate(results):
            print(f"{index + 1}. {result}")
        ## the printing can be modified to check if two symptoms have the same cause -> use dict, cause is the key and syptoms
    else:
        print("The symptoms entered are not registered in our system :)")
###########################################################################

def display_menue():
    print("***************************************")
    print('Plants tracker')
    print('1. Add a new plant to the collection')
    print('2. Record a plant care activity')
    print('3. view plants due for care')
    print('4. Search plants by name or location')
    print('5. view all plants')
    print('6. Plant diagnosis')
    print('7. Add image of your plant')
    print('8. Plant growth')
    print('9. Watering seasonal adjustment')
    print('0. Exit')
    return input('enter your choice(1,9): ')


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
            plant_care()
        elif choice =='4':
            plant_search()
        elif choice =='5':
            plant_view()
        elif choice == '6':
            diagnosis()
        elif choice == '7':
            add_image()
        elif choice == '8':
            plant_growth()
        elif choice == '9':
            adjust_care()
        elif choice =='0':
            print('Thank You!')
            break
        else:
            print('Enter a valid number between 1-9')


            