def main():
    name = input("Enter full name: ")
    city = input("Enter city: ")
    birth_year = int(input("Enter birth year: "))
    current_year = int(input("Enter current year: "))
    foods_raw = input("Enter favorite foods (comma-separated): ")

    age = current_year - birth_year

    foods_list = [food.strip() for food in foods_raw.split(',') if food.strip()]
    foods_set = set(foods_list)

    profile_dict = {
        'name': name,
        'city': city,
        'age': age,
        'foods': foods_list
    }
    
    summary_tuple = (name, age, city)

    print("--------------------")
    print(f"Name: {name}")
    print(f"City: {city}")
    print(f"Age: {age}")
    print(f"Foods (list): {foods_list}")
    print(f"Foods count: {len(foods_list)}")
    print(f"Unique foods: {len(foods_set)}")
    print(f"Profile (dict): {profile_dict}")
    print(f"Summary (tuple): {summary_tuple}")
    print("--------------------")

if __name__ == "__main__":
    main()