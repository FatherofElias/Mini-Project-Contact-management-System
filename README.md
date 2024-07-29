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