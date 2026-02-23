import csv
import os

CSV_FILE = "contacts.csv"

# -------------------- FILE HANDLING --------------------

def load_contacts():
    contacts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    return contacts


def save_contacts(contacts):
    with open(CSV_FILE, "w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

# -------------------- CRUD OPERATIONS --------------------

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    contacts = load_contacts()

    for c in contacts:
        if c["phone"] == phone:
            print("❌ Contact with this phone number already exists.")
            return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully.")


def search_contact():
    search_phone = input("Enter phone number to search: ").strip()
    contacts = load_contacts()

    for c in contacts:
        if c["phone"] == search_phone:
            print("\nContact Found")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            return

    print("❌ Contact not found.")


def update_contact():
    phone = input("Enter phone number to update: ").strip()
    contacts = load_contacts()

    for c in contacts:
        if c["phone"] == phone:
            print("Leave blank to keep old value.")
            new_name = input(f"New name ({c['name']}): ").strip()
            new_email = input(f"New email ({c['email']}): ").strip()

            if new_name:
                c["name"] = new_name
            if new_email:
                c["email"] = new_email

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact():
    phone = input("Enter phone number to delete: ").strip()
    contacts = load_contacts()

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("❌ Contact not found.")

# -------------------- MAIN MENU --------------------

def main():
    while True:
        print("\n===== Contact Book Application =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Byee")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------- PROGRAM START --------------------

if __name__ == "__main__":
    main()
