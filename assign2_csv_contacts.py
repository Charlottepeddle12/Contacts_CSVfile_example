import csv


def menu():
    '''

    Returns nothing
    -------
    Prints the statements below

    '''
    print("list- List all contacts")
    print("view- View a contact")
    print("add- Add a contact")
    print("del- Delete a contact")
    print("exit- Exit program")
    
def command():
    '''

    Returns choice.lower() 
    -------
    TYPE: String
        DESCRIPTION: Asks the user for a command and returns it in lowercase

    '''
    choice = input("\nCommand: ")
    return choice.lower()

def list_contacts():
    '''

    Returns nothing
    -------
    Opens the CSV file using "contacts_csv_file" as a file handler name.
    it reads the contacts and specifically takes the name.
    each name is printed 
    number (presented next to the name) is added by 1

    '''
    number = 1
    with open("contacts.csv", "r", newline="") as contacts_csv_file:
        reader = csv.reader(contacts_csv_file)
        for name in reader:
            print("{}. {}".format(number, name[0]))
            number +=1
             
def view_contact():
    '''

    Returns nothing
    -------
    Asks the user for the numer of the contact they'd liek to view (number is then subtracted by 1)
    an empty list called 'data_list' is created to hold the data from the CSV file
    the fiel is opened and given "contents_csv_file" as a file handler.
    a for loop iterates though the file and appends it to the list
    using the index provided, the data is extracted from the list and printed
    

    '''
    index = int(input("Number: "))
    index -= 1
    data_list = []
    with open("contacts.csv", "r", newline="") as contacts_csv_file:
        reader = csv.reader(contacts_csv_file)
        for row in reader:
            data_list.append(row)
        name, email, number = data_list[index]
        print("Name: {}\nEmail: {}\nNumber: {}".format(name, email, number))
    
def add_contact():
    '''

    Returns nothing
    -------
    Asks for a name, email, and number.
    a list called "new_contact" is created and the data inputed by the user is put into the list
    the CSV file is opned under "contacts_csv_file" as file handler
    the new_contact list is added to the file
    a statement saying that the person was added is printed

    '''
    
    name = input("Name: ")
    email = input("Email: ")
    number = input("Number: ")
    new_contact = [name, email, number]
    with open("contacts.csv", "a", newline="") as contacts_csv_file:
        writer = csv.writer(contacts_csv_file)
        writer.writerow(new_contact)
    print("{} was added".format(name))

def delete_contact():
    '''
    Returns nothing
    -------
    An empty lsit called "contacts list' is created to hold the contacts
    the CSV file is opned and it's contents are appended to the contacts_list
    the user is asked for the index of the person they want to remove (which is them subtracted by 1)
    the contact is popped from the list and a print statement prints that the person was removed
    the CSV file is opned and the list is put back into the file

    '''
    
    contacts_list = []
    with open("contacts.csv", "r", newline="") as contacts_csv_file:
        reader = csv.reader(contacts_csv_file)
        for row in reader:
            contacts_list.append(row)
    index = int(input("Number: "))
    index -= 1
    print("{} was deleted".format(contacts_list[index][0]))
    contacts_list.pop(index)
    with open("contacts.csv", "w", newline="") as contacts_csv_file:
        writer = csv.writer(contacts_csv_file)
        writer.writerows(contacts_list)

#go controls the while loop. while go is "y", the loop will continue
go = "y"

print("Contact Manager\n")
menu()

while go == "y":
    
    #asks the user for a choice and stores it in the choice variable
    choice = command()

    if choice.lower() == "list":
        list_contacts()

    elif choice.lower() == "view":
        view_contact()
    
    elif choice.lower() == "add":
        add_contact()

    elif choice.lower() == "del":
        delete_contact()

#program exits if the user enters exit
    elif choice.lower() == "exit":
        break

#if something invalid is entered, it will print this statement
    else:
        print("Not a valid command. Try again")

#bye pritns after it ends
print("\nBye!")
