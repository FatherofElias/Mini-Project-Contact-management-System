import re

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def validate_phone(phone):
    pattern = re.compile(r'^\+?1?\d{9,15}$')
    return pattern.match(phone)

def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return pattern.match(email)

def add_contact():
    identifier = input("Enter unique identifier (phone number or email): ")
    if identifier in contacts:
        print("Contact already exists.")
        return
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return
    email = input("Enter email address: ")
    if not validate_email(email):
        print("Invalid email address format.")
        return
    additional_info = input("Enter additional information (address, notes): ")
    contacts[identifier] = {
        "name": name,
        "phone": phone,
        "email": email,
        "additional_info": additional_info
    }
    print("Contact added successfully.")

def edit_contact():
    identifier = input("Enter unique identifier of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return
    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return
    email = input("Enter new email address: ")
    if not validate_email(email):
        print("Invalid email address format.")
        return
    additional_info = input("Enter new additional information (address, notes): ")
    contacts[identifier] = {
        "name": name,
        "phone": phone,
        "email": email,
        "additional_info": additional_info
    }
    print("Contact updated successfully.")

def delete_contact():
    identifier = input("Enter unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    identifier = input("Enter unique identifier of the contact to search: ")
    if identifier in contacts:
        print("Contact details:")
        for key, value in contacts[identifier].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for identifier, details in contacts.items():
        print(f"Identifier: {identifier}")
        for key, value in details.items():
            print(f"  {key}: {value}")

def export_contacts():
    filename = input("Enter filename to export contacts: ")
    with open(filename, 'w') as file:
        for identifier, details in contacts.items():
            file.write(f"{identifier}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    print("Contacts exported successfully.")

def import_contacts():
    filename = input("Enter filename to import contacts from: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            identifier = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if ':' not in line:
                    identifier = line
                    contacts[identifier] = {}
                else:
                    key, value = line.split(': ', 1)
                    contacts[identifier][key] = value
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()