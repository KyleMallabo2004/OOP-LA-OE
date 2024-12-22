class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"


def create_phone():
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    price = float(input("Enter the price: "))
    return Phone(brand, model, price)


def modify_phone(phone):
    print(f"Modifying phone: {phone}")
    phone.brand = input("Enter new brand: ")
    phone.model = input("Enter new model: ")
    phone.price = float(input("Enter new price: "))


def delete_phone_attribute(phone, attribute):
    if attribute == 'brand':
        phone.brand = None
    elif attribute == 'model':
        phone.model = None
    elif attribute == 'price':
        phone.price = None


def delete_phone(phones, phone_index):
    if 0 <= phone_index < len(phones):
        del phones[phone_index]


def display_phones(phones):
    if not phones:
        print("No phones in the list.")
    else:
        for i, phone in enumerate(phones):
            print(f"[{i}] {phone}")


def main_menu():
    phones = []

    while True:
        print("\n--- Phone Management System ---")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. Display Phones")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            phone = create_phone()
            phones.append(phone)
        elif choice == '2':
            display_phones(phones)
            phone_index = int(input("Enter phone index to modify: "))
            if 0 <= phone_index < len(phones):
                modify_phone(phones[phone_index])
        elif choice == '3':
            display_phones(phones)
            phone_index = int(input("Enter phone index to delete: "))
            delete_phone(phones, phone_index)
        elif choice == '4':
            display_phones(phones)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
