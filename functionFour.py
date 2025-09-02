## searching by name or location
def search():
    
    search_name = input("Enter the name of the plant or the location the plant is placed in: ")
        
    found = []
    with open(file_name, mode='r') as file:
        content = csv.DictReader(file)
        for plant in content:
            if plant["plant_name/species"] == search_name or plant["location in home"] == search_name:
                found.append(plant)
            else:
                print("No plants found!!")
                return main()
    if len(found) > 0:
        df = pd.DataFrame(found)
        print(df)

## showing all plants
def showAll():
    if os.path.exists(file_name):
        with open(file_name, mode='r') as file:
            content = csv.DictReader(file)
            df = pd.DataFrame(content)
            print(df)
    else:
        print("File does not exist")
        return