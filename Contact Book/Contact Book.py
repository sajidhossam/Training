import sys

contacts = []

def add_contact(name,phone):
    contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    print(f"Contact {name} Added succesfully")

def view_contact():
    if not contacts :
        print("you don't have any contacts")
        return
    print("Contact List")
    for i, contact in enumerate(contacts, start = 1):
        print(f"{i}. Name: {contact['name']}\n Phone: {contact['phone']}\n")

def delete_contact(name):

    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print(f"Contact '{name}' deleted successfully.")


def show_help():
    """Display help information."""
    print("Available commands:")
    print("  add <name> <phone> - Add a new contact")
    print("  view - View all contacts")
    print("  delete <name> - Delete a contact by name")
    print("  help - Show this help message")
    print("  quit - Exit the application")

def main():
    print("Welcome to contact manager")
    show_help()

    while True:
        command = input("\n Enter command: ").strip().split()

        if not command:
            continue
        
        cmd = command[0].lower()

        if cmd == "add" and  len(command) == 3:
            _, name, phone = command
            add_contact(name, phone)
        
        elif cmd == "view":
            view_contact()

        elif cmd == "delete" and len(command) == 2:
            _, name = command
            delete_contact(name)

        elif cmd == "help":
            show_help()

        elif cmd == "quit":
            print("Exiting the application")
            sys.exit()
        
        else:
            print("invalid command type 'help'  for more information")
if __name__ == "__main__":
    main()

