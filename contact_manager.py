import os

contacts = []

def add_contacts():
    name = input("Enter the contact's name: ")
   
    try:
       phone_number = input("Enter the phone number: ")
       int(phone_number)
    except ValueError:
        print("Invalid phone number.")
        input("Press Enter to continue...")
        return
    
    email_address = input("Enter the email address: ")
    
    contact = {
        "name": name,
        "phone": phone_number,
        "email": email_address
    }
    
    contacts.append(contact)
    save_contacts(contact)
    print(f'Contact "{name}" added.')
    input("Press Enter too continue...")
    
def clear_contacts():
    confirm = input("Are you sure you want to delete all contacts? (y/n): ").strip().lower()
    if confirm == "y":
        with open("contacts.txt", "w") as f:
            pass
        print("All contacts have been deleted.")
    else:
        print("Canceled.")
    
def save_contacts(contact):
    with open("contacts.txt", "a") as f:
        f.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def show_saved_contacts():
    if not os.path.exists("contacts.txt"):
        print("No contacts saved yet.")
        return
    with open("contacts.txt", "r") as f:
        print("Saved contacts and their info:")
        for line in f:
            name, phone, email = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
    
            
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Contacts")
    print("1. Add contacts")
    print("2. Show saved contacts")
    print("3. Clear all contacts")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contacts()
            
    elif choice == "2":
        show_saved_contacts()
        input("Press Enter to continue...")
        
    elif choice == "3":
        clear_contacts()
        input("Press Enter to continue...")
            
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        input("Press Enter to continue...")
