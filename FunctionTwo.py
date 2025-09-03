import pandas as pd
from datetime import datetime

def record_activity():
    
    plant_df = pd.read_csv('plants.csv')

    name = input('What is the name of the plant you took care of? type [exit] to quit: ').strip()

    if name =="exit":
        print('\nReturning to the menu')
        return 

    elif name not in plant_df['plant_name/species'].values: 
        print('\nThis plant does not exist! Please check the name.')
        name = input('\nWhat is the name of the plant you took care of? type [exit] to quit: ').strip()


    
    all_activities = ["Watering", "Fertilizing", "Repotting", "Pruning"]
    activity = input('\n\nWhich activity have you performed? Choose from [Watering - Fertilizing - Repotting - Pruning]: ').strip()

    while activity not in all_activities:
        print("\nThis activity does not exist! Please choose again")
        activity = input('\n\nWhich activity have you performed? Choose from [Watering - Fertilizing - Repotting - Pruning]: ').strip()

    
    
    date_input= input('\n\nWhen did you perform this activity? Enter the date in this format (YY-MM-DD)').strip()  
    try:
        activity_date= datetime.strptime(date_input,'%y-%m-%d')
    except ValueError:
        print("Date format is invalid!")
        return

    
    
    rows = []
    with open('plants.csv', mode='r') as file:
        content = csv.DictReader(file)
        for plant in content:
            if plant['plant_name/species'].lower() == name.lower():
                plant["Activity"] = activity
                plant["Activity_Date"] = datetime.strptime(date_input,'%y-%m-%d')
            rows.append(plant)

    with open('plants.csv', mode='w', newline='') as file:
        writing = csv.DictWriter(file, fieldnames=rows[0].keys())
        writing.writeheader()
        writing.writerows(rows)

    
    print(f'\n\n{activity} was added for the plant {name} on the datee {activity_date} successfully.')

record_activity()
