This is the full description of the contact management system and how it works and how to operate it!



Imports and Initialization :

import re: This imports the re module, which provides support for regular expressions.
contacts = {}: This initializes an empty dictionary to store contact information.

Display Menu : 

display_menu(): This function prints the menu options for the user to choose from.


Validating phone numbers : 

validate_phone(phone): This funtion uses Regex to validate phone numbers. The pattern allows for an optional + and 1 at the beginning, followed by 9 to 15 digits.

Validating email addresses : 

validate_email(email): This function uses a regular expression to validate email addresses. The pattern matches common email formats.


Adding a New Contact :

add_contact(): This function prompts the user to enter contact details and adds the contact to the 'contacts' dictionary

Edit Contact : 

edit_contact(): This function allows the user to edit an existing contact’s details.

Delete Contact : 

delete_contact(): This function deletes a contact based on the unique identifier provided by the user.


Search Contact : 

search_contact(): This function searches for a contact and displays its details.


Display All Contacts : 

display_all_contacts(): This function displays all contacts stored in the 'contacts' dictionary.


Export Contacts : 

export_contacts(): This function exports all contacts to a text file.


Import Contacts : 

import_contacts(): This function imports contacts from a text file.


Main Function : 

main(): This function displays the menu and handles user input to call the appropriate functions.


Entry Point : 

if __name__ == "__main__":
    main()

This ensures that the main function is called when the script is run directly





                            HOW TO USE
    When you run the script, the menu will be displayed.
Enter the number corresponding to the action you want to perform and press Enter.
For example, to add a new contact, enter 1.

If you choose to add a new contact, you will be prompted to enter the contact details:

The system will validate the phone number and email address formats. If they are valid, the contact will be added successfully.

To edit a contact, choose option 2 and enter the unique identifier of the contact you want to edit.
You will be prompted to enter the new details for the contact.

To delete a contact, choose option 3 and enter the unique identifier of the contact you want to delete.
The contact will be deleted if it exists.


To search for a contact, choose option 4 and enter the unique identifier of the contact you want to search for.
The contact details will be displayed if the contact is found.

To display all contacts, choose option 5.
All contacts in the system will be displayed.

To export contacts, choose option 6 and enter the filename where you want to save the contacts.
The contacts will be saved to the specified file.

To import contacts, choose option 7 and enter the filename from which you want to import the contacts.
The contacts will be imported from the specified file.


To quit the program, choose option 8.
The program will exit with a “Goodbye!” message.