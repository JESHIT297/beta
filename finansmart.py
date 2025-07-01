from random import randint

# Constants
INCOME_MIN = 1_000_000
INCOME_MAX = 8_000_000
NUMBER_CLIENTS = 5

# List to save clients
clients = []

for i in range(NUMBER_CLIENTS):
    print(f"\n=== Data entry for client {i+1} ===")

    full_name = input("Full name : ")
    id_number = input("ID number: ")
    age = int(input("Age: "))
    monthly_expenses =float(input("Monthly expenses: "))
    mobile_phone = input("Mobile phone: ")
    address = input("Address: ")
    client_status = True  # Default state

    monthly_income = randint(INCOME_MIN, INCOME_MAX)
    balance = monthly_income - monthly_expenses

    client = {
        "Full name": full_name,
        "ID number": id_number,
        "Age": age,
        "Monthly expenses":monthly_expenses,
        "Mobile phone": mobile_phone,
        "Address": address,
        "Client status": client_status,
        "Monthly income": monthly_income,
        "Balance": balance
    }

    # Add the client to the list
    clients.append(client)

# Show all clients
print("\n=== REPORT OF ALL CLIENTS ===")

for idx, client in enumerate(clients, start=1):
    print(f"\n--- client {idx} ---")
    print(f"Full name: {client['Full name']}")
    print(f"ID number: {client['ID number']}")
    print(f"Age: {client['Age']}")
    print(f"Monthly expenses: ${client['Monthly expenses']:,.0f}")
    print(f"Mobile phone: {client['Mobile phone']}")
    print(f"Address: {client['Address']}")
    print(f"Client status: {client['Client status']}")
    print(f"Monthly income: ${client['Monthly income']:,.0f}")
    print(f"Balance: ${client['Balance']:,.0f}")