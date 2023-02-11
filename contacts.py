import pickle

class Contact:

    def __init__(self, firstName, secondName):
        self.firstName = firstName
        self.secondName = secondName
        self.phoneNumbers = []


class Controller:

    def __init__(self):
        self.contacts = []

    # Adding a contact
    def addContact(self, firstName, secondName):
        contact = Contact(firstName, secondName)
        self.contacts.append(contact)
        print(f"Added {firstName} {secondName} to the contact list")
        self.save()

    # Showing all contacts
    def showContacts(self):
        for contact in self.contacts:
            print(f"First Name: {contact.firstName}\nSecond Name: {contact.secondName}\nPhone Numbers:")
            for i, phoneNumber in enumerate(contact.phoneNumbers):
                print(f"\t{i+1}: {phoneNumber}")
            print()

    # Adding a phone number to the selected contact
    def addPhoneNumber(self, contact, phoneNumber):
        contact.phoneNumbers.append(phoneNumber)
        print(f"Added {phoneNumber} to the list of {contact.firstName} {contact.secondName}'s phone numbers")
        self.save()

    # Deleting a contact
    def deleteContact(self, contact):
        self.contacts.remove(contact)
        print(f"Deleted {contact.firstName} {contact.secondName} from the contact list")
        self.save()

    # Deleting a phone number from the selected contact
    def deletePhoneNumber(self, contact, phoneNumber):
        contact.phoneNumbers.remove(phoneNumber)
        print(f"Deleted {phoneNumber} from the list of {contact.firstName} {contact.secondName}'s phone numbers")
        self.save()

    # Saving data to binary file "data.dat"
    def save(self):
        f = open("data.dat", "wb")
        pickle.dump(self.contacts, f)
        f.close()




class App(Controller):

    def __init__(self):
        super().__init__()
        # Connecting to the binary file "data.dat", if it's not found - creating a new one
        try:
            f = open("data.dat", "rb")
            self.contacts = pickle.load(f)
            f.close()
        except:
            f = open("data.dat", "wb")
            pickle.dump([], f)
            f.close()

    # Menu that shows up when you start the app
    def menu(self):
        menu = "1 - Add a Contact, 2 - Show Contacts, 3 - Add a Phone Number, 4 - Delete a Contact, 5 - Delete a Phone Number, 6 - Exit"
        while True:
            print(menu)
            prompt = input(">> ")

            if prompt == "1":

                firstName = input("First Name: ")
                secondName = input("Second Name: ")
                self.addContact(firstName, secondName)

            elif prompt == "2":

                self.showContacts()

            elif prompt == "3":

                secondName = input("Second Name of the contact: ")
                contact = self.find(secondName)
                if contact:
                    phoneNumber = input("Phone Number: ")
                    self.addPhoneNumber(contact, phoneNumber)

            elif prompt == "4":

                secondName = input("Second Name of the contact: ")
                contact = self.find(secondName)
                if contact:
                    self.deleteContact(contact)

            elif prompt == "5":

                secondName = input("Second Name of the contact: ")
                contact = self.find(secondName)
                if contact:
                    for i, phoneNumber in enumerate(contact.phoneNumbers):
                        print(f"{i}: {phoneNumber}")

                    indeks = input("Index of the phone number: ")

                    try:
                        phoneNumber = contact.phoneNumbers[int(indeks)]
                        self.deletePhoneNumber(contact, phoneNumber)
                    except:
                        print("Invalid index")

            elif prompt == "6":
                break
            else:
                print("I don't understand")

    # Finding a contact in contacts by matching the secondName values
    def find(self, secondName):
        for contact in self.contacts:
            if contact.secondName == secondName:
                return contact
        print(f"Couldn't find a person named {secondName}")
        return 0



app = App()
app.menu()