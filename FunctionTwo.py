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

    
    
    row= plant_df.loc[plant_df["plant_name/species"] == name].iloc[0]
    plant_id = row["id"]
    
    try:
        with open('care.csv', 'r', newline='') as file:
            pass
    except FileNotFoundError:
            with open('care.csv', 'w', newline='') as file:
                writing = csv.writer(file)
                writing.writerow(['plant_id','Activity','Activity_Date'])
    
    with open('care.csv', 'a', newline='') as file:
        writing = csv.writer(file)
        writing.writerow([plant_id, activity, activity_date])

    
    print(f'\n\n{activity} was added for the plant {name} on the datee {activity_date} successfully.')

record_activity()
