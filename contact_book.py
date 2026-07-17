contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[name] = [phone, email, address]
        print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details[0])
                print()

    elif choice == "3":
        search = input("Enter Name: ")

        if search in contacts:
            print("Name:", search)
            print("Phone:", contacts[search][0])
            print("Email:", contacts[search][1])
            print("Address:", contacts[search][2])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in contacts:
            phone = input("Enter New Phone: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")

            contacts[name] = [phone, email, address]
            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")