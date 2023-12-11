# Listing pro skaters skill level, age and stance below
pro_skaters = {
    "Tony Hawk": {"skill_level": 95, "age": 53, "stance": "Regular"},
    "Nyjah Huston": {"skill_level": 98, "age": 27, "stance": "Goofy"},
    "Leticia Bufoni": {"skill_level": 92, "age": 29, "stance": "Regular"},
    "Ryan Sheckler": {"skill_level": 90, "age": 31, "stance": "Regular"},
    "Aori Nishimura": {"skill_level": 88, "age": 20, "stance": "Goofy"},
    "Yuto Horigome": {"skill_level": 89, "age": 24, "stance": "Goofy"},
    "Tyshawn Jones": {"skill_level": 93, "age": 24, "stance": "Regular"},
    "Mark Gonzales": {"skill_level": 90, "age": 55, "stance": "Regular"},
    "Gustavo Ribeiro": {"skill_level": 94, "age": 22, "stance": "Goofy"},
    "Lucas Rabelo": {"skill_level": 84, "age": 24, "stance": "Goofy"},
}

# Displaying all the possible options for the menu
def skater_menu():
    print("1. Add a skater")
    print("2. Update skater information")
    print("3. Delete a skater")
    print("4. Display skater information")
    print("5. Display all skaters")
    print("6. Exit")

# Function to add a new pro skater
def add_skater():
    name = input("Enter skater's name: ")
    skill_level = int(input("Enter skill level: "))
    age = int(input("Enter age: "))
    stance = input("Enter stance (Regular/Goofy): ").capitalize()

    pro_skaters[name] = {"skill_level": skill_level, "age": age, "stance": stance}
    print(f"{name} has been added to the pro skaters list.")

# Function to update skater information
def update_skater():
    name = input("Enter skater's name to update: ")
    if name in pro_skaters:
        print(f"Updating information for {name}:")
        skill_level = int(input("Enter new Skill level: "))
        age = int(input("Enter new age: "))
        stance = input("Enter new stance (Regular/Goofy): ").capitalize()

        pro_skaters[name] = {"skill_level": skill_level, "age": age, "stance": stance}
        print(f"{name}'s information has been updated.")
    else:
        print(f"{name} not found in the skaters list.")

# Function to delete a skater
def delete_skater():
    name = input("Enter skater's name to delete: ")
    if name in pro_skaters:
        del pro_skaters[name]
        print(f"{name} has been deleted from the skaters list.")
    else:
        print(f"{name} not found in the skaters list.")

# Function to display information for a specific skater
def display_skater():
    name = input("Enter skater's name to display: ")
    if name in pro_skaters:
        print(f"Skater Information for {name}:")
        skater_info = pro_skaters[name]
        for key, value in skater_info.items():
            print(f"{key}: {value}")
    else:
        print(f"{name} not found in the skaters list.")

# Function to display information for all skaters
def display_all_skaters():
    print("All Skaters:")
    print("{:<20} {:<15} {:<10} {:<10}".format("Name", "Skill Level", "Age", "Stance"))
    print("=" * 55)
    for name, info in pro_skaters.items():
        print("{:<20} {:<15} {:<10} {:<10}".format(name, info["skill_level"], info["age"], info["stance"]))

# Function to reset (delete) all skaters in the list
def reset_dictionary():
    pro_skaters.clear()
    print("All skaters have been removed from the list.")

# Function to load additional data into the skaters list
def load_data():
    new_data = {
        "New Skater": {"skill_level": 85, "age": 22, "stance": "Regular"},
        # Add more skaters as needed
    }
    pro_skaters.update(new_data)
    print("Data has been loaded into the skaters list.")

# Main function to manage the skater system
def skater_management():
    while True:
        skater_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_skater()
        elif choice == "2":
            update_skater()
        elif choice == "3":
            delete_skater()
        elif choice == "4":
            display_skater()
        elif choice == "5":
            display_all_skaters()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Entry point of the program
if __name__ == "__main__":
    skater_management()
